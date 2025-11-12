#!/usr/bin/env bash
set -euo pipefail

# Les fonctions communes
if [ -f .utils ]; then
  source .utils
else
  printf '[X] %s\n' "Error: .utils file is missing!" >&2; exit 1;
fi

# Ce fichier utilise le .json créé par getData.sh pour générer (PAS AUTOMATIQUEMENT !) :
# * Un fichier .json qui liste le nom des auteurs et les variantes apparaissant dans les publis

# Fichiers d'entrée
BIBLIO_FILE="assets/data/biblio.json"
MAPPINGS_FILE="assets/data/author_mappings.json"

# Vérifier l'existence des fichiers
if [[ ! -f "$BIBLIO_FILE" ]]; then
  die "Erreur : fichier $BIBLIO_FILE introuvable."
fi

# Extraction des auteurs sous "Prénom Nom" exact depuis `_data/biblio.json`
AUTHORS=$(jq -r '.[] | .authors[]? | select(.family) | "\(.given) \(.family)"' "$BIBLIO_FILE" | sort -u)

if [[ ! -f "$MAPPINGS_FILE" ]]; then
  die "Erreur : fichier $MAPPINGS_FILE introuvable."
fi

declare -A author_to_slug
log $(date -Iseconds)" Loading author_mappings.json..."

# Charger `assets/data/author_mappings.json` en mémoire
while IFS= read -r entry; do
  slug=$(read_json "$entry" '.key')
  # Lire toutes les variations associées à ce slug
  while IFS= read -r variation; do
    author_to_slug["$(echo "$variation" | iconv -c -f UTF-8 -t UTF-8)"]="$slug"
  done < <(jq -r ".\"$slug\"[]" "$MAPPINGS_FILE")
done < <(jq -c 'to_entries[]' "$MAPPINGS_FILE")

log $(date -Iseconds)" Starting authors identification..."
sorted_pairs=()
k=0
# Vérification des correspondances
while IFS= read -r author; do
  found=false || :
  
  for known in "${!author_to_slug[@]}"; do
    if [[ "$author" == "$known" ]]; then
      log "$author → ${author_to_slug[$known]}"
      found=true
      break
    fi
  done

  if [[ "$found" == false ]]; then
    
    # Requête OpenAlex
    query=$(echo "$author" | sed 's/ /+/g')
    result=$(safe_curl "https://api.openalex.org/authors?search=$query&per-page=5")

    # Extraction de l’auteur avec le plus haut relevance_score
    best=$(read_json "$result" '.results | max_by(.relevance_score // 0) // empty')

    if [[ -n "$best" && "$best" != "null" ]]; then
      display=$(read_json "$best" '.display_name')
      slug=$(slugify "$display")
      to_add="  \"$slug\": [ \"$author\""
      if ! diff -q "$author" "$display" > /dev/null; then
        to_add+=", \"$display\""
      fi
      while IFS= read -r name; do
        to_add+=", \"$name\""
      done < <(echo "$best" | jq -c '.display_name_alternatives[]' 2>/dev/null)
      to_add+=" ]"
      last_name=$(echo "$display" | awk '{print $NF}')  # Extraire le dernier mot
    else
      slug=$(slugify "$author")
      to_add="  \"$slug\": [ \"$author\" ]"
      last_name=$(echo "$author" | awk '{print $NF}')  # Extraire le dernier mot
    fi
    
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
    
    log " Not found: $author"
    sorted_pairs+=("$normalized_last_name	$to_add")  # Tabulation pour séparer proprement
    (( k+=1 ))
  fi
done <<< "$AUTHORS"

# Trier les auteurs par leur dernier mot
IFS=$'\n' sorted_pairs=($(sort -u -k1 <<<"${sorted_pairs[*]}"))
unset IFS

log "! AFTER VERIFICATION ! Add or replace/complete in author_mappings.json:"

for pair in "${sorted_pairs[@]}"; do
  last_name=$(echo "$pair" | cut -f1)
  to_add=$(echo "$pair" | cut -f2-)
  echo ","
  echo "$to_add"
  echo ""
done

log "End: $k unknown entries."
exit 0

