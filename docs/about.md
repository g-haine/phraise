---
layout: page
title: About
permalink: /about/
---

This site is a **bibliographic survey** dedicated to research on **port-Hamiltonian systems**. Its goal is to provide a curated collection of publications that helps researchers follow developments in the field, identify potential research gaps, and discover related work.

The canonical bibliography is updated through reviewed maintenance cycles. A separate **arXiv cache** is refreshed automatically on a schedule so that recent preprints can be displayed without becoming part of the canonical bibliography.

## **Powered by BibReview**

PHRAISE is powered by [**BibReview**](https://github.com/g-haine/bibreview), an open-source, human-reviewed bibliographic engine for reproducible literature-review websites. BibReview manages the generic bibliographic workflow, provider integration, canonical metadata, contributor identities, audit/review tools, and deterministic generation of publication, author, and year pages. PHRAISE remains responsible for the **port-Hamiltonian scope**, scientific curation, project configuration, and Jekyll presentation.

## **How to Contribute?**

Contributions are welcome in the form of **DOI submissions**. You can:

- Submit a **pull request** adding new DOI values to `docs/newDOI.txt` on the project's [**GitHub repository**](https://github.com/g-haine/phraise).
- Send [**an email**](mailto:ghislain.haine@isae.fr?subject=%5BPHRAISE%5D) with a list of new DOI values or a metadata correction.

Canonical bibliography changes are not merged automatically. Provider metadata, relevance decisions, and ambiguous contributor identities remain reviewable, and repository changes reach the production `main` branch through pull requests.

## **Scope & Methodology**

### **Why DOIs?**

At present, the canonical PHRAISE bibliography is deliberately restricted to **published works with a DOI**. A DOI provides a stable identity key and makes provider-based collection, reconciliation, and reproducible updates practical. Provider metadata is nevertheless treated as evidence rather than unquestionable truth and may be corrected after review.

The PHRAISE project configuration is publicly available on the [**GitHub repository**](https://github.com/g-haine/phraise), while the generic bibliographic engine is maintained separately in the [**BibReview repository**](https://github.com/g-haine/bibreview).

### **Data Sources**

PHRAISE uses several external services for different purposes rather than relying on a single strict provider hierarchy:

1. [**OpenAlex**](https://docs.openalex.org/how-to-use-the-api/api-overview) is used to discover DOI-backed candidate publications, provides independent comparison evidence during bibliography audits, and can supply an abstract when publisher/CrossRef enrichment leaves that field empty.
2. [**CrossRef**](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) is the core metadata source for DOI-backed collection and also contributes independent audit evidence.
3. Publisher APIs from [**Elsevier / Scopus**](https://dev.elsevier.com/), [**Springer Nature**](https://dev.springernature.com/) and [**IEEE Xplore**](https://developer.ieee.org/) can enrich records with information such as abstracts, keywords, or event metadata when available.
4. [**Semantic Scholar**](https://www.semanticscholar.org/product/api) and [**Mendeley**](https://dev.mendeley.com/) also provide optional abstract fallback enrichment when configured. BibReview cleans fallback candidates before comparing them and retains the longest valid abstract available from OpenAlex, Semantic Scholar, or Mendeley. Semantic Scholar also contributes independent evidence to the audit workflow.
5. DOI content negotiation is used for citation and BibTeX retrieval when available.

Provider output is never assumed to be infallible. BibReview keeps canonical data, staging, BibTeX, and audit evidence inspectable so that corrections can be reviewed before publication.

PHRAISE stores bibliographic metadata, abstracts, keywords and related citation information when available; **full texts are not collected**.

The canonical database is [available for download]({{ site.baseurl }}/assets/data/bibliography.json) as JSON.

### **arXiv**

The [arXiv API](https://info.arxiv.org/help/api/user-manual.html) is used by BibReview's optional arXiv module to maintain a small display-only cache of recent preprints related to port-Hamiltonian systems.

The browser does **not** query arXiv dynamically. A scheduled GitHub Actions workflow refreshes the cache, opens or updates a dedicated pull request when the cache changes, validates that change through the PHRAISE integration workflow, and only then merges it. The published arXiv page therefore reads a static JSON cache from [`assets/data/arxiv.json`]({{ site.baseurl }}/assets/data/arxiv.json).

arXiv entries remain separate from the canonical DOI bibliography. They are not converted automatically into canonical publications, do not change the canonical bibliography update date, and are not included in the [search tool]({{ site.baseurl }}/search/).

### **Handling Authors' Names**

The [Author pages]({{ site.baseurl }}/authors/) need reviewed mappings because the same person can appear under several source-visible name variants.

BibReview compares canonical author names with the reviewed mapping file and can apply only **safe, unambiguous proposals** automatically. Possible identity collisions remain under manual review rather than being guessed. You can inspect the [author-name mapping]({{ site.baseurl }}/assets/data/author_mappings.json) and [suggest corrections](mailto:ghislain.haine@isae.fr?subject=%5BPHRAISE%5D) when needed.

### **Curation Process**

PHRAISE does not perform an additional scientific peer review of the works it lists. Inclusion means that a work matches the bibliographic scope of the survey; it is not an endorsement of its results.

Bibliographic metadata is curated separately from scientific content. New records pass through explicit staging and merge steps, ambiguous author identities remain human-reviewed, and historical metadata can be audited against independent evidence from CrossRef, OpenAlex, and Semantic Scholar before reviewed corrections are promoted to the canonical database. Audit history is retained locally so routine audits do not repeatedly request publications already visited; a deliberate full audit can still be run when fresh evidence is required for the entire bibliography.

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
