#!/bin/bash

# Ce fichier prenant une liste de DOI en argument permet de générer :
# * Un fichier .json unique qui permettra de créer les posts et de faciliter la recherche sur le site

# Vérifie si un fichier d'entrée est fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <fichier_doi.txt>"
    exit 1
fi

# Mail, Scopus key and Springer key
if [ -f .env ]; then
    source .env
else
    echo "Erreur : fichier .env introuvable !" >&2
    exit 1
fi

# S'assurer de ne pas rechercher de doublon
doi_file=$1
input_file="DOIuniq.txt"

# Les entrées doivent être unique dans le fichier & ne pas être dans DOI.txt
awk '!seen[$0]++' $doi_file > $input_file
grep -avf "DOI.txt" $input_file > $doi_file
input_file=$doi_file

# D'abord quelques fonctions

# Une fonction de slugify des titres
slugify () {
    echo "$1" |
    iconv -t ascii//TRANSLIT |
    tr '[:upper:]' '[:lower:]' |
    tr -cs 'a-z0-9' '-' |
    sed -E 's/^-+|-+$//g'
}

# Appel à l'API de crossref
fetch_metadata_crossref () {
    local doi=$1
    request=$(curl -s -w "%{http_code}" "https://api.crossref.org/works/$doi?mailto=$MAIL")
    http=${request: -3}
    response=${request:: -3}
    if [[ "$http" -eq 200 ]]; then
        echo $response
    else
        echo '{"status":"error"}'
    fi
}

# Appel à l'API de scopus
fetch_metadata_scopus () {
    local doi=$1
    echo $(curl -s -X GET "https://api.elsevier.com/content/article/doi/$doi" -H "Accept: application/json" -H "X-ELS-APIKey: $SCOPUS_API_KEY")
}

# Abstract via scopus
abstract_from_scopus () {
    local json=$1
    if echo "$json" | jq empty 2>/dev/null; then
        local scopus_abstract=$(echo "$json" | jq -r '.["full-text-retrieval-response"].coredata."dc:description" // ""')
        [ -n "$scopus_abstract" ] && echo "$scopus_abstract"
    fi
}

