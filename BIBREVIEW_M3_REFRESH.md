# BibReview M3 refresh/recollect integration

This step integrates BibReview's canonical refresh workflow into the PHRAISE migration branch and completes extraction of the maintenance half of the historical `looking4Update.py` behavior.

## PHRAISE refresh policy

`bibreview.yml` now states the historical PHRAISE eligibility rule explicitly:

- publication type: `journal-article`;
- refresh check when at least one of `volume`, `issue`, or `pages` is empty.

For eligible DOI-backed publications, BibReview compares the stored BibTeX file with the current DOI BibTeX. Missing or changed BibTeX makes the publication a refresh candidate.

## Intentional architectural improvement

Historical PHRAISE removed stale records from `biblio.json`, removed their DOI values from `DOI.txt`, archived the old records, and queued them in `newDOI.txt` so `getData.py` could recollect them later.

BibReview does not delete canonical state before recollection. Instead:

```text
existing incomplete publication
        ↓
BibTeX missing or changed
        ↓
bibreview refresh
        ↓
collected.json staging
        ↓
bibreview merge
        ↓
updated publication, original UUID retained
```

The authoritative publication remains present until merge succeeds. This removes the temporary hole in the bibliography and uses the persistent identity model as intended.

Changed stored BibTeX is backed up before replacement. Missing BibTeX is created directly. If refreshed CrossRef metadata is unavailable, the canonical publication and its stored BibTeX remain untouched so a later refresh can retry.

## Known-state consistency

The historical workflow also detected DOI values present in `DOI.txt` but absent from the bibliography. BibReview preserves this behavior as a state-consistency repair: such DOI values are removed from `known` and appended to `pending` for the normal collection workflow.

## Integration validation

`.github/scripts/compare_bibreview_refresh.py` uses deterministic historical and canonical fixtures to verify:

- identical stale-record triggers for missing and changed BibTeX;
- unchanged incomplete records do not refresh;
- complete journal records and non-journal records are ignored by the PHRAISE policy;
- orphaned known DOI values are recovered;
- canonical bibliography bytes remain unchanged during refresh planning/application;
- changed BibTeX is archived and replaced;
- recollected publications are staged rather than deleting authoritative records;
- the subsequent exact-DOI merge updates metadata while retaining the original persistent UUID.

The historical delete-before-recollect intermediate state is intentionally not reproduced.

## Status after this integration

Once this integration and its BibReview dependency are merged and green, both responsibilities of `looking4Update.py` are owned by BibReview:

1. new-publication discovery/relevance → `bibreview discover`;
2. stale existing-publication maintenance → `bibreview refresh`.

At that point `looking4Update.py` is fully legacy on `bibreview-migration`.
