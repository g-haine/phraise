#!/usr/bin/env python3
"""Compare historical PHRAISE refresh triggers with canonical BibReview refresh.

The legacy workflow removed stale publications before recollection. BibReview
intentionally keeps canonical state intact, writes recollected publications to
``collected.json``, and lets the normal DOI merge update them while preserving
persistent UUIDs. This comparison therefore checks equivalent refresh triggers
and the final canonical effect rather than identical intermediate files.
"""
from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path
import json
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config  # noqa: E402
from bibreview.identity import new_publication_id  # noqa: E402
from bibreview.model import Publication  # noqa: E402
from bibreview.project import apply_project_merge, plan_project_merge  # noqa: E402
from bibreview.project_refresh import apply_project_refresh, plan_project_refresh  # noqa: E402
from bibreview.storage import read_bibliography, write_bibliography  # noqa: E402
from phraise_tools.update import find_updates  # noqa: E402


CHANGED = "10.1000/changed"
MISSING = "10.1000/missing"
UNCHANGED = "10.1000/unchanged"
COMPLETE = "10.1000/complete"
BOOK = "10.1000/book"
ORPHANED = "10.1000/orphaned"
PREEXISTING = "10.1000/preexisting"

CURRENT_BIBTEX = {
    CHANGED: "new changed bibtex\n",
    MISSING: "new missing bibtex\n",
    UNCHANGED: "same bibtex\n",
}


def legacy_record(doi: str, title: str, *, type_: str = "journal-article", volume: str = "", issue: str = "", pages: str = "", permalink: str) -> dict:
    return {
        "doi": doi,
        "type": type_,
        "title": title,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "permalink": permalink,
    }


LEGACY_RECORDS = [
    legacy_record(CHANGED, "Changed", volume="", issue="1", pages="", permalink="changed"),
    legacy_record(MISSING, "Missing", volume="", issue="", pages="", permalink="missing"),
    legacy_record(UNCHANGED, "Unchanged", volume="", issue="2", pages="", permalink="unchanged"),
    legacy_record(COMPLETE, "Complete", volume="1", issue="2", pages="1--2", permalink="complete"),
    legacy_record(BOOK, "Book", type_="book", volume="", issue="", pages="", permalink="book"),
]


class LegacyClient:
    def openalex(self, cursor):
        return {"results": [], "meta": {"next_cursor": None}}

    def bibtex(self, doi):
        return CURRENT_BIBTEX[doi]

    def crossref(self, doi):
        raise AssertionError("discovery must have no candidates in refresh fixture")


class RefreshProvider:
    def __init__(self):
        self.calls = []

    def work(self, doi):
        self.calls.append(doi)
        if doi not in {CHANGED, MISSING}:
            return None
        title = "Changed refreshed" if doi == CHANGED else "Missing refreshed"
        return {
            "type": "journal-article",
            "title": [title],
            "container-title": ["Journal"],
            "created": {"date-parts": [[2026, 9, 17]]},
            "published-print": {"date-parts": [[2026]]},
            "volume": "12",
            "issue": "3",
            "page": "10-20",
        }


def canonical_publication(record: dict) -> Publication:
    return Publication(
        id=new_publication_id(),
        identifiers={"doi": record["doi"]},
        type=record["type"],
        title=record["title"],
        publication_year="2025",
        volume=record["volume"],
        issue=record["issue"],
        pages=record["pages"],
        created_date=date(2025, 1, 2),
        permalink=record["permalink"],
    )


def write_lines(path: Path, values) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{value}\n" for value in values), encoding="utf-8")


def read_lines(path: Path) -> tuple[str, ...]:
    return tuple(path.read_text(encoding="utf-8").splitlines())


def prepare_legacy(root: Path) -> None:
    (root / "assets/data").mkdir(parents=True, exist_ok=True)
    (root / "assets/bib").mkdir(parents=True, exist_ok=True)
    (root / "assets/data/biblio.json").write_text(
        json.dumps(LEGACY_RECORDS, indent=2) + "\n",
        encoding="utf-8",
    )
    write_lines(root / "DOI.txt", (CHANGED, MISSING, UNCHANGED, COMPLETE, BOOK, ORPHANED))
    write_lines(root / "newDOI.txt", (PREEXISTING,))
    write_lines(root / "badDOI.txt", ())
    write_lines(root / "checkDOI.txt", ())
    (root / "assets/bib/changed.bib").write_text("old changed bibtex\n", encoding="utf-8")
    # missing.bib is deliberately absent.
    (root / "assets/bib/unchanged.bib").write_text("same bibtex\n", encoding="utf-8")
    (root / "assets/bib/complete.bib").write_text("complete bibtex\n", encoding="utf-8")
    (root / "assets/bib/book.bib").write_text("book bibtex\n", encoding="utf-8")


def prepare_canonical(root: Path) -> tuple[Publication, ...]:
    publications = tuple(canonical_publication(record) for record in LEGACY_RECORDS)
    write_bibliography(root / "bibliography.json", publications)
    write_bibliography(root / "collected.json", [])
    write_lines(root / "known.txt", (CHANGED, MISSING, UNCHANGED, COMPLETE, BOOK, ORPHANED))
    write_lines(root / "pending.txt", (PREEXISTING,))
    write_lines(root / "rejected.txt", ())
    write_lines(root / "review.txt", ())
    bib = root / "bib"
    bib.mkdir(parents=True, exist_ok=True)
    (bib / "changed.bib").write_text("old changed bibtex\n", encoding="utf-8")
    (bib / "unchanged.bib").write_text("same bibtex\n", encoding="utf-8")
    (bib / "complete.bib").write_text("complete bibtex\n", encoding="utf-8")
    (bib / "book.bib").write_text("book bibtex\n", encoding="utf-8")
    return publications


