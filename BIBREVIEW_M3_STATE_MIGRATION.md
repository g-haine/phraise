# BibReview M3 — PHRAISE canonical state migration

## Purpose

PHRAISE still stores its checked-in bibliography in the historical `docs/assets/data/biblio.json` schema, while BibReview's `merge` command now operates on the canonical persisted `Publication` schema with stable internal UUIDs.

The migration must therefore be explicit and reviewable. It must not overwrite the current site-facing file before the remaining PHRAISE rendering scripts have been migrated.

## Proposed staged-state transition

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

The migration is not expected to preserve arbitrary legacy serialization artifacts forever, but no information-bearing difference may be silently introduced.

The first real-data audit exposed two genuine canonical-model gaps that had been hidden by the legacy compatibility envelope:

- 141 legacy ISBN values were not promoted into canonical publication identifiers;
- a small set of source records use literal author names (`name`) rather than `given` / `family`, and those names were being discarded canonically.

BibReview was corrected before the PHRAISE state migration: ISBN is now retained in `Publication.identifiers["isbn"]`, and `Author.literal` represents source-provided literal author names. After these corrections, canonical persistence and reprojection introduce **no ISBN loss and no author loss**.

The only remaining differences are in legacy reference DOI spelling:

- **17,354** reference DOI values differ only by canonical DOI normalization (principally case) and resolve to exactly the same normalized DOI;
- exactly **two** legacy reference DOI strings contain illegal embedded whitespace and therefore are deliberately not promoted as canonical DOI identifiers:
  - publication `10.1080/01495739.2021.1917322`, reference `10.1016/j.geomphys. 2021.104201`;
  - publication `10.1109/tpel.2020.3041653`, reference `10.1007/978-1- 4471-0549-7`.

Those two malformed values project as `null` once the compatibility envelope is removed. This is an explicit cleanup of invalid legacy identifier strings, not a silent loss of valid bibliographic information.

The migration audit locks the complete reviewed surface: 2,349 publications and UUIDs are preserved, exactly 17,356 reference DOI leaf values differ, exactly 17,354 are normalization-equivalent, and only the two malformed strings listed above may be omitted. Any additional changed field, DOI semantic change, malformed value, or count change fails the integration workflow.

## Cutover rule

`concatenate.py` remains the authoritative production path until the canonical file is committed, `bibreview.yml` points to it, the legacy projection is generated deterministically, and the full PHRAISE integration workflow remains green.

After that cutover, `bibreview merge` becomes authoritative for bibliography state and `concatenate.py` can move to legacy/removal cleanup.
