#!/usr/bin/env bash
set -euo pipefail

# Les fonctions communes
if [ -f .utils ]; then
  source .utils
else
  printf '[X] %s\n' "Error: .utils file is missing!" >&2; exit 1;
fi

# Ce fichier permet de :
# * concaténer les fichiers DOI.txt et newDOI.txt
# * vider newDOI.txt
# * concaténer les fichiers biblio.json avec la dernière sauvegarde générée par getData.sh
# * supprimer les éventuels doublons dans le biblio.json
# * nettoyer le fichier DOI.txt

# Fichiers de DOI
DOI_FILE="DOI.txt"
NEW_DOI_FILE="newDOI.txt"
BAD_DOI_FILE="badDOI.txt"

# Fichiers JSON
BIBLIO_FILE="assets/data/biblio.json"
BACKUP_DIR="assets/data"
BACKUP_FILE=$(ls -t "$BACKUP_DIR"/biblio-*.json 2>/dev/null | head -n 1)

# Ajouter le contenu de "newDOI.txt" à "DOI.txt"
cat "$NEW_DOI_FILE" >> "$DOI_FILE"

# Vider "newDOI.txt"
> "$NEW_DOI_FILE"

# Concaténer les fichiers JSON (biblio.json et la dernière sauvegarde trouvée)
if [[ -n "$BACKUP_FILE" ]]; then
  jq -s 'add' "$BACKUP_FILE" "$BIBLIO_FILE" > "$BIBLIO_FILE.tmp" && mv "$BIBLIO_FILE.tmp" "$BIBLIO_FILE"
  log $(date -Iseconds)" JSON files concatenation OK."
else
  die " You need a backup biblio file!"
fi

# Fichiers JSON temporaire
TEMP_JSON="assets/data/biblio_temp.json"

log $(date -Iseconds)" Deleting duplicate in $BIBLIO_FILE..."

# Utilise jq pour éliminer les doublons en fonction du champ DOI
jq 'unique_by(.doi)' "$BIBLIO_FILE" > "$TEMP_JSON"

# Vérifie si la commande jq a réussi
if [[ $? -eq 0 ]]; then
  mv "$TEMP_JSON" "$BIBLIO_FILE"
  log $(date -Iseconds)" Done."
else
  rm -f "$TEMP_JSON"
  die "Error with $BIBLIO_FILE."
fi

log $(date -Iseconds)" Cleaning $BIBLIO_FILE according to $BAD_DOI_FILE..."

# Suppression des éventuelles entrées qui sont dans badDOI.txt
tmp=$(mktemp)
# Copie initiale
cp "$BIBLIO_FILE" "$tmp"

while IFS= read -r doi; do
  # On évite les lignes vides ou commentées
  [[ -z "$doi" || "$doi" =~ ^# ]] && continue

  jq --arg doi "$doi" 'del(.[] | select(.doi==$doi))' "$tmp" > "$tmp.new"
  mv "$tmp.new" "$tmp"
done < "$BAD_DOI_FILE"

# Une fois la boucle finie, on remplace le fichier d'origine
mv "$tmp" "$BIBLIO_FILE"

log $(date -Iseconds)" Cleaning $DOI_FILE according to $BAD_DOI_FILE..."

# On nettoie DOI.txt
tmp_doi=$(mktemp)
# Supprime toutes les lignes de DOI.txt qui apparaissent dans badDOI.txt
grep -vFxf "$BAD_DOI_FILE" "$DOI_FILE" > "$tmp_doi"
mv "$tmp_doi" "$DOI_FILE"

log $(date -Iseconds)" Update OK!"

