#!/usr/bin/env python3
"""Exercise canonical BibReview collect -> merge on a real PHRAISE state mirror."""
from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import shutil
import tempfile

from bibreview.config import load_config
from bibreview.pipeline.enrich import EnrichmentService
from bibreview.providers.base import Enrichment
from bibreview.project import (
    apply_project_collection,
    apply_project_merge,
    plan_project_collection,
    plan_project_merge,
)
from bibreview.storage import read_bibliography, write_bibliography


ROOT = Path(__file__).resolve().parents[2]
KNOWN_DOI = "10.1002/acs.2433"
NEW_DOI = "10.1/new"
MISSING_DOI = "10.1/missing"
BIBTEX = "@article{new,\n  title={{Canonical project collection}}\n}\n"


def source_message() -> dict:
    return {
        "title": ["Canonical project collection"],
        "type": "journal-article",
        "author": [{
            "given": "Ada",
            "family": "Lovelace",
            "sequence": "first",
            "affiliation": [{"name": "Example Institute"}],
        }],
        "abstract": "CrossRef abstract",
        "container-title": ["Journal"],
        "created": {"date-parts": [[2026, 9, 17]]},
        "published-print": {"date-parts": [[2026]]},
        "volume": "1",
        "issue": "2",
        "page": "1-5",
        "publisher": "Publisher",
        "subject": ["port-Hamiltonian"],
        "reference": [{"DOI": "10.1/ref"}],
    }


class WorkProvider:
    def work(self, doi: str):
        return source_message() if doi == NEW_DOI else None


class PublisherProvider:
    def enrich(self, doi: str) -> Enrichment:
        return Enrichment(
            abstract="Publisher abstract",
            keywords=("control", "energy"),
            event="Conference",
        )


def copy_if_present(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.exists():
        shutil.copyfile(source, destination)
    else:
        destination.write_text("", encoding="utf-8")


def main() -> int:
    config = load_config(ROOT / "bibreview.yml")
    canonical = read_bibliography(config.paths.bibliography)
    if len(canonical) != 2349:
        raise AssertionError(f"unexpected PHRAISE canonical count: {len(canonical)}")
    if KNOWN_DOI not in {publication.doi for publication in canonical}:
        raise AssertionError(f"fixture known DOI is absent from PHRAISE: {KNOWN_DOI}")

    with tempfile.TemporaryDirectory() as directory:
        temp = Path(directory)
        paths = replace(
            config.paths,
            bibliography=temp / "bibliography.json",
            collected=temp / "collected.json",
            author_mappings=temp / "author_mappings.json",
            known=temp / "DOI.txt",
            pending=temp / "newDOI.txt",
            rejected=temp / "badDOI.txt",
            review=temp / "checkDOI.txt",
            bibtex=temp / "bib",
            archive=temp / "archive",
            site=temp / "site",
        )
        mirror = replace(config, paths=paths)

        shutil.copyfile(config.paths.bibliography, paths.bibliography)
        copy_if_present(config.paths.known, paths.known)
        copy_if_present(config.paths.rejected, paths.rejected)
        copy_if_present(config.paths.review, paths.review)
        write_bibliography(paths.collected, ())
        paths.pending.write_text(
            f"{KNOWN_DOI}\n{NEW_DOI}\n{MISSING_DOI}\n{NEW_DOI.upper()}\n",
            encoding="utf-8",
        )
        paths.bibtex.mkdir(parents=True, exist_ok=True)
        (paths.bibtex / "canonical-project-collection.bib").write_text(
            "existing collision fixture\n",
            encoding="utf-8",
        )

        service = EnrichmentService(publisher=PublisherProvider())
        before = paths.bibliography.read_bytes()
        plan = plan_project_collection(
            mirror,
            provider=WorkProvider(),
            enrichment_lookup=service.for_collection,
            citation_lookup=lambda doi: "A cited publication",
            bibtex_lookup=lambda doi: BIBTEX,
        )

        if paths.bibliography.read_bytes() != before:
            raise AssertionError("project collection planning mutated canonical bibliography")
        if plan.result.candidates != (NEW_DOI, MISSING_DOI):
            raise AssertionError(f"unexpected project collection candidates: {plan.result.candidates!r}")
        if plan.result.unavailable != (MISSING_DOI,):
            raise AssertionError(f"unexpected unavailable DOI state: {plan.result.unavailable!r}")
        if len(plan.result.items) != 1:
            raise AssertionError("expected one collected fixture publication")

        apply_project_collection(plan)
        staged = read_bibliography(paths.collected)
        if len(staged) != 1 or staged[0].doi != NEW_DOI:
            raise AssertionError("canonical collected.json does not contain the expected fixture")
        staged_id = staged[0].id
        if paths.pending.read_text(encoding="utf-8") != f"{NEW_DOI}\n{MISSING_DOI}\n":
            raise AssertionError("pending DOI queue does not preserve collected + retryable unavailable DOI values")
        expected_bib = paths.bibtex / "canonical-project-collection0.bib"
        if expected_bib.read_text(encoding="utf-8") != BIBTEX:
            raise AssertionError("BibTeX output or slug-collision handling differs from expected behavior")

        merge_plan = plan_project_merge(mirror)
        if merge_plan.incoming_count != 1 or len(merge_plan.result.publications) != 2350:
            raise AssertionError("BibReview merge does not consume the collected fixture correctly")
        apply_project_merge(merge_plan)

        merged = read_bibliography(paths.bibliography)
        if len(merged) != 2350:
            raise AssertionError("real PHRAISE mirror did not gain exactly one publication")
        new_publication = next((publication for publication in merged if publication.doi == NEW_DOI), None)
        if new_publication is None or new_publication.id != staged_id:
            raise AssertionError("collected publication UUID was not preserved through merge")
        if read_bibliography(paths.collected):
            raise AssertionError("collected staging was not cleared by merge")
        if paths.pending.read_text(encoding="utf-8") != f"{MISSING_DOI}\n":
            raise AssertionError("unavailable DOI did not remain pending after merge")
        known = set(paths.known.read_text(encoding="utf-8").splitlines())
        if NEW_DOI not in known:
            raise AssertionError("merged DOI was not promoted to known state")

    print("PHRAISE real canonical mirror: 2349 -> 2350 publications")
    print("project collect planning: read-only")
    print("known DOI filtering / duplicate normalization: correct")
    print("canonical collected.json staging: correct")
    print("BibTeX slug collision handling: correct")
    print("unavailable DOI retry state: preserved")
    print("collect -> merge UUID continuity: preserved")
    print("tracked PHRAISE state: untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
