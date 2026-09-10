"""Render author suggestions, posts and index pages in memory before writing."""
from collections import defaultdict
from datetime import date
import html
import json
from pathlib import Path
import re

from unidecode import unidecode

from .common import (author_names, backup_path, bibliography, mappings, mathjaxify,
                     read_lines, record_date, safe_component, slugify, text, write_batch)


def author_suggestions(root: Path):
    records = bibliography(root)
    _, reverse = mappings(root)
    unknown = {name for r in records for name in author_names(r)} - reverse.keys()
    names = sorted(unknown, key=lambda n: (unidecode(n.split()[-1]), n))
    # A valid standalone object replaces the shell's copy/paste fragment.
    proposed = defaultdict(list)
    for name in names:
        slug = slugify(name)
        if not slug:
            raise ValueError(f'Cannot generate an author slug for {name!r}')
        proposed[slug].append(name)
    return json.dumps(proposed, ensure_ascii=False, indent=2)


def category(record):
    kind, event = record.get('type'), record.get('event') or ''
    if kind == 'proceedings-article' or re.search('Conference|Workshop|Symposium|Congress|Proceeding|Consortium', event):
        return 'proceedings'
    categories = {'journal-article': 'articles', 'book-chapter': 'chapters', 'book': 'books', 'monograph': 'books'}
    if kind not in categories:
        raise ValueError(f'Unknown publication type {kind!r} for {record.get("doi")}')
    return categories[kind]


def yaml_scalar(value):
    """Keep ordinary legacy scalars; quote YAML-sensitive values when needed."""
    if not value or re.search(r'[:#\n\r\[\]{}]', value) or value[0] in "!&*?|-<>=@`\"'" or value.lower() in {'null', 'true', 'false', 'yes', 'no', 'on', 'off', '~'}:
        return json.dumps(value, ensure_ascii=False)
    return value


def validate_authors(records, reverse):
    unknown = sorted({name for r in records for name in author_names(r)} - reverse.keys())
    if unknown:
        raise ValueError('Unknown authors; complete author_mappings.json first: ' + ', '.join(unknown))


def render_post(record, reverse, known, permalinks, bibtex):
    day = record_date(record)
    slug = safe_component(record.get('permalink'))
    title = mathjaxify(text(record.get('title')))
    names = author_names(record)
    keywords = mathjaxify(text(record.get('keywords', '')))
    get = lambda key: text(record.get(key))
    lines = ['---', f'title: {json.dumps(title, ensure_ascii=False)}',
             f'date: {day} 00:00:00 +0100', f'permalink: {slug}',
             f'year: {get("year")}', f'authors: {yaml_scalar(", ".join(names))}',
             f'category: {category(record)}']
    if keywords:
        lines.append('tags:')
        lines.extend('  - ' + yaml_scalar(word.strip(' ')) for word in keywords.split(';'))
    lines.extend(['---', ' ', '## Authors', ', '.join(f'[{n}](authors/{reverse[n]})' for n in names),
                  ' ', '## Abstract', mathjaxify(get('abstract')), ' '])
    if keywords:
        lines.extend(['## Keywords', keywords, ' '])
    lines.append('## Citation')
    if re.search('book|monograph', get('type')):
        lines.append(f'- **ISBN:** {get("isbn")}')
    else:
        for label, field in [('Journal', 'journal'), ('Year', 'year'), ('Volume', 'volume'), ('Issue', 'issue'), ('Pages', 'pages')]:
            lines.append(f'- **{label}:** {get(field)}')
    doi = get('doi')
    lines.extend([f'- **Publisher:** {get("publisher")}', f'- **DOI:** [{doi}](https://doi.org/{doi})'])
    if record.get('event'):
        lines.append(f'- **Note:** {record["event"]}')
    lines.extend([' ', '## BibTeX', '{% highlight bibtex %}', '{% raw %}'])
    rendered = '\n'.join(lines) + '\n' + bibtex
    rendered += '\n'.join(['{% endraw %}', '{% endhighlight %}', ' ',
                           '[Download the bib file]({{ site.baseurl }}/assets/bib/' + slug + '.bib)', ' ', ''])
    refs = []
    for ref in record.get('references') or []:
        title_ref = text(ref.get('title'))
        ref_doi = text(ref.get('doi')).lower()
        if ref_doi != 'null':
            if ref_doi in known and permalinks.get(ref_doi):
                title_ref = f'[{title_ref}]({permalinks[ref_doi]})'
            refs.append(f'- {title_ref} -- [{ref_doi}](https://doi.org/{ref_doi})')
        elif title_ref:
            refs.append(f'- {title_ref}')
    if refs:
        rendered += '## References\n' + '\n'.join(refs) + '\n\n'
    return f'{day}-{slug}.md', rendered


