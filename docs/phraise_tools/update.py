"""Discover publications and queue incomplete records for later recollection."""
from pathlib import Path
import re
import unicodedata

from .common import (backup_path, bibliography, json_bytes, lines_bytes,
                     read_json, read_lines, safe_component, write_batch)
from .metadata import enriched_fields

TYPES = {'journal-article', 'proceedings-article', 'book-chapter', 'book', 'monograph'}


def is_relevant(value):
    value = ''.join('-' if unicodedata.category(c) == 'Pd' else c for c in value)
    return bool(re.search(r'port[-\s]+(controlled )?hamiltonian|interconnection and damping assignment|dirac structure|dissipative hamiltonian', value, re.I))


def find_updates(root: Path, client, max_pages=20):
    records = bibliography(root)
    known = read_lines(root / 'DOI.txt')
    pending = read_lines(root / 'newDOI.txt')
    bad = sorted(set(read_lines(root / 'badDOI.txt')))
    check = read_lines(root / 'checkDOI.txt')
    trash_path = root / 'trash/trash.json'
    trash = read_json(trash_path, list) if trash_path.exists() and trash_path.stat().st_size else []
    candidates = []
    cursor = '*'
    seen_cursors = set()
    for _ in range(max_pages):
        if not cursor or cursor == 'null' or cursor in seen_cursors:
            break
        seen_cursors.add(cursor)
        page = client.openalex(cursor)
        for work in page['results']:
            doi = work.get('doi')
            if doi:
                candidates.append(doi.removeprefix('https://doi.org/').lower())
        cursor = page['meta'].get('next_cursor')
    excluded = set(known) | set(bad)
    for doi in dict.fromkeys(candidates):
        if doi in excluded or 'arxiv' in doi or 'zenodo' in doi:
            continue
        message = client.crossref(doi)
        if message is None or message.get('type') not in TYPES:
            bad.append(doi)
            continue
        abstract, keywords, _ = enriched_fields(message, doi, client, discovery=True)
        title = (message.get('title') or [''])[0]
        (pending if is_relevant(f'{title} {abstract} {keywords}') else check).append(doi)
    outputs = {}
    to_remove = []
    removed_dois = set()
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
    write_batch(outputs)
    for bib in to_remove:
        bib.unlink()
    return f'Queued {len(pending)} DOIs; {len(removed_dois)} records archived; {len(check)} to check.'
