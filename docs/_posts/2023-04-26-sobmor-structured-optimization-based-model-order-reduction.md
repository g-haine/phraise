---
title: "SOBMOR: Structured Optimization-Based Model Order Reduction"
date: 2023-04-26 00:00:00 +0100
permalink: sobmor-structured-optimization-based-model-order-reduction
year: 2023
authors: Paul Schwerdtner, Matthias Voigt
category: articles
---
 
## Authors
[Paul Schwerdtner](authors/paul-schwerdtner), [Matthias Voigt](authors/matthias-voigt)
 
## Abstract
Model order reduction (MOR) methods that are designed to preserve structural features of a given full order model (FOM) often suffer from a lower accuracy when compared to their non-structure-preserving counterparts. In this paper, we present a framework for structure-preserving MOR, which allows to compute structured reduced order models (ROMs) with a much higher accuracy. The framework is based on parameter optimization, i.e., the elements of the system matrices of the ROM are iteratively varied to minimize an objective functional that measures the difference between the FOM and the ROM. The structural constraints can be encoded in the parametrization of the ROM. The method only depends on frequency response data and can thus be applied to a wide range of dynamical systems. We illustrate the effectiveness of our method on a port-Hamiltonian and on a symmetric second-order system in a comparison with other structure-preserving MOR algorithms.
 
## Citation
- **Journal:** SIAM Journal on Scientific Computing
- **Year:** 2023
- **Volume:** 45
- **Issue:** 2
- **Pages:** A502--A529
- **Publisher:** Society for Industrial & Applied Mathematics (SIAM)
- **DOI:** [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Schwerdtner_2023,
  title={{SOBMOR: Structured Optimization-Based Model Order Reduction}},
  volume={45},
  ISSN={1095-7197},
  DOI={10.1137/20m1380235},
  number={2},
  journal={SIAM Journal on Scientific Computing},
  publisher={Society for Industrial & Applied Mathematics (SIAM)},
  author={Schwerdtner, Paul and Voigt, Matthias},
  year={2023},
  pages={A502--A529}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/sobmor-structured-optimization-based-model-order-reduction.bib)
 
## References
- Aliyev, N., Benner, P., Mengi, E., Schwerdtner, P. & Voigt, M. Large-Scale Computation of $\mathcal{L}_\infty$-Norms by a Greedy Subspace Method. SIAM Journal on Matrix Analysis and Applications vol. 38 1496–1516 (2017) -- [10.1137/16m1086200](https://doi.org/10.1137/16m1086200)
- Antoulas, A. C. Approximation of Large-Scale Dynamical Systems. (2005) doi:10.1137/1.9780898718713 -- [10.1137/1.9780898718713](https://doi.org/10.1137/1.9780898718713)
- Antoulas, A. C., Beattie, C. A. & Güğercin, S. Interpolatory Methods for Model Reduction. (Society for Industrial and Applied Mathematics, 2020). doi:10.1137/1.9781611976083 -- [10.1137/1.9781611976083](https://doi.org/10.1137/1.9781611976083)
- Bai, Z. & Su, Y. Dimension Reduction of Large-Scale Second-Order Dynamical Systems via a Second-Order Arnoldi Method. SIAM Journal on Scientific Computing vol. 26 1692–1709 (2005) -- [10.1137/040605552](https://doi.org/10.1137/040605552)
- Beddig, R. S. et al. Model Reduction for Second‐Order Dynamical Systems Revisited. PAMM vol. 19 (2019) -- [10.1002/pamm.201900224](https://doi.org/10.1002/pamm.201900224)
- Benner, P., Kürschner, P. & Saak, J. An improved numerical method for balanced truncation for symmetric second-order systems. Mathematical and Computer Modelling of Dynamical Systems vol. 19 593–615 (2013) -- [10.1080/13873954.2013.794363](https://doi.org/10.1080/13873954.2013.794363)
- Benner, P., Sima, V. & Voigt, M. &lt;formula formulatype="inline"&gt;&lt;tex Notation="TeX"&gt;${