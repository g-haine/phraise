#!/bin/bash

# Ce fichier prenant le .json créé par getData.sh en argument permet de générer :
# * Un fichier markdown par DOI qui permettra de poster la référence sur le site

# Fichier JSON source
BIBLIO_JSON="assets/data/biblio.json"

# Nettoyer les anciens fichiers
rm -f "_posts"/*.md

# Assurer la présence du fichier JSON
if [ ! -f "$BIBLIO_JSON" ]; then
    echo "Erreur : Fichier $BIBLIO_JSON introuvable !" >&2
    exit 1
fi

# Ajoute un zéro si le mois ou le jour est entre 1 et 9
pad_zero () {
    printf "%02d" "$1"
}

# Une fonctione qui récupère le bibtex depuis crossref
print_bib () {
    local doi=$1
    crossrefEndpoint="http://api.crossref.org/works/$doi/transform/application/x-bibtex"
    crossrefBib="$(curl -s $crossrefEndpoint)"
    if ! echo $crossrefBib | head -n 1 | grep -q "Resource" ; then
        bibtex="$(echo "$crossrefBib" \
        | sed -e 's/ @/@/g' \
        | sed -e 's/},/},\n /g' \
        | sed -e 's/, series/,\n  series/g' \
        | sed -e 's/, pages/,\n  pages/g' \
        | sed -e 's/, title/,\n  title/g' \
        | sed -e '/title/s/={/={{/g' \
        | sed -e '/title/s/},/}},/g' \
        | sed -e 's/ }/\n}/g' \
        | sed -e 's/, }/\n}/g' \
        | sed -e '/pages/s/–/--/g' \
        | sed -e '/month/d' \
        | sed -e '/url/d' \
        | tac | sed -e '2 s/,//g' | tac)"
        echo "$bibtex"
    fi
}

# Format the authors
format_authors () {
    authors=$(echo $1 | jq -r '[.[] | select(.family) | "\(.given) \(.family)"] | join(", ")')
    echo "$authors"
}

# Remplace les $ par les balises markdwon de mathjax
sed_abstract () {
    abstract=$(echo "$1" \
    | sed -e 's/<[^>]*>//g' \
    | sed -e 's/Abstract//g' \
    | sed -e 's/ABSTRACT//g' \
    | sed -e 's/\*/\\\*/g' \
    | awk '{
        in_math = 0;
        for (i=1; i<=length($0); i++) {
            c = substr($0, i, 1);
            if (c == "$") {
                if (in_math == 0) {
                    printf "\\\\( ";
                    in_math = 1;
                } else {
                    printf " \\\\)";
                    in_math = 0;
                }
            } else {
                printf "%s", c;
            }
        }
        printf "\n";
    }')
    
    echo "$abstract"
}

