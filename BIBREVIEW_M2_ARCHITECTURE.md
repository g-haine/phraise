# M2 — BibReview architecture and configuration design

This document fixes the architecture to be used for the first BibReview implementation. It is a design milestone: **M2 does not extract or change PHRAISE runtime code**.

M2 starts from the accepted M1 decisions recorded in `BIBREVIEW_M1_DECISIONS.md` and the detailed extraction audit in `BIBREVIEW_M1_EXTRACTION_MAP.md`.

The main objective is to make the M3 extraction mechanical and reviewable rather than inventing interfaces while moving code.

---

## 1. Design principles

BibReview must remain understandable and maintainable without requiring knowledge of PHRAISE internals.

The following rules are fixed for the first implementation:

1. **BibReview is a Python package and CLI; PHRAISE is a configured consumer.**
2. **The Python engine is usable without Ruby/Jekyll installed.**
3. **The reusable website layer belongs to BibReview but is isolated from the bibliographic engine.**
4. **Project scientific policy is configuration, never hard-coded engine logic.**
5. **Publication identity is independent of DOI.**
6. **A DOI is an optional external identifier, not a primary key.**
7. **Project files remain project-owned; BibReview never hides user data in package directories.**
8. **Network providers are adapters around a small internal model.**
9. **Provider/API failures must remain explicit and testable.**
10. **Human review remains a supported part of the workflow.** BibReview must not automate ambiguous author identity or relevance decisions merely to provide a one-command pipeline.
11. **PHRAISE remains the end-to-end regression case throughout M3–M5.**
12. **The initial implementation favours the Python standard library and the dependencies already justified by PHRAISE.**

---

## 2. Distribution and packaging

The future repository is expected to be named `BibReview` and the import package `bibreview`.

The first package targets **Python 3.12+**, matching the current validated PHRAISE maintenance environment.

BibReview will use a modern `pyproject.toml` package with a `src/` layout:

```text
BibReview/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── bibreview/
├── tests/
└── examples/
```

The `src/` layout is intentional: tests and local commands should exercise the installed package rather than accidentally importing a checkout-only module.

### Initial runtime dependencies

Keep the dependency set small and close to the current working PHRAISE implementation:

- `requests`
- `urllib3`
- `beautifulsoup4`
- `Unidecode`
- `python-dotenv`
- a YAML reader for `bibreview.yml` (initially `PyYAML` is sufficient)

Do **not** introduce Pydantic, Click, Typer, Jinja2, an ORM, or a database solely to structure the first extraction. They can be reconsidered later if an actual need appears.

### CLI entry point

`pyproject.toml` will expose:

```toml
[project.scripts]
bibreview = "bibreview.cli:main"
```

The CLI implementation will initially use `argparse` from the standard library.

### Licence

BibReview should start under **GNU GPL v3**, matching the existing PHRAISE code from which the first implementation is extracted. Use SPDX identifier `GPL-3.0-only` unless the future BibReview repository explicitly adopts an "or later" grant.

---

## 3. Target package tree

The M2 target is deliberately compact:

```text
src/bibreview/
├── __init__.py
├── __main__.py
├── cli.py
├── config.py
├── model.py
├── identity.py
├── storage.py
├── text.py
├── providers/
│   ├── __init__.py
│   ├── http.py
│   ├── crossref.py
│   ├── openalex.py
│   ├── elsevier.py
│   ├── springer.py
│   ├── ieee.py
│   ├── semantic_scholar.py
│   └── mendeley.py
├── pipeline/
│   ├── __init__.py
│   ├── discover.py
│   ├── collect.py
│   ├── authors.py
│   ├── merge.py
│   └── validate.py
└── site/
    ├── __init__.py
    ├── transform.py
    ├── render.py
    └── template/
        └── ...
```

This tree is the initial target, not a requirement to create empty modules during M3. Modules should appear when real code is moved into them.

### Responsibility boundaries

#### `config.py`

- load `bibreview.yml`;
- resolve paths relative to the project configuration file;
- apply documented defaults;
- validate configuration types and required values;
- expose immutable/typed configuration objects where useful.

It must not perform network calls or mutate project data.

#### `model.py`

- publication data model;
- author/name representation;
- external identifiers;
- references;
- date/value normalization that is intrinsic to the data model.

