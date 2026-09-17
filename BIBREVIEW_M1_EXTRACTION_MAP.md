# M1 — PHRAISE to BibReview extraction map

This document classifies the current PHRAISE repository before any code is moved into **BibReview**.

M1 is an audit and boundary-definition milestone. It deliberately changes no runtime behaviour. Its purpose is to decide what will become reusable BibReview code, what will remain PHRAISE project data/configuration, what belongs to a reusable site template, and what is generated output or project infrastructure.

## Reference

- PHRAISE repository: `g-haine/phraise`
- M0 frozen functional baseline: `8c0682301016ac14156c63569ee6f1b5a2169421`
- Frozen comparison branch: `baseline/pre-bibreview-extraction`
- M1 audit starts from `main` after the M0 documentation merge.

The M0 branch remains immutable. All later migration work must continue to be comparable with it.

## Target boundary

The final relationship should be:

```text
BibReview
├── bibliographic engine
├── provider adapters
├── validation / normalization / identity handling
├── CLI and pipeline orchestration
└── reusable site generator/template
        ↓
PHRAISE
├── BibReview configuration
├── port-Hamiltonian discovery/relevance policy
├── bibliography and author data
├── PHRAISE editorial content and branding
├── generated site content
└── GitHub Pages deployment
```

The key rule is:

> BibReview must not know that PHRAISE exists, while PHRAISE may explicitly depend on BibReview.

A second bibliography project must be creatable by changing configuration and project content without editing BibReview source code.

## Classification legend

| Code | Meaning |
|---|---|
| **E** | Extract into the BibReview Python engine/CLI |
| **T** | Extract or refactor into BibReview's reusable site template/generator |
| **P** | Remain PHRAISE project-specific configuration, content or source data |
| **G** | Generated/cache output owned by the PHRAISE instance |
| **I** | Infrastructure: keep in PHRAISE, but optionally provide a reusable example/template from BibReview |
| **R** | Review before migration; do not copy blindly |

A file can have more than one classification when it currently mixes responsibilities. Such files must be split during later milestones rather than copied wholesale.

---

# 1. Repository root

| Current path | Class | M1 decision |
|---|---:|---|
| `README.md` | P | Remains the PHRAISE README. Later rewrite it so PHRAISE is presented as a BibReview-powered demonstrator rather than as the engine itself. |
| `LICENSE` | P | Remains PHRAISE's licence file. BibReview needs its own explicit licence decision in M2; do not infer that by copying this file automatically. |
| `.gitignore` | I | Remains project infrastructure. BibReview will need its own package-oriented ignore rules. |
| `install.sh` | E/I | Transitional environment helper. Do not copy as a permanent BibReview interface. Its dependency knowledge belongs in BibReview packaging/environment metadata; PHRAISE may later keep only a minimal consumer setup helper if useful. |
| `phraise.yml` | E/P | Most Python dependencies describe the future BibReview engine, but the environment name is PHRAISE-specific. M2 should convert this dependency set into BibReview packaging/environment metadata and leave PHRAISE with consumer-level configuration only. |
| `BIBREVIEW_M0_BASELINE.md` | P | Migration record owned by PHRAISE. Never part of the BibReview runtime package. |
| `BIBREVIEW_M1_EXTRACTION_MAP.md` | P | Migration record owned by PHRAISE. |

## Root-level conclusion

The root contains no reusable engine code that should simply be copied into BibReview. `install.sh` and `phraise.yml` are useful evidence for BibReview's dependency definition, not target architecture.

---

# 2. Python command entry points

Current command wrappers under `docs/` are thin front ends around `phraise_tools` and should become a single BibReview CLI rather than survive as six unrelated scripts.

