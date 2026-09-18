# BibReview M4 — PHRAISE site-writer cutover

This increment makes BibReview the effective writer for PHRAISE's generated
Jekyll publication, author and year artifacts.

## Ownership boundary

The runtime path is now:

```text
PHRAISE legacy projection + reviewed author mappings
                         ↓
             phraise_tools.site adapter
                         ↓
                BibReview Publication
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
- the temporary legacy bibliography projection used by the current maintenance
  commands.

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
functions on a temporary copy of the real `docs/` tree:

- all 2,349 publication posts must remain byte-identical;
- all 2,692 author/year artifacts must remain byte-identical;
- obsolete probes below `_posts`, `authors` and `years` must be removed;
- no network BibTeX fallback may be required for the tracked current site;
- a manual file outside the managed roots must remain untouched.

The ordinary PHRAISE maintenance unit tests are also run in the migration CI.

## Deliberately deferred

This step changes site rendering and persistence ownership only. It does not yet
remove the legacy bibliography projection or move the remaining maintenance
workflow (`looking4Update.py`, `getData.py`, `concatenate.py`) onto the
BibReview CLI/project API. Those are subsequent migration steps.
