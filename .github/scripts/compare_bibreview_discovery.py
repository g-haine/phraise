#!/usr/bin/env python3
"""Compare PHRAISE legacy discovery/relevance with canonical BibReview discovery.

The historical refresh/recollect half of ``looking4Update.py`` is deliberately
neutralized: the fixture contains one complete known journal record, so only
OpenAlex candidate discovery, CrossRef type filtering, relevance screening, and
DOI queue updates produce changes.
"""
from __future__ import annotations

from dataclasses import replace
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
from bibreview.pipeline.enrich import crossref_enrichment  # noqa: E402
from bibreview.project import apply_project_discovery, plan_project_discovery  # noqa: E402
from bibreview.storage import write_bibliography  # noqa: E402
from phraise_tools.update import TYPES, find_updates  # noqa: E402


CANDIDATES = (
    "10.1000/known",
    "10.1000/bad",
    "10.1000/arxiv-record",
    "10.1000/zenodo-record",
    "10.1000/relevant-title",
    "10.1000/relevant-abstract",
    "10.1000/relevant-keywords",
    "10.1000/manual-review",
    "10.1000/unsupported",
    "10.1000/missing",
    "10.1000/relevant-title",
)

WORKS = {
    "10.1000/relevant-title": {
        "type": "journal-article",
        "title": ["A port–Hamiltonian formulation"],
        "abstract": "Neutral abstract",
        "subject": [],
    },
    "10.1000/relevant-abstract": {
        "type": "proceedings-article",
        "title": ["A coupled model"],
        "abstract": "We use a port-Hamiltonian representation.",
        "subject": [],
    },
    "10.1000/relevant-keywords": {
        "type": "book-chapter",
        "title": ["Geometric methods"],
        "abstract": "Neutral abstract",
        "subject": ["Dirac structure"],
    },
    "10.1000/manual-review": {
        "type": "book",
        "title": ["Generic control methods"],
        "abstract": "Neutral abstract",
        "subject": [],
    },
    "10.1000/unsupported": {
        "type": "dataset",
        "title": ["Port-Hamiltonian dataset"],
        "abstract": "Neutral abstract",
        "subject": [],
    },
}


class LegacyClient:
    def __init__(self) -> None:
        self.pages = {
            "*": {
                "results": [
                    {"doi": f"https://doi.org/{doi}"}
                    for doi in CANDIDATES[:6]
                ],
                "meta": {"next_cursor": "page-2"},
            },
            "page-2": {
                "results": [
                    {"doi": f"https://doi.org/{doi}"}
                    for doi in CANDIDATES[6:]
                ],
                "meta": {"next_cursor": None},
            },
        }

    def openalex(self, cursor):
        return self.pages[cursor]

    def crossref(self, doi):
        return WORKS.get(doi)

    def publisher(self, doi):
        return "", "", ""

    def complement(self, doi):
        return "Not available"

    def bibtex(self, doi):
        raise AssertionError("refresh/recollect must not run in discovery fixture")


class DiscoveryProvider:
    def __init__(self) -> None:
        self.calls = []

    def discover(self, query, *, max_pages=20):
        self.calls.append((query, max_pages))
        return tuple(dict.fromkeys(CANDIDATES))


class WorkProvider:
    def __init__(self) -> None:
        self.calls = []

    def work(self, doi):
        self.calls.append(doi)
        return WORKS.get(doi)


