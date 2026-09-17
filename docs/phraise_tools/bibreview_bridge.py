"""Temporary PHRAISE compatibility bridge for the BibReview migration.

This module projects BibReview's canonical in-memory objects onto the current
PHRAISE record and queue conventions. It deliberately performs no file I/O and
is kept on the migration branch so the historical workflow can be compared
before it is replaced.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Iterable

from bibreview.compat import legacy_record_to_publication
from bibreview.model import Author, Publication
from bibreview.pipeline.collect import CollectionResult
from bibreview.pipeline.merge import merge_publications


_REFERENCE_DOI_REPAIRS = {
    (
        '10.1080/01495739.2021.1917322',
        '10.1016/j.geomphys. 2021.104201',
    ): '10.1016/j.geomphys.2021.104201',
    (
        '10.1109/tpel.2020.3041653',
        '10.1007/978-1- 4471-0549-7',
    ): '10.1007/978-1-4471-0549-7',
}


def repair_legacy_reference_dois(records: Iterable[dict]) -> tuple[list[dict], int]:
    """Return a repaired copy of the two reviewed malformed PHRAISE references.

    This is an explicit project-data correction used only for the one-shot
    PHRAISE migration. BibReview's generic DOI normalization remains strict and
    must not silently remove embedded whitespace from arbitrary DOI strings.
    """
    repaired = deepcopy(list(records))
    count = 0
    for record in repaired:
        publication_doi = record.get('doi')
        references = record.get('references')
        if not isinstance(references, list):
            continue
        for reference in references:
            if not isinstance(reference, dict):
                continue
            current = reference.get('doi')
            replacement = _REFERENCE_DOI_REPAIRS.get((publication_doi, current))
            if replacement is not None:
                reference['doi'] = replacement
                count += 1
    return repaired, count


def _legacy_author(author: Author) -> dict:
    result = deepcopy(dict(author.source_fields))
    if author.given is not None:
        result['given'] = author.given
    if author.family is not None:
        result['family'] = author.family
    if author.literal is not None:
        result['name'] = author.literal
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


def rejected_dois_from_legacy_bytes(data: bytes) -> set[str]:
    """Reproduce PHRAISE's established badDOI parsing during migration.

    Only newline-terminated, non-empty, non-comment lines exclude bibliography
    records. The unusual unterminated-final-line rule is compatibility behavior,
    not a BibReview core contract.
    """
    return {
        line.decode('utf-8')
        for line in data.split(b'\n')[:-1]
        if line and not line.startswith(b'#')
    }


def _legacy_lines(data: bytes) -> list[bytes]:
    return data.removesuffix(b'\n').split(b'\n') if data else []


def legacy_queue_outputs(known: bytes, pending: bytes, rejected: bytes) -> tuple[bytes, bytes]:
    """Return PHRAISE-compatible DOI.txt and newDOI.txt output bytes.

    This intentionally preserves ordering, duplicates, comments, blank lines,
    and the historical distinction for an unterminated final rejected line.
    """
    rejected_lines = set(_legacy_lines(rejected))
    combined = known + pending
    cleaned = b''.join(
        line + b'\n'
        for line in _legacy_lines(combined)
        if line not in rejected_lines
    )
    return cleaned, b''


def merge_legacy_records(
    old_records: Iterable[dict],
    new_records: Iterable[dict],
    *,
    rejected_dois: Iterable[str] = (),
) -> list[dict]:
    """Merge current PHRAISE DOI-backed records through BibReview canonically.

    The migration bridge retains PHRAISE's historical first-record-wins behavior
    when an incoming DOI is already present, while BibReview's canonical merge
    itself remains capable of explicit metadata refreshes. PHRAISE's current
    bibliography is DOI-backed, so DOI-less legacy records are rejected here
    instead of reproducing the old ``None``-key collapse.
    """
    old = list(old_records)
    new = list(new_records)
    for record in old + new:
        if record.get('doi') in (None, ''):
            raise ValueError('PHRAISE merge compatibility requires DOI-backed records')

    existing = tuple(legacy_record_to_publication(record).publication for record in old)
    existing_dois = {publication.doi for publication in existing}
    incoming = tuple(
        legacy_record_to_publication(record).publication
        for record in new
        if str(record.get('doi')).strip().lower() not in existing_dois
    )
    merged = merge_publications(existing, incoming).publications
    rejected = set(rejected_dois)
    projected = [
        publication_to_legacy_record(publication)
        for publication in merged
        if publication.doi not in rejected
    ]
    return sorted(projected, key=lambda record: record['doi'])
