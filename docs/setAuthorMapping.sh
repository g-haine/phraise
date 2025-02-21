#!/bin/bash

# Fichiers d'entrée
BIBLIO_FILE="assets/data/biblio.json"
MAPPINGS_FILE="assets/data/author_mappings.json"

# Vérifier l'existence des fichiers
if [[ ! -f "$BIBLIO_FILE" ]]; then
    echo "Erreur : fichier $BIBLIO_FILE introuvable."
    exit 1
fi

if [[ ! -f "$MAPPINGS_FILE" ]]; then
    echo "Erreur : fichier $MAPPINGS_FILE introuvable."
    exit 1
fi

declare -A author_to_slug

# Charger `_data/author_mappings.json` en mémoire
while IFS= read -r entry; do
    slug=$(echo "$entry" | jq -r '.key')
    
    # Lire toutes les variations associées à ce slug
    while IFS= read -r variation; do
        author_to_slug["$variation"]="$slug"
    done < <(jq -r ".\"$slug\"[]" "$MAPPINGS_FILE")
done < <(jq -c 'to_entries[]' "$MAPPINGS_FILE")

echo "🔎 Vérification des auteurs dans _data/author_mappings.json..."
echo ""

# Extraction des auteurs sous "Prénom Nom" exact depuis `_data/biblio.json`
AUTHORS=$(jq -r '.[] | .authors[]? | select(.family) | "\(.given) \(.family)"' "$BIBLIO_FILE")


# Vérification des correspondances
while IFS= read -r author; do
    found=false

    for known in "${!author_to_slug[@]}"; do
        if [[ "$author" == "$known" ]]; then
            echo "✅ $author → ${author_to_slug[$known]}"
            found=true
            break
        fi
    done

    if [[ "$found" == false ]]; then
        echo "⚠️  À ajouter : $author"
    fi
done <<< "$AUTHORS"

echo ""
echo "📝 Fin de la vérification."

