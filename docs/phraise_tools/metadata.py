"""HTTP adapters and provider extraction, separated from file mutations.

Provider endpoints and field mappings are centralized here. Network failures
raise instead of being interpreted as missing publications. 404 is an absent
result.
"""
from __future__ import annotations

import html
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from dotenv import dotenv_values

from .common import clean_metadata


class MetadataError(ValueError):
    """An API failed or returned an unexpected response."""

    def __init__(self, message, *, status_code=None):
        super().__init__(message)
        self.status_code = status_code


class Client:
    def __init__(self, root: Path, session=None):
        self.config = {**dotenv_values(root / '.env'), **os.environ}
        self.session = session or requests.Session()
        self._semantic_scholar_limited = False
        self._mendeley_unauthorized = False
        if session is None:
            retry = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504], allowed_methods=['GET'], raise_on_status=False)
            self.session.mount('https://', HTTPAdapter(max_retries=retry))

    def request(self, url, *, params=None, headers=None, context=None,
                allow_landing_denial=False):
        """Report sanitized errors; optionally use a denied publisher landing URL.

        Publisher discovery needs the final URL, not the landing page body.
        This exception never applies to metadata, citations or BibTeX requests.
        """
        response = None
        initial_host = urlsplit(url).hostname or 'unknown host'
        try:
            response = self.session.get(url, params=params, headers=headers, timeout=(5, 30), allow_redirects=True)
            if response.status_code == 404:
                return None
            final_url = response.url if isinstance(response.url, str) else url
            final_host = urlsplit(final_url).hostname or initial_host
            if (allow_landing_denial and response.status_code in (401, 403)
                    and final_host != initial_host):
                return response
            response.raise_for_status()
            return response
        except requests.RequestException as error:
            # Never expose URL queries, credentials, headers or raw exception text.
            failure = error.response if error.response is not None else response
            final_url = getattr(failure, 'url', None)
            final_host = (urlsplit(final_url).hostname if isinstance(final_url, str) else None) or initial_host
            location = initial_host if final_host == initial_host else f'{initial_host} -> {final_host}'
            status = getattr(failure, 'status_code', None)
            if isinstance(status, int):
                detail = f'HTTP {status}'
                hints = {401: 'authentication required by the responding service',
                         403: 'access denied by the responding service',
                         429: 'rate limit reached after retries'}
                if status in hints:
                    detail += ': ' + hints[status]
            elif isinstance(error, requests.exceptions.SSLError):
                detail = 'TLS certificate or handshake failure'
            elif isinstance(error, requests.Timeout):
                detail = 'request timed out'
            elif isinstance(error, requests.TooManyRedirects):
                detail = 'too many redirects'
            elif isinstance(error, requests.ConnectionError):
                detail = 'connection failed (DNS, proxy or network)'
            else:
                detail = 'HTTP transport failure'
            prefix = f'{context}: ' if context else ''
            raise MetadataError(f'{prefix}{location}: {detail}',
                                status_code=status if isinstance(status, int) else None) from error

    def json(self, url, **kwargs):
        response = self.request(url, **kwargs)
        if response is None:
            return None
        try:
            return response.json()
        except ValueError as error:
            raise MetadataError(f'{urlsplit(url).netloc}: invalid JSON response') from error

    def key(self, name):
        value = self.config.get(name)
        if not value:
            raise MetadataError(f'{name} is required for this provider; set it in docs/.env or the environment')
        return value

    def crossref(self, doi):
        response = self.json(f'https://api.crossref.org/works/{quote(doi, safe="")}',
                             params={'mailto': self.config['MAIL']} if self.config.get('MAIL') else {})
        if response is None:
            return None
        if not isinstance(response, dict) or response.get('status') != 'ok' or not isinstance(response.get('message'), dict):
            raise MetadataError(f'CrossRef: unexpected response for {doi}')
        return response['message']

    def publisher(self, doi):
        response = self.request(f'https://doi.org/{quote(doi, safe="")}',
                                context=f'Publisher lookup for DOI {doi}', allow_landing_denial=True)
        if response is None:
            return '', '', ''
        url = response.url
        result = ('', '', '')
        for provider in ('elsevier', 'springer', 'ieee'):
            if provider not in url:
                continue
            encoded = quote(doi, safe='')
            if provider == 'elsevier':
                data = self.json(f'https://api.elsevier.com/content/article/doi/{encoded}',
                                 headers={'Accept': 'application/json', 'X-ELS-APIKey': self.key('SCOPUS_API_KEY')})
            elif provider == 'springer':
                data = self.json('https://api.springernature.com/meta/v2/json',
                                 params={'q': f'doi:{doi}', 'api_key': self.key('SPRINGER_API_KEY')})
            else:
                data = self.json(f'https://ieeexploreapi.ieee.org/api/v1/articles/doi/{encoded}',
                                 params={'apikey': self.key('IEEE_API_KEY'), 'format': 'json'})
            result = extract_provider(provider, data or {})
        return result

    def bibtex(self, doi):
        response = self.request(f'https://doi.org/{quote(doi, safe="")}', headers={'Accept': 'application/x-bibtex;q=1.0'},
                                context=f'BibTeX lookup for DOI {doi}')
        return format_bibtex(response.text if response is not None else '')

    def citation(self, doi):
        response = self.request('https://citation.doi.org/format', params={
            'doi': doi, 'style': 'springer-basic-author-date-no-et-al-with-issue', 'lang': 'en-US'},
                                context=f'Citation lookup for DOI {doi}')
        if response is None:
            return ''
        last = response.text.rstrip('\n').split('\n')[-1]
        return re.sub(r'^1.\s*', '', last)[:-1]

    def complement(self, doi):
        candidates = []
        data = None
        if not self._semantic_scholar_limited:
            try:
                data = self.json(f'https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe="")}',
                                 params={'fields': 'abstract'})
            except MetadataError as error:
                if error.status_code != 429:
                    raise
                self._semantic_scholar_limited = True
                print('phraise: warning: Semantic Scholar HTTP 429; skipping this optional '
                      'abstract provider for the rest of this run. Some abstracts may remain '
                      'unavailable; Mendeley will still be tried when configured.', file=sys.stderr)
        if isinstance(data, dict) and data.get('abstract'):
            candidates.append(data['abstract'])
        # Mendeley is optional; no token means no request to its authenticated API.
        if self.config.get('MENDELEY_API_KEY') and not self._mendeley_unauthorized:
            try:
                data = self.json('https://api.mendeley.com/catalog', params={'doi': doi, 'view': 'all'}, headers={
                    'Accept': 'application/vnd.mendeley-document.1+json',
                    'Authorization': f'Bearer {self.config["MENDELEY_API_KEY"]}'})
            except MetadataError as error:
                if error.status_code != 401:
                    raise
                self._mendeley_unauthorized = True
                data = None
                print('phraise: warning: Mendeley HTTP 401; skipping this optional abstract '
                      'provider for the rest of this run. Check MENDELEY_API_KEY before a '
                      'future run. Existing abstracts are retained; some may remain unavailable.',
                      file=sys.stderr)
            if isinstance(data, list) and data and data[0].get('link'):
                page = self.request(data[0]['link'], headers={'User-Agent': 'PHRAISE abstract-fallback', 'Accept': 'text/html'})
                if page is not None:
                    abstract = mendeley_abstract(page.text)
                    if abstract:
                        candidates.append(abstract)
        return max((c.strip() for c in candidates), key=len, default='Not available')

    def openalex(self, cursor):
        params = {'filter': 'title_and_abstract.search:port-Hamiltonian', 'per-page': 200,
                  'sort': 'publication_date:desc', 'cursor': cursor}
        if self.config.get('OPENALEX_API_KEY'):
            params['api_key'] = self.config['OPENALEX_API_KEY']
        data = self.json('https://api.openalex.org/works', params=params)
        if not isinstance(data, dict) or not isinstance(data.get('results'), list) or not isinstance(data.get('meta'), dict):
            raise MetadataError('OpenAlex: unexpected page response')
        return data


