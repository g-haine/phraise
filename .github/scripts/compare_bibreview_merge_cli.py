#!/usr/bin/env python3
"""Validate the BibReview merge CLI on a temporary canonical PHRAISE mirror."""
from __future__ import annotations

from datetime import date
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import yaml

DOCS = Path(__file__).resolve().parents[2] / "docs"
sys.path.insert(0, str(DOCS))

spec = importlib.util.spec_from_file_location("concatenate", DOCS / "concatenate.py")
concatenate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(concatenate)

from bibreview.compat import load_legacy_bibliography
from bibreview.identity import new_publication_id, normalize_doi
from bibreview.model import Author, Publication
from bibreview.storage import read_bibliography, write_bibliography
from phraise_tools.bibreview_bridge import publication_to_legacy_record

SOURCE_BIBLIOGRAPHY = DOCS / "assets/data/biblio.json"
SOURCE_KNOWN = DOCS / "DOI.txt"
SOURCE_REJECTED = DOCS / "badDOI.txt"
SOURCE_REVIEW = DOCS / "checkDOI.txt"

ACCEPTED_DOI = "10.9999/bibreview-m3-accepted"
REJECTED_DOI = "10.9999/bibreview-m3-rejected"


def append_line(data: bytes, value: str) -> bytes:
    if data and not data.endswith(b"\n"):
        data += b"\n"
    return data + value.encode("utf-8") + b"\n"


