#!/bin/bash

# Ce script cherche :
#   * les nouveaux dois de crossref qui comportent "port-Hamiltonian" dans le titre ou l'abstract
#   * les dois pour lesquels il manque des infos (mais qui étaient déjà online) :
# /!\ Il ne fait PAS la mise à jour /!\
# Il identifie dans le assets/data/biblio.json les articles (uniquement !) incomplets
# Il vérifie les bibtex de crossref pour voir s'ils sont différents
# Il les déplace dans un dossier "trash" (en les retirant du DOI.txt, du .json, et des bibtex)
# Il complète le fichier newDOI.txt
# Ensuite, il faut lancer la procédure d'update habituelle avec newDOI.txt
# Puis annuler certains changements  avec "trash" /!\ certaines données en ligne ayant des soucis
# Et enfin, supprimer "trash"

#!/bin/bash

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

# On commence par une recherche d'update dans crossref
echo $(date -Iseconds)" Looking for news on CrossRef."
QUERY="port-Hamiltonian"
TMP_JSON="crossref_results.json"
TMP_DOIS="temp_dois.txt"

# Récupérer les 1000 publications les plus récentes contenant le mot-clé
curl -s "https://api.crossref.org/works?query=${QUERY}&rows=1000&sort=published&order=desc" -o "$TMP_JSON"

# Extraire les DOI uniques
jq -r '.message.items[] | select(
                                  ((.title[0] // "") | test("port-Hamiltonian"; "i")) or
                                  ((.abstract // "") | test("port-Hamiltonian"; "i"))
                                ) | .DOI' "$TMP_JSON" | sort -u > "$TMP_DOIS"

# Conserver uniquement les DOI non présents dans DOI.txt
comm -23 "$TMP_DOIS" <(sort "$DOI_SOURCE") >> "$DOI_FILE"

# On vérifie que les titres parlent bien de systèmes Hamiltoniens
while IFS= read -r doi; do
    # Échapper les slashs pour rechercher proprement dans le JSON
    title=$(jq -r --arg doi "$doi" '.message.items[] | select(.DOI == $doi) | .title[0]' "$TMP_JSON")
    printf "• %s\n  %s\n\n" "$doi: " "$title"
done < "$DOI_FILE"

# On va maintenant regarder dans notre database ce qu'il faut mettre à jour
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

# Boucle sur les DOI qui n'ont PAS d'entrées dans le biblio.json
while IFS= read -r doi; do
    if ! jq -e --arg DOI "$doi" '.[] | select(.doi == $DOI)' $BIBLIO_JSON > /dev/null; then
        echo -e "\t DOI still NOT in the database: $doi"
        echo "$doi" >> $DOI_FILE
        sed -i -e "\|$doi|Id" "$DOI_SOURCE"
    fi
done < $DOI_SOURCE

# Nettoyage
rm -f "$TMP_JSON" "$TMP_DOIS"
rm "$bibcurrent"

# Tout s'est bien passé !
echo $(date -Iseconds)" Search for update successful!"
exit 0