def extract_provider(provider, data):
    def stripped(value):
        return re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', str(value or ''))).strip()

    def keywords(values):
        return ', '.join(sorted({str(v).lower().strip() for v in values if v is not None and str(v).strip()}))

    if provider == 'elsevier':
        core = data.get('full-text-retrieval-response', {}).get('coredata', {})
        subjects = [v.get('$', '') for v in core.get('dcterms:subject') or []]
        terms = re.split('[|;,]', core.get('authkeywords') or '')
        return stripped(core.get('dc:description')), keywords(subjects + terms), stripped(core.get('prism:issueName'))
    if provider == 'springer':
        record = (data.get('records') or [{}])[0]
        terms = record.get('keyword') or []
        if isinstance(terms, str):
            terms = re.split('[,;|]', terms)
        event = ' '.join(v.get('confSeriesName', '') for v in record.get('conferenceInfo') or [])
        return stripped(record.get('abstract')), keywords(terms), event.strip()
    if provider == 'ieee':
        record = (data.get('articles') or [{}])[0]
        nested = record.get('index_terms') or {}
        if not isinstance(nested, dict):
            nested = {}
        terms = []
        for source in [record, nested]:
            for name in ['author_terms', 'ieee_terms']:
                if isinstance(source.get(name), list):
                    terms.extend(source[name])
        event = record.get('publication_title', '') if str(record.get('content_type', '')).lower() == 'conferences' else ''
        return stripped(record.get('abstract')), keywords(terms), event
    raise ValueError(f'Unknown provider: {provider}')