# Keywords via scopus
keywords_from_scopus () {
    local json=$1
    if echo "$json" | jq empty 2>/dev/null; then
        local scopus_keywords=$(echo "$json" | jq -r 'if .["full-text-retrieval-response"].coredata."dcterms:subject" then 
              [.["full-text-retrieval-response"].coredata."dcterms:subject"[]["$"]] | join("; ") 
           else 
              "" 
           end')
        [ -n "$scopus_keywords" ] && echo "$scopus_keywords"
    fi
}

# event via scopus : super pour le nom de la conf IFAC
event_from_scopus () {
    local json=$1
    if echo "$json" | jq empty 2>/dev/null; then
        local scopus_nameIssue=$(echo "$json" | jq -r '.["full-text-retrieval-response"].coredata."prism:issueName" // ""')
        [ -n "$scopus_nameIssue" ] && echo "$scopus_nameIssue"
    fi
}

# Appel à l'API de Springer
fetch_metadata_springer () {
    local doi=$1
    echo $(curl -s -X GET "https://api.springernature.com/meta/v2/json?q=doi:$doi&api_key=$SPRINGER_API_KEY")
}

# Abstract via Springer
abstract_from_springer () {
    local json=$1
    if echo "$json" | jq empty 2>/dev/null; then
        local springer_abstract=$(echo "$json" | jq -r '.records[0].abstract // ""')
        [ -n "$springer_abstract" ] && echo "$springer_abstract"
    fi
}

# Keywords via Springer
keywords_from_springer () {
    local json=$1
    if echo "$json" | jq empty 2>/dev/null; then
        local springer_keywords=$(echo "$json" | jq -r 'if .records[0].keyword then 
              [.records[0].keyword[]] | join("; ") 
           else 
              "" 
           end')
        [ -n "$springer_keywords" ] && echo "$springer_keywords"
    fi
}

# event via springer : super pour le nom de la conf également, type GSI
event_from_springer () {
    local json=$1
    if echo "$json" | jq empty 2>/dev/null; then
        local springer_nameIssue=$(echo "$json" | jq -r '.records[0].conferenceInfo[] | select(.confSeriesName) | "\(.confSeriesName)"')
        [ -n "$springer_nameIssue" ] && echo "$springer_nameIssue"
    fi
}

# Optimisation avancée de la récupération des abstracts avec correction des erreurs de boucle
fetch_abstract_complement () {
    local doi=$1
    local abstract="No abstract available"
    local candidates=()

    # Fonction de sécurité pour les appels API avec suivi des redirections
    safe_curl () {
        curl -Ls --connect-timeout 5 --retry 3 --retry-delay 2 "$1" || echo ""
    }

    # 1. Essai via OpenAlex
    local openalex_response=$(safe_curl "https://api.openalex.org/works/https://doi.org/$doi")
    if echo "$openalex_response" | jq empty 2>/dev/null; then
        local openalex_abstract=$(echo "$openalex_response" | jq -r '.abstract_inverted_index | to_entries? | map(.value) | unique | join(" ") // ""')
        [ -n "$openalex_abstract" ] && candidates+=("$openalex_abstract")
    fi

    # 2. Essai via Semantic Scholar
    local semantics_response=$(safe_curl "https://api.semanticscholar.org/v1/paper/$doi")
    if echo "$semantics_response" | jq empty 2>/dev/null; then
        local semantics_abstract=$(echo "$semantics_response" | jq -r '.abstract // ""')
        [ -n "$semantics_abstract" ] && candidates+=("$semantics_abstract")
    fi

    # 3. Sélection de l'abstract le plus long
    for candidate in "${candidates[@]}"; do
        if [ "${#candidate}" -gt "${#abstract}" ]; then
            abstract="$candidate"
        fi
    done

    echo "$abstract"
}

# Maintenant la boucle sur les DOI

# Le fichier .json créé
output_json="assets/data/biblio.json"

# Sauve les précédentes extractions de données
mv $output_json "assets/data/biblio-"$(date -Iseconds)".json"

echo "[" > $output_json

# Pour ajouter une virgule à partir de la deuxième entrée
first=true

# Boucle sur les DOIs
while IFS= read -r doi; do
    # Extraction des données
    response=$(fetch_metadata_crossref "$doi")
    status=$(echo "$response" | jq -r '.status')

    if [[ "$status" == "ok" ]]; then
        title=$(echo $response | jq -r '.message.title // [""] | .[0]')
        authors=$(echo $response | jq -r '.message.author')
        type=$(echo $response | jq -r '.message.type // ""')
        abstract=$(echo $response | jq -r '.message.abstract // ""')
        journal=$(echo $response | jq -r '.message["container-title"] // [""] | .[0]')
        year=$(echo $response | jq -r '.message["published-print"]["date-parts"][0][0] // ""')
        volume=$(echo $response | jq -r '.message.volume // ""')
        issue=$(echo $response | jq -r '.message.issue // ""')
        event=""
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
        
        # Récupère l'url "final" (avant redirection js) à partir du DOI
        url=$(curl -Ls -o /dev/null -w "%{url_effective}" "https://doi.org/$doi")
        
        # Update si elsevier
        if echo "$url" | grep -q "elsevier"; then
            json_scopus=$(fetch_metadata_scopus "$doi")
            abstract=$(abstract_from_scopus "$json_scopus")
            keywords=$(keywords_from_scopus "$json_scopus")
            event=$(event_from_scopus "$json_scopus")
        fi
        
        # Update si springer
        if echo "$url" | grep -q "springer"; then
            json_springer=$(fetch_metadata_springer "$doi")
            abstract=$(abstract_from_springer "$json_springer")
            keywords=$(keywords_from_springer "$json_springer")
            event=$(event_from_springer "$json_springer")
        fi
        
        # Complement pour l'abstract
        if [ -z "$abstract" ]; then
            complement=$(fetch_abstract_complement $doi)
            [ -n "$complement" ] && abstract="$complement"
        fi

        # Nettoyage de l'abstract
        abstract=$(echo $abstract | tr -d '\000-\031' | sed -E 's/\\/\\\\/g' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/"/\\"/g')
        
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
        echo "    \"abstract\": \"$abstract\","  >> $output_json
        echo "    \"journal\": \"$journal\"," >> $output_json
        echo "    \"year\": \"$year\"," >> $output_json
        echo "    \"volume\": \"$volume\"," >> $output_json
        echo "    \"issue\": \"$issue\"," >> $output_json
        echo "    \"event\": \"$event\"," | tr -d '\000-\031' | sed -E 's/\\/\\\\/g' >> $output_json
        echo "    \"isbn\": \"$isbn\"," >> $output_json
        echo "    \"pages\": \"$pages\"," >> $output_json
        echo "    \"publisher\": \"$publisher\"," >> $output_json
        echo "    \"keywords\": \"$keywords\"," >> $output_json
        echo "    \"dateY\": \"$dateY\"," >> $output_json
        echo "    \"dateM\": \"$dateM\"," >> $output_json
        echo "    \"dateD\": \"$dateD\"," >> $output_json
        echo "    \"permalink\": \"$(slugify "$title")\"," >> $output_json
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

