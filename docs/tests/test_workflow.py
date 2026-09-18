"""Offline integration tests. No real credentials, data or network are used."""
from copy import deepcopy
import base64
import io
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
from bibreview.compat import legacy_record_to_publication
from bibreview.storage import write_bibliography
from phraise_tools.collect import collect
from phraise_tools.common import json_bytes, mathjaxify, Reporter, slugify, write_batch
from phraise_tools.generate import (apply_safe_author_mappings, author_mapping_plan,
                                    format_author_mapping_plan, generate_pages,
                                    generate_posts, render_post)
from phraise_tools.metadata import (Client, MetadataError, extract_provider, format_bibtex,
                                    mendeley_abstract)
from phraise_tools.update import find_updates, is_relevant
from concatenate import concatenate
import requests

DOCS = Path(__file__).resolve().parents[1]
LEGACY = DOCS / 'tests/fixtures/legacy'


def record(doi='10.1/old', slug='old'):
    return {'doi': doi, 'title': 'Port-Hamiltonian systems', 'type': 'journal-article',
            'authors': [{'given': 'Ada', 'family': 'Lovelace'}], 'abstract': 'An abstract.',
            'journal': 'Journal', 'year': '2024', 'volume': '1', 'issue': '2', 'pages': '1--9',
            'event': '', 'isbn': '', 'publisher': 'Publisher', 'keywords': 'control; energy',
            'dateY': '2024', 'dateM': '3', 'dateD': '8', 'permalink': slug, 'references': []}


def write_canonical_fixture(root, records):
    """Write canonical BibReview state corresponding to synthetic legacy records."""
    publications = tuple(
        legacy_record_to_publication(item).publication
        for item in records
    )
    write_bibliography(root / 'assets/data/bibliography.json', publications)


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
        initial_records = [record()]
        self.save('assets/data/biblio.json', initial_records)
        write_canonical_fixture(self.root, initial_records)
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

    def test_dry_run_all_workflow_stages_leave_every_file_unchanged(self):
        (self.root / 'newDOI.txt').write_text('10.1/new\n')
        self.client.messages['10.1/new'] = message()
        self.client.pages['*']['results'] = [
            {'doi': 'https://doi.org/10.1/new'}]
        (self.root / '_posts/obsolete.md').write_text('obsolete')
        (self.root / 'assets/bib/orphan.bib').write_text('orphan')
        backup = self.root / 'assets/data/biblio-backup.json'
        backup.write_bytes((self.root / 'assets/data/biblio.json').read_bytes())
        before = self.snapshot()

        results = [
            collect(self.root, self.root / 'newDOI.txt', self.client,
                    dry_run=True),
            find_updates(self.root, self.client, dry_run=True),
            concatenate(*(self.root / path for path in [
                'DOI.txt', 'newDOI.txt', 'badDOI.txt',
                'assets/data/biblio.json', 'assets/data']), dry_run=True),
            generate_posts(self.root, self.client, dry_run=True),
            generate_pages(self.root, dry_run=True),
        ]

        self.assertTrue(all(result.startswith('Dry run:') for result in results))
        self.assertEqual(before, self.snapshot())

    def test_collection_failure_leaves_inputs_unchanged(self):
        (self.root / 'newDOI.txt').write_text('10.1/a\n10.1/b\n')
        self.client.messages['10.1/a'] = message()
        before = self.snapshot()
        with patch.object(self.client, 'bibtex', side_effect=MetadataError('offline')):
            with self.assertRaises(MetadataError):
                collect(self.root, self.root / 'newDOI.txt', self.client)
        self.assertEqual(before, self.snapshot())

    def test_author_plan_is_structured_and_does_not_write(self):
        self.save('assets/data/author_mappings.json', {})
        before = self.snapshot()
        plan = author_mapping_plan(self.root)
        self.assertEqual(plan['safe'], {'ada-lovelace': ['Ada Lovelace']})
        self.assertEqual(plan['review'], [])
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

    def test_site_writer_ignores_legacy_bibliography_projection(self):
        legacy = self.root / 'assets/data/biblio.json'
        legacy.write_text('{ deliberately invalid legacy projection', encoding='utf-8')
        before = legacy.read_bytes()

        generate_posts(self.root, self.client)
        generate_pages(self.root)

        self.assertTrue((self.root / '_posts/2024-03-08-old.md').exists())
        self.assertTrue((self.root / 'authors/ada-lovelace.md').exists())
        self.assertEqual(legacy.read_bytes(), before)

    def test_generation_error_preserves_existing_outputs(self):
        (self.root / '_posts/keep.md').write_text('keep')
        self.save('assets/data/author_mappings.json', {})
        before = self.snapshot()
        for function in [lambda: generate_posts(self.root, self.client), lambda: generate_pages(self.root)]:
            with self.assertRaisesRegex(ValueError, 'unmapped author'):
                function()
            self.assertEqual(before, self.snapshot())

    def test_unsafe_and_duplicate_permalink_rejected(self):
        for slug in ['../escape', 'old']:
            records = [record(), record('10.1/other', slug)]
            self.save('assets/data/biblio.json', records)
            write_canonical_fixture(self.root, records)
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
        self.assertEqual(author_mapping_plan(self.root)['unknown_names'], 0)
        concatenate(*(self.root / p for p in ['DOI.txt', 'newDOI.txt', 'badDOI.txt', 'assets/data/biblio.json', 'assets/data']))
        # The production migration branch now expects BibReview's canonical
        # collect -> merge handoff.  This synthetic legacy workflow explicitly
        # materializes that handoff so generation is tested from canonical state.
        write_canonical_fixture(
            self.root,
            self.load('assets/data/biblio.json'),
        )
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
            self.assertIn(b'--dry-run', result.stdout)
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


