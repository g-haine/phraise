#!/usr/bin/env python3
"""Apply or validate the one-shot PHRAISE author-data cleanup for BibReview."""
from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from audit_bibreview_authors import cleaned_mapping
from bibreview.config import load_config
from bibreview.pipeline.authors import plan_author_mappings, publication_author_names
from bibreview.storage import (
    atomic_write_batch,
    bibliography_data,
    json_bytes,
    read_bibliography,
    read_json,
)
from phraise_tools.bibreview_bridge import publication_to_legacy_record

LEGACY_BIBLIOGRAPHY = DOCS / "assets" / "data" / "biblio.json"

# These 25 exact strings were inspected in PR #35.  Every occurrence is an
# affiliation/address interleaved with real person authors, never a legitimate
# group author.  This set is intentionally PHRAISE-specific; BibReview itself
# continues to support literal/group authors.
MALFORMED_LITERAL_AUTHORS = frozenset(
    {
        ",Applied Mechanics and Aerospace Engineering, Waseda University, Okubo, Shinjuku, Tokyo 169-8555",
        ",Department of Mathematics, Imperial College London, South Kensington Campus, London, SW7 2AZ",
        ",Departamento de Matemática, Universidad Nacional del Sur, CONICET, Av. Alem 1253, 8000 Bahía Blanca, Argentina",
        ",FEMTO-ST/AS2M, ENSMM Besan¸con, 24 rue Alain Savary, 25 000 Besanon",
        "Department of Engineering Mechanics, Dalian University of Technology, Linggong Road No.2, 116085, Dalian V.R China",
        "Institute of Automation, Qufu Normal University, Qufu 273165, China",
        ",LCIS Laboratoire de Conception et d'Intégration des Systèmes, Grenoble Alpes University, F-26902",
        ",LAGEP, Université de Lyon, Lyon, F-69003",
        "Fédération ENAC ISAE-SUPAERO ONERA, Université de Toulouse, Toulouse, France",
        "Université Grenoble Alpes, Grenoble INP, Laboratoire de Conception et d'Intégration des Systèmes, Valence, France",
        "Chair of Materials Handling, Material Flow, Logistics, Technical University of Munich, Boltzmannstr. 15, 85748, Garching,Germany",
        ",University of Wuppertal, Work group Functional Analysis, 42097 Wuppertal, Germany",
        "Technische Universität Ilmenau, Germany",
        "Universität Augsburg, Germany",
        "Universidad Autónoma de San Luis Potosí, México",
        "Universidad Nacional Autónoma de México",
        "Universidad Nacional Autónoma de México, México",
        "Universidad Autónoma de San Luis Potosí",
        ",Departamento de Matemática Aplicada, Universidad Politécnica de Madrid, Av. Juan de Herrera 4, 28040 Madrid, Spain",
        ",Instituto de Ciencias Matemáticas (CSIC-UAM-UC3M-UCM), C/Nicolás Cabrera 13-15, 28049 Madrid, Spain",
        "Delft University of Technology",
        ",Department of Mathematics, Namik Kemal University, 59030 Tekirdaǧ",
        ",Division of Mathematical Methods in Physics, University of Warsaw, ul. Pasteura 5, 02-093 Warszawa",
        ",Institute of Mathematics, Polish Academy of Sciences, Śniadeckich 8, 00-656 Warszawa",
        ",Fachbereich C - Mathematik und Naturwissenschaften, Bergische Universität Wuppertal, Gaußstraße 20, D-42119 Wuppertal",
    }
)


