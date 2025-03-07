---
layout: post
title: "Dual field structure-preserving discretization of port-Hamiltonian systems using finite element exterior calculus"
date: 2022-09-16 00:00:00 +0100
permalink: dual-field-structure-preserving-discretization-of-port-hamiltonian-systems-using-finite-element-exterior-calculus
year: 2022
authors: Andrea Brugnoli, Ramy Rashad, Stefano Stramigioli
category: articles
tags:
  - Port-Hamiltonian systems
  - Structure preserving discretization
  - Finite element exterior calculus
  - de Rham complex
  - Dual field representation
---
 
## Authors
[Andrea Brugnoli](authors/andrea_brugnoli), [Ramy Rashad](authors/ramy_rashad), [Stefano Stramigioli](authors/stefano_stramigioli)
 
## Abstract
In this paper we propose a novel approach to discretize linear port-Hamiltonian systems while preserving the underlying structure. We present a finite element exterior calculus formulation that is able to mimetically represent conservation laws and cope with mixed open boundary conditions using a single computational mesh. The possibility of including open boundary conditions allows for modular composition of complex multi-physical systems whereas the exterior calculus formulation provides a coordinate-free treatment. Our approach relies on a dual-field representation of the physical system that is redundant at the continuous level but eliminates the need of mimicking the Hodge star operator at the discrete level. By considering the Stokes-Dirac structure representing the system together with its adjoint, which embeds the metric information directly in the codifferential, the need for an explicit discrete Hodge star is avoided altogether. By imposing the boundary conditions in a strong manner, the power balance characterizing the Stokes-Dirac structure is then retrieved at the discrete level via symplectic Runge-Kutta integrators based on Gauss-Legendre collocation points. Numerical experiments validate the convergence of the method and the conservation properties in terms of energy balance both for the wave and Maxwell equations in a three dimensional domain. For the latter example, the magnetic and electric fields preserve their divergence free nature at the discrete level.
 
## Keywords
Port-Hamiltonian systems; Structure preserving discretization; Finite element exterior calculus; de Rham complex; Dual field representation
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2022
- **Volume:** 471
- **Issue:** 
- **Pages:** 111601
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2022.111601](https://doi.org/10.1016/j.jcp.2022.111601)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Brugnoli_2022,
  title={{Dual field structure-preserving discretization of port-Hamiltonian systems using finite element exterior calculus}},
  volume={471},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2022.111601},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Brugnoli, Andrea and Rashad, Ramy and Stramigioli, Stefano},
  year={2022},
  pages={111601}
}
{% endraw %}
{% endhighlight %}
 
