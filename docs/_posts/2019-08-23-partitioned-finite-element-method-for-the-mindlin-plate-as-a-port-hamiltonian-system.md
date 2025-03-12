---
layout: post
title: "Partitioned Finite Element Method for the Mindlin Plate as a Port-Hamiltonian system"
date: 2019-08-23 00:00:00 +0100
permalink: partitioned-finite-element-method-for-the-mindlin-plate-as-a-port-hamiltonian-system
year: 2019
authors: Andrea Brugnoli, Daniel Alazard, Valérie Pommier-Budinger, Denis Matignon
category: proceedings
tags:
  - Port-Hamiltonian systems (pHs)
  - Geometric Discretization
  - Mindlin-Reissner Plate
  - Partitioned Finite Element Method (PFEM)
  - Symplectic Integration
---
 
## Authors
[Andrea Brugnoli](authors/andrea-brugnoli), [Daniel Alazard](authors/daniel-alazard), [Valérie Pommier-Budinger](authors/valerie-pommier-budinger), [Denis Matignon](authors/denis-matignon)
 
## Abstract
The port-Hamiltonian framework allows for a structured representation and interconnection of distributed parameter systems described by Partial Differential Equations (PDE) from different realms. Here, the Mindlin-Reissner model of a thick plate is presented in a tensorial formulation. Taking into account collocated boundary control and observation gives rise to an infinite-dimensional port-Hamiltonian system (pHs). The Partitioned Finite Element Method (PFEM), already presented in our previous work, allows obtaining a structure-preserving finite-dimensional port-Hamiltonian system, and accounting for boundary control in a straightforward manner. In order to illustrate the flexibility of PFEM, both types of boundary controls can be dealt with: either through forces and momenta, or through kinematic variables. The discrete model is easily implementable by using the FEniCS platform. Computation of eigenfrequencies and vibration modes, together with time-domain simulation results demonstrate the consistency of the proposed approach.
 
## Keywords
Port-Hamiltonian systems (pHs); Geometric Discretization; Mindlin-Reissner Plate; Partitioned Finite Element Method (PFEM); Symplectic Integration
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2019
- **Volume:** 52
- **Issue:** 2
- **Pages:** 88--95
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2019.08.016](https://doi.org/10.1016/j.ifacol.2019.08.016)
- **Note:** 3rd IFAC Workshop on Control of Systems Governed by Partial Differential Equations CPDE 2019- Oaxaca, Mexico, 20–24 May 2019
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Brugnoli_2019,
  title={{Partitioned Finite Element Method for the Mindlin Plate as a Port-Hamiltonian system}},
  volume={52},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2019.08.016},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Brugnoli, Andrea and Alazard, Daniel and Pommier-Budinger, Valérie and Matignon, Denis},
  year={2019},
  pages={88--95}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/partitioned-finite-element-method-for-the-mindlin-plate-as-a-port-hamiltonian-system.bib)
 
## References
- [Beattie, C., Mehrmann, V., Xu, H. & Zwart, H. Linear port-Hamiltonian descriptor systems. Mathematics of Control, Signals, and Systems vol. 30 (2018)](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Applied Mathematical Modelling vol. 75 940–960 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- Dawe, D. J. & Roufaeil, O. L. Rayleigh-Ritz vibration analysis of Mindlin plates. Journal of Sound and Vibration vol. 69 345–359 (1980) -- [10.1016/0022-460x(80)90477-0](https://doi.org/10.1016/0022-460x(80)90477-0)
- Duindam, (2009)
- Durán, R., Hervella-Nieto, L., Liberman, E., Hervella-Nieto, L. & Solomin, J. Approximation of the vibration modes of a plate by Reissner-Mindlin equations. Mathematics of Computation vol. 68 1447–1463 (1999) -- [10.1090/s0025-5718-99-01094-7](https://doi.org/10.1090/s0025-5718-99-01094-7)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Grinfeld, (2015)
- Huang, H. C. & Hinton, E. A nine node Lagrangian Mindlin plate element with enhanced shear interpolation. Engineering Computations vol. 1 369–379 (1984) -- [10.1108/eb023593](https://doi.org/10.1108/eb023593)
- Jacob, (2012)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics vol. 361 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- Kurula, Linear wave systems on n-d spatial domains. International Journal of Control (2015)
- Logg, (2012)
- Mindlin, R. D. Influence of Rotatory Inertia and Shear on Flexural Motions of Isotropic, Elastic Plates. Journal of Applied Mechanics vol. 18 31–38 (1951) -- [10.1115/1.4010217](https://doi.org/10.1115/1.4010217)
- [Moulla, R., Lefévre, L. & Maschke, B. Pseudo-spectral methods for the spatial symplectic reduction of open systems of conservation laws. Journal of Computational Physics vol. 231 1272–1292 (2012)](pseudo-spectral-methods-for-the-spatial-symplectic-reduction-of-open-systems-of-conservation-laws) -- [10.1016/j.jcp.2011.10.008](https://doi.org/10.1016/j.jcp.2011.10.008)
- [Seslija, M., van der Schaft, A. & Scherpen, J. M. A. Discrete exterior geometry approach to structure-preserving discretization of distributed-parameter port-Hamiltonian systems. Journal of Geometry and Physics vol. 62 1509–1531 (2012)](discrete-exterior-geometry-approach-to-structure-preserving-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.geomphys.2012.02.006](https://doi.org/10.1016/j.geomphys.2012.02.006)
- [Trenchant, V., Ramirez, H., Le Gorrec, Y. & Kotyczka, P. Finite differences on staggered grids preserving the port-Hamiltonian structure with application to an acoustic duct. Journal of Computational Physics vol. 373 673–697 (2018)](finite-differences-on-staggered-grids-preserving-the-port-hamiltonian-structure-with-application-to-an-acoustic-duct) -- [10.1016/j.jcp.2018.06.051](https://doi.org/10.1016/j.jcp.2018.06.051)
- van der Schaft, Port-Hamiltonian differential-algebraic systems. (2013)

