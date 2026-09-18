"""PHRAISE-specific adapter for BibReview static-site rendering and persistence.

BibReview owns the generic site model, Jekyll renderers, and safe persistence
mechanism.  This module supplies only PHRAISE presentation policy and the
temporary compatibility conversion from PHRAISE's legacy bibliography records.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path

from bibreview.compat import legacy_record_to_publication
from bibreview.site import (
    JekyllIndexRenderOptions,
    JekyllPublicationRenderOptions,
    RenderedArtifact,
    SitePersistencePlan,
    apply_rendered_artifacts,
    build_site_model,
    plan_rendered_artifacts,
    render_jekyll_index_pages,
    render_jekyll_publication_posts,
)


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

PHRAISE_INDEX_OPTIONS = JekyllIndexRenderOptions(
    author_index_extra_html=PHRAISE_AUTHOR_INDEX_EXTRA_HTML,
    include_authorless_year_publications=False,
)

PHRAISE_PUBLICATION_OPTIONS = JekyllPublicationRenderOptions(
    category_by_type={
        "journal-article": "articles",
        "proceedings-article": "proceedings",
        "book-chapter": "chapters",
        "book": "books",
        "monograph": "books",
    },
    event_category_rules=(
        (
            r"Conference|Workshop|Symposium|Congress|Proceeding|Consortium",
            "proceedings",
        ),
    ),
    # Historical PHRAISE render_post() used re.search("book|monograph", type),
    # which also classified book-chapter citations through the ISBN branch.
    isbn_types=("book", "book-chapter", "monograph"),
)


def _site_model(records: Iterable[Mapping[str, object]], author_mappings):
    """Build BibReview site data from PHRAISE's temporary legacy projection."""
    publications = tuple(
        legacy_record_to_publication(record).publication
        for record in records
    )
    return build_site_model(publications, author_mappings)


def render_publication_artifacts(
    records: Iterable[Mapping[str, object]],
    author_mappings,
    bibtex_by_permalink: Mapping[str, str],
) -> tuple[RenderedArtifact, ...]:
    """Render all PHRAISE publication posts through BibReview."""
    model = _site_model(records, author_mappings)
    bibtex_by_id: dict[str, str] = {}
    for publication in model.publications:
        try:
            bibtex_by_id[publication.id] = bibtex_by_permalink[publication.permalink]
        except KeyError as error:
            raise ValueError(
                f"Missing BibTeX for publication permalink {publication.permalink!r}"
            ) from error
    return render_jekyll_publication_posts(
        model,
        bibtex_by_id,
        options=PHRAISE_PUBLICATION_OPTIONS,
    )


def render_index_artifacts(
    records: Iterable[Mapping[str, object]],
    author_mappings,
) -> tuple[RenderedArtifact, ...]:
    """Render all PHRAISE author/year pages through BibReview."""
    model = _site_model(records, author_mappings)
    return render_jekyll_index_pages(model, options=PHRAISE_INDEX_OPTIONS)


def persist_artifacts(
    root: Path,
    artifacts: Iterable[RenderedArtifact],
    *,
    managed_roots: tuple[str, ...],
    dry_run: bool,
) -> SitePersistencePlan:
    """Plan and, unless dry-running, apply BibReview-managed site artifacts."""
    plan = plan_rendered_artifacts(
        root,
        artifacts,
        managed_roots=managed_roots,
    )
    if not dry_run:
        apply_rendered_artifacts(plan)
    return plan
