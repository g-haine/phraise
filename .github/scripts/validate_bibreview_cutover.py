#!/usr/bin/env python3
"""Validate PHRAISE after the canonical BibReview state cutover."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys

DOCS = Path(__file__).resolve().parents[2] / "docs"
ROOT = DOCS.parent
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config
from bibreview.project import plan_project_merge
from bibreview.storage import json_bytes, read_bibliography
from phraise_tools.bibreview_bridge import publication_to_legacy_record

CANONICAL = DOCS / "assets" / "data" / "bibliography.json"
COLLECTED = DOCS / "assets" / "data" / "collected.json"
LEGACY = DOCS / "assets" / "data" / "biblio.json"

_REPAIRED_REFERENCES = {
    "10.1080/01495739.2021.1917322": "10.1016/j.geomphys.2021.104201",
    "10.1109/tpel.2020.3041653": "10.1007/978-1-4471-0549-7",
}
_MALFORMED_VALUES = {
    "10.1016/j.geomphys. 2021.104201",
    "10.1007/978-1- 4471-0549-7",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    config = load_config(ROOT / "bibreview.yml")
    if config.paths.bibliography != CANONICAL.resolve():
        raise SystemExit("bibreview.yml does not point to canonical bibliography.json")
    if config.paths.collected != COLLECTED.resolve():
        raise SystemExit("bibreview.yml does not point to canonical collected.json")

    publications = read_bibliography(CANONICAL)
    collected = read_bibliography(COLLECTED)
    if len(publications) != 2349:
        raise SystemExit(f"unexpected canonical publication count: {len(publications)}")
    if len({publication.id for publication in publications}) != len(publications):
        raise SystemExit("canonical publication UUIDs are not unique")
    dois = [publication.doi for publication in publications]
    if None in dois or len(set(dois)) != len(dois):
        raise SystemExit("canonical publication DOIs are missing or duplicated")
    if collected:
        raise SystemExit("collected.json must be empty immediately after cutover")

    by_doi = {publication.doi: publication for publication in publications}
    for publication_doi, reference_doi in _REPAIRED_REFERENCES.items():
        publication = by_doi.get(publication_doi)
        if publication is None:
            raise SystemExit(f"missing publication containing repaired reference: {publication_doi}")
        reference_dois = {
            reference.identifiers.get("doi")
            for reference in publication.references
            if reference.identifiers.get("doi") is not None
        }
        if reference_doi not in reference_dois:
            raise SystemExit(
                f"repaired reference DOI {reference_doi} missing from {publication_doi}"
            )

    for publication in publications:
        for reference in publication.references:
            doi = reference.identifiers.get("doi")
            if doi is not None and any(character.isspace() for character in doi):
                raise SystemExit(f"canonical reference DOI contains whitespace: {doi!r}")

    expected_legacy = json_bytes(
        [publication_to_legacy_record(publication) for publication in publications]
    )
    if LEGACY.read_bytes() != expected_legacy:
        raise SystemExit("biblio.json is not the exact projection of canonical state")

    legacy_text = LEGACY.read_text(encoding="utf-8")
    if any(value in legacy_text for value in _MALFORMED_VALUES):
        raise SystemExit("legacy projection still contains a reviewed malformed DOI")
    if any(value not in legacy_text for value in _REPAIRED_REFERENCES.values()):
        raise SystemExit("legacy projection is missing a repaired DOI")

    plan = plan_project_merge(config)
    if plan.incoming_count != 0 or plan.changed:
        raise SystemExit("empty collected state should produce a no-op BibReview merge plan")

    print(f"canonical publications: {len(publications)}")
    print(f"unique canonical UUIDs: {len({publication.id for publication in publications})}")
    print(f"unique canonical DOIs: {len(set(dois))}")
    print("canonical staging batch: empty")
    print("reviewed reference DOI repairs: preserved")
    print("legacy compatibility projection: byte-exact")
    print("empty BibReview merge plan: no-op")
    print(f"bibliography.json SHA-256: {_sha256(CANONICAL)}")
    print(f"biblio.json SHA-256: {_sha256(LEGACY)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