def generate_posts(root: Path, client):
    records = bibliography(root)
    _, reverse = mappings(root)
    validate_authors(records, reverse)
    known = set(read_lines(root / 'DOI.txt'))
    permalinks = {r['doi']: r.get('permalink', '') for r in records}
    outputs = {}
    valid = set()
    for record in records:
        slug = safe_component(record.get('permalink'))
        if slug in valid:
            raise ValueError(f'Duplicate permalink: {slug}')
        valid.add(slug)
        bib = root / f'assets/bib/{slug}.bib'
        bibtex = bib.read_text(encoding='utf-8') if bib.exists() else client.bibtex(record['doi'])
        name, content = render_post(record, reverse, known, permalinks, bibtex)
        outputs[root / '_posts' / name] = content.encode('utf-8')
        if not bib.exists():
            outputs[bib] = bibtex.encode('utf-8')
    orphan_bibs = [p for p in (root / 'assets/bib').rglob('*.bib') if p.stem not in valid]
    for bib in orphan_bibs:
        target = root / 'trash' / bib.name
        if target.exists() or target in outputs:
            target = backup_path(root / 'trash', bib.stem, '.bib')
            while target in outputs:
                target = target.with_stem(target.stem + '0')
        outputs[target] = bib.read_bytes()
    outputs[root / '_data/library.yml'] = f'last_update: "{date.today().isoformat()}"\n'.encode()
    obsolete = [p for p in (root / '_posts').glob('*.md') if p not in outputs]
    write_batch(outputs)
    for path in obsolete + orphan_bibs:
        path.unlink()
    return f'Generated {len(records)} posts; archived {len(orphan_bibs)} orphan BibTeX files.'


def page_header(title, permalink):
    return f'---\ntitle: {yaml_scalar(title)}\npermalink: {permalink}\n---\n\n'


def publication_list(items):
    # Shell sort compares date descending, then the full row to break ties.
    result = '<ul class="post-list">\n'
    result += '\n'.join(item[1] for item in sorted(items, reverse=True))
    return result + '\n\n</ul>\n{% include count-posts.html %}\n'


def generate_pages(root: Path):
    records = bibliography(root)
    mapping, reverse = mappings(root)
    validate_authors(records, reverse)
    authors, years = defaultdict(list), defaultdict(list)
    for record in records:
        if record.get('authors') is None:
            continue
        names = author_names(record)
        slug = safe_component(record.get('permalink'))
        year = safe_component(text(record.get('year')))
        if not year.isdecimal():
            raise ValueError(f'Invalid publication year: {year}')
        day = record_date(record)
        # In HTML, one MathJax backslash remains after the shell's echo -e.
        title = mathjaxify(text(record.get('title'))).replace('\\\\', '\\')
        row = (f"<li><span class='post-meta'>{year} -- {html.escape(', '.join(names), quote=False)}</span>"
               f'<h3><a class="post-link" href="{{{{ site.baseurl }}}}/{slug}">{html.escape(title, quote=False)}</a></h3></li>')
        row = row.replace('class="post-link"', "class='post-link'")
        for name in names:
            authors[reverse[name]].append((day, row))
        years[year].append((day, row))
    outputs = {}
    intro = page_header('Authors', '/authors/')
    intro += f'<h3>There are {len(authors)} authors referenced.</h3>\n'
    intro += "<p id='info-authors'>For <a href='{{ site.baseurl }}/about/#handling-authors-names'>simplicity</a>, the authors are sorted using the last word of their name.<br />For example, <i>Arjan van der Schaft</i> appears under the letter <strong>S</strong>, and <i>Yann Le Gorrec</i> under the letter <strong>G</strong>.</p>\n"
    intro += "<p>You may want to look at <a href='{{ site.baseurl }}/assets/data/author_mappings.json'>the array managing name variations</a> (a JSON file) for verification/correction.</p>\n<hr />\n"
    intro += "<p id='links-letters'>" + ' - '.join(f"<a href='#{c}'>{c.upper()}</a>" for c in 'abcdefghijklmnopqrstuvwxyz') + '</p>\n'
    intro += "<div class='grid'>\n"
    letter = ''
    for slug in sorted(authors, key=lambda s: (unidecode(mapping[s][0].split()[-1]).replace("d'", ''), mapping[s][0])):
        author = mapping[slug][0]
        first = unidecode(author.split()[-1]).replace("d'", '')[:1].upper()
        if first != letter:
            intro += f"</div>\n## {first}\n<div class='grid'>\n"
            letter = first
        intro += "<a href='{{ site.baseurl }}/authors/" + slug + "'>" + html.escape(author) + '</a>\n'
        content = page_header(f'Publications by {author}', f'/authors/{slug}')
        content += '<h3 id="number-posts">There are ... items referenced.</h3>\n'
        content += "<p id='info-authors'>Alternative author names: " + html.escape(', '.join(mapping[slug])) + '.</p>\n<hr />\n'
        content += publication_list(authors[slug])
        outputs[root / 'authors' / f'{slug}.md'] = content.encode('utf-8')
    outputs[root / 'authors/index.md'] = (intro + '</div>\n').encode('utf-8')
    year_index = page_header('Years', '/years/') + '<div class="grid">\n'
    for year in sorted(years, key=int):
        year_index += "<a href='{{ site.baseurl }}/years/" + year + "'>" + year + '</a>\n'
        content = page_header(f'Published in {year}', f'/years/{year}')
        content += '<h3 id="number-posts">There are ... items referenced.</h3>\n' + publication_list(years[year])
        outputs[root / 'years' / f'{year}.md'] = content.encode('utf-8')
    outputs[root / 'years/index.md'] = (year_index + '</div>\n').encode('utf-8')
    obsolete = [p for folder in ['authors', 'years'] for p in (root / folder).glob('*.md') if p not in outputs]
    write_batch(outputs)
    for path in obsolete:
        path.unlink()
    return f'Generated pages for {len(authors)} authors and {len(years)} years.'
