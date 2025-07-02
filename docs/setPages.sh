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

# Les fonctions communes
if [ -f .utils ]; then
    source .utils
else
    echo "Erreur : fichier .utils introuvable !" >&2
    exit 1
fi

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
    dateY=$(echo "$entry" | jq -r '.dateY')
    dateM=$(echo "$entry" | jq -r '.dateM')
    dateD=$(echo "$entry" | jq -r '.dateD')
    date=$dateY"-"$(pad_zero "$dateM")"-"$(pad_zero "$dateD")
    author_names=$(echo "$entry" | jq -r '
      if (.authors // null) == null then
        "No author"
      else
        [.authors[] | select(.family) | "\(.given) \(.family)"] | join(", ")
      end' | iconv -c -f UTF-8 -t UTF-8)

    if [[ "$author_names" == "No author" ]]; then
        continue
    fi

    POST="
    $date|<li><span class='post-meta'>$year -- $author_names</span><h3><a class='post-link' href=\"{{ site.baseurl }}/$permalink\">$(mathjaxify "$title")</a></h3></li>"

    # Lire chaque "Prénom Nom" pour y ajouter le post
    while IFS= read -d ", " -r author; do
        author=$(echo "$author" | sed 's/^ *//;s/ *$//')
        if [[ $author != "" ]]; then
            slug="${author_to_slug[$author]}"
            if [[ $slug == "" ]]; then
                continue
            fi
            standardized_author="${slug_to_name[$slug]:-$author}"
            sanitized_author=$(slugify "$standardized_author")
            authors["$standardized_author"]+=$POST
        fi
    done <<< "$author_names, "
    # Ajoute le post à son année
    years["$year"]+=$POST
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

echo "<h3>There are ${#authors[@]} authors referenced.</h3>" >> "$AUTHORS_DIR/index.md"

echo "<p id='info-authors'>For <a href='{{ site.baseurl }}/about/#handling-authors-names'>simplicity</a>, the authors are sorted using the last word of their name.<br />For example, <i>Arjan van der Schaft</i> appears under the letter <strong>S</strong>, and <i>Yann Le Gorrec</i> under the letter <strong>G</strong>.</p>" >> "$AUTHORS_DIR/index.md"

echo "<p>You may want to look at <a href='{{ site.baseurl }}/assets/data/author_mappings.json'>the array managing name variations</a> (a JSON file) for verification/correction.</p>" >> "$AUTHORS_DIR/index.md"

echo "<hr />" >> "$AUTHORS_DIR/index.md"

echo "<p id='links-letters'><a href='#a'>A</a> - <a href='#b'>B</a> - <a href='#c'>C</a> - <a href='#d'>D</a> - <a href='#e'>E</a> - <a href='#f'>F</a> - <a href='#g'>G</a> - <a href='#h'>H</a> - <a href='#i'>I</a> - <a href='#j'>J</a> - <a href='#k'>K</a> - <a href='#l'>L</a> - <a href='#m'>M</a> - <a href='#n'>N</a> - <a href='#o'>O</a> - <a href='#p'>P</a> - <a href='#q'>Q</a> - <a href='#r'>R</a> - <a href='#s'>S</a> - <a href='#t'>T</a> - <a href='#u'>U</a> - <a href='#v'>V</a> - <a href='#w'>W</a> - <a href='#x'>X</a> - <a href='#y'>Y</a> - <a href='#z'>Z</a></p>" >> "$AUTHORS_DIR/index.md"

letter=""
echo "<div class='grid'>" >> "$AUTHORS_DIR/index.md"

for pair in "${sorted_pairs[@]}"; do
    last_name=$(echo "$pair" | cut -f1)  
    author=$(echo "$pair" | cut -f2-)  
    
    if [[ $author == "" ]]; then
        continue
    fi
    
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
    echo '<h3 id="number-posts">There are ... items referenced.</h3>' >> "$AUTHORS_DIR/$sanitized_slug.md"
    echo "<p id='info-authors'>Alternative author names: "$(jq -r --arg slug "$sanitized_slug" '.[$slug] | join(", ")' $MAPPINGS_FILE)".</p>" >> "$AUTHORS_DIR/$sanitized_slug.md"

    echo "<hr />" >> "$AUTHORS_DIR/$sanitized_slug.md"
    
    echo '<ul class="post-list">' >> "$AUTHORS_DIR/$sanitized_slug.md"
    echo -e "${authors[$author]}" | sort -t'|' -k1,1r | cut -d'|' -f2 | iconv -t UTF-8 >> "$AUTHORS_DIR/$sanitized_slug.md"
    echo "</ul>" >> "$AUTHORS_DIR/$sanitized_slug.md"
    echo "{% include count-posts.html %}" >> "$AUTHORS_DIR/$sanitized_slug.md"
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
    echo '<h3 id="number-posts">There are ... items referenced.</h3>' >> "$YEARS_DIR/$year.md"
    echo '<ul class="post-list">' >> "$YEARS_DIR/$year.md"
    echo -e "${years[$year]}" | sort -t'|' -k1,1r | cut -d'|' -f2 | iconv -t UTF-8 >> "$YEARS_DIR/$year.md"
    echo "</ul>" >> "$YEARS_DIR/$year.md"
    echo "{% include count-posts.html %}" >> "$YEARS_DIR/$year.md"
done

echo "Pages generated!"
exit 0

