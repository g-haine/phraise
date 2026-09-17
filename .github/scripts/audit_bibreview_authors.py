#!/usr/bin/env python3
"""Audit PHRAISE author mapping state against BibReview canonical authors."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config
from bibreview.pipeline.authors import (
    plan_author_mappings,
    publication_author_names,
    validate_author_mappings,
)
from bibreview.storage import read_bibliography, read_json
from phraise_tools.generate import author_mapping_plan as legacy_author_mapping_plan


def cleaned_mapping(mapping: dict, canonical_names: set[str]):
    """Repair only historical ``null X`` variants that map exactly to canonical X."""
    result = deepcopy(mapping)
    repaired = []
    unresolved = []
    for slug, names in result.items():
        updated = []
        for name in names:
            if name.startswith("null "):
                candidate = name.removeprefix("null ").strip()
                if candidate in canonical_names:
                    repaired.append((slug, name, candidate))
                    name = candidate
                else:
                    unresolved.append((slug, name))
            if name not in updated:
                updated.append(name)
        result[slug] = updated
    validate_author_mappings(result)
    return result, repaired, unresolved


def main() -> int:
    config = load_config(ROOT / "bibreview.yml")
    publications = read_bibliography(config.paths.bibliography)
    mapping = read_json(config.paths.author_mappings, dict)
    canonical_occurrences = publication_author_names(publications)
    canonical_names = set(canonical_occurrences)

    legacy_plan = legacy_author_mapping_plan(DOCS)
    before = plan_author_mappings(publications, mapping)
    cleaned, repaired, unresolved = cleaned_mapping(mapping, canonical_names)
    after = plan_author_mappings(publications, cleaned)

    mapped_variants = sum(len(names) for names in mapping.values())
    cleaned_variants = sum(len(names) for names in cleaned.values())
    literal_authors = sum(
        1
        for publication in publications
        for author in publication.authors
        if author.literal
    )
    family_only = sum(
        1
        for publication in publications
        for author in publication.authors
        if not author.literal and not (author.given or "").strip() and (author.family or "").strip()
    )

    print(f"publications: {len(publications)}")
    print(f"canonical author occurrences: {len(canonical_occurrences)}")
    print(f"canonical distinct source names: {len(canonical_names)}")
    print(f"mapping slugs: {len(mapping)}")
    print(f"mapping name variants: {mapped_variants}")
    print(f"literal author occurrences: {literal_authors}")
    print(f"family-only author occurrences: {family_only}")
    print(f"historical unknown names: {legacy_plan['unknown_names']}")
    print(f"canonical unknown names before cleanup: {before.unknown_names}")
    print(f"repairable historical null variants: {len(repaired)}")
    print(f"unresolved historical null variants: {len(unresolved)}")
    print(f"mapping variants after cleanup: {cleaned_variants}")
    print(f"canonical unknown names after cleanup: {after.unknown_names}")
    print(f"canonical safe proposals after cleanup: {len(after.safe)}")
    print(f"canonical review proposals after cleanup: {len(after.review)}")

    if repaired:
        print("sample repaired variants:")
        for slug, old, new in repaired[:10]:
            print(f"  {slug}: {old!r} -> {new!r}")
    if unresolved:
        print("unresolved null variants:")
        for slug, name in unresolved:
            print(f"  {slug}: {name!r}")
    if after.safe:
        print("safe canonical proposals after cleanup:")
        for slug, names in list(after.safe.items())[:25]:
            print(f"  + {slug}: {', '.join(names)}")
    if after.review:
        print("manual-review canonical proposals after cleanup:")
        for item in after.review[:25]:
            print(f"  ? {item.slug}: {', '.join(item.names)}")
            print(f"    {'; '.join(item.reasons)}")

    if unresolved:
        raise AssertionError("some historical null author variants cannot be repaired deterministically")
    if len(repaired) != family_only:
        raise AssertionError(
            "repairable null variants do not match canonical family-only author occurrences; "
            f"repairs={len(repaired)}, occurrences={family_only}"
        )

    # This is audit-only: the tracked mapping must remain untouched here.
    if json.loads(config.paths.author_mappings.read_text(encoding="utf-8")) != mapping:
        raise AssertionError("author mapping audit mutated project state")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
