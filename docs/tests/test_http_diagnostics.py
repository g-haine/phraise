"""Offline regression tests for DOI redirects and sanitized HTTP diagnostics."""
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phraise_tools.metadata import Client, MetadataError


def response(status, url):
    result = requests.Response()
    result.status_code = status
    result.url = url
    result._content = b'{}'
    return result


class HttpDiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.client = Client(Path('/nonexistent'), self.session)

    def test_denied_publisher_landing_page_still_selects_api(self):
        self.client.config['SPRINGER_API_KEY'] = 'test-key'
        for status in (401, 403):
            self.session.get.return_value = response(status, 'https://link.springer.com/article/test')
            with patch.object(self.client, 'json', return_value={'records': [{'abstract': 'Found'}]}) as api:
                self.assertEqual(self.client.publisher('10.1/test'), ('Found', '', ''))
                self.assertEqual(api.call_args.args[0], 'https://api.springernature.com/meta/v2/json')

    def test_denied_doi_resolver_is_not_ignored(self):
        self.session.get.return_value = response(403, 'https://doi.org/10.1/test')
        with self.assertRaisesRegex(MetadataError, r'Publisher lookup for DOI 10.1/test: doi.org: HTTP 403'):
            self.client.publisher('10.1/test')

    def test_bibtex_denial_reports_doi_operation_status_and_final_host(self):
        self.session.get.return_value = response(403, 'https://publisher.test/paper?token=secret-key')
        with self.assertRaises(MetadataError) as error:
            self.client.bibtex('10.1/test')
        self.assertIn('BibTeX lookup for DOI 10.1/test', str(error.exception))
        self.assertIn('doi.org -> publisher.test: HTTP 403', str(error.exception))
        self.assertNotIn('secret-key', str(error.exception))
        self.assertNotIn('/paper', str(error.exception))

    def test_rate_limit_and_server_errors_remain_fatal(self):
        for status in (429, 500, 503):
            self.session.get.return_value = response(status, 'https://publisher.test/paper')
            with self.assertRaisesRegex(MetadataError, f'HTTP {status}'):
                self.client.publisher('10.1/test')
        retry = Client(Path('/nonexistent')).session.get_adapter('https://').max_retries
        self.assertEqual(retry.total, 3)
        self.assertFalse(retry.raise_on_status)

    def test_transport_causes_are_distinguished_without_leaking_secrets(self):
        for failure, expected in [(requests.Timeout, 'timed out'),
                                  (requests.exceptions.SSLError, 'TLS certificate'),
                                  (requests.ConnectionError, 'connection failed'),
                                  (requests.TooManyRedirects, 'too many redirects')]:
            self.session.get.side_effect = failure('secret-key')
            with self.assertRaises(MetadataError) as error:
                self.client.bibtex('10.1/test')
            self.assertIn(expected, str(error.exception))
            self.assertNotIn('secret-key', str(error.exception))

    def test_unknown_denied_publisher_retains_crossref_fallback(self):
        self.session.get.return_value = response(403, 'https://unknown-publisher.test/paper')
        self.assertEqual(self.client.publisher('10.1/test'), ('', '', ''))

    def test_provider_api_denial_remains_fatal(self):
        self.client.config['SPRINGER_API_KEY'] = 'test-key'
        self.session.get.side_effect = [response(403, 'https://link.springer.com/article/test'),
                                       response(401, 'https://api.springernature.com/meta/v2/json?api_key=test-key')]
        with self.assertRaisesRegex(MetadataError, 'api.springernature.com: HTTP 401') as error:
            self.client.publisher('10.1/test')
        self.assertNotIn('test-key', str(error.exception))


if __name__ == '__main__':
    unittest.main()
