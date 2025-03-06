---
layout: post
title: "Symplectic Hamiltonian HDG methods for wave propagation phenomena"
date: 2017-09-11 00:00:00 +0100
permalink: symplectic-hamiltonian-hdg-methods-for-wave-propagation-phenomena
year: 2017
authors: M.A. Sánchez, C. Ciuca, N.C. Nguyen, J. Peraire, B. Cockburn
category:
  - articles
tags:
  - finite element methods
  - discontinuous galerkin methods
  - hybrid/mixed methods
  - acoustic wave equation
  - hamiltonian systems
  - symplectic time integrators
  - energy conservation
---
 
## Authors
[M.A. Sánchez](authors/manuel_a_sanchez), [C. Ciuca](authors/c_ciuca), [N.C. Nguyen](authors/ngoc_cuong_nguyen), [J. Peraire](authors/jaime_peraire), [B. Cockburn](authors/bernardo_cockburn)
 
## Abstract
We devise the first symplectic Hamiltonian hybridizable discontinuous Galerkin (HDG) methods for the acoustic wave equation. We discretize in space by using a Hamiltonian HDG scheme, that is, an HDG method which preserves the Hamiltonian structure of the wave equation, and in time by using symplectic, diagonally implicit and explicit partitioned Runge–Kutta methods. The fundamental feature of the resulting scheme is that the conservation of a discrete energy, which is nothing but a discrete version of the original Hamiltonian, is guaranteed. We present numerical experiments which indicate that the method achieves optimal approximations of orderk+1in theL2-norm when polynomials of degreek≥0and Runge–Kutta time-marching methods of orderk+1are used. In addition, by means of post-processing techniques and by increasing the order of the Runge–Kutta method tok+2, we obtain superconvergent approximations of orderk+2in theL2-norm for the displacement and the velocity. We also present numerical examples that corroborate that the methods conserve energy and that they compare favorably with dissipative HDG schemes, of similar accuracy properties, for long-time simulations.
 
## Keywords
Finite element methods; Discontinuous Galerkin methods; Hybrid/mixed methods; Acoustic wave equation; Hamiltonian systems; Symplectic time integrators; Energy conservation
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2017
- **Volume:** 350
- **Issue:** 
- **Pages:** 951--973
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2017.09.010](https://doi.org/10.1016/j.jcp.2017.09.010)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{S_nchez_2017,
  title={{Symplectic Hamiltonian HDG methods for wave propagation phenomena}},
  volume={350},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2017.09.010},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Sánchez, M.A. and Ciuca, C. and Nguyen, N.C. and Peraire, J. and Cockburn, B.},
  year={2017},
  pages={951--973}
}
{% endraw %}
{% endhighlight %}
 
