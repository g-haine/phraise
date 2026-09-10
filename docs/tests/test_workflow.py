"""Offline integration tests. No real credentials, data or network are used."""
from copy import deepcopy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phraise_tools.collect import collect
from phraise_tools.common import json_bytes, mathjaxify, slugify, write_batch
from phraise_tools.generate import author_suggestions, generate_pages, generate_posts, render_post
from phraise_tools.metadata import (Client, MetadataError, extract_provider, format_bibtex,
                                    mendeley_abstract)
from phraise_tools.update import find_updates, is_relevant
from concatenate import concatenate
import requests

DOCS = Path(__file__).resolve().parents[1]


def record(doi='10.1/old', slug='old'):
    return {'doi': doi, 'title': 'Port-Hamiltonian systems', 'type': 'journal-article',
            'authors': [{'given': 'Ada', 'family': 'Lovelace'}], 'abstract': 'An abstract.',
            'journal': 'Journal', 'year': '2024', 'volume': '1', 'issue': '2', 'pages': '1--9',
            'event': '', 'isbn': '', 'publisher': 'Publisher', 'keywords': 'control; energy',
            'dateY': '2024', 'dateM': '3', 'dateD': '8', 'permalink': slug, 'references': []}


def message(title='Port-Hamiltonian systems'):
    return {'title': [title], 'type': 'journal-article', 'author': [{'given': 'Ada', 'family': 'Lovelace'}],
            'abstract': 'A CrossRef description.', 'container-title': ['Journal'],
            'created': {'date-parts': [[2024, 3, 8]]}, 'volume': '7', 'issue': '1', 'page': '1-9',
            'publisher': 'Publisher', 'subject': ['control'], 'reference': []}