It must not know about Jekyll paths or PHRAISE.

#### `identity.py`

- generation and validation of stable internal publication IDs;
- external-identifier normalization (`doi`, later `arxiv`, etc.);
- matching/deduplication helpers;
- author-identity planning and ambiguity reporting.

It must not silently merge ambiguous records.

#### `storage.py`

- read/write canonical project state;
- safe and atomic/staged writes;
- backups;
- queue/archive loading;
- path safety;
- JSON serialization.

No provider-specific HTTP logic belongs here.

#### `text.py`

- slugification;
- metadata cleaning;
- MathJax/Liquid-safe text transformations that are still required by the current output contract.

Site-only wording does not belong here.

#### `providers/`

Each provider module adapts one external service to BibReview concepts.

`providers/http.py` owns shared HTTP session, retry, timeout, sanitized diagnostics and transport errors. Provider modules own endpoint-specific field extraction.

A provider receives the information it needs from configuration/call arguments. It must not embed PHRAISE queries, contact details, repository URLs or filesystem paths.

#### `pipeline/`

Pipeline modules coordinate project state and providers:

- `discover.py`: find and classify candidates;
- `collect.py`: obtain metadata for accepted identifiers and create/update publication records;
- `authors.py`: author-name mapping plan and safe additions;
- `merge.py`: merge collected data into canonical project state;
- `validate.py`: structural and cross-file consistency validation.

These modules implement workflow rules, but scientific relevance criteria come from configuration.

#### `site/`

The site package is a separate layer:

- `transform.py`: convert bibliography/model data into deterministic site-facing views;
- `render.py`: render publication, author, year and category outputs;
- `template/`: reusable Jekyll layouts/includes/assets/scaffold.

The bibliographic engine must be fully testable without importing Jekyll/Ruby tooling.

---

## 4. Publication model

### 4.1 Internal identity

Every publication has a persistent BibReview internal identifier:

```text
id: "..."
```

The identifier is opaque. It is not a DOI, title slug, filename or database row number.

For new records, BibReview uses a UUID generated once and persisted. The implementation should use the Python standard library `uuid` module.

For the initial PHRAISE migration, existing DOI-backed publications may receive deterministic UUIDv5 values derived from a fixed BibReview migration namespace and the **normalized DOI**. This gives reproducible migration output while keeping the DOI out of the model's identity contract.

Important invariants:

- once persisted, `id` never changes merely because metadata changes;
- adding a DOI later to a DOI-less publication does not change `id`;
- correcting or replacing a DOI does not change `id`;
- site permalinks/slugs are separate and may be changed by explicit migration without changing identity.

### 4.2 External identifiers

External identifiers are stored separately:

```yaml
identifiers:
  doi: "10.1234/example"
  # later: arxiv, openalex, pubmed, isbn-as-appropriate, ...
```

`doi` is optional.

Normalization rules belong to the corresponding identifier helper/provider. For DOI, the canonical stored value is lower-case without `https://doi.org/`.

### 4.3 Core record

The initial `Publication` model should cover the information PHRAISE currently needs without pretending that every field is universal:

```text
Publication
├── id: str
├── identifiers: dict[str, str]
├── type: str
├── title: str
├── authors: list[Author]
├── abstract: str
├── container_title: str
├── publication_year: str
├── volume: str
├── issue: str
├── pages: str
├── publisher: str
├── event: str
├── keywords: list[str] or normalized textual representation
├── created_date: date-like value required for current deterministic output
├── permalink: str
└── references: list[Reference]
```

The M3 migration may initially keep a compatibility serializer for current `biblio.json`; changing every persisted field name is **not** required before extraction succeeds.

### 4.4 Author representation

An author attached to a publication represents the source-provided name, not an automatically inferred real-world identity:

```text
Author
├── given: str | None
├── family: str | None
└── optional source fields preserved when useful
```

Canonical author identity remains project state (`author_mappings`) because ambiguous mappings require human judgment.

A later dedicated author entity can be introduced only if it solves a concrete problem; it is not required for M3.

### 4.5 References

A reference must be able to exist without DOI:

```text
Reference
├── identifiers: dict[str, str]
└── citation: str
```

