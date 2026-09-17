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
from bibreview.text import slugify
from phraise_tools.generate import author_mapping_plan as legacy_author_mapping_plan


def cleaned_mapping(mapping: dict, canonical_names: set[str]):
    """Classify and repair only deterministic historical ``null X`` artifacts.

    The old PHRAISE renderer converted a missing given name into the literal word
    ``null``.  Some of those variants were stored beside the clean name, some got
    their own ``null-*`` slug, and some are the only variant for a legacy slug.
    Only structurally deterministic repairs are applied here; any other ownership
    collision is reported for human review.
    """
    result = deepcopy(mapping)
    exact_owners: dict[str, set[str]] = {}
    for owner_slug, names in mapping.items():
        for name in names:
            if not name.startswith("null "):
                exact_owners.setdefault(name, set()).add(owner_slug)

    same_slug = []
    replaced = []
    renamed_slugs = []
    duplicate_slugs = []
    collisions = []
    unresolved = []
    remove_slugs: set[str] = set()
    additions: dict[str, list[str]] = {}

    for slug, names in mapping.items():
        updated: list[str] = []
        for name in names:
            if not name.startswith("null "):
                if name not in updated:
                    updated.append(name)
                continue

            candidate = name.removeprefix("null ").strip()
            if candidate not in canonical_names:
                unresolved.append((slug, name, candidate))
                updated.append(name)
                continue

            canonical_slug = slugify(candidate)
            owners = exact_owners.get(candidate, set())

            if slug in owners:
                # The same mapping already contains the canonical spelling.
                same_slug.append((slug, name, candidate))
                continue

            if not owners:
                if slug == f"null-{canonical_slug}" and canonical_slug not in mapping:
                    # The bogus prefix contaminated both the display name and slug.
                    rename_names = [
                        candidate if value == name else value
                        for value in names
                        if value != name or candidate not in names
                    ]
                    additions.setdefault(canonical_slug, [])
                    for value in rename_names:
                        if value not in additions[canonical_slug]:
                            additions[canonical_slug].append(value)
                    remove_slugs.add(slug)
                    renamed_slugs.append((slug, canonical_slug, name, candidate))
                    updated = []
                    break
                replaced.append((slug, name, candidate))
                if candidate not in updated:
                    updated.append(candidate)
                continue

            if (
                owners == {canonical_slug}
                and slug == f"null-{canonical_slug}"
                and all(
                    value.startswith("null ")
                    and value.removeprefix("null ").strip() == candidate
                    for value in names
                )
            ):
                # A separate null-* identity duplicates the already-canonical slug.
                remove_slugs.add(slug)
                duplicate_slugs.append((slug, canonical_slug, name, candidate))
                updated = []
                break

            collisions.append((slug, name, candidate, tuple(sorted(owners))))
            updated.append(name)

        result[slug] = updated

    for slug in remove_slugs:
        result.pop(slug, None)
    for slug, names in additions.items():
        if slug in result:
            collisions.append((slug, "<slug rename>", ", ".join(names), (slug,)))
            continue
        result[slug] = names

    # Empty entries can only arise from a deliberately removed null-* slug.
    result = {slug: names for slug, names in result.items() if names}
    if not collisions:
        validate_author_mappings(result)
    return (
        result,
        same_slug,
        replaced,
        renamed_slugs,
        duplicate_slugs,
        collisions,
        unresolved,
    )


