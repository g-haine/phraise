"""Discover publications and queue incomplete records for later recollection."""
from pathlib import Path
import re
import unicodedata

from .common import (backup_path, bibliography, json_bytes, lines_bytes,
                     read_json, read_lines, Reporter, safe_component, write_batch)
from .metadata import enriched_fields

TYPES = {'journal-article', 'proceedings-article', 'book-chapter', 'book', 'monograph'}


def is_relevant(value):
    value = ''.join('-' if unicodedata.category(c) == 'Pd' else c for c in value)
    return bool(re.search(r'port[-\s]+(controlled )?hamiltonian|interconnection and damping assignment|dirac structure|dissipative hamiltonian', value, re.I))


def find_updates(root: Path, client, max_pages=20, reporter=None):
    reporter = reporter or Reporter(-1)
    records = bibliography(root)
    known = read_lines(root / 'DOI.txt')
    pending = read_lines(root / 'newDOI.txt')
    bad = sorted(set(read_lines(root / 'badDOI.txt')))
    check = read_lines(root / 'checkDOI.txt')
    trash_path = root / 'trash/trash.json'
    trash = read_json(trash_path, list) if trash_path.exists() and trash_path.stat().st_size else []
    reporter.step(f'Loaded {len(records)} publications and {len(known)} known DOI(s)')
    reporter.step(f'Searching OpenAlex (up to {max_pages} page(s))')
    candidates = []
    cursor = '*'
    seen_cursors = set()
    for page_number in range(1, max_pages + 1):
        if not cursor or cursor == 'null' or cursor in seen_cursors:
            break
        seen_cursors.add(cursor)
        page = client.openalex(cursor)
        reporter.detail(f'OpenAlex page {page_number}: {len(page["results"])} result(s)')
        for work in page['results']:
            doi = work.get('doi')
            if doi:
                candidates.append(doi.removeprefix('https://doi.org/').lower())
        cursor = page['meta'].get('next_cursor')
    unique_candidates = list(dict.fromkeys(candidates))
    reporter.step(f'OpenAlex returned {len(unique_candidates)} unique DOI candidate(s)')
    excluded = set(known) | set(bad)
    for index, doi in enumerate(unique_candidates, 1):
        if doi in excluded or 'arxiv' in doi or 'zenodo' in doi:
            reporter.detail(f'[{index}/{len(unique_candidates)}] skipped known/excluded {doi}')
            continue
        reporter.detail(f'[{index}/{len(unique_candidates)}] verifying {doi}')
        message = client.crossref(doi)
        if message is None or message.get('type') not in TYPES:
            bad.append(doi)
            reason = 'absent from CrossRef' if message is None else f'unsupported type {message.get("type")}'
            reporter.detail(f'{doi}: rejected ({reason})')
            continue
        abstract, keywords, _ = enriched_fields(message, doi, client, discovery=True)
        title = (message.get('title') or [''])[0]
        if is_relevant(f'{title} {abstract} {keywords}'):
            pending.append(doi)
            reporter.detail(f'{doi}: queued for collection')
        else:
            check.append(doi)
            reporter.detail(f'{doi}: queued for manual relevance check')
    outputs = {}
    to_remove = []
    removed_dois = set()
    reporter.step('Checking incomplete journal records and BibTeX changes')
    for record in records:
        if record.get('type') != 'journal-article' or not any(record.get(key) == '' for key in ('volume', 'issue', 'pages')):
            continue
        doi = record['doi']
        slug = safe_component(record.get('permalink'))
        bib = root / f'assets/bib/{slug}.bib'
        missing = not bib.exists()
        if missing or bib.read_bytes() != client.bibtex(doi).encode('utf-8'):
            pending.append(doi)
            known = [d for d in known if d.lower() != doi.lower()]
            # Also remove records with missing BibTeX, otherwise concatenate keeps
            # the stale backup entry instead of the newly fetched metadata.
            removed_dois.add(doi)
            trash.append(record)
            reporter.detail(f'{doi}: archived for recollection ({"missing BibTeX" if missing else "changed BibTeX"})')
            if not missing:
                target = root / 'trash' / bib.name
                if target.exists():
                    target = backup_path(root / 'trash', slug, '.bib')
                outputs[target] = bib.read_bytes()
                to_remove.append(bib)
    retained = [r for r in records if r['doi'] not in removed_dois]
    in_database = {r['doi'].lower() for r in retained}
    missing_dois = sorted({d.lower() for d in known} - in_database)
    pending.extend(missing_dois)
    missing_set = set(missing_dois)
    known = [d for d in known if d.lower() not in missing_set]
    known_set, bad_set = set(known), set(bad)
    pending = [d for d in dict.fromkeys(d.lower() for d in pending) if d not in known_set]
    check = [d for d in check if d not in bad_set]
    outputs.update({root / 'DOI.txt': lines_bytes(known), root / 'newDOI.txt': lines_bytes(pending),
                    root / 'badDOI.txt': lines_bytes(bad), root / 'checkDOI.txt': lines_bytes(check),
                    root / 'assets/data/biblio.json': json_bytes(retained), trash_path: json_bytes(trash)})
    reporter.step('Writing DOI queues, bibliography and archive')
    write_batch(outputs)
    for bib in to_remove:
        bib.unlink()
    return f'Queued {len(pending)} DOIs; {len(removed_dois)} records archived; {len(check)} to check.'
