# PHRAISE
Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy

PHRAISE gathers research material related to the port-Hamiltonian framework for modelling, discretizing and controlling physical systems.

## Contributing new DOIs

We welcome contributions in the form of **DOI submissions**:

- Open a pull request that adds the references to `docs/newDOI.txt` in the [GitHub repository](https://github.com/g-haine/phraise).
- Alternatively, send the new DOIs by [email](mailto:ghislain.haine@isae.fr).

## Updating the website

The maintenance scripts rely on API keys for Scopus and Springer. Once you have the keys available, run the following workflow from the `docs` directory:

1. `./looking4Update.sh` – update metadata (volume, issue, etc.) and fetch the latest CrossRef entries.
2. `./getData.sh newDOI.txt`
3. `./setAuthorMapping.sh` – correct `biblio.json` entries as needed.
4. Add new name variations or entries to `assets/data/author_mappings.json`.
5. `./concatenate.sh`
6. `./setPosts.sh`
7. `./setPages.sh`
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
