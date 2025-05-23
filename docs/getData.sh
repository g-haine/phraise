#!/bin/bash

# Ce fichier prenant une liste de DOI en argument permet de générer :
# * Un fichier .json unique qui permettra de créer les posts et de faciliter la recherche sur le site
#
# Il regroupe tous les appels aux différentes API pour les minimiser.

# Vérifie si un fichier d'entrée est fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <fichier_doi.txt>"
    exit 1
fi

# S'assurer de ne pas rechercher de doublon
doi_file=$1
input_file="DOIuniq.txt"

# Les entrées doivent être unique dans le fichier & ne pas être dans DOI.txt
echo $(date -Iseconds)" Check unicity of DOIs..."
tmp_file=$(mktemp)
cat $doi_file | tr '[:upper:]' '[:lower:]' > $tmp_file
awk '!seen[$0]++' $tmp_file > $input_file
grep -vFxf DOI.txt "$input_file" > "$doi_file"
input_file=$doi_file
rm "DOIuniq.txt"

# Les fonctions communes
if [ -f .utils ]; then
    source .utils
else
    echo "Erreur : fichier .utils introuvable !" >&2
    exit 1
fi

# Maintenant la boucle sur les DOI

# Le fichier .json créé
output_json="assets/data/biblio.json"

# Sauve les précédentes extractions de données
echo $(date -Iseconds)" Start .json database creation..."
mv $output_json "assets/data/biblio-"$(date -Iseconds)".json"

echo "[" > $output_json

# Pour ajouter une virgule à partir de la deuxième entrée
first=true

