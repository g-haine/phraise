#!/bin/bash

# Ce fichier utilise le .json créé par getData.sh pour générer (PAS AUTOMATIQUEMENT !) :
# * Un fichier .json qui liste le nom des auteurs et les variantes apparaissant dans les publis

# Fichiers d'entrée
BIBLIO_FILE="assets/data/biblio.json"
MAPPINGS_FILE="assets/data/author_mappings.json"

# Vérifier l'existence des fichiers
if [[ ! -f "$BIBLIO_FILE" ]]; then
    echo "Erreur : fichier $BIBLIO_FILE introuvable."
    exit 1
fi

# Extraction des auteurs sous "Prénom Nom" exact depuis `_data/biblio.json`
AUTHORS=$(jq -r '.[] | .authors[]? | select(.family) | "\(.given) \(.family)"' "$BIBLIO_FILE")

if [[ ! -f "$MAPPINGS_FILE" ]]; then
    echo "Erreur : fichier $MAPPINGS_FILE introuvable."
    exit 1
fi

# Les fonctions communes
if [ -f .utils ]; then
    source .utils
else
    echo "Erreur : fichier .utils introuvable !" >&2
    exit 1
fi

declare -A author_to_slug

# Charger `_data/author_mappings.json` en mémoire
while IFS= read -r entry; do
    slug=$(echo "$entry" | jq -r '.key')
    
    # Lire toutes les variations associées à ce slug
    while IFS= read -r variation; do
        author_to_slug["$(echo "$variation" | iconv -c -f UTF-8 -t UTF-8)"]="$slug"
    done < <(jq -r ".\"$slug\"[]" "$MAPPINGS_FILE")
done < <(jq -c 'to_entries[]' "$MAPPINGS_FILE")

echo "Vérification des auteurs dans _data/author_mappings.json..."
echo ""

sorted_pairs=()
k=0
# Vérification des correspondances
while IFS= read -r author; do
    found=false
    
    for known in "${!author_to_slug[@]}"; do
        if [[ "$author" == "$known" ]]; then
            echo "$author → ${author_to_slug[$known]}"
            found=true
            break
        fi
    done

    if [[ "$found" == false ]]; then
    
        last_name=$(echo "$author" | awk '{print $NF}')  # Extraire le dernier mot
    
        # Normaliser le dernier mot en ASCII
        normalized_last_name=$(echo "$last_name" | iconv -f UTF-8 -t ASCII//TRANSLIT | sed -E '
            s/Ü/U/;
            s/Ç/C/;
            s/Š/S/;
            s/Ž/Z/;
            s/Ð/D/;
            s/Ñ/N/;
            s/Ł/L/;
            s/Ø/O/;
            s/Æ/A/;
            s/Œ/OE/')
        slug=$(slugify "$author")
        to_add="  \"$slug\": [ \"$author\" ]"
        echo "Not found: $author"
        sorted_pairs+=("$normalized_last_name	$to_add")  # Tabulation pour séparer proprement
        (( k+=1 ))
    fi
done <<< "$AUTHORS"

# Trier les auteurs par leur dernier mot
IFS=$'\n' sorted_pairs=($(sort -k1 <<<"${sorted_pairs[*]}"))
unset IFS

echo ""
echo "Add to the author_mappings.json file:"
echo ""

for pair in "${sorted_pairs[@]}"; do
    last_name=$(echo "$pair" | cut -f1)  
    to_add=$(echo "$pair" | cut -f2-)  
    echo ","
    echo "$to_add"
    echo ""
done

echo ""
echo "Fin de la vérification : $k entrées non-trouvées."

