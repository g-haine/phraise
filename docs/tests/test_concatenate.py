"""Regression tests; fixtures are synthetic and all writes stay in temp dirs."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

DOCS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("concatenate", DOCS / "concatenate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ConcatenateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.fixture(self.root)

    def fixture(self, root):
        data = root / "assets/data"
        data.mkdir(parents=True)
        (root / "DOI.txt").write_bytes(b"z\na\n#comment\n\nbad\n")
        (root / "newDOI.txt").write_bytes(b"b\na\n")
        (root / "badDOI.txt").write_bytes(b"#comment\n\nbad\n")
        (data / "biblio.json").write_text(json.dumps([{"doi": "a", "title": "new"}, {"doi": "b"}, {"doi": "bad"}]))
        (data / "biblio-recent.json").write_text(json.dumps([{"doi": "z"}, {"doi": "a", "title": "Énergie"}, {"title": "missing"}, {"doi": None}]))
        (data / "biblio-old.json").write_text('[{"doi":"wrong"}]')
        os.utime(data / "biblio-old.json", (100, 100))
        os.utime(data / "biblio-recent.json", (200, 200))

    def run_python(self, root=None):
        root = root or self.root
        return module.concatenate(*(root / name for name in (
            "DOI.txt", "newDOI.txt", "badDOI.txt", "assets/data/biblio.json", "assets/data")))

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def test_merge_and_filter(self):
        self.run_python()
        records = json.loads((self.root / 'assets/data/biblio.json').read_text())
        self.assertEqual(records, [{"title": "missing"}, {"doi": "a", "title": "Énergie"}, {"doi": "b"}, {"doi": "z"}])
        self.assertEqual((self.root / 'DOI.txt').read_bytes(), b'z\na\nb\na\n')
        self.assertEqual((self.root / 'newDOI.txt').read_bytes(), b'')

    @unittest.skipUnless(shutil.which('bash') and shutil.which('jq'), 'Bash and jq required')
    def test_shell_parity(self):
        for bad in [b'#comment\n\nbad\n', b'bad', b'', b'a\r\nbad\n']:
            with self.subTest(bad=bad), tempfile.TemporaryDirectory() as directory:
                shell = Path(directory) / 'shell'
                python = Path(directory) / 'python'
                for root in [shell, python]:
                    self.fixture(root)
                    (root / 'badDOI.txt').write_bytes(bad)
                    (root / 'newDOI.txt').write_bytes(b'b\na')
                shutil.copy(DOCS / '.utils', shell / '.utils')
                (shell / '.env').touch()
                subprocess.run(['bash', str(DOCS / 'concatenate.sh')], cwd=shell, check=True, capture_output=True)
                self.run_python(python)
                for name in ['DOI.txt', 'newDOI.txt']:
                    self.assertEqual((shell / name).read_bytes(), (python / name).read_bytes())
                self.assertEqual(json.loads((shell / 'assets/data/biblio.json').read_bytes()),
                                 json.loads((python / 'assets/data/biblio.json').read_bytes()))

    def test_invalid_json_or_schema_preserves_inputs(self):
        for content in ['{', '{}', '[1]', '[{"doi":12}]']:
            with self.subTest(content=content):
                (self.root / 'assets/data/biblio.json').write_text(content)
                before = self.snapshot()
                with self.assertRaises(ValueError):
                    self.run_python()
                self.assertEqual(before, self.snapshot())

    def test_missing_inputs_preserves_files(self):
        for name in ['DOI.txt', 'newDOI.txt', 'badDOI.txt', 'assets/data/biblio.json']:
            path = self.root / name
            content = path.read_bytes()
            path.unlink()
            before = self.snapshot()
            with self.assertRaises(OSError):
                self.run_python()
            self.assertEqual(before, self.snapshot())
            path.write_bytes(content)

    def test_no_backup(self):
        for path in self.root.glob('assets/data/biblio-*.json'):
            path.unlink()
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'no biblio'):
            self.run_python()
        self.assertEqual(before, self.snapshot())

    def test_all_dois_filtered(self):
        (self.root / 'badDOI.txt').write_bytes(b'z\na\nb\nbad\n#comment\n\n')
        self.run_python()
        self.assertEqual((self.root / 'DOI.txt').read_bytes(), b'')

    def test_staging_failure_preserves_inputs_and_cleans_temps(self):
        before = self.snapshot()
        original = module.tempfile.NamedTemporaryFile
        count = 0
        def fail_second(*args, **kwargs):
            nonlocal count
            count += 1
            if count == 2:
                raise OSError('staging failed')
            return original(*args, **kwargs)
        with patch.object(module.tempfile, 'NamedTemporaryFile', side_effect=fail_second):
            with self.assertRaises(OSError):
                self.run_python()
        self.assertEqual(before, self.snapshot())

    def test_cli_from_root_and_docs(self):
        for cwd in [DOCS, DOCS.parent]:
            result = subprocess.run([sys.executable, str(DOCS / 'concatenate.py'), '--root', str(self.root)], cwd=cwd, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_default_root_is_script_directory(self):
        shutil.copy(DOCS / 'concatenate.py', self.root / 'concatenate.py')
        result = subprocess.run([sys.executable, str(self.root / 'concatenate.py')], cwd=DOCS.parent, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_cli_error(self):
        (self.root / 'assets/data/biblio.json').write_text('{')
        result = subprocess.run([sys.executable, str(DOCS / 'concatenate.py'), '--root', str(self.root)], capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn(b'biblio.json', result.stderr)
        self.assertNotIn(b'Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
