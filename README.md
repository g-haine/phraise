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

PHRAISE pins **BibReview v1.7.2** for reproducible maintenance and CI.

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

The publication search uses [Pagefind](https://pagefind.app/). Its fully static
index is generated after the Jekyll build in `site/_site/pagefind/`; it is a
deployment artifact, never a tracked source file. Only rendered publication
pages are indexed, so author, category, year, and arXiv listing pages do not
pollute publication search results. CI pins Pagefind to `1.5.2`.


## Monthly bibliography update — 10 steps

This is the **repeatable monthly checklist** for maintaining PHRAISE. Work from
the **repository root**, not from `site/`. Replace `2026-11` below with the
month being updated. The commands assume **BibReview v1.7.2**, installed by
`phraise.yml`; use the detailed BibReview documentation only for unusual cases.

Do **not** run `bibreview init` on this existing bibliography. No separate
`audit`, `references`, `refresh`, `backfill` or `hygiene` campaign is
necessary just to add this month's publications.

### 1. Sync, create a branch, and activate the environment

~~~bash
git switch main
git pull --ff-only
git status --short
git switch -c maintenance/2026-11
conda activate phraise
bibreview --version
~~~

**Stop if the working tree is not clean** before creating the branch. After a
BibReview version change, run `bash install.sh` before `conda activate
phraise` to update the pinned Conda environment. Expect `bibreview 1.7.2`.

### 2. Check project health and provider access

~~~bash
bibreview validate
bibreview status
bibreview providers --check
~~~

Address configuration or provider errors before continuing; a temporary API
failure is not a reason to reject a publication.

### 3. Discover new publications

~~~bash
bibreview --dry-run discover
bibreview discover
~~~

Candidates enter `data/newID.txt` (accepted for collection),
`data/checkID.txt` (human relevance review), or `data/badID.txt`
(rejected). Discovery does not change canonical publications.

### 4. Make the relevance decisions

~~~bash
bibreview --dry-run review
bibreview review
~~~

For each candidate, choose **KEEP**, **REJECT** or **defer**. The interactive
reviewer displays the publication evidence and saves each decision; no Python
snippet or manual movement between the DOI queue files is needed. If there is
nothing to review, continue.

### 5. Collect accepted records

~~~bash
bibreview --dry-run collect
bibreview collect
bibreview status
~~~

Collection writes **staging**, not the canonical bibliography. A provider
error or structurally incomplete record can remain pending without blocking
other valid publications.

### 6. Inspect staging, then explicitly merge

~~~bash
git status --short
git diff --stat
git diff -- data/collected.json
bibreview --dry-run merge
bibreview merge
~~~

**Before running the real merge**, inspect the planned added/updated counts,
the staged publication metadata in `data/collected.json`, and the relevant
tracked BibTeX changes in `bib/`. Stop and resolve unexpected results.
`merge` is the *only* step here that promotes staged publications to the
canonical `data/bibliography.json`.

### 7. Resolve author identities

~~~bash
bibreview authors
bibreview authors --apply-safe
bibreview authors --review
bibreview authors
~~~

The safe pass handles unambiguous names. Use the interactive reviewer for
remaining identities (merge with an existing identity, create a new identity,
or defer). There is no need to edit `data/author_mappings.json` directly.

### 8. Regenerate the website

~~~bash
bibreview --dry-run render
bibreview render
bibreview --dry-run render
~~~

Review the resulting changes. The second dry-run should report no remaining
rendering differences. The website's canonical bibliography update date changes
only when an effective merge changed the bibliography.

### 9. Check the diff and optionally preview the site

~~~bash
git diff --check
git status --short
git diff --stat
~~~

Inspect changed publication pages, BibTeX and any generated files. For a local
preview (optional for a routine update; recommended when presentation changes):

~~~bash
cd site
bundle exec jekyll build
npx --yes pagefind@1.5.2 --site _site
bundle exec jekyll serve --no-watch
~~~

Visit `http://127.0.0.1:4000/phraise/`; stop the server with Ctrl+C and
return to the repository root using `cd ..`.

### 10. Commit and open a pull request

After reviewing the changed files (and only those files):

~~~bash
git add data/ bib/ site/
git diff --cached --check
git diff --cached --stat
git commit -m "Update PHRAISE bibliography (2026-11)"
git push -u origin maintenance/2026-11
~~~

Open a **PR to `main`**, inspect its final diff and wait for **BibReview
integration** CI to pass; the maintainer performs the final **squash & merge**.
Do not push bibliographic changes directly to `main`.

**If no new publications were found:** a no-op merge/render is normal. There is
no need to create an empty monthly PR.

**Exceptional case — missing contributor metadata:** if `collect` leaves a
candidate pending because the provider has no usable author/editor, first
finish any already staged merge (step 6; `repair` requires empty staging), then
run:

~~~bash
bibreview --dry-run repair
bibreview repair
bibreview --dry-run merge
bibreview merge
~~~

Inspect the repaired staging before merging, then repeat author reconciliation
and rendering. Repairs are explicit human decisions, never provider guesses.

### DOI-less additions (when needed)

A publication without a DOI is **not** processed by `discover`. For each
reviewed DOI-less addition, initialize and complete an evidence manifest:

~~~bash
bibreview import --init publication.yml
# Complete publication.yml from authoritative sources (including reviewed BibTeX).
bibreview --dry-run import publication.yml
bibreview import publication.yml
bibreview --dry-run merge
bibreview merge
~~~

Inspect its staging, BibTeX and `data/imports/` evidence before merging; then
repeat steps 7–10 above. Do not invent a DOI.

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
- the complete Jekyll build;
- deterministic Pagefind index generation after the Jekyll build;
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
bundle exec jekyll build
npx --yes pagefind@1.5.2 --site _site
bundle exec jekyll serve --no-watch
~~~

Then open <http://127.0.0.1:4000/phraise/>.

Run the Pagefind command again after rebuilding the site. The deployment
workflow performs both build steps automatically.

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