def format_bibtex(value):
    """Preserve the established line-oriented BibTeX format and title braces."""
    value = value.replace(' @', '@').replace('},', '},\n ')
    for field in ['series', 'pages', 'title']:
        value = value.replace(f', {field}', f',\n  {field}')
    lines = []
    for line in value.split('\n'):
        if 'title' in line:
            line = line.replace('={', '={{').replace('},', '}},')
        line = line.replace(' }', '\n}').replace(', }', '\n}')
        for part in line.split('\n'):
            if 'month' in part or 'url' in part:
                continue
            if 'pages' in part:
                part = part.replace('–', '--')
            lines.append(part)
    # The shell echo supplies one newline, while command substitution removes it.
    if lines and lines[-1] == '':
        lines.pop()
    if len(lines) >= 2:
        lines[-2] = lines[-2].replace(',', '')
    value = '\n'.join(lines).replace('&amp;', '\\&').rstrip('\n')
    return (value if any(line.startswith('@') for line in value.split('\n')) else 'No BibTeX found!') + '\n'


def mendeley_abstract(markup):
    soup = BeautifulSoup(markup, 'html.parser')
    def clean(value):
        return re.sub(r'\s+', ' ', html.unescape(value or '')).strip()
    result = ''
    title = soup.find(lambda tag: tag.name in ('h2', 'h3', 'h4', 'h5') and
                      (tag.get('data-name') == 'abstract-title' or re.fullmatch(r'\s*abstract\s*', tag.get_text(), re.I)))
    if title:
        container = title.find_parent(['div', 'section', 'article']) or title.parent
        card = container
        while card and not any('card' == c or c.startswith('card__') for c in card.get('class', [])):
            card = card.parent
        target = (card or container).select_one('p[data-name="content"]')
        if target:
            spans = target.find_all('span')
            result = clean(' '.join(s.get_text(strip=True) for s in spans) if spans else target.get_text(strip=True))
    if not result:
        for selector in ['#Abs1-content', 'section.Abstract', 'div.Abstract', 'div#abstract', 'section#abstract', 'div.article__abstract', 'article .abstract']:
            element = soup.select_one(selector)
            if element and len(clean(element.get_text(' ', strip=True)).split()) > 30:
                result = clean(element.get_text(' ', strip=True))
                break
    if not result:
        for key in ['citation_abstract', 'dcterms.abstract', 'DC.Description', 'dc.Description', 'og:description', 'description']:
            element = soup.find('meta', attrs={'name': key}) or soup.find('meta', attrs={'property': key})
            value = clean(element.get('content', '')) if element else ''
            if len(value.split()) >= 40 and not value.endswith('...'):
                result = value
                break
    result = re.sub(r'^(abstract|résumé|summary|zusammenfassung)\s*[:–—-]\s*', '', result, flags=re.I)
    return result if len(result.split()) >= 40 else ''


def enriched_fields(message, doi, client, *, discovery=False):
    abstract = message.get('abstract') or ''
    keywords = ', '.join(message.get('subject') or [])
    publisher_abstract, publisher_keywords, event = client.publisher(doi)
    if discovery:
        abstract += publisher_abstract
        if publisher_keywords:
            keywords += ', ' + publisher_keywords
    else:
        # Do not discard CrossRef data when a provider returns no usable fields.
        abstract = publisher_abstract or abstract
        keywords = publisher_keywords or keywords
    if not abstract:
        abstract = client.complement(doi)
    return clean_metadata(abstract, True), clean_metadata(keywords), clean_metadata(event)