| Current path | Class | Future responsibility |
|---|---:|---|
| `docs/looking4Update.py` | E | BibReview discovery/update command |
| `docs/getData.py` | E | BibReview collection/enrichment command |
| `docs/setAuthorMapping.py` | E | BibReview author-identity command |
| `docs/concatenate.py` | E/R | Bibliography merge operation, but its duplicated reporter/file-write machinery must be consolidated instead of copied |
| `docs/setPosts.py` | E/T | Site publication generation command |
| `docs/setPages.py` | E/T | Site author/year index generation command |

The filenames are historical interfaces, not target APIs. M2 should define commands along the lines of:

```text
bibreview discover
bibreview collect
bibreview authors
bibreview merge
bibreview build
bibreview update
bibreview validate
```

Exact naming is an M2 design decision. M1 only establishes that the command logic is reusable and should be owned by BibReview.

## Important `concatenate.py` observation

`concatenate.py` is intentionally standalone today and therefore duplicates functionality already present in `phraise_tools.common` (reporting, JSON handling and atomic file replacement). BibReview should have one implementation of those primitives.

There is also a model inconsistency worth fixing before future no-DOI support:

- `concatenate.py` accepts records whose DOI is a string or `null`;
- `phraise_tools.common.bibliography()` currently requires every record to contain a non-empty DOI string.

This must be resolved at the model-design level in M2/M3 rather than patched separately in each command.

---

# 3. `docs/phraise_tools/` — current bibliographic engine

This directory is the principal source for BibReview, but it contains several embedded PHRAISE assumptions that must be turned into configuration/policies.

## `docs/phraise_tools/__init__.py`

**Classification: E**

Rename/recreate as the BibReview package. The current PHRAISE-specific package description is not retained.

## `docs/phraise_tools/common.py`

**Classification: E, with mandatory refactor**

Reusable responsibilities:

- CLI reporting and verbosity;
- JSON/text loading;
- atomic/staged writes;
- path safety;
- slugification;
- date validation;
- metadata text cleanup;
- author-name helpers.

PHRAISE coupling to remove:

- `phraise:` in diagnostics;
- default root inferred from the PHRAISE `docs/` layout;
- fixed paths such as `assets/data/biblio.json` and `assets/data/author_mappings.json`;
- the assumption that every publication has a non-empty DOI.

Likely M2 split:

```text
bibreview.cli
bibreview.io
bibreview.model / bibliography
bibreview.text
bibreview.identities
```

The exact module names are not fixed by M1.

## `docs/phraise_tools/metadata.py`

**Classification: E/P mixed**

Generic BibReview material:

- HTTP client behaviour;
- retry/error handling;
- CrossRef adapter;
- DOI BibTeX retrieval;
- citation formatting lookup;
- Scopus/Elsevier enrichment;
- Springer enrichment;
- IEEE enrichment;
- Semantic Scholar optional abstract fallback;
- Mendeley optional abstract fallback;
- OpenAlex transport and pagination support;
- provider field extraction.

PHRAISE-specific material that must move to configuration/project policy:

- OpenAlex query `title_and_abstract.search:port-Hamiltonian`;
- `PHRAISE` in user-agent strings;
- project contact/repository identity;
- `.env` location assumptions and error text mentioning `docs/.env`;
- any provider enable/disable policy that should be project-configurable.

Target rule: a generic OpenAlex adapter receives a query; it never contains the port-Hamiltonian query itself.

## `docs/phraise_tools/collect.py`

**Classification: E, with data-layout abstraction**

Reusable responsibilities:

- DOI collection;
- CrossRef record construction;
- publisher/abstract enrichment;
- reference collection;
- BibTeX acquisition;
- deterministic slug generation;
- backup before mutation;
- dry-run behaviour.

Current coupling to remove:

- fixed paths (`DOI.txt`, `assets/data/biblio.json`, `assets/bib/`);
- DOI as the mandatory publication identity;
- direct construction of the current PHRAISE JSON schema without a formal internal model.

This is a strong candidate for the first extraction after the model/configuration design is fixed.

## `docs/phraise_tools/update.py`

**Classification: E/P mixed**

