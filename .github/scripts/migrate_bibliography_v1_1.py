"""One-shot PHRAISE bibliography repair for the BibReview 1.1 contributor invariant.

This migration is intentionally project-specific and temporary. It repairs the
reviewed historical author/editor cases, removes three confirmed bad/duplicate
records, updates tracked BibTeX, and leaves site regeneration to BibReview.
"""

from __future__ import annotations

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
BIBLIOGRAPHY = ROOT / "docs/assets/data/bibliography.json"
AUTHOR_MAPPINGS = ROOT / "docs/assets/data/author_mappings.json"
KNOWN = ROOT / "docs/DOI.txt"
BIB_DIR = ROOT / "docs/assets/bib"

EXPECTED_AUTHORLESS = 18
EXPECTED_PUBLICATIONS_BEFORE = 2349
EXPECTED_PUBLICATIONS_AFTER = 2346
MIGRATION_DATE = "2026-09-21"


def contributor(given: str, family: str, *, first: bool = False) -> dict:
    return {
        "given": given,
        "family": family,
        "literal": None,
        "source_fields": {
            "sequence": "first" if first else "additional",
        },
    }


SECCHI_TEAM = [
    contributor("Cristian", "Secchi", first=True),
    contributor("Cesare", "Fantuzzi"),
    contributor("Stefano", "Stramigioli"),
]

AUTHOR_REPAIRS = {
    "10.1007/978-3-540-49715-8": SECCHI_TEAM,
    "10.1007/978-3-540-49715-8_1": SECCHI_TEAM,
    "10.1007/978-3-540-49715-8_2": SECCHI_TEAM,
    "10.1007/978-3-540-49715-8_3": SECCHI_TEAM,
    "10.1007/978-3-540-49715-8_4": SECCHI_TEAM,
    "10.1007/978-3-540-49715-8_5": SECCHI_TEAM,
    "10.1007/bfb0110406": [
        contributor("Stefano", "Stramigioli", first=True),
    ],
    "10.1049/pbce076e_ch6": [
        contributor("H.", "Fujioka", first=True),
    ],
    "10.1109/mcs.2007.338279": [
        contributor("Peter J.", "Gawthrop", first=True),
        contributor("Geraint P.", "Bevan"),
    ],
    "10.1109/tac.2004.840477": [
        contributor("Romeo", "Ortega", first=True),
        contributor("Martha", "Galaz"),
        contributor("Alessandro", "Astolfi"),
        contributor("Yuanzhang", "Sun"),
        contributor("Tielong", "Shen"),
    ],
    "10.1142/9789813230392_0002": [
        contributor("Vladimir G.", "Ivancevic", first=True),
        contributor("Darryn J.", "Reid"),
        contributor("Michael J.", "Pilling"),
    ],
    "10.1515/9781400865246.221": [
        contributor("Wassim M.", "Haddad", first=True),
        contributor("VijaySekhar", "Chellaboina"),
        contributor("Sergey G.", "Nersesov"),
    ],
    "10.20508/ijrer.v9i4.9737.g7782": [
        contributor("Nidhal", "Khefifi", first=True),
        contributor("Azeddine", "Houari"),
        contributor("Mohamed", "Machmoum"),
        contributor("Malek", "Ghanes"),
    ],
}

EDITOR_REPAIRS = {
    "10.1007/978-94-007-0089-5": [
        contributor("Peter", "Benner", first=True),
        contributor("Michael", "Hinze"),
        contributor("E. Jan W.", "ter Maten"),
    ],
    "10.1007/978-3-642-34928-7": [
        contributor("Achim", "Ilchmann", first=True),
        contributor("Timo", "Reis"),
    ],
}

DELETE_DOIS = {
    "10.1002/pamm.201900001",
    "10.1016/0967-0661(93)90438-w",
    "10.1201/b19290-8",
}

EXPECTED_DUPLICATE = {
    "bad": "10.1201/b19290-8",
    "good": "10.1201/b19290-4",
}

