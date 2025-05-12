#!/bin/bash

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
    echo "Erreur : fichier .env introuvable !" >&2
    exit 1
fi

# Nettoyer les anciens fichiers
rm -f "_posts"/*.md

# Assurer la présence du fichier JSON
if [ ! -f "$BIBLIO_JSON" ]; then
    echo "Erreur : Fichier $BIBLIO_JSON introuvable !" >&2
    exit 1
fi

# Chargement des DOI connus dans un tableau
echo $(date -Iseconds)" Load known DOIs..."
mapfile -t known_dois < "$DOI_TXT"

# Chargement des noms de tous les permalink de biblio.json dans une table associative
echo $(date -Iseconds)" Load DOI <-> permalink table..."
declare -A doi_keywords
while IFS= read -r line; do
    key=$(echo "$line" | jq -r '.doi')
    value=$(echo "$line" | jq -r '.permalink // ""')
    doi_keywords["$key"]="$value"
done < <(jq -c '.[]' "$BIBLIO_JSON")

# Les fonctions communes
if [ -f .utils ]; then
    source .utils
else
    echo "Erreur : fichier .utils introuvable !" >&2
    exit 1
fi

# Ajoute un zéro si le mois ou le jour est entre 1 et 9
pad_zero () {
    printf "%02d" "$1"
}

# Charger les correspondances "Prénom Nom" → "slug"
echo $(date -Iseconds)" Load names -> slugs table..."
declare -A author_to_slug

while IFS= read -r entry; do
    slug=$(echo "$entry" | jq -r '.key')
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
            first=false
        else
            authors+=", "
        fi
        if $2; then
            slug="${author_to_slug[$author]}"
            authors+="[$author]($AUTHORS_DIR/$slug)"
        else
            authors+="$author"
        fi
    done < <(echo $1 | jq -rc '.[] | select(.family) | "\(.given) \(.family)"')
    echo "$authors"
}

# Identifie la catégorie du post
identify_category () {
    local type_ref=$1
    local event=$2
    # Proceedings
    if [ "$type_ref" = "proceedings-article" ]; then
        echo "proceedings"
        exit 0
    fi
    if [ -n "$event" ]; then
        if echo $event | grep -q -e "Conference" -e "Workshop" -e "Symposium" -e "Congress" -e "Proceeding" -e "Consortium"; then
            echo "proceedings"
            exit 0
        fi
    fi
    # Article
    if [ "$type_ref" = "journal-article" ]; then
        echo "articles"
        exit 0
    fi
    # Chapter
    if [ "$type_ref" = "book-chapter" ]; then
        echo "chapters"
        exit 0
    fi
    # Book
    if [ "$type_ref" = "book" ] || [ "$type_ref" = "monograph" ]; then
        echo "books"
        exit 0
    fi
    
    echo "unknown"
}

# Génération de fichiers Markdown pour chaque DOI (différencié selon le type, et avec cross-ref à l'intérieur du site)
create_markdown_post () {
    local data=$1
    date=$(echo "$data" | jq -r .dateY)-$(pad_zero $(echo "$data" | jq -r .dateM))-$(pad_zero $(echo "$data" | jq -r .dateD))
    permalink=$(echo "$data" | jq -r .permalink)
    local output_md="_posts/$date-$permalink.md"
    local bibtex="assets/bib/$permalink.bib"

    echo $(date -Iseconds)" Post under creation: $output_md"

    echo "---" > "$output_md"
    echo "layout: post" >> "$output_md"
    title=$(echo "$data" | jq -r .title)
    title=$(mathjaxify "$title" | sed -e 's/\\/\\\\/g')
    echo "title: \"$title\"" >> "$output_md"
    echo "date: $date 00:00:00 +0100" >> "$output_md"
    echo "permalink: $permalink" >> "$output_md"
    echo "year: $(echo "$data" | jq -r .year)" >> "$output_md"
    authors=$(echo "$data" | jq -r .authors 2>/dev/null)
    echo "authors: $(format_authors "$authors" false)" >> "$output_md"
    type_ref=$(echo "$data" | jq -r .type)
    event=$(echo "$data" | jq -r .event)
    echo "category: $(identify_category "$type_ref" "$event")" >> "$output_md"
    keywords=$(echo "$data" | jq -r .keywords)
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

    abstract=$(echo "$data" | jq -r .abstract)
    if [ "$abstract" != "No abstract available" ]; then
        echo "## Abstract" >> "$output_md"
        echo "$(mathjaxify "$abstract")" >> "$output_md"
        echo " " >> "$output_md"
    fi

    if [ -n "$keywords" ]; then
        echo "## Keywords" >> "$output_md"
        echo "$keywords" >> "$output_md"
        echo " " >> "$output_md"
    fi

    echo "## Citation" >> "$output_md"
    if echo $type_ref | grep -q "book\|monograph"; then
        echo "- **ISBN:** $(echo "$data" | jq -r .isbn)" >> "$output_md"
    else
        echo "- **Journal:** $(echo "$data" | jq -r .journal)" >> "$output_md"
        echo "- **Year:** $(echo "$data" | jq -r .year)" >> "$output_md"
        echo "- **Volume:** $(echo "$data" | jq -r .volume)" >> "$output_md"
        echo "- **Issue:** $(echo "$data" | jq -r .issue)" >> "$output_md"
        echo "- **Pages:** $(echo "$data" | jq -r .pages)" >> "$output_md"
    fi
    echo "- **Publisher:** $(echo "$data" | jq -r .publisher)" >> "$output_md"
    doi=$(echo "$data" | jq -r .doi)
    echo "- **DOI:** [$doi](https://doi.org/$doi)" >> "$output_md"
    if [ -n "$event" ]; then
        echo "- **Note:** $event" >> "$output_md"
    fi
    echo " " >> "$output_md"
    
    echo "## BibTeX" >> "$output_md"
    echo "{% highlight bibtex %}" >> "$output_md"
    echo "{% raw %}" >> "$output_md"
    cat "$bibtex" >> "$output_md"
    echo "{% endraw %}" >> "$output_md"
    echo "{% endhighlight %}" >> "$output_md"
    echo " " >> "$output_md"
    echo "[Download the bib file]({{ site.baseurl }}/$bibtex)" >> "$output_md"
    echo " " >> "$output_md"

    references=""
    references_json=$(echo "$data" | jq -c '.references' 2>/dev/null)
    while IFS= read -r ref; do
        title_ref=$(echo "$ref" | jq -r .title 2>/dev/null)
        doi_ref=$(echo "$ref" | jq -r .doi 2>/dev/null | tr '[:upper:]' '[:lower:]')
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
}

# Puis, la génération des posts en markdown
    
echo $(date -Iseconds)" Start creation !"
# Boucle à travers toutes les entrées du JSON et génère les posts
jq -c '.[]' "$BIBLIO_JSON" | while IFS= read -r entry; do
    create_markdown_post "$entry" &
    # Parallèlisé jusqu'à 16 processus
    [ $( jobs | wc -l ) -ge 16 ] && wait
done

# Tout s'est bien passé !
echo "Posts generated!"
exit 0