The current `{"doi": ..., "title": ...}` form can be supported by the compatibility adapter during migration.

---

## 5. Deduplication and matching policy

Internal identity and duplicate detection are deliberately separate concepts.

Initial matching order:

1. exact normalized DOI match when both records have a DOI;
2. exact match on another strong external identifier when supported later;
3. otherwise **no automatic destructive merge** in the first implementation.

Title/author/year similarity may later be used to *suggest* possible duplicates, but must initially send uncertain cases to human review rather than automatically merge them.

This conservative rule is important for publications without DOI.

---

## 6. Project configuration: `bibreview.yml`

`bibreview.yml` is project-owned and lives at the project root by default.

The first line-level contract is:

```yaml
schema_version: 1
```

The schema version is mandatory. BibReview must refuse unknown future major schema versions rather than silently reinterpret configuration.

The configuration is divided into six responsibilities:

```text
project
paths
discovery
relevance
providers
site
```

An example PHRAISE-oriented configuration is stored separately in `BIBREVIEW_M2_CONFIG_EXAMPLE.yml`.

### 6.1 `project`

Project identity and contact information:

- `name`: human-readable project name;
- `slug`: filesystem/cache-safe project namespace;
- `title` and `description`;
- `repository` URL;
- maintainer name/contact when supplied.

The project slug replaces hard-coded strings such as `phraise_biblio_cache` in reusable site code.

### 6.2 `paths`

All project state paths are explicit/configurable and resolved relative to `bibreview.yml`.

BibReview defines sensible canonical defaults for new projects, but PHRAISE is allowed to keep its current `docs/...` layout during migration.

Paths cover at least:

- bibliography data;
- author mappings;
- known/pending/rejected/manual-review queues;
- BibTeX assets;
- archive/backups;
- site source/output locations as needed.

No engine module may reconstruct PHRAISE paths independently once the configuration layer exists.

### 6.3 `discovery`

Discovery describes **where candidate publications are searched**.

The first supported discovery backend remains OpenAlex. Its query is configuration:

```yaml
discovery:
  provider: openalex
  query: "port-Hamiltonian"
  max_pages: 20
```

Provider-specific query syntax is allowed. BibReview must not pretend all scholarly services share one query language.

### 6.4 `relevance`

Relevance describes the **project's scientific acceptance policy** after discovery.

To preserve PHRAISE behaviour without hard-coding it, schema v1 supports configurable case-insensitive regular expressions:

```yaml
relevance:
  patterns:
    - 'port[-\\s]+(controlled )?hamiltonian'
    - 'interconnection and damping assignment'
    - 'dirac structure'
    - 'dissipative hamiltonian'
```

A candidate matching one configured pattern can be automatically queued for collection; otherwise it goes to manual review, preserving the current workflow.

Regex configuration is intentionally explicit. A friendlier keyword/expression layer can be added later without weakening the reproducibility of PHRAISE's current selection policy.

### 6.5 `providers`

Provider configuration controls enablement and credential environment-variable names.

Secrets are **never stored in `bibreview.yml`**.

Example concept:

```yaml
providers:
  crossref:
    enabled: true
  semantic_scholar:
    enabled: true
  mendeley:
    enabled: false
    token_env: MENDELEY_API_KEY
```

BibReview may provide conventional environment variable defaults. A project's `.env` remains local and ignored by Git.

### 6.6 `site`

The site section describes reusable rendering while leaving branding/content project-owned:

- enabled/disabled;
- implementation (`jekyll` for schema v1);
- template name (`default` initially);
- site source root;
- title/URL/base path overrides where needed;
- logo/favicon references;
- optional feature flags such as search or analytics.

The first implementation does not need multiple visual themes. The current PHRAISE appearance becomes the initial reusable `default` template after project-specific values are removed.

---

## 7. CLI design

The M2 CLI intentionally mirrors human review boundaries rather than forcing a monolithic command.

Initial commands:

```text
bibreview discover
bibreview collect [INPUT]
bibreview authors [--apply-safe] [--json]
bibreview merge
bibreview render
bibreview validate
bibreview status
```

Every command accepts a project configuration path, defaulting to `bibreview.yml` in the current directory:

```text
bibreview --config path/to/bibreview.yml <command>
```

