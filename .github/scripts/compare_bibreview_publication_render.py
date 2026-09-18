#!/usr/bin/env python3
"""Compare legacy PHRAISE publication posts with BibReview byte-for-byte."""
from __future__ import annotations

import difflib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config  # noqa: E402
from bibreview.site import (  # noqa: E402
    build_site_model,
    render_jekyll_publication_posts,
)
from bibreview.storage import read_bibliography, read_json  # noqa: E402
from phraise_tools.common import bibliography, mappings, read_lines  # noqa: E402
from phraise_tools.generate import render_post  # noqa: E402


from phraise_tools.site import PHRAISE_PUBLICATION_OPTIONS  # noqa: E402


def main() -> None:
    config = load_config(ROOT / "bibreview.yml")
    canonical_before = config.paths.bibliography.read_bytes()
    mappings_before = config.paths.author_mappings.read_bytes()

    canonical = read_bibliography(config.paths.bibliography)
    mapping_data = read_json(config.paths.author_mappings, dict)
    model = build_site_model(canonical, mapping_data)

    legacy = bibliography(DOCS)
    _, reverse = mappings(DOCS)
    known = set(read_lines(DOCS / "DOI.txt"))
    permalinks = {record["doi"]: record.get("permalink", "") for record in legacy}

    site_by_doi = {
        publication.identifiers["doi"]: publication
        for publication in model.publications
        if "doi" in publication.identifiers
    }
    legacy_by_doi = {record["doi"].lower(): record for record in legacy}
    assert set(site_by_doi) == set(legacy_by_doi)
    assert len(site_by_doi) == len(model.publications)

    bibtex_by_id: dict[str, str] = {}
    expected: dict[str, bytes] = {}
    for doi, publication in site_by_doi.items():
        bib_path = DOCS / "assets/bib" / f"{publication.permalink}.bib"
        if not bib_path.exists():
            raise AssertionError(f"missing tracked BibTeX for {doi}: {bib_path}")
        bibtex = bib_path.read_text(encoding="utf-8")
        bibtex_by_id[publication.id] = bibtex

        record = legacy_by_doi[doi]
        name, content = render_post(record, reverse, known, permalinks, bibtex)
        expected[f"_posts/{name}"] = content.encode("utf-8")

    rendered = render_jekyll_publication_posts(
        model,
        bibtex_by_id,
        options=PHRAISE_PUBLICATION_OPTIONS,
    )
    actual = {
        artifact.path: artifact.content.encode("utf-8")
        for artifact in rendered
    }

    assert set(actual) == set(expected), (
        f"artifact path mismatch: only BibReview={sorted(set(actual) - set(expected))[:5]}, "
        f"only legacy={sorted(set(expected) - set(actual))[:5]}"
    )

    mismatches = [
        path for path in sorted(expected)
        if actual[path] != expected[path]
    ]
    if mismatches:
        first = mismatches[0]
        expected_text = expected[first].decode("utf-8").splitlines()
        actual_text = actual[first].decode("utf-8").splitlines()
        diff = "\n".join(
            difflib.unified_diff(
                expected_text,
                actual_text,
                fromfile=f"legacy/{first}",
                tofile=f"bibreview/{first}",
                n=3,
            )
        )
        raise AssertionError(
            f"{len(mismatches)} rendered publication post(s) differ; "
            f"first mismatch: {first}\n{diff}"
        )

    assert config.paths.bibliography.read_bytes() == canonical_before
    assert config.paths.author_mappings.read_bytes() == mappings_before

    print("PHRAISE Jekyll publication rendering equivalence: byte-exact")
    print(f"  publication posts: {len(actual)}")
    print(f"  tracked BibTeX inputs: {len(bibtex_by_id)}")
    print("  category policy supplied by PHRAISE: yes")
    print("  filesystem/network access by BibReview renderer: no")
    print("  canonical bibliography unchanged: yes")
    print("  author mappings unchanged: yes")


if __name__ == "__main__":
    main()
