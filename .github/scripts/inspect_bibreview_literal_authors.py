#!/usr/bin/env python3
"""Report literal author entries in the canonical PHRAISE bibliography."""
from __future__ import annotations

import json
from pathlib import Path

from bibreview.config import load_config
from bibreview.storage import read_bibliography

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    config = load_config(ROOT / "bibreview.yml")
    publications = read_bibliography(config.paths.bibliography)

    occurrences = []
    distinct = set()
    for publication in publications:
        doi = publication.identifiers.get("doi", "")
        for index, author in enumerate(publication.authors):
            if not author.literal:
                continue
            literal = author.literal.strip()
            if not literal:
                continue
            distinct.add(literal)
            occurrences.append((publication, doi, index, author))

    print(f"literal author occurrences: {len(occurrences)}")
    print(f"literal distinct source names: {len(distinct)}")
    for publication, doi, index, author in occurrences:
        print("---")
        print(f"doi: {doi}")
        print(f"publication id: {publication.id}")
        print(f"title: {publication.title}")
        print(f"author index: {index}")
        print(f"literal: {author.literal}")
        print(
            "source_fields: "
            + json.dumps(dict(author.source_fields), ensure_ascii=False, sort_keys=True)
        )
        print("canonical authors:")
        for candidate in publication.authors:
            print(
                "  - "
                + json.dumps(
                    {
                        "given": candidate.given,
                        "family": candidate.family,
                        "literal": candidate.literal,
                        "source_fields": dict(candidate.source_fields),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )

    if len(distinct) != 25:
        raise AssertionError(
            f"expected 25 distinct literal author names from the audit, got {len(distinct)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
