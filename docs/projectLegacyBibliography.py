#!/usr/bin/env python3
"""Project canonical BibReview state onto PHRAISE's temporary legacy schema."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config
from bibreview.storage import atomic_write, json_bytes, read_bibliography
from phraise_tools.bibreview_bridge import publication_to_legacy_record

LEGACY = DOCS / "assets" / "data" / "biblio.json"


def projected_bytes() -> bytes:
    """Return the deterministic PHRAISE legacy projection of canonical state."""
    config = load_config(ROOT / "bibreview.yml")
    publications = read_bibliography(config.paths.bibliography)
    records = [publication_to_legacy_record(publication) for publication in publications]
    return json_bytes(records)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Project canonical BibReview state onto PHRAISE biblio.json."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that biblio.json already matches the canonical projection",
    )
    args = parser.parse_args()

    expected = projected_bytes()
    if args.check:
        current = LEGACY.read_bytes()
        if current != expected:
            raise SystemExit("legacy bibliography projection is out of date")
        print("legacy bibliography projection: exact")
        return 0

    atomic_write(LEGACY, expected)
    print(f"legacy bibliography projection written: {LEGACY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
