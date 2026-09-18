# BibReview M4 — pure Jekyll index renderer

This increment validates the first rendering layer extracted from PHRAISE.

## Boundary

BibReview now owns the pure transformation:

```text
SiteModel
   ↓
render_jekyll_index_pages()
   ↓
RenderedArtifact(path, content)
```

The renderer performs no filesystem access. PHRAISE still owns persistence, tracked
generated files, Jekyll build/deployment, CSS/templates, branding, and project-specific
editorial prose.

The PHRAISE author-index explanatory paragraphs are passed explicitly through
`JekyllIndexRenderOptions.author_index_extra_html`. They are not embedded in
BibReview.

## Regression contract

The migration CI renders all author/year pages twice:

1. legacy `phraise_tools.generate.generate_pages()` into a temporary directory;
2. BibReview `render_jekyll_index_pages()` in memory from the canonical bibliography.

The complete artifact path set and every UTF-8 byte must match. The authoritative
bibliography and author mappings must remain unchanged.

Publication-post rendering is intentionally deferred to the next M4 increment.