def main() -> None:
    config = load_config(ROOT / "bibreview.yml")
    assert config.refresh.types == ("journal-article",)
    assert config.refresh.when_missing_any == ("volume", "issue", "pages")

    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        legacy_root = temporary / "legacy"
        canonical_root = temporary / "canonical"
        prepare_legacy(legacy_root)
        canonical_root.mkdir(parents=True)
        canonical_initial = prepare_canonical(canonical_root)
        initial_ids = {publication.doi: publication.id for publication in canonical_initial}

        find_updates(legacy_root, LegacyClient(), max_pages=1, dry_run=False)
        legacy_pending = read_lines(legacy_root / "newDOI.txt")
        legacy_known = read_lines(legacy_root / "DOI.txt")
        legacy_refresh_triggers = tuple(
            doi for doi in legacy_pending if doi not in {PREEXISTING, ORPHANED}
        )
        assert legacy_refresh_triggers == (CHANGED, MISSING)
        assert ORPHANED in legacy_pending
        assert CHANGED not in legacy_known and MISSING not in legacy_known and ORPHANED not in legacy_known
        legacy_retained = json.loads((legacy_root / "assets/data/biblio.json").read_text(encoding="utf-8"))
        assert {record["doi"] for record in legacy_retained} == {UNCHANGED, COMPLETE, BOOK}
        legacy_trash = json.loads((legacy_root / "trash/trash.json").read_text(encoding="utf-8"))
        assert {record["doi"] for record in legacy_trash} == {CHANGED, MISSING}

        paths = config.paths
        canonical_config = replace(
            config,
            paths=replace(
                paths,
                bibliography=canonical_root / "bibliography.json",
                collected=canonical_root / "collected.json",
                known=canonical_root / "known.txt",
                pending=canonical_root / "pending.txt",
                rejected=canonical_root / "rejected.txt",
                review=canonical_root / "review.txt",
                bibtex=canonical_root / "bib",
                archive=canonical_root / "archive",
                site=canonical_root / "site",
            ),
        )
        provider = RefreshProvider()
        before_bibliography = canonical_config.paths.bibliography.read_bytes()
        plan = plan_project_refresh(
            canonical_config,
            provider=provider,
            bibtex_lookup=lambda doi: CURRENT_BIBTEX[doi],
        )

        assert canonical_config.paths.bibliography.read_bytes() == before_bibliography
        assert plan.result.candidates == legacy_refresh_triggers
        assert plan.orphaned_known == (ORPHANED,)
        assert provider.calls == [CHANGED, MISSING]
        assert len(plan.result.items) == 2
        assert len(plan.bibtex_backups) == 1

        apply_project_refresh(plan)
        assert canonical_config.paths.bibliography.read_bytes() == before_bibliography
        staged = read_bibliography(canonical_config.paths.collected)
        assert {publication.doi for publication in staged} == {CHANGED, MISSING}
        assert read_lines(canonical_config.paths.pending) == (PREEXISTING, ORPHANED)
        # Existing stale DOI values remain known because canonical refresh does not
        # delete their authoritative publications before merge.
        assert read_lines(canonical_config.paths.known) == (CHANGED, MISSING, UNCHANGED, COMPLETE, BOOK)
        assert (canonical_config.paths.bibtex / "changed.bib").read_text(encoding="utf-8") == CURRENT_BIBTEX[CHANGED]
        assert (canonical_config.paths.bibtex / "missing.bib").read_text(encoding="utf-8") == CURRENT_BIBTEX[MISSING]
        assert plan.bibtex_backups[0].read_text(encoding="utf-8") == "old changed bibtex\n"

        merge = plan_project_merge(canonical_config)
        apply_project_merge(merge)
        final = read_bibliography(canonical_config.paths.bibliography)
        final_by_doi = {publication.doi: publication for publication in final}
        assert set(final_by_doi) == {CHANGED, MISSING, UNCHANGED, COMPLETE, BOOK}
        assert final_by_doi[CHANGED].id == initial_ids[CHANGED]
        assert final_by_doi[MISSING].id == initial_ids[MISSING]
        assert final_by_doi[CHANGED].volume == "12"
        assert final_by_doi[MISSING].volume == "12"
        assert final_by_doi[UNCHANGED].id == initial_ids[UNCHANGED]
        assert read_bibliography(canonical_config.paths.collected) == ()

        print("PHRAISE refresh/recollect trigger equivalence: OK")
        print("  historical stale triggers: 2")
        print("  canonical staged refreshes: 2")
        print("  orphaned known DOI recovered: 1")
        print("  changed BibTeX backups: 1")
        print("  canonical bibliography unchanged before merge: yes")
        print("  persisted UUIDs retained after merge: yes")
        print("  historical delete-before-recollect step intentionally eliminated")


if __name__ == "__main__":
    main()