def mapping_bytes(mapping: dict[str, list[str]]) -> bytes:
    """Preserve PHRAISE's compact historical author-mapping layout."""
    lines = ["{"]
    items = list(mapping.items())
    for index, (slug, names) in enumerate(items):
        encoded_slug = json.dumps(slug, ensure_ascii=False)
        encoded_names = ", ".join(json.dumps(name, ensure_ascii=False) for name in names)
        lines.append(f"  {encoded_slug}: [ {encoded_names} ]")
        if index != len(items) - 1:
            lines.append(",")
    lines.append("}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def malformed_literal_names(publications) -> set[str]:
    return {
        author.literal.strip()
        for publication in publications
        for author in publication.authors
        if author.literal and author.literal.strip()
    }


def cleaned_publications(publications):
    actual = malformed_literal_names(publications)
    if actual and actual != MALFORMED_LITERAL_AUTHORS:
        missing = sorted(MALFORMED_LITERAL_AUTHORS - actual)
        unexpected = sorted(actual - MALFORMED_LITERAL_AUTHORS)
        raise AssertionError(
            "literal-author review surface changed; "
            f"missing={missing!r}; unexpected={unexpected!r}"
        )

    removed = 0
    result = []
    for publication in publications:
        authors = tuple(
            author
            for author in publication.authors
            if not (
                author.literal
                and author.literal.strip() in MALFORMED_LITERAL_AUTHORS
            )
        )
        removed += len(publication.authors) - len(authors)
        if (
            publication.authors
            and not authors
            and publication.doi != "10.1002/pamm.201900001"
        ):
            raise AssertionError(f"cleanup would remove every author from {publication.doi}")
        result.append(replace(publication, authors=authors))
    return tuple(result), removed


def clean_state(config):
    publications = read_bibliography(config.paths.bibliography)
    mapping = read_json(config.paths.author_mappings, dict)
    cleaned_publication_state, removed = cleaned_publications(publications)
    canonical_names = set(publication_author_names(cleaned_publication_state))

    (
        cleaned_author_mapping,
        same_slug,
        replaced,
        renamed_slugs,
        duplicate_slugs,
        collisions,
        unresolved,
    ) = cleaned_mapping(mapping, canonical_names)

    if collisions:
        raise AssertionError(f"non-deterministic null-author collisions: {collisions!r}")
    if unresolved:
        raise AssertionError(f"unresolved null-author variants: {unresolved!r}")

    plan = plan_author_mappings(cleaned_publication_state, cleaned_author_mapping)
    if plan.unknown_names or plan.safe or plan.review:
        raise AssertionError(
            "author cleanup does not yield a closed mapping state: "
            f"unknown={plan.unknown_names}; safe={dict(plan.safe)!r}; review={plan.review!r}"
        )

    residual_null = [
        (slug, name)
        for slug, names in cleaned_author_mapping.items()
        for name in names
        if name.startswith("null ")
    ]
    if residual_null:
        raise AssertionError(f"residual null author variants: {residual_null!r}")

    return {
        "publications": cleaned_publication_state,
        "mapping": cleaned_author_mapping,
        "removed_literals": removed,
        "same_slug": same_slug,
        "replaced": replaced,
        "renamed_slugs": renamed_slugs,
        "duplicate_slugs": duplicate_slugs,
    }


def validate_cutover(config) -> dict:
    state = clean_state(config)
    current_publications = read_bibliography(config.paths.bibliography)
    if malformed_literal_names(current_publications):
        raise AssertionError("malformed literal affiliation authors remain in canonical state")
    current_mapping = read_json(config.paths.author_mappings, dict)
    if current_mapping != state["mapping"]:
        raise AssertionError("author mapping is not in deterministic post-cutover form")
    expected_legacy = json_bytes(
        [publication_to_legacy_record(publication) for publication in current_publications]
    )
    if LEGACY_BIBLIOGRAPHY.read_bytes() != expected_legacy:
        raise AssertionError("legacy bibliography projection is out of date after author cutover")
    return state


def write_cutover(config) -> dict:
    before_publications = read_bibliography(config.paths.bibliography)
    before_literals = malformed_literal_names(before_publications)
    state = clean_state(config)

    if before_literals:
        if state["removed_literals"] != 53:
            raise AssertionError(
                f"expected to remove 53 malformed literal-author occurrences, got {state['removed_literals']}"
            )
        expected_counts = (48, 2, 4, 2)
        actual_counts = (
            len(state["same_slug"]),
            len(state["replaced"]),
            len(state["renamed_slugs"]),
            len(state["duplicate_slugs"]),
        )
        if actual_counts != expected_counts:
            raise AssertionError(
                f"historical null cleanup surface changed: expected {expected_counts}, got {actual_counts}"
            )

    outputs = {
        config.paths.bibliography: json_bytes(bibliography_data(state["publications"])),
        config.paths.author_mappings: mapping_bytes(state["mapping"]),
        LEGACY_BIBLIOGRAPHY: json_bytes(
            [publication_to_legacy_record(publication) for publication in state["publications"]]
        ),
    }
    atomic_write_batch(outputs)
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="apply the reviewed one-shot cleanup; default is post-cutover validation",
    )
    args = parser.parse_args()

    config = load_config(ROOT / "bibreview.yml")
    if args.write:
        state = write_cutover(config)
        print(f"removed malformed literal-author occurrences: {state['removed_literals']}")
        print(f"author mapping slugs after cleanup: {len(state['mapping'])}")
        print("author-data cutover written")
    else:
        state = validate_cutover(config)
        print(f"canonical publications: {len(state['publications'])}")
        print("malformed literal-author occurrences: 0")
        print("historical null author variants: 0")
        print("unknown canonical author names: 0")
        print("safe author proposals: 0")
        print("manual-review author proposals: 0")
        print(f"author mapping slugs: {len(state['mapping'])}")
        print("author-data cutover: exact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
