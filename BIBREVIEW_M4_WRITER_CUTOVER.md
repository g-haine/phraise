# BibReview M4 — PHRAISE site-writer cutover

This increment makes BibReview the effective writer for PHRAISE's generated
Jekyll publication, author and year artifacts.

## Ownership boundary

The runtime path is now:

```text
canonical bibliography.json + reviewed author mappings
                         ↓
             phraise_tools.site adapter
                         ↓
                    SiteModel
                         ↓
               pure Jekyll renderers
                         ↓
                RenderedArtifact[]
                         ↓
             plan_rendered_artifacts()
                         ↓
                SitePersistencePlan
                         ↓
             apply_rendered_artifacts()
                         ↓
        _posts / authors / years generated files
```

BibReview therefore owns:

- the renderer-independent site model;
- publication-post rendering;
- author/year rendering;
- reconciliation of expected and existing generated files;
- writes and deletion of obsolete files below the declared generated roots.

PHRAISE still owns:

- the project-specific Jekyll presentation options supplied by
  `phraise_tools.site`;
- acquisition and storage of missing BibTeX;
- archival of orphan BibTeX files;
- `_data/library.yml` last-update metadata;
- Jekyll templates, CSS, includes, build and deployment;
- the remaining temporary legacy maintenance/oracle paths outside the effective
  site writer.

## Regression oracle

The cutover does not immediately delete the historical renderers.

- `render_post()` remains the publication-post oracle.
- The former author/year generator is retained as
  `generate_pages_legacy()` for migration validation only.

CI still renders the complete real PHRAISE site through both the historical and
BibReview paths and requires byte-for-byte equivalence before exercising the
new writer.

## Writer validation

The migration workflow additionally executes the public PHRAISE generation
functions on a temporary copy of the real `docs/` tree. The effective writer
reads `assets/data/bibliography.json` directly; `biblio.json` is not an input
to `generate_posts()` or `generate_pages()`.

- all 2,349 publication posts must remain byte-identical;
- all 2,692 author/year artifacts must remain byte-identical;
- obsolete probes below `_posts`, `authors` and `years` must be removed;
- no network BibTeX fallback may be required for the tracked current site;
- an intentionally invalid `biblio.json` must not affect generation;
- a manual file outside the managed roots must remain untouched.

The ordinary PHRAISE maintenance unit tests are also run in the migration CI.

## Deliberately deferred

The site writer no longer depends on the legacy bibliography projection.
`biblio.json` still exists because author-mapping migration helpers and the
historical regression oracles consume it. The remaining maintenance workflow
(`looking4Update.py`, `getData.py`, `concatenate.py`) is also still legacy.
Those dependencies must be removed before `biblio.json`,
`projectLegacyBibliography.py`, and the compatibility bridge can be deleted.