class LegacyGoldenTests(unittest.TestCase):
    setUp = WorkflowTests.setUp
    save = WorkflowTests.save
    # Golden files capture the outputs of the validated workflow before cleanup.
    def test_post_golden(self):
        generate_posts(self.root, self.client)
        self.assertEqual((self.root / '_posts/2024-03-08-old.md').read_bytes(),
                         base64.b64decode((LEGACY / 'post.b64').read_text()))

    def test_common_formatting_golden(self):
        for source, expected in json.loads((LEGACY / 'mathjax.json').read_text()).items():
            self.assertEqual(mathjaxify(source), expected)
        raw = (LEGACY / 'bibtex_input.txt').read_text().rstrip('\n')
        self.assertEqual(format_bibtex(raw), (LEGACY / 'bibtex_output.bib').read_text())

    def test_pages_golden(self):
        generate_pages(self.root)
        for expected in (LEGACY / 'pages').rglob('*.md'):
            actual = self.root / expected.relative_to(LEGACY / 'pages')
            self.assertEqual(actual.read_bytes(), expected.read_bytes())

    def test_collection_golden(self):
        (self.root / 'newDOI.txt').write_text('10.1/NEW\n10.1/new\n')
        self.client.messages['10.1/new'] = message()
        collect(self.root, self.root / 'newDOI.txt', self.client)
        self.assertEqual(json.loads((self.root / 'assets/data/biblio.json').read_text()),
                         json.loads((LEGACY / 'collection/biblio.json').read_text()))
        self.assertEqual((self.root / 'newDOI.txt').read_bytes(),
                         (LEGACY / 'collection/newDOI.txt').read_bytes())
        self.assertEqual((self.root / 'assets/bib/port-hamiltonian-systems.bib').read_bytes(),
                         (LEGACY / 'collection/publication.bib').read_bytes())

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


class ReportingTests(unittest.TestCase):
    setUp = WorkflowTests.setUp
    save = WorkflowTests.save

    def test_reporter_levels(self):
        stream = io.StringIO()
        reporter = Reporter(0, stream)
        reporter.step('step')
        reporter.detail('detail')
        reporter.debug('debug')
        reporter.warning('warning')
        self.assertEqual(stream.getvalue(), '[*] step\nphraise: warning: warning\n')

        stream = io.StringIO()
        reporter = Reporter(2, stream)
        reporter.step('step')
        reporter.detail('detail')
        reporter.debug('debug')
        self.assertEqual(stream.getvalue(), '[*] step\n    detail\n      debug\n')

    def test_cli_default_verbose_and_quiet_output(self):
        command = [sys.executable, str(DOCS / 'setPages.py'), '--root', str(self.root)]
        normal = subprocess.run(command, capture_output=True)
        self.assertEqual(normal.returncode, 0, normal.stderr)
        self.assertIn(b'[*] Indexing authors and years', normal.stderr)
        self.assertNotIn(b'authors/ada-lovelace.md:', normal.stderr)

        verbose = subprocess.run(command + ['-v'], capture_output=True)
        self.assertEqual(verbose.returncode, 0, verbose.stderr)
        self.assertIn(b'authors/ada-lovelace.md:', verbose.stderr)

        quiet = subprocess.run(command + ['--quiet'], capture_output=True)
        self.assertEqual(quiet.returncode, 0, quiet.stderr)
        self.assertEqual(quiet.stdout, b'')
        self.assertEqual(quiet.stderr, b'')

    def test_http_debug_is_sanitized(self):
        session = Mock()
        response = session.get.return_value
        response.status_code = 200
        response.url = 'https://publisher.test/paper?token=secret'
        response.raise_for_status.return_value = None
        stream = io.StringIO()
        client = Client(Path('/nonexistent'), session, Reporter(2, stream))
        client.request('https://doi.org/10.1/test?api_key=secret',
                       context='Publisher lookup for DOI 10.1/test')
        output = stream.getvalue()
        self.assertIn('GET doi.org', output)
        self.assertIn('HTTP 200 from doi.org -> publisher.test', output)
        self.assertNotIn('secret', output)