def write_lines(path: Path, values: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{value}\n" for value in values), encoding="utf-8")


def read_lines(path: Path) -> tuple[str, ...]:
    return tuple(path.read_text(encoding="utf-8").splitlines())


def prepare_legacy(root: Path) -> None:
    (root / "assets/data").mkdir(parents=True, exist_ok=True)
    known_record = [{
        "doi": "10.1000/known",
        "type": "journal-article",
        "volume": "1",
        "issue": "1",
        "pages": "1-2",
        "permalink": "known",
        "authors": [],
    }]
    (root / "assets/data/biblio.json").write_text(
        json.dumps(known_record, indent=2) + "\n",
        encoding="utf-8",
    )
    write_lines(root / "DOI.txt", ("10.1000/known",))
    write_lines(root / "newDOI.txt", ("10.1000/preexisting-pending",))
    write_lines(root / "badDOI.txt", ("10.1000/bad",))
    write_lines(root / "checkDOI.txt", ("10.1000/preexisting-review",))


def queues(root: Path, *, legacy: bool) -> dict[str, tuple[str, ...]]:
    names = (
        ("pending", "newDOI.txt"),
        ("rejected", "badDOI.txt"),
        ("review", "checkDOI.txt"),
    ) if legacy else (
        ("pending", "pending.txt"),
        ("rejected", "rejected.txt"),
        ("review", "review.txt"),
    )
    return {key: read_lines(root / filename) for key, filename in names}


def main() -> None:
    config = load_config(ROOT / "bibreview.yml")
    assert config.discovery.query == "port-Hamiltonian"
    assert config.discovery.max_pages == 20
    assert set(config.discovery.accepted_types) == TYPES
    assert config.discovery.exclude_doi_substrings == ("arxiv", "zenodo")
    assert config.relevance.unmatched == "manual-review"

    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        legacy_root = temporary / "legacy"
        canonical_root = temporary / "canonical"
        prepare_legacy(legacy_root)
        canonical_root.mkdir(parents=True)

        find_updates(
            legacy_root,
            LegacyClient(),
            max_pages=config.discovery.max_pages,
            dry_run=False,
        )

        bibliography = canonical_root / "bibliography.json"
        known = canonical_root / "known.txt"
        pending = canonical_root / "pending.txt"
        rejected = canonical_root / "rejected.txt"
        review = canonical_root / "review.txt"
        write_bibliography(
            bibliography,
            [Publication(
                id=new_publication_id(),
                identifiers={"doi": "10.1000/known"},
                type="journal-article",
                title="Known publication",
                volume="1",
                issue="1",
                pages="1-2",
                permalink="known",
            )],
        )
        write_lines(known, ("10.1000/known",))
        write_lines(pending, ("10.1000/preexisting-pending",))
        write_lines(rejected, ("10.1000/bad",))
        write_lines(review, ("10.1000/preexisting-review",))

        canonical_config = replace(
            config,
            paths=replace(
                config.paths,
                bibliography=bibliography,
                known=known,
                pending=pending,
                rejected=rejected,
                review=review,
            ),
        )
        discovery_provider = DiscoveryProvider()
        work_provider = WorkProvider()
        before_bibliography = bibliography.read_bytes()
        plan = plan_project_discovery(
            canonical_config,
            discovery_provider=discovery_provider,
            provider=work_provider,
            enrichment_lookup=lambda doi, message: crossref_enrichment(message),
        )
        assert bibliography.read_bytes() == before_bibliography, "discovery planning mutated bibliography"
        apply_project_discovery(plan)
        assert bibliography.read_bytes() == before_bibliography, "discovery application mutated bibliography"

        legacy_queues = queues(legacy_root, legacy=True)
        canonical_queues = queues(canonical_root, legacy=False)
        assert canonical_queues == legacy_queues, (
            "BibReview discovery queue result differs from historical PHRAISE discovery:\n"
            f"legacy={json.dumps(legacy_queues, indent=2)}\n"
            f"bibreview={json.dumps(canonical_queues, indent=2)}"
        )
        assert discovery_provider.calls == [("port-Hamiltonian", 20)]
        assert plan.result.queued == (
            "10.1000/relevant-title",
            "10.1000/relevant-abstract",
            "10.1000/relevant-keywords",
        )
        assert plan.result.review == ("10.1000/manual-review",)
        assert plan.result.rejected == ("10.1000/unsupported", "10.1000/missing")
        assert "10.1000/arxiv-record" in plan.result.skipped
        assert "10.1000/zenodo-record" in plan.result.skipped

        print("PHRAISE discovery/relevance equivalence: OK")
        print(f"  candidates: {len(plan.result.candidates)}")
        print(f"  queued: {len(plan.result.queued)}")
        print(f"  manual review: {len(plan.result.review)}")
        print(f"  rejected: {len(plan.result.rejected)}")
        print(f"  skipped: {len(plan.result.skipped)}")
        print("  canonical bibliography unchanged: yes")
        print("  refresh/recollect fixture: neutralized")


if __name__ == "__main__":
    main()
