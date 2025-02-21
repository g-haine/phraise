---
layout: page
title: Search Publications
permalink: /search/
---

<input type="text" id="search-input" placeholder="Search by title, author, year, abstract, keyword, event, or journal..." onkeyup="searchPublications()">
<div id="search-results"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    fetch("{{ site.baseurl }}/assets/data/biblio.json")
        .then(response => response.json())
        .then(data => {
            window.publications = data;
            displayPublications(data); // Affichage initial
        })
        .catch(error => console.error("Error loading biblio.json:", error));
});

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
        const keywords = entry.keywords ? entry.keywords : "No keywords.";  // ✅ Fix keywords
        const event = entry.event ? entry.event : "No event.";
        const journal = entry.journal ? entry.journal : "No journal.";
        const permalink = entry.permalink ? `{{ site.baseurl }}/${entry.permalink}` : "#";

        const resultHTML = `
            <div class="publication">
                <h3><a href="${permalink}">${title}</a></h3>
                <p><strong>Authors:</strong> ${authors}</p>
                <p><strong>Year:</strong> ${year}</p>
                <p><strong>Journal:</strong> ${journal}</p>
                <p><strong>Abstract:</strong> ${abstract}</p>
                <p><strong>Keywords:</strong> ${keywords}</p>
                <p><strong>Event:</strong> ${event}</p>
            </div>
        `;
        resultsContainer.innerHTML += resultHTML;
    });
}

function searchPublications() {
    const query = document.getElementById("search-input").value.toLowerCase();
    const filteredData = window.publications.filter(entry => {
        const authors = entry.authors ? entry.authors.map(a => `${a.given} ${a.family}`).join(", ").toLowerCase() : "";
        const year = entry.year ? entry.year.toString() : "";
        const title = entry.title ? entry.title.toLowerCase() : "";
        const abstract = entry.abstract ? entry.abstract.toLowerCase() : "";
        const keywords = entry.keywords ? entry.keywords.toLowerCase() : "";  // ✅ Fix keywords
        const event = entry.event ? entry.event.toLowerCase() : "";
        const journal = entry.journal ? entry.journal.toLowerCase() : "";

        return (
            title.includes(query) || 
            authors.includes(query) || 
            year.includes(query) ||
            abstract.includes(query) ||
            keywords.includes(query) ||
            event.includes(query) ||
            journal.includes(query)
        );
    });

    displayPublications(filteredData);
}
</script>