Reusable engine responsibilities:

- discovery pagination;
- candidate normalization and deduplication;
- known/rejected/pending queues;
- CrossRef verification;
- incomplete-record detection;
- recollection/archive logic;
- BibTeX-change detection;
- dry-run-safe mutations.

PHRAISE-specific policy that must remain outside the engine:

- `is_relevant()` scientific regexes for port-Hamiltonian material;
- the OpenAlex subject/query implied by the provider call;
- project-specific relevance vocabulary such as `dirac structure`, `dissipative hamiltonian`, etc.

The supported publication-type set can become a BibReview default, but it should not be entangled with the PHRAISE scientific topic.

Target rule:

```text
provider results
    ↓
generic candidate pipeline
    ↓
project-configured relevance policy
    ↓
accept / manual-check / reject
```

## `docs/phraise_tools/generate.py`

**Classification: E/T mixed**

Reusable engine-side responsibilities:

- author mapping analysis;
- safe/ambiguous identity detection;
- category derivation from publication type;
- validation before generation;
- deterministic grouping/sorting.

Reusable site-template responsibilities:

- rendering publication pages;
- rendering author pages;
- rendering year pages;
- rendering indexes;
- handling Jekyll front matter and links;
- publication-category pages.

Text that should become template/configuration rather than Python literals:

- explanatory author-index prose;
- labels and site-facing wording;
- page structure that should be editable independently of engine algorithms.

`generate.py` should therefore not migrate as one large module. M2 should separate bibliographic transformations from Jekyll/site rendering.

---

# 4. Tests

Current tests:

```text
docs/tests/test_concatenate.py
docs/tests/test_http_diagnostics.py
docs/tests/test_mendeley_auth.py
docs/tests/test_semantic_rate_limit.py
docs/tests/test_workflow.py
docs/tests/fixtures/legacy/
```

**Classification: E + P integration split**

Move to BibReview:

- unit tests for generic merge logic;
- HTTP diagnostics and error sanitization;
- provider behaviour;
- optional-provider failure behaviour;
- generic pipeline tests;
- generic renderer regression fixtures.

Keep/add in PHRAISE:

- an end-to-end consumer/integration test proving that PHRAISE configuration and data still build through BibReview;
- selected M0 output comparisons where they are useful as migration acceptance tests.

The current tests are particularly valuable because they already isolate production data and mock external services. They should travel with the code they protect rather than remain permanently in PHRAISE after extraction.

---

# 5. PHRAISE source data and state

These files are **not BibReview source code**. BibReview must understand their concepts, but the actual data belongs to PHRAISE.

| Current path | Class | Decision |
|---|---:|---|
| `docs/DOI.txt` | P | PHRAISE publication identifier state |
| `docs/newDOI.txt` | P | PHRAISE pending queue |
| `docs/badDOI.txt` | P | PHRAISE exclusion state |
| `docs/checkDOI.txt` | P | PHRAISE manual-review queue |
| `docs/assets/data/biblio.json` | P | PHRAISE canonical bibliography content |
| `docs/assets/data/author_mappings.json` | P | PHRAISE author identity decisions |
| runtime bibliography backups | P/G | Instance state; never package data inside BibReview |
| runtime `trash/` archive | P/G | Instance archive; not BibReview package content |

BibReview may eventually change the on-disk representation, but migration must preserve meaning and provide an explicit conversion path if formats change.

## Identifier warning

The current data flow uses DOI simultaneously as:

- external identifier;
- deduplication key;
- queue key;
- record identity;
- lookup key;
- citation link source.

That coupling is the main blocker for publications without DOI. M2 should design a publication identity independent of DOI before M3 extraction hardens the current schema.

---

# 6. Generated PHRAISE content

The following are outputs of the engine/site generator and should remain in the PHRAISE instance, not be packaged as BibReview source:

| Current path | Class | Decision |
|---|---:|---|
| `docs/_posts/*.md` | G | Generated publication pages |
| `docs/authors/*.md` | G | Generated author pages/index |
| `docs/years/*.md` | G | Generated year pages/index |
| `docs/assets/bib/*.bib` | G | Generated/downloaded BibTeX assets |
| `docs/_data/library.yml` | G | Generated bibliography update metadata |

During migration these files are important regression artefacts: BibReview should initially regenerate functionally equivalent content for PHRAISE.

They are not templates. The templates/rules that produce them belong to BibReview; the generated files belong to PHRAISE.

---

# 7. Jekyll site template

The current Jekyll website contains a reusable visual/navigation layer. This should become a BibReview-provided template or scaffold, while PHRAISE retains project-specific configuration and branding.

## Reusable template candidates

**Classification: T** unless noted otherwise.

```text
docs/_layouts/base.html
docs/_layouts/category.html
docs/_layouts/home.html
docs/_layouts/page.html
docs/_layouts/post.html

docs/_includes/count-posts.html
docs/_includes/head.html
docs/_includes/header.html
docs/_includes/search-box.html
docs/_includes/social.html

docs/assets/css/style.scss
docs/_sass/minima/**
docs/assets/js/copy-to-clipboard.js
docs/assets/js/scroll-to-top.js
docs/assets/js/search-worker.js
docs/assets/js/search.js

docs/categories/articles.md
docs/categories/books.md
docs/categories/chapters.md
docs/categories/proceedings.md
docs/categories/unknown.md
docs/search.md
docs/404.html
```

These files should not simply be moved unchanged. M2/M4 must parameterize project names, paths, storage keys and optional features.

### Search JavaScript

The search implementation is generic in purpose but currently exposes PHRAISE naming (`PhraiseSearch`, `phraise_biblio_cache`, `phraise_` cache prefix) and fixed paths to the current JSON database.

Therefore:

- search logic → BibReview site template;
- project/cache namespace and data URL → generated/configured values;
- DOI search/display must tolerate records without DOI once the model supports them.

## Mixed or project-specific includes

| Path | Class | Decision |
|---|---:|---|
| `docs/_includes/footer.html` | T/P | Generic footer structure is reusable; PHRAISE GoatCounter/site identifiers and project links are configuration/instance data. |
| `docs/_includes/custom-head.html` | T/P | Review and parameterize any project-specific metadata. |
| `docs/_includes/google-analytics.html` | R/T | Optional analytics integration, not part of the bibliographic core. Keep only if the future template deliberately supports it. |
| `docs/_includes/disqus_comments.html` | R/T | Optional legacy feature. Do not make it a BibReview dependency by default. |

## Jekyll configuration

`docs/_config.yml` is **P/T mixed**.

PHRAISE-specific values that remain with the project include:

- site title and description;
- author/contact details;
- URL/baseurl;
- GitHub username/repository link;
- PHRAISE logo/favicon;
- domain-specific external links;
- enabled header pages;
- analytics identities.

Reusable Jekyll defaults, plugins and template conventions can become part of the BibReview site scaffold.

Long term, BibReview's own configuration should be the authoritative project description and should generate or complement the required Jekyll configuration rather than force users to edit duplicated settings in multiple files.

---

# 8. PHRAISE editorial content and branding

These remain entirely in PHRAISE:

| Path | Class | Reason |
|---|---:|---|
| `docs/index.html` | P | PHRAISE homepage/editorial introduction |
| `docs/about.md` | P | PHRAISE scope, contribution instructions and project explanation |
| `docs/.keywords.md` | P | PHRAISE-specific site/content material |
| `docs/assets/img/logo.png` | P | PHRAISE branding |
| `docs/assets/img/logo.webp` | P | PHRAISE branding |
| `docs/assets/img/logo.xcf` | P | PHRAISE source artwork |
| `docs/assets/img/favicon.ico` | P | PHRAISE branding |
| `docs/assets/img/logo-isae.*` | P | PHRAISE institutional branding/content |
| `docs/_data/navigation.yml` | P/T | Current navigation choices are PHRAISE-specific; navigation mechanism belongs to template. |

