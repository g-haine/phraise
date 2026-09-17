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

1. Read the current `docs/assets/data/biblio.json`.
2. Apply the two reviewed PHRAISE data repairs listed below on an in-memory copy. This repair is project-local and does not weaken BibReview's generic DOI validation.
3. Convert all repaired records to canonical `Publication` objects.
4. Persist them to a new canonical `bibliography.json` using BibReview storage.
5. Read the canonical file back and verify exact canonical round-trip.
6. Verify publication count, normalized DOI uniqueness, and UUID uniqueness.
7. Project the reloaded canonical publications back to the current PHRAISE record shape and audit every remaining difference against the repaired legacy source.
8. Only after this audit is accepted, repoint `bibreview.yml: paths.bibliography` to `docs/assets/data/bibliography.json` and initialize `collected.json` as an empty canonical list.

## Compatibility boundary

The migration is not expected to preserve arbitrary legacy serialization artifacts forever, but no information-bearing difference may be silently introduced.

The first real-data audit exposed two genuine canonical-model gaps that had been hidden by the legacy compatibility envelope:

- 141 legacy ISBN values were not promoted into canonical publication identifiers;
- a small set of source records use literal author names (`name`) rather than `given` / `family`, and those names were being discarded canonically.

BibReview was corrected before the PHRAISE state migration: ISBN is now retained in `Publication.identifiers["isbn"]`, and `Author.literal` represents source-provided literal author names. After these corrections, canonical persistence and reprojection introduce **no ISBN loss and no author loss**.

The audit also found two malformed reference DOI strings containing a single embedded whitespace. Both can be repaired unambiguously and are therefore corrected explicitly before canonicalisation:

- publication `10.1080/01495739.2021.1917322`:
  - `10.1016/j.geomphys. 2021.104201`
  - becomes `10.1016/j.geomphys.2021.104201`;
- publication `10.1109/tpel.2020.3041653`:
  - `10.1007/978-1- 4471-0549-7`
  - becomes `10.1007/978-1-4471-0549-7`.

This correction is deliberately implemented in the PHRAISE migration bridge rather than in `bibreview.identity.normalize_doi()`: BibReview must continue to reject arbitrary DOI values with embedded whitespace instead of guessing a repair.

After these two reviewed repairs, the only remaining differences are **17,354 reference DOI spellings** that differ solely by canonical DOI normalization, principally case. Every one resolves to the same normalized DOI before and after migration. No reference DOI is dropped.

The migration audit locks the complete reviewed surface: 2,349 publications and UUIDs are preserved, exactly the two reviewed source repairs are applied, and every remaining changed leaf is one of the 17,354 normalization-equivalent reference DOI spellings. Any additional changed field, repair, DOI semantic change, publication-count change, or UUID-count change fails the integration workflow.

## Cutover rule

`concatenate.py` remains the authoritative production path until the canonical file is committed, `bibreview.yml` points to it, the repaired legacy projection is generated deterministically, and the full PHRAISE integration workflow remains green.

At cutover, the site-facing `biblio.json` compatibility projection will contain the two corrected DOI strings as well. The audit PR itself remains read-only with respect to checked-in bibliography data.

After that cutover, `bibreview merge` becomes authoritative for bibliography state and `concatenate.py` can move to legacy/removal cleanup.
