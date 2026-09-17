#!/usr/bin/env python3
"""Read-only integration validation of PHRAISE bibliography through BibReview."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from bibreview.compat import legacy_records, load_legacy_bibliography


BIBLIOGRAPHY = Path("docs/assets/data/biblio.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    before_hash = sha256(BIBLIOGRAPHY)
    source_records = json.loads(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    items = load_legacy_bibliography(BIBLIOGRAPHY)

    publication_ids = [item.publication.id for item in items]
    dois = [item.publication.doi for item in items if item.publication.doi is not None]
    roundtrip_records = legacy_records(items)

    if len(items) != len(source_records):
        raise SystemExit("BibReview changed the publication count during legacy loading")
    if len(set(publication_ids)) != len(publication_ids):
        raise SystemExit("BibReview produced duplicate internal publication UUIDs")
    if len(set(dois)) != len(dois):
        raise SystemExit("PHRAISE bibliography contains duplicate normalized DOIs")
    if roundtrip_records != source_records:
        raise SystemExit("Legacy -> BibReview -> legacy round-trip is not lossless")

    after_hash = sha256(BIBLIOGRAPHY)
    if before_hash != after_hash:
        raise SystemExit("Read-only BibReview validation modified biblio.json")

    print(f"publications: {len(items)}")
    print(f"unique internal UUIDs: {len(set(publication_ids))}")
    print(f"DOI-backed publications: {len(dois)}")
    print(f"unique normalized DOIs: {len(set(dois))}")
    print("legacy round-trip: exact")
    print(f"biblio.json SHA-256 unchanged: {before_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