# Génération de fichiers Markdown pour chaque DOI (différencié selon le type, et avec cross-ref à l'intérieur du site)
create_markdown_post () {
    local doi=$1
    local data=$2
    date=$(echo "$data" | jq -r .dateY)-$(echo "$data" | jq -r .dateM)-$(echo "$data" | jq -r .dateD)
    local output_md="_posts/$date-$(echo "$data" | jq -r .permalink).md"

    echo "---" > "$output_md"
    echo "layout: post" >> "$output_md"
    title=$(echo "$data" | jq -r .title)
    echo "title: $title" >> "$output_md"
    echo "date: $(echo "$data" | jq -r .dateY)-$(echo "$data" | jq -r .dateM)-$(echo "$data" | jq -r .dateD) 00:00:00 +0100" >> "$output_md"
    echo "permalink: "$(slugify "$title") >> "$output_md"
    echo "year: $(echo "$data" | jq -r .year)" >> "$output_md"
    authors=$(echo "$data" | jq -r .authors 2>/dev/null)
    echo "authors: $(format_authors "$authors")" >> "$output_md"
    type_ref=$(echo "$data" | jq -r .type)
    echo "category: $type_ref" >> "$output_md"
    keywords=$(echo "$data" | jq -r .keywords)
    if [ -n "$keywords" ]; then
        echo "tag: $keywords" >> "$output_md"
    fi
    echo "---" >> "$output_md"
    echo " " >> "$output_md"

    echo "## Authors" >> "$output_md"
    echo "**$(format_authors "$authors")**" >> "$output_md"
    echo " " >> "$output_md"

    abstract=$(echo "$data" | jq -r .abstract)
    if [ "$abstract" != "No abstract available" ]; then
        echo "## Abstract" >> "$output_md"
        echo "$(sed_abstract "$abstract")" >> "$output_md"
        echo " " >> "$output_md"
    fi

    keywords=$(echo "$data" | jq -r .keywords)
    if [ -n "$keywords" ]; then
        echo "## Keywords" >> "$output_md"
        echo "$keywords" >> "$output_md"
        echo " " >> "$output_md"
    fi

    echo "## Citation" >> "$output_md"
    if echo $type_ref | grep -q "book"; then
        echo "- **ISBN:** $(echo "$data" | jq -r .isbn)" >> "$output_md"
    else
        echo "- **Journal:** $(echo "$data" | jq -r .journal)" >> "$output_md"
        echo "- **Year:** $(echo "$data" | jq -r .year)" >> "$output_md"
        echo "- **Volume:** $(echo "$data" | jq -r .volume)" >> "$output_md"
        echo "- **Issue:** $(echo "$data" | jq -r .issue)" >> "$output_md"
        echo "- **Pages:** $(echo "$data" | jq -r .pages)" >> "$output_md"
    fi
    echo "- **Publisher:** $(echo "$data" | jq -r .publisher)" >> "$output_md"
    echo "- **DOI:** [$doi](https://doi.org/$doi)" >> "$output_md"
    event=$(echo "$data" | jq -r .event)
    if [ -n "$event" ]; then
        echo "- **Note:** $event" >> "$output_md"
    fi
    echo " " >> "$output_md"
    
    echo "## BibTeX" >> "$output_md"
    echo "{% highlight bibtex %}" >> "$output_md"
    echo "{% raw %}" >> "$output_md"
    echo "$(print_bib "$doi")" >> "$output_md"
    echo "{% endraw %}" >> "$output_md"
    echo "{% endhighlight %}" >> "$output_md"
    echo " " >> "$output_md"
    
    # Chargement des noms de tous les markdown de biblio.json dans une table associative
    declare -A doi_keywords
    while IFS= read -r line; do
        key=$(echo "$line" | jq -r '.doi')
        value=$(echo "$line" | jq -r '.permalink // ""')
        doi_keywords["$key"]="$value"
    done < <(jq -c '.[]' "$BIBLIO_JSON")

    references=""
    references_json=$(echo "$data" | jq -c '.references' 2>/dev/null)
    while IFS= read -r ref; do
        title_ref=$(echo "$ref" | jq -r .title 2>/dev/null)
        doi_ref=$(echo "$ref" | jq -r .doi 2>/dev/null)
        if [ -n "$title_ref" ] && [ -n "$doi_ref" ]; then
            # Si DOI connu, appliquer le format markdown selon biblio.json
            if [[ " ${known_dois[@]} " =~ " $doi_ref " ]] && [ -n "${doi_keywords[$doi_ref]}" ]; then
                title_ref="[$title_ref](${doi_keywords[$doi_ref]})"
            fi
            references+="- $title_ref -- [$doi_ref](https://doi.org/$doi_ref)\\n"
        fi
        if [ -n "$title_ref" ] && [ -z "$doi_ref" ]; then
            references+="- $title_ref\\n"
        fi
        if [ -z "$title_ref" ] && [ -n "$doi_ref" ]; then
            references+="- [$doi_ref](https://doi.org/$doi_ref)\\n"
        fi
    done < <(echo "$references_json" | jq -c '.[]' 2>/dev/null)

    if [ -n "$references" ]; then
        echo "## References" >> "$output_md"
        echo -e "$references" >> "$output_md"
    fi
}

# Puis, la génération des posts en markdown

# Boucle à travers toutes les entrées du JSON et génère les posts
jq -c '.[]' "$BIBLIO_JSON" | while IFS= read -r entry; do
    doi=$(echo "$entry" | jq -r .doi)
    create_markdown_post "$doi" "$entry"
done

# Tout s'est bien passé !
echo "Posts générés avec succès !"
exit 0

