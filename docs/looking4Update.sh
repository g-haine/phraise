#!/usr/bin/env bash
set -euo pipefail

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

# Fichier DOI source
DOI_SOURCE="DOI.txt"

# Fichier JSON source
BIBLIO_JSON="assets/data/biblio.json"

# Fichier de sortie des DOI à mettre à jour
DOI_FILE="newDOI.txt"
DOI_BAD="badDOI.txt"
DOI_TO_CHECK="checkDOI.txt"

# La "poubelle" (on supprimera à la main si tout va bien)
TRASH_DIR="trash/"
TRASH_JSON="trash.json"

# Les fonctions communes
if [ -f .utils ]; then
  source .utils
else
  die "Error: .env file is missing!"
fi

# On commence par une recherche d'update dans openalex & croisement avec crossref
echo $(date -Iseconds)" Looking in OpenAlex & verifying with CrossRef..."

# Liste de motifs PHS (PCRE)
PHS_PATTERNS=(
    'port[\p{Pd}\s]+(controlled )?hamiltonian'  # pHs
    'interconnection and damping assignment'    # IDA-PBC
    'dirac structure'                           # classique
    'dissipative hamiltonian'                   # J-R
)
# PCRE, insensible à la casse avec -Pi
PHS_PATTERN="$(printf '%s|' "${PHS_PATTERNS[@]}" | sed 's/|$//')"

# Interroger OpenAlex
TYPES_AUTORISES=("journal-article" "proceedings-article" "book-chapter" "book" "monograph")
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
    (( ++PAGE_COUNT )) || :
done
sed -i 's|^https://doi.org/||' "$TMP_DOIS_OA"
sed -i '/^[[:space:]]*$/d' "$TMP_DOIS_OA"
sed -i '/null/d' "$TMP_DOIS_OA"

# Les entrées doivent être unique dans le fichier & ne pas être dans DOI.txt
echo $(date -Iseconds)" Check unicity of DOIs..."
# S'assurer de ne pas rechercher de doublon
sort -u -o "$DOI_BAD" "$DOI_BAD"
doi_file="$TMP_DOIS_OA"
uniq_file=$(mktemp)
tmp_file=$(mktemp)
cat "$doi_file" | tr '[:upper:]' '[:lower:]' > "$tmp_file"
awk '!seen[$0]++' "$tmp_file" > "$uniq_file"
grep -vFxf "$DOI_SOURCE" "$uniq_file" | grep -vFxf "$DOI_BAD" > "$TMP_DOIS_OA"

# Pas de preprint ou de supplementary material
sed -i '/arxiv/d' "$TMP_DOIS_OA"
sed -i '/zenodo/d' "$TMP_DOIS_OA"

# Filtrer avec CrossRef pour s'assurer du type et que "port-Hamiltonian" est dans titre/abstract
echo $(date -Iseconds)" CrossRef verification..."
k=0
while IFS= read -r doi; do
    # Appel CrossRef
    response=$(fetch_metadata_crossref "$doi")
    status=$(echo "$response" | jq -r '.status')

    if [[ "$status" == "ok" ]]; then
        type=$(echo "$response" | jq -r '.message.type // ""')
        title=$(echo "$response" | jq -r '.message.title // [""] | .[0]' | sed -E 's/<[^>]*mml[^>]*>//g' | sed -E 's/"/\\"/g')
        abstract=$(echo "$response" | jq -r '.message.abstract // ""')
        keywords=$(echo "$response" | jq -r '.message.subject // [] | join(", ")')
        
        # Récupère l'url "final" (avant redirection js) à partir du DOI
        url=$(curl -Ls -o /dev/null -w "%{url_effective}" "https://doi.org/$doi")
        
        # Update si elsevier
        if echo "$url" | grep -q "elsevier"; then
            json_scopus=$(fetch_metadata_scopus "$doi")
            abstract+=$(abstract_from_scopus "$json_scopus")
            keywords+=", "$(keywords_from_scopus "$json_scopus")
        fi
        
        # Update si springer
        if echo "$url" | grep -q "springer"; then
            json_springer=$(fetch_metadata_springer "$doi")
            abstract+=$(abstract_from_springer "$json_springer")
            keywords+=", "$(keywords_from_springer "$json_springer")
        fi
        
        # Update si ieee
        if echo "$url" | grep -q "ieee"; then
            json_ieee=$(fetch_metadata_ieee "$doi")
            abstract+=$(abstract_from_ieee "$json_ieee")
            keywords+=", "$(keywords_from_ieee "$json_ieee")
        fi
        
        # Complement pour l'abstract
        if [ -z "$abstract" ]; then
            complement=$(fetch_abstract_complement "$doi")
            [ -n "$complement" ] && abstract="$complement"
        fi
        
        # Nettoyage de l'abstract
        abstract=$(echo "$abstract" | tr -d '\000-\031' | sed -E 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed -E 's/\\/\\\\/g' | sed -E 's/"/\\"/g' | sed -E 's/<[^>]*jats[^>]*>//g' | sed -E 's/summary//Ig' | sed -E 's/abstract//Ig')
        
        # Vérifie le type
        if [[ " ${TYPES_AUTORISES[*]} " =~ " ${type} " ]]; then
            # Vérifie si "port-Hamiltonian" est présent dans le titre ou l'abstract, ou encore les keywords
            if echo "$title $abstract $keywords" | grep -Piq "$PHS_PATTERN"; then
                k=$(( k + 1 ))
                echo -e "\t DOI $k to fetch on CrossRef: $doi"
                echo "$doi" >> "$DOI_FILE"
            else
                echo -e "\t Please check, seems not port-Hamiltonian: $doi"
                echo "$doi" >> "$DOI_TO_CHECK"
            fi
        else
            echo -e "\t Forget, not the good type: $doi"
            echo "$doi" >> "$DOI_BAD"
        fi
    else
        echo -e "\t Forget, not in CrossRef: $doi"
        echo "$doi" >> "$DOI_BAD"
    fi