Common flags:

```text
-v / -vv
-q / --quiet
--dry-run
```

Network commands retain the current rule: `--dry-run` prevents mutations but may still perform HTTP requests.

### `discover`

Equivalent responsibility to current `looking4Update.py`:

- query discovery provider;
- normalize candidate identifiers;
- verify supported records;
- apply configured relevance policy;
- update pending/manual/rejected state;
- inspect incomplete records that require recollection.

### `collect [INPUT]`

Equivalent to `getData.py`:

- default input is the configured pending queue;
- an explicit input path may be supplied;
- create candidate publication records and BibTeX assets;
- do not merge them blindly into canonical state if the current workflow requires a separate merge step.

### `authors`

Equivalent to `setAuthorMapping.py`:

- report safe proposals and ambiguous mappings;
- `--apply-safe` writes only unambiguous additions;
- ambiguity remains a human decision.

### `merge`

Equivalent to `concatenate.py`:

- merge collected records with canonical bibliography;
- update identifier queues;
- apply exclusions;
- preserve backup semantics.

Merge uses internal `Publication.id` and strong external identifiers appropriately; it must not restore DOI as the universal identity.

### `render`

Equivalent to the reusable part of `setPosts.py && setPages.py`:

- generate publication pages;
- generate author/year/category views;
- produce/refresh instance outputs;
- never rewrite project editorial pages unless explicitly part of a scaffold operation.

`render` does **not** invoke Ruby/Jekyll itself in the core M3 implementation.

### `validate`

Checks project state without network access by default:

- configuration schema;
- publication model validity;
- duplicate internal IDs;
- duplicate strong external identifiers;
- author mapping consistency;
- path safety;
- required referenced files;
- site-view prerequisites when site rendering is enabled.

### `status`

A read-only operator summary:

- canonical publication count;
- pending/rejected/manual-review counts;
- unknown author names;
- configuration/provider enablement summary;
- whether the project needs human action before rendering/updating.

This command is new but intentionally simple. It makes the multi-step workflow easier to operate without hiding its state.

### No `update` command in schema/API v1

M1 suggested a possible `bibreview update`, but M2 deliberately defers it.

The current workflow contains two real human review points:

1. scientific relevance (`checkDOI.txt`);
2. ambiguous author identity.

A one-command `update` would either stop halfway, hide these decisions, or define automation semantics prematurely. It can be added later as an orchestrator once the individual commands and stop conditions are stable.

---

## 8. Storage design and migration compatibility

### Canonical new-project layout

For a new project, BibReview should recommend a simple project-owned layout such as:

```text
my-review/
├── bibreview.yml
├── data/
│   ├── bibliography.json
│   ├── authors.json
│   ├── known.txt
│   ├── pending.txt
│   ├── rejected.txt
│   └── review.txt
├── bib/
├── archive/
└── site/
```

This is a default, not a hard-coded layout.

### PHRAISE compatibility during M3

PHRAISE should initially configure existing paths:

```text
docs/assets/data/biblio.json
docs/assets/data/author_mappings.json
docs/DOI.txt
docs/newDOI.txt
docs/badDOI.txt
docs/checkDOI.txt
docs/assets/bib/
docs/trash/
docs/
```

This avoids combining code extraction with a large data-tree migration.

### Persistence format

JSON remains the canonical bibliography persistence format for the first extraction. It is already proven on the PHRAISE dataset and keeps M3 focused.

The internal Python model may be cleaner than the legacy JSON schema. A compatibility adapter can therefore read/write the current PHRAISE representation until an explicit data migration is performed.

Do not introduce SQLite in M3.

---

## 9. Provider interface

Providers should remain ordinary Python classes/functions rather than a dynamic plugin framework in the first version.

Conceptually:

```text
CrossRefProvider
OpenAlexProvider
ElsevierProvider
SpringerProvider
IEEEProvider
SemanticScholarProvider
MendeleyProvider
```

They share a configured HTTP transport and return provider-specific payloads or normalized helper values to the pipeline.

M2 explicitly rejects premature entry-point/plugin discovery. The provider package boundary is enough to add another built-in provider later.

### Provider configuration invariant

No provider may contain:

- `PHRAISE` as application identity;
- `g-haine/phraise` as repository identity;
- port-Hamiltonian queries;
- maintainer email literals;
- fixed `docs/` paths.

HTTP identification should be assembled from BibReview version + project contact/repository where appropriate.

---

## 10. Site architecture

The site layer has two kinds of material and they should not be confused.

### Generated bibliography views

Owned by `bibreview.site` logic:

- publication pages;
- author pages/index;
- year pages/index;
- category views;
- search data linkage;
- generated update metadata.

### Static reusable template

Owned by `bibreview.site.template`:

- layouts;
- generic includes;
- CSS/Sass;
- generic JavaScript;
- generic category/search/404 scaffold.

### Project-owned site content

Never package PHRAISE-specific content as defaults:

- PHRAISE homepage prose;
- PHRAISE about/contribution text;
- PHRAISE logos and institutional logos;
- PHRAISE analytics IDs;
- PHRAISE external domain links.

### Search JavaScript

The current browser search remains useful and can become generic once:

- class names lose `Phraise` naming;
- local-storage keys are namespaced from `project.slug`;
- bibliography URL is configurable/generated;
- DOI display is optional;
- records without DOI are valid.

### arXiv

The separate latest-arXiv subsystem remains outside M3 core extraction. It is revisited only after the provider/config/site boundaries above exist.

---

## 11. Validation and tests

BibReview tests should be organized by responsibility rather than by historical script name:

```text
tests/
├── test_config.py
├── test_model.py
├── test_identity.py
├── test_storage.py
├── providers/
├── pipeline/
├── site/
└── fixtures/
```

Key invariants to test from the start:

- a publication without DOI is model-valid;
- duplicate internal IDs are rejected;
- duplicate DOI detection is separate from internal identity;
- adding/changing DOI does not change persisted internal ID;
- project paths resolve relative to the configuration file;
- no provider needs PHRAISE-specific constants;
- dry-run is byte-for-byte non-mutating;
- API credentials are not exposed in diagnostics;
- PHRAISE legacy fixtures continue to produce equivalent outputs during migration.

PHRAISE itself should retain a small end-to-end consumer test once code moves to BibReview.

---

## 12. M3 extraction order

M3 should not copy `phraise_tools` wholesale. Use this order:

1. create BibReview repository/package skeleton and packaging metadata;
2. implement configuration loading and path resolution;
3. implement publication identity/model compatibility layer;
4. extract shared text/storage/reporting utilities;
5. extract HTTP transport and CrossRef first;
6. extract collection pipeline and its tests;
7. extract remaining metadata/enrichment providers;
8. extract merge logic;
9. extract author mapping logic;
10. extract discovery/OpenAlex logic with relevance supplied by PHRAISE configuration;
11. leave site rendering in PHRAISE until bibliographic engine equivalence is established;
12. only then begin the site/template extraction milestone.

At every meaningful step, PHRAISE remains runnable against the M0 reference behaviour.

---

## 13. Explicit non-goals for M2/M3

Do not add these while extracting the working engine:

- a web application/server;
- SQL/SQLite persistence;
- an ORM;
- a provider plugin marketplace;
- a GUI;
- parallel/distributed collection;
- a new Jekyll theme system;
- automatic fuzzy duplicate merging;
- automatic ambiguous author merging;
- Zotero fallback;
- full arXiv integration into the core pipeline;
- a one-command unattended update workflow.

These would mix product expansion with extraction and make regression analysis harder.

---

## 14. M2 acceptance criteria

M2 is complete when the following are accepted:

- [x] package boundary and `src/` layout;
- [x] Python baseline and minimal dependency policy;
- [x] licence direction compatible with extracted PHRAISE code;
- [x] publication internal identity independent of DOI;
- [x] conservative duplicate matching policy;
- [x] `bibreview.yml` schema responsibilities;
- [x] project path/configuration ownership;
- [x] scientific discovery/relevance configuration boundary;
- [x] provider boundary;
- [x] CLI command set and human review points;
- [x] engine/site separation;
- [x] PHRAISE compatibility strategy for M3;
- [x] initial test invariants;
- [x] extraction order for M3.

M2 deliberately ends with architecture and interface decisions. **M3 is the first milestone that creates the BibReview codebase and begins moving working code out of PHRAISE.**