A new BibReview project may provide its own homepage/about text and branding without modifying the BibReview package.

---

# 9. arXiv latest-publications feature

The arXiv cache is useful and reusable in concept, but it is currently a separate PHRAISE-specific subsystem.

Current files:

```text
.github/scripts/update_arxiv.py
.github/workflows/update-arxiv.yml
docs/_includes/arXiv.html
docs/arXiv.md
docs/data/arxiv.json
```

Classification:

- arXiv client/cache logic: **T/E candidate**;
- workflow: **I**;
- page/include: **T**;
- generated cache: **G**;
- current query/contact/repository identity: **P**.

Current hard-coded PHRAISE elements include:

- query `all:port AND all:Hamiltonian`;
- `PHRAISE/1.0` user agent;
- PHRAISE repository URL;
- maintainer contact email;
- output path under `docs/data/`;
- client-side function naming tied to port-Hamiltonian papers.

M1 decision: **do not extract this first**. The feature should remain operational in PHRAISE while the main bibliography engine is separated. Once BibReview's configuration and provider abstractions exist, this can be folded into a generic optional arXiv/latest-results feature.

---

# 10. GitHub/Jekyll infrastructure

| Path | Class | Decision |
|---|---:|---|
| `.github/workflows/update-arxiv.yml` | I | PHRAISE owns its schedule; BibReview may later ship an example workflow. |
| `docs/Gemfile` | I/T | Current Jekyll dependency declaration. Use as the initial site-template dependency reference; do not make Ruby part of BibReview's Python engine. |
| `docs/script/bootstrap` | R/I | Legacy/convenience Jekyll helper; review before carrying forward. |
| `docs/script/build` | R/I | Same. |
| `docs/script/cibuild` | R/I | Same. |
| `docs/script/server` | R/I | Same. |
| `docs/.gitignore` | I | PHRAISE/Jekyll build ignore rules; BibReview package gets separate ignore rules. |

The Python engine and the Jekyll implementation must remain separable. A BibReview bibliography pipeline should be testable without Ruby/Jekyll installed; site generation/build validation may add the site-specific dependency layer.

---

# 11. Proposed BibReview responsibility map

The audit suggests the following logical components for M2 design:

```text
bibreview
├── cli
├── config
├── model
├── io
├── identities
├── providers
│   ├── crossref
│   ├── openalex
│   ├── elsevier
│   ├── springer
│   ├── ieee
│   ├── semantic_scholar
│   ├── mendeley
│   └── later: arxiv
├── pipeline
│   ├── discover
│   ├── collect
│   ├── merge
│   └── validate
└── site
    ├── model / transformations
    ├── renderers
    └── template assets
```

This is a responsibility map, **not yet the final package tree**. M2 must decide the smallest human-readable architecture before files are created.

---

# 12. Configuration responsibilities discovered by M1

The following values are currently embedded in code or Jekyll configuration and must become project configuration if BibReview is to be genuinely generic:

## Project identity

- project name;
- title/description;
- repository URL;
- site URL/base path;
- maintainer/contact identity;
- logo/favicon;
- social/external links.

## Bibliographic discovery

- primary query/expression;
- provider-specific query representation;
- relevance expressions/rules;
- accepted publication types;
- exclusions/manual-review policy;
- discovery page/result limits.

## Providers

- enabled providers;
- optional enrichment/fallback providers;
- credentials through environment variables;
- contact information where APIs request it.

## Site

- enabled pages/features;
- categories/navigation;
- latest-arXiv feature on/off;
- search cache namespace;
- analytics integrations;
- theme/branding overrides.

No PHRAISE scientific keyword should remain as a constant in the BibReview package.

---

# 13. Extraction order implied by the dependency graph

