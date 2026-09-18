#!/usr/bin/env python3
"""One-shot migration of PHRAISE bibliography.json to BibReview document shape."""

from __future__ import annotations

import json
from pathlib import Path
import re
import tempfile
import os

ROOT = Path(__file__).resolve().parents[2]
BIBLIOGRAPHY = ROOT / "docs/assets/data/bibliography.json"
LIBRARY = ROOT / "docs/_data/library.yml"
EXPECTED_PUBLICATIONS = 2349


def main() -> None:
    raw = json.loads(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    if isinstance(raw, dict):
        if set(raw) != {"metadata", "publications"}:
            raise SystemExit("unexpected existing bibliography document fields")
        publications = raw["publications"]
        if not isinstance(publications, list) or len(publications) != EXPECTED_PUBLICATIONS:
            raise SystemExit("unexpected existing bibliography publication count")
        print("bibliography.json already uses BibReview document shape")
        return

    if not isinstance(raw, list) or len(raw) != EXPECTED_PUBLICATIONS:
        raise SystemExit(
            f"expected historical list with {EXPECTED_PUBLICATIONS} publications"
        )

    match = re.search(
        r'^last_update:\s*["\']?(\d{4}-\d{2}-\d{2})["\']?\s*$',
        LIBRARY.read_text(encoding="utf-8"),
        flags=re.MULTILINE,
    )
    if match is None:
        raise SystemExit("could not read last_update from docs/_data/library.yml")

    document = {
        "metadata": {
            "schema_version": 1,
            "last_update": match.group(1),
        },
        "publications": raw,
    }
    payload = json.dumps(
        document,
        ensure_ascii=False,
        indent=2,
        allow_nan=False,
    ) + "\n"

    BIBLIOGRAPHY.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=BIBLIOGRAPHY.parent,
        prefix=f".{BIBLIOGRAPHY.name}.",
        delete=False,
    ) as stream:
        temporary = Path(stream.name)
        stream.write(payload)
    try:
        os.replace(temporary, BIBLIOGRAPHY)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "migrated bibliography.json: "
        f"{len(raw)} publications; last_update={match.group(1)}"
    )


if __name__ == "__main__":
    main()
