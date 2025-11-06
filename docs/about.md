---
layout: page
title: About
permalink: /about/
---

This site is a **bibliographic survey** dedicated to research on **port-Hamiltonian systems**. The goal is to provide a **collection of papers** to help researchers stay informed about the latest advancements, identify potential research gaps, and foster collaborations.

The site is **updated at regular intervals** to reflect newly published works.

## **How to Contribute?**
Contributions are welcome in the form of **DOI submissions**. You can:
- Submit a **pull request** with new DOIs in the `newDOI.txt` file on the project's [**GitHub repository**](https://github.com/g-haine/phraise).
- Send [**an email**](mailto:ghislain.haine@isae.fr?subject=%5BPHRAISE%5D) with a list of new DOIs.

**Automated contributions are not possible** due to API rate limitations. The metadata compilation will be manually performed before each update, but the site itself is automatically rebuilt with [Jekyll](https://jekyllrb.com/) after each push.

## **Scope & Methodology**

### **Why DOIs?**
Maintaining a large database manually is challenging. To ensure a sustainable and (almost) automated process, we **restrict** this survey to **published works with a DOI**. This guarantees easy updates and avoids manually managing metadata.

While the scripts used for collecting metadata are **publicly available** on the [**GitHub repository**](https://github.com/g-haine/phraise), they will primarily be run by the site maintainer.

### **Data Sources**
The metadata is retrieved using a hierarchical approach using the following APIs:  
1. [**CrossRef**](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) & [**DOI Foundation**](https://www.doi.org/doi-handbook/HTML/doi-rest-api.html): primary sources, ensuring completeness of minimal metadata;  
2. [**Scopus**](https://dev.elsevier.com/documentation/SCOPUSSearchAPI.wadl): for abstracts and keywords, when available via Elsevier;  
3. [**Springer Meta API**](https://dev.springernature.com/docs/api-endpoints/meta-api/): for abstracts and keywords from Springer;  
4. [**IEEE Xplore API**](https://developer.ieee.org/docs): for abstracts and keywords from IEEE;  
5. [**Mendeley**](https://api.mendeley.com/apidocs/openapi) & [**Semantic Scholar**](https://www.semanticscholar.org/product/api): as fallback sources for missing abstracts.

Currently, **only metadata and abstracts** are collected: **full texts are not included**.

The resulting database is [available for download]({{ site.baseurl }}/assets/data/biblio.json) (a JSON file).

### **arXiv**
To stay as up to date as possible, we use the [arXiv API](https://info.arxiv.org/help/api/user-manual.html) to retrieve the latest preprints related to port-Hamiltonian systems.

However, since these preprints have not been peer-reviewed or officially published, they do not have DOIs registered in **CrossRef**. For this reason, **arXiv** entries are displayed on a separate page. These entries are dynamically fetched and are not part of the **PHRAISE** internal database. As a result, they are not included in the [search tool]({{ site.baseurl }}/search/).

### **Handling Author's names**
The [Author pages]({{ site.baseurl }}/authors/) need a management to take care of the different ways an author can appear in a publication. We use the [OpenAlex API](https://docs.openalex.org/how-to-use-the-api/api-overview) to minimize the task. Nevertheless, this can be a source of errors, so please do not hesitate to [suggest corrections](mailto:ghislain.haine@isae.fr?subject=%5BPHRAISE%5D). You may want to take a look at [the array managing name variations]({{ site.baseurl }}/assets/data/author_mappings.json) (a JSON file).

### **Curation Process**
No additional **peer review** is conducted; the survey relies on **CrossRef's metadata**, assuming that all indexed works have already undergone editorial scrutiny.

## **Useful Links**

### Community

- [**PHSys**](https://www.phsys.eu): Community website for researchers in **port-Hamiltonian Systems** (PHS).
- [**PH-Seminar**](https://www.fan.uni-wuppertal.de/en/research/ph-seminar/): Monthly seminar, usually first Wednesday, 4 pm (CET) via Zoom.
- [**EMS-TAG on PHS**](https://ems-phs.uni-wuppertal.de/en/): A thematic activity group related to PHS.
- [**French-Dutch-German Doctoral College**](https://www.epc.ed.tum.de/en/rt/cdfa-phs/): “Port-Hamiltonian Systems: Modeling, Numerics and Control” supported by the Franco-Bavarian University Cooperation Center BayFrance, coordinated by P. Kotyczka, B. Maschke and J. Scherpen.

### Softwares

- [**SCRIMP**](https://g-haine.github.io/scrimp/): A finite element framework for **port-Hamiltonian PDE simulations**.
- [**EPHS**](https://markuslohmayer.github.io/EPHS.jl/dev/): A compositional, energy-based (software) framework for modeling mechanical, electromagnetic, and thermodynamic systems in [Julia](http://julialang.org/).
- [**port-Hamiltonian Benchmark**](https://algopaul.github.io/PortHamiltonianBenchmarkSystems/): A repository collecting various port-Hamiltonian systems for numerical benchmarking.
- [**PyPHS**](https://pyphs.github.io/pyphs/): A Python software (Py) dedicated to the simulation of multi-physical Port-Hamiltonian Systems (PHS) described by graph structures.

## **GDPR Policy**
Cookies are small text files stored by your web browser when visiting websites. We have chosen not to use any cookies or tracking technologies on this website.

However, to better understand how the site is used and to improve its content, we collect anonymous traffic statistics using [GoatCounter](https://www.goatcounter.com/), a privacy-friendly analytics tool that does not use cookies.
