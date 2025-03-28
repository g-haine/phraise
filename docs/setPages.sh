#!/bin/bash

# Ce fichier utilise le .json créé par getData.sh et le .json de author_mapping.shen pour générer :
# * Un fichier markdown "Page" par auteur et par année, aves les index associés

# Force UTF-8
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export LANGUAGE=C.UTF-8

# Dossiers de sortie
AUTHORS_DIR="authors"
YEARS_DIR="years"
MAPPINGS_FILE="assets/data/author_mappings.json"

# S'assurer que les dossiers existent
mkdir -p "$AUTHORS_DIR" "$YEARS_DIR"

# Fichier JSON source
BIBLIO_JSON="assets/data/biblio.json"

# Nettoyer les anciens fichiers
rm -f "$AUTHORS_DIR"/*.md "$YEARS_DIR"/*.md
touch "$AUTHORS_DIR/index.md"
touch "$YEARS_DIR/index.md"
iconv -f UTF-8 -t UTF-8 "$AUTHORS_DIR/index.md" -o "$AUTHORS_DIR/index.md"
iconv -f UTF-8 -t UTF-8 "$YEARS_DIR/index.md" -o "$YEARS_DIR/index.md"

# Vérifier la présence des fichiers JSON
if [[ ! -f "$BIBLIO_JSON" || ! -f "$MAPPINGS_FILE" ]]; then
    echo "Erreur : Fichier(s) JSON manquant(s) !" >&2
    exit 1
fi

# Fonction pour slugifier un texte
slugify() {
    echo "$1" | iconv -t ascii//TRANSLIT | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed -E 's/^-+|-+$//g'
}

# Remplace les $ par les balises markdwon de mathjax dans les titre
mathjaxify () {
    title=$(echo "$1" | sed -e 's/$$/$/g') # au cas où il y aurait des double $
    title=$(echo "$title" | sed -e 's/{{/{[[:space:]]{/g') # Pour éviter les conflits avec jekyll
    title=$(echo "$title" | sed -e 's/}}/}[[:space:]]}/g') # Pour éviter les conflits avec jekyll
    # Mathjax \( ... \) avec les escape nécessaires
    title=$(echo "$title" \
    | awk '{
        in_math = 0;
        for (i=1; i<=length($0); i++) {
            c = substr($0, i, 1);
            if (c == "$") {
                if (in_math == 0) {
                    printf "\\( ";
                    in_math = 1;
                } else {
                    printf " \\)";
                    in_math = 0;
                }
            } else {
                printf "%s", c;
            }
        }
        printf "\n";
    }')
    
    echo "$title"
}

# Charger les correspondances "Prénom Nom" → "slug"
echo $(date -Iseconds)" Load names <-> slugs tables..."
declare -A author_to_slug
declare -A slug_to_name

while IFS= read -r entry; do
    slug=$(echo "$entry" | jq -r '.key')
    slug_to_name["$slug"]=$(echo "$entry" | jq -r '.value[0]' | iconv -c -f UTF-8 -t UTF-8)
    
    # Lire toutes les variations associées à ce slug
    while IFS= read -r variation; do
        author_to_slug["$variation"]="$slug"
    done < <(jq -r ".\"$slug\"[]" "$MAPPINGS_FILE")
done < <(jq -c 'to_entries[]' "$MAPPINGS_FILE")

# Extraction des auteurs et des années
echo $(date -Iseconds)" Load names and years from .json..."
declare -A authors
declare -A years

while read -r entry; do
    permalink=$(echo "$entry" | jq -r '.permalink')
    title=$(echo "$entry" | jq -r '.title')
    year=$(echo "$entry" | jq -r '.year')
    author_names=$(echo "$entry" | jq -r '[.authors[] | select(.family) | "\(.given) \(.family)"] | join(", ")' | iconv -c -f UTF-8 -t UTF-8)

    if [[ -z "$author_names" ]]; then
        echo "Erreur : Auteurs vides pour $title" >&2
        continue
    fi

    # Lire chaque "Prénom Nom" sans découper sur les espaces
    while IFS= read -d ", " -r author; do
        author=$(echo "$author" | sed 's/^ *//;s/ *$//') # Supprimer espaces inutiles
        slug="${author_to_slug[$author]}"
        standardized_author="${slug_to_name[$slug]:-$author}"
        sanitized_author=$(slugify "$standardized_author")
        authors["$standardized_author"]+="
        $year|<li><span class='post-meta'>$year -- $author_names</span><h3><a class='post-link' href=\"{{ site.baseurl }}/$permalink\">$(mathjaxify "$title")</a></h3></li>"
    done <<< "$author_names, "

    years["$year"]+='
  <li>
    <span class="post-meta">'$year' -- '$author_names'</span>
    <h3><a class="post-link" href="{{ site.baseurl }}/'$permalink'">'$(mathjaxify "$title")'</a></h3>
  </li>'

