# BibReview M3 — PHRAISE canonical collection cutover

This increment removes the last effective collection write to the temporary
legacy bibliography projection.

## Effective path

For DOI values already queued in `docs/newDOI.txt`, PHRAISE now uses:

```text
newDOI.txt
    ↓
getData.py
    ↓
phraise_tools.canonical
    ↓
BibReview plan_project_collection()
    ↓
collected.json
    ↓
bibreview merge
    ↓
bibliography.json + DOI state
    ↓
bibreview authors
    ↓
canonical site writer
```

`getData.py` keeps PHRAISE's current HTTP adapters and command-line reporting,
but bibliography state transitions are owned by BibReview.

## Adapter boundary

`phraise_tools.canonical` adapts the existing PHRAISE client to BibReview's
generic provider contracts:

- CrossRef work lookup → BibReview work provider;
- publisher enrichment → BibReview `Enrichment`;
- Semantic Scholar / Mendeley fallback → abstract fallback;
- citation lookup → canonical reference citation;
- BibTeX lookup → canonical collected item.

The adapter also rebinds `bibreview.yml` paths to `--root` for isolated tests
and local copies.

## State semantics

Collection is now deliberately two-phase:

1. `getData.py` writes collected publications to
   `assets/data/collected.json`; it does **not** mutate
   `assets/data/bibliography.json`.
2. `bibreview merge` accepts/rejects the staging batch, updates canonical
   bibliography state, promotes accepted DOIs to `DOI.txt`, updates pending /
   review queues, creates a canonical bibliography backup, and clears staging.

A non-empty `collected.json` blocks a second collection run until the previous
batch is merged or otherwise resolved.

## Legacy status

The historical PHRAISE `phraise_tools.collect.collect()` implementation is
retained only as a regression oracle. `concatenate.py` is likewise no longer an
effective merge step on `bibreview-migration`.

`biblio.json` is not modified by canonical collection or canonical merge.
It remains only for migration helpers and historical regression comparisons.

## Validation

CI covers both the generic BibReview project API and the PHRAISE adapter.

On a temporary copy of the real PHRAISE state it verifies:

- canonical bibliography starts with 2,349 publications;
- collection planning leaves `bibliography.json` unchanged;
- one synthetic publication is staged canonically;
- DOI normalization and duplicate filtering are preserved;
- an unavailable DOI remains pending;
- BibTeX slug collisions are resolved deterministically;
- merge produces exactly 2,350 canonical publications;
- the staged publication UUID survives the merge;
- staging is cleared after merge;
- the accepted DOI is promoted to known state;
- `biblio.json` remains byte-identical throughout.

## Subsequent M3 update cutover

Discovery and refresh have now also moved to BibReview. The effective
maintenance cycle is documented in `BIBREVIEW_M3_UPDATE_CUTOVER.md`; the
historical PHRAISE update engine remains only as a non-regression oracle.
