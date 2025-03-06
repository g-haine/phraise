---
layout: post
title: "From discrete modeling to explicit FE models for port-Hamiltonian systems of conservation laws"
date: 2022-11-23 00:00:00 +0100
permalink: from-discrete-modeling-to-explicit-fe-models-for-port-hamiltonian-systems-of-conservation-laws
year: 2022
authors: Paul Kotyczka, Tobias Thoma
category:
  - proceedings
tags:
  - port-hamiltonian systems
  - conservation laws
  - exterior calculus
  - non-uniform boundary conditions
  - structure-preserving discretization
  - mixed finite elements
  - weak form
---
 
## Authors
[Paul Kotyczka](authors/paul_kotyczka), [Tobias Thoma](authors/tobias_thoma)
 
## Abstract
Mixed finite element (FE) approaches have proven very useful for the structure-preserving discretization of port-Hamiltonian (PH) distributed parameter systems, but non-uniform boundary conditions (BCs) were treated in an implicit manner up to now. We apply our recent approach from structure mechanics, which relies on the weak imposition of both Neumann and Dirichlet BCs based on a suitable variational principle, to the class of PH systems of two conservation laws. We illustrate (a) starting with the integral conservation laws the transition to an exterior calculus representation suitable for FE approximation according to Farle et al. (2013). Based thereon, we show (b) the variational formulation with weakly imposed BCs of both types. We discuss (c) on a simple example on a quadrilateral mesh the structure and the variables of the resulting FE models compared to the equations derived from a direct discrete approach on dual cell complexes. We (d) provide the corresponding FEniCS code for download.
 
## Keywords
Port-Hamiltonian systems; conservation laws; exterior calculus; non-uniform boundary conditions; structure-preserving discretization; mixed finite elements; weak form
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2022
- **Volume:** 55
- **Issue:** 30
- **Pages:** 412--417
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2022.11.088](https://doi.org/10.1016/j.ifacol.2022.11.088)
- **Event:** 25th International Symposium on Mathematical Theory of Networks and Systems MTNS 2022- Bayreuth, Germany, September 12-16, 2022
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Kotyczka_2022,
  title={{From discrete modeling to explicit FE models for port-Hamiltonian systems of conservation laws}},
  volume={55},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2022.11.088},
  number={30},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Kotyczka, Paul and Thoma, Tobias},
  year={2022},
  pages={412--417}
}
{% endraw %}
{% endhighlight %}
 
## References
- [Argus, F. J., Bradley, C. P. & Hunter, P. J. Theory and Implementation of Coupled Port-Hamiltonian Continuum and Lumped Parameter Models. Journal of Elasticity vol. 145 339–382 (2021)](theory-and-implementation-of-coupled-port-hamiltonian-continuum-and-lumped-parameter-models) -- [10.1007/s10659-021-09846-4](https://doi.org/10.1007/s10659-021-09846-4)
- Arnold, D., Falk, R. & Winther, R. Finite element exterior calculus: from Hodge theory to numerical stability. Bulletin of the American Mathematical Society vol. 47 281–354 (2010) -- [10.1090/S0273-0979-10-01278-4](https://doi.org/10.1090/S0273-0979-10-01278-4)
- [Brugnoli, A., Cardoso-Ribeiro, F. L., Haine, G. & Kotyczka, P. Partitioned finite element method for structured discretization with mixed boundary conditions. IFAC-PapersOnLine vol. 53 7557–7562 (2020)](partitioned-finite-element-method-for-structured-discretization-with-mixed-boundary-conditions) -- [10.1016/j.ifacol.2020.12.1351](https://doi.org/10.1016/j.ifacol.2020.12.1351)
- [Brugnoli, A., Haine, G., Serhani, A. & Vasseur, X. Numerical Approximation of Port-Hamiltonian Systems for Hyperbolic or Parabolic PDEs with Boundary Control. Journal of Applied Mathematics and Physics vol. 09 1278–1321 (2021)](numerical-approximation-of-port-hamiltonian-systems-for-hyperbolic-or-parabolic-pdes-with-boundary-control) -- [10.4236/jamp.2021.96088](https://doi.org/10.4236/jamp.2021.96088)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information vol. 38 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Hiptmair, R. & Li, J. Shape derivatives in differential forms I: an intrinsic perspective. Annali di Matematica Pura ed Applicata vol. 192 1077–1098 (2012) -- [10.1007/s10231-012-0259-9](https://doi.org/10.1007/s10231-012-0259-9)
- Kotyczka, P. (2022). Explicit-PH-FE-Model-2CL.py. doi: 10.14459/2022mp1664162.
- [Kotyczka, P. & Maschke, B. Discrete port-Hamiltonian formulation and numerical approximation for systems of two conservation laws. at - Automatisierungstechnik vol. 65 308–322 (2017)](discrete-port-hamiltonian-formulation-and-numerical-approximation-for-systems-of-two-conservation-laws) -- [10.1515/auto-2016-0098](https://doi.org/10.1515/auto-2016-0098)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics vol. 361 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- Lu, K., Augarde, C. E., Coombs, W. M. & Hu, Z. Weak impositions of Dirichlet boundary conditions in solid mechanics: A critique of current approaches and extension to partially prescribed boundaries. Computer Methods in Applied Mechanics and Engineering vol. 348 632–659 (2019) -- [10.1016/j.cma.2019.01.035](https://doi.org/10.1016/j.cma.2019.01.035)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Scheuermann, T. M. et al. An Object-Oriented Library for Heat Transfer Modelling and Simulation in Open Cell Foams. IFAC-PapersOnLine vol. 53 7575–7580 (2020) -- [10.1016/j.ifacol.2020.12.1354](https://doi.org/10.1016/j.ifacol.2020.12.1354)
- [Seslija, M., Scherpen, J. M. A. & van der Schaft, A. Explicit simplicial discretization of distributed-parameter port-Hamiltonian systems. Automatica vol. 50 369–377 (2014)](explicit-simplicial-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.11.020](https://doi.org/10.1016/j.automatica.2013.11.020)
- [Trenchant, V., Ramirez, H., Le Gorrec, Y. & Kotyczka, P. Finite differences on staggered grids preserving the port-Hamiltonian structure with application to an acoustic duct. Journal of Computational Physics vol. 373 673–697 (2018)](finite-differences-on-staggered-grids-preserving-the-port-hamiltonian-structure-with-application-to-an-acoustic-duct) -- [10.1016/j.jcp.2018.06.051](https://doi.org/10.1016/j.jcp.2018.06.051)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3)

