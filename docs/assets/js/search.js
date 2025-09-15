class PhraiseSearch {
    constructor() {
        this.worker = new Worker('../assets/js/search-worker.js');
        this.isDataLoaded = false;
        this.pendingQueries = [];
        
        this.worker.onmessage = (e) => {
            const { type, data } = e.data;
            
            if (type === 'dataLoaded') {
                this.isDataLoaded = true;
                document.getElementById('loading').style.display = 'none';
                document.getElementById('result-count').style.display = 'block';
                this.processPendingQueries();
                console.log('Data loaded');
            } else if (type === 'searchResults') {
                this.displayResults(data.results, data.query);
            } else if (type === 'error') {
                console.error('Error:', data);
                document.getElementById('loading').innerHTML = 'Data loading error';
            }
        };
        
        this.loadData();
    }

    async loadData() {
        try {
            const response = await fetch('../assets/data/biblio.json');
            if (!response.ok) throw new Error('HTTP error ' + response.status);
            
            const data = await response.json();
            
            this.worker.postMessage({
                type: 'loadData',
                data: data
            });
        } catch (error) {
            console.error('Loading error:', error);
            this.worker.postMessage({
                type: 'error',
                data: error.message
            });
        }
    }

    search(query) {
        const trimmedQuery = query.trim();
        if (!trimmedQuery || trimmedQuery.length < 2) {
            this.displayResults([], '');
            return;
        }

        if (!this.isDataLoaded) {
            this.pendingQueries.push(trimmedQuery);
            return;
        }

        this.worker.postMessage({
            type: 'search',
            query: trimmedQuery.toLowerCase(),
            limit: 50
        });
    }

    processPendingQueries() {
        while (this.pendingQueries.length > 0) {
            this.search(this.pendingQueries.shift());
        }
    }

    displayResults(results, query) {
        const resultsContainer = document.getElementById('search-results');
        if (!resultsContainer) return;


        // Mettre à jour le compteur de résultats
        const resultCount = document.getElementById('result-count');
        if (resultCount) {
            if (!query || query.length < 2) {
                resultCount.textContent = 'Please enter at least two caracters';
                return;
            }
            if (results.length === 0) {
                resultCount.textContent = 'No result found for "' + this.escapeHtml(query) + '"';
                return;
            } else {
                resultCount.textContent = `${results.length} matching item(s)`;
            }
        }

        resultsContainer.innerHTML = results.map(result => `
              <span class="post-meta">
                <h3><a class="post-link" href="../${result.permalink}">${this.highlightText(result.title, query)}</a></h3>
                
                ${result.authors.length > 0 ? `
                    <p><strong>Authors:</strong> ${this.highlightText(this.formatAuthors(result.authors), query)}</p>
                ` : ''}
                
                ${result.journal ? `<p><strong>Journal:</strong> ${this.highlightText(result.journal, query)}</p>` : ''}
                
                ${result.year ? `<p><strong>Year:</strong> ${result.year}</p>` : ''}
                
                ${result.abstract && result.abstract !== 'No  available' ? `
                    <p><strong>Abstract:</strong> ${this.highlightText(result.abstract, query)}</p>
                ` : ''}
                
                ${result.keywords && result.keywords !== '' ? `
                    <p><strong>Keywords:</strong> ${this.highlightText(result.keywords, query)}</p>
                ` : ''}
                
                ${result.doi ? `
                    <p><strong>DOI:</strong> 
                        <a href="https://doi.org/${result.doi}" target="_blank" class="doi-link">
                            ${result.doi}
                        </a>
                    </p>
                ` : ''}
        `).join('<hr />');
    }

    formatAuthors(authors) {
        return authors.map(author => {
            if (author.given && author.family) {
                return `${author.given} ${author.family}`;
            }
            return author.family || author.given || '';
        }).filter(name => name).join(', ');
    }

    highlightText(text, query) {
        if (!text || !query) return this.escapeHtml(text?.toString() || '');
        
        const escapedText = this.escapeHtml(text.toString());
        const regex = new RegExp(`(${this.escapeRegex(query)})`, 'gi');
        return escapedText.replace(regex, '<mark>$1</mark>');
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    truncateText(text, length) {
        if (text.length <= length) return text;
        return text.substring(0, length) + '...';
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', function() {
    const search = new PhraiseSearch();
    let timeout;

    const searchInput = document.getElementById('search-input');
    const resultCount = document.createElement('div');
    resultCount.id = 'result-count';
    resultCount.className = 'result-count';
    resultCount.textContent = 'Waiting for input...';
    resultCount.style.display = 'none';
    
    if (searchInput) {
        searchInput.parentNode.insertBefore(resultCount, searchInput.nextSibling);
        
        searchInput.addEventListener('input', function(e) {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                search.search(e.target.value);
            }, 300);
        });

        // Recherche aussi avec le bouton Entrée
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                clearTimeout(timeout);
                search.search(e.target.value);
            }
        });
    }
});