NEW_AUTHOR_MAPPINGS = {
    "h-fujioka": ["H. Fujioka"],
    "peter-j-gawthrop": ["Peter J. Gawthrop"],
    "geraint-p-bevan": ["Geraint P. Bevan"],
    "vladimir-g-ivancevic": ["Vladimir G. Ivancevic"],
    "darryn-j-reid": ["Darryn J. Reid"],
    "michael-j-pilling": ["Michael J. Pilling"],
}


def display_names(values: list[dict]) -> list[str]:
    return [
        " ".join(part for part in (item.get("given"), item.get("family")) if part)
        if not item.get("literal")
        else item["literal"]
        for item in values
    ]


def set_bibtex_field(text: str, field: str, value: str) -> str:
    line = f"  {field}={{{value}}},"
    pattern = re.compile(rf"(?im)^\s*{re.escape(field)}\s*=.*$")
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    newline = text.find("\n")
    if newline < 0 or not text.lstrip().startswith("@"):
        raise ValueError(f"cannot insert BibTeX field {field!r}")
    return text[: newline + 1] + line + "\n" + text[newline + 1 :]


def repair_bibtex(publication: dict, *, role: str, contributors: list[dict]) -> None:
    path = BIB_DIR / f"{publication['permalink']}.bib"
    if not path.exists():
        raise SystemExit(f"missing BibTeX source: {path}")

    names = " and ".join(display_names(contributors))
    doi = publication["identifiers"]["doi"]

    if doi == "10.1515/9781400865246.221":
        path.write_text(
            "@inbook{haddad2006energy,\n"
            f"  author={{{names}}},\n"
            f"  title={{{publication['title']}}},\n"
            "  DOI={10.1515/9781400865246.221},\n"
            "  booktitle={Impulsive and Hybrid Dynamical Systems},\n"
            "  publisher={Princeton University Press},\n"
            "  year={2006},\n"
            "  pages={221--318}\n"
            "}\n",
            encoding="utf-8",
        )
        return

    text = path.read_text(encoding="utf-8")
    text = set_bibtex_field(text, "title", publication["title"])
    text = set_bibtex_field(text, role, names)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    document = json.loads(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    publications = document["publications"]

    already_migrated = (
        document.get("metadata", {}).get("schema_version") == 2
        and len(publications) == EXPECTED_PUBLICATIONS_AFTER
        and all(item.get("authors") or item.get("editors") for item in publications)
    )
    if already_migrated:
        print(
            f"Migration already applied: {len(publications)} publications, "
            "all with authors or editors."
        )
        return

    if len(publications) != EXPECTED_PUBLICATIONS_BEFORE:
        raise SystemExit(
            f"expected {EXPECTED_PUBLICATIONS_BEFORE} publications, got {len(publications)}"
        )

    authorless = [item for item in publications if not item.get("authors")]
    if len(authorless) != EXPECTED_AUTHORLESS:
        raise SystemExit(
            f"expected {EXPECTED_AUTHORLESS} authorless records, got {len(authorless)}"
        )

    by_doi = {
        item.get("identifiers", {}).get("doi", "").lower(): item
        for item in publications
        if item.get("identifiers", {}).get("doi")
    }

    if EXPECTED_DUPLICATE["good"] not in by_doi:
        raise SystemExit("confirmed good 10.1201/b19290-4 record is missing")
    good = by_doi[EXPECTED_DUPLICATE["good"]]
    if not good.get("authors"):
        raise SystemExit("confirmed good 10.1201/b19290-4 record unexpectedly has no authors")

    expected_targets = set(AUTHOR_REPAIRS) | set(EDITOR_REPAIRS) | DELETE_DOIS
    actual_targets = {
        item["identifiers"]["doi"].lower()
        for item in authorless
    }
    if actual_targets != expected_targets:
        missing = sorted(expected_targets - actual_targets)
        unexpected = sorted(actual_targets - expected_targets)
        raise SystemExit(
            f"authorless target mismatch; missing={missing}, unexpected={unexpected}"
        )

    for doi, authors in AUTHOR_REPAIRS.items():
        publication = by_doi[doi]
        if publication.get("authors"):
            raise SystemExit(f"{doi}: authors unexpectedly already present")
        publication["authors"] = authors
        publication.pop("editors", None)
        repair_bibtex(publication, role="author", contributors=authors)

    for doi, editors in EDITOR_REPAIRS.items():
        publication = by_doi[doi]
        if publication.get("authors"):
            raise SystemExit(f"{doi}: editor-only repair unexpectedly has authors")
        publication["authors"] = []
        publication["editors"] = editors
        repair_bibtex(publication, role="editor", contributors=editors)

    removed = []
    retained = []
    for publication in publications:
        doi = publication.get("identifiers", {}).get("doi", "").lower()
        if doi in DELETE_DOIS:
            removed.append(publication)
        else:
            retained.append(publication)

    if {item["identifiers"]["doi"].lower() for item in removed} != DELETE_DOIS:
        raise SystemExit("did not remove exactly the three reviewed DOI records")
    document["publications"] = retained
    document["metadata"]["schema_version"] = 2
    document["metadata"]["last_update"] = MIGRATION_DATE

    if len(retained) != EXPECTED_PUBLICATIONS_AFTER:
        raise SystemExit(
            f"expected {EXPECTED_PUBLICATIONS_AFTER} publications after cleanup, got {len(retained)}"
        )
    remaining_without_responsibility = [
        item.get("identifiers", {}).get("doi", item["id"])
        for item in retained
        if not item.get("authors") and not item.get("editors")
    ]
    if remaining_without_responsibility:
        raise SystemExit(
            "records without authors/editors remain: "
            + ", ".join(remaining_without_responsibility)
        )

    dois = [
        item["identifiers"]["doi"].lower()
        for item in retained
        if item.get("identifiers", {}).get("doi")
    ]
    if len(dois) != len(set(dois)):
        raise SystemExit("duplicate canonical DOI after migration")

    BIBLIOGRAPHY.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    mappings = json.loads(AUTHOR_MAPPINGS.read_text(encoding="utf-8"))
    owners = {
        variant: slug
        for slug, variants in mappings.items()
        for variant in variants
    }
    for slug, variants in NEW_AUTHOR_MAPPINGS.items():
        for variant in variants:
            owner = owners.get(variant)
            if owner is not None and owner != slug:
                raise SystemExit(
                    f"author variant {variant!r} already belongs to {owner!r}"
                )
        if slug in mappings and mappings[slug] != variants:
            raise SystemExit(f"author slug {slug!r} already exists with different variants")
        mappings.setdefault(slug, variants)

    AUTHOR_MAPPINGS.write_text(
        json.dumps(mappings, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    known_lines = KNOWN.read_text(encoding="utf-8").splitlines()
    removed_known = {
        line.strip().lower()
        for line in known_lines
        if line.strip().lower() in DELETE_DOIS
    }
    if removed_known != DELETE_DOIS:
        raise SystemExit(
            "known DOI state does not contain exactly the three deletion targets"
        )
    known_lines = [
        line
        for line in known_lines
        if line.strip().lower() not in DELETE_DOIS
    ]
    KNOWN.write_text("\n".join(known_lines) + "\n", encoding="utf-8")

    canonical_dois = {
        item["identifiers"]["doi"].lower()
        for item in retained
        if item.get("identifiers", {}).get("doi")
    }
    known_dois = {
        line.strip().lower()
        for line in known_lines
        if line.strip() and not line.lstrip().startswith("#")
    }
    if known_dois != canonical_dois:
        raise SystemExit(
            f"known/canonical DOI mismatch after migration: "
            f"known_only={sorted(known_dois - canonical_dois)}, "
            f"canonical_only={sorted(canonical_dois - known_dois)}"
        )

    for publication in removed:
        bibtex = BIB_DIR / f"{publication['permalink']}.bib"
        if not bibtex.exists():
            raise SystemExit(f"missing BibTeX source for deleted record: {bibtex}")
        bibtex.unlink()

    print(
        "Migration complete: "
        f"{len(AUTHOR_REPAIRS)} author repairs, "
        f"{len(EDITOR_REPAIRS)} editor repairs, "
        f"{len(removed)} deletions, "
        f"{len(retained)} publications retained."
    )


if __name__ == "__main__":
    main()
