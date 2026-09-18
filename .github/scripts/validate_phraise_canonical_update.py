#!/usr/bin/env python3
"""Validate PHRAISE's effective canonical discovery -> refresh -> collect cycle."""
from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config  # noqa: E402
from bibreview.pipeline.enrich import crossref_enrichment  # noqa: E402
from bibreview.project import (  # noqa: E402
    apply_project_discovery,
    apply_project_merge,
    plan_project_discovery,
    plan_project_merge,
)
from bibreview.project_refresh import (  # noqa: E402
    apply_project_refresh,
    plan_project_refresh,
)
from bibreview.storage import read_bibliography, write_bibliography  # noqa: E402
from phraise_tools.canonical import collect_canonical, merge_canonical  # noqa: E402


DISCOVERED = "10.1/discovered-relevant"
MANUAL = "10.1/discovered-review"
UNSUPPORTED = "10.1/discovered-unsupported"
EXCLUDED = "10.1/arxiv-discovery-fixture"

STORED_BIBTEX = "@article{old,\n title={{Stored refresh fixture}}\n}\n"
CURRENT_BIBTEX = "@article{new,\n title={{Refreshed fixture}}\n}\n"
NEW_BIBTEX = "@article{discovered,\n title={{Discovered port-Hamiltonian fixture}}\n}\n"


def write_lines(path: Path, values) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{value}\n" for value in values), encoding="utf-8")


def work_message(title: str, *, type_: str = "journal-article") -> dict:
    return {
        "type": type_,
        "title": [title],
        "author": [{"given": "Ada", "family": "Lovelace"}],
        "abstract": "Neutral abstract",
        "container-title": ["Journal"],
        "created": {"date-parts": [[2026, 9, 18]]},
        "published-print": {"date-parts": [[2026]]},
        "volume": "12",
        "issue": "3",
        "page": "10-20",
        "publisher": "Publisher",
        "subject": [],
        "reference": [],
    }


class DiscoveryProvider:
    def __init__(self, known_doi: str) -> None:
        self.known_doi = known_doi
        self.calls = []

    def discover(self, query: str, *, max_pages: int = 20):
        self.calls.append((query, max_pages))
        return (
            self.known_doi,
            DISCOVERED,
            MANUAL,
            UNSUPPORTED,
            EXCLUDED,
            DISCOVERED,
        )


class DiscoveryWorkProvider:
    def work(self, doi: str):
        if doi == DISCOVERED:
            return work_message("A port-Hamiltonian discovered publication")
        if doi == MANUAL:
            return work_message("A generic control publication")
        if doi == UNSUPPORTED:
            return work_message("A port-Hamiltonian dataset", type_="dataset")
        raise AssertionError(f"unexpected discovery metadata lookup: {doi}")


class RefreshProvider:
    def __init__(self, target_doi: str) -> None:
        self.target_doi = target_doi
        self.calls = []

    def work(self, doi: str):
        self.calls.append(doi)
        if doi != self.target_doi:
            raise AssertionError(f"unexpected refresh metadata lookup: {doi}")
        return work_message("Refreshed canonical PHRAISE fixture")


class CollectionClient:
    def crossref(self, doi: str):
        return (
            work_message("Discovered port-Hamiltonian fixture")
            if doi == DISCOVERED
            else None
        )

    def publisher(self, doi: str):
        return "", "", ""

    def complement(self, doi: str):
        return "Not available"

    def citation(self, doi: str):
        return "A cited publication"

    def bibtex(self, doi: str):
        if doi != DISCOVERED:
            raise AssertionError(f"unexpected collection BibTeX lookup: {doi}")
        return NEW_BIBTEX


