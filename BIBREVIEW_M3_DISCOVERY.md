# BibReview M3 discovery/relevance integration

This step integrates BibReview's canonical discovery workflow into the PHRAISE migration branch without yet removing the historical `looking4Update.py` script.

## PHRAISE policy now expressed in `bibreview.yml`

The migration configuration explicitly preserves the historical PHRAISE discovery policy:

- provider: OpenAlex;
- query: `port-Hamiltonian`;
- maximum pages: 20;
- accepted CrossRef types: `journal-article`, `proceedings-article`, `book-chapter`, `book`, and `monograph`;
- excluded DOI substrings: `arxiv` and `zenodo`;
- relevance patterns: the four historical regular expressions already present in the migration configuration;
- unmatched supported works: manual review;
- optional OpenAlex key: `OPENALEX_API_KEY` through BibReview runtime composition.

## Canonical workflow boundary

`bibreview discover` owns only new-publication discovery and relevance classification:

```text
OpenAlex
   ↓
CrossRef + discovery enrichment
   ↓
configured relevance policy
   ↓
pending / review / rejected DOI queues
```

It does not mutate `bibliography.json`.

The historical second half of `looking4Update.py` — detecting incomplete existing journal records or changed/missing BibTeX and archiving them for recollection — is deliberately not part of discovery. That behavior belongs to a separate future refresh/recollect workflow.

## Integration validation

`.github/scripts/compare_bibreview_discovery.py` runs the historical and BibReview discovery paths on the same deterministic fixture. It covers:

- known and rejected DOI skipping;
- arXiv/Zenodo exclusions;
- relevance detected in title, abstract, and keywords;
- Unicode dash normalization;
- unsupported CrossRef types;
- missing CrossRef records;
- manual-review classification;
- OpenAlex duplicate DOI candidates;
- preservation of pre-existing queue entries;
- byte-level immutability of the canonical bibliography during BibReview discovery.

The fixture contains one complete known journal record. This keeps the historical refresh/recollect and missing-known-record maintenance logic as a no-op while still exercising known-DOI skipping. The final `pending`, `rejected`, and `review` queues must match between the historical and BibReview discovery paths.

## Status after this integration

Once this integration is merged and green, the discovery/relevance half of `looking4Update.py` is functionally owned by BibReview. The script itself remains transitional until the separate refresh/recollect behavior has also been extracted.
