#!/usr/bin/env python3
"""Merge bibliography updates using the established concatenation conventions.

Requires Python 3.9+. Paths are relative to --root (default: this script's
folder). Validation and staging precede writes; replacements are atomic per
file, not a transaction across files. Do not run concurrent updates.
"""
import argparse
import json
from itertools import chain
import os
from pathlib import Path
import stat
import sys
import tempfile


class Reporter:
    """Small standard-library reporter; concatenate.py remains standalone."""

    def __init__(self, verbosity=0):
        self.verbosity = verbosity

    def step(self, message):
        if self.verbosity >= 0:
            print(f"[*] {message}", file=sys.stderr)

    def detail(self, message):
        if self.verbosity >= 1:
            print(f"    {message}", file=sys.stderr)


def load_bibliography(path):
    """Read an array of records, accepting string or absent/null DOI keys."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as error:
        raise ValueError(f"{path}: {error}") from error
    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a JSON array")
    for index, entry in enumerate(data):
        if not isinstance(entry, dict) or not isinstance(entry.get("doi"), (str, type(None))):
            raise ValueError(f"{path}: record {index + 1} must be an object with a string or null DOI")
    return data


def merge_bibliographies(old, new):
    """Keep the first record per DOI, sorting null before strings for stable output."""
    records = {}
    for entry in chain(old, new):
        records.setdefault(entry.get("doi"), entry)
    return [records[key] for key in sorted(records, key=lambda key: (key is not None, key or ""))]


def lines(data):
    """Split LF-delimited bytes without stripping spaces or CR characters."""
    return data.removesuffix(b"\n").split(b"\n") if data else []


def concatenate(doi, new_doi, bad_doi, biblio, backup_dir, reporter=None,
                dry_run=False):
    """Validate inputs, prepare outputs, then replace bibliography and DOI files."""
    reporter = reporter or Reporter(-1)
    reporter.step("Validating DOI lists and bibliography files")
    backups = sorted((p for p in backup_dir.glob("biblio-*.json") if p.is_file()),
                     key=lambda p: (-p.stat().st_mtime_ns, p.name))
    if not backups:
        raise ValueError(f"{backup_dir}: no biblio-*.json backup found")
    backup = backups[0]
    reporter.detail(f"selected backup: {backup}")
    paths = [doi, new_doi, bad_doi, biblio, backup]
    if len({p.resolve() for p in paths}) != len(paths):
        raise ValueError("Input and output paths must be distinct")
    old, new = load_bibliography(backup), load_bibliography(biblio)
    combined = doi.read_bytes() + new_doi.read_bytes()
    bad = bad_doi.read_bytes()
    # Preserve the established distinction for an unterminated final line.
    json_bad = {line.decode("utf-8") for line in bad.split(b"\n")[:-1]
                if line and not line.startswith(b"#")}
    merged = merge_bibliographies(old, new)
    filtered = [entry for entry in merged if entry.get("doi") not in json_bad]
    doi_bad = set(lines(bad))
    cleaned = b"".join(line + b"\n" for line in lines(combined) if line not in doi_bad)
    outputs = [(biblio, (json.dumps(filtered, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")),
               (doi, cleaned), (new_doi, b"")]
    reporter.step(f"Merging {len(old) + len(new)} record(s): {len(merged)} unique, {len(filtered)} retained")
    if dry_run:
        reporter.step("Would replace bibliography and DOI files")
    else:
        staged = []
        try:
            for path, content in outputs:
                with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as stream:
                    temp = Path(stream.name)
                    staged.append((temp, path))
                    stream.write(content)
                temp.chmod(stat.S_IMODE(path.stat().st_mode))
            reporter.step("Replacing bibliography and DOI files")
            for temp, path in staged:
                os.replace(temp, path)
        finally:
            for temp, _ in staged:
                temp.unlink(missing_ok=True)
    result = f"Backup: {backup}; input: {len(old) + len(new)}; duplicates removed: {len(old) + len(new) - len(merged)}; excluded: {len(merged) - len(filtered)}; retained: {len(filtered)}"
    return f"Dry run: {result}" if dry_run else result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    output = parser.add_mutually_exclusive_group()
    output.add_argument("-v", "--verbose", action="count", default=0,
                        help="Show selected paths and detailed progress")
    output.add_argument("-q", "--quiet", action="store_true",
                        help="Suppress progress and success output")
    parser.add_argument("--dry-run", action="store_true",
                        help="Validate and compute changes without writing files")
    for name, default in [("doi", "DOI.txt"), ("new-doi", "newDOI.txt"), ("bad-doi", "badDOI.txt"),
                          ("biblio", "assets/data/biblio.json"), ("backup-dir", "assets/data")]:
        parser.add_argument(f"--{name}", type=Path, default=Path(default))
    args = parser.parse_args(argv)
    reporter = Reporter(-1 if args.quiet else args.verbose)
    try:
        summary = concatenate(*(args.root / getattr(args, name) for name in
                                ("doi", "new_doi", "bad_doi", "biblio", "backup_dir")),
                              reporter=reporter, dry_run=args.dry_run)
        if not args.quiet:
            print(summary)
    except (OSError, ValueError) as error:
        print(f"concatenate: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
