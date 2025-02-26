#!/bin/bash

# Ce fichier prenant le .json créé par getData.sh en argument permet de vérifier rapidement les trop longs titres et les doublons permalink par malchance !

# Ajoute des zéros si nécessaire
pad_zero () {
    printf "%03d" "$1"
}

# Fichier JSON source
BIBLIO_JSON="assets/data/biblio.json"

# Assurer la présence du fichier JSON
if [ ! -f "$BIBLIO_JSON" ]; then
    echo "Erreur : Fichier $BIBLIO_JSON introuvable !" >&2
    exit 1
fi

OUT="permalinks.txt"
OUT_SORTED="permalinks_sorted.txt"
OUT_UNIQ="permalinks_uniq.txt"
OUT_DIFF="permalinks_diff.txt"
rm -f "$OUT" "$OUT_SORTED" "$OUT_UNIQ" "$OUT_DIFF"
touch "$OUT"
touch "$OUT_SORTED"
touch "$OUT_UNIQ"
touch "$OUT_DIFF"

echo "Collecte les permalinks..."
# Boucle à travers toutes les entrées du JSON
jq -c '.[]' "$BIBLIO_JSON" | while IFS= read -r entry; do
    permalink=$(echo "$entry" | jq -r '.permalink')
    echo $(pad_zero ${#permalink})" $permalink" >> $OUT
done

echo "Tri les permalinks..."
sort -i $OUT > $OUT_SORTED
sort -i -u $OUT > $OUT_UNIQ

echo "Compare les permalinks..."
comm -3 $OUT_SORTED $OUT_UNIQ > $OUT_DIFF

# Tout s'est bien passé !
echo "Test sur les permalinks effectué !"
exit 0