done < "$TMP_DOIS_OA"
grep -vFxf "$DOI_BAD" "$DOI_TO_CHECK" > check.tmp && mv check.tmp "$DOI_TO_CHECK"

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
    # Quand le DOI exists, mais que le bibtex n'a pas pu être fabriquer précédemment
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
    
done < <(jq -c '.[] | select(.type == "journal-article" and (.volume == "" or .issue == "" or .pages == ""))' "$BIBLIO_JSON")

sed -i -z -e "s/]\n\[/,/g" $trash
tmp_file=$(mktemp)
jq --indent 2 . $trash > $tmp_file
mv $tmp_file $trash

while IFS= read -r line; do
    doi=$(echo "$line" | jq -r '.doi')
    tmp_file=$(mktemp)
    jq --arg DOI "$doi" '[.[] | select(.doi != $DOI)]' "$BIBLIO_JSON" > tmp_file && mv tmp_file "$BIBLIO_JSON"
done < <(jq -c '.[]' "$trash")

# Cherche les DOI qui n'ont PAS encore d'entrées dans le biblio.json
echo $(date -Iseconds)" Identification of DOI not in the database..."

# Extraire les DOI du JSON (en minuscules pour plus de robustesse)
jq -r '.[].doi' "$BIBLIO_JSON" | tr '[:upper:]' '[:lower:]' | sort -u > dois_in_db.tmp

# Normaliser et trier la source
tr '[:upper:]' '[:lower:]' < "$DOI_SOURCE" | sort -u > dois_in_source.tmp

# Comparer : ne garder que ceux qui ne sont PAS dans la base
comm -23 dois_in_source.tmp dois_in_db.tmp > dois_missing.tmp

# Affichage et ajout dans $DOI_FILE
while IFS= read -r doi; do
    echo -e "\t DOI still NOT in the database: $doi"
    echo "$doi" >> "$DOI_FILE"
    sed -i -e "\|$doi|Id" "$DOI_SOURCE"
done < dois_missing.tmp

# Nettoyage
rm -f *.tmp "$TMP_DOIS_OA" "$bibcurrent"
rm -rf "$TMP_DIR"

# Unification des DOIs
echo $(date -Iseconds)" Check unicity of DOIs..."
uniq_file="DOIuniq.txt"
tmp_file=$(mktemp)
cat $DOI_FILE | tr '[:upper:]' '[:lower:]' > $tmp_file
awk '!seen[$0]++' $tmp_file > $uniq_file
grep -vFxf DOI.txt "$uniq_file" > "$DOI_FILE"
rm "$uniq_file"
cat "$DOI_FILE"

# Tout s'est bien passé !
echo $(date -Iseconds)" Search for update successful!"
exit 0

