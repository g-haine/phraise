"""Collect new DOI metadata and BibTeX without modifying files during fetching."""
from pathlib import Path
import re

from .common import (backup_path, bibliography, clean_metadata, json_bytes,
                     lines_bytes, read_lines, safe_component, slugify, text, write_batch)
from .metadata import enriched_fields


def make_record(doi, message, slug, client):
    title = re.sub(r'<[^>]*mml[^>]*>', '', (message.get('title') or [''])[0])
    created = (message.get('created', {}).get('date-parts') or [[]])[0]
    if len(created) < 3:
        raise ValueError(f'{doi}: missing CrossRef creation date')
    published = (message.get('published-print', {}).get('date-parts') or [[]])[0]
    abstract, keywords, event = enriched_fields(message, doi, client)
    references = []
    for ref in message.get('reference') or []:
        ref_doi = text(ref.get('DOI'))
        if re.search('10.', ref_doi):
            title_ref = client.citation(ref_doi)
        else:
            values = [(str(ref['author']) + ',') if ref.get('author') else '',
                      (str(ref['article-title']) + '.') if ref.get('article-title') else '',
                      ref.get('journal-title'), ref.get('volume-title'),
                      f'({ref["year"]})' if ref.get('year') else '']
            title_ref = ' '.join(str(v) for v in values if v)
        references.append({'doi': ref_doi, 'title': clean_metadata(title_ref)})
    return {
        'doi': doi, 'type': message.get('type') or '', 'title': title,
        'authors': message.get('author'), 'abstract': abstract,
        'journal': (message.get('container-title') or [''])[0],
        'year': str(published[0] if published else created[0]),
        'volume': str(message.get('volume') or ''), 'issue': str(message.get('issue') or ''),
        'event': event, 'isbn': (message.get('isbn-type') or [{}])[0].get('value', ''),
        'pages': str(message.get('page') or '').replace('-', '--'),
        'publisher': message.get('publisher') or '', 'keywords': keywords,
        'dateY': str(created[0]), 'dateM': str(created[1]), 'dateD': str(created[2]),
        'permalink': slug, 'references': references,
    }


def collect(root: Path, input_path: Path, client):
    biblio_path = root / 'assets/data/biblio.json'
    bibliography(root)  # Validate the backup before collecting anything.
    if input_path.resolve() in {biblio_path.resolve(), (root / 'DOI.txt').resolve()}:
        raise ValueError('The input DOI file must differ from DOI.txt and biblio.json')
    known = set(read_lines(root / 'DOI.txt'))
    candidates = [doi for doi in dict.fromkeys(d.lower() for d in read_lines(input_path)) if doi not in known]
    if not candidates:
        return 'No new DOIs; bibliography unchanged.'
    outputs = {}
    records = []
    absent = []
    used = {p.stem for p in (root / 'assets/bib').glob('*.bib')}
    for doi in candidates:
        message = client.crossref(doi)
        if message is None:
            absent.append(doi)
            continue
        title = re.sub(r'<[^>]*mml[^>]*>', '', (message.get('title') or [''])[0])
        slug = slugify(title)
        safe_component(slug)
        while slug in used:
            slug += '0'
        used.add(slug)
        records.append(make_record(doi, message, slug, client))
        outputs[root / f'assets/bib/{slug}.bib'] = client.bibtex(doi).encode('utf-8')
    backup = backup_path(root / 'assets/data', 'biblio', '.json')
    outputs = {backup: biblio_path.read_bytes(), **outputs,
               biblio_path: json_bytes(records), input_path: lines_bytes(candidates)}
    write_batch(outputs)
    return f'Collected {len(records)} publications; unavailable: {len(absent)}; backup: {backup}'
