#!/usr/bin/env python3
"""Offline comparison of PHRAISE collection with the BibReview M3 stack."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile

DOCS = Path(__file__).resolve().parents[2] / 'docs'
sys.path.insert(0, str(DOCS))

from bibreview.pipeline.collect import build_publication, collect as bibreview_collect
from bibreview.pipeline.enrich import EnrichmentService
from bibreview.providers.base import Enrichment
from phraise_tools.bibreview_bridge import collection_to_legacy_records, publication_to_legacy_record
from phraise_tools.collect import collect as legacy_collect, make_record
from phraise_tools.common import json_bytes


DOI = '10.1/new'
BIBTEX = '@article{test,\n title={{Port-Hamiltonian systems}}\n}\n'


def source_message(*, abstract: str = 'A CrossRef description.') -> dict:
    return {
        'title': ['Port-Hamiltonian systems'],
        'type': 'journal-article',
        'author': [{
            'given': 'Ada',
            'family': 'Lovelace',
            'ORCID': 'example-orcid',
            'sequence': 'first',
            'affiliation': [{'name': 'Example Institute'}],
        }],
        'abstract': abstract,
        'container-title': ['Journal'],
        'created': {'date-parts': [[2024, 3, 8]]},
        'published-print': {'date-parts': [[2025]]},
        'volume': '7',
        'issue': '1',
        'page': '1-9',
        'publisher': 'Publisher',
        'subject': ['CrossRef'],
        'isbn-type': [{'type': 'print', 'value': '978-0-00-000000-0'}],
        'reference': [
            {'DOI': '10.1/ref'},
            {'author': 'A', 'article-title': 'Title', 'year': 2020},
        ],
    }


def old_record() -> dict:
    return {
        'doi': '10.1/old',
        'title': 'Old publication',
        'type': 'journal-article',
        'authors': [{'given': 'Ada', 'family': 'Lovelace'}],
        'abstract': 'Old abstract.',
        'journal': 'Journal',
        'year': '2024',
        'volume': '1',
        'issue': '2',
        'pages': '1--9',
        'event': '',
        'isbn': '',
        'publisher': 'Publisher',
        'keywords': 'control',
        'dateY': '2024',
        'dateM': '3',
        'dateD': '8',
        'permalink': 'old',
        'references': [],
    }


def normalized_for_comparison(record: dict) -> dict:
    """Ignore only the deliberate canonical trimming of abstract edge whitespace."""
    result = deepcopy(record)
    if isinstance(result.get('abstract'), str):
        result['abstract'] = result['abstract'].strip()
    return result


class LegacyClient:
    def __init__(self, message: dict, *, publisher=('', '', ''), fallback='Not available'):
        self.message = message
        self.publisher_value = publisher
        self.fallback_value = fallback

    def crossref(self, doi):
        return self.message if doi == DOI else None

    def publisher(self, doi):
        return self.publisher_value

    def complement(self, doi):
        return self.fallback_value

    def citation(self, doi):
        return 'A cited publication'

    def bibtex(self, doi):
        return BIBTEX


class WorkProvider:
    def __init__(self, message: dict):
        self.message = message

    def work(self, doi: str):
        return self.message if doi == DOI else None


class PublisherProvider:
    def __init__(self, value: Enrichment):
        self.value = value

    def enrich(self, doi: str) -> Enrichment:
        return self.value


class FallbackProvider:
    def __init__(self, value: str):
        self.value = value

    def abstract(self, doi: str) -> str:
        return self.value


def compare_full_collection() -> None:
    message = source_message()
    legacy_client = LegacyClient(
        message,
        publisher=('Publisher abstract', 'control, energy', 'Conference'),
    )

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        (root / 'assets/data').mkdir(parents=True)
        (root / 'assets/bib').mkdir(parents=True)
        (root / 'assets/data/biblio.json').write_bytes(json_bytes([old_record()]))
        (root / 'DOI.txt').write_text('10.1/old\n', encoding='utf-8')
        pending = root / 'newDOI.txt'
        pending.write_text('10.1/OLD\n10.1/NEW\n10.1/new\n10.1/missing\n', encoding='utf-8')
        (root / 'assets/bib/port-hamiltonian-systems.bib').write_text('existing', encoding='utf-8')

        legacy_collect(root, pending, legacy_client)
        expected_records = json.loads((root / 'assets/data/biblio.json').read_text(encoding='utf-8'))
        expected_bibtex = (root / 'assets/bib/port-hamiltonian-systems0.bib').read_text(encoding='utf-8')

    service = EnrichmentService(
        publisher=PublisherProvider(
            Enrichment(
                abstract='Publisher abstract',
                keywords=('control', 'energy'),
                event='Conference',
            )
        ),
        fallback=FallbackProvider('Not available'),
    )
    result = bibreview_collect(
        ['10.1/OLD', '10.1/NEW', '10.1/new', '10.1/missing'],
        provider=WorkProvider(message),
        known=['10.1/old'],
        used_slugs=['port-hamiltonian-systems'],
        enrichment_lookup=service.for_collection,
        citation_lookup=lambda doi: 'A cited publication',
        bibtex_lookup=lambda doi: BIBTEX,
    )
    actual_records = collection_to_legacy_records(result)

    if result.candidates != ('10.1/new', '10.1/missing'):
        raise AssertionError(f'unexpected candidates: {result.candidates!r}')
    if result.unavailable != ('10.1/missing',):
        raise AssertionError(f'unexpected unavailable DOIs: {result.unavailable!r}')
    if [normalized_for_comparison(record) for record in actual_records] != [
        normalized_for_comparison(record) for record in expected_records
    ]:
        raise AssertionError(
            'BibReview collection differs from historical PHRAISE beyond canonical abstract trimming\n'
            f'expected: {expected_records!r}\nactual:   {actual_records!r}'
        )
    if result.items[0].bibtex != expected_bibtex:
        raise AssertionError('BibReview BibTeX result differs from the historical output')
    author = actual_records[0]['authors'][0]
    if author.get('ORCID') != 'example-orcid' or author.get('affiliation') != [{'name': 'Example Institute'}]:
        raise AssertionError('source-provided author metadata was not preserved')


def compare_abstract_fallback() -> None:
    message = source_message(abstract='')
    message['subject'] = []
    legacy_client = LegacyClient(message, fallback='Fallback abstract')
    expected = make_record(DOI, message, 'port-hamiltonian-systems', legacy_client)

    service = EnrichmentService(
        publisher=PublisherProvider(Enrichment()),
        fallback=FallbackProvider('Fallback abstract'),
    )
    publication = build_publication(
        DOI,
        message,
        'port-hamiltonian-systems',
        enrichment_lookup=service.for_collection,
        citation_lookup=lambda doi: 'A cited publication',
    )
    actual = publication_to_legacy_record(publication)
    if normalized_for_comparison(actual) != normalized_for_comparison(expected):
        raise AssertionError(
            'BibReview fallback collection differs from historical PHRAISE beyond canonical abstract trimming'
        )


def main() -> int:
    compare_full_collection()
    compare_abstract_fallback()
    print('historical PHRAISE vs BibReview collection: equivalent on comparison fixtures')
    print('intentional difference: canonical abstract edge whitespace is trimmed')
    print('candidate filtering / unavailable DOI tracking: exact')
    print('slug collision / references / BibTeX: exact')
    print('publisher enrichment / abstract fallback: equivalent')
    print('author source metadata: preserved')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
