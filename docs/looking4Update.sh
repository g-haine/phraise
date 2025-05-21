#!/bin/bash

# Ce script cherche :
#   * les nouveaux dois de openalex vérifiés dans crossref comportant "port-Hamiltonian" quelque part
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
DOI_BAD="badDOI.txt"

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

# On commence par une recherche d'update dans openalex & croisement avec crossref
echo $(date -Iseconds)" Looking in OpenAlex & verifying with CrossRef..."

# Interroger OpenAlex
TYPES_AUTORISES=("journal-article" "proceeding-article" "book-chapter" "book" "monograph")
QUERY="port-Hamiltonian"
CURSOR="*"
MAX_PAGES=20
PAGE_COUNT=0
TMP_DOIS_OA="openalex_all_dois.txt"
TMP_DIR="openalex_pages"
mkdir -p "$TMP_DIR"
> "$TMP_DOIS_OA"

while [[ "$CURSOR" != "null" && $PAGE_COUNT -lt $MAX_PAGES ]]; do
    echo $(date -Iseconds)" OpenAlex page $((PAGE_COUNT+1))..."
    OUT_FILE="$TMP_DIR/page_$PAGE_COUNT.json"

    curl -s "https://api.openalex.org/works?filter=title_and_abstract.search:${QUERY// /+}&per-page=200&sort=publication_date:desc&cursor=$CURSOR" -o "$OUT_FILE"

    # Extraire DOI + type
    jq -r '.results[] | .doi' "$OUT_FILE" >> "$TMP_DOIS_OA"

    # Obtenir le curseur pour la prochaine page
    CURSOR=$(jq -r '.meta.next_cursor' "$OUT_FILE")
    ((PAGE_COUNT++))
done
sed -i 's|^https://doi.org/||' "$TMP_DOIS_OA"
sed -i '/^[[:space:]]*$/d' "$TMP_DOIS_OA"
sed -i '/null/d' "$TMP_DOIS_OA"

# Les entrées doivent être unique dans le fichier & ne pas être dans DOI.txt
echo $(date -Iseconds)" Check unicity of DOIs..."
# S'assurer de ne pas rechercher de doublon
doi_file=$TMP_DOIS_OA
uniq_file=$(mktemp)
tmp_file=$(mktemp)
cat $doi_file | tr '[:upper:]' '[:lower:]' > $tmp_file
awk '!seen[$0]++' $tmp_file > $uniq_file
grep -avf "$DOI_SOURCE" "$uniq_file" | grep -avf "$DOI_BAD" > "$TMP_DOIS_OA"

# Pas de preprint ou de supplementary material
sed -i '/arxiv/d' $TMP_DOIS_OA
sed -i '/zenodo/d' $TMP_DOIS_OA

# Filtrer avec CrossRef pour s'assurer du type et que "port-Hamiltonian" est dans titre/abstract
echo $(date -Iseconds)" CrossRef verification..."
k=0
while IFS= read -r doi; do
    # Appel CrossRef
    response=$(fetch_metadata_crossref "$doi")
    status=$(echo "$response" | jq -r '.status')

    if [[ "$status" == "ok" ]]; then
        title=$(echo "$response" | jq -r '.message.title // [""] | .[0]' | sed -E 's/<[^>]*mml[^>]*>//g' | sed -E 's/"/\\"/g')
        abstract=$(echo "$response" | jq -r '.message.abstract // ""')
        type=$(echo "$response" | jq -r '.message.type // ""')
        
        # Complement pour l'abstract
        if [ -z "$abstract" ]; then
            complement=$(fetch_abstract_complement $doi)
            [ -n "$complement" ] && abstract="$complement"
        fi

        # Vérifie le type
        if [[ " ${TYPES_AUTORISES[*]} " =~ " ${type} " ]]; then
            # Vérifie si "port-Hamiltonian" est présent dans le titre ou l'abstract
            if echo "$title $abstract" | grep -iq "port-Hamiltonian"; then
                k=$(( $k + 1 ))
                echo -e "\t DOI $k to fetch on CrossRef: $doi"
                echo "$doi" >> "$DOI_FILE"
            elif echo "$title $abstract" | grep -iq "port-controlled Hamiltonian"; then
                k=$(( $k + 1 ))
                echo -e "\t DOI $k to fetch on CrossRef: $doi"
                echo "$doi" >> "$DOI_FILE"
            else
                echo -e "\t Forget DOI, not port-Hamiltonian: $doi"
                echo "$doi" >> "$DOI_BAD"
            fi
        else
            echo -e "\t Forget DOI, not the good type: $doi"
            echo "$doi" >> "$DOI_BAD"
        fi
    else
        echo -e "\t Forget DOI, not in CrossRef: $doi"
    fi
done < "$TMP_DOIS_OA"

# On va maintenant regarder dans notre database ce qu'il faut mettre à jour
echo $(date -Iseconds)" Identification of incomplete publications starts..."

# On prépare une poubelle
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
echo $(date -Iseconds)" Identification of DOI not in the database..."
while IFS= read -r doi; do
    if ! jq -e --arg DOI "$doi" '.[] | select(.doi == $DOI)' $BIBLIO_JSON > /dev/null; then
        echo -e "\t DOI still NOT in the database: $doi"
        echo "$doi" >> $DOI_FILE
        sed -i -e "\|$doi|Id" "$DOI_SOURCE"
    fi
done < $DOI_SOURCE

# Nettoyage
rm -f "$TMP_DOIS_OA" "$bibcurrent"
rm -rf "$TMP_DIR"

# Tout s'est bien passé !
echo $(date -Iseconds)" Search for update successful!"
exit 0

