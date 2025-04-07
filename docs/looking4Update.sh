#!/bin/bash

# Ce script cherche les dois pour lesquels il manque des infos (mais qui étaient déjà online) :
# /!\ Il ne fait PAS la mise à jour /!\
# Il identifie dans le assets/data/biblio.json les articles (uniquement !) incomplets
# Il vérifie les bibtex de crossref pour voir s'ils sont différents
# Il les déplace dans un dossier "trash" (en les retirant du DOI.txt, du .json, et des bibtex)
# Il génère un fichier updateDOI.txt
# Ensuite, il faut lancer la procédure d'update habituelle avec newDOI.txt
# Puis annuler certains changements  avec "trash" /!\ certaines données en ligne ayant des soucis
# Et enfin, supprimer "trash"

# Fichier DOI source
DOI_SOURCE="DOI.txt"

# Fichier JSON source
BIBLIO_JSON="assets/data/biblio.json"

# Fichier de sortie des DOI à mettre à jour
DOI_FILE="newDOI.txt"

# La "poubelle" (on supprimera à la main si tout va bien)
TRASH_DIR="trash/"
TRASH_JSON="trash.json"

# Les fonctions communes
if [ -f .utils ]; then
    source .utils
else
    echo "Erreur : fichier .utils introuvable !" >&2
    exit 1
fi

echo $(date -Iseconds)" Identification of incomplete publications starts."
mkdir $TRASH_DIR
trash="$TRASH_DIR$TRASH_JSON"
: > $trash
bibcurrent="currentBib.bib"
touch $bibcurrent

# Boucle sur les éléments du biblio.json
while IFS= read -r line; do
    doi=$(echo "$line" | jq -r '.doi')
    slug=$(echo "$line" | jq -r '.permalink // ""')
    echo $(date -Iseconds)" Looking for DOI: $doi"
    bibfile="assets/bib/$slug.bib"
    # Quand le DOI exists, mais que la bibtex n'a pas pu être fabriquer précédemment
    if [ ! -f $bibfile ]; then
        echo -e "\t No bibtex!" >&2
        echo "$doi" >> $DOI_FILE
        sed -i -e "\|$doi|Id" "$DOI_SOURCE"
        continue
    fi
    
    # Récupère le bibtex actuellement en ligne
    $(print_bib "$doi" "$bibcurrent")
    
    # Sinon, on compare avec l'ancien bibtex
    if ! diff -q "$bibfile" "$bibcurrent" > /dev/null; then
        echo -e "\t Different bibtex!"
        echo "$doi" >> $DOI_FILE
        sed -i -e "\|$doi|Id" "$DOI_SOURCE"
        mv "$bibfile" "$TRASH_DIR$(basename $bibfile)"
        jq --arg DOI "$doi" '[.[] | select(.doi == $DOI)]' "$BIBLIO_JSON" >> $trash
        continue
    fi
    echo -e "\t OK, pass"
    
done < <(jq -c '.[] | select(.type == "journal-article" and (.volume == "" or .pages == ""))' "$BIBLIO_JSON")

sed -i -z -e "s/]\n\[/,/g" $trash
tmp_file=$(mktemp)
jq --indent 2 . $trash > $tmp_file
mv $tmp_file $trash

while IFS= read -r line; do
    doi=$(echo "$line" | jq -r '.doi')
    tmp_file=$(mktemp)
    jq --arg DOI "$doi" '[.[] | select(.doi != $DOI)]' "$BIBLIO_JSON" > tmp_file && mv tmp_file "$BIBLIO_JSON"
done < <(jq -c '.[]' "$trash")

rm "$bibcurrent"

# Boucle sur les DOI qui n'ont PAS d'entrées dans le biblio.json
while IFS= read -r doi; do
    if ! jq -e --arg DOI "$doi" '.[] | select(.doi == $DOI)' $BIBLIO_JSON > /dev/null; then
        echo -e "\t DOI still NOT in the database: $doi"
        echo "$doi" >> $DOI_FILE
        sed -i -e "\|$doi|Id" "$DOI_SOURCE"
    fi
done < $DOI_SOURCE

# Tout s'est bien passé !
echo $(date -Iseconds)" Search for update successful!"
exit 0

