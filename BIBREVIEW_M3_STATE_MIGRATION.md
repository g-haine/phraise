# BibReview M3 — PHRAISE canonical state migration

## Purpose

PHRAISE still stores its checked-in bibliography in the historical `docs/assets/data/biblio.json` schema, while BibReview's `merge` command now operates on the canonical persisted `Publication` schema with stable internal UUIDs.

The migration must therefore be explicit and reviewable. It must not overwrite the current site-facing file before the remaining PHRAISE rendering scripts have been migrated.

## Proposed two-file transition

During the remaining M3/M4 migration window:

- `docs/assets/data/bibliography.json` becomes the **authoritative canonical BibReview state**;
- `docs/assets/data/collected.json` is the canonical staging batch consumed by `bibreview merge`;
- `docs/assets/data/biblio.json` remains a **temporary legacy compatibility projection** for the current PHRAISE/Jekyll tooling.

Once the site-generation layer is extracted to BibReview and no PHRAISE script consumes the legacy schema, `biblio.json` and the compatibility projection can be removed.

## One-shot migration algorithm

1. Read the current `docs/assets/data/biblio.json` with BibReview's legacy compatibility loader.
2. Convert all publications to canonical `Publication` objects.
3. Persist them to a new canonical `bibliography.json` using BibReview storage.
4. Read the canonical file back and verify exact canonical round-trip.
5. Verify publication count, normalized DOI uniqueness, and UUID uniqueness.
6. Project the reloaded canonical publications back to the current PHRAISE record shape and audit every difference against the legacy source.
7. Only after this audit is accepted, repoint `bibreview.yml: paths.bibliography` to `docs/assets/data/bibliography.json` and initialize `collected.json` as an empty canonical list.

## Compatibility boundary

The migration is not expected to preserve arbitrary legacy serialization artifacts forever. However, no information-bearing difference may be silently introduced.

The compatibility work has already identified two historical irregularities that cannot be represented exactly by the strict canonical model:

- one reference contains a malformed DOI with embedded whitespace; the raw malformed value is kept only by the legacy compatibility envelope and is intentionally not promoted as a canonical DOI;
- one publication contains an empty author object; the empty entry is retained by the legacy compatibility envelope but intentionally omitted from the canonical `Author` tuple.

The migration audit must fail if any additional publication or field differs after canonical persistence and projection.

## Cutover rule

`concatenate.py` remains the authoritative production path until the canonical file is committed, `bibreview.yml` points to it, the legacy projection is generated deterministically, and the full PHRAISE integration workflow remains green.

After that cutover, `bibreview merge` becomes authoritative for bibliography state and `concatenate.py` can move to legacy/removal cleanup.
