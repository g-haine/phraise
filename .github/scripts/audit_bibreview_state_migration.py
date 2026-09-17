#!/usr/bin/env python3
"""Audit a one-shot PHRAISE migration from legacy to canonical BibReview state."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
import tempfile

DOCS = Path(__file__).resolve().parents[2] / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.compat import load_legacy_bibliography
from bibreview.identity import IdentityError, normalize_doi
from bibreview.storage import read_bibliography, write_bibliography
from phraise_tools.bibreview_bridge import publication_to_legacy_record

LEGACY = Path("docs/assets/data/biblio.json")
_MISSING = object()
_INDEX = re.compile(r"\[\d+\]")


@dataclass(frozen=True)
class Difference:
    path: str
    before: object
    after: object

    @property
    def category(self) -> str:
        return _INDEX.sub("[*]", self.path)


def differences(left: object, right: object, prefix: str = "") -> list[Difference]:
    """Return leaf differences with their before/after values."""
    if type(left) is not type(right):
        return [Difference(prefix or "<root>", left, right)]
    if isinstance(left, dict):
        result: list[Difference] = []
        for key in sorted(set(left) | set(right)):
            child = f"{prefix}.{key}" if prefix else str(key)
            if key not in left:
                result.append(Difference(child, _MISSING, right[key]))
            elif key not in right:
                result.append(Difference(child, left[key], _MISSING))
            else:
                result.extend(differences(left[key], right[key], child))
        return result
    if isinstance(left, list):
        result: list[Difference] = []
        if len(left) != len(right):
            result.append(Difference(f"{prefix}.length", len(left), len(right)))
        for index, (l_item, r_item) in enumerate(zip(left, right)):
            result.extend(differences(l_item, r_item, f"{prefix}[{index}]"))
        return result
    return [] if left == right else [Difference(prefix or "<root>", left, right)]


def _display(value: object) -> str:
    if value is _MISSING:
        return "<missing>"
    text = repr(value)
    return text if len(text) <= 180 else text[:177] + "..."


def _normalized_doi(value: object) -> str | None:
    if not isinstance(value, str) or not value.strip() or value.strip().lower() == "null":
        return None
    try:
        return normalize_doi(value)
    except IdentityError:
        return None


def _doi_difference_class(diff: Difference) -> str:
    before = _normalized_doi(diff.before)
    after = _normalized_doi(diff.after)
    if before is not None and before == after:
        return "equivalent-normalization"
    if before is None and after is None:
        return "both-noncanonical-or-missing"
    if before is None and after is not None:
        return "canonical-doi-added"
    if before is not None and after is None:
        return "canonical-doi-lost"
    return "semantic-doi-change"


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

    category_counts: dict[str, int] = defaultdict(int)
    category_examples: dict[str, list[tuple[int, str | None, Difference]]] = defaultdict(list)
    doi_classes: dict[str, int] = defaultdict(int)
    doi_class_examples: dict[str, list[tuple[int, str | None, Difference]]] = defaultdict(list)
    changed_record_count = 0

    for index, (before, after) in enumerate(zip(source, projected)):
        record_diffs = differences(before, after)
        if not record_diffs:
            continue
        changed_record_count += 1
        publication_doi = before.get("doi") if isinstance(before, dict) else None
        for diff in record_diffs:
            category_counts[diff.category] += 1
            if len(category_examples[diff.category]) < 3:
                category_examples[diff.category].append((index, publication_doi, diff))
            if diff.category == "references[*].doi":
                kind = _doi_difference_class(diff)
                doi_classes[kind] += 1
                if len(doi_class_examples[kind]) < 3:
                    doi_class_examples[kind].append((index, publication_doi, diff))

    print(f"legacy publications: {len(source)}")
    print(f"canonical publications: {len(publications)}")
    print(f"unique canonical UUIDs: {len({publication.id for publication in publications})}")
    print(f"records changed after canonical persistence + legacy projection: {changed_record_count}")
    print("changed path categories:")
    for category, count in sorted(category_counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"  {count:5d}  {category}")
        for index, publication_doi, diff in category_examples[category]:
            print(
                f"         example index={index} publication_doi={publication_doi!r} "
                f"path={diff.path}: {_display(diff.before)} -> {_display(diff.after)}"
            )

    if doi_classes:
        print("reference DOI difference classification:")
        for kind, count in sorted(doi_classes.items(), key=lambda item: (-item[1], item[0])):
            print(f"  {count:5d}  {kind}")
            for index, publication_doi, diff in doi_class_examples[kind]:
                print(
                    f"         example index={index} publication_doi={publication_doi!r} "
                    f"path={diff.path}: {_display(diff.before)} -> {_display(diff.after)}"
                )

    # The fidelity fixes upstream must leave only DOI representation changes in
    # references. This remains red until the two non-canonical source values
    # are identified and explicitly reviewed below.
    expected_categories = {"references[*].doi"}
    unexpected = set(category_counts) - expected_categories
    semantic_doi_changes = sum(
        count
        for kind, count in doi_classes.items()
        if kind not in {"equivalent-normalization", "both-noncanonical-or-missing"}
    )
    noncanonical_reference_dois = doi_classes.get("both-noncanonical-or-missing", 0)
    if unexpected or semantic_doi_changes or noncanonical_reference_dois != 2:
        reasons = []
        if unexpected:
            reasons.append("unexpected fields: " + ", ".join(sorted(unexpected)))
        if semantic_doi_changes:
            reasons.append(f"semantic reference DOI changes: {semantic_doi_changes}")
        if noncanonical_reference_dois != 2:
            reasons.append(
                "non-canonical reference DOI differences: "
                f"{noncanonical_reference_dois} (expected 2 pending review)"
            )
        raise SystemExit("migration audit requires review: " + "; ".join(reasons))

    raise SystemExit(
        "migration audit requires review: two non-canonical reference DOI values remain; "
        "see classified examples above"
    )


if __name__ == "__main__":
    raise SystemExit(main())
