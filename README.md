# PHRAISE
Port-Hamiltonian Representation and Approximation of Interconnected Systems using Energy

The project **PHRAISE** aims at regrouping the research works on the port-Hamiltonian framework for the modelling, the discretization and the control of physical systems.

## To contribute

Contributions are welcome in the form of **DOI submissions**. You can:
- Submit a **pull request** with new DOIs in the `newDOI.txt` file on the project's [**GitHub repository**](https://github.com/g-haine/phraise).
- Send [**an email**](mailto:ghislain.haine@isae.fr) with new DOIs list.

## To update

You need API keys for Scopus and Springer.

- 0- ./looking4Update.sh (to update, *e.g.*, volume, issue, etc., and fetch last CrossRef entries)
- 1- ./getData.sh newDOI.txt
- 2- ./setAuthorMapping.sh <-> Correction of biblio.json entries
- 3- Add new name variations or new entry to author_mappings.json
- 4- ./concatenate.sh
- 5- ./setPosts.sh
- 6- ./setPages.sh
- 7- bundle exec jekyll serve --watch (for verification of the building process, last corrections)
- 8- commit & push !
- 9- verify if it deploys correctly on github pages
