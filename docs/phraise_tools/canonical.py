"""PHRAISE adapter for BibReview canonical project collection and merge.

This module preserves PHRAISE's current HTTP client and command-line ergonomics
while delegating bibliography state transitions to BibReview's canonical project
APIs.
"""
from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from bibreview.config import load_config
from bibreview.pipeline.enrich import EnrichmentService
from bibreview.project import (
    ProjectCollectionPlan,
    ProjectMergePlan,
    apply_project_collection,
    apply_project_merge,
    plan_project_collection,
    plan_project_merge,
)
from bibreview.providers.base import Enrichment

from .common import Reporter, summary


_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_PATH = _REPOSITORY_ROOT / "bibreview.yml"


class _WorkProvider:
    def __init__(self, client):
        self.client = client

    def work(self, doi: str):
        return self.client.crossref(doi)


class _PublisherProvider:
    def __init__(self, client):
        self.client = client

    def enrich(self, doi: str) -> Enrichment:
        abstract, keywords, event = self.client.publisher(doi)
        return Enrichment(
            abstract=abstract,
            keywords=tuple(
                item.strip()
                for item in keywords.split(",")
                if item.strip()
            ),
            event=event,
        )


class _AbstractFallback:
    def __init__(self, client):
        self.client = client

    def abstract(self, doi: str) -> str:
        return self.client.complement(doi)


def project_config(root: Path, *, pending: Path | None = None):
    """Return the PHRAISE BibReview config rebound to an isolated project root."""
    root = root.resolve()
    config = load_config(_CONFIG_PATH)
    paths = replace(
        config.paths,
        bibliography=root / "assets/data/bibliography.json",
        collected=root / "assets/data/collected.json",
        author_mappings=root / "assets/data/author_mappings.json",
        known=root / "DOI.txt",
        pending=(pending or root / "newDOI.txt").resolve(),
        rejected=root / "badDOI.txt",
        review=root / "checkDOI.txt",
        bibtex=root / "assets/bib",
        archive=root / "trash",
        site=root,
    )
    return replace(config, paths=paths)


def plan_canonical_collection(
    root: Path,
    input_path: Path,
    client,
    reporter=None,
) -> ProjectCollectionPlan:
    """Plan canonical collection from PHRAISE's DOI input file without writing."""
    reporter = reporter or Reporter(-1)
    config = project_config(root, pending=input_path)

    protected = {
        config.paths.bibliography.resolve(),
        config.paths.collected.resolve(),
        config.paths.known.resolve(),
        (root / "assets/data/biblio.json").resolve(),
    }
    if config.paths.pending.resolve() in protected:
        raise ValueError(
            "The input DOI file must differ from DOI.txt, bibliography.json, "
            "biblio.json, and collected.json"
        )

    service = EnrichmentService(
        publisher=_PublisherProvider(client),
        fallback=_AbstractFallback(client),
    )
    plan = plan_project_collection(
        config,
        provider=_WorkProvider(client),
        enrichment_lookup=service.for_collection,
        citation_lookup=client.citation,
        bibtex_lookup=client.bibtex,
        reporter=reporter,
    )
    reporter.step(
        "Canonical collection plan: "
        f"{len(plan.result.items)} publication(s), "
        f"{len(plan.result.unavailable)} unavailable DOI(s)"
    )
    return plan


def collect_canonical(
    root: Path,
    input_path: Path,
    client,
    reporter=None,
    dry_run: bool = False,
) -> str:
    """Collect DOI metadata into canonical collected.json staging."""
    reporter = reporter or Reporter(-1)
    plan = plan_canonical_collection(root, input_path, client, reporter)

    action = "Would write" if dry_run else "Writing"
    reporter.step(
        f"{action} canonical staging for {len(plan.result.items)} publication(s)"
    )
    if not dry_run:
        apply_project_collection(plan)

    return summary(
        "Collected "
        f"{len(plan.result.items)} publications into canonical staging; "
        f"unavailable: {len(plan.result.unavailable)}.",
        dry_run,
    )


def plan_canonical_merge(root: Path) -> ProjectMergePlan:
    """Plan BibReview's authoritative merge for a PHRAISE project root."""
    return plan_project_merge(project_config(root))


def merge_canonical(
    root: Path,
    reporter=None,
    dry_run: bool = False,
) -> str:
    """Merge collected.json into canonical bibliography.json."""
    reporter = reporter or Reporter(-1)
    plan = plan_canonical_merge(root)
    reporter.step(
        f"{'Would merge' if dry_run else 'Merging'} canonical staging: "
        f"{plan.incoming_count} incoming publication(s)"
    )
    if not dry_run:
        apply_project_merge(plan)
    return summary(plan.summary(), dry_run)
