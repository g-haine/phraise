# PHRAISE

**Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy**

PHRAISE is a curated bibliography of research on port-Hamiltonian systems.

The public site is available at
[https://g-haine.github.io/phraise/](https://g-haine.github.io/phraise/).

PHRAISE is powered by
[BibReview](https://github.com/g-haine/bibreview), which manages the generic
bibliographic workflow, review state, canonical data, BibTeX, and generated
Jekyll pages. PHRAISE itself contains the subject-specific configuration,
curated bibliography, and website presentation.

PHRAISE pins **BibReview v1.7.0** for reproducible maintenance and CI.

## Contributing a publication

Contributions are welcome for published work within the PHRAISE scope.

### Publication with a DOI

Either:

- open a pull request adding a typed `doi:<value>` line to
  `data/newID.txt`; or
- send the DOI to <ghislain.haine@isae.fr>.

The maintainer then uses the normal BibReview collection/review workflow before
anything becomes canonical.

### Publication without a DOI

Do **not** invent a DOI and do not place ISBN, arXiv, PMLR, or publisher IDs in
`data/newID.txt`.

Instead, provide:

- an official publication/source page when available;
- reviewed bibliographic metadata;
- reliable citation/BibTeX information.

BibReview's reviewed DOI-less import workflow stores provenance explicitly and
assigns a persistent internal UUID.

## Repository structure

The main project state is intentionally small and inspectable:

~~~text
bibreview.yml

data/
  bibliography.json
  collected.json
  author_mappings.json
  ID.txt
  newID.txt
  checkID.txt
  badID.txt
  imports/

bib/
audit/
archive/
site/
~~~

The important distinction is:

- `data/bibliography.json` — canonical reviewed bibliography;
- `data/collected.json` — temporary staging before merge;
- `data/ID.txt` — exactly one canonical identity token per publication;
- `data/newID.txt`, `checkID.txt`, `badID.txt` — DOI-only
  acquisition state;
- `data/imports/` — durable evidence for reviewed DOI-less imports;
- `bib/` — tracked canonical BibTeX;
- `audit/` — local/review campaign state;
- `site/` — Jekyll source and generated bibliographic presentation.

Generated public bibliography snapshots live under
`site/assets/data/bibreview/`; public BibTeX copies live under
`site/assets/bib/`. They are generated outputs, not merge inputs.

## Maintenance

Run commands from the repository root. `bibreview.yml` is discovered
automatically.

Validate the project and configured providers:

~~~bash
bibreview validate
bibreview status
bibreview providers --check
~~~

### Add DOI-backed publications

~~~bash
bibreview discover
# Review data/checkID.txt when needed.
bibreview collect
bibreview --dry-run merge
bibreview merge
~~~

Inspect `data/collected.json` and the BibTeX diff before merging.

### Add a DOI-less publication

~~~bash
bibreview import --init publication.yml
# Complete and review publication.yml from authoritative sources.
bibreview --dry-run import publication.yml
bibreview import publication.yml
bibreview --dry-run merge
bibreview merge
~~~

### Resolve contributor identities

~~~bash
bibreview authors
bibreview authors --apply-safe
bibreview authors
~~~

Resolve any remaining ambiguous cases manually in
`data/author_mappings.json`.

### Render the site

~~~bash
bibreview --dry-run render
bibreview render
~~~

Rendering is deterministic. In a clean canonical state, running
`bibreview render` should leave the tracked tree unchanged.

## Maintenance workflows

The normal update cycle above is intentionally separate from larger data-quality
campaigns.

BibReview also provides:

- `audit` — compare canonical publications with current provider evidence;
- `references` — review reconstructed reference lists;
- `refresh` — review safe fills for incomplete/stale records;
- `backfill` — enrich specific missing fields;
- `hygiene` — review historical structured-text/title/citation artifacts.

All of these preserve the same rule:

~~~text
provider/reconstructed evidence
        ↓
human or deterministic review
        ↓
collected.json
        ↓
explicit merge
        ↓
canonical bibliography
~~~

PHRAISE does not accept silent provider-driven canonical rewrites.

For the detailed behavior of these commands, see the
[BibReview documentation](https://github.com/g-haine/bibreview/tree/main/docs).

## Local environment

Create or update the Conda environment:

~~~bash
bash install.sh
conda activate phraise
~~~

The environment contains Python 3.12 and the exact BibReview release pinned by
`phraise.yml`.

Provider credentials stay local in `.env`. The expected variables are:

~~~text
SCOPUS_API_KEY=
SPRINGER_API_KEY=
IEEE_API_KEY=
OPENALEX_API_KEY=
SEMANTIC_SCHOLAR_API_KEY=
MENDELEY_CLIENT_ID=
MENDELEY_CLIENT_SECRET=
~~~

Values already exported in the process environment take precedence over dotenv
values.

Never commit `.env`.

## CI and deployment

`main` is the production branch.

The **BibReview integration** workflow checks, among other things:

- the exact pinned BibReview version;
- configuration validity;
- canonical merge no-op state;
- the one-token-per-publication `ID.txt` projection;
- author mapping consistency;
- deterministic rendering;
- JavaScript syntax;
- the complete Jekyll build;
- the displayed canonical bibliography date.

The GitHub Pages workflow rebuilds the public site from the reviewed project
state.

The optional scheduled arXiv workflow is deliberately separate from the
canonical bibliography. It may update only
`site/assets/data/arxiv.json`; semantic no-op refreshes do not create
timestamp-only churn.

## Local site preview

~~~bash
cd site
bundle install
bundle exec jekyll serve --watch
~~~

Then open <http://127.0.0.1:4000/phraise/>.

## Design boundary

PHRAISE should contain **no project-specific bibliographic Python engine**.

Reusable bibliography logic belongs in BibReview. PHRAISE should remain a clean
demonstrator consisting of:

- subject policy;
- reviewed canonical data;
- tracked BibTeX;
- Jekyll presentation;
- integration/deployment configuration.

This separation is what makes improvements tested on PHRAISE reusable by other
BibReview projects.
