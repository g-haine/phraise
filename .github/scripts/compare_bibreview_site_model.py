#!/usr/bin/env python3
"""Validate BibReview's renderer-independent site model on real PHRAISE data."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config  # noqa: E402
from bibreview.site import build_site_model  # noqa: E402
from bibreview.storage import read_bibliography, read_json  # noqa: E402
from phraise_tools.common import (  # noqa: E402
    author_names,
    bibliography,
    mappings,
    read_lines,
    record_date,
    text,
)


def main() -> None:
    config = load_config(ROOT / "bibreview.yml")
    canonical_before = config.paths.bibliography.read_bytes()
    mappings_before = config.paths.author_mappings.read_bytes()

    canonical = read_bibliography(config.paths.bibliography)
    mapping_data = read_json(config.paths.author_mappings, dict)
    model = build_site_model(canonical, mapping_data)

    legacy = bibliography(DOCS)
    mapping, reverse = mappings(DOCS)
    known = set(read_lines(DOCS / "DOI.txt"))
    legacy_permalinks = {record["doi"].lower(): record.get("permalink", "") for record in legacy}

    assert len(model.publications) == len(canonical) == len(legacy)
    assert config.paths.bibliography.read_bytes() == canonical_before
    assert config.paths.author_mappings.read_bytes() == mappings_before

    site_by_doi = {
        publication.identifiers["doi"]: publication
        for publication in model.publications
        if "doi" in publication.identifiers
    }
    legacy_by_doi = {record["doi"].lower(): record for record in legacy}
    assert set(site_by_doi) == set(legacy_by_doi)

    expected_author_membership: dict[str, list[str]] = defaultdict(list)
    expected_year_membership: dict[str, list[str]] = defaultdict(list)
    internal_reference_count = 0

    for doi, record in legacy_by_doi.items():
        publication = site_by_doi[doi]
        assert publication.permalink == record.get("permalink")
        assert publication.created_date.isoformat() == record_date(record)
        assert publication.year == text(record.get("year"))
        assert publication.type == text(record.get("type"))
        assert publication.title == text(record.get("title"))

        names = author_names(record)
        expected_authors = tuple((reverse[name], name) for name in names)
        actual_authors = tuple((author.slug, author.name) for author in publication.authors)
        assert actual_authors == expected_authors, f"author link mismatch for {doi}"

        for slug, _ in expected_authors:
            expected_author_membership[slug].append(publication.id)
        expected_year_membership[publication.year].append(publication.id)

        expected_references = []
        for reference in record.get("references") or []:
            raw_doi = text(reference.get("doi")).lower()
            reference_doi = None if raw_doi == "null" else raw_doi
            permalink = (
                legacy_permalinks.get(raw_doi)
                if reference_doi is not None and raw_doi in known
                else None
            )
            if permalink:
                internal_reference_count += 1
            expected_references.append(
                (reference_doi, text(reference.get("title")), permalink or None)
            )
        actual_references = [
            (reference.doi, reference.citation, reference.permalink)
            for reference in publication.references
        ]
        assert actual_references == expected_references, f"reference mismatch for {doi}"

    assert set(model.authors) == set(expected_author_membership)
    for slug, page in model.authors.items():
        assert page.author.name == mapping[slug][0]
        assert page.author.variants == tuple(mapping[slug])
        assert set(page.publication_ids) == set(expected_author_membership[slug])

    assert set(model.years) == set(expected_year_membership)
    for year, page in model.years.items():
        assert set(page.publication_ids) == set(expected_year_membership[year])

    # The historical renderer links internally only through DOI.txt.  PHRAISE's
    # authoritative state currently has one known DOI per canonical DOI-backed
    # publication, so BibReview's direct bibliography-based resolution is
    # equivalent while avoiding a renderer dependency on workflow queue state.
    assert known == set(site_by_doi)

    print("PHRAISE renderer-independent site model: OK")
    print(f"  publications: {len(model.publications)}")
    print(f"  referenced author identities: {len(model.authors)}")
    print(f"  publication years: {len(model.years)}")
    print(f"  internally linked references: {internal_reference_count}")
    print("  canonical bibliography unchanged: yes")
    print("  author mappings unchanged: yes")
    print("  Markdown/HTML/Jekyll rendering intentionally outside this comparison")


if __name__ == "__main__":
    main()
