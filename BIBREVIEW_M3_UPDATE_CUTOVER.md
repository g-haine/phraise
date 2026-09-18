# BibReview M3 — PHRAISE canonical discovery/refresh cutover

This increment removes the historical `looking4Update.py` entry point from the
effective PHRAISE maintenance workflow.

## Effective maintenance cycle

The update path is now deliberately split into explicit canonical stages:

```text
bibreview discover
      ↓
newDOI / checkDOI / badDOI queues
      ↓
human review of checkDOI
      ↓
bibreview refresh
      ↓
collected.json (refreshed existing publications, if any)
      ↓
bibreview merge
      ↓
bibliography.json
      ↓
getData.py newDOI.txt
      ↓
collected.json (new/recovered publications)
      ↓
bibreview merge
      ↓
bibliography.json
      ↓
bibreview authors
      ↓
canonical site writer
```

Two merge points are intentional. Refresh and collection both use the same
canonical `collected.json` staging area and both refuse to overwrite a
non-empty batch.

## Discovery ownership

`bibreview discover` now owns:

- OpenAlex candidate discovery;
- CrossRef work verification;
- accepted-type filtering;
- project-configured DOI exclusions;
- project-configured relevance matching;
- queue updates to `newDOI.txt`, `checkDOI.txt`, and `badDOI.txt`.

The OpenAlex page limit and relevance policy live in `bibreview.yml`, not in a
PHRAISE command-line wrapper.

## Refresh ownership

`bibreview refresh` now owns:

- selection of incomplete existing publication types/fields from
  `bibreview.yml`;
- stored/current BibTeX comparison;
- canonical recollection of stale publications;
- changed-BibTeX backup;
- recovery of DOI values recorded as known but absent from canonical
  bibliography.

Unlike the historical workflow, refresh does not delete an authoritative
publication before recollection. It stages the refreshed version and relies on
the normal merge to update the publication while preserving its persistent UUID.

## Runtime secrets

`bibreview.yml` declares:

```yaml
environment:
  file: docs/.env
```

BibReview therefore uses the same local provider-secret file as the earlier
PHRAISE maintenance scripts. File values are defaults; exported environment
variables take precedence. The environment-file capability is generic BibReview
runtime functionality, not a PHRAISE special case.

## Legacy status

The executable `docs/looking4Update.py` file is removed.

`phraise_tools.update.find_updates()` remains temporarily because migration CI
still compares historical discovery/refresh behavior against BibReview. It is a
test oracle only and must not be used as project state machinery.

## Validation

CI retains the focused historical-vs-BibReview comparisons and adds an
integrated canonical update validation. The integrated fixture starts from all
2,349 canonical PHRAISE publications, keeps their real persistent identities,
and verifies:

- discovery updates only DOI queue state;
- known and configured-excluded DOI values are skipped;
- relevant, manual-review, and rejected classifications follow `bibreview.yml`;
- exactly one controlled stale existing publication is staged by refresh;
- canonical bibliography is unchanged before the refresh merge;
- changed BibTeX is backed up;
- refresh merge preserves the existing publication UUID;
- the discovered DOI is then collected only after refresh staging has been
  cleared;
- the new publication UUID survives its collection merge;
- the final canonical count is 2,350;
- manual-review and rejected queue state remain correct;
- legacy `biblio.json` remains byte-identical throughout.

## Remaining migration work

After this cutover, the effective maintenance path no longer depends on the
legacy discovery, merge, author, or site-writing entry points.

The remaining cleanup work is primarily removal of migration scaffolding and
oracles once their non-regression value is no longer needed: the deterministic
legacy projection, compatibility bridge, historical collector/update/merge/
author renderers, and their comparison scripts.