done < <(jq -c '.[]' "$BIBLIO_JSON")

# Créer un tableau temporaire pour le tri des auteurs
echo $(date -Iseconds)" Sorting authors..."
sorted_pairs=()
for author in "${!authors[@]}"; do
    last_name=$(echo "$author" | awk '{print $NF}')  # Extraire le dernier mot
    
    # Normaliser le dernier mot en ASCII
    normalized_last_name=$(echo "$last_name" | iconv -f UTF-8 -t ASCII//TRANSLIT | sed -E "
        s/d'//;
        s/Ü/U/;
        s/Ç/C/;
        s/Š/S/;
        s/Ž/Z/;
        s/Ð/D/;
        s/Ñ/N/;
        s/Ł/L/;
        s/Ø/O/;
        s/Æ/A/;
        s/Œ/OE/")
    
    sorted_pairs+=("$normalized_last_name	$author")  # Tabulation pour séparer proprement
done

# Trier les auteurs par leur dernier mot
IFS=$'\n' sorted_pairs=($(sort -k1 <<<"${sorted_pairs[*]}"))
unset IFS

# Générer l'index des auteurs avec sous-titres alphabétiques et affichage en 3 colonnes
echo $(date -Iseconds)" Page $AUTHORS_DIR/index.md creation..."
cat <<EOF > "$AUTHORS_DIR/index.md"
---
layout: page
title: Authors
permalink: /authors/
---

EOF

letter=""
echo "<div class='grid'>" >> "$AUTHORS_DIR/index.md"

for pair in "${sorted_pairs[@]}"; do
    last_name=$(echo "$pair" | cut -f1)  
    author=$(echo "$pair" | cut -f2-)  
    
    # Extraire la première lettre après normalisation
    first_letter=$(echo "$last_name" | cut -c1 | tr '[:lower:]' '[:upper:]')

    # Vérifier si on doit insérer un sous-titre alphabétique
    if [[ "$first_letter" != "$letter" ]]; then
        echo "</div>" >> "$AUTHORS_DIR/index.md"
        echo "## $first_letter" >> "$AUTHORS_DIR/index.md"
        echo "<div class='grid'>" >> "$AUTHORS_DIR/index.md"
        letter="$first_letter"
    fi

    slug="${author_to_slug[$author]}"
    sanitized_slug=$(slugify "$slug")

    echo "<a href='{{ site.baseurl }}/$AUTHORS_DIR/$sanitized_slug'>$author</a>" | iconv -t UTF-8 >> "$AUTHORS_DIR/index.md"
    
    echo $(date -Iseconds)" Page $AUTHORS_DIR/$sanitized_slug.md creation..."
    cat <<EOF > "$AUTHORS_DIR/$sanitized_slug.md"
---
layout: page
title: Publications by $author
permalink: /authors/$sanitized_slug
---

EOF
    echo '<ul class="post-list">' >> "$AUTHORS_DIR/$sanitized_slug.md"
    echo -e "${authors[$author]}" | sort -t'|' -k1,1r | cut -d'|' -f2 | iconv -t UTF-8 >> "$AUTHORS_DIR/$sanitized_slug.md"
    echo "</ul>" >> "$AUTHORS_DIR/$sanitized_slug.md"
done

echo "</div>" >> "$AUTHORS_DIR/index.md"

# Trier les années avant de les afficher dans l'index
echo $(date -Iseconds)" Sorting years..."
IFS=$'\n' sorted_years=($(sort -n <<<"${!years[*]}"))
unset IFS

# Générer l'index des années avec affichage en 3 colonnes et tri correct
echo $(date -Iseconds)" Page $YEARS_DIR/index.md creation..."
cat <<EOF > "$YEARS_DIR/index.md"
---
layout: page
title: Years
permalink: /years/
---

<div class="grid">
EOF

for year in "${sorted_years[@]}"; do
    echo "<a href='{{ site.baseurl }}/$YEARS_DIR/$year'>$year</a>" >> "$YEARS_DIR/index.md"
done

echo "</div>" >> "$YEARS_DIR/index.md"

# Générer les fichiers correspondants
for year in "${sorted_years[@]}"; do
    echo $(date -Iseconds)" Page $YEARS_DIR/$year.md creation..."
    cat <<EOF > "$YEARS_DIR/$year.md"
---
layout: page
title: Published in $year
permalink: /years/$year
---

EOF
    echo '<ul class="post-list">' >> "$YEARS_DIR/$year.md"
    echo -e "${years[$year]}" >> "$YEARS_DIR/$year.md"
    echo "</ul>" >> "$YEARS_DIR/$year.md"
done

echo "Pages generated!"
exit 0

