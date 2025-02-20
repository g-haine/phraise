---
layout: page
title: About
permalink: /about/
---

This site is a **bibliographic survey** dedicated to research on **port-Hamiltonian systems**. The goal is to provide an **exhaustive collection of papers** to help researchers stay informed about the latest advancements, identify potential research gaps, and foster collaborations.

The site is **automatically updated** at regular intervals to reflect newly published works.

## **Scope & Methodology**

### **Why DOIs?**
Maintaining a large database manually is challenging. To ensure a sustainable and automated process, we **restrict** this survey to **published works with a DOI**. This guarantees easy updates and avoids manually managing metadata.

While the scripts used for collecting metadata are **publicly available**, they will primarily be run by the site maintainer.

### **Data Sources**
The metadata is retrieved using a hierarchical approach:
1. **CrossRef** (primary source, ensuring completeness of minimal metadata)
2. **Scopus** (for abstracts and keywords, when available via Elsevier)
3. **Springer Metadata API** (for abstracts and keywords from Springer)
4. **OpenAlex & Semantic Scholar** (as fallback sources for missing abstracts and keywords)

Currently, **only metadata and abstracts** are collected—**full texts are not included**.

## **How to Contribute?**
Contributions are welcome in the form of **DOI submissions**. You can:
- Submit a **pull request** with new DOIs in the `DOI.txt` file on the project's [GitHub repository](https://github.com/g-haine/phraise).
- Send an email to the site maintainer.

**Automated contributions are not possible** due to API rate limitations. The metadata compilation will be manually performed before each update, but the site itself is automatically rebuilt with Jekyll after each push.

### **Curation Process**
No additional **peer review** is conducted—the survey relies on **CrossRef's metadata**, assuming that all indexed works have already undergone editorial scrutiny.

## **Useful Links**
- [**PHSys**](https://www.phsys.eu): Community website for researchers in **port-Hamiltonian Systems** (PHS).
- **EMS-TAG on PHS**: A thematic activity group related to PHS (link to be added).
- **Franco-German School on PHS**: Dedicated research & training program (link to be added).
- **SCRIMP**: A finite element framework for **port-Hamiltonian PDE simulations** (link to be added).
- **port-Hamiltonian Benchmark**: A repository collecting various port-Hamiltonian systems for numerical benchmarking (link to be added).
- **Software by Antoine Falaize**: A software suite for **finite-dimensional PHS modeling** (additional details to be added).
