let searchData = [];
let searchIndex = [];

self.onmessage = function(e) {
    const { type, data, query, limit } = e.data;

    try {
        switch (type) {
            case 'loadData':
                processData(data);
                break;
                
            case 'search':
                const results = performSearch(query, limit);
                self.postMessage({
                    type: 'searchResults',
                    data: {
                        results: results,
                        query: query,
                        total: results.length
                    }
                });
                break;
                
            case 'error':
                console.error('Error in worker:', data);
                break;
        }
    } catch (error) {
        self.postMessage({
            type: 'error',
            data: error.message
        });
    }
};

function processData(data) {
    searchData = data;
    
    // Créer un index de recherche optimisé spécifique à votre structure
    searchIndex = data.map((item, index) => ({
        id: index,
        searchableText: createSearchableText(item),
        item: item
    }));
    
    self.postMessage({ type: 'dataLoaded' });
}

function createSearchableText(item) {
    // Concaténer tous les champs pertinents pour la recherche
    const fields = [
        item.title,
        item.journal,
        item.abstract,
        item.keywords,
        item.year?.toString(),
        item.doi,
        ...(item.authors?.map(author => 
            `${author.given} ${author.family}`.toLowerCase()
        ) || [])
    ];
    
    return fields.filter(Boolean).join(' ').toLowerCase();
}

function performSearch(query, limit = 50) {
    if (!query || query.length < 2) {
        return [];
    }

    const results = [];
    const queryTerms = query.split(/\s+/).filter(term => term.length > 1);
    
    for (const indexedItem of searchIndex) {
        const score = calculateRelevanceScore(indexedItem.searchableText, queryTerms, indexedItem.item);
        
        if (score > 0) {
            results.push({
                ...indexedItem.item,
                score: score
            });
        }
    }
    
    // Trier par pertinence et limiter les résultats
    return results
        .sort((a, b) => b.score - a.score)
        .slice(0, limit);
}

function calculateRelevanceScore(text, queryTerms, item) {
    let score = 0;
    
    for (const term of queryTerms) {
        const occurrences = (text.match(new RegExp(term, 'g')) || []).length;
        score += occurrences * term.length;
        
        // Bonus pour les correspondances dans le titre
        if (item.title && item.title.toLowerCase().includes(term)) {
            score += 20;
        }
        
        // Bonus pour les correspondances dans les auteurs
        if (item.authors && item.authors.some(author => 
            author.family?.toLowerCase().includes(term) || 
            author.given?.toLowerCase().includes(term)
        )) {
            score += 15;
        }
        
        // Bonus pour le DOI exact
        if (item.doi && item.doi.toLowerCase() === term) {
            score += 50;
        }
        
        // Bonus pour les mots-clés
        if (item.keywords && item.keywords.toLowerCase().includes(term)) {
            score += 25; // Fort bonus pour les mots-clés
        }
    }
    
    return score;
}
