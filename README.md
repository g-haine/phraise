# PHRAISE
Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy

The project **PHRAISE** aims at regrouping the research works on the port-Hamiltonian framework for the modelling, the discretization and the control of physical systems.

## To contribute

Contributions are welcome in the form of **DOI submissions**. You can:
- Submit a **pull request** with new DOIs in the `newDOI.txt` file on the project's [**GitHub repository**](https://github.com/g-haine/phraise).
- Send [**an email**](mailto:ghislain.haine@isae.fr) with new DOIs list.

## To update

You need API keys for Scopus and Springer.

- 1- ./getData.sh newDOI.sh
- 2- ./setAuthorMapping.sh
- 3- Correction of biblio.json entries <-> ./setAuthorMapping.sh
- 4- Add new name variations or new entry to author_mappings.json
- 5- Concatenate biblio.json with the old one (the backup is done at assets/data/biblio-{date}.json)
- 6- Concatenate newDOI.txt within DOI.txt, then newDOI.txt should be freed
- 7- ./setPosts.sh (potential need for another correction of biblio.json entries)
- 8- ./setPages.sh (potential need for another correction of biblio.json entries)
- 9- bundle exec jekyll serve --watch (for verification of the building process, last corrections)
- 10- commit & push !
- 11- verify if it deploys correctly on github pages
