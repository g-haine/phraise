# M2 — Decisions summary

This companion file records the architecture decisions that M3 must implement. The full rationale is in `BIBREVIEW_M2_ARCHITECTURE.md`.

## Package and scope

1. BibReview is a Python 3.12+ package using `pyproject.toml` and a `src/bibreview/` layout.
2. The command-line interface is exposed as `bibreview` and initially uses the standard-library `argparse` module.
3. Runtime dependencies stay minimal; no framework, ORM, database, dynamic plugin system or template framework is introduced merely for extraction.
4. The Python bibliographic engine remains usable without Ruby/Jekyll.
5. The reusable Jekyll site is an isolated `bibreview.site` layer.
6. BibReview starts under GNU GPL v3, compatible with the PHRAISE code being extracted (`GPL-3.0-only` unless an explicit future relicensing decision changes that).

## Data model and identity

7. Every publication has a persistent opaque internal `id` independent of DOI.
8. New IDs use Python UUIDs; the initial PHRAISE migration may deterministically assign UUIDv5 IDs from normalized existing DOIs so migration output is reproducible.
9. Once assigned, a publication ID does not change when DOI or metadata changes.
10. DOI is an optional external identifier stored separately under `identifiers`.
11. References and publications without DOI are valid model objects.
12. Exact DOI/strong-identifier matches may establish duplicates; fuzzy title/author matching may only suggest review initially, never silently merge records.
13. JSON remains the canonical persisted bibliography format for the first extraction; a compatibility adapter preserves PHRAISE's current schema while the internal model becomes cleaner.

## Configuration

14. Each project owns a versioned `bibreview.yml` beginning with `schema_version: 1`.
15. Configuration sections are `project`, `paths`, `discovery`, `relevance`, `providers`, and `site`.
16. Paths are resolved relative to the configuration file and are never reconstructed from PHRAISE-specific assumptions inside engine modules.
17. PHRAISE keeps its existing `docs/...` paths during M3 to avoid combining extraction with a data-tree migration.
18. Provider queries and scientific relevance rules are project configuration.
19. Secrets remain in environment variables/local `.env`; they are never stored in `bibreview.yml`.
20. `project.slug` provides the reusable namespace for caches and site-side identifiers that are currently hard-coded as PHRAISE.

## CLI and workflow

21. Initial commands are `discover`, `collect`, `authors`, `merge`, `render`, `validate`, and `status`.
22. `--config`, verbosity, quiet mode and dry-run semantics are common CLI concerns.
23. `status` is read-only and exposes pending human actions instead of hiding workflow state.
24. There is deliberately no monolithic `update` command in the first interface because scientific relevance and ambiguous author identity are genuine human-review boundaries.
25. `render` generates site source outputs but does not invoke Ruby/Jekyll in the core extraction milestone.

## Providers and site

26. Built-in provider adapters live under `bibreview.providers`; a dynamic plugin architecture is deferred.
27. Shared HTTP retry, timeout and sanitized diagnostics live in a common provider transport module.
28. Providers receive query/contact/project information from configuration and contain no PHRAISE literals.
29. `bibreview.site` separates deterministic bibliography-to-view transformations from static reusable Jekyll template assets.
30. PHRAISE homepage/about prose, logos, analytics identities and institutional branding remain PHRAISE-owned.
31. The independent latest-arXiv subsystem remains in PHRAISE until the core BibReview configuration/provider/site abstractions are stable.

## M3 order

32. M3 creates the separate BibReview repository/package before extracting code.
33. Extract configuration and model/identity first, then shared storage/text/reporting, HTTP/CrossRef, collection, remaining providers, merge, author mapping and discovery.
34. Site extraction begins only after the bibliographic engine reproduces PHRAISE behaviour.
35. PHRAISE remains the end-to-end regression consumer throughout the extraction.
