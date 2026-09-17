# BibReview M4 site transformation integration

This step starts M4 by validating a renderer-independent site model against the real PHRAISE bibliography before extracting any Markdown/Jekyll rendering.

## Boundary

BibReview now owns a pure transformation layer:

```text
canonical Publication objects + reviewed author mappings
                         ↓
                 build_site_model
                         ↓
                     SiteModel
```

`SiteModel` contains the bibliographic information required by a static scholarly site without choosing how that information is rendered. In particular, it carries:

- publication permalinks, creation dates, publication years, types and bibliographic metadata;
- source-visible author names linked to reviewed canonical author slugs;
- author-index membership;
- year-index membership;
- references with an internal permalink when their DOI is present in the same bibliography.

The transformation performs no filesystem mutation and contains no Markdown, HTML, Liquid, Jekyll, CSS, category-label, or PHRAISE-branding logic.

## PHRAISE integration audit

`.github/scripts/compare_bibreview_site_model.py` builds the BibReview site model from the authoritative `bibliography.json` and `author_mappings.json`, then compares it with the structured information currently consumed by the historical PHRAISE renderer through `biblio.json`.

The audit checks the complete real bibliography for:

- publication count and DOI set;
- permalink equivalence;
- creation-date equivalence;
- publication-year equivalence;
- publication type and title equivalence;
- source-visible author names and their author-page slugs;
- author-page membership;
- year-page membership;
- reference DOI/citation data;
- internal reference links;
- byte-level immutability of canonical bibliography and author mappings.

PHRAISE currently has one `DOI.txt` entry for every DOI-backed canonical publication. The historical renderer therefore resolves the same internal references as BibReview, while the new model no longer needs workflow queue state in order to determine whether a referenced publication exists.

## Deliberately not extracted yet

This step does **not** replace `setPosts.py`, `setPages.py`, or `phraise_tools.generate`.

The following remain PHRAISE/legacy concerns until the next M4 increments:

- publication category naming (`articles`, `proceedings`, `chapters`, `books`);
- MathJax/Liquid escaping;
- YAML front matter;
- publication Markdown;
- author/year page HTML;
- PHRAISE explanatory prose on author pages;
- BibTeX download links and orphan-file cleanup;
- Jekyll-specific output paths;
- CSS, includes, layouts, navigation and branding.

This separation is intentional: the renderer will consume `SiteModel`; it must not redefine bibliographic identity or indexing rules.
