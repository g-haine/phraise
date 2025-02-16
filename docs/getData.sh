#!/bin/bash

# Ce fichier prenant une liste de DOI en argument permet de générer :
# * Un fichier .json unique qui permettra de faciliter la recherche sur le site
# * Un fichier markdown par DOI qui permettra de référencer la référence sur le site

# Vérifie si un fichier d'entrée est fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <fichier_doi.txt>"
    exit 1
fi
input_file=$1

# Une fonction de slugify des titres
slugify () {
    echo "$1" \
    | sed -r 's/[~\^]+//g' \
    | sed -r 's/[^a-zA-Z0-9]+/-/g' \
    | sed -r 's/^-+|-+$//g' \
    | tr '[:upper:]' '[:lower:]' \
    | sed -r 's/ /-/g' \
    | iconv -t ascii//TRANSLIT
}

# Ajoute un zéro si le mois ou le jour est entre 1 et 9
pad_zero () {
    printf "%02d" "$1"
}

# Une fonctione qui récupère le bibtex depuis crossref
print_bib () {
    local doi=$1
    crossrefEndpoint="http://api.crossref.org/works/$doi/transform/application/x-bibtex"
    crossrefBib="$(curl -s $crossrefEndpoint)"
    if ! echo $crossrefBib | head -n 1 | grep -q "Resource" ; then
        bibtex="$(echo "{% raw %}"$crossrefBib"{% endraw %}" \
        | sed -e 's/ @/@/g' \
        | sed -e 's/},/},\n /g' \
        | sed -e 's/, series/,\n  series/g' \
        | sed -e 's/, pages/,\n  pages/g' \
        | sed -e 's/, title/,\n  title/g' \
        | sed -e '/title/s/={/={{/g' \
        | sed -e '/title/s/},/}},/g' \
        | sed -e 's/ }/\n}/g' \
        | sed -e 's/, }/\n}/g' \
        | sed -e '/pages/s/–/--/g' \
        | sed -e '/month/d' \
        | sed -e '/url/d' \
        | tac | sed -e '2 s/,//g' | tac)"
        echo "$bibtex"
    fi
}

# Le fichier .json créé
output_json="_data/biblio.json"

# Le path des posts markdown
path_md="_posts/"

echo "[" > $output_json

# Appel à l'API de crossref
fetch_metadata () {
    local doi=$1
    echo $(curl -s "https://api.crossref.org/works/$doi")
}

# Pour ajouter une virgule à partir de la deuxième entrée
first=true

# Boucle sur les DOIs
while IFS= read -r doi; do
    # Extraction des données
    response=$(fetch_metadata "$doi")

    title=$(echo $response | jq -r '.message.title // [""] | .[0]')
    authors=$(echo $response | jq -r '.message.author // [] | map("\(.given // "") \(.family // "")") | join(", ")')
    type=$(echo $response | jq -r '.message.type // ""')
    abstract=$(echo $response | jq -r '.message.abstract // ""')
    journal=$(echo $response | jq -r '.message["container-title"] // [""] | .[0]')
    year=$(echo $response | jq -r '.message["published-print"]["date-parts"][0][0] // ""')
    volume=$(echo $response | jq -r '.message.volume // ""')
    issue=$(echo $response | jq -r '.message.issue // ""')
    isbn=$(echo $response | jq -r '.message["isbn-type"][0]["value"] // ""')
    pages=$(echo $response | jq -r '.message.page // "" | gsub("-"; "--")')
    publisher=$(echo $response | jq -r '.message.publisher // ""')
    keywords=$(echo $response | jq -r '.message.subject // [] | join(", ")')
    dateY=$(echo $response | jq -r '.message.created["date-parts"][0][0] // ""')
    dateM=$(echo $response | jq -r '.message.created["date-parts"][0][1] // ""')
    dateD=$(echo $response | jq -r '.message.created["date-parts"][0][2] // ""')
    references=$(echo $response | jq -c '[.message.reference[]? | {doi: (.DOI // ""), title: (.unstructured // "")}]')
    
    # Year from creation if not published-print
    if [ -z "$year" ]; then
        year=$(echo $dateY)
    fi

    # Complément abstract et keywords avec Semantic Scholar
    ss_response=$(curl -s "https://api.semanticscholar.org/v1/paper/$doi")
    if [ -z "$abstract" ]; then
        abstract=$(echo $ss_response | jq -r '.abstract // ""')
    fi
    if [ -z "$keywords" ]; then
        keywords=$(echo $ss_response | jq -r '.keywords // [] | join(", ")')
    fi

    if [ "$first" = true ]; then
        first=false
    else
        echo "," >> $output_json
    fi

    # .json format pour jekyll-search
    echo "  {" >> $output_json
    echo "    \"doi\": \"$doi\"," >> $output_json
    echo "    \"type\": \"$type\"," >> $output_json
    echo "    \"title\": \"$title\"," >> $output_json
    echo "    \"authors\": \"$authors\"," >> $output_json
    echo "    \"abstract\": \"$abstract\"," >> $output_json
    echo "    \"journal\": \"$journal\"," >> $output_json
    echo "    \"year\": \"$year\"," >> $output_json
    echo "    \"volume\": \"$volume\"," >> $output_json
    echo "    \"issue\": \"$issue\"," >> $output_json
    echo "    \"isbn\": \"$isbn\"," >> $output_json
    echo "    \"pages\": \"$pages\"," >> $output_json
    echo "    \"publisher\": \"$publisher\"," >> $output_json
    echo "    \"keywords\": \"$keywords\"," >> $output_json
    echo "    \"dateY\": \"$dateY\"," >> $output_json
    echo "    \"dateM\": \"$dateM\"," >> $output_json
    echo "    \"dateD\": \"$dateD\"," >> $output_json
    echo "    \"references\": $references" >> $output_json
    echo "  }" >> $output_json

    # Création du post en markdown
    output_md="$path_md$(pad_zero $dateY)-$(pad_zero $dateM)-$(pad_zero $dateD)-$(slugify "$title").md"
    
    echo "---" > $output_md
    echo "layout: post" >> $output_md
    echo "title: $title" >> $output_md
    echo "date: $dateY-$dateM-$dateD 00:00:00 +0100" >> $output_md
    echo "categories: $type" >> $output_md
    echo "---" >> $output_md
    echo "" >> $output_md
    echo "## Authors:" >> $output_md
    echo "$authors" >> $output_md
    echo "" >> $output_md
    echo "## BibTeX:" >> $output_md
    echo "{% highlight latex %}" >> $output_md
    echo "$(print_bib $doi)" >> $output_md
    echo "{% endhighlight %}" >> $output_md
    echo "" >> $output_md

done < "$input_file"

echo "]" >> $output_json

# Tout s'est bien passé !
exit 0

