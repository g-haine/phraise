#!/usr/bin/env python3
"""One-off deterministic cleanup of PHRAISE canonical bibliography data."""

from __future__ import annotations

import json
from pathlib import Path

BIBLIOGRAPHY = Path("docs/assets/data/bibliography.json")
ABSTRACT_SENTINELS = {
    "No  available",
    "No abstract available",
    "Not available",
}
UNICODE_HYPHEN = "\u2010"


def count_state(document: dict) -> dict[str, int]:
    empty_references = 0
    sentinel_abstracts = 0
    padded_abstracts = 0
    unicode_reference_dois = 0

    for publication in document["publications"]:
        abstract = publication["abstract"]
        if abstract in ABSTRACT_SENTINELS:
            sentinel_abstracts += 1
        if abstract != abstract.strip():
            padded_abstracts += 1

        for reference in publication.get("references", []):
            identifiers = reference.get("identifiers", {})
            if reference.get("citation", "") == "" and not identifiers:
                empty_references += 1
            doi = identifiers.get("doi")
            if isinstance(doi, str) and UNICODE_HYPHEN in doi:
                unicode_reference_dois += 1

    return {
        "publications": len(document["publications"]),
        "empty_references": empty_references,
        "sentinel_abstracts": sentinel_abstracts,
        "padded_abstracts": padded_abstracts,
        "unicode_reference_dois": unicode_reference_dois,
    }


def main() -> None:
    document = json.loads(BIBLIOGRAPHY.read_text(encoding="utf-8"))

    before = count_state(document)
    expected_before = {
        "publications": 2349,
        "empty_references": 2102,
        "sentinel_abstracts": 110,
        "padded_abstracts": 55,
        "unicode_reference_dois": 13,
    }
    if before != expected_before:
        raise SystemExit(
            f"Refusing cleanup: unexpected input state: {before!r} != {expected_before!r}"
        )

    sentinel_breakdown = {
        value: sum(
            publication["abstract"] == value
            for publication in document["publications"]
        )
        for value in sorted(ABSTRACT_SENTINELS)
    }
    expected_breakdown = {
        "No  available": 62,
        "No abstract available": 24,
        "Not available": 24,
    }
    if sentinel_breakdown != expected_breakdown:
        raise SystemExit(
            "Refusing cleanup: unexpected abstract sentinel breakdown: "
            f"{sentinel_breakdown!r}"
        )

    for publication in document["publications"]:
        abstract = publication["abstract"].strip()
        publication["abstract"] = "" if abstract in ABSTRACT_SENTINELS else abstract

        cleaned_references = []
        for reference in publication.get("references", []):
            identifiers = reference.get("identifiers", {})
            if reference.get("citation", "") == "" and not identifiers:
                continue

            doi = identifiers.get("doi")
            if isinstance(doi, str) and UNICODE_HYPHEN in doi:
                identifiers["doi"] = doi.replace(UNICODE_HYPHEN, "-")

            cleaned_references.append(reference)

        publication["references"] = cleaned_references

    after = count_state(document)
    expected_after = {
        "publications": 2349,
        "empty_references": 0,
        "sentinel_abstracts": 0,
        "padded_abstracts": 0,
        "unicode_reference_dois": 0,
    }
    if after != expected_after:
        raise SystemExit(
            f"Cleanup failed postcondition: {after!r} != {expected_after!r}"
        )

    # Historical mechanical cleanup is not a new BibReview merge.
    if document["metadata"]["last_update"] != "2026-09-11":
        raise SystemExit("Unexpected bibliography metadata.last_update")

    BIBLIOGRAPHY.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("Mechanical bibliography cleanup complete")
    print(f"Before: {before}")
    print(f"Sentinels: {sentinel_breakdown}")
    print(f"After: {after}")


if __name__ == "__main__":
    main()
