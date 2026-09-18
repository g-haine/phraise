#!/usr/bin/env python3
"""Validate the PHRAISE writer cutover through its public generation functions."""
from __future__ import annotations

from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

import sys
sys.path.insert(0, str(DOCS))

from phraise_tools.generate import generate_pages, generate_posts  # noqa: E402


MANAGED_ROOTS = ("_posts", "authors", "years")


class NoNetworkBibTeXClient:
    """Fail if the real PHRAISE tree unexpectedly requires a BibTeX download."""

    def bibtex(self, doi: str) -> str:
        raise AssertionError(f"unexpected BibTeX network fallback for {doi}")


def _snapshot(root: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    for folder in MANAGED_ROOTS:
        directory = root / folder
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                result[path.relative_to(root).as_posix()] = path.read_bytes()
    return result


def main() -> None:
    expected = _snapshot(DOCS)

    with tempfile.TemporaryDirectory() as tmp:
        site_root = Path(tmp) / "docs"
        shutil.copytree(DOCS, site_root)

        stale = (
            site_root / "_posts" / "__bibreview_writer_probe__.md",
            site_root / "authors" / "__bibreview_writer_probe__.md",
            site_root / "years" / "__bibreview_writer_probe__.md",
        )
        for path in stale:
            path.write_text("obsolete generated probe\n", encoding="utf-8")

        manual = site_root / "__bibreview_manual_probe__.txt"
        manual.write_text("manual content must remain untouched\n", encoding="utf-8")
        manual_before = manual.read_bytes()

        legacy = site_root / "assets/data/biblio.json"
        legacy.write_text(
            "{ deliberately invalid legacy projection",
            encoding="utf-8",
        )
        legacy_before = legacy.read_bytes()

        generate_posts(site_root, NoNetworkBibTeXClient())
        generate_pages(site_root)

        for path in stale:
            assert not path.exists(), f"obsolete generated probe survived: {path}"
        assert manual.read_bytes() == manual_before
        assert legacy.read_bytes() == legacy_before
        assert _snapshot(site_root) == expected

    posts = sum(path.startswith("_posts/") for path in expected)
    author_year = len(expected) - posts
    print("PHRAISE BibReview writer cutover: OK")
    print(f"  publication posts byte-identical after real writer: {posts}")
    print(f"  author/year artifacts byte-identical after real writer: {author_year}")
    print("  obsolete probes removed through public writer path: 3")
    print("  tracked BibTeX required network fallback: no")
    print("  invalid legacy biblio.json ignored by writer: yes")
    print("  manual file outside managed roots untouched: yes")


if __name__ == "__main__":
    main()
