---
layout: post
title: "Friedrichs' systems discretized with the DGM: domain decomposable model order reduction and Graph Neural Networks approximating vanishing viscosity solutions"
date: 2025-03-13 00:00:00 +0100
permalink: friedrichs-systems-discretized-with-the-dgm-domain-decomposable-model-order-reduction-and-graph-neural-networks-approximating-vanishing-viscosity-solutions
year: 2025
authors: Francesco Romor, Davide Torlo, Gianluigi Rozza
category: articles
tags:
  - Friedrichs' systems
  - Model order reduction
  - Graph neural networks
---
 
## Authors
[Francesco Romor](authors/francesco-romor), [Davide Torlo](authors/davide-torlo), [Gianluigi Rozza](authors/gianluigi-rozza)
 
## Abstract
Friedrichs' systems (FS) are symmetric positive linear systems of first-order partial differential equations (PDEs), which provide a unified framework for describing various elliptic, parabolic and hyperbolic semi-linear PDEs such as the linearized Euler equations of gas dynamics, the equations of compressible linear elasticity and the Dirac-Klein-Gordon system. FS were studied to approximate PDEs of mixed elliptic and hyperbolic type in the same domain. For this and other reasons, the discontinuous Galerkin method (DGM) represents the most common and versatile choice of approximation space for FS in the literature. We implement a distributed memory solver for stationary FS in deal.II. Our focus is model order reduction. Since FS model hyperbolic PDEs, they often suffer from a slow Kolmogorov n-width decay. We develop and combine two approaches to tackle this problem in the context of large-scale applications. The first is domain decomposable reduced-order models (DD-ROMs). We will show that the DGM offers a natural formulation of DD-ROMs, in particular regarding interface penalties, compared to the continuous finite element method. We also develop new repartitioning strategies to obtain more efficient local approximations of the solution manifold. The second approach involves shallow graph neural networks used to infer the limit of a succession of projection-based linear ROMs corresponding to lower viscosity constants: the heuristic behind concerns the development of a multi-fidelity super-resolution paradigm to mimic the mathematical convergence to vanishing viscosity solutions while exploiting to the most interpretable and certified projection-based DD-ROMs.
 
## Keywords
Friedrichs' systems; Model order reduction; Graph neural networks
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2025
- **Volume:** 531
- **Issue:** 
- **Pages:** 113915
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2025.113915](https://doi.org/10.1016/j.jcp.2025.113915)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Romor_2025,
  title={{Friedrichs’ systems discretized with the DGM: domain decomposable model order reduction and Graph Neural Networks approximating vanishing viscosity solutions}},
  volume={531},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2025.113915},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Romor, Francesco and Torlo, Davide and Rozza, Gianluigi},
  year={2025},
  pages={113915}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/friedrichs-systems-discretized-with-the-dgm-domain-decomposable-model-order-reduction-and-graph-neural-networks-approximating-vanishing-viscosity-solutions.bib)
 
