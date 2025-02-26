---
layout: page
title: Search Publications
permalink: /search/
---

This search tool filters publications with your entries. Click "Search" to start.

<input type="text" id="search-input" placeholder="Search by title, author, year, abstract, keyword, event, journal, DOI...">
<button id="search-button">Search</button>
<div id="search-results"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    let publications = null; // Stocke les publications après chargement

    document.getElementById("search-button").addEventListener("click", function() {
        performSearch();
    });

    document.getElementById("search-input").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            performSearch();
        }
    });

    function performSearch() {
        const query = document.getElementById("search-input").value.toLowerCase().trim();
        const keywords = query.split(/\s+/); // Sépare la requête en mots-clés

        if (!publications) {
            // Charge le fichier JSON une seule fois
            fetch("{{ site.baseurl }}/assets/data/biblio.json")
                .then(response => response.json())
                .then(data => {
                    publications = data;
                    searchPublications(keywords, publications);
                })
                .catch(error => console.error("Error loading biblio.json:", error));
        } else {
            searchPublications(keywords, publications);
        }
    }

    function searchPublications(keywords, data) {
        const results = data.map(entry => {
            const fields = [
                entry.title ? entry.title.toLowerCase() : "",
                entry.authors ? entry.authors.map(a => `${a.given} ${a.family}`).join(", ").toLowerCase() : "",
                entry.year ? entry.year.toString() : "",
                entry.abstract ? entry.abstract.toLowerCase() : "",
                entry.keywords ? entry.keywords.toLowerCase() : "",
                entry.event ? entry.event.toLowerCase() : "",
                entry.journal ? entry.journal.toLowerCase() : "",
                entry.doi ? entry.doi.toString() : ""
            ];

            // Compte le nombre de mots-clés trouvés dans AU MOINS un champ
            let matchCount = keywords.reduce((count, keyword) => {
                return count + (fields.some(field => field.includes(keyword)) ? 1 : 0);
            }, 0);

            return matchCount > 0 ? { entry, score: matchCount } : null;
        }).filter(result => result !== null);

        // Trie les résultats par pertinence (score décroissant)
        results.sort((a, b) => b.score - a.score);

        displayPublications(results.map(r => r.entry));
    }

    function displayPublications(data) {
        const resultsContainer = document.getElementById("search-results");
        resultsContainer.innerHTML = "";

        if (data.length === 0) {
            resultsContainer.innerHTML = "<p>No results found.</p>";
            return;
        }

        data.forEach(entry => {
            const authors = entry.authors ? entry.authors.map(a => `${a.given} ${a.family}`).join(", ") : "Unknown Author";
            const year = entry.year ? entry.year : "Unknown Year";
            const title = entry.title ? entry.title : "Untitled";
            const abstract = entry.abstract ? entry.abstract : "No abstract available.";
            const keywords = entry.keywords ? entry.keywords : "No keywords.";
            const event = entry.event ? entry.event : "No event.";
            const journal = entry.journal ? entry.journal : "No journal.";
            const permalink = entry.permalink ? `{{ site.baseurl }}/${entry.permalink}` : "#";
            const doi = entry.doi ? entry.doi : "No DOI.";

            const resultHTML = `
                <div class="publication">
                    <h3><a href="${permalink}">${title}</a></h3>
                    <p><strong>Authors:</strong> ${authors}</p>
                    <p><strong>Year:</strong> ${year}</p>
                    <p><strong>Journal:</strong> ${journal}</p>
                    <p><strong>Abstract:</strong> ${abstract}</p>
                    <p><strong>Keywords:</strong> ${keywords}</p>
                    <p><strong>Event:</strong> ${event}</p>
                    <p><strong>DOI:</strong> ${doi}</p>
                </div>
            `;
            resultsContainer.innerHTML += resultHTML;
        });
    }
});
</script>

