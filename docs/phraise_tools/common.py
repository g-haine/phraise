"""Shared CLI, validation, text handling and staged file writes."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, datetime
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
from typing import Mapping

from unidecode import unidecode

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Reporter:
    """Write consistent progress messages without exposing sensitive values."""

    verbosity: int = 0
    stream: object = None

    def step(self, message: str) -> None:
        if self.verbosity >= 0:
            print(f'[*] {message}', file=self.stream or sys.stderr)

    def detail(self, message: str) -> None:
        if self.verbosity >= 1:
            print(f'    {message}', file=self.stream or sys.stderr)

    def debug(self, message: str) -> None:
        if self.verbosity >= 2:
            print(f'      {message}', file=self.stream or sys.stderr)

    def warning(self, message: str) -> None:
        print(f'phraise: warning: {message}', file=self.stream or sys.stderr)


def parser(description: str) -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=description)
    result.add_argument('--root', type=Path, default=ROOT,
                        help='Data directory (default: docs beside these scripts)')
    output = result.add_mutually_exclusive_group()
    output.add_argument('-v', '--verbose', action='count', default=0,
                        help='Show DOI/file details; repeat (-vv) for HTTP diagnostics')
    output.add_argument('-q', '--quiet', action='store_true',
                        help='Suppress progress and success output; errors and warnings remain')
    result.add_argument('--dry-run', action='store_true',
                        help='Validate and compute changes without writing or deleting files')
    return result


def summary(message: str, dry_run: bool) -> str:
    """Make simulations unmistakable in command output."""
    return f'Dry run: {message}' if dry_run else message


def run_cli(action, args) -> int:
    args.reporter = Reporter(-1 if args.quiet else args.verbose)
    try:
        summary = action(args)
        if summary and (not args.quiet or getattr(args, 'json', False)):
            print(summary)
    except (OSError, ValueError) as error:
        print(f'phraise: {error}', file=sys.stderr)
        return 1
    return 0


def read_json(path: Path, expected_type):
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, UnicodeError) as error:
        raise ValueError(f'{path}: {error}') from error
    if not isinstance(value, expected_type):
        raise ValueError(f'{path}: expected {expected_type.__name__}')
    return value


def bibliography(root: Path) -> list[dict]:
    path = root / 'assets/data/biblio.json'
    records = read_json(path, list)
    for index, record in enumerate(records):
        if not isinstance(record, dict) or not isinstance(record.get('doi'), str) or not record['doi']:
            raise ValueError(f'{path}: record {index + 1} needs a non-empty DOI string')
        authors = record.get('authors')
        if authors is not None and (not isinstance(authors, list) or any(not isinstance(a, dict) for a in authors)):
            raise ValueError(f'{path}: invalid authors for {record["doi"]}')
    return records


def mappings(root: Path) -> tuple[dict, dict]:
    path = root / 'assets/data/author_mappings.json'
    mapping = read_json(path, dict)
    reverse = {}
    for slug, names in mapping.items():
        safe_component(slug)
        if not isinstance(names, list) or not names or any(not isinstance(n, str) or not n for n in names):
            raise ValueError(f'{path}: {slug} needs a non-empty list of names')
        for name in names:
            if name in reverse and reverse[name] != slug:
                raise ValueError(f'{path}: ambiguous author {name!r}')
            reverse[name] = slug
    return mapping, reverse


def text(value) -> str:
    """Represent a nullable scalar; use an explicit default at call sites if needed."""
    return 'null' if value is None else str(value)


def author_names(record: dict) -> list[str]:
    """Render legacy author records using the canonical missing-given-name policy."""
    result = []
    for author in record.get('authors') or []:
        family = author.get('family')
        if not family:
            continue
        given = author.get('given')
        result.append(f'{given} {family}'.strip() if given else str(family).strip())
    return result


def slugify(value: str) -> str:
    """Portable ASCII transliteration; preserve the legacy 240-character limit."""
    return re.sub('[^a-z0-9]+', '-', unidecode(value[:240]).lower()).strip('-')


def safe_component(value: str) -> str:
    if not isinstance(value, str) or not value or value in {'.', '..', 'index'} or re.search(r'[/\\\x00-\x1f<>:"|?*]', value):
        raise ValueError(f'Unsafe or reserved file name: {value!r}')
    return value


def record_date(record: dict) -> str:
    try:
        return date(*(int(record[f'date{part}']) for part in 'YMD')).isoformat()
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(f'Invalid creation date for {record.get("doi")}') from error


def mathjaxify(value: str) -> str:
    """Keep the existing Liquid escaping and dollar-math conventions."""
    value = value.replace('{{', '{[[:space:]]{').replace('}}', '}[[:space:]]}')
    result = []
    for line in value.split('\n'):
        pieces = line.split('$')
        result.append(''.join(piece + (('\\\\( ' if i % 2 == 0 else ' \\\\)') if i < len(pieces) - 1 else '')
                              for i, piece in enumerate(pieces)))
    return '\n'.join(result)


def clean_metadata(value: str, abstract: bool = False) -> str:
    value = re.sub(r'[\x00-\x19]', '', value).strip()
    value = re.sub(r'<[^>]*jats[^>]*>', '', value)
    return re.sub('summary|abstract', '', value, flags=re.I) if abstract else value


def read_lines(path: Path) -> list[str]:
    # Retain exact contents except LF; normalize only where the workflow did.
    data = path.read_bytes().decode('utf-8')
    return data.removesuffix('\n').split('\n') if data else []


def lines_bytes(values) -> bytes:
    return ''.join(f'{value}\n' for value in values).encode('utf-8')


def json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')


def write_batch(outputs: Mapping[Path, bytes]) -> None:
    """Stage every file before replacement. Atomic per file, not per batch."""
    staged = []
    try:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f'.{path.name}.', delete=False) as stream:
                temporary = Path(stream.name)
                staged.append((temporary, path))
                stream.write(content)
            temporary.chmod(stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644)
        for temporary, path in staged:
            os.replace(temporary, path)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)


def backup_path(directory: Path, prefix: str, suffix: str) -> Path:
    """Portable timestamp without colons, including collision protection."""
    stamp = datetime.now().astimezone().strftime('%Y-%m-%dT%H-%M-%S%z')
    path = directory / f'{prefix}-{stamp}{suffix}'
    count = 0
    while path.exists():
        count += 1
        path = directory / f'{prefix}-{stamp}-{count}{suffix}'
    return path