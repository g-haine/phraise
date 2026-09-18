#!/usr/bin/env python3
"""Validate BibReview's safe rendered-artifact persistence on real PHRAISE data."""
from __future__ import annotations

from pathlib import Path
import shutil
import tempfile

from bibreview.site import (
    JekyllIndexRenderOptions,
    apply_rendered_artifacts,
    build_site_model,
    plan_rendered_artifacts,
    render_jekyll_index_pages,
    render_jekyll_publication_posts,
)
from bibreview.storage import read_bibliography, read_json

from compare_bibreview_index_render import PHRAISE_AUTHOR_INDEX_EXTRA_HTML
from compare_bibreview_publication_render import PHRAISE_PUBLICATION_OPTIONS


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

EXPECTED_POSTS = 2349
EXPECTED_AUTHOR_PAGES = 2651
EXPECTED_YEAR_PAGES = 39
EXPECTED_INDEX_CONTENT_PAGES = EXPECTED_AUTHOR_PAGES + EXPECTED_YEAR_PAGES
EXPECTED_INDEX_ARTIFACTS = EXPECTED_INDEX_CONTENT_PAGES + 2
EXPECTED_MANAGED_ARTIFACTS = EXPECTED_POSTS + EXPECTED_INDEX_ARTIFACTS
MANAGED_ROOTS = ("_posts", "authors", "years")


def _render_artifacts(site_root: Path):
    canonical = read_bibliography(site_root / "assets/data/bibliography.json")
    mapping_data = read_json(site_root / "assets/data/author_mappings.json", dict)
    model = build_site_model(canonical, mapping_data)

    bibtex_by_id: dict[str, str] = {}
    for publication in model.publications:
        bib_path = site_root / "assets/bib" / f"{publication.permalink}.bib"
        if not bib_path.exists():
            doi = publication.identifiers.get("doi", publication.id)
            raise AssertionError(f"missing tracked BibTeX for {doi}: {bib_path}")
        bibtex_by_id[publication.id] = bib_path.read_text(encoding="utf-8")

    posts = render_jekyll_publication_posts(
        model,
        bibtex_by_id,
        options=PHRAISE_PUBLICATION_OPTIONS,
    )
    indexes = render_jekyll_index_pages(
        model,
        options=JekyllIndexRenderOptions(
            author_index_extra_html=PHRAISE_AUTHOR_INDEX_EXTRA_HTML,
            include_authorless_year_publications=False,
        ),
    )
    return posts, indexes


def _assert_expected_counts(posts, indexes) -> None:
    author_pages = sum(
        1
        for artifact in indexes
        if artifact.path.startswith("authors/") and artifact.path != "authors/index.md"
    )
    year_pages = sum(
        1
        for artifact in indexes
        if artifact.path.startswith("years/") and artifact.path != "years/index.md"
    )

    assert len(posts) == EXPECTED_POSTS, (
        f"expected {EXPECTED_POSTS} publication posts, got {len(posts)}"
    )
    assert author_pages == EXPECTED_AUTHOR_PAGES, (
        f"expected {EXPECTED_AUTHOR_PAGES} author pages, got {author_pages}"
    )
    assert year_pages == EXPECTED_YEAR_PAGES, (
        f"expected {EXPECTED_YEAR_PAGES} year pages, got {year_pages}"
    )
    assert len(indexes) == EXPECTED_INDEX_ARTIFACTS, (
        f"expected {EXPECTED_INDEX_ARTIFACTS} author/year artifacts "
        f"including the two indexes, got {len(indexes)}"
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        site_root = Path(tmp) / "docs"
        shutil.copytree(DOCS, site_root)

        posts, indexes = _render_artifacts(site_root)
        _assert_expected_counts(posts, indexes)
        artifacts = posts + indexes

        plan = plan_rendered_artifacts(
            site_root,
            artifacts,
            managed_roots=MANAGED_ROOTS,
        )
        assert plan.expected_count == EXPECTED_MANAGED_ARTIFACTS
        if plan.changed or plan.unchanged_count != EXPECTED_MANAGED_ARTIFACTS:
            writes = [
                path.relative_to(site_root).as_posix()
                for path in plan.writes
            ]
            deletes = [
                path.relative_to(site_root).as_posix()
                for path in plan.deletes
            ]
            raise AssertionError(
                "unexpected pre-existing persistence changes; "
                f"{plan.summary()}; writes={writes}; deletes={deletes}"
            )
        assert not plan.changed

        obsolete = site_root / "_posts" / "__bibreview_obsolete_probe__.md"
        obsolete.write_text("obsolete generated probe\n", encoding="utf-8")
        manual = site_root / "__bibreview_manual_probe__.txt"
        manual.write_text("manual content must remain untouched\n", encoding="utf-8")
        manual_before = manual.read_bytes()

        reconciliation = plan_rendered_artifacts(
            site_root,
            artifacts,
            managed_roots=MANAGED_ROOTS,
        )
        assert reconciliation.expected_count == EXPECTED_MANAGED_ARTIFACTS
        assert reconciliation.unchanged_count == EXPECTED_MANAGED_ARTIFACTS
        assert not reconciliation.writes
        assert reconciliation.deletes == (obsolete,)
        assert reconciliation.changed
        assert manual not in reconciliation.deletes

        apply_rendered_artifacts(reconciliation)

        assert not obsolete.exists()
        assert manual.read_bytes() == manual_before

        final_plan = plan_rendered_artifacts(
            site_root,
            artifacts,
            managed_roots=MANAGED_ROOTS,
        )
        assert not final_plan.changed
        assert final_plan.unchanged_count == EXPECTED_MANAGED_ARTIFACTS
        assert manual.read_bytes() == manual_before

    print("PHRAISE rendered-artifact persistence integration: OK")
    print(f"  publication posts unchanged: {EXPECTED_POSTS}")
    print(
        "  author/year content pages unchanged: "
        f"{EXPECTED_INDEX_CONTENT_PAGES} "
        f"({EXPECTED_AUTHOR_PAGES} authors + {EXPECTED_YEAR_PAGES} years)"
    )
    print("  author/year index pages unchanged: 2")
    print(f"  managed artifacts unchanged before probe: {EXPECTED_MANAGED_ARTIFACTS}")
    print("  obsolete generated probe detected and removed: yes")
    print("  manual file outside managed roots untouched: yes")
    print("  final persistence plan: no-op")


if __name__ == "__main__":
    main()
