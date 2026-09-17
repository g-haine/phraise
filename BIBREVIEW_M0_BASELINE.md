# M0 — PHRAISE baseline before BibReview extraction

This document freezes the functional PHRAISE reference used before extracting the generic bibliographic engine into **BibReview**.

The purpose of M0 is not to redesign PHRAISE. It is to define a stable point of comparison so that later extraction work can be checked against known behaviour.

## Reference state

- Repository: `g-haine/phraise`
- Reference date: 2026-09-17
- Reference commit: `8c0682301016ac14156c63569ee6f1b5a2169421`
- Frozen reference branch: `baseline/pre-bibreview-extraction`
- Default development branch: `main`

The frozen branch must remain unchanged during the BibReview extraction. Ongoing bibliography and arXiv cache updates continue on `main`.

At the reference commit, GitHub Pages completed its build and deployment successfully. The latest recorded full maintenance validation before M0 was performed for PR #15 (2026-09-11): 65 unit tests passed, the complete workflow was run against the real bibliography, and the Jekyll site was generated successfully.

## Current responsibilities

PHRAISE currently contains both the bibliographic engine and its port-Hamiltonian-specific website.

The maintenance pipeline is split as follows:

| Command | Current responsibility |
|---|---|
| `docs/looking4Update.py` | Discover candidate publications, verify DOIs, and queue incomplete records |
| `docs/getData.py` | Collect CrossRef metadata and enrich it with publisher/reference/BibTeX data |
| `docs/setAuthorMapping.py` | Analyse author identities, apply safe mappings, and report ambiguous cases |
| `docs/concatenate.py` | Merge bibliography data, backups, new DOIs, and exclusions |
| `docs/setPosts.py` | Generate publication posts and maintain generated publication content |
| `docs/setPages.py` | Generate author/year pages and indexes |
| `.github/scripts/update_arxiv.py` | Refresh the independent arXiv cache used by the website |
| Jekyll under `docs/` | Build the PHRAISE GitHub Pages website |

Shared Python maintenance code lives under `docs/phraise_tools/`.

## Python environment

The maintenance environment is defined by `phraise.yml` and currently uses Python 3.12 with:

- Requests
- urllib3
- Beautiful Soup
- Unidecode
- python-dotenv

Create or update it from the repository root with:

```bash
bash install.sh
conda activate phraise
```

Ruby, Bundler and Jekyll are separate website dependencies and are not installed by `install.sh`.

## Deterministic validation contract

These checks must remain available throughout the BibReview extraction and should be run before accepting a migration step.

From the repository root:

```bash
python -m compileall -q docs/*.py docs/phraise_tools docs/tests
python -m unittest discover -s docs/tests -v
```

The unit tests use synthetic fixtures and mocked external responses. They must not modify the production bibliography or require API credentials.

For the website:

```bash
cd docs
bundle install
bundle exec jekyll build
```

A successful Jekyll build is the minimum site-level regression check.

## Real maintenance workflow

The current operator workflow remains the functional reference:

```text
1. python looking4Update.py
2. review checkDOI.txt and classify entries
3. python getData.py newDOI.txt
4. python setAuthorMapping.py
5. python setAuthorMapping.py --apply-safe
6. python concatenate.py
7. python setPosts.py && python setPages.py
8. bundle exec jekyll serve --watch
9. review, commit and push
10. confirm GitHub Pages deployment
```

The network-facing commands depend on external services, credentials, quotas and provider availability. They are therefore part of functional validation but are **not** deterministic baseline tests.

## Dry-run contract

Every maintenance command supports `--dry-run`. Dry runs must preserve the production tree byte-for-byte while still validating inputs and computing planned changes.

Network commands still perform their normal HTTP requests during a dry run. A dry run can therefore consume provider quota and can fail because of an external service.

## Baseline data boundaries

The following are part of the PHRAISE reference state and must not be silently reinterpreted during extraction:

- `docs/DOI.txt` — canonical DOI list used by the current workflow
- `docs/newDOI.txt` — queue of new DOI records
- `docs/badDOI.txt` — excluded DOI records
- `docs/assets/data/biblio.json` — canonical bibliography database used by generation code
- `docs/assets/data/author_mappings.json` — author identity mapping data
- `docs/_posts/` — generated publication pages
- `docs/authors/` and `docs/years/` — generated navigation pages
- `docs/data/arxiv.json` — independently refreshed arXiv cache

These files do not all have to keep the same location in BibReview, but their current semantics must be understood before migration.

## Reproducibility limits

M0 deliberately records the current system rather than pretending it is fully reproducible in isolation.

- API credentials are intentionally not stored in the repository.
- Publisher and discovery services can change, rate-limit or fail.
- The arXiv cache is refreshed automatically on `main`, so `main` is a moving content target.
- The frozen baseline branch is the immutable comparison point for extraction work.
- The current Ruby dependencies are resolved through the existing `docs/Gemfile`; there is no requirement in M0 to redesign or modernize the website toolchain.

## M0 acceptance criteria

M0 is complete when all of the following are true:

- [x] A precise reference commit has been selected.
- [x] A frozen baseline branch points to that commit.
- [x] The current maintenance responsibilities are documented.
- [x] The Python and Jekyll validation commands are documented.
- [x] Deterministic tests are distinguished from network-dependent validation.
- [x] The current data boundaries are documented.
- [x] A successful GitHub Pages deployment exists for the reference commit.
- [ ] The deterministic Python tests are rerun locally from the frozen reference and the result is recorded here.
- [ ] The Jekyll build is rerun locally from the frozen reference and the result is recorded here.

Once the two local validation results are recorded, M0 can be closed and M1 — the extraction audit — can begin.
