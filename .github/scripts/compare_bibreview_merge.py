#!/usr/bin/env python3
"""Offline comparison of PHRAISE concatenation with BibReview merge/storage."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile

DOCS = Path(__file__).resolve().parents[2] / 'docs'
sys.path.insert(0, str(DOCS))

spec = importlib.util.spec_from_file_location('concatenate', DOCS / 'concatenate.py')
concatenate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(concatenate)

from bibreview.compat import legacy_record_to_publication
from bibreview.identity import new_publication_id
from bibreview.model import Publication
from bibreview.pipeline.merge import merge_publications
from bibreview.storage import read_bibliography, write_bibliography
from phraise_tools.bibreview_bridge import publication_to_legacy_record


def legacy_record(doi: str, title: str, slug: str) -> dict:
    return {
        'doi': doi,
        'type': 'journal-article',
        'title': title,
        'authors': [{'given': 'Ada', 'family': 'Lovelace'}],
        'abstract': 'Abstract',
        'journal': 'Journal',
        'year': '2026',
        'volume': '1',
        'issue': '2',
        'event': '',
        'isbn': '',
        'pages': '1--9',
        'publisher': 'Publisher',
        'keywords': 'control, energy',
        'dateY': '2026',
        'dateM': '9',
        'dateD': '17',
        'permalink': slug,
        'references': [],
    }


def canonical(records: list[dict]) -> tuple[Publication, ...]:
    return tuple(legacy_record_to_publication(record).publication for record in records)


def by_doi(records: list[dict]) -> dict[str, dict]:
    return {record['doi']: record for record in records}


def compare_doi_backed_merge() -> tuple[Publication, ...]:
    old = [
        legacy_record('10.1/z', 'Z', 'z'),
        legacy_record('10.1/a', 'A', 'a'),
    ]
    new = [legacy_record('10.1/b', 'B', 'b')]

    historical = concatenate.merge_bibliographies(old, new)
    result = merge_publications(canonical(old), canonical(new))
    projected = [publication_to_legacy_record(publication) for publication in result.publications]

    if by_doi(projected) != by_doi(historical):
        raise AssertionError('BibReview DOI-backed merge differs from PHRAISE content')
    if [publication.doi for publication in result.publications] != ['10.1/z', '10.1/a', '10.1/b']:
        raise AssertionError('BibReview did not preserve existing order and append incoming publications')
    return result.publications


def compare_refresh_identity() -> None:
    existing = legacy_record_to_publication(
        legacy_record('10.1/item', 'Old title', 'item')
    ).publication
    incoming = Publication(
        id=new_publication_id(),
        identifiers={'doi': '10.1/item'},
        type=existing.type,
        title='Corrected title',
        authors=existing.authors,
        abstract=existing.abstract,
        container_title=existing.container_title,
        publication_year=existing.publication_year,
        volume=existing.volume,
        issue=existing.issue,
        pages=existing.pages,
        publisher=existing.publisher,
        event=existing.event,
        keywords=existing.keywords,
        created_date=existing.created_date,
        permalink=existing.permalink,
        references=existing.references,
    )
    merged = merge_publications([existing], [incoming]).publications
    if len(merged) != 1 or merged[0].id != existing.id or merged[0].title != 'Corrected title':
        raise AssertionError('BibReview metadata refresh did not preserve the persisted UUID')


def compare_doi_less_behavior() -> None:
    historical = concatenate.merge_bibliographies(
        [{'doi': None, 'title': 'One'}],
        [{'doi': None, 'title': 'Two'}],
    )
    first = Publication(id=new_publication_id(), title='One')
    second = Publication(id=new_publication_id(), title='Two')
    canonical_result = merge_publications([first], [second]).publications

    if len(historical) != 1:
        raise AssertionError('historical DOI-less fixture no longer exposes the expected legacy collapse')
    if canonical_result != (first, second):
        raise AssertionError('BibReview collapsed distinct DOI-less publications')


def compare_canonical_storage(publications: tuple[Publication, ...]) -> None:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'bibliography.json'
        write_bibliography(path, publications)
        loaded = read_bibliography(path)
        if loaded != publications:
            raise AssertionError('canonical BibReview bibliography storage is not lossless')
        if not path.read_bytes().endswith(b'\n'):
            raise AssertionError('canonical bibliography is not written in the expected readable format')


def main() -> int:
    publications = compare_doi_backed_merge()
    compare_refresh_identity()
    compare_doi_less_behavior()
    compare_canonical_storage(publications)
    print('PHRAISE DOI-backed concatenate vs BibReview merge: equivalent content')
    print('BibReview persisted UUID on metadata refresh: preserved')
    print('DOI-less legacy collapse: detected and intentionally not reproduced')
    print('canonical bibliography write/read round-trip: exact')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