## References
- Friedrichs, K. O. Symmetric positive linear differential equations. Communications on Pure and Applied Mathematics vol. 11 333–418 (1958) -- [10.1002/cpa.3160110306](https://doi.org/10.1002/cpa.3160110306)
- Rauch, J. Symmetric positive systems with boundary characteristic of constant multiplicity. Transactions of the American Mathematical Society vol. 291 167–187 (1985) -- [10.1090/s0002-9947-1985-0797053-4](https://doi.org/10.1090/s0002-9947-1985-0797053-4)
- Rauch, Boundary value problems with nonuniformal characteristic boundary. J. Math. Pures Appl. (1994)
- Ern, A. & Guermond, J. L. Discontinuous Galerkin Methods for Friedrichs’ Systems. I. General theory. SIAM Journal on Numerical Analysis vol. 44 753–778 (2006) -- [10.1137/050624133](https://doi.org/10.1137/050624133)
- Ern, A., Guermond, J.-L. & Caplain, G. An Intrinsic Criterion for the Bijectivity of Hilbert Operators Related to Friedrich’ Systems. Communications in Partial Differential Equations vol. 32 317–341 (2007) -- [10.1080/03605300600718545](https://doi.org/10.1080/03605300600718545)
- Antonic, On equivalent descriptions of boundary conditions for Friedrichs systems. Math. Montisnigri (2009)
- Di Pietro, (2011)
- Sonar, T. & Süli, E. A dual graph-norm refinement indicator for finite volume approximations of the Euler equations. Numerische Mathematik vol. 78 619–658 (1998) -- [10.1007/s002110050328](https://doi.org/10.1007/s002110050328)
- Hoang, C., Choi, Y. & Carlberg, K. Domain-decomposition least-squares Petrov–Galerkin (DD-LSPG) nonlinear model reduction. Computer Methods in Applied Mechanics and Engineering vol. 384 113997 (2021) -- [10.1016/j.cma.2021.113997](https://doi.org/10.1016/j.cma.2021.113997)
- Jensen, (2004)
- Ern, A. & Guermond, J. Discontinuous Galerkin Methods for Friedrichs’ Systems. Part II. Second‐order Elliptic PDEs. SIAM Journal on Numerical Analysis vol. 44 2363–2388 (2006) -- [10.1137/05063831x](https://doi.org/10.1137/05063831x)
- Ern, A. & Guermond, J.-L. Discontinuous Galerkin Methods for Friedrichs’ Systems. Part III. Multifield Theories with Partial Coercivity. SIAM Journal on Numerical Analysis vol. 46 776–804 (2008) -- [10.1137/060664045](https://doi.org/10.1137/060664045)
- Bui-Thanh, T., Demkowicz, L. & Ghattas, O. A Unified Discontinuous Petrov--Galerkin Method and Its Analysis for Friedrichs’ Systems. SIAM Journal on Numerical Analysis vol. 51 1933–1958 (2013) -- [10.1137/110854369](https://doi.org/10.1137/110854369)
- Chen, J.-U., Kang, S., Bui-Thanh, T. & Shadid, J. N. A unified hp-HDG framework for Friedrichs’ PDE systems. Computers &amp; Mathematics with Applications vol. 154 236–266 (2024) -- [10.1016/j.camwa.2023.12.009](https://doi.org/10.1016/j.camwa.2023.12.009)
- Prud’homme, C. et al. Reliable Real-Time Solution of Parametrized Partial Differential Equations: Reduced-Basis Output Bound Methods. Journal of Fluids Engineering vol. 124 70–80 (2001) -- [10.1115/1.1448332](https://doi.org/10.1115/1.1448332)
- Maday, Y. & Rønquist, E. M. Journal of Scientific Computing vol. 17 447–459 (2002) -- [10.1023/a:1015197908587](https://doi.org/10.1023/a:1015197908587)
- Hesthaven, (2016)
- Rozza, (2022)
- Parish, E. J. & Rizzi, F. On the impact of dimensionally-consistent and physics-based inner products for POD-Galerkin and least-squares model reduction of compressible flows. Journal of Computational Physics vol. 491 112387 (2023) -- [10.1016/j.jcp.2023.112387](https://doi.org/10.1016/j.jcp.2023.112387)
- Hesthaven, Structure-preserving model order reduction of Hamiltonian systems. Proc. Int. Cong. Math. (2022)
- Van Der Schaft, Port-Hamiltonian systems theory: an introductory overview. Found. Trends Syst. Comput. (2014)
- Beattie, Structure-preserving interpolatory model reduction for port-Hamiltonian differential-algebraic systems. (2022)
- Bui-Thanh, T., Demkowicz, L. & Ghattas, O. Constructively well-posed approximation methods with unity inf–sup and continuity constants for partial differential equations. Mathematics of Computation vol. 82 1923–1952 (2013) -- [10.1090/s0025-5718-2013-02697-x](https://doi.org/10.1090/s0025-5718-2013-02697-x)
- Beurer, E., Feuerle, M., Reich, N. & Urban, K. An Ultraweak Variational Method for Parameterized Linear Differential-Algebraic Equations. Frontiers in Applied Mathematics and Statistics vol. 8 (2022) -- [10.3389/fams.2022.910786](https://doi.org/10.3389/fams.2022.910786)
- Hain, S. & Urban, K. An ultra-weak space-time variational formulation for the Schrödinger equation. Journal of Complexity vol. 85 101868 (2024) -- [10.1016/j.jco.2024.101868](https://doi.org/10.1016/j.jco.2024.101868)
- Henning, J., Palitta, D., Simoncini, V. & Urban, K. An ultraweak space-time variational formulation for the wave equation: Analysis and efficient numerical solution. ESAIM: Mathematical Modelling and Numerical Analysis vol. 56 1173–1198 (2022) -- [10.1051/m2an/2022035](https://doi.org/10.1051/m2an/2022035)
- Renelt, L., Engwer, C. & Ohlberger, M. An Optimally Stable Approximation of Reactive Transport Using Discrete Test and Infinite Trial Spaces. Springer Proceedings in Mathematics &amp; Statistics 289–298 (2023) doi:10.1007/978-3-031-40860-1_30 -- [10.1007/978-3-031-40860-1_30](https://doi.org/10.1007/978-3-031-40860-1_30)
- Taddei, T. A Registration Method for Model Order Reduction: Data Compression and Geometry Reduction. SIAM Journal on Scientific Computing vol. 42 A997–A1027 (2020) -- [10.1137/19m1271270](https://doi.org/10.1137/19m1271270)
- Iollo, A. & Lombardi, D. Advection modes by optimal mass transfer. Physical Review E vol. 89 (2014) -- [10.1103/physreve.89.022923](https://doi.org/10.1103/physreve.89.022923)
- Peherstorfer, B. Model Reduction for Transport-Dominated Problems via Online Adaptive Bases and Adaptive Sampling. SIAM Journal on Scientific Computing vol. 42 A2803–A2836 (2020) -- [10.1137/19m1257275](https://doi.org/10.1137/19m1257275)
- Rim, D. & Mandli, K. T. Displacement Interpolation Using Monotone Rearrangement. SIAM/ASA Journal on Uncertainty Quantification vol. 6 1503–1531 (2018) -- [10.1137/18m1168315](https://doi.org/10.1137/18m1168315)
- Carlberg, K., Bou‐Mosleh, C. & Farhat, C. Efficient non‐linear model reduction via a least‐squares Petrov–Galerkin projection and compressive tensor approximations. International Journal for Numerical Methods in Engineering vol. 86 155–181 (2010) -- [10.1002/nme.3050](https://doi.org/10.1002/nme.3050)
- Cagniart, (2019)
- Amsallem, D. & Farhat, C. Interpolation Method for Adapting Reduced-Order Models and Application to Aeroelasticity. AIAA Journal vol. 46 1803–1813 (2008) -- [10.2514/1.35374](https://doi.org/10.2514/1.35374)
- Lee, K. & Carlberg, K. T. Model reduction of dynamical systems on nonlinear manifolds using deep convolutional autoencoders. Journal of Computational Physics vol. 404 108973 (2020) -- [10.1016/j.jcp.2019.108973](https://doi.org/10.1016/j.jcp.2019.108973)
- Crisovan, R., Torlo, D., Abgrall, R. & Tokareva, S. Model order reduction for parametrized nonlinear hyperbolic problems as an application to uncertainty quantification. Journal of Computational and Applied Mathematics vol. 348 466–489 (2019) -- [10.1016/j.cam.2018.09.018](https://doi.org/10.1016/j.cam.2018.09.018)
- Torlo,
- Iollo, A. & Taddei, T. Mapping of coherent structures in parameterized flows by learning optimal transportation with Gaussian models. Journal of Computational Physics vol. 471 111671 (2022) -- [10.1016/j.jcp.2022.111671](https://doi.org/10.1016/j.jcp.2022.111671)
- Maday, Y. & Ronquist, E. M. The Reduced Basis Element Method: Application to a Thermal Fin Problem. SIAM Journal on Scientific Computing vol. 26 240–258 (2004) -- [10.1137/s1064827502419932](https://doi.org/10.1137/s1064827502419932)
- Phuong Huynh, D. B., Knezevic, D. J. & Patera, A. T. A Static condensation Reduced Basis Element method : approximation anda posteriorierror estimation. ESAIM: Mathematical Modelling and Numerical Analysis vol. 47 213–251 (2012) -- [10.1051/m2an/2012022](https://doi.org/10.1051/m2an/2012022)
- Eftang, J., Huynh, D., Knezevic, D., Ronquist, E. & Patera, A. Adaptive Port Reduction in Static Condensation. IFAC Proceedings Volumes vol. 45 695–699 (2012) -- [10.3182/20120215-3-at-3016.00123](https://doi.org/10.3182/20120215-3-at-3016.00123)
- Xiao, D. et al. A domain decomposition non-intrusive reduced order model for turbulent flows. Computers &amp; Fluids vol. 182 15–27 (2019) -- [10.1016/j.compfluid.2019.02.012](https://doi.org/10.1016/j.compfluid.2019.02.012)
- Oleinik, Discontinuous solutions of nonlinear differential equations. Am. Math. Soc. Transl. (1963)
- Kružkov, S. N. FIRST ORDER QUASILINEAR EQUATIONS IN SEVERAL INDEPENDENT VARIABLES. Mathematics of the USSR-Sbornik vol. 10 217–243 (1970) -- [10.1070/sm1970v010n02abeh002156](https://doi.org/10.1070/sm1970v010n02abeh002156)
- DiPerna, Convergence of approximate solutions to conservation laws. (1982)
- Goodman, J. & Xin, Z. Viscous limits for piecewise smooth solutions to systems of conservation laws. Archive for Rational Mechanics and Analysis vol. 121 235–265 (1992) -- [10.1007/bf00410614](https://doi.org/10.1007/bf00410614)
- Tencer, J. & Potter, K. A Tailored Convolutional Neural Network for Nonlinear Manifold Learning of Computational Physics Data Using Unstructured Spatial Discretizations. SIAM Journal on Scientific Computing vol. 43 A2581–A2613 (2021) -- [10.1137/20m1344263](https://doi.org/10.1137/20m1344263)
- Hughes, T. J. R., Mallet, M. & Akira, M. A new finite element formulation for computational fluid dynamics: II. Beyond SUPG. Computer Methods in Applied Mechanics and Engineering vol. 54 341–355 (1986) -- [10.1016/0045-7825(86)90110-6](https://doi.org/10.1016/0045-7825(86)90110-6)
- Houston, P., Mackenzie, J. A., S�li, E. & Warnecke, G. A posteriori error analysis for numerical approximations of Friedrichs systems. Numerische Mathematik vol. 82 433–470 (1999) -- [10.1007/s002110050426](https://doi.org/10.1007/s002110050426)
- Antonić, N., Burazin, K., Crnjac, I. & Erceg, M. Complex Friedrichs systems and applications. Journal of Mathematical Physics vol. 58 (2017) -- [10.1063/1.5005608](https://doi.org/10.1063/1.5005608)
- Jolliffe, (2002)
- Kunisch, K. & Volkwein, S. Galerkin proper orthogonal decomposition methods for parabolic problems. Numerische Mathematik vol. 90 117–148 (2001) -- [10.1007/s002110100282](https://doi.org/10.1007/s002110100282)
- Torlo, D. & Ricchiuto, M. Model order reduction strategies for weakly dispersive waves. Mathematics and Computers in Simulation vol. 205 997–1028 (2023) -- [10.1016/j.matcom.2022.10.034](https://doi.org/10.1016/j.matcom.2022.10.034)
- Prud’homme, C., Rovas, D. V., Veroy, K. & Patera, A. T. A Mathematical and Computational Framework for Reliable Real-Time Solution of Parametrized Partial Differential Equations. ESAIM: Mathematical Modelling and Numerical Analysis vol. 36 747–771 (2002) -- [10.1051/m2an:2002035](https://doi.org/10.1051/m2an:2002035)
- Baiges, J., Codina, R. & Idelsohn, S. A domain decomposition strategy for reduced order models. Application to the incompressible Navier–Stokes equations. Computer Methods in Applied Mechanics and Engineering vol. 267 23–42 (2013) -- [10.1016/j.cma.2013.08.001](https://doi.org/10.1016/j.cma.2013.08.001)
- Xiao, D., Fang, F., Heaney, C. E., Navon, I. M. & Pain, C. C. A domain decomposition method for the non-intrusive reduced order modelling of fluid flow. Computer Methods in Applied Mechanics and Engineering vol. 354 307–330 (2019) -- [10.1016/j.cma.2019.05.039](https://doi.org/10.1016/j.cma.2019.05.039)
- del Pino,
- Iollo, A., Sambataro, G. & Taddei, T. A one-shot overlapping Schwarz method for component-based model reduction: application to nonlinear elasticity. Computer Methods in Applied Mechanics and Engineering vol. 404 115786 (2023) -- [10.1016/j.cma.2022.115786](https://doi.org/10.1016/j.cma.2022.115786)
- Prusak, I., Nonino, M., Torlo, D., Ballarin, F. & Rozza, G. An optimisation–based domain–decomposition reduced order model for the incompressible Navier-Stokes equations. Computers &amp; Mathematics with Applications vol. 151 172–189 (2023) -- [10.1016/j.camwa.2023.09.039](https://doi.org/10.1016/j.camwa.2023.09.039)
- Prusak, I., Torlo, D., Nonino, M. & Rozza, G. An optimisation–based domain–decomposition reduced order model for parameter–dependent non–stationary fluid dynamics problems. Computers &amp; Mathematics with Applications vol. 166 253–268 (2024) -- [10.1016/j.camwa.2024.05.004](https://doi.org/10.1016/j.camwa.2024.05.004)
- Lucia, D. J., King, P. I. & Beran, P. S. Domain Decomposition for Reduced-Order Modeling of a Flow with Moving Shocks. AIAA Journal vol. 40 2360–2362 (2002) -- [10.2514/2.1576](https://doi.org/10.2514/2.1576)
- Kaulmann, S., Ohlberger, M. & Haasdonk, B. A new local reduced basis discontinuous Galerkin approach for heterogeneous multiscale problems. Comptes Rendus. Mathématique vol. 349 1233–1238 (2011) -- [10.1016/j.crma.2011.10.024](https://doi.org/10.1016/j.crma.2011.10.024)
- Buhr, Localized model reduction for parameterized problems. (2020)
- Ohlberger, M. & Schindler, F. Error Control for the Localized Reduced Basis Multiscale Method with Adaptive On-Line Enrichment. SIAM Journal on Scientific Computing vol. 37 A2865–A2895 (2015) -- [10.1137/151003660](https://doi.org/10.1137/151003660)
- Chen, A seamless reduced basis element method for 2D Maxwell's problem: an introduction. (2011)
- Yano, M. Discontinuous Galerkin reduced basis empirical quadrature procedure for model reduction of parametrized nonlinear conservation laws. Advances in Computational Mathematics vol. 45 2287–2320 (2019) -- [10.1007/s10444-019-09710-z](https://doi.org/10.1007/s10444-019-09710-z)
- Antonietti, P. F., Pacciarini, P. & Quarteroni, A. A discontinuous Galerkin reduced basis element method for elliptic problems. ESAIM: Mathematical Modelling and Numerical Analysis vol. 50 337–360 (2016) -- [10.1051/m2an/2015045](https://doi.org/10.1051/m2an/2015045)
- Arndt, D. et al. The deal.II library, Version 9.3. Journal of Numerical Mathematics vol. 29 171–186 (2021) -- [10.1515/jnma-2021-0081](https://doi.org/10.1515/jnma-2021-0081)
- Bangerth, W., Burstedde, C., Heister, T. & Kronbichler, M. Algorithms and data structures for massively parallel generic adaptive finite element codes. ACM Transactions on Mathematical Software vol. 38 1–28 (2011) -- [10.1145/2049673.2049678](https://doi.org/10.1145/2049673.2049678)
- Burstedde, C., Wilcox, L. C. & Ghattas, O. <tt>p4est</tt>: Scalable Algorithms for Parallel Adaptive Mesh Refinement on Forests of Octrees. SIAM Journal on Scientific Computing vol. 33 1103–1133 (2011) -- [10.1137/100791634](https://doi.org/10.1137/100791634)
- Balay,
- Dalcin, L. D., Paz, R. R., Kler, P. A. & Cosimo, A. Parallel distributed computing using Python. Advances in Water Resources vol. 34 1124–1139 (2011) -- [10.1016/j.advwatres.2011.04.013](https://doi.org/10.1016/j.advwatres.2011.04.013)
- Romor, F., Tezzele, M. & Rozza, G. A Local Approach to Parameter Space Reduction for Regression and Classification Tasks. Journal of Scientific Computing vol. 99 (2024) -- [10.1007/s10915-024-02542-0](https://doi.org/10.1007/s10915-024-02542-0)
- Zimmermann, (2021)
- Godlewski, (1991)
- DiPerna, R. J. Convergence of the viscosity method for isentropic gas dynamics. Communications in Mathematical Physics vol. 91 1–30 (1983) -- [10.1007/bf01206047](https://doi.org/10.1007/bf01206047)
- Maday, Y. & Tadmor, E. Analysis of the Spectral Vanishing Viscosity Method for Periodic Conservation Laws. SIAM Journal on Numerical Analysis vol. 26 854–870 (1989) -- [10.1137/0726047](https://doi.org/10.1137/0726047)
- Cohen, A. & DeVore, R. Approximation of high-dimensional parametric PDEs. Acta Numerica vol. 24 1–159 (2015) -- [10.1017/s0962492915000033](https://doi.org/10.1017/s0962492915000033)
- Cohen, Kolmogorov widths under holomorphic mappings. IMA J. Numer. Anal. (2016)
- Arbes, F., Greif, C. & Urban, K. The Kolmogorov N-width for linear transport: exact representation and the influence of the data. Advances in Computational Mathematics vol. 51 (2025) -- [10.1007/s10444-025-10224-0](https://doi.org/10.1007/s10444-025-10224-0)
- Xie, X., Wells, D., Wang, Z. & Iliescu, T. Numerical analysis of the Leray reduced order model. Journal of Computational and Applied Mathematics vol. 328 12–29 (2018) -- [10.1016/j.cam.2017.06.026](https://doi.org/10.1016/j.cam.2017.06.026)
- Wells, D., Wang, Z., Xie, X. & Iliescu, T. An evolve‐then‐filter regularized reduced order model for convection‐dominated flows. International Journal for Numerical Methods in Fluids vol. 84 598–615 (2017) -- [10.1002/fld.4363](https://doi.org/10.1002/fld.4363)
- Fukami, K., Fukagata, K. & Taira, K. Super-resolution reconstruction of turbulent flows with machine learning. Journal of Fluid Mechanics vol. 870 106–120 (2019) -- [10.1017/jfm.2019.238](https://doi.org/10.1017/jfm.2019.238)
- Kochkov, D. et al. Machine learning–accelerated computational fluid dynamics. Proceedings of the National Academy of Sciences vol. 118 (2021) -- [10.1073/pnas.2101784118](https://doi.org/10.1073/pnas.2101784118)
- Franco, N. R., Manzoni, A. & Zunino, P. Mesh-Informed Neural Networks for Operator Learning in Finite Element Spaces. Journal of Scientific Computing vol. 97 (2023) -- [10.1007/s10915-023-02331-1](https://doi.org/10.1007/s10915-023-02331-1)
- Pichi, F., Moya, B. & Hesthaven, J. S. A graph convolutional autoencoder approach to model order reduction for parametrized PDEs. Journal of Computational Physics vol. 501 112762 (2024) -- [10.1016/j.jcp.2024.112762](https://doi.org/10.1016/j.jcp.2024.112762)
- Pfaff, Learning mesh-based simulation with graph networks. (2020)
- Gilmer, Neural message passing for quantum chemistry. (2017)
- Simonovsky, Dynamic edge-conditioned filters in convolutional neural networks on graphs. (2017)
- Hamilton, Inductive representation learning on large graphs. Adv. Neural Inf. Process. Syst. (2017)
- Harris, C. R. et al. Array programming with NumPy. Nature vol. 585 357–362 (2020) -- [10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)
- Dalcin, L. & Fang, Y.-L. L. mpi4py: Status Update After 12 Years of Development. Computing in Science &amp; Engineering vol. 23 47–54 (2021) -- [10.1109/mcse.2021.3083216](https://doi.org/10.1109/mcse.2021.3083216)
- Amestoy, P. R., Guermouche, A., L’Excellent, J.-Y. & Pralet, S. Hybrid scheduling for the parallel solution of linear systems. Parallel Computing vol. 32 136–156 (2006) -- [10.1016/j.parco.2005.07.004](https://doi.org/10.1016/j.parco.2005.07.004)
- Fey, Fast graph representation learning with PyTorch geometric. (2019)
- Kingma,

