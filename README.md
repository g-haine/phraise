# PHRAISE

**Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy**

PHRAISE is a bibliographic survey dedicated to research on port-Hamiltonian
systems. The website is a project powered by
[BibReview](https://github.com/g-haine/bibreview): BibReview owns the
bibliographic workflow, canonical state transitions, author handling, and static
site rendering; PHRAISE supplies the subject-specific configuration, curated
data, and Jekyll presentation. The optional arXiv cache is also managed by
BibReview but remains separate from the canonical DOI bibliography.

PHRAISE currently pins **BibReview v1.0.0** for reproducible maintenance and
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
    "schema_version": 1,
    "last_update": "2026-09-11"
  },
  "publications": [
    {
      "id": "...",
      "identifiers": {
        "doi": "..."
      },
      "title": "..."
    }
  ]
}
```

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
`docs/data/arxiv.json`, and squash-merges the PR only after validation succeeds.
No daily maintainer approval is required.

## Maintenance environment

Create or update the maintenance environment from the repository root:

```bash
bash install.sh
conda activate phraise
```

The Conda environment contains Python 3.12 and **BibReview v1.0.0**.
BibReview itself declares and installs its Python dependencies.

Provider secrets remain local. `bibreview.yml` points BibReview at
`docs/.env`. A typical file is:

```text
SCOPUS_API_KEY=
SPRINGER_API_KEY=
IEEE_API_KEY=
MENDELEY_API_KEY=
OPENALEX_API_KEY=
```

Values already exported in the process environment take precedence over values
from `.env`.

## Updating the bibliography

Run commands from the repository root.

1. Discover and classify new candidates:

   ```bash
   bibreview --config bibreview.yml discover
   ```

2. Review `docs/checkDOI.txt` manually and move classified DOI values to
   `docs/newDOI.txt` or `docs/badDOI.txt`.

3. Refresh incomplete existing publications:

   ```bash
   bibreview --config bibreview.yml refresh
   bibreview --config bibreview.yml merge
   ```

   Refresh and collection share `collected.json`, so refresh staging is merged
   before collecting new DOI values.

4. Collect pending new/recovered DOI values, then merge them:

   ```bash
   bibreview --config bibreview.yml collect
   bibreview --config bibreview.yml merge
   ```

5. Review author identities:

   ```bash
   bibreview --config bibreview.yml authors
   ```

   Apply only unambiguous additions when appropriate:

   ```bash
   bibreview --config bibreview.yml authors --apply-safe
   ```

   Review any remaining ambiguous cases manually in
   `docs/assets/data/author_mappings.json`.

6. Render the complete generated site surface:

   ```bash
   bibreview --config bibreview.yml render
   ```

   Rendering performs no provider/network fallback. Every canonical publication
   must already have its tracked BibTeX file. Unused BibTeX files are reported,
   not moved or deleted.

For a read-only preview of any supported mutation, use the global
`--dry-run` option, for example:

```bash
bibreview --config bibreview.yml --dry-run render
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
bibreview --config bibreview.yml arxiv
```

The scheduled GitHub workflow runs this command and changes only
`docs/data/arxiv.json`. If the cache changes, the workflow opens or updates a
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

- exact BibReview v1.0.0 installation;
- BibReview configuration validation;
- canonical merge no-op state;
- author mapping consistency;
- full `bibreview render` reconciliation;
- clean tracked tree after rendering;
- JavaScript syntax for the canonical bibliography search;
- complete Jekyll build;
- displayed canonical bibliography update date;
- clean tracked tree after the build.

There is no separate PHRAISE bibliographic Python engine: reusable
bibliographic behavior belongs in BibReview.
