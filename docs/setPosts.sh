#!/usr/bin/env bash
set -euo pipefail

# Les fonctions communes
if [ -f .utils ]; then
  source .utils
else
  printf '[X] %s\n' "Error: .utils file is missing!" >&2; exit 1;
fi

# Ce fichier utilise le .json créé par getData.sh pour générer :
# * Un fichier markdown "Post" par DOI qui permettra de poster la référence sur le site

# Fichiers JSON source
BIBLIO_JSON="assets/data/biblio.json"
MAPPINGS_FILE="assets/data/author_mappings.json"

# Fichier DOI source
DOI_TXT="DOI.txt"

# Le répertoire authors
AUTHORS_DIR="authors"

# Mail, Scopus key and Springer key
if [ -f .env ]; then
  source .env
else
  die "Erreur : fichier .env introuvable !"
fi

# Nettoyer les anciens fichiers
rm -f "_posts"/*.md

# Assurer la présence du fichier JSON
if [ ! -f "$BIBLIO_JSON" ]; then
  die "Erreur : Fichier $BIBLIO_JSON introuvable !"
fi

# Chargement des DOI connus dans un tableau
log $(date -Iseconds)" Load known DOIs..."
mapfile -t known_dois < "$DOI_TXT"

# Chargement des noms de tous les permalink de biblio.json dans une table associative
log $(date -Iseconds)" Load DOI <-> permalink table..."
declare -A doi_keywords
valid_slugs=()
while IFS= read -r line; do
  key=$(read_json "$line" '.doi')
  value=$(read_json "$line" '.permalink // ""')
  valid_slugs+=("$value")
  doi_keywords["$key"]="$value"
done < <(jq -c '.[]' "$BIBLIO_JSON")

# Charger les correspondances "Prénom Nom" → "slug"
log $(date -Iseconds)" Load names -> slugs table..."
declare -A author_to_slug
while IFS= read -r entry; do
  slug=$(read_json "$entry" '.key')
  # Lire toutes les variations associées à ce slug
  while IFS= read -r variation; do
    author_to_slug["$variation"]="$slug"
  done < <(jq -r ".\"$slug\"[]" "$MAPPINGS_FILE")
done < <(jq -c 'to_entries[]' "$MAPPINGS_FILE")

# Format the authors
format_authors () {
  authors=""
  first=true
  while IFS= read -r author; do
    if [ "$first" = true ]; then
      first=false || :
    else
      authors+=", "
    fi
    if "$2"; then
      slug="${author_to_slug[$author]}"
      authors+="[$author]($AUTHORS_DIR/$slug)"
    else
      authors+="$author"
    fi
  done < <(echo "${1:-[]}" | jq -rc 'if type == "array" then .[] | select(.family) | "\(.given) \(.family)" else empty end')

  echo "$authors"
  return 0
}

# Identifie la catégorie du post
identify_category () {
  local type_ref="$1"
  local event="$2"
  # Proceedings
  if [ "$type_ref" = "proceedings-article" ]; then
    echo "proceedings"
    return 0
  fi
  if [ -n "$event" ]; then
    if echo $event | grep -q -e "Conference" -e "Workshop" -e "Symposium" -e "Congress" -e "Proceeding" -e "Consortium"; then
      echo "proceedings"
      return 0
    fi
  fi
  # Article
  if [ "$type_ref" = "journal-article" ]; then
    echo "articles"
    return 0
  fi
  # Chapter
  if [ "$type_ref" = "book-chapter" ]; then
    echo "chapters"
    return 0
  fi
  # Book
  if [ "$type_ref" = "book" ] || [ "$type_ref" = "monograph" ]; then
    echo "books"
    return 0
  fi
  
  die "Unknown category for $type_ref"
}

# Génération de fichiers Markdown pour chaque DOI (différencié selon le type, et avec cross-ref à l'intérieur du site)
create_markdown_post () {
  local data="$1"
  date=$(read_json "$data" ".dateY")-$(pad_zero $(read_json "$data" ".dateM"))-$(pad_zero $(read_json "$data" ".dateD"))
  permalink=$(read_json "$data" ".permalink")
  local output_md="_posts/$date-$permalink.md"
  local bibtex="assets/bib/$permalink.bib"

  log $(date -Iseconds)" Post under creation: $output_md"

  echo "---" > "$output_md"
  title=$(read_json "$data" ".title")
  title=$(mathjaxify "$title" | sed -e 's/\\/\\\\/g')
  echo "title: \"$title\"" >> "$output_md"
  echo "date: $date 00:00:00 +0100" >> "$output_md"
  echo "permalink: $permalink" >> "$output_md"
  echo "year: $(read_json "$data" ".year")" >> "$output_md"
  authors=$(read_json "$data" ".authors")
  echo "authors: $(format_authors "$authors" false)" >> "$output_md"
  type_ref=$(read_json "$data" ".type")
  event=$(read_json "$data" ".event")
  echo "category: $(identify_category "$type_ref" "$event")" >> "$output_md"
  keywords=$(read_json "$data" ".keywords")
  keywords=$(mathjaxify "$keywords")
  if [ -n "$keywords" ]; then
    echo "tags:" >> "$output_md"
    IFS=";" read -ra words <<< "$keywords"
    for word in "${words[@]}"; do
      echo "  - $(echo "$word" | sed 's/^ *//;s/ *$//')" >> "$output_md"
    done
  fi
  echo "---" >> "$output_md"
  echo " " >> "$output_md"

  echo "## Authors" >> "$output_md"
  echo "$(format_authors "$authors" true)" >> "$output_md"
  echo " " >> "$output_md"

  abstract=$(read_json "$data" ".abstract")
  echo "## Abstract" >> "$output_md"
  echo "$(mathjaxify "$abstract")" >> "$output_md"
  echo " " >> "$output_md"

  if [ -n "$keywords" ]; then
    echo "## Keywords" >> "$output_md"
    echo "$keywords" >> "$output_md"
    echo " " >> "$output_md"
  fi

  echo "## Citation" >> "$output_md"
  if echo $type_ref | grep -q "book\|monograph"; then
    echo "- **ISBN:** $(read_json "$data" ".isbn")" >> "$output_md"
  else
    echo "- **Journal:** $(read_json "$data" ".journal")" >> "$output_md"
    echo "- **Year:** $(read_json "$data" ".year")" >> "$output_md"
    echo "- **Volume:** $(read_json "$data" ".volume")" >> "$output_md"
    echo "- **Issue:** $(read_json "$data" ".issue")" >> "$output_md"
    echo "- **Pages:** $(read_json "$data" ".pages")" >> "$output_md"
  fi
  echo "- **Publisher:** $(read_json "$data" ".publisher")" >> "$output_md"
  doi=$(read_json "$data" ".doi")
  echo "- **DOI:** [$doi](https://doi.org/$doi)" >> "$output_md"
  if [ -n "$event" ]; then
      echo "- **Note:** $event" >> "$output_md"
  fi
  echo " " >> "$output_md"
  
  echo "## BibTeX" >> "$output_md"
  echo "{% highlight bibtex %}" >> "$output_md"
  echo "{% raw %}" >> "$output_md"
  if [ ! -f $bibtex ]; then
    print_bib "$doi" "$bibtex"
  fi
  cat "$bibtex" >> "$output_md"
  echo "{% endraw %}" >> "$output_md"
  echo "{% endhighlight %}" >> "$output_md"
  echo " " >> "$output_md"
  echo "[Download the bib file]({{ site.baseurl }}/$bibtex)" >> "$output_md"
  echo " " >> "$output_md"

  references=""
  references_json=$(echo "$data" | jq -c '.references' 2>/dev/null)
  while IFS= read -r ref; do
    title_ref=$(read_json "$ref" ".title")
    doi_ref=$(read_json "$ref" ".doi" | tr '[:upper:]' '[:lower:]')
    # Si on a un DOI (alors on a récupéré un titre), on formatte
    if [[ "$doi_ref" != "null" ]]; then
      # Si le DOI est connu, on lie avec la page correspondante
      if [[ " ${known_dois[@]} " =~ " $doi_ref " ]] && [ -n "${doi_keywords[$doi_ref]}" ]; then
        title_ref=$(echo "[$title_ref](${doi_keywords[$doi_ref]})")
      fi
      # On ajoute la réf
      references+="- $title_ref -- [$doi_ref](https://doi.org/$doi_ref)\\n"
    # Si on a seulement un titre
    else
      if [[ $title_ref != "" ]]; then
        references+=$(echo "- $title_ref\\n")
      fi
    fi
  done < <(echo "$references_json" | jq -c '.[]' 2>/dev/null)

  if [ -n "$references" ]; then
    echo "## References" >> "$output_md"
    echo -e "$references" >> "$output_md"
  fi
  return 0
}

# Puis, la génération des posts en markdown
    
log $(date -Iseconds)" Start creation!"
# Boucle à travers toutes les entrées du JSON et génère les posts
max_jobs=100
while IFS= read -r entry; do
  create_markdown_post "$entry" &
  # Throttle : on attend qu'au moins un job finisse si on atteint la limite
  while [ "$(jobs -rp | wc -l)" -ge "$max_jobs" ]; do
    wait -n
  done
done < <(jq -c '.[]' "$BIBLIO_JSON")
# S'assure que toutes les pages ont bien été créées avant de poursuivre
wait

# Enfin, on supprime les fichiers .bib orphelins s'il en existe
POST_DIR="_posts"
BIB_DIR="assets/bib"
TRASH_DIR="trash/"
mkdir -p "$TRASH_DIR"

log $(date -Iseconds)" Cleaning orphan bib files..."

# Pour chaque .bib dans assets/bib
find "$BIB_DIR" -name '*.bib' | while read -r bibfile; do
  bibname=$(basename "$bibfile" .bib)
  is_valid=false || :
  for slug in "${valid_slugs[@]}"; do
    if [[ "$bibname" == "$slug" ]]; then
      is_valid=true
      break
    fi
  done
  if ! $is_valid; then
    log " Deleting: $bibfile"
    mv "$bibfile" "$TRASH_DIR/$bibname.bib"
  fi
done

# Tout s'est bien passé !
echo "Posts generated!"
exit 0