class AuthorMappingPlanTests(unittest.TestCase):
    setUp = WorkflowTests.setUp
    save = WorkflowTests.save
    load = WorkflowTests.load
    snapshot = WorkflowTests.snapshot

    def prepare_unknown_authors(self):
        records = []
        for index, name in enumerate(['Grace Hopper', 'A. Lovelace', 'José Núñez', 'Jose Nunez']):
            given, family = name.rsplit(' ', 1)
            item = record(f'10.1/{index}', f'publication-{index}')
            item['authors'] = [{'given': given, 'family': family}]
            records.append(item)
        self.save('assets/data/biblio.json', records)

    def test_plan_separates_safe_and_ambiguous_names(self):
        self.prepare_unknown_authors()
        plan = author_mapping_plan(self.root)
        self.assertEqual(plan['safe'], {'grace-hopper': ['Grace Hopper']})
        review = {item['slug']: item for item in plan['review']}
        self.assertIn('same surname and first initial', review['a-lovelace']['reason'])
        self.assertEqual(review['a-lovelace']['possible_matches'][0]['slug'], 'ada-lovelace')
        self.assertIn('several unknown names', review['jose-nunez']['reason'])
        report = format_author_mapping_plan(plan)
        self.assertIn('Safe proposals:', report)
        self.assertIn('Manual review required:', report)

    def test_apply_safe_is_atomic_and_idempotent(self):
        self.prepare_unknown_authors()
        stream = io.StringIO()
        applied, remaining = apply_safe_author_mappings(self.root, Reporter(1, stream))
        mapping = self.load('assets/data/author_mappings.json')
        self.assertEqual(applied, 1)
        self.assertEqual(mapping['grace-hopper'], ['Grace Hopper'])
        self.assertEqual(mapping['ada-lovelace'], ['Ada Lovelace'])
        self.assertNotIn('a-lovelace', mapping)
        self.assertEqual(remaining['unknown_names'], 3)
        self.assertIn('added grace-hopper', stream.getvalue())
        applied_again, _ = apply_safe_author_mappings(self.root)
        self.assertEqual(applied_again, 0)

    def test_apply_safe_dry_run_reports_without_writing(self):
        self.prepare_unknown_authors()
        before = self.snapshot()
        stream = io.StringIO()
        applied, plan = apply_safe_author_mappings(
            self.root, Reporter(1, stream), dry_run=True)
        self.assertEqual(applied, 1)
        self.assertEqual(plan['safe'], {'grace-hopper': ['Grace Hopper']})
        self.assertIn('would add grace-hopper', stream.getvalue())
        self.assertEqual(before, self.snapshot())

    def test_cli_json_and_apply_safe(self):
        self.prepare_unknown_authors()
        command = [sys.executable, str(DOCS / 'setAuthorMapping.py'), '--root', str(self.root)]
        analysis = subprocess.run(command + ['--json', '--quiet'], capture_output=True)
        self.assertEqual(analysis.returncode, 0, analysis.stderr)
        # JSON is the requested data output; quiet suppresses only progress.
        self.assertEqual(json.loads(analysis.stdout)['applied'], 0)
        self.assertEqual(analysis.stderr, b'')

        applied = subprocess.run(command + ['--apply-safe', '--json'], capture_output=True)
        self.assertEqual(applied.returncode, 0, applied.stderr)
        report = json.loads(applied.stdout)
        self.assertEqual(report['applied'], 1)
        self.assertEqual(report['unknown_names'], 3)

    def test_cli_apply_safe_dry_run_json(self):
        self.prepare_unknown_authors()
        before = self.snapshot()
        command = [sys.executable, str(DOCS / 'setAuthorMapping.py'),
                   '--root', str(self.root), '--apply-safe', '--dry-run',
                   '--json', '--quiet']
        result = subprocess.run(command, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report['dry_run'])
        self.assertEqual(report['applied'], 0)
        self.assertEqual(report['would_apply'], 1)
        self.assertEqual(before, self.snapshot())

        human = subprocess.run(command[:-2], capture_output=True)
        self.assertEqual(human.returncode, 0, human.stderr)
        self.assertTrue(human.stdout.startswith(b'Dry run:'))
        self.assertEqual(before, self.snapshot())
