#!/usr/bin/env python3
"""Fetch the latest port-Hamiltonian papers from arXiv and cache them as JSON."""

from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ARXIV_API = "https://export.arxiv.org/api/query"
OUTPUT = Path("docs/data/arxiv.json")
MAX_RESULTS = 25
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
RETRY_DELAYS_SECONDS = (60, 180, 600)
MAX_RETRY_AFTER_SECONDS = 300
RETRYABLE_HTTP_STATUS_CODES = {408, 429, 500, 502, 503, 504}


class TemporaryArxivError(RuntimeError):
    """Report a transient arXiv failure after all retry attempts are exhausted."""


def _clean(text: str | None) -> str:
    return (text or "").strip()


def _warning(message: str) -> None:
    """Emit a warning that is visible in the GitHub Actions summary."""
    print(f"::warning title=Temporary arXiv API failure::{message}")


def _retry_after_seconds(error: HTTPError) -> int | None:
    """Return a bounded Retry-After delay from an HTTP error, when available."""
    value = error.headers.get("Retry-After") if error.headers else None
    if not value:
        return None

    try:
        seconds = math.ceil(float(value))
    except (ValueError, OverflowError):
        try:
            retry_at = parsedate_to_datetime(value)
            if retry_at.tzinfo is None:
                retry_at = retry_at.replace(tzinfo=timezone.utc)
            seconds = math.ceil(
                (retry_at - datetime.now(timezone.utc)).total_seconds()
            )
        except (TypeError, ValueError, OverflowError):
            return None

    return min(max(seconds, 1), MAX_RETRY_AFTER_SECONDS)


def _fetch_xml(request: Request) -> bytes:
    """Fetch the Atom feed, retrying transient HTTP and network failures."""
    attempts = len(RETRY_DELAYS_SECONDS) + 1

    for attempt in range(attempts):
        retry_after: int | None = None
        try:
            with urlopen(request, timeout=30) as response:
                return response.read()
        except HTTPError as error:
            if error.code not in RETRYABLE_HTTP_STATUS_CODES:
                raise
            failure = f"arXiv returned HTTP {error.code}"
            retry_after = _retry_after_seconds(error)
        except (URLError, TimeoutError) as error:
            failure = f"arXiv request failed: {error}"

        if attempt == attempts - 1:
            raise TemporaryArxivError(
                f"{failure} after {attempts} attempts"
            ) from None

        delay = retry_after or RETRY_DELAYS_SECONDS[attempt]
        _warning(
            f"{failure}; retrying in {delay} seconds "
            f"(attempt {attempt + 2}/{attempts})"
        )
        time.sleep(delay)

    raise AssertionError("unreachable")


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

    root = ET.fromstring(_fetch_xml(request))
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
    try:
        papers = fetch_papers()
    except TemporaryArxivError as error:
        _warning(f"{error}; keeping the existing cache unchanged")
        return

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