def main() -> None:
    config = load_config(ROOT / "bibreview.yml")
    if config.environment.file != DOCS / ".env":
        raise AssertionError(
            f"unexpected PHRAISE environment file: {config.environment.file!r}"
        )

    canonical = read_bibliography(DOCS / "assets/data/bibliography.json")
    if len(canonical) != 2349:
        raise AssertionError(f"unexpected canonical PHRAISE count: {len(canonical)}")

    target = next(
        publication
        for publication in canonical
        if publication.type == "journal-article"
        and publication.doi is not None
        and publication.permalink
    )

    # Preserve the complete real bibliography/identity surface while making only
    # one journal publication eligible for the configured refresh policy.
    mirror_publications = []
    for publication in canonical:
        if publication.id == target.id:
            mirror_publications.append(replace(publication, volume=""))
        elif publication.type == "journal-article":
            mirror_publications.append(
                replace(
                    publication,
                    volume=publication.volume or "fixture-volume",
                    issue=publication.issue or "fixture-issue",
                    pages=publication.pages or "fixture-pages",
                )
            )
        else:
            mirror_publications.append(publication)

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        data = root / "assets/data"
        bib = root / "assets/bib"
        trash = root / "trash"
        data.mkdir(parents=True)
        bib.mkdir(parents=True)
        trash.mkdir(parents=True)

        bibliography = data / "bibliography.json"
        collected = data / "collected.json"
        legacy = data / "biblio.json"
        write_bibliography(bibliography, mirror_publications)
        write_bibliography(collected, ())
        shutil.copyfile(DOCS / "assets/data/biblio.json", legacy)
        legacy_before = legacy.read_bytes()

        known_dois = [
            publication.doi
            for publication in mirror_publications
            if publication.doi is not None
        ]
        write_lines(root / "DOI.txt", known_dois)
        write_lines(root / "newDOI.txt", ())
        write_lines(root / "badDOI.txt", ())
        write_lines(root / "checkDOI.txt", ())
        (bib / f"{target.permalink}.bib").write_text(
            STORED_BIBTEX,
            encoding="utf-8",
        )

        paths = replace(
            config.paths,
            bibliography=bibliography,
            collected=collected,
            author_mappings=data / "author_mappings.json",
            known=root / "DOI.txt",
            pending=root / "newDOI.txt",
            rejected=root / "badDOI.txt",
            review=root / "checkDOI.txt",
            bibtex=bib,
            archive=trash,
            site=root,
        )
        mirror = replace(config, paths=paths)

        # 1. Canonical discovery updates only queue state.
        discovery_provider = DiscoveryProvider(target.doi)
        before_discovery = bibliography.read_bytes()
        discovery = plan_project_discovery(
            mirror,
            discovery_provider=discovery_provider,
            provider=DiscoveryWorkProvider(),
            enrichment_lookup=lambda doi, message: crossref_enrichment(message),
        )
        apply_project_discovery(discovery)

        if bibliography.read_bytes() != before_discovery:
            raise AssertionError("discovery mutated canonical bibliography")
        if discovery_provider.calls != [("port-Hamiltonian", 20)]:
            raise AssertionError(f"unexpected discovery policy: {discovery_provider.calls!r}")
        if discovery.result.queued != (DISCOVERED,):
            raise AssertionError(f"unexpected discovered queue: {discovery.result.queued!r}")
        if discovery.result.review != (MANUAL,):
            raise AssertionError(f"unexpected manual-review queue: {discovery.result.review!r}")
        if discovery.result.rejected != (UNSUPPORTED,):
            raise AssertionError(f"unexpected rejected queue: {discovery.result.rejected!r}")
        if EXCLUDED not in discovery.result.skipped or target.doi not in discovery.result.skipped:
            raise AssertionError("known/excluded discovery filtering changed")

        # 2. Canonical refresh stages one stale existing publication.
        refresh_provider = RefreshProvider(target.doi)
        before_refresh = bibliography.read_bytes()
        refresh = plan_project_refresh(
            mirror,
            provider=refresh_provider,
            bibtex_lookup=lambda doi: (
                CURRENT_BIBTEX
                if doi == target.doi
                else (_ for _ in ()).throw(
                    AssertionError(f"unexpected refresh BibTeX lookup: {doi}")
                )
            ),
        )
        if refresh.result.candidates != (target.doi,):
            raise AssertionError(f"unexpected refresh candidates: {refresh.result.candidates!r}")
        if len(refresh.result.items) != 1:
            raise AssertionError("expected exactly one staged refresh")
        if len(refresh.bibtex_backups) != 1:
            raise AssertionError("expected exactly one changed-BibTeX backup")

        apply_project_refresh(refresh)
        if bibliography.read_bytes() != before_refresh:
            raise AssertionError("refresh application mutated bibliography before merge")
        staged = read_bibliography(collected)
        if len(staged) != 1 or staged[0].doi != target.doi:
            raise AssertionError("refresh did not stage the expected publication")

        refresh_merge = plan_project_merge(mirror)
        apply_project_merge(refresh_merge)
        refreshed = read_bibliography(bibliography)
        refreshed_target = next(
            publication for publication in refreshed if publication.doi == target.doi
        )
        if refreshed_target.id != target.id:
            raise AssertionError("refresh merge did not preserve persistent UUID")
        if refreshed_target.volume != "12":
            raise AssertionError("refresh merge did not install refreshed metadata")
        if read_bibliography(collected):
            raise AssertionError("refresh staging was not cleared by merge")

        # 3. The discovered DOI is then collected and merged through the PHRAISE
        # adapter already used by getData.py.
        collect_canonical(root, root / "newDOI.txt", CollectionClient())
        staged_new = read_bibliography(collected)
        if len(staged_new) != 1 or staged_new[0].doi != DISCOVERED:
            raise AssertionError("discovered DOI was not collected canonically")
        new_id = staged_new[0].id
        merge_canonical(root)

        final = read_bibliography(bibliography)
        if len(final) != 2350:
            raise AssertionError(f"unexpected final canonical count: {len(final)}")
        discovered = next(
            publication for publication in final if publication.doi == DISCOVERED
        )
        if discovered.id != new_id:
            raise AssertionError("collected publication UUID changed during merge")
        if read_bibliography(collected):
            raise AssertionError("collection staging was not cleared by merge")

        pending = (root / "newDOI.txt").read_text(encoding="utf-8").splitlines()
        review = (root / "checkDOI.txt").read_text(encoding="utf-8").splitlines()
        rejected = (root / "badDOI.txt").read_text(encoding="utf-8").splitlines()
        if pending:
            raise AssertionError(f"unexpected pending DOI values after collection: {pending!r}")
        if review != [MANUAL]:
            raise AssertionError(f"unexpected manual-review state: {review!r}")
        if rejected != [UNSUPPORTED]:
            raise AssertionError(f"unexpected rejected state: {rejected!r}")
        if legacy.read_bytes() != legacy_before:
            raise AssertionError("legacy biblio.json changed during canonical update cycle")

    print("PHRAISE canonical discovery/refresh cutover: OK")
    print("  canonical baseline publications: 2349")
    print("  discovery queue policy from bibreview.yml: exact")
    print("  discovery mutates canonical bibliography: no")
    print("  refresh staging before merge: 1 publication")
    print("  refresh persistent UUID preserved: yes")
    print("  changed BibTeX backup: 1")
    print("  discovered DOI collected after refresh merge: yes")
    print("  final canonical publications: 2350")
    print("  manual-review / rejected queue state: preserved")
    print("  legacy biblio.json untouched: yes")


if __name__ == "__main__":
    main()
