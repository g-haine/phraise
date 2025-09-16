class PhraiseSearch {
    constructor() {
        this.worker = new Worker('../assets/js/search-worker.js');
        this.isDataLoaded = false;
        this.pendingQueries = [];
        this.cacheKey = 'phraise_biblio_cache';
        this.cacheVersion = '1.0';
        this.useCache = true; // Flag pour contrôler l'usage du cache
        this.localData = null; // Stockage en mémoire pour fallback
        
        this.worker.onmessage = (e) => {
            const { type, data } = e.data;
            
            if (type === 'dataLoaded') {
                this.isDataLoaded = true;
                document.getElementById('loading').style.display = 'none';
                document.getElementById('result-count').style.display = 'block';
                this.processPendingQueries();
                console.log('Data loaded successfully');
            } else if (type === 'searchResults') {
                this.displayResults(data.results, data.query);
            } else if (type === 'error') {
                console.error('Worker error:', data);
                this.showError('Search error. Please try again.');
            }
        };
        
        // Vérifier si localStorage est disponible
        this.checkLocalStorageAvailability();
        this.loadDataWithCache();
    }

    checkLocalStorageAvailability() {
        try {
            const test = 'test';
            localStorage.setItem(test, test);
            localStorage.removeItem(test);
            this.useCache = true;
        } catch (e) {
            console.warn('LocalStorage not available, disabling cache');
            this.useCache = false;
        }
    }

    async loadDataWithCache() {
        try {
            // Essayer le cache si disponible
            if (this.useCache) {
                const cachedData = this.getCachedData();
                if (cachedData) {
                    console.log('Using cached database');
                    this.localData = cachedData.data; // Sauvegarde pour fallback
                    this.worker.postMessage({
                        type: 'loadData',
                        data: cachedData.data
                    });
                    return;
                }
            }

            // Charger depuis le serveur
            await this.loadFromServer();
            
        } catch (error) {
            console.error('Loading error:', error);
            this.showError('Unable to load database. Please refresh the page.');
        }
    }

    async loadFromServer() {
        try {
            const response = await fetch('../assets/data/biblio.json', {
                headers: { 'Cache-Control': 'no-cache' }
            });
            
            if (!response.ok) throw new Error('HTTP error ' + response.status);
            
            const data = await response.json();
            this.localData = data; // Toujours stocker en mémoire
            
            // Sauvegarder en cache seulement si possible
            if (this.useCache) {
                try {
                    const etag = response.headers.get('ETag') || this.generateHash(JSON.stringify(data));
                    this.saveToCache(data, etag);
                } catch (cacheError) {
                    console.warn('Cache save failed, continuing without cache:', cacheError);
                    this.useCache = false; // Désactiver le cache après erreur
                }
            }
            
            this.worker.postMessage({
                type: 'loadData',
                data: data
            });
            
        } catch (error) {
            console.error('Server loading failed:', error);
            throw error;
        }
    }

    getCachedData() {
        if (!this.useCache) return null;
        
        try {
            const cache = localStorage.getItem(this.cacheKey);
            if (!cache) return null;
            
            const parsed = JSON.parse(cache);
            
            // Vérifier la version et l'âge du cache (30 jours max)
            if (parsed.version !== this.cacheVersion) return null;
            if (Date.now() - parsed.timestamp > 30 * 24 * 60 * 60 * 1000) return null;
            
            console.log('Cache found and valid');
            return parsed;
        } catch (e) {
            console.warn('Cache reading error, disabling cache:', e);
            this.useCache = false;
            return null;
        }
    }

    saveToCache(data, etag) {
        if (!this.useCache) return;
        
        try {
            const cacheData = {
                data: data,
                etag: etag,
                timestamp: Date.now(),
                version: this.cacheVersion
            };
            
            localStorage.setItem(this.cacheKey, JSON.stringify(cacheData));
            console.log('Database saved in cache');
            
        } catch (e) {
            if (e.name === 'QuotaExceededError') {
                console.warn('Storage quota exceeded, clearing old data...');
                this.clearOldCache();
                
                // Réessayer une fois
                try {
                    const cacheData = {
                        data: data,
                        etag: etag,
                        timestamp: Date.now(),
                        version: this.cacheVersion
                    };
                    localStorage.setItem(this.cacheKey, JSON.stringify(cacheData));
                    console.log('Cache saved after cleanup');
                } catch (e2) {
                    console.warn('Still unable to save cache, disabling:', e2);
                    this.useCache = false;
                }
            } else {
                console.warn('Cache save error, disabling cache:', e);
                this.useCache = false;
            }
        }
    }

    clearOldCache() {
        // Nettoyer seulement les vieux caches similaires
        const prefix = 'phraise_';
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key && key.startsWith(prefix) && key !== this.cacheKey) {
                try {
                    localStorage.removeItem(key);
                } catch (e) {
                    console.warn('Could not remove item:', key, e);
                }
            }
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
            this.showWarning('Database still loading...');
            return;
        }

        // Timeout pour fallback si worker ne répond pas
        const fallbackTimeout = setTimeout(() => {
            if (this.localData) {
                console.warn('Worker timeout, using direct search');
                this.searchDirect(trimmedQuery);
            }
        }, 5000);

        this.worker.postMessage({
            type: 'search',
            query: trimmedQuery.toLowerCase(),
            limit: 50
        });

        // Annuler le timeout si le worker répond
        setTimeout(() => clearTimeout(fallbackTimeout), 4000);
    }

    // Fallback de recherche directe
    searchDirect(query) {
        if (!this.localData) {
            this.showError('No data available for search');
            return;
        }

        try {
            const results = this.performDirectSearch(query, this.localData);
            this.displayResults(results, query);
        } catch (error) {
            console.error('Direct search error:', error);
            this.showError('Search failed. Please try again.');
        }
    }

    performDirectSearch(query, data) {
        const queryTerms = query.toLowerCase().split(/\s+/).filter(term => term.length > 1);
        const results = [];

        for (const item of data) {
            const score = this.calculateItemScore(item, queryTerms);
            if (score > 0) {
                results.push({ ...item, score });
            }
        }

        return results.sort((a, b) => b.score - a.score).slice(0, 50);
    }

    calculateItemScore(item, queryTerms) {
        let score = 0;
        const searchText = this.createSearchableText(item).toLowerCase();

        for (const term of queryTerms) {
            const occurrences = (searchText.match(new RegExp(term, 'g')) || []).length;
            score += occurrences * term.length;

            if (item.title?.toLowerCase().includes(term)) score += 20;
            if (this.checkAuthors(item.authors, term)) score += 15;
            if (item.keywords?.toLowerCase().includes(term)) score += 25;
            if (item.doi?.toLowerCase() === term) score += 50;
        }

        return score;
    }

    checkAuthors(authors, term) {
        return authors?.some(author => 
            author.family?.toLowerCase().includes(term) || 
            author.given?.toLowerCase().includes(term)
        );
    }

    createSearchableText(item) {
        const fields = [
            item.title,
            item.journal,
            item.abstract,
            item.keywords,
            item.year?.toString(),
            item.doi,
            ...(item.authors?.map(author => `${author.given} ${author.family}`) || [])
        ];
        
        return fields.filter(Boolean).join(' ');
    }

    processPendingQueries() {
        while (this.pendingQueries.length > 0) {
            this.search(this.pendingQueries.shift());
        }
    }

    showError(message) {
        const errorDiv = document.getElementById('error-message') || this.createMessageDiv('error');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
        
        // Cacher après 5 secondes
        setTimeout(() => {
            errorDiv.style.display = 'none';
        }, 5000);
    }

    showWarning(message) {
        const warningDiv = document.getElementById('warning-message') || this.createMessageDiv('warning');
        warningDiv.textContent = message;
        warningDiv.style.display = 'block';
    }

    createMessageDiv(type) {
        const div = document.createElement('div');
        div.id = `${type}-message`;
        div.className = `message ${type}-message`;
        document.getElementById('search-container').prepend(div);
        return div;
    }

    generateHash(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            hash = ((hash << 5) - hash) + str.charCodeAt(i);
            hash |= 0;
        }
        return hash.toString();
    }

    displayResults(results, query) {
        const resultsContainer = document.getElementById('search-results');
        if (!resultsContainer) return;

        // Cacher les messages
        this.hideMessages();

        const resultCount = document.getElementById('result-count');
        if (resultCount) {
            if (!query || query.length < 2) {
                resultCount.textContent = 'Please enter at least two characters';
                resultsContainer.innerHTML = '';
                return;
            }
            if (results.length === 0) {
                resultCount.textContent = 'No result found for "' + this.escapeHtml(query) + '"';
                resultsContainer.innerHTML = '';
                return;
            } else {
                resultCount.textContent = `${results.length} matching item(s)`;
                if (results.length === 50) {
                    resultCount.textContent += ` (limited to 50 results)`;
                }
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
                </span>
            <hr />
        `).join('');
    }

    hideMessages() {
        ['error', 'warning'].forEach(type => {
            const element = document.getElementById(`${type}-message`);
            if (element) element.style.display = 'none';
        });
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
        const searchContainer = searchInput.parentNode;
        searchContainer.insertBefore(resultCount, searchInput.nextSibling);
        
        searchInput.addEventListener('input', function(e) {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                search.search(e.target.value);
            }, 300);
        });

        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                clearTimeout(timeout);
                search.search(e.target.value);
            }
        });
    }
});
