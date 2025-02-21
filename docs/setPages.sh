#!/bin/bash

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

# Vérifier la présence des fichiers JSON
if [[ ! -f "$BIBLIO_JSON" || ! -f "$MAPPINGS_FILE" ]]; then
    echo "Erreur : Fichier(s) JSON manquant(s) !" >&2
    exit 1
fi

# Fonction pour slugifier un texte
slugify() {
    echo "$1" | iconv -t ascii//TRANSLIT | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed -E 's/^-+|-+$//g'
}

# Charger les correspondances "Prénom Nom" → "slug"
declare -A author_to_slug
declare -A slug_to_name

while IFS= read -r entry; do
    slug=$(echo "$entry" | jq -r '.key')
    slug_to_name["$slug"]=$(echo "$entry" | jq -r '.value[0]')
    
    # Lire toutes les variations associées à ce slug
    while IFS= read -r variation; do
        author_to_slug["$variation"]="$slug"
    done < <(jq -r ".\"$slug\"[]" "$MAPPINGS_FILE")
done < <(jq -c 'to_entries[]' "$MAPPINGS_FILE")

# Extraction des auteurs et des années
declare -A authors
declare -A years

while read -r entry; do
    permalink=$(echo "$entry" | jq -r '.permalink')
    title=$(echo "$entry" | jq -r '.title')
    year=$(echo "$entry" | jq -r '.year')
    author_names=$(echo "$entry" | jq -r '[.authors[] | select(.family) | "\(.given) \(.family)"] | join(";")')

    if [[ -z "$author_names" ]]; then
        echo "Erreur : Auteurs vides pour $title" >&2
        continue
    fi

    # Lire chaque "Prénom Nom" sans découper sur les espaces
    while IFS= read -d ";" -r author; do
        author=$(echo "$author" | sed 's/^ *//;s/ *$//') # Supprimer espaces inutiles
        slug="${author_to_slug[$author]}"
        standardized_author="${slug_to_name[$slug]:-$author}"
        sanitized_author=$(slugify "$standardized_author")
        authors["$standardized_author"]+="- [$title](../../$permalink)\\n"
    done <<< "$author_names;"

    years["$year"]+="- [$title](../../$permalink)\\n"

done < <(jq -c '.[]' "$BIBLIO_JSON")

# Créer un tableau temporaire pour le tri des auteurs
sorted_pairs=()
for author in "${!authors[@]}"; do
    last_word=$(echo "$author" | awk '{print $NF}')  # Extraire le dernier mot
    sorted_pairs+=("$last_word	$author")  # Tabulation pour séparer proprement
done

# Trier les auteurs par leur dernier mot
IFS=$'\n' sorted_pairs=($(sort -k1 <<<"${sorted_pairs[*]}"))
unset IFS

# Générer l'index des auteurs avec sous-titres alphabétiques et affichage en 3 colonnes
cat <<EOF > "$AUTHORS_DIR/index.md"
---
layout: page
title: Browse by authors
permalink: /authors/
---

EOF

letter=""
echo "<div class='grid'>" >> "$AUTHORS_DIR/index.md"

for pair in "${sorted_pairs[@]}"; do
    last_name=$(echo "$pair" | cut -f1)  
    author=$(echo "$pair" | cut -f2-)  

    first_letter=$(echo "$last_name" | cut -c1 | tr '[:lower:]' '[:upper:]')

    if [[ "$first_letter" != "$letter" ]]; then
        echo "</div>" >> "$AUTHORS_DIR/index.md"
        echo "## $first_letter" >> "$AUTHORS_DIR/index.md"
        echo "<div class='grid'>" >> "$AUTHORS_DIR/index.md"
        letter="$first_letter"
    fi

    slug="${author_to_slug[$author]}"
    sanitized_slug=$(slugify "$slug")

    echo "<a href='./$sanitized_slug/'>$author</a>" >> "$AUTHORS_DIR/index.md"

    cat <<EOF > "$AUTHORS_DIR/$sanitized_slug.md"
---
layout: page
title: Publications by $author
permalink: /authors/$sanitized_slug/
---

EOF
    echo -e "${authors[$author]}" >> "$AUTHORS_DIR/$sanitized_slug.md"
done

echo "</div>" >> "$AUTHORS_DIR/index.md"

# Trier les années avant de les afficher dans l'index
IFS=$'\n' sorted_years=($(sort -n <<<"${!years[*]}"))
unset IFS

# Générer l'index des années avec affichage en 3 colonnes et tri correct
cat <<EOF > "$YEARS_DIR/index.md"
---
layout: page
title: Browse by years
permalink: /years/
---

<div class="grid">
EOF

for year in "${sorted_years[@]}"; do
    echo "<a href='{{ site.baseurl }}/years/$year/'>$year</a>" >> "$YEARS_DIR/index.md"
done

echo "</div>" >> "$YEARS_DIR/index.md"

# Générer les fichiers correspondants
for year in "${sorted_years[@]}"; do
    cat <<EOF > "$YEARS_DIR/$year.md"
---
layout: page
title: Published in $year
permalink: /years/$year/
---

EOF
    echo -e "${years[$year]}" >> "$YEARS_DIR/$year.md"
done

echo "Pages des auteurs et années générées avec succès !"
exit 0