M1 recommends the following extraction sequence for later milestones:

```text
1. configuration + publication model
        ↓
2. common I/O / validation / CLI primitives
        ↓
3. provider adapters
        ↓
4. collection and merge pipeline
        ↓
5. discovery/update pipeline with configurable relevance policy
        ↓
6. author identity handling
        ↓
7. site transformation/rendering
        ↓
8. Jekyll template/search assets
        ↓
9. optional arXiv latest-results feature
```

This order avoids extracting code whose interfaces still depend on PHRAISE-specific paths or DOI-only identity assumptions.

---

# 14. Main risks identified by M1

## R1 — DOI is overloaded as publication identity

This is the most important architectural risk. Publications without DOI cannot be cleanly supported until internal identity is separated from external identifiers.

**M2 action:** define the publication model and identifier strategy first.

## R2 — configuration is currently spread across Python, Jekyll and environment files

The scientific query, relevance regexes, branding, API credentials and site configuration live in different places.

**M2 action:** define one BibReview project configuration contract and clear precedence rules for environment secrets.

## R3 — site rendering and bibliographic transformation are mixed in `generate.py`

Moving `generate.py` unchanged would reproduce the current coupling.

**M2 action:** separate transformations from renderers/templates.

## R4 — paths encode the current PHRAISE/Jekyll repository layout

Engine functions know `assets/data`, `assets/bib`, `_posts`, `DOI.txt`, etc.

**M2 action:** define project paths through configuration/context objects, with sensible defaults in the BibReview project scaffold.

## R5 — duplicate utility implementations

`concatenate.py` duplicates reporting and staged-write concepts.

**M3 action:** consolidate into one tested implementation when extraction starts.

## R6 — generated files are currently versioned alongside source data

This is acceptable for PHRAISE/GitHub Pages, but source-of-truth boundaries must stay explicit.

**M2 action:** distinguish input state, canonical database, generated site files and caches in the configuration/model.

## R7 — arXiv is a second network subsystem

It uses separate HTTP machinery and project identity.

**Action:** defer its generalization until the core provider/config abstractions are stable.

## R8 — backward compatibility can become accidental complexity

The current commands and file names are useful migration references but are not contractual public APIs.

**Action:** preserve output behaviour for PHRAISE during extraction, but do not preserve obsolete internal architecture merely for compatibility.

---

# 15. What must stay unchanged during extraction

Until PHRAISE fully consumes BibReview, each significant migration step must preserve the M0 functional contract:

- deterministic Python tests remain green;
- PHRAISE's real bibliography remains readable;
- current author mappings remain valid;
- generated publication/author/year pages remain functionally equivalent;
- Jekyll builds successfully;
- dry runs remain non-mutating;
- network/provider errors remain sanitized;
- no credentials are committed;
- existing permalinks are preserved;
- the arXiv cache workflow remains operational unless deliberately migrated in a dedicated step.

---

# 16. M1 acceptance criteria

M1 is complete when all of the following are true:

- [x] The Python command wrappers are classified.
- [x] Every `phraise_tools` module has an extraction decision.
- [x] Tests are split conceptually into BibReview unit/regression tests and PHRAISE consumer tests.
- [x] PHRAISE source data is distinguished from BibReview source code.
- [x] Generated files are identified explicitly.
- [x] The reusable Jekyll/template layer is separated conceptually from PHRAISE branding/content.
- [x] The arXiv subsystem has an explicit migration decision.
- [x] Project infrastructure is distinguished from engine code.
- [x] Hard-coded PHRAISE scientific/configuration assumptions are identified.
- [x] The DOI-only identity risk is recorded before model design.
- [x] An extraction dependency order is defined.
- [x] No runtime code has been moved or behaviour changed during M1.

Once this map is accepted, **M2 — BibReview architecture and configuration design** can begin. M2 should design the package, publication model, identifier model, project configuration and CLI before the first code extraction.