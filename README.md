# PHRAISE

**Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy**

PHRAISE is a bibliographic survey dedicated to research on port-Hamiltonian
systems. The website is a project powered by
[BibReview](https://github.com/g-haine/bibreview): BibReview owns the
bibliographic workflow, canonical state transitions, contributor handling, and
static site rendering; PHRAISE supplies the subject-specific configuration,
curated data, and Jekyll presentation. The optional arXiv cache is also managed by
BibReview but remains separate from the canonical DOI bibliography.

PHRAISE currently pins **BibReview v1.6.2** for reproducible maintenance and
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
  collect/refresh before merge;
- `docs/assets/data/author_mappings.json` — reviewed author identities;
- `audit/campaign.json`, `audit/report.json`, and `audit/resolutions.json` — local
  historical-audit checkpoint, review report, and resumable human decisions,
  separate from canonical staging and ignored by Git;
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

The Conda environment contains Python 3.12 and **BibReview v1.6.2**.
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

## Auditing the historical bibliography

BibReview v1.6.2 can compare the existing canonical bibliography with current
CrossRef, OpenAlex, and Semantic Scholar evidence without modifying canonical
metadata.
Network lookups are batched where the provider supports exact multi-DOI
requests: CrossRef uses bounded groups of 25 DOI values, OpenAlex up to 100,
and Semantic Scholar up to 500. This changes transport efficiency only; audit
comparison and review semantics are unchanged. Existing campaign-schema-1 checkpoints are read transparently and
rewritten as campaign schema 2 on the next audit-state update; audit progress and
the report are preserved.

Preview a small pilot batch without writing audit state or calling providers:

```bash
bibreview --dry-run audit --batch-size 25
```

Run the 25-publication pilot:

```bash
bibreview audit --batch-size 25
```

Provider differences are evidence for review, not automatic corrections.
BibReview v1.6.2 provides a derived read-only review that applies the current
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
BibReview v1.6.2, page-range proposals are normalized to BibTeX-style double
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
unchanged. BibReview v1.6.2 also reports accepted/custom resolutions that already
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

Once the review rules are satisfactory, subsequent networked audit invocations
return to PHRAISE's configured default batch size of 50:

```bash
bibreview audit
```

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

3. Refresh incomplete existing publications:

   ```bash
   bibreview refresh
   bibreview merge
   ```

   Refresh and collection share `collected.json`, so refresh staging is merged
   before collecting new DOI values.

4. Collect pending new/recovered DOI values, then merge them:

   ```bash
   bibreview collect
   bibreview merge
   ```

5. Review author identities:

   ```bash
   bibreview authors
   ```

   Apply only unambiguous additions when appropriate:

   ```bash
   bibreview authors --apply-safe
   ```

   Review any remaining ambiguous cases manually in
   `docs/assets/data/author_mappings.json`.

6. Render the complete generated site surface:

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

- exact BibReview v1.6.2 installation;
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
