#!/usr/bin/env python3
"""Fetch the latest port-Hamiltonian papers from arXiv and cache them as JSON."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ARXIV_API = "https://export.arxiv.org/api/query"
OUTPUT = Path("docs/data/arxiv.json")
MAX_RESULTS = 25
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _clean(text: str | None) -> str:
    return (text or "").strip()


def fetch_papers() -> list[dict[str, object]]:
    params = urlencode(
        {
            "search_query": "all:port AND all:Hamiltonian",
            "start": 0,
            "max_results": MAX_RESULTS,
            "sortBy": "lastUpdatedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API}?{params}"
    request = Request(
        url,
        headers={
            "User-Agent": (
                "PHRAISE/1.0 (arXiv cache; "
                "https://g-haine.github.io/phraise/)"
            )
        },
    )

    with urlopen(request, timeout=30) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    papers: list[dict[str, object]] = []

    for entry in root.findall("atom:entry", ATOM_NS):
        authors = [
            _clean(author.findtext("atom:name", namespaces=ATOM_NS))
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        papers.append(
            {
                "title": _clean(entry.findtext("atom:title", namespaces=ATOM_NS)),
                "summary": _clean(entry.findtext("atom:summary", namespaces=ATOM_NS)),
                "url": _clean(entry.findtext("atom:id", namespaces=ATOM_NS)),
                "authors": authors,
                "updated": _clean(
                    entry.findtext("atom:updated", namespaces=ATOM_NS)
                ).split("T", 1)[0],
            }
        )

    if not papers:
        raise RuntimeError("arXiv returned no entries; refusing to overwrite the cache")

    return papers


def main() -> None:
    papers = fetch_papers()

    if OUTPUT.exists():
        try:
            current = json.loads(OUTPUT.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            current = {}
        if current.get("papers") == papers:
            print("arXiv cache is already up to date")
            return

    payload = {
        "generated_at": datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "papers": papers,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated {OUTPUT} with {len(papers)} papers")


if __name__ == "__main__":
    main()