class FakeClient:
    def __init__(self):
        self.messages = {}
        self.bibs = {}
        self.pages = {'*': {'results': [], 'meta': {'next_cursor': None}}}
        self.calls = []

    def crossref(self, doi):
        self.calls.append(('crossref', doi))
        return self.messages.get(doi)

    def publisher(self, doi):
        return '', '', ''

    def complement(self, doi):
        return 'Not available'

    def citation(self, doi):
        return 'A cited publication'

    def bibtex(self, doi):
        return self.bibs.get(doi, '@article{test,\n title={{Port-Hamiltonian systems}}\n}\n')

    def openalex(self, cursor):
        self.calls.append(('openalex', cursor))
        return self.pages[cursor]


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.client = FakeClient()
        self.save('assets/data/biblio.json', [record()])
        self.save('assets/data/author_mappings.json', {'ada-lovelace': ['Ada Lovelace']})
        for name, content in [('DOI.txt', '10.1/old\n'), ('newDOI.txt', ''), ('badDOI.txt', ''), ('checkDOI.txt', '')]:
            (self.root / name).write_text(content)
        (self.root / 'assets/bib').mkdir()
        (self.root / 'assets/bib/old.bib').write_text(self.client.bibtex('10.1/old'))
        (self.root / '_posts').mkdir()

    def save(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(json_bytes(data))

    def load(self, name):
        return json.loads((self.root / name).read_text())

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def test_collection_dedup_backup_collision_and_references(self):
        pending = self.root / 'newDOI.txt'
        pending.write_text('10.1/OLD\n10.1/NEW\n10.1/new\n10.1/missing\n')
        data = message()
        data['reference'] = [{'DOI': '10.1/ref'}, {'author': 'A', 'article-title': 'Title', 'year': 2020}]
        self.client.messages['10.1/new'] = data
        (self.root / 'assets/bib/port-hamiltonian-systems.bib').write_text('existing')
        old = (self.root / 'assets/data/biblio.json').read_bytes()
        collect(self.root, pending, self.client)
        new = self.load('assets/data/biblio.json')[0]
        self.assertEqual(new['permalink'], 'port-hamiltonian-systems0')
        self.assertEqual(new['pages'], '1--9')
        self.assertEqual(new['year'], '2024')
        self.assertEqual(new['references'], [{'doi': '10.1/ref', 'title': 'A cited publication'},
                                             {'doi': 'null', 'title': 'A, Title. (2020)'}])
        self.assertEqual(next(self.root.glob('assets/data/biblio-*.json')).read_bytes(), old)
        self.assertEqual(pending.read_text(), '10.1/new\n10.1/missing\n')

    def test_empty_collection_is_noop(self):
        before = self.snapshot()
        collect(self.root, self.root / 'newDOI.txt', self.client)
        self.assertEqual(before, self.snapshot())

    def test_collection_failure_leaves_inputs_unchanged(self):
        (self.root / 'newDOI.txt').write_text('10.1/a\n10.1/b\n')
        self.client.messages['10.1/a'] = message()
        before = self.snapshot()
        with patch.object(self.client, 'bibtex', side_effect=MetadataError('offline')):
            with self.assertRaises(MetadataError):
                collect(self.root, self.root / 'newDOI.txt', self.client)
        self.assertEqual(before, self.snapshot())

    def test_suggestions_are_valid_json_and_do_not_write(self):
        self.save('assets/data/author_mappings.json', {})
        before = self.snapshot()
        self.assertEqual(json.loads(author_suggestions(self.root)), {'ada-lovelace': ['Ada Lovelace']})
        self.assertEqual(before, self.snapshot())

    def test_generate_posts_and_pages(self):
        (self.root / '_posts/obsolete.md').write_text('obsolete')
        (self.root / 'assets/bib/orphan.bib').write_text('orphan')
        generate_posts(self.root, self.client)
        generate_pages(self.root)
        post = (self.root / '_posts/2024-03-08-old.md').read_text()
        self.assertIn('category: articles', post)
        self.assertIn('[Ada Lovelace](authors/ada-lovelace)', post)
        self.assertIn('1--9', post)
        self.assertFalse((self.root / '_posts/obsolete.md').exists())
        self.assertEqual((self.root / 'trash/orphan.bib').read_text(), 'orphan')
        self.assertIn('/old', (self.root / 'years/2024.md').read_text())
        self.assertIn('Ada Lovelace', (self.root / 'authors/ada-lovelace.md').read_text())
        self.assertIn('last_update:', (self.root / '_data/library.yml').read_text())

    def test_generation_error_preserves_existing_outputs(self):
        (self.root / '_posts/keep.md').write_text('keep')
        self.save('assets/data/author_mappings.json', {})
        before = self.snapshot()
        for function in [lambda: generate_posts(self.root, self.client), lambda: generate_pages(self.root)]:
            with self.assertRaisesRegex(ValueError, 'Unknown authors'):
                function()
            self.assertEqual(before, self.snapshot())

    def test_unsafe_and_duplicate_permalink_rejected(self):
        for slug in ['../escape', 'old']:
            records = [record(), record('10.1/other', slug)]
            self.save('assets/data/biblio.json', records)
            before = self.snapshot()
            with self.assertRaises(ValueError):
                generate_posts(self.root, self.client)
            self.assertEqual(before, self.snapshot())

    def test_categories_references_and_yaml_quoting(self):
        for kind, category in [('journal-article', 'articles'), ('proceedings-article', 'proceedings'),
                               ('book-chapter', 'chapters'), ('book', 'books'), ('monograph', 'books')]:
            data = record()
            data.update(type=kind, title='A "quoted": $x$ title', keywords='key: value; #tag',
                        references=[{'doi': '10.1/old', 'title': 'Old'}, {'doi': 'null', 'title': 'No DOI'}])
            _, output = render_post(data, {'Ada Lovelace': 'ada-lovelace'}, {'10.1/old'}, {'10.1/old': 'old'}, 'bib\n')
            self.assertIn(f'category: {category}', output)
            self.assertIn('- [Old](old) -- [10.1/old]', output)
            self.assertIn('- No DOI', output)
            self.assertIn('  - "key: value"', output)
            title_line = output.splitlines()[1].removeprefix('title: ')
            self.assertEqual(json.loads(title_line), mathjaxify(data['title']))

    def test_update_discovery_pagination_and_requeue(self):
        incomplete = record()
        incomplete['volume'] = ''
        self.save('assets/data/biblio.json', [incomplete])
        self.client.bibs['10.1/old'] = '@article{updated}\n'
        self.client.pages['*'] = {'results': [{'doi': f'https://doi.org/10.1/{d}'} for d in ['new', 'check', 'bad', 'absent']], 'meta': {'next_cursor': 'a+/='}}
        self.client.pages['a+/='] = {'results': [{'doi': 'https://doi.org/10.1/new'}], 'meta': {'next_cursor': None}}
        self.client.messages.update({'10.1/new': message(), '10.1/check': message('Unrelated topic'), '10.1/bad': {**message(), 'type': 'dataset'}})
        find_updates(self.root, self.client)
        self.assertEqual(self.load('assets/data/biblio.json'), [])
        self.assertEqual(self.load('trash/trash.json'), [incomplete])
        self.assertEqual((self.root / 'newDOI.txt').read_text(), '10.1/new\n10.1/old\n')
        self.assertEqual((self.root / 'checkDOI.txt').read_text(), '10.1/check\n')
        self.assertEqual((self.root / 'badDOI.txt').read_text(), '10.1/bad\n10.1/absent\n')
        self.assertFalse((self.root / 'assets/bib/old.bib').exists())
        self.assertEqual(self.client.calls.count(('crossref', '10.1/new')), 1)

    def test_missing_bib_requeued_without_stale_record(self):
        incomplete = record()
        incomplete['issue'] = ''
        self.save('assets/data/biblio.json', [incomplete])
        (self.root / 'assets/bib/old.bib').unlink()
        find_updates(self.root, self.client)
        self.assertEqual(self.load('assets/data/biblio.json'), [])
        self.assertEqual(self.load('trash/trash.json'), [incomplete])
        self.assertEqual((self.root / 'newDOI.txt').read_text(), '10.1/old\n')

    def test_update_network_failure_preserves_every_file(self):
        before = self.snapshot()
        with patch.object(self.client, 'openalex', side_effect=MetadataError('timeout')):
            with self.assertRaises(MetadataError):
                find_updates(self.root, self.client)
        self.assertEqual(before, self.snapshot())

    def test_empty_update_preserves_existing_trash(self):
        self.save('trash/trash.json', [record('10.1/archived', 'archived')])
        find_updates(self.root, self.client)
        self.assertEqual(self.load('trash/trash.json')[0]['doi'], '10.1/archived')
        self.assertEqual((self.root / 'newDOI.txt').read_text(), '')

    def test_full_offline_workflow(self):
        self.client.pages['*']['results'] = [{'doi': 'https://doi.org/10.1/new'}]
        self.client.messages['10.1/new'] = message()
        find_updates(self.root, self.client)
        collect(self.root, self.root / 'newDOI.txt', self.client)
        self.assertEqual(json.loads(author_suggestions(self.root)), {})
        concatenate(*(self.root / p for p in ['DOI.txt', 'newDOI.txt', 'badDOI.txt', 'assets/data/biblio.json', 'assets/data']))
        generate_posts(self.root, self.client)
        generate_pages(self.root)
        self.assertEqual(len(self.load('assets/data/biblio.json')), 2)
        self.assertEqual(len(list((self.root / '_posts').glob('*.md'))), 2)
        self.assertEqual((self.root / 'newDOI.txt').read_text(), '')
        self.assertEqual(set((self.root / 'DOI.txt').read_text().splitlines()), {'10.1/new', '10.1/old'})

    def test_all_cli_help_and_local_commands(self):
        for script in ['getData', 'looking4Update', 'setAuthorMapping', 'setPosts', 'setPages']:
            result = subprocess.run([sys.executable, str(DOCS / f'{script}.py'), '--help'], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        for cwd in [DOCS.parent, DOCS]:
            for script in ['setAuthorMapping', 'setPosts', 'setPages']:
                result = subprocess.run([sys.executable, str(DOCS / f'{script}.py'), '--root', str(self.root)], cwd=cwd, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)


class MetadataTests(unittest.TestCase):
    def test_provider_mappings(self):
        cases = [('elsevier', {'full-text-retrieval-response': {'coredata': {'dc:description': '<p>Text</p>', 'dcterms:subject': [{'$': 'Control'}], 'authkeywords': 'Energy;control', 'prism:issueName': 'Conference'}}}),
                 ('springer', {'records': [{'abstract': '<p>Text</p>', 'keyword': ['Energy', 'Control', 'control'], 'conferenceInfo': [{'confSeriesName': 'Conference'}]}]}),
                 ('ieee', {'articles': [{'abstract': '<p>Text</p>', 'author_terms': ['Control'], 'index_terms': {'ieee_terms': ['Energy']}, 'content_type': 'Conferences', 'publication_title': 'Conference'}]})]
        for provider, data in cases:
            self.assertEqual(extract_provider(provider, data), ('Text', 'control, energy', 'Conference'))
            self.assertEqual(extract_provider(provider, {}), ('', '', ''))

    def test_mendeley_card_and_meta(self):
        abstract = ' '.join(f'word{i}' for i in range(45))
        card = f'<div class="card"><h3 data-name="abstract-title">Abstract</h3><p data-name="content"><span>{abstract}</span></p></div>'
        self.assertEqual(mendeley_abstract(card), abstract)
        self.assertEqual(mendeley_abstract(f'<meta name="citation_abstract" content="{abstract}">'), abstract)
        self.assertEqual(mendeley_abstract('<meta name="description" content="Short teaser...">'), '')

    def test_http_timeout_does_not_expose_key(self):
        session = Mock()
        session.get.side_effect = requests.Timeout('secret-key')
        client = Client(Path('/nonexistent'), session)
        with self.assertRaises(MetadataError) as context:
            client.json('https://api.example.test?key=secret-key')
        self.assertNotIn('secret-key', str(context.exception))

    def test_http_404_invalid_json_and_crossref_shape(self):
        session = Mock()
        response = session.get.return_value
        response.status_code = 404
        client = Client(Path('/nonexistent'), session)
        self.assertIsNone(client.crossref('10.1/a'))
        response.status_code = 200
        response.json.side_effect = ValueError('bad')
        with self.assertRaisesRegex(MetadataError, 'invalid JSON'):
            client.crossref('10.1/a')
        response.json.side_effect = None
        response.json.return_value = {'status': 'error'}
        with self.assertRaisesRegex(MetadataError, 'unexpected'):
            client.crossref('10.1/a')

    def test_encoded_doi_and_openalex_cursor(self):
        session = Mock()
        session.get.return_value.status_code = 200
        session.get.return_value.json.return_value = {'status': 'ok', 'message': {}}
        client = Client(Path('/nonexistent'), session)
        client.crossref('10.1/a?b')
        self.assertIn('10.1%2Fa%3Fb', session.get.call_args.args[0])
        session.get.return_value.json.return_value = {'results': [], 'meta': {'next_cursor': None}}
        client.openalex('a+/=')
        self.assertEqual(session.get.call_args.kwargs['params']['cursor'], 'a+/=')
        self.assertEqual(session.get.call_args.kwargs['timeout'], (5, 30))

    def test_environment_is_not_executed_and_shell_overrides(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.env').write_text('MAIL="from file"\nSCOPUS_API_KEY=$(touch sentinel)\n')
            with patch.dict(os.environ, {'MAIL': 'from environment'}):
                client = Client(root, Mock())
                self.assertEqual(client.config['MAIL'], 'from environment')
                self.assertEqual(client.config['SCOPUS_API_KEY'], '$(touch sentinel)')
            self.assertFalse((root / 'sentinel').exists())

    def test_relevance_and_transliteration(self):
        for title in ['port–Hamiltonian', 'port controlled hamiltonian', 'Dirac structure', 'interconnection and damping assignment']:
            self.assertTrue(is_relevant(title))
        self.assertFalse(is_relevant('quantum computation'))
        self.assertEqual(slugify('Énergie & contrôle'), 'energie-controle')


@unittest.skipUnless(shutil.which('bash') and shutil.which('jq'), 'Bash and jq required')
class ShellParityTests(unittest.TestCase):
    setUp = WorkflowTests.setUp
    save = WorkflowTests.save
    # Only parity tests here; do not repeat inherited integration tests.
    def test_post_parity(self):
        with tempfile.TemporaryDirectory() as directory:
            shell = Path(directory)
            shutil.copytree(self.root, shell, dirs_exist_ok=True)
            shutil.copy(DOCS / '.utils', shell / '.utils')
            (shell / '.env').touch()
            result = subprocess.run(['bash', str(DOCS / 'setPosts.sh')], cwd=shell, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            generate_posts(self.root, self.client)
            name = '_posts/2024-03-08-old.md'
            self.assertEqual((self.root / name).read_text(), (shell / name).read_text())

    def test_math_and_bibtex_parity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copy(DOCS / '.utils', root / '.utils')
            (root / '.env').touch()
            for value in ['Title $x+y$ and $$z$$', '{{foo}} & bar']:
                result = subprocess.run(['bash', '-c', 'source .utils; mathjaxify "$1"', '_', value], cwd=root, capture_output=True, check=True)
                self.assertEqual(result.stdout.decode().rstrip('\n'), mathjaxify(value))
            raw = '@article{key, title={A title}, author={Ada}, pages={1–9}, month={March}, url={https://test}, year={2024} }'
            # Use an overridden print source, not the URL argument passed to safe_curl.
            result = subprocess.run(['bash', '-c', 'source .utils; RAW="$1"; safe_curl() { printf "%s\\n" "$RAW"; }; print_bib test output.bib', '_', raw], cwd=root, capture_output=True, check=True)
            self.assertEqual((root / 'output.bib').read_text(), format_bibtex(raw))

    def test_pages_parity(self):
        with tempfile.TemporaryDirectory() as directory:
            shell = Path(directory)
            shutil.copytree(self.root, shell, dirs_exist_ok=True)
            shutil.copy(DOCS / '.utils', shell / '.utils')
            (shell / '.env').touch()
            result = subprocess.run(['bash', str(DOCS / 'setPages.sh')], cwd=shell, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            generate_pages(self.root)
            for folder in ['authors', 'years']:
                self.assertEqual({p.name for p in (shell / folder).glob('*.md')},
                                 {p.name for p in (self.root / folder).glob('*.md')})
                for file in (shell / folder).glob('*.md'):
                    self.assertEqual(file.read_text(), (self.root / folder / file.name).read_text())

    def test_collection_parity_with_simulated_apis(self):
        with tempfile.TemporaryDirectory() as directory:
            shell = Path(directory)
            (self.root / 'newDOI.txt').write_text('10.1/NEW\n10.1/new\n')
            self.client.messages['10.1/new'] = message()
            shutil.copytree(self.root, shell, dirs_exist_ok=True)
            (shell / 'response.json').write_text(json.dumps({'status': 'ok', 'message': message()}))
            utils = (DOCS / '.utils').read_text() + '''
fetch_metadata_crossref() { cat response.json; }
print_bib() { printf '@article{test,\\n title={{Port-Hamiltonian systems}}\\n}\\n' > "$2"; }
curl() { printf 'https://example.test/article'; }
'''
            (shell / '.utils').write_text(utils)
            (shell / '.env').touch()
            result = subprocess.run(['bash', str(DOCS / 'getData.sh'), 'newDOI.txt'], cwd=shell, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            collect(self.root, self.root / 'newDOI.txt', self.client)
            self.assertEqual(json.loads((shell / 'assets/data/biblio.json').read_text()),
                             json.loads((self.root / 'assets/data/biblio.json').read_text()))
            self.assertEqual((shell / 'newDOI.txt').read_bytes(), (self.root / 'newDOI.txt').read_bytes())
            self.assertEqual((shell / 'assets/bib/port-hamiltonian-systems.bib').read_bytes(),
                             (self.root / 'assets/bib/port-hamiltonian-systems.bib').read_bytes())

    def test_author_suggestion_parity(self):
        # The shell emits comma-prefixed fragments; Python emits a JSON object.
        with tempfile.TemporaryDirectory() as directory:
            shell = Path(directory)
            self.save('assets/data/author_mappings.json', {})
            shutil.copytree(self.root, shell, dirs_exist_ok=True)
            shutil.copy(DOCS / '.utils', shell / '.utils')
            (shell / '.env').touch()
            result = subprocess.run(['bash', str(DOCS / 'setAuthorMapping.sh')], cwd=shell, capture_output=True, check=True)
            fragment = result.stdout.decode().strip().removeprefix(',').strip()
            self.assertEqual(json.loads('{' + fragment + '}'), json.loads(author_suggestions(self.root)))


class InstallerTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('bash'), 'Bash required')
    def test_create_update_and_failure_with_conda_stub(self):
        with tempfile.TemporaryDirectory(prefix='phraise install ') as directory:
            root = Path(directory)
            script = root / 'install.sh'
            shutil.copy(DOCS.parent / 'install.sh', script)
            shutil.copy(DOCS.parent / 'phraise.yml', root / 'phraise.yml')
            conda = root / 'conda'
            conda.write_text('''#!/bin/bash
if [[ "$1" == "list" ]]; then exit "${TEST_ENV_MISSING:-0}"; fi
printf '%s\\n' "$@" > "$TEST_LOG"
exit "${TEST_CONDA_FAILURE:-0}"
''')
            conda.chmod(0o755)
            for missing, failure, action in [('0', '0', 'update'), ('1', '0', 'create'), ('0', '1', 'update')]:
                env = {**os.environ, 'PATH': str(root) + os.pathsep + os.environ['PATH'],
                       'TEST_ENV_MISSING': missing, 'TEST_CONDA_FAILURE': failure, 'TEST_LOG': str(root / 'log')}
                result = subprocess.run(['bash', str(script)], cwd='/', env=env, capture_output=True)
                self.assertEqual(result.returncode, int(failure), result.stderr)
                self.assertEqual((root / 'log').read_text().splitlines(),
                                 ['env', action, '--name', 'phraise', '--file', str(root / 'phraise.yml')])
                if failure == '1':
                    self.assertNotIn(b'Environment ready', result.stdout)
