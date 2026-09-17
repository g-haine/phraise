#!/usr/bin/env python3
"""Offline comparison of PHRAISE concatenation with BibReview merge/storage."""
from __future__ import annotations

import importlib.util
import json
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
from bibreview.storage import atomic_write_batch, json_bytes, read_bibliography, write_bibliography
from phraise_tools.bibreview_bridge import (
    legacy_queue_outputs,
    merge_legacy_records,
    publication_to_legacy_record,
    rejected_dois_from_legacy_bytes,
)


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


def _legacy_state_fixture(root: Path) -> tuple[list[dict], list[dict], bytes, bytes, bytes]:
    data = root / 'assets/data'
    data.mkdir(parents=True)
    old = [
        legacy_record('10.1/z', 'Z', 'z'),
        legacy_record('10.1/a', 'A', 'a'),
    ]
    new = [
        legacy_record('10.1/b', 'B', 'b'),
        legacy_record('10.1/bad', 'Bad', 'bad'),
        legacy_record('10.1/a', 'Should not replace old A', 'a-new'),
    ]
    known = b'10.1/z\n10.1/a\n#comment\n\n10.1/bad\n'
    pending = b'10.1/b\n10.1/a\n'
    rejected = b'#comment\n\n10.1/bad\n'

    (root / 'DOI.txt').write_bytes(known)
    (root / 'newDOI.txt').write_bytes(pending)
    (root / 'badDOI.txt').write_bytes(rejected)
    (data / 'biblio.json').write_bytes(json_bytes(new))
    (data / 'biblio-reference.json').write_bytes(json_bytes(old))
    return old, new, known, pending, rejected


def compare_full_legacy_state() -> None:
    with tempfile.TemporaryDirectory() as historical_dir, tempfile.TemporaryDirectory() as bibreview_dir:
        historical_root = Path(historical_dir)
        old, new, known, pending, rejected = _legacy_state_fixture(historical_root)
        concatenate.concatenate(
            historical_root / 'DOI.txt',
            historical_root / 'newDOI.txt',
            historical_root / 'badDOI.txt',
            historical_root / 'assets/data/biblio.json',
            historical_root / 'assets/data',
        )
        expected = {
            'biblio': (historical_root / 'assets/data/biblio.json').read_bytes(),
            'known': (historical_root / 'DOI.txt').read_bytes(),
            'pending': (historical_root / 'newDOI.txt').read_bytes(),
        }

        bibreview_root = Path(bibreview_dir)
        (bibreview_root / 'assets/data').mkdir(parents=True)
        (bibreview_root / 'DOI.txt').write_bytes(known)
        (bibreview_root / 'newDOI.txt').write_bytes(pending)
        (bibreview_root / 'badDOI.txt').write_bytes(rejected)
        (bibreview_root / 'assets/data/biblio.json').write_bytes(json_bytes(new))

        before = {
            path: path.read_bytes()
            for path in (
                bibreview_root / 'DOI.txt',
                bibreview_root / 'newDOI.txt',
                bibreview_root / 'badDOI.txt',
                bibreview_root / 'assets/data/biblio.json',
            )
        }
        rejected_dois = rejected_dois_from_legacy_bytes(rejected)
        merged_records = merge_legacy_records(old, new, rejected_dois=rejected_dois)
        known_output, pending_output = legacy_queue_outputs(known, pending, rejected)

        if any(path.read_bytes() != content for path, content in before.items()):
            raise AssertionError('planning PHRAISE compatibility outputs mutated files')

        atomic_write_batch({
            bibreview_root / 'assets/data/biblio.json': json_bytes(merged_records),
            bibreview_root / 'DOI.txt': known_output,
            bibreview_root / 'newDOI.txt': pending_output,
        })
        actual = {
            'biblio': (bibreview_root / 'assets/data/biblio.json').read_bytes(),
            'known': (bibreview_root / 'DOI.txt').read_bytes(),
            'pending': (bibreview_root / 'newDOI.txt').read_bytes(),
        }
        if actual != expected:
            raise AssertionError(
                'BibReview merge/storage compatibility does not reproduce PHRAISE state\n'
                f'expected bibliography: {json.loads(expected["biblio"])}\n'
                f'actual bibliography:   {json.loads(actual["biblio"])}\n'
                f'expected DOI.txt: {expected["known"]!r}\n'
                f'actual DOI.txt:   {actual["known"]!r}\n'
                f'expected newDOI.txt: {expected["pending"]!r}\n'
                f'actual newDOI.txt:   {actual["pending"]!r}'
            )


def main() -> int:
    publications = compare_doi_backed_merge()
    compare_refresh_identity()
    compare_doi_less_behavior()
    compare_canonical_storage(publications)
    compare_full_legacy_state()
    print('PHRAISE DOI-backed concatenate vs BibReview merge: equivalent content')
    print('BibReview persisted UUID on metadata refresh: preserved')
    print('DOI-less legacy collapse: detected and intentionally not reproduced')
    print('canonical bibliography write/read round-trip: exact')
    print('PHRAISE bibliography + DOI queue state through BibReview batch storage: byte-exact')
    print('compatibility planning: read-only before explicit batch apply')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
