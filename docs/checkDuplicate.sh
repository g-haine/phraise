#!/bin/bash

# Ce fichier utilise le .json créé par getData.sh et retire les doublons

# Fichiers JSON source et temporaire
BIBLIO_JSON="assets/data/biblio.json"
TEMP_JSON="assets/data/biblio_temp.json"

# Vérifie si le fichier JSON existe
if [[ ! -f "$BIBLIO_JSON" ]]; then
  echo "Fichier $BIBLIO_JSON introuvable."
  exit 1
fi

echo "Suppression des doublons dans $BIBLIO_JSON..."

# Utilise jq pour éliminer les doublons en fonction du champ DOI
jq 'unique_by(.doi)' "$BIBLIO_JSON" > "$TEMP_JSON"

# Vérifie si la commande jq a réussi
if [[ $? -eq 0 ]]; then
  mv "$TEMP_JSON" "$BIBLIO_JSON"
  echo "Doublons supprimés avec succès."
else
  echo "Erreur lors du traitement du fichier JSON."
  rm -f "$TEMP_JSON"
  exit 1
fi