def snapshot(root: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def doi_values(data: bytes) -> tuple[str, ...]:
    values: list[str] = []
    seen: set[str] = set()
    for raw in data.decode("utf-8").splitlines():
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        doi = normalize_doi(value)
        if doi not in seen:
            seen.add(doi)
            values.append(doi)
    return tuple(values)


def synthetic_publication(doi: str, title: str, permalink: str) -> Publication:
    return Publication(
        id=new_publication_id(),
        identifiers={"doi": doi},
        type="journal-article",
        title=title,
        authors=(Author(given="Ada", family="Lovelace"),),
        abstract="Synthetic integration fixture",
        container_title="BibReview Integration Journal",
        publication_year="2026",
        volume="1",
        issue="1",
        pages="1--2",
        publisher="Integration Publisher",
        keywords=("integration", "migration"),
        created_date=date(2026, 9, 17),
        permalink=permalink,
    )


def historical_result(source_records: list[dict], accepted: Publication, rejected: Publication) -> tuple[list[dict], bytes]:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        data = root / "assets/data"
        data.mkdir(parents=True)
        (root / "DOI.txt").write_bytes(SOURCE_KNOWN.read_bytes())
        (root / "newDOI.txt").write_bytes(
            f"{ACCEPTED_DOI}\n{REJECTED_DOI}\n".encode("utf-8")
        )
        rejected_bytes = append_line(SOURCE_REJECTED.read_bytes(), REJECTED_DOI)
        (root / "badDOI.txt").write_bytes(rejected_bytes)
        (data / "biblio.json").write_text(
            json.dumps(
                [publication_to_legacy_record(accepted), publication_to_legacy_record(rejected)],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        backup = data / "biblio-integration.json"
        backup.write_text(json.dumps(source_records, ensure_ascii=False), encoding="utf-8")

        concatenate.concatenate(
            root / "DOI.txt",
            root / "newDOI.txt",
            root / "badDOI.txt",
            data / "biblio.json",
            data,
        )
        return (
            json.loads((data / "biblio.json").read_text(encoding="utf-8")),
            (root / "DOI.txt").read_bytes(),
        )


def write_project_config(root: Path) -> Path:
    config = {
        "schema_version": 1,
        "project": {"name": "PHRAISE integration mirror", "slug": "phraise-integration"},
        "paths": {
            "bibliography": "data/bibliography.json",
            "collected": "data/collected.json",
            "known": "data/known.txt",
            "pending": "data/pending.txt",
            "rejected": "data/rejected.txt",
            "review": "data/review.txt",
            "archive": "archive",
            "author_mappings": "data/authors.json",
            "bibtex": "bib",
            "site": "site",
        },
        "providers": {},
        "site": {"enabled": False},
    }
    path = root / "bibreview.yml"
    path.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
    return path


def main() -> int:
    source_records = json.loads(SOURCE_BIBLIOGRAPHY.read_text(encoding="utf-8"))
    legacy_items = load_legacy_bibliography(SOURCE_BIBLIOGRAPHY)
    existing = tuple(item.publication for item in legacy_items)
    existing_ids = {publication.doi: publication.id for publication in existing}

    accepted = synthetic_publication(ACCEPTED_DOI, "Accepted integration publication", "bibreview-m3-accepted")
    rejected = synthetic_publication(REJECTED_DOI, "Rejected integration publication", "bibreview-m3-rejected")
    historical_records, historical_known = historical_result(source_records, accepted, rejected)

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        data = root / "data"
        data.mkdir(parents=True)
        (root / "archive").mkdir()

        write_bibliography(data / "bibliography.json", existing)
        write_bibliography(data / "collected.json", (accepted, rejected))
        (data / "known.txt").write_bytes(SOURCE_KNOWN.read_bytes())
        (data / "pending.txt").write_text(f"{ACCEPTED_DOI}\n{REJECTED_DOI}\n", encoding="utf-8")
        (data / "rejected.txt").write_bytes(append_line(SOURCE_REJECTED.read_bytes(), REJECTED_DOI))
        (data / "review.txt").write_bytes(
            append_line(append_line(SOURCE_REVIEW.read_bytes(), ACCEPTED_DOI), REJECTED_DOI)
        )
        config = write_project_config(root)

        before = snapshot(root)
        dry = subprocess.run(
            [sys.executable, "-m", "bibreview", "--config", str(config), "--dry-run", "merge"],
            text=True,
            capture_output=True,
        )
        if dry.returncode != 0:
            raise SystemExit(f"BibReview merge dry-run failed: {dry.stderr}")
        if not dry.stdout.startswith("Dry run:"):
            raise SystemExit("BibReview merge dry-run did not report itself as a dry run")
        if snapshot(root) != before:
            raise SystemExit("BibReview merge dry-run modified the temporary PHRAISE mirror")

        old_canonical_bytes = (data / "bibliography.json").read_bytes()
        applied = subprocess.run(
            [sys.executable, "-m", "bibreview", "--config", str(config), "merge"],
            text=True,
            capture_output=True,
        )
        if applied.returncode != 0:
            raise SystemExit(f"BibReview merge failed: {applied.stderr}")

        final = read_bibliography(data / "bibliography.json")
        final_by_doi = {publication.doi: publication for publication in final if publication.doi}
        if len(final) != len(existing) + 1:
            raise SystemExit("BibReview merge produced an unexpected PHRAISE publication count")
        if ACCEPTED_DOI not in final_by_doi or REJECTED_DOI in final_by_doi:
            raise SystemExit("BibReview merge did not apply accepted/rejected DOI semantics")
        for doi, publication_id in existing_ids.items():
            if final_by_doi.get(doi) is None or final_by_doi[doi].id != publication_id:
                raise SystemExit(f"BibReview merge changed persisted UUID for {doi}")

        if read_bibliography(data / "collected.json"):
            raise SystemExit("BibReview merge did not empty collected staging")
        if doi_values((data / "pending.txt").read_bytes()):
            raise SystemExit("BibReview merge did not clear processed pending DOI values")
        review_values = set(doi_values((data / "review.txt").read_bytes()))
        if ACCEPTED_DOI in review_values or REJECTED_DOI in review_values:
            raise SystemExit("BibReview merge did not clear processed review DOI values")

        backups = list((root / "archive").glob("bibliography-*.json"))
        if len(backups) != 1 or backups[0].read_bytes() != old_canonical_bytes:
            raise SystemExit("BibReview merge did not create an exact pre-merge canonical backup")

        historical_dois = {record.get("doi") for record in historical_records if record.get("doi")}
        final_dois = set(final_by_doi)
        if historical_dois != final_dois:
            raise SystemExit("BibReview CLI merge and historical concatenate differ on retained DOI set")
        if set(doi_values(historical_known)) != set(doi_values((data / "known.txt").read_bytes())):
            raise SystemExit("BibReview CLI merge and historical concatenate differ on known DOI semantics")

    print(f"real PHRAISE publications canonicalized for temporary mirror: {len(existing)}")
    print("bibreview --dry-run merge: read-only")
    print("bibreview merge: accepted/rejected queue semantics validated")
    print("persisted UUIDs: preserved for all existing PHRAISE publications")
    print("canonical pre-merge backup: exact")
    print("historical concatenate vs BibReview CLI: retained DOI semantics equivalent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