## References
- [Blanes, S. & Moan, P. C. Practical symplectic partitioned Runge–Kutta and Runge–Kutta–Nyström methods. Journal of Computational and Applied Mathematics vol. 142 313–330 (2002)](practical-symplectic-partitioned-runge-kutta-and-runge-kutta-nystrom-methods) -- [10.1016/S0377-0427(01)00492-7](https://doi.org/10.1016/S0377-0427(01)00492-7)
- Bochev, P. B. & Scovel, C. On quadratic invariants and symplectic structure. BIT vol. 34 337–345 (1994) -- [10.1007/BF01935643](https://doi.org/10.1007/BF01935643)
- Chung, E. T. & Engquist, B. Optimal Discontinuous Galerkin Methods for the Acoustic Wave Equation in Higher Dimensions. SIAM Journal on Numerical Analysis vol. 47 3820–3848 (2009) -- [10.1137/080729062](https://doi.org/10.1137/080729062)
- Chung, E. T. & Engquist, B. Optimal Discontinuous Galerkin Methods for the Acoustic Wave Equation in Higher Dimensions. SIAM Journal on Numerical Analysis vol. 47 3820–3848 (2009) -- [10.1137/080729062](https://doi.org/10.1137/080729062)
- Cockburn, B. & Fu, G. Superconvergence byM-decompositions. Part II: Construction of two-dimensional finite elements. ESAIM: Mathematical Modelling and Numerical Analysis vol. 51 165–186 (2016) -- [10.1051/m2an/2016016](https://doi.org/10.1051/m2an/2016016)
- Cockburn, B. & Fu, G. Superconvergence byM-decompositions. Part III: Construction of three-dimensional finite elements. ESAIM: Mathematical Modelling and Numerical Analysis vol. 51 365–398 (2016) -- [10.1051/m2an/2016023](https://doi.org/10.1051/m2an/2016023)
- Cockburn, B., Fu, G. & Sayas, F. J. Superconvergence by $M$-decompositions. Part I: General theory for HDG methods for diffusion. Mathematics of Computation vol. 86 1609–1641 (2016) -- [10.1090/mcom/3140](https://doi.org/10.1090/mcom/3140)
- Cockburn, B., Gopalakrishnan, J. & Lazarov, R. Unified Hybridization of Discontinuous Galerkin, Mixed, and Continuous Galerkin Methods for Second Order Elliptic Problems. SIAM Journal on Numerical Analysis vol. 47 1319–1365 (2009) -- [10.1137/070706616](https://doi.org/10.1137/070706616)
- Cockburn, B. & Quenneville-Bélair, V. Uniform-in-time superconvergence of the HDG methods for the acoustic wave equation. Mathematics of Computation vol. 83 65–85 (2013) -- [10.1090/S0025-5718-2013-02743-3](https://doi.org/10.1090/S0025-5718-2013-02743-3)
- COOPER, G. J. Stability of Runge-Kutta Methods for Trajectory Problems. IMA Journal of Numerical Analysis vol. 7 1–13 (1987) -- [10.1093/imanum/7.1.1](https://doi.org/10.1093/imanum/7.1.1)
- Cowsat, L. C., Dupont, T. F. & Wheeler, M. F. A priori estimates for mixed finite element methods for the wave equation. Computer Methods in Applied Mechanics and Engineering vol. 82 205–222 (1990) -- [10.1016/0045-7825(90)90165-I](https://doi.org/10.1016/0045-7825(90)90165-I)
- Beirão da Veiga, L., Lopez, L. & Vacca, G. Mimetic finite difference methods for Hamiltonian wave equations in 2D. Computers &amp; Mathematics with Applications vol. 74 1123–1141 (2017) -- [10.1016/j.camwa.2017.05.022](https://doi.org/10.1016/j.camwa.2017.05.022)
- Falk, R. S. & Richter, G. R. Explicit Finite Element Methods for Symmetric Hyperbolic Equations. SIAM Journal on Numerical Analysis vol. 36 935–952 (1999) -- [10.1137/S0036142997329463](https://doi.org/10.1137/S0036142997329463)
- Geveci, T. On the application of mixed finite element methods to the wave equations. ESAIM: Mathematical Modelling and Numerical Analysis vol. 22 243–250 (1988) -- [10.1051/m2an/1988220202431](https://doi.org/10.1051/m2an/1988220202431)
- Grote, M. J., Schneebeli, A. & Schötzau, D. Discontinuous Galerkin Finite Element Method for the Wave Equation. SIAM Journal on Numerical Analysis vol. 44 2408–2431 (2006) -- [10.1137/05063194X](https://doi.org/10.1137/05063194X)
- [Kirby, R. C. & Kieu, T. T. Symplectic-mixed finite element approximation of linear acoustic wave equations. Numerische Mathematik vol. 130 257–291 (2014)](symplectic-mixed-finite-element-approximation-of-linear-acoustic-wave-equations) -- [10.1007/s00211-014-0667-4](https://doi.org/10.1007/s00211-014-0667-4)
- McLachlan, R. I. & Atela, P. The accuracy of symplectic integrators. Nonlinearity vol. 5 541–562 (1992) -- [10.1088/0951-7715/5/2/011](https://doi.org/10.1088/0951-7715/5/2/011)
- Nguyen, N. C. & Peraire, J. Hybridizable discontinuous Galerkin methods for partial differential equations in continuum mechanics. Journal of Computational Physics vol. 231 5955–5988 (2012) -- [10.1016/j.jcp.2012.02.033](https://doi.org/10.1016/j.jcp.2012.02.033)
- Petersen, S., Farhat, C. & Tezaur, R. A space–time discontinuous Galerkin method for the solution of the wave equation in the time domain. International Journal for Numerical Methods in Engineering vol. 78 275–295 (2008) -- [10.1002/nme.2485](https://doi.org/10.1002/nme.2485)
- Piperno, S. Symplectic local time-stepping in non-dissipative DGTD methods applied to wave propagation problems. ESAIM: Mathematical Modelling and Numerical Analysis vol. 40 815–841 (2006) -- [10.1051/m2an:2006035](https://doi.org/10.1051/m2an:2006035)
- Ruth, R. D. A Can0nical Integrati0n Technique. IEEE Transactions on Nuclear Science vol. 30 2669–2671 (1983) -- [10.1109/TNS.1983.4332919](https://doi.org/10.1109/TNS.1983.4332919)
- Stanglmeier, M., Nguyen, N. C., Peraire, J. & Cockburn, B. An explicit hybridizable discontinuous Galerkin method for the acoustic wave equation. Computer Methods in Applied Mechanics and Engineering vol. 300 748–769 (2016) -- [10.1016/j.cma.2015.12.003](https://doi.org/10.1016/j.cma.2015.12.003)
- Xing, Y. et al. Energy conserving local discontinuous Galerki
methods for wave propagation problems. Inverse Problems &amp; Imaging vol. 7 967–986 (2013) -- [10.3934/ipi.2013.7.967](https://doi.org/10.3934/ipi.2013.7.967)

