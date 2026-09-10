"""Authentication failure in an optional fallback must preserve useful results."""
from contextlib import redirect_stderr
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phraise_tools.metadata import Client, MetadataError


class MendeleyAuthTests(unittest.TestCase):
    def setUp(self):
        self.client = Client(Path('/nonexistent'), Mock())
        self.client.config = {'MENDELEY_API_KEY': 'secret-token'}
        self.log = io.StringIO()

    def test_preserves_semantic_abstract_and_warns_only_once(self):
        self.client.json = Mock(side_effect=[{'abstract': 'First abstract'}, MetadataError('denied', status_code=401),
                                            {'abstract': 'Second abstract'}])
        with redirect_stderr(self.log):
            self.assertEqual(self.client.complement('10.1/a'), 'First abstract')
            self.assertEqual(self.client.complement('10.1/b'), 'Second abstract')
        self.assertEqual(self.client.json.call_count, 3)
        self.assertEqual(self.log.getvalue().count('warning:'), 1)
        self.assertIn('MENDELEY_API_KEY', self.log.getvalue())
        self.assertNotIn('secret-token', self.log.getvalue())

    def test_both_unavailable_does_not_abort_or_repeat_requests(self):
        self.client.json = Mock(side_effect=[MetadataError('limited', status_code=429), MetadataError('denied', status_code=401)])
        with redirect_stderr(self.log):
            self.assertEqual(self.client.complement('10.1/a'), 'Not available')
            self.assertEqual(self.client.complement('10.1/b'), 'Not available')
        self.assertEqual(self.client.json.call_count, 2)
        self.assertEqual(self.log.getvalue().count('warning:'), 2)

    def test_other_mendeley_errors_remain_visible(self):
        self.client._semantic_scholar_limited = True
        self.client.json = Mock(side_effect=MetadataError('server failure', status_code=503))
        with self.assertRaises(MetadataError):
            self.client.complement('10.1/a')
        self.assertFalse(self.client._mendeley_unauthorized)

    def test_fresh_client_retries_and_missing_token_skips(self):
        self.assertFalse(self.client._mendeley_unauthorized)
        self.client.config = {}
        self.client._semantic_scholar_limited = True
        self.client.json = Mock()
        self.assertEqual(self.client.complement('10.1/a'), 'Not available')
        self.client.json.assert_not_called()
