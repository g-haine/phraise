#!/bin/bash

# Ce fichier permet de :
# * concaténer les fichiers DOI.txt et newDOI.txt
# * vider newDOI.txt
# * concaténer les fichiers biblio.json avec la dernière sauvegarde générée par getData.sh

# Fichiers de DOI
DOI_FILE="DOI.txt"
NEW_DOI_FILE="newDOI.txt"

# Fichiers JSON
BIBLIO_FILE="assets/data/biblio.json"
BACKUP_DIR="assets/data"
BACKUP_FILE=$(ls -t "$BACKUP_DIR"/biblio-*.json 2>/dev/null | head -n 1)

# 1. Ajouter le contenu de "newDOI.txt" à "DOI.txt"
cat "$NEW_DOI_FILE" >> "$DOI_FILE"

# 2. Vider "newDOI.txt"
> "$NEW_DOI_FILE"

# 3. Concaténer les fichiers JSON (biblio.json et la dernière sauvegarde trouvée)
if [[ -n "$BACKUP_FILE" ]]; then
    jq -s 'add' "$BACKUP_FILE" "$BIBLIO_FILE" > "$BIBLIO_FILE.tmp" && mv "$BIBLIO_FILE.tmp" "$BIBLIO_FILE"
    echo "JSON files concatenation OK."
else
    echo "You need a backup biblio file!"
fi

echo "Update OK!"

