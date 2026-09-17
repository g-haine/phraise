# M1 — Decisions summary

This short companion file records the decisions that must survive into M2. The detailed audit remains in `BIBREVIEW_M1_EXTRACTION_MAP.md`.

## Core decisions

1. **BibReview is the generic engine; PHRAISE is a configured consumer and demonstrator.**
2. **BibReview must not contain PHRAISE-specific scientific keywords, branding, repository identity or contact details.**
3. **The reusable website is a distinct BibReview site/template layer, not part of the pure bibliographic engine.**
4. **PHRAISE bibliography data, DOI queues, author mappings, branding and editorial pages remain PHRAISE-owned.**
5. **Generated posts, author/year pages and BibTeX files remain instance outputs, not BibReview package data.**
6. **The current DOI must stop being the internal publication identity before no-DOI publications are implemented.**
7. **`generate.py` must be split between bibliographic transformations and site rendering rather than migrated wholesale.**
8. **Scientific discovery/relevance policy must be supplied by project configuration.**
9. **Current command scripts become a coherent BibReview CLI; their historical filenames are not public compatibility constraints.**
10. **The arXiv latest-results subsystem is deliberately deferred until the core configuration/provider abstractions are stable.**
11. **PHRAISE remains the end-to-end regression case throughout extraction.**
12. **M2 designs the package/configuration/model first; M3 starts code extraction only after those interfaces are fixed.**

## M2 entry condition

M2 may begin once the M1 extraction map is accepted. No further audit is required before architecture design unless the PHRAISE tree changes materially in the meantime.
