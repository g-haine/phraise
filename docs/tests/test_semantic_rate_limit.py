"""Semantic Scholar throttling must not abort optional abstract enrichment."""
from contextlib import redirect_stderr
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phraise_tools.metadata import Client, MetadataError, enriched_fields


def response(status, content=b'{}'):
    result = requests.Response()
    result.status_code = status
    result.url = 'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1/test'
    result._content = content
    return result


class SemanticRateLimitTests(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.client = Client(Path('/nonexistent'), self.session)
        self.client.config = {}

    def test_429_warns_once_and_skips_later_dois(self):
        self.session.get.return_value = response(429)
        log = io.StringIO()
        with redirect_stderr(log):
            self.assertEqual(self.client.complement('10.1/first'), 'Not available')
            self.assertEqual(self.client.complement('10.1/second'), 'Not available')
        self.assertEqual(self.session.get.call_count, 1)
        self.assertEqual(log.getvalue().count('warning:'), 1)
        self.assertIn('HTTP 429', log.getvalue())

    def test_mendeley_still_provides_abstract(self):
        self.client.config['MENDELEY_API_KEY'] = 'test-token'
        abstract = ' '.join(['word'] * 45)
        page = response(200, f'<meta name="citation_abstract" content="{abstract}">'.encode())
        self.session.get.side_effect = [response(429), response(200, b'[{"link":"https://mendeley.test/paper"}]'), page,
                                       response(200, b'[{"link":"https://mendeley.test/paper"}]'), page]
        with redirect_stderr(io.StringIO()):
            self.assertEqual(self.client.complement('10.1/first'), abstract)
            self.assertEqual(self.client.complement('10.1/second'), abstract)
        self.assertEqual(self.session.get.call_count, 5)

    def test_other_errors_are_not_swallowed(self):
        for status in (401, 403, 503):
            self.session.get.return_value = response(status)
            with self.assertRaises(MetadataError) as error:
                self.client.complement('10.1/test')
            self.assertEqual(error.exception.status_code, status)
            self.assertFalse(self.client._semantic_scholar_limited)

    def test_new_client_retries_provider(self):
        self.client._semantic_scholar_limited = True
        fresh = Client(Path('/nonexistent'), self.session)
        fresh.config = {}
        self.session.get.return_value = response(200, b'{"abstract":"Recovered abstract"}')
        self.assertEqual(fresh.complement('10.1/test'), 'Recovered abstract')

    def test_discovery_can_continue_with_title_and_keywords(self):
        self.session.get.return_value = response(429)
        with patch.object(self.client, 'publisher', return_value=('', '', '')), redirect_stderr(io.StringIO()):
            self.assertEqual(enriched_fields({'subject': ['port-Hamiltonian']}, '10.1/test', self.client, discovery=True),
                             ('Not available', 'port-Hamiltonian', ''))

    def test_existing_crossref_abstract_is_preserved_without_request(self):
        with patch.object(self.client, 'publisher', return_value=('', '', '')):
            self.assertEqual(enriched_fields({'abstract': 'CrossRef text'}, '10.1/test', self.client),
                             ('CrossRef text', '', ''))
        self.session.get.assert_not_called()
