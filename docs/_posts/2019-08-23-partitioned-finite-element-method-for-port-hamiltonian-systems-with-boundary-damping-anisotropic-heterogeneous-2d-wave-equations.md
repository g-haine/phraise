---
layout: post
title: "Partitioned Finite Element Method for port-Hamiltonian systems with Boundary Damping: Anisotropic Heterogeneous 2D wave equations"
date: 2019-08-23 00:00:00 +0100
permalink: partitioned-finite-element-method-for-port-hamiltonian-systems-with-boundary-damping-anisotropic-heterogeneous-2d-wave-equations
year: 2019
authors: Anass Serhani, Denis Matignon, Ghislain Haine
category: proceedings
tags:
  - Port-Hamiltonian systems (pHs)
  - distributed-parameter system (DPS)
  - structure preserving discretization
  - partitioned finite element method (PFEM)
  - boundary damping
---
 
## Authors
[Anass Serhani](authors/anass-serhani), [Denis Matignon](authors/denis-matignon), [Ghislain Haine](authors/ghislain-haine)
 
## Abstract
A 2D wave equation with boundary damping of impedance type can be recast into an infinite-dimensional port-Hamiltonian system (pHs) with an appropriate feedback law, where the structure operator J is formally skew-symmetric. It is known that the underlying semigroup proves dissipative, even though no dissipation operator R is to be found in the pHs model. The Partitioned Finite Element Method (PFEM) introduced in Cardoso-Ribeiro et al. (2018), is structure-preserving and provides a natural way to discretize such systems. It gives rise to a non null symmetric matrix R. Moreover, since this matrix accounts for boundary damping, its rank is very low: only the basis functions at the boundary have an influence. Lastly, this matrix can be factorized out when considering the boundary condition as a feedback law for the pHs, involving the impedance parameter. Note that pHs - as open system - is used here as a tool to accurately discretize the wave equation with boundary damping as a closed system. In the worked-out numerical examples in 2D, the isotropic and homogeneous case is presented and the influence of the impedance is assessed; then, an anisotropic and heterogeneous wave equation with space-varying impedance at the boundary is investigated.
 
## Keywords
Port-Hamiltonian systems (pHs); distributed-parameter system (DPS); structure preserving discretization; partitioned finite element method (PFEM); boundary damping
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2019
- **Volume:** 52
- **Issue:** 2
- **Pages:** 96--101
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2019.08.017](https://doi.org/10.1016/j.ifacol.2019.08.017)
- **Note:** 3rd IFAC Workshop on Control of Systems Governed by Partial Differential Equations CPDE 2019- Oaxaca, Mexico, 20–24 May 2019
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Serhani_2019,
  title={{Partitioned Finite Element Method for port-Hamiltonian systems with Boundary Damping: Anisotropic Heterogeneous 2D wave equations}},
  volume={52},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2019.08.017},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Serhani, Anass and Matignon, Denis and Haine, Ghislain},
  year={2019},
  pages={96--101}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/partitioned-finite-element-method-for-port-hamiltonian-systems-with-boundary-damping-anisotropic-heterogeneous-2d-wave-equations.bib)
 
## References
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A structure-preserving Partitioned Finite Element Method for the 2D wave equation. IFAC-PapersOnLine vol. 51 119–124 (2018)](a-structure-preserving-partitioned-finite-element-method-for-the-2d-wave-equation) -- [10.1016/j.ifacol.2018.06.033](https://doi.org/10.1016/j.ifacol.2018.06.033)
- Cowsar, L. C., Dupont, T. F. & Wheeler, M. F. A Priori Estimates for Mixed Finite Element Approximations of Second-Order Hyperbolic Equations with Absorbing Boundary Conditions. SIAM Journal on Numerical Analysis vol. 33 492–504 (1996) -- [10.1137/0733026](https://doi.org/10.1137/0733026)
- Duindam, (2009)
- [Egger, H., Kugler, T., Liljegren-Sailer, B., Marheineke, N. & Mehrmann, V. On Structure-Preserving Model Reduction for Damped Wave Propagation in Transport Networks. SIAM Journal on Scientific Computing vol. 40 A331–A365 (2018)](on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks) -- [10.1137/17m1125303](https://doi.org/10.1137/17m1125303)
- Engquist, B. & Majda, A. Absorbing boundary conditions for the numerical simulation of waves. Mathematics of Computation vol. 31 629–651 (1977) -- [10.1090/s0025-5718-1977-0436612-4](https://doi.org/10.1090/s0025-5718-1977-0436612-4)
- [Farle, O., Klis, D., Jochum, M., Floch, O. & Dyczij-Edlinger, R. A port-hamiltonian finite-element formulation for the maxwell equations. 2013 International Conference on Electromagnetics in Advanced Applications (ICEAA) 324–327 (2013) doi:10.1109/iceaa.2013.6632246](a-port-hamiltonian-finite-element-formulation-for-the-maxwell-equations) -- [10.1109/iceaa.2013.6632246](https://doi.org/10.1109/iceaa.2013.6632246)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Jacob, (2012)
- Kergomard, J., Debut, V. & Matignon, D. Resonance modes in a one-dimensional medium with two purely resistive boundaries: Calculation methods, orthogonality, and completeness. The Journal of the Acoustical Society of America vol. 119 1356–1367 (2006) -- [10.1121/1.2166709](https://doi.org/10.1121/1.2166709)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics vol. 361 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- Kurula, Linear wave systems on n-D spatial domains. International Journal of Control (2015)
- [Le Gorrec, Y. & Matignon, D. Coupling between hyperbolic and diffusive systems: A port-Hamiltonian formulation. European Journal of Control vol. 19 505–512 (2013)](coupling-between-hyperbolic-and-diffusive-systems-a-port-hamiltonian-formulation) -- [10.1016/j.ejcon.2013.09.003](https://doi.org/10.1016/j.ejcon.2013.09.003)
- [Matignon, D. & Hélie, T. A class of damping models preserving eigenspaces for linear conservative port-Hamiltonian systems. European Journal of Control vol. 19 486–494 (2013)](a-class-of-damping-models-preserving-eigenspaces-for-linear-conservative-port-hamiltonian-systems) -- [10.1016/j.ejcon.2013.10.003](https://doi.org/10.1016/j.ejcon.2013.10.003)
- Monteghetti, F., Matignon, D. & Piot, E. Energy analysis and discretization of nonlinear impedance boundary conditions for the time-domain linearized Euler equations. Journal of Computational Physics vol. 375 393–426 (2018) -- [10.1016/j.jcp.2018.08.037](https://doi.org/10.1016/j.jcp.2018.08.037)
- [Moulla, R., Lefévre, L. & Maschke, B. Pseudo-spectral methods for the spatial symplectic reduction of open systems of conservation laws. Journal of Computational Physics vol. 231 1272–1292 (2012)](pseudo-spectral-methods-for-the-spatial-symplectic-reduction-of-open-systems-of-conservation-laws) -- [10.1016/j.jcp.2011.10.008](https://doi.org/10.1016/j.jcp.2011.10.008)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- [Villegas, J. A., Zwart, H., Le Gorrec, Y. & Maschke, B. Exponential Stability of a Class of Boundary Control Systems. IEEE Transactions on Automatic Control vol. 54 142–147 (2009)](exponential-stability-of-a-class-of-boundary-control-systems) -- [10.1109/tac.2008.2007176](https://doi.org/10.1109/tac.2008.2007176)