def main() -> int:
    config = load_config(ROOT / "bibreview.yml")
    publications = read_bibliography(config.paths.bibliography)
    mapping = read_json(config.paths.author_mappings, dict)
    canonical_occurrences = publication_author_names(publications)
    canonical_names = set(canonical_occurrences)

    legacy_plan = legacy_author_mapping_plan(DOCS)
    before = plan_author_mappings(publications, mapping)
    (
        cleaned,
        same_slug,
        replaced,
        renamed_slugs,
        duplicate_slugs,
        collisions,
        unresolved,
    ) = cleaned_mapping(mapping, canonical_names)
    after = plan_author_mappings(publications, cleaned) if not collisions else None

    mapped_variants = sum(len(names) for names in mapping.values())
    cleaned_variants = sum(len(names) for names in cleaned.values())
    literal_names = {
        author.literal.strip()
        for publication in publications
        for author in publication.authors
        if author.literal and author.literal.strip()
    }
    family_only_names = {
        author.family.strip()
        for publication in publications
        for author in publication.authors
        if (
            not author.literal
            and not (author.given or "").strip()
            and (author.family or "").strip()
        )
    }

    print(f"publications: {len(publications)}")
    print(f"canonical author occurrences: {len(canonical_occurrences)}")
    print(f"canonical distinct source names: {len(canonical_names)}")
    print(f"mapping slugs: {len(mapping)}")
    print(f"mapping name variants: {mapped_variants}")
    print(f"literal distinct source names: {len(literal_names)}")
    print(f"family-only distinct source names: {len(family_only_names)}")
    print(f"historical unknown names: {legacy_plan['unknown_names']}")
    print(f"canonical unknown names before cleanup: {before.unknown_names}")
    print(f"null variants already paired in same slug: {len(same_slug)}")
    print(f"null variants replaceable in existing slug: {len(replaced)}")
    print(f"null-prefixed slugs safely renameable: {len(renamed_slugs)}")
    print(f"duplicate null-prefixed slugs safely collapsible: {len(duplicate_slugs)}")
    print(f"non-deterministic null collisions: {len(collisions)}")
    print(f"unresolved historical null variants: {len(unresolved)}")
    print(f"mapping variants after deterministic cleanup: {cleaned_variants}")
    if after is not None:
        print(f"canonical unknown names after cleanup: {after.unknown_names}")
        print(f"canonical safe proposals after cleanup: {len(after.safe)}")
        print(f"canonical review proposals after cleanup: {len(after.review)}")

    for label, items in (
        ("same-slug null variants", same_slug),
        ("replaceable null variants", replaced),
        ("renameable null slugs", renamed_slugs),
        ("duplicate null slugs", duplicate_slugs),
    ):
        if items:
            print(f"sample {label}:")
            for item in items[:10]:
                print("  " + " -> ".join(repr(value) for value in item))

    if collisions:
        print("non-deterministic null collisions:")
        for slug, old, candidate, owners in collisions:
            print(f"  {slug}: {old!r} -> {candidate!r}; existing owners={owners!r}")
    if unresolved:
        print("unresolved null variants:")
        for slug, old, candidate in unresolved:
            print(f"  {slug}: {old!r}; canonical candidate={candidate!r}")

    if after is not None and after.safe:
        print("safe canonical proposals after cleanup:")
        for slug, names in list(after.safe.items())[:25]:
            print(f"  + {slug}: {', '.join(names)}")
    if after is not None and after.review:
        print("manual-review canonical proposals after cleanup:")
        for item in after.review[:25]:
            print(f"  ? {item.slug}: {', '.join(item.names)}")
            print(f"    {'; '.join(item.reasons)}")

    if collisions:
        raise AssertionError("some null author variants require human identity review")
    if unresolved:
        raise AssertionError("some historical null author variants have no canonical source name")

    # Every family-only canonical source name must be represented after cleanup.
    _, cleaned_reverse = validate_author_mappings(cleaned)
    missing_family_only = sorted(family_only_names - cleaned_reverse.keys())
    if missing_family_only:
        raise AssertionError(
            "family-only canonical names remain unmapped after cleanup: "
            + ", ".join(missing_family_only)
        )

    # This is audit-only: the tracked mapping must remain untouched here.
    if json.loads(config.paths.author_mappings.read_text(encoding="utf-8")) != mapping:
        raise AssertionError("author mapping audit mutated project state")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
