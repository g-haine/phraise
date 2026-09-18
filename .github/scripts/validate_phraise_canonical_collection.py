#!/usr/bin/env python3
"""Validate PHRAISE's effective canonical getData -> merge path on real state."""
from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.storage import read_bibliography  # noqa: E402
from phraise_tools.canonical import collect_canonical, merge_canonical  # noqa: E402


NEW_DOI = "10.1/canonical-cutover"
MISSING_DOI = "10.1/canonical-missing"
BIBTEX = "@article{canonical,\n title={{Canonical collection cutover}}\n}\n"


def source_message() -> dict:
    return {
        "title": ["Canonical collection cutover"],
        "type": "journal-article",
        "author": [{"given": "Ada", "family": "Lovelace"}],
        "abstract": "CrossRef abstract",
        "container-title": ["Journal"],
        "created": {"date-parts": [[2026, 9, 18]]},
        "published-print": {"date-parts": [[2026]]},
        "volume": "1",
        "issue": "2",
        "page": "1-5",
        "publisher": "Publisher",
        "subject": ["port-Hamiltonian"],
        "reference": [{"DOI": "10.1/ref"}],
    }


class FakeClient:
    """PHRAISE client contract used by the canonical collection adapter."""

    def crossref(self, doi: str):
        return source_message() if doi == NEW_DOI else None

    def publisher(self, doi: str):
        return "Publisher abstract", "control, energy", "Conference"

    def complement(self, doi: str):
        return "Not available"

    def citation(self, doi: str):
        return "A cited publication"

    def bibtex(self, doi: str):
        return BIBTEX


def copy_if_present(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.exists():
        shutil.copyfile(source, destination)
    else:
        destination.write_text("", encoding="utf-8")


def main() -> None:
    canonical = read_bibliography(DOCS / "assets/data/bibliography.json")
    assert len(canonical) == 2349

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "assets/data").mkdir(parents=True)
        (root / "assets/bib").mkdir(parents=True)

        shutil.copyfile(
            DOCS / "assets/data/bibliography.json",
            root / "assets/data/bibliography.json",
        )
        shutil.copyfile(
            DOCS / "assets/data/biblio.json",
            root / "assets/data/biblio.json",
        )
        copy_if_present(DOCS / "DOI.txt", root / "DOI.txt")
        copy_if_present(DOCS / "badDOI.txt", root / "badDOI.txt")
        copy_if_present(DOCS / "checkDOI.txt", root / "checkDOI.txt")
        pending = root / "newDOI.txt"
        pending.write_text(
            f"{NEW_DOI.upper()}\n{NEW_DOI}\n{MISSING_DOI}\n",
            encoding="utf-8",
        )

        collision = root / "assets/bib/canonical-collection-cutover.bib"
        collision.write_text("existing collision fixture\n", encoding="utf-8")

        canonical_before = (root / "assets/data/bibliography.json").read_bytes()
        legacy_before = (root / "assets/data/biblio.json").read_bytes()

        collect_canonical(root, pending, FakeClient())

        assert (root / "assets/data/bibliography.json").read_bytes() == canonical_before
        assert (root / "assets/data/biblio.json").read_bytes() == legacy_before

        staged = read_bibliography(root / "assets/data/collected.json")
        assert len(staged) == 1
        assert staged[0].doi == NEW_DOI
        staged_id = staged[0].id
        assert pending.read_text(encoding="utf-8") == f"{NEW_DOI}\n{MISSING_DOI}\n"

        expected_bib = root / "assets/bib/canonical-collection-cutover0.bib"
        assert expected_bib.read_text(encoding="utf-8") == BIBTEX

        merge_canonical(root)

        merged = read_bibliography(root / "assets/data/bibliography.json")
        assert len(merged) == 2350
        new = next(publication for publication in merged if publication.doi == NEW_DOI)
        assert new.id == staged_id
        assert read_bibliography(root / "assets/data/collected.json) == ()
        assert pending.read_text(encoding="utf-8") == f"{MISSING_DOI}\n"
        assert NEW_DOI in set((root / "DOI.txt").read_text(encoding="utf-8").splitlines())
        assert (root / "assets/data/biblio.json").read_bytes() == legacy_before

    print("PHRAISE canonical collection cutover: OK")
    print("  real canonical mirror: 2349 -> 2350 publications")
    print("  getData adapter writes collected.json staging: yes")
    print("  bibliography.json unchanged before merge: yes")
    print("  legacy biblio.json untouched by collect and merge: yes")
    print("  DOI normalization / duplicate filtering: correct")
    print("  unavailable DOI remains pending: yes")
    print("  BibTeX slug collision handling: correct")
    print("  staged UUID preserved through merge: yes")


if __name__ == "__main__":
    main()
