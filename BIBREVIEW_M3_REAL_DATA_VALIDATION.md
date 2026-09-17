# M3 — Real PHRAISE bibliography validation

This migration-only validation exercises the real PHRAISE bibliography through the current BibReview compatibility layer.

It is intentionally read-only and runs only on pull requests targeting `bibreview-migration` (or by manual dispatch). Production `main` is not involved.

The workflow pins BibReview commit:

`45ed1a66a81229cb1aa53b7823bd8dca26243272`

The integration check verifies:

- the full `docs/assets/data/biblio.json` loads through BibReview;
- publication count is preserved;
- every generated internal UUID is unique;
- normalized DOI values are unique;
- `legacy -> BibReview -> legacy` reproduces the source records exactly;
- the bibliography file SHA-256 is unchanged;
- `git diff --exit-code` remains clean after validation.

No UUID is persisted into PHRAISE data at this stage.