# Boucle sur les DOIs
k=0
while IFS= read -r doi; do
    (( k+=1 ))
    echo $(date -Iseconds)" DOI $k: $doi"
    # Extraction des données
    response=$(fetch_metadata_crossref "$doi")
    status=$(echo "$response" | jq -r '.status')

    if [[ "$status" == "ok" ]]; then
        # Récupère les data
        title=$(echo "$response" | jq -r '.message.title // [""] | .[0]' | sed -E 's/<[^>]*mml[^>]*>//g' | sed -E 's/"/\\"/g')
        authors=$(echo "$response" | jq -r '.message.author')
        type=$(echo "$response" | jq -r '.message.type // ""')
        abstract=$(echo "$response" | jq -r '.message.abstract // ""')
        journal=$(echo "$response" | jq -r '.message["container-title"] // [""] | .[0]')
        year=$(echo "$response" | jq -r '.message["published-print"]["date-parts"][0][0] // ""')
        volume=$(echo "$response" | jq -r '.message.volume // ""')
        issue=$(echo "$response" | jq -r '.message.issue // ""')
        event=""
        isbn=$(echo "$response" | jq -r '.message["isbn-type"][0]["value"] // ""')
        pages=$(echo "$response" | jq -r '.message.page // "" | gsub("-"; "--")')
        publisher=$(echo "$response" | jq -r '.message.publisher // ""')
        keywords=$(echo "$response" | jq -r '.message.subject // [] | join(", ")')
        dateY=$(echo "$response" | jq -r '.message.created["date-parts"][0][0] // ""')
        dateM=$(echo "$response" | jq -r '.message.created["date-parts"][0][1] // ""')
        dateD=$(echo "$response" | jq -r '.message.created["date-parts"][0][2] // ""')
        
        # Génère le slug, vérifie son unicité grâce aux bib existants, puis génère le .bib associé
        slug=$(slugify "$title")
        bibfile="assets/bib/$slug.bib"
        while [ -f $bibfile ]; do
            slug+="0"
            bibfile="assets/bib/$slug.bib"
        done
        $(print_bib "$doi" "$bibfile")
        
        # Formate les références
        references="["
        while IFS= read -r ref; do
            d_ref=$(echo "$ref" | jq -r .DOI 2>/dev/null)
            if echo "$d_ref" | grep -q "10."; then
                ti_ref=$(get_citation "$d_ref" | tr -d '\000-\031' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/\\/\\\\/g' | sed -E 's/"/\\"/g')
            else
                ti_ref=$(echo "$ref" | jq -r '
                    [
                        (if .author then .author + "," else empty end),
                        (if .["article-title"] then .["article-title"] + "." else empty end),
                        (if .["journal-title"] then .["journal-title"] else empty end),
                        (if .["volume-title"] then .["volume-title"] else empty end),
                        (if .year then "(" + (.year|tostring) + ")" else empty end)
                    ] | map(select(. != "")) | join(" ")' | tr -d '\000-\031' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/\\/\\\\/g' | sed -E 's/"/\\"/g' | sed -E 's/<[^>]*jats[^>]*>//g')
            fi
            references+='{"doi": "'$d_ref'", "title": "'$ti_ref'"},'
        done < <(echo "$response" | jq -c '.message.reference[]' 2>/dev/null)
        if [ "$references" != "[" ]; then
            references=${references::-1}
        fi
        references+="]"
        
        # Year from creation if not published-print
        if [ -z "$year" ]; then
            year=$(echo $dateY)
        fi
        
        # Récupère l'url "final" (avant redirection js) à partir du DOI
        url=$(curl -Ls -o /dev/null -w "%{url_effective}" "https://doi.org/$doi")
        
        # Update si elsevier
        if echo "$url" | grep -q "elsevier"; then
            json_scopus=$(fetch_metadata_scopus "$doi")
            abstract=$(abstract_from_scopus "$json_scopus")
            keywords=$(keywords_from_scopus "$json_scopus")
            event=$(event_from_scopus "$json_scopus" | tr -d '\000-\031' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/\\/\\\\/g' | sed -E 's/"/\\"/g' | sed -E 's/<[^>]*jats[^>]*>//g')
        fi
        
        # Update si springer
        if echo "$url" | grep -q "springer"; then
            json_springer=$(fetch_metadata_springer "$doi")
            abstract=$(abstract_from_springer "$json_springer")
            keywords=$(keywords_from_springer "$json_springer")
            event=$(event_from_springer "$json_springer" | tr -d '\000-\031' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/\\/\\\\/g' | sed -E 's/"/\\"/g' | sed -E 's/<[^>]*jats[^>]*>//g')
        fi
        
        # Complement pour l'abstract
        if [ -z "$abstract" ]; then
            complement=$(fetch_abstract_complement $doi)
            [ -n "$complement" ] && abstract="$complement"
        fi

        # Nettoyage de l'abstract
        abstract=$(echo $abstract | tr -d '\000-\031' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/\\/\\\\/g' | sed -E 's/"/\\"/g' | sed -E 's/<[^>]*jats[^>]*>//g' | sed -E 's/summary//Ig' | sed -E 's/abstract//Ig')
        
        if [ "$first" = true ]; then
            first=false
        else
            echo "," >> $output_json
        fi

        # .json format de toutes les datas
        echo "  {" >> $output_json
        echo "    \"doi\": \"$doi\"," >> $output_json
        echo "    \"type\": \"$type\"," >> $output_json
        echo "    \"title\": \"$title\"," >> $output_json
        echo "    \"authors\": $authors," >> $output_json
        echo "    \"abstract\": \"$abstract\"," >> $output_json
        echo "    \"journal\": \"$journal\"," >> $output_json
        echo "    \"year\": \"$year\"," >> $output_json
        echo "    \"volume\": \"$volume\"," >> $output_json
        echo "    \"issue\": \"$issue\"," >> $output_json
        echo "    \"event\": \"$event\"," >> $output_json
        echo "    \"isbn\": \"$isbn\"," >> $output_json
        echo "    \"pages\": \"$pages\"," >> $output_json
        echo "    \"publisher\": \"$publisher\"," >> $output_json
        echo "    \"keywords\": \"$keywords\"," >> $output_json
        echo "    \"dateY\": \"$dateY\"," >> $output_json
        echo "    \"dateM\": \"$dateM\"," >> $output_json
        echo "    \"dateD\": \"$dateD\"," >> $output_json
        echo "    \"permalink\": \"$slug\"," >> $output_json
        echo "    \"references\": $references" >> $output_json
        echo "  }" >> $output_json
    else
        echo "DOI: $doi is not available yet."
    fi

done < "$input_file"

echo "]" >> $output_json

# Tout s'est bien passé !
echo "Données récupérées avec succès !"
exit 0

