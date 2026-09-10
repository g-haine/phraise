# PHRAISE
Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy

PHRAISE gathers research material related to the port-Hamiltonian framework for modelling, discretizing and controlling physical systems.

## Contributing new DOIs

We welcome contributions in the form of **DOI submissions**:

- Open a pull request that adds the references to `docs/newDOI.txt` in the [GitHub repository](https://github.com/g-haine/phraise).
- Alternatively, send the new DOIs by [email](mailto:ghislain.haine@isae.fr).

## Updating the website

The maintenance scripts rely on API keys for Scopus, Springer, IEEE and Mendeley. Once you have the keys available, save them in `.env` in the `docs` folder as follow:  
```
MAIL=your-email@example.fr
SCOPUS_API_KEY=
SPRINGER_API_KEY=
IEEE_API_KEY=
MENDELEY_API_KEY=
```
Then, run the following workflow from the `docs` directory:

1. `./looking4Update.sh` – update metadata (volume, issue, etc.) and fetch the latest CrossRef entries 
2. Check entries in checkDOI.txt and decide where they belong: bad/newDOI.txt
3. `./getData.sh newDOI.txt`
4. `./setAuthorMapping.sh` – correct `biblio.json` entries as needed.
5. Add new name variations or entries to `assets/data/author_mappings.json` – retry `./setAuthorMapping.sh` to check
6. `python3 concatenate.py`
7. `./setPosts.sh && ./setPages.sh`
8. `bundle exec jekyll serve --watch` – verify the build locally and make final corrections.
9. Commit and push the changes.
10. Confirm that the site deploys correctly on GitHub Pages.

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

### Bibliography concatenation (Python 3.9+)

`python3 docs/concatenate.py` also works from the repository root. No Python
packages, API keys or `.env` are needed for this step. Use `--root DIR` for a
separate data directory; `--doi`, `--new-doi`, `--bad-doi`, `--biblio` and
`--backup-dir` override paths relative to that root (absolute paths also work).
Run `python3 docs/concatenate.py --help` for details.

The newest backup by modification time is merged first, so its record wins
when a DOI occurs twice. Records are sorted by DOI. Historical exact-line
filtering is preserved, including the shell's different handling of comments,
blank lines and an unterminated final line in `badDOI.txt` for JSON and DOI text.
Missing/null DOI keys form one group; other non-string DOI values are rejected.
An entirely filtered DOI list now succeeds instead of failing at `grep`.

All inputs are checked and all outputs staged before replacement. Each file is
replaced atomically, with `newDOI.txt` cleared last. This is not a multi-file
transaction: an interruption during replacement may leave a partial update.
Keep the backup and avoid concurrent runs. The original `concatenate.sh` is
retained temporarily as a deprecated reference until a full live workflow has
been validated.

Run the tests from the repository root:

```bash
python3 -m unittest discover -s docs/tests -v
```

The shell parity tests additionally require Bash and jq; they use isolated
fixtures and never modify the production bibliography.
