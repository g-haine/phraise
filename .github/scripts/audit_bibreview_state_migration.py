#!/usr/bin/env python3
"""Audit a one-shot PHRAISE migration from legacy to canonical BibReview state."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile

DOCS = Path(__file__).resolve().parents[2] / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.compat import load_legacy_bibliography
from bibreview.storage import read_bibliography, write_bibliography
from phraise_tools.bibreview_bridge import publication_to_legacy_record

LEGACY = Path("docs/assets/data/biblio.json")


def differing_paths(left: object, right: object, prefix: str = "") -> list[str]:
    """Return leaf paths whose values differ."""
    if type(left) is not type(right):
        return [prefix or "<root>"]
    if isinstance(left, dict):
        paths: list[str] = []
        for key in sorted(set(left) | set(right)):
            child = f"{prefix}.{key}" if prefix else str(key)
            if key not in left or key not in right:
                paths.append(child)
            else:
                paths.extend(differing_paths(left[key], right[key], child))
        return paths
    if isinstance(left, list):
        paths: list[str] = []
        if len(left) != len(right):
            paths.append(f"{prefix}.length" if prefix else "length")
        for index, (l_item, r_item) in enumerate(zip(left, right)):
            paths.extend(differing_paths(l_item, r_item, f"{prefix}[{index}]"))
        return paths
    return [] if left == right else [prefix or "<root>"]


def category(path: str) -> str:
    """Collapse list indices so the audit reports stable field categories."""
    if path.startswith("authors["):
        return "authors[*]" + path[path.find("]") + 1 :]
    if path.startswith("references["):
        return "references[*]" + path[path.find("]") + 1 :]
    return path


def main() -> int:
    source = json.loads(LEGACY.read_text(encoding="utf-8"))
    legacy_items = load_legacy_bibliography(LEGACY)
    publications = tuple(item.publication for item in legacy_items)

    with tempfile.TemporaryDirectory() as directory:
        canonical_path = Path(directory) / "bibliography.json"
        write_bibliography(canonical_path, publications)
        reloaded = read_bibliography(canonical_path)
        if reloaded != publications:
            raise SystemExit("canonical write/read round-trip changed publications")
        projected = [publication_to_legacy_record(publication) for publication in reloaded]

    if len(projected) != len(source):
        raise SystemExit("canonical migration changed publication count")

    changed_records: list[tuple[int, str | None, list[str]]] = []
    changed_categories: dict[str, int] = {}
    for index, (before, after) in enumerate(zip(source, projected)):
        paths = differing_paths(before, after)
        if not paths:
            continue
        doi = before.get("doi") if isinstance(before, dict) else None
        changed_records.append((index, doi, paths))
        for path in paths:
            key = category(path)
            changed_categories[key] = changed_categories.get(key, 0) + 1

    print(f"legacy publications: {len(source)}")
    print(f"canonical publications: {len(publications)}")
    print(f"unique canonical UUIDs: {len({publication.id for publication in publications})}")
    print(f"records changed after canonical persistence + legacy projection: {len(changed_records)}")
    print("changed path categories:")
    for path, count in sorted(changed_categories.items(), key=lambda item: (-item[1], item[0])):
        print(f"  {count:4d}  {path}")
    print("changed records:")
    for index, doi, paths in changed_records:
        print(f"  index={index} doi={doi!r}: {', '.join(paths)}")

    # This first migration audit deliberately fails if the persistent canonical
    # form exposes anything beyond the two legacy irregularities already found
    # during the compatibility work: one empty author entry and one malformed
    # reference DOI. The exact affected DOI values are reported above rather
    # than hard-coded as part of BibReview's generic contract.
    if len(changed_records) != 2:
        raise SystemExit(
            "unexpected canonical migration surface: expected exactly two known legacy irregularities"
        )
    allowed = {"authors.length", "references[*].doi"}
    unexpected = set(changed_categories) - allowed
    if unexpected:
        raise SystemExit("unexpected canonical migration fields: " + ", ".join(sorted(unexpected)))

    print("migration audit: only the two previously known legacy irregularities differ")
    print("repository state: read-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
