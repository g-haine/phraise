# PHRAISE
Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy

PHRAISE gathers research material related to the port-Hamiltonian framework for modelling, discretizing and controlling physical systems.

## Contributing new DOIs

We welcome contributions in the form of **DOI submissions**:

- Open a pull request that adds the references to `docs/newDOI.txt` in the [GitHub repository](https://github.com/g-haine/phraise).
- Alternatively, send the new DOIs by [email](mailto:ghislain.haine@isae.fr).

## Updating the website

The metadata adapters use API keys for Scopus, Springer, IEEE and optionally
Mendeley. `bibreview.yml` explicitly points BibReview at `docs/.env`, so the
same local secret file is used by both the remaining PHRAISE adapter and the
BibReview CLI. Once you have the keys available, save them in `.env` in the
`docs` folder as follows:
```
MAIL=your-email@example.fr
SCOPUS_API_KEY=
SPRINGER_API_KEY=
IEEE_API_KEY=
MENDELEY_API_KEY=
```
Install the Python maintenance environment from the repository root first:

```bash
bash install.sh
conda activate phraise
```

The installer creates or updates the `phraise` environment from `phraise.yml`.
It does not activate or deactivate environments, change shell configuration, or
install Conda itself. On systems without Bash, use `conda env create -f
phraise.yml` once, then `conda env update -n phraise -f phraise.yml` for updates.
Python 3.12, Requests, Beautiful Soup, Unidecode and python-dotenv are installed
from conda-forge. The maintenance environment also installs the pinned BibReview
engine used for site modeling, rendering and generated-artifact persistence.
Ruby, Bundler and Jekyll remain separate website dependencies.

`.env` uses plain `KEY=value` assignments (optional quotes), not executable shell
code. Existing environment variables take precedence. Publisher keys are needed
only when the corresponding provider is queried. Mendeley is an optional abstract
fallback; `OPENALEX_API_KEY` may also be supplied for OpenAlex. Local author/page
rendering and concatenation need no API keys.

On the `bibreview-migration` branch, the effective maintenance path is now
fully canonical through discovery, refresh, collection, merge and site writing:

1. `bibreview --config ../bibreview.yml discover` – query OpenAlex, verify
   candidates, and update `newDOI.txt`, `checkDOI.txt` and `badDOI.txt`
   according to the policy in `bibreview.yml`.
2. Review `checkDOI.txt` and move each manually classified DOI to
   `newDOI.txt` or `badDOI.txt`.
3. `bibreview --config ../bibreview.yml refresh` – detect incomplete existing
   journal records whose BibTeX is missing or changed and stage refreshed
   canonical publications in `assets/data/collected.json`.
4. `bibreview --config ../bibreview.yml merge` – merge any refresh staging
   before collecting new DOI values. This is a safe no-op when refresh staged
   nothing.
5. `python getData.py newDOI.txt` – collect pending new/recovered DOI metadata
   and BibTeX into canonical `assets/data/collected.json` staging.
6. `bibreview --config ../bibreview.yml merge` – merge the collection batch,
   update DOI state, and clear staging.
7. `bibreview --config ../bibreview.yml authors` – inspect author identities.
8. `bibreview --config ../bibreview.yml authors --apply-safe` – add only
   unambiguous mappings, then review any remaining cases in
   `assets/data/author_mappings.json` and rerun the previous command.
9. `python setPosts.py && python setPages.py` – render and persist the site from
   canonical bibliography state.
10. `bundle exec jekyll serve --watch` – verify the build locally and make final
    corrections.
11. Commit and push the changes, then confirm the GitHub Pages deployment.

The former `looking4Update.py` entry point has been removed. Its historical
engine remains only as a regression oracle in `phraise_tools.update`.
`concatenate.py` and `setAuthorMapping.py` are likewise legacy migration
oracles rather than effective workflow steps.

## Local development

The static website that showcases the PHRAISE publications lives in the `docs/`
folder and is built with [Jekyll](https://jekyllrb.com/). To preview the site or
validate content changes locally:

1. Install Ruby (version 3.0 or newer is recommended) and [Bundler](https://bundler.io/).
2. Install the site dependencies:

   ```bash
   cd docs
   bundle install
   ```

3. Serve the website with live reloading:

   ```bash
   bundle exec jekyll serve --watch
   ```

4. Open <http://127.0.0.1:4000> in your browser to review the generated pages.

When you are finished, stop the server with `Ctrl+C`. Running the site locally
is especially helpful after adding new DOIs to make sure the generated posts and
pages render correctly before publishing them.

### Legacy bibliography concatenation oracle (Python 3.12)

`concatenate.py` is retained during the BibReview migration for regression
comparison only; it is not the effective merge step on `bibreview-migration`.
Use `bibreview --config bibreview.yml merge` from the repository root, or
`bibreview --config ../bibreview.yml merge` from `docs/`, for canonical
project state.

`python docs/concatenate.py` still works from the repository root. No Python
packages, API keys or `.env` are needed for this step. Use `--root DIR` for a
separate data directory; `--doi`, `--new-doi`, `--bad-doi`, `--biblio` and
`--backup-dir` override paths relative to that root (absolute paths also work).
Run `python docs/concatenate.py --help` for details.

The newest backup by modification time is merged first, so its record wins
when a DOI occurs twice. Records are sorted by DOI. Historical exact-line
filtering is preserved, including the former workflow's different handling of
comments, blank lines and an unterminated final line in `badDOI.txt` for JSON
and DOI text.
Missing/null DOI keys form one group; other non-string DOI values are rejected.
An entirely filtered DOI list is accepted as a valid result.

All inputs are checked and all outputs staged before replacement. Each file is
replaced atomically, with `newDOI.txt` cleared last. This is not a multi-file
transaction: an interruption during replacement may leave a partial update.
Keep the backup and avoid concurrent runs.

Run the tests from the repository root:

```bash
python3 -m unittest discover -s docs/tests -v
```

The tests use synthetic inputs and retained reference outputs. They never modify
the production bibliography or call external services.

### Python maintenance architecture and validation

| Command | Responsibility |
|---|---|
| `bibreview ... discover` | OpenAlex discovery, CrossRef verification, relevance screening and DOI queue updates |
| `bibreview ... refresh` | Canonical refresh staging for incomplete existing publications with missing/changed BibTeX |
| `getData.py newDOI.txt` | Canonical BibReview collection into `collected.json`, using PHRAISE's current HTTP adapters |
| `bibreview ... merge` | Authoritative merge from canonical staging into `bibliography.json` |
| `bibreview ... authors` | Canonical author mapping analysis and safe additions |
| `setAuthorMapping.py` | Legacy author-mapping oracle retained during migration |
| `concatenate.py` | Legacy merge oracle retained during migration |
| `setPosts.py` | BibReview-rendered publication posts; PHRAISE missing-BibTeX acquisition, orphan archival and last-update date |
| `setPages.py` | BibReview-rendered author/year pages and indexes |

All commands default to the directory containing the scripts, regardless of the
working directory. For example, `python docs/getData.py newDOI.txt` from the
repository root and `python getData.py newDOI.txt` from `docs/` are equivalent.
Use `--root /path/to/copy` to work on an isolated data tree. DOI input paths are
relative to that root unless absolute. `discovery.max_pages` in `bibreview.yml` controls the OpenAlex discovery
limit (currently 20), keeping provider policy in project configuration rather
than command-line source code.

Every command reports its main stages by default. Add `-v` to see each DOI or
generated file and `-vv` to include sanitized HTTP diagnostics (operation, host,
redirect and status, without URLs, queries, headers or API keys). Use `--quiet`
for automation: success and progress output are suppressed, while warnings and
errors remain visible. For `setAuthorMapping.py --json`, the requested JSON is
still written to standard output when `--quiet` is used.

Use `--dry-run` with any maintenance command to validate inputs, perform the
normal lookups and compute its complete result without writing, archiving or
deleting files. The summary starts with `Dry run:` and progress messages use
“Would …” for planned mutations. Network commands still make their normal HTTP
requests, so a simulation can consume provider quota and report API errors.

`setAuthorMapping.py` proposes a new identity automatically only when its slug
is unique and no known author shares its normalized surname and first initial.
`--apply-safe` writes those proposals atomically and leaves collisions and
possible variants in the report for manual review. The operation is idempotent.
Use `--json` when a structured report is more convenient.

`docs/phraise_tools/` now contains the narrow PHRAISE adapters still required
during migration plus legacy non-regression oracles. Discovery and refresh are
owned directly by BibReview. `phraise_tools.site` is the narrow PHRAISE
adapter to BibReview: it supplies PHRAISE's Jekyll presentation policy and
delegates canonical site modeling, rendering, reconciliation planning and
generated-file persistence to BibReview. `setPosts.py` and `setPages.py`
read `assets/data/bibliography.json` directly and do not consume
`assets/data/biblio.json`. The historical PHRAISE renderers remain only as
migration non-regression oracles. JSON is parsed once per input directly.
Generation is deterministic and runs sequentially, so failures propagate reliably. The maintenance workflow requires no Bash, curl, jq, GNU sed
or iconv. `install.sh` is the only retained Bash helper. Existing permalinks and
mapping keys are kept.
New slugs use Unidecode instead of the platform-dependent iconv transliteration;
non-Latin names may therefore produce different new suggestions.

The tests cover a complete simulated workflow, HTTP failures and provider field
extraction, pagination, BibTeX, references, publication types and validation
before writes. Retained reference outputs preserve the behavior established by
the former workflow. External responses are mocked; no credentials or production
data are changed. The installer is tested with a Conda stub for
create/update/failure and paths with spaces. The complete Python workflow and
the Jekyll build have also been validated with the real bibliography.

Intentional corrections beyond successful-input parity:

- Empty update sets succeed, and collection with no new DOI leaves the database
  untouched. HTTP/network errors abort instead of marking a DOI as bad; a 404
  remains an absent result. Requests have timeouts and bounded retries.
  Diagnostics distinguish HTTP status, timeout, TLS, connection and redirect
  errors without displaying API keys. DOI lookups identify the operation and
  DOI, plus the responding host after redirection. During publisher discovery
  only, a redirected landing page returning 401/403 can still identify the
  publisher API; metadata and BibTeX errors remain fatal, except for the optional
  Semantic Scholar abstract fallback: after HTTP 429 exhausts the retries, it
  emits one warning and is skipped for the rest of that command. Mendeley is
  still tried when configured; otherwise the abstract may remain unavailable.
  A new command invocation tries Semantic Scholar again. Likewise, a Mendeley
  catalog HTTP 401 emits one warning and disables that optional provider for
  the current command, preserving any Semantic Scholar abstract already found.
  Check `MENDELEY_API_KEY` before a future run to restore Mendeley enrichment;
  the warning does not mean its authentication has been repaired.
- Inputs and generated content are prepared before file replacement. Invalid
  authors, ambiguous mappings, dates and output paths produce explicit errors.
  Old pages are removed only after successful generation. Writes remain atomic
  per file, not a transaction across the whole workflow; do not run concurrent
  maintenance commands.
- Unknown-author suggestions are a valid JSON object, with colliding suggestions
  grouped under their slug. Review and merge the suggestions manually rather
  than replacing the mapping file with the command output.
- Empty publisher fields do not erase usable CrossRef metadata. JSON/YAML/HTML
  quoting is handled explicitly so quotation marks and special characters do
  not corrupt generated files.
- The historical update oracle removed stale records before recollection. The
  effective BibReview refresh path deliberately no longer does so: the
  authoritative publication remains in `bibliography.json`, a refreshed copy
  is staged in `collected.json`, changed BibTeX is backed up, and the later
  merge preserves the persistent UUID. DOI state repair for orphaned known DOI
  values is handled without deleting canonical publications.
- Existing archived data and conflicting BibTeX backups are preserved. Backup
  timestamps use file names valid on Windows as well as Unix.
