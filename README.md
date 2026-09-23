# PHRAISE

**Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy**

PHRAISE is a bibliographic survey dedicated to research on port-Hamiltonian
systems. The website is a project powered by
[BibReview](https://github.com/g-haine/bibreview): BibReview owns the
bibliographic workflow, canonical state transitions, contributor handling, and
static site rendering; PHRAISE supplies the subject-specific configuration,
curated data, and Jekyll presentation. The optional arXiv cache is also managed by
BibReview but remains separate from the canonical DOI bibliography.

PHRAISE currently pins **BibReview v1.6.13** for reproducible maintenance and
continuous integration.

## Contributing new DOIs

Contributions are welcome in the form of DOI submissions:

- open a pull request adding DOI values to `docs/newDOI.txt`;
- or send them by email to <ghislain.haine@isae.fr>.

## Project architecture

The central project configuration is `bibreview.yml`.

Important state files are:

- `docs/assets/data/bibliography.json` — canonical BibReview bibliography
  document;
- `docs/assets/data/collected.json` — temporary canonical staging used by
  collect and reviewed apply workflows before merge;
- `docs/assets/data/author_mappings.json` — reviewed author identities;
- `audit/campaign.json`, `audit/report.json`, and `audit/resolutions.json` — local
  persistent audit history, review report, and resumable human decisions;
- `audit/backfill.json`, `audit/backfill-resolutions.json`,
  `audit/refresh.json`, and `audit/refresh-resolutions.json` — local
  proposal/review state for human-reviewed missing-field enrichment and safe
  refresh, separate from canonical staging and ignored by Git;
- `docs/assets/bib/` — tracked BibTeX sources;
- `docs/DOI.txt`, `docs/newDOI.txt`, `docs/checkDOI.txt`,
  `docs/badDOI.txt` — DOI workflow state.

Generated Jekyll artifacts are owned by `bibreview render`:

- `docs/_posts/`;
- `docs/authors/`;
- `docs/years/`;
- `docs/_data/bibreview/`.

PHRAISE contains no project-specific Python bibliographic code. The optional
arXiv cache is configured in `bibreview.yml` and remains intentionally
independent of the canonical bibliography.

## Canonical bibliography document

`bibliography.json` is a BibReview document, not a bare publication array:

```json
{
  "metadata": {
    "schema_version": 2,
    "last_update": "2026-09-21"
  },
  "publications": [
    {
      "id": "...",
      "identifiers": {
        "doi": "..."
      },
      "title": "...",
      "authors": [
        {
          "given": "...",
          "family": "...",
          "literal": null,
          "source_fields": {}
        }
      ]
    }
  ]
}
```

Schema version 2 requires every canonical publication to contain at least one
author or editor. Empty `editors` lists are omitted from the canonical JSON.

`metadata.last_update` changes only when an effective BibReview merge adds or
updates publications. An arXiv-only update therefore does **not** change the
bibliography update date displayed on the website.

During rendering, BibReview derives
`docs/_data/bibreview/metadata.json` from this canonical metadata so Jekyll can
use it without duplicating the source of truth.

The canonical database is also exposed by the website and used directly by the
search interface.

## Repository governance

`main` is the production branch for the published PHRAISE site. Changes to
bibliographic state, generated site artifacts, configuration, workflows, or
presentation are intended to reach `main` through pull requests.

The `BibReview integration` workflow validates pull requests targeting
`main`. It checks the BibReview configuration and version, canonical state,
author mappings, deterministic rendering, search JavaScript, the complete
Jekyll build, and the displayed bibliography update date.

The scheduled arXiv workflow never writes directly to `main`. When the cache
changes, it creates or updates the `automation/update-arxiv` branch and opens
a pull request. The updater then explicitly dispatches the PHRAISE integration
workflow on that branch, verifies that the diff contains **only**
`docs/assets/data/arxiv.json`, and squash-merges the PR only after validation succeeds.
No daily maintainer approval is required.

## Maintenance environment

Create or update the maintenance environment from the repository root:

```bash
bash install.sh
conda activate phraise
```

The Conda environment contains Python 3.12 and **BibReview v1.6.13**.
BibReview itself declares and installs its Python dependencies.

Provider secrets remain local. `bibreview.yml` points BibReview at
`docs/.env`. A typical file is:

```text
SCOPUS_API_KEY=
SPRINGER_API_KEY=
IEEE_API_KEY=
OPENALEX_API_KEY=
SEMANTIC_SCHOLAR_API_KEY=
MENDELEY_CLIENT_ID=
MENDELEY_CLIENT_SECRET=
```

Values already exported in the process environment take precedence over values
from `.env`.

Provider request pacing is project policy in `bibreview.yml`. PHRAISE currently
uses:

```yaml
providers:
  crossref:
    min_interval_seconds: 0.5
  openalex:
    min_interval_seconds: 0.5
  elsevier:
    min_interval_seconds: 0.5
  springer:
    min_interval_seconds: 0.5
  ieee:
    min_interval_seconds: 0.5
  semantic_scholar:
    min_interval_seconds: 1.5
  mendeley:
    min_interval_seconds: 0.5
```

The value is the minimum interval between the start of two successive HTTP
requests to the same provider. Each provider is throttled independently, so the
Semantic Scholar delay does not slow OpenAlex, CrossRef, or publisher lookups.
This policy can be changed in YAML if an upstream provider changes its rate-limit
guidance; no BibReview code change is required. Check the effective values with:

```bash
bibreview providers
```

With OpenAlex enabled in `bibreview.yml`, BibReview v1.6.13 uses it for three
separate purposes in PHRAISE: DOI discovery, independent audit evidence, and
optional abstract fallback when publisher/CrossRef enrichment leaves an abstract
empty. Semantic Scholar and Mendeley remain optional abstract fallbacks as well.
Fallback candidates are cleaned before comparison (surrounding whitespace and
leading labels such as `Abstract`, `Résumé`, etc. are removed conservatively),
then BibReview keeps the longest valid candidate. An OpenAlex API key is optional
but may improve rate-limit predictability.

## Human-reviewed enrichment and safe refresh

BibReview v1.6.13 provides two complementary workflows for existing canonical
records.

For a known missing field such as an abstract, use `backfill`:

```bash
bibreview backfill --field abstract
bibreview backfill --resolve
bibreview --dry-run backfill --apply
bibreview backfill --apply
```

Provider values are only proposals. The resolver requires an explicit human
decision for every candidate. Accepted/custom values alone reach
`collected.json`; existing meaningful canonical fields are never replaced.
BibReview v1.6.13 batches exact multi-DOI backfill lookups where supported:
CrossRef work metadata in groups of up to 25 DOI values, OpenAlex abstract
fallback in groups of up to 100, and Semantic Scholar abstract fallback in
groups of up to 500; publisher enrichment and Mendeley remain per DOI.
BibReview v1.6.13 also allows scalar-field backfill from partial provider records:
an abstract proposal no longer depends on unrelated provider authors, editors, or
creation dates being present. Normal collection of new canonical publications
remains strict and still requires at least one author or editor.

For `abstract`, BibReview v1.6.13 treats the historical placeholder
`Not Available` as semantically missing, case- and whitespace-insensitively.
Those records are therefore eligible for reviewed backfill. Provider/fallback
values that normalize to the same placeholder are treated as unavailable and
are never proposed as real abstracts.

Optional publisher enrichment is failure-tolerant in v1.6.13. If Elsevier,
Springer, or IEEE returns an HTTP access/rate-limit/service error, BibReview
reports a warning and continues with the remaining configured enrichment and
abstract fallback sources instead of aborting the whole maintenance run. Persistent
HTTP 401/403/429 responses disable only that optional publisher for the rest of
the current run; non-HTTP contract/type errors still stop execution because they
indicate an implementation defect rather than temporary provider unavailability.

For configured incomplete journal records, `refresh` is now non-destructive:

```bash
bibreview refresh
bibreview -v refresh --review
bibreview refresh --resolve
bibreview --dry-run refresh --apply
bibreview refresh --apply
```

Remote DOI BibTeX is used only to detect staleness. A stale record is recollected
in memory and compared field-by-field with the canonical publication. Only
configured fields that are semantically missing can become safe proposals.
For abstracts, the historical `Not Available` placeholder follows the same
missing-value rule used by backfill. Differences affecting already-populated
title, authors, journal, dates, pages, publisher, or other metadata are kept as
collateral evidence and cannot be promoted by `refresh`.

Tracked BibTeX is never replaced wholesale from the remote provider during
refresh. Only accepted fields may be edited locally, with a backup, and
`bibreview merge` remains the only canonical promotion boundary.

## Auditing the historical bibliography

BibReview v1.6.13 can compare the existing canonical bibliography with current
CrossRef, OpenAlex, and Semantic Scholar evidence without modifying canonical
metadata. Audit state is persistent and incremental: publications already marked
`completed` in the local audit history are not requested again by a normal
`bibreview audit` run, while newly added canonical publication UUIDs are
appended automatically as pending work. Retryable provider failures remain
eligible after never-audited publications.

Network lookups are batched where the provider supports exact multi-DOI
requests: CrossRef uses bounded groups of 25 DOI values, OpenAlex up to 100,
and Semantic Scholar up to 500. This changes transport efficiency only; audit
comparison and review semantics are unchanged. Existing campaign-schema-1
checkpoints are read transparently and rewritten as campaign schema 2 on the
next audit-state update; audit progress and the report are preserved.

Preview a small pilot batch without writing audit state or calling providers:

```bash
bibreview --dry-run audit --batch-size 25
```

Run the 25-publication pilot:

```bash
bibreview audit --batch-size 25
```

Provider differences are evidence for review, not automatic corrections.
BibReview v1.6.13 provides a derived read-only review that applies the current
normalization and corroboration rules without network access or file changes.
The default review is intentionally concise:

```bash
bibreview audit --review
```

Use the global verbose option only when the full publication-by-publication
findings are needed:

```bash
bibreview -v audit --review
```

Once the campaign is complete, resolve actionable findings interactively without
changing the canonical bibliography:

```bash
bibreview audit --resolve
```

Decisions are resumable and stored separately from canonical/staging data. In
BibReview v1.6.13, page-range proposals are normalized to BibTeX-style double
hyphens, for example `8793--8805`; tuple-valued custom corrections such as
authors accept semicolon-separated values; and interactive terminal line editing
is enabled when Python's standard `readline` module is available.

Once every actionable finding has a final decision, promote the reviewed
accepted/custom corrections explicitly into the normal `collected.json`
staging:

```bash
bibreview --dry-run audit --apply
bibreview audit --apply
```

`audit --apply` never writes `bibliography.json` directly. It requires empty
staging, rejects stale canonical values or incomplete resolution state, updates
applicable tracked BibTeX fields with backups, and leaves rejected decisions
unchanged. BibReview v1.6.13 also reports accepted/custom resolutions that already
match the canonical value explicitly as no-op resolutions; they are not staged
and do not trigger BibTeX writes. Inspect the resulting JSON/BibTeX diff before
the normal `bibreview merge` boundary.

A provider-only alternative remains informational by default. A missing or
substantively different canonical value becomes actionable only when the same
alternative is corroborated by at least two independent providers after
review-equivalent representations are grouped. One-day `created_date` offsets,
obvious provider truncations of a fuller canonical abstract, role disagreements,
and isolated contributor anomalies remain informational evidence.

When audit comparison rules improve, preview an offline reclassification of the
already-collected evidence:

```bash
bibreview --dry-run audit --reclassify
```

If the before/after counts are satisfactory, apply it:

```bash
bibreview audit --reclassify
bibreview audit --review
```

Reclassification rewrites only the local `audit/report.json`; it does not
change campaign progress or canonical bibliography data.

Normal subsequent networked audit invocations use PHRAISE's configured default
batch size of 50 and process only new or retryable audit items:

```bash
bibreview audit
```

When fresh provider evidence is deliberately required for the entire current
canonical bibliography, force a complete new pass with:

```bash
bibreview audit --full
```

`--full` preserves the local report and attempt history while requeueing all
current canonical publication UUIDs. It refuses to reset an interrupted open
batch; resume that batch first.

## Updating the bibliography

Run commands from the repository root. Because the configuration file is named
`bibreview.yml`, the CLI uses it by default; `--config bibreview.yml` is
therefore unnecessary here.

1. Discover and classify new candidates:

   ```bash
   bibreview discover
   ```

2. Review `docs/checkDOI.txt` manually and move classified DOI values to
   `docs/newDOI.txt` or `docs/badDOI.txt`.

3. Review and resolve safe refresh proposals for incomplete existing publications:

   ```bash
   bibreview refresh
   bibreview -v refresh --review
   bibreview refresh --resolve
   bibreview --dry-run refresh --apply
   bibreview refresh --apply
   bibreview --dry-run merge
   bibreview merge
   ```

   The initial refresh scan writes only local review state. Only human-approved
   missing-field fills reach `collected.json`.

4. When a specific missing field should be enriched independently of BibTeX
   staleness, use reviewed backfill, for example:

   ```bash
   bibreview backfill --field abstract
   bibreview backfill --resolve
   bibreview --dry-run backfill --apply
   bibreview backfill --apply
   bibreview --dry-run merge
   bibreview merge
   ```

5. Collect pending new/recovered DOI values, then merge them:

   ```bash
   bibreview collect
   bibreview merge
   ```

6. Review author identities:

   ```bash
   bibreview authors
   ```

   Apply only unambiguous additions when appropriate:

   ```bash
   bibreview authors --apply-safe
   ```

   Review any remaining ambiguous cases manually in
   `docs/assets/data/author_mappings.json`.

7. Render the complete generated site surface:

   ```bash
   bibreview render
   ```

   Rendering performs no provider/network fallback. Every canonical publication
   must already have its tracked BibTeX file. Unused BibTeX files are reported,
   not moved or deleted.

For a read-only preview of any supported mutation, use the global
`--dry-run` option, for example:

```bash
bibreview --dry-run render
```

After a maintenance cycle, review the complete Git diff and submit the resulting
state and generated artifacts through a pull request.

## Local website preview

PHRAISE uses Jekyll for presentation. Install Ruby and Bundler, then:

```bash
cd docs
bundle install
bundle exec jekyll serve --watch
```

Open <http://127.0.0.1:4000> and inspect the generated site.

## arXiv cache

arXiv entries are deliberately separate from the canonical DOI bibliography.
They are display-only links managed by BibReview's optional arXiv module:

```bash
bibreview arxiv
```

The scheduled GitHub workflow runs this command and changes only
`docs/assets/data/arxiv.json`. If the cache changes, the workflow opens or updates a
pull request instead of pushing to `main`. That PR is merged automatically only
after the updater explicitly runs the integration CI and verifies a cache-only
diff. If the arXiv provider is temporarily unavailable, the workflow keeps the
existing cache untouched and ends without opening a PR. The module does not
create canonical `Publication` objects and does not affect
`bibliography.json.metadata.last_update`.

This separation is why the bibliography date comes from
`bibliography.json.metadata.last_update` rather than the Jekyll build time.

## Validation

The PHRAISE integration workflow verifies the current architecture directly:

- exact BibReview v1.6.13 installation;
- BibReview configuration validation;
- canonical merge no-op state;
- author mapping consistency;
- full `bibreview render` reconciliation;
- clean tracked tree after rendering;
- JavaScript syntax for the canonical bibliography search;
- complete Jekyll build;
- displayed canonical bibliography update date.

There is no separate PHRAISE bibliographic Python engine: reusable
bibliographic behavior belongs in BibReview.
