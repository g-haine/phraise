# BibReview M4 — pure Jekyll publication renderer

This increment validates publication-post rendering extracted from PHRAISE.

## Boundary

BibReview now owns the pure transformation:

```text
SiteModel + BibTeX-by-UUID + category policy
                    ↓
      render_jekyll_publication_posts()
                    ↓
        RenderedArtifact(path, content)
```

The renderer performs no filesystem or network access. PHRAISE still owns:

- where BibTeX files live and how missing BibTeX is acquired;
- project category policy;
- persistence and cleanup of generated files;
- orphan BibTeX archival and last-update metadata;
- Jekyll build/deployment, templates, CSS, branding and editorial content.

## Regression contract

The migration CI renders all publication posts twice:

1. legacy `phraise_tools.generate.render_post()`;
2. BibReview `render_jekyll_publication_posts()`.

Both paths use the same tracked BibTeX input. The complete artifact path set and every
UTF-8 byte must match. The authoritative bibliography and author mappings must remain
unchanged.

PHRAISE-specific compatibility policy remains explicit in the integration layer,
including proceedings event overrides and the historical `book-chapter` ISBN branch.
