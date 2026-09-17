"""Temporary PHRAISE compatibility bridge for the BibReview migration.

This module converts BibReview's canonical in-memory collection result to the
legacy PHRAISE record shape. It deliberately performs no file I/O and is kept on
the migration branch so the historical workflow can be compared before it is
replaced.
"""
from __future__ import annotations

from copy import deepcopy

from bibreview.model import Author, Publication
from bibreview.pipeline.collect import CollectionResult


def _legacy_author(author: Author) -> dict:
    result = deepcopy(dict(author.source_fields))
    if author.given is not None:
        result['given'] = author.given
    if author.family is not None:
        result['family'] = author.family
    return result


def publication_to_legacy_record(publication: Publication) -> dict:
    """Project a canonical BibReview publication onto PHRAISE's current schema."""
    if publication.created_date is None:
        raise ValueError('PHRAISE compatibility output requires a creation date')

    authors = [_legacy_author(author) for author in publication.authors]
    references = [
        {
            'doi': reference.identifiers.get('doi') or 'null',
            'title': reference.citation,
        }
        for reference in publication.references
    ]
    created = publication.created_date
    return {
        'doi': publication.doi,
        'type': publication.type,
        'title': publication.title,
        'authors': authors or None,
        'abstract': publication.abstract,
        'journal': publication.container_title,
        'year': publication.publication_year,
        'volume': publication.volume,
        'issue': publication.issue,
        'event': publication.event,
        'isbn': publication.identifiers.get('isbn', ''),
        'pages': publication.pages,
        'publisher': publication.publisher,
        'keywords': ', '.join(publication.keywords),
        'dateY': str(created.year),
        'dateM': str(created.month),
        'dateD': str(created.day),
        'permalink': publication.permalink,
        'references': references,
    }


def collection_to_legacy_records(result: CollectionResult) -> list[dict]:
    """Return legacy records for a read-only BibReview collection result."""
    return [publication_to_legacy_record(item.publication) for item in result.items]
