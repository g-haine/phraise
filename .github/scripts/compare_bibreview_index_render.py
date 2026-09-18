#!/usr/bin/env python3
"""Compare legacy PHRAISE index rendering with BibReview byte-for-byte."""
from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))

from bibreview.config import load_config  # noqa: E402
from bibreview.site import (  # noqa: E402
    JekyllIndexRenderOptions,
    build_site_model,
    render_jekyll_index_pages,
)
from bibreview.storage import read_bibliography, read_json  # noqa: E402
from phraise_tools.generate import generate_pages  # noqa: E402


PHRAISE_AUTHOR_INDEX_EXTRA_HTML = (
    "<p id='info-authors'>For <a href='{{ site.baseurl }}/about/#handling-authors-names'>"
    "simplicity</a>, the authors are sorted using the last word of their name.<br />"
    "For example, <i>Arjan van der Schaft</i> appears under the letter "
    "<strong>S</strong>, and <i>Yann Le Gorrec</i> under the letter "
    "<strong>G</strong>.</p>\n"
    "<p>You may want to look at <a href='{{ site.baseurl }}/assets/data/author_mappings.json'>"
    "the array managing name variations</a> (a JSON file) for verification/correction.</p>\n"
    "<hr />\n"
)


def _legacy_outputs(root: Path) -> dict[str, bytes]:
    outputs: dict[str, bytes] = {}
    for folder in ("authors", "years"):
        for path in sorted((root / folder).glob("*.md")):
            outputs[path.relative_to(root).as_posix()] = path.read_bytes()
    return outputs


def main() -> None:
    config = load_config(ROOT / "bibreview.yml")
    canonical_before = config.paths.bibliography.read_bytes()
    mappings_before = config.paths.author_mappings.read_bytes()

    canonical = read_bibliography(config.paths.bibliography)
    mapping_data = read_json(config.paths.author_mappings, dict)
    model = build_site_model(canonical, mapping_data)

    rendered = render_jekyll_index_pages(
        model,
        options=JekyllIndexRenderOptions(
            author_index_extra_html=PHRAISE_AUTHOR_INDEX_EXTRA_HTML,
        ),
    )
    actual = {artifact.path: artifact.content.encode("utf-8") for artifact in rendered}

    with tempfile.TemporaryDirectory() as tmp:
        legacy_root = Path(tmp)
        (legacy_root / "assets/data").mkdir(parents=True)
        (legacy_root / "authors").mkdir()
        (legacy_root / "years").mkdir()
        shutil.copy2(DOCS / "assets/data/biblio.json", legacy_root / "assets/data/biblio.json")
        shutil.copy2(
            DOCS / "assets/data/author_mappings.json",
            legacy_root / "assets/data/author_mappings.json",
        )
        generate_pages(legacy_root, dry_run=False)
        expected = _legacy_outputs(legacy_root)

    assert set(actual) == set(expected), (
        f"artifact path mismatch: only BibReview={sorted(set(actual) - set(expected))[:5]}, "
        f"only legacy={sorted(set(expected) - set(actual))[:5]}"
    )
    mismatches = [
        path for path in sorted(expected)
        if actual[path] != expected[path]
    ]
    if mismatches:
        first = mismatches[0]
        raise AssertionError(
            f"{len(mismatches)} rendered artifact(s) differ; first mismatch: {first}"
        )

    assert config.paths.bibliography.read_bytes() == canonical_before
    assert config.paths.author_mappings.read_bytes() == mappings_before

    author_pages = sum(
        1 for path in actual if path.startswith("authors/") and path != "authors/index.md"
    )
    year_pages = sum(
        1 for path in actual if path.startswith("years/") and path != "years/index.md"
    )
    print("PHRAISE Jekyll author/year rendering equivalence: byte-exact")
    print(f"  rendered artifacts: {len(actual)}")
    print(f"  author pages: {author_pages}")
    print(f"  year pages: {year_pages}")
    print("  author index: exact with PHRAISE editorial HTML supplied as project option")
    print("  year index: exact")
    print("  canonical bibliography unchanged: yes")
    print("  author mappings unchanged: yes")
    print("  filesystem persistence remains outside BibReview renderer")


if __name__ == "__main__":
    main()
