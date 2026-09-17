# BibReview M3 — PHRAISE canonical state migration

## Status

The real-data audit is complete and the canonical-state cutover is now materialized on the BibReview migration branch.

During the remaining M3/M4 migration window:

- `docs/assets/data/bibliography.json` is the **authoritative canonical BibReview state**;
- `docs/assets/data/collected.json` is the canonical staging batch consumed by `bibreview merge`;
- `docs/assets/data/biblio.json` is a **temporary deterministic legacy projection** for the current PHRAISE/Jekyll tooling.

`bibreview.yml` points to `bibliography.json`. The legacy projection must not be edited independently: regenerate it from canonical state with

```bash
python docs/projectLegacyBibliography.py
```

or verify it without writing with

```bash
python docs/projectLegacyBibliography.py --check
```

Once the site-generation layer is extracted to BibReview and no PHRAISE script consumes the legacy schema, `biblio.json`, the projection script, and the temporary compatibility bridge can be removed.

## One-shot migration result

The checked-in historical `biblio.json` was converted to canonical `Publication` objects using the reviewed PHRAISE compatibility bridge. The cutover preserves all 2,349 publications and assigns one stable BibReview UUID to each publication.

The first audit exposed two genuine canonical-model gaps before cutover:

- 141 legacy ISBN values were not promoted into canonical publication identifiers;
- a small set of source records use literal author names (`name`) rather than `given` / `family`.

BibReview was corrected before cutover: ISBN is retained in `Publication.identifiers["isbn"]`, and `Author.literal` represents source-provided literal author names. Canonical persistence therefore introduces no ISBN or author loss.

The audit also found two malformed reference DOI strings containing one embedded whitespace. Both repairs are unambiguous and are applied explicitly on the PHRAISE side before canonicalisation:

- publication `10.1080/01495739.2021.1917322`:
  - `10.1016/j.geomphys. 2021.104201`
  - becomes `10.1016/j.geomphys.2021.104201`;
- publication `10.1109/tpel.2020.3041653`:
  - `10.1007/978-1- 4471-0549-7`
  - becomes `10.1007/978-1-4471-0549-7`.

This repair remains project-local. `bibreview.identity.normalize_doi()` deliberately stays strict and must not guess repairs for arbitrary DOI strings containing embedded whitespace.

After those two corrections, the remaining 17,354 reference DOI changes are semantics-preserving canonical normalization, principally case. No reference DOI is lost.

## Cutover invariants

The integration workflow now verifies that:

- the canonical bibliography contains exactly 2,349 publications;
- all 2,349 internal UUIDs and publication DOI values are unique;
- `collected.json` is empty immediately after cutover;
- the two reviewed DOI repairs are present canonically and in the legacy projection;
- no canonical reference DOI contains whitespace;
- `biblio.json` is byte-for-byte the deterministic projection of `bibliography.json`;
- `bibreview --dry-run merge` is a no-op on the empty staging state;
- the historical collection/merge comparison fixtures remain green;
- the PHRAISE Jekyll site still builds successfully.

## Operational boundary during the rest of M3

`bibreview merge` is now the authoritative merge mechanism for canonical bibliography state. `concatenate.py` is therefore legacy on the migration branch and can be removed once the remaining staging/collection path no longer depends on the historical workflow.

`getData.py` is **not yet replaced operationally**: the next M3 step must make collection write canonical `collected.json` instead of using the old temporary-`biblio.json` convention. Until that step is complete, do not run the historical end-to-end update sequence on `bibreview-migration`.

The production `main` branch remains unaffected until the broader BibReview migration is ready to land.