## References
- [Maschke, B. M. & van der Schaft, A. J. PORT-CONTROLLED HAMILTONIAN SYSTEMS: MODELLING ORIGINS AND SYSTEMTHEORETIC PROPERTIES. Nonlinear Control Systems Design 1992 359–365 (1993) doi:10.1016/b978-0-08-041901-5.50064-6](port-controlled-hamiltonian-systems-modelling-origins-and-systemtheoretic-properties-93) -- [10.1016/B978-0-08-041901-5.50064-6](https://doi.org/10.1016/B978-0-08-041901-5.50064-6)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3)
- [Courant, T. J. Dirac manifolds. Transactions of the American Mathematical Society vol. 319 631–661 (1990)](dirac-manifolds) -- [10.1090/S0002-9947-1990-0998124-1](https://doi.org/10.1090/S0002-9947-1990-0998124-1)
- [Le Gorrec, Y., Zwart, H. & Maschke, B. Dirac structures and Boundary Control Systems associated with Skew-Symmetric Differential Operators. SIAM Journal on Control and Optimization vol. 44 1864–1892 (2005)](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- [Skrepek, N. Well-posedness of linear first order port-Hamiltonian Systems on multidimensional spatial domains. Evolution Equations &amp; Control Theory vol. 10 965 (2021)](well-posedness-of-linear-first-order-port-hamiltonian-systems-on-multidimensional-spatial-domains) -- [10.3934/eect.2020098](https://doi.org/10.3934/eect.2020098)
- [Jacob, B., Kaiser, J. T. & Zwart, H. Riesz Bases of Port-Hamiltonian Systems. SIAM Journal on Control and Optimization vol. 59 4646–4665 (2021)](riesz-bases-of-port-hamiltonian-systems) -- [10.1137/20M1366216](https://doi.org/10.1137/20M1366216)
- [Ramirez, H., Le Gorrec, Y., Macchelli, A. & Zwart, H. Exponential Stabilization of Boundary Controlled Port-Hamiltonian Systems With Dynamic Feedback. IEEE Transactions on Automatic Control vol. 59 2849–2855 (2014)](exponential-stabilization-of-boundary-controlled-port-hamiltonian-systems-with-dynamic-feedback) -- [10.1109/TAC.2014.2315754](https://doi.org/10.1109/TAC.2014.2315754)
- [Augner, B. & Jacob, B. Stability and stabilization of infinite-dimensional linear port-Hamiltonian systems. Evolution Equations &amp; Control Theory vol. 3 207–229 (2014)](stability-and-stabilization-of-infinite-dimensional-linear-port-hamiltonian-systems) -- [10.3934/eect.2014.3.207](https://doi.org/10.3934/eect.2014.3.207)
- [Cervera, J., van der Schaft, A. J. & Baños, A. Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica vol. 43 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Pommier-Budinger, V. A port-Hamiltonian model of liquid sloshing in moving containers and application to a fluid-structure system. Journal of Fluids and Structures vol. 69 402–427 (2017)](a-port-hamiltonian-model-of-liquid-sloshing-in-moving-containers-and-application-to-a-fluid-structure-system) -- [10.1016/j.jfluidstructs.2016.12.007](https://doi.org/10.1016/j.jfluidstructs.2016.12.007)
- [Altmann, R. & Schulze, P. A port-Hamiltonian formulation of the Navier–Stokes equations for reactive flows. Systems &amp; Control Letters vol. 100 51–55 (2017)](a-port-hamiltonian-formulation-of-the-navier-stokes-equations-for-reactive-flows) -- [10.1016/j.sysconle.2016.12.005](https://doi.org/10.1016/j.sysconle.2016.12.005)
- [Califano, F., Rashad, R., Schuller, F. P. & Stramigioli, S. Geometric and energy-aware decomposition of the Navier–Stokes equations: A port-Hamiltonian approach. Physics of Fluids vol. 33 (2021)](geometric-and-energy-aware-decomposition-of-the-navier-stokes-equations-a-port-hamiltonian-approach) -- [10.1063/5.0048359](https://doi.org/10.1063/5.0048359)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. A Port-Hamiltonian formulation of linear thermoelasticity and its mixed finite element discretization. Journal of Thermal Stresses vol. 44 643–661 (2021)](a-port-hamiltonian-formulation-of-linear-thermoelasticity-and-its-mixed-finite-element-discretization) -- [10.1080/01495739.2021.1917322](https://doi.org/10.1080/01495739.2021.1917322)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Arnold, D. N., Falk, R. S. & Winther, R. Finite element exterior calculus, homological techniques, and applications. Acta Numerica vol. 15 1–155 (2006) -- [10.1017/S0962492906210018](https://doi.org/10.1017/S0962492906210018)
- [Moulla, R., Lefévre, L. & Maschke, B. Pseudo-spectral methods for the spatial symplectic reduction of open systems of conservation laws. Journal of Computational Physics vol. 231 1272–1292 (2012)](pseudo-spectral-methods-for-the-spatial-symplectic-reduction-of-open-systems-of-conservation-laws) -- [10.1016/j.jcp.2011.10.008](https://doi.org/10.1016/j.jcp.2011.10.008)
- [Trenchant, V., Ramirez, H., Le Gorrec, Y. & Kotyczka, P. Finite differences on staggered grids preserving the port-Hamiltonian structure with application to an acoustic duct. Journal of Computational Physics vol. 373 673–697 (2018)](finite-differences-on-staggered-grids-preserving-the-port-hamiltonian-structure-with-application-to-an-acoustic-duct) -- [10.1016/j.jcp.2018.06.051](https://doi.org/10.1016/j.jcp.2018.06.051)
- [Seslija, M., Scherpen, J. M. A. & van der Schaft, A. Explicit simplicial discretization of distributed-parameter port-Hamiltonian systems. Automatica vol. 50 369–377 (2014)](explicit-simplicial-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.11.020](https://doi.org/10.1016/j.automatica.2013.11.020)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics vol. 361 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Hiptmair, R. Discrete Hodge operators. Numerische Mathematik vol. 90 265–289 (2001) -- [10.1007/s002110100295](https://doi.org/10.1007/s002110100295)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information vol. 38 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Palha, A., Rebelo, P. P., Hiemstra, R., Kreeft, J. & Gerritsma, M. Physics-compatible discretization techniques on single and dual grids, with application to the Poisson equation of volume forms. Journal of Computational Physics vol. 257 1394–1422 (2014) -- [10.1016/j.jcp.2013.08.005](https://doi.org/10.1016/j.jcp.2013.08.005)
- Rathgeber, F. et al. Firedrake. ACM Transactions on Mathematical Software vol. 43 1–27 (2016) -- [10.1145/2998441](https://doi.org/10.1145/2998441)
- [Iftime, O. V., Roman, M. & Sandovici, A. A Kernel Representation of Dirac Structures for Infinite-dimensional Systems. Mathematical Modelling of Natural Phenomena vol. 9 295–308 (2014)](a-kernel-representation-of-dirac-structures-for-infinite-dimensional-systems) -- [10.1051/mmnp/20149520](https://doi.org/10.1051/mmnp/20149520)
- Arnold, D. N. & Lee, J. J. Mixed Methods for Elastodynamics with Weak Symmetry. SIAM Journal on Numerical Analysis vol. 52 2743–2769 (2014) -- [10.1137/13095032X](https://doi.org/10.1137/13095032X)
- Anees, A. & Angermann, L. Time Domain Finite Element Method for Maxwell’s Equations. IEEE Access vol. 7 63852–63867 (2019) -- [10.1109/ACCESS.2019.2916394](https://doi.org/10.1109/ACCESS.2019.2916394)
- [Beattie, C., Mehrmann, V., Xu, H. & Zwart, H. Linear port-Hamiltonian descriptor systems. Mathematics of Control, Signals, and Systems vol. 30 (2018)](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- [Altmann, R., Mehrmann, V. & Unger, B. Port-Hamiltonian formulations of poroelastic network models. Mathematical and Computer Modelling of Dynamical Systems vol. 27 429–452 (2021)](port-hamiltonian-formulations-of-poroelastic-network-models) -- [10.1080/13873954.2021.1975137](https://doi.org/10.1080/13873954.2021.1975137)
- Sanz-Serna, J. M. Symplectic integrators for Hamiltonian problems: an overview. Acta Numerica vol. 1 243–286 (1992) -- [10.1017/S0962492900002282](https://doi.org/10.1017/S0962492900002282)
- [Kotyczka, P. & Lefèvre, L. Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters vol. 133 104530 (2019)](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- Wu, Y. & Bai, Y. Error Analysis of Energy-Preserving Mixed Finite Element Methods for the Hodge Wave Equation. SIAM Journal on Numerical Analysis vol. 59 1433–1454 (2021) -- [10.1137/19M1307950](https://doi.org/10.1137/19M1307950)
- [Payen, G., Matignon, D. & Haine, G. Modelling and structure-preserving discretization of Maxwell’s equations as port-Hamiltonian system. IFAC-PapersOnLine vol. 53 7581–7586 (2020)](modelling-and-structure-preserving-discretization-of-maxwell-s-equations-as-port-hamiltonian-system) -- [10.1016/j.ifacol.2020.12.1355](https://doi.org/10.1016/j.ifacol.2020.12.1355)
- Jain, V., Zhang, Y., Palha, A. & Gerritsma, M. Construction and application of algebraic dual polynomial representations for finite element methods on quadrilateral and hexahedral meshes. Computers &amp; Mathematics with Applications vol. 95 101–142 (2021) -- [10.1016/j.camwa.2020.09.022](https://doi.org/10.1016/j.camwa.2020.09.022)
- Buffa, A., Costabel, M. & Sheen, D. On traces for H(curl,Ω) in Lipschitz domains. Journal of Mathematical Analysis and Applications vol. 276 845–867 (2002) -- [10.1016/S0022-247X(02)00455-9](https://doi.org/10.1016/S0022-247X(02)00455-9)

