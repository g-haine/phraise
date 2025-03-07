---
layout: post
title: "On Structure-Preserving Model Reduction for Damped Wave Propagation in Transport Networks"
date: 2018-02-13 00:00:00 +0100
permalink: on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks
year: 2018
authors: H. Egger, T. Kugler, B. Liljegren-Sailer, N. Marheineke, V. Mehrmann
category: articles
---
 
## Authors
[H. Egger](authors/herbert_egger), [T. Kugler](authors/t_kugler), [B. Liljegren-Sailer](authors/bjorn_liljegren_sailer), [N. Marheineke](authors/nicole_marheineke), [V. Mehrmann](authors/volker_mehrmann)
 
## Abstract
We consider the discretization and subsequent model reduction of a system of partial differential-algebraic equations describing the propagation of pressure waves in a pipeline network. Important properties like conservation of mass, dissipation of energy, passivity, existence of steady states, and exponential stability can be preserved by an appropriate semidiscretization in space via a mixed finite element method and also during the further dimension reduction by structure- preserving Galerkin projection, which is the main focus of this paper. Krylov subspace methods are employed for the construction of the reduced models, and we discuss certain modifications needed to satisfy some algebraic compatibility conditions which are required to ensure the well-posedness of the reduced models and the preservation of the key properties. Our arguments are based on a careful analysis of the underlying infinite dimensional problem and its Galerkin approximations. The proposed algorithms therefore have a direct inte...
 
## Citation
- **Journal:** SIAM Journal on Scientific Computing
- **Year:** 2018
- **Volume:** 40
- **Issue:** 1
- **Pages:** A331--A365
- **Publisher:** Society for Industrial & Applied Mathematics (SIAM)
- **DOI:** [10.1137/17M1125303](https://doi.org/10.1137/17M1125303)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Egger_2018,
  title={{On Structure-Preserving Model Reduction for Damped Wave Propagation in Transport Networks}},
  volume={40},
  ISSN={1095-7197},
  DOI={10.1137/17m1125303},
  number={1},
  journal={SIAM Journal on Scientific Computing},
  publisher={Society for Industrial & Applied Mathematics (SIAM)},
  author={Egger, H. and Kugler, T. and Liljegren-Sailer, B. and Marheineke, N. and Mehrmann, V.},
  year={2018},
  pages={A331--A365}
}
{% endraw %}
{% endhighlight %}
 
## References
- Bai, Z. Krylov subspace techniques for reduced-order modeling of large-scale dynamical systems. Applied Numerical Mathematics vol. 43 9–44 (2002) -- [10.1016/S0168-9274(02)00116-2](https://doi.org/10.1016/S0168-9274(02)00116-2)
- Bai, Z. & Freund, R. W. A partial Padé-via-Lanczos method for reduced-order modeling. Linear Algebra and its Applications vols 332–334 139–164 (2001) -- [10.1016/S0024-3795(00)00291-3](https://doi.org/10.1016/S0024-3795(00)00291-3)
- Bai, Z. & Su, Y. Dimension Reduction of Large-Scale Second-Order Dynamical Systems via a Second-Order Arnoldi Method. SIAM Journal on Scientific Computing vol. 26 1692–1709 (2005) -- [10.1137/040605552](https://doi.org/10.1137/040605552)
- Bai, Z. & Su, Y. SOAR: A Second-order Arnoldi Method for the Solution of the Quadratic Eigenvalue Problem. SIAM Journal on Matrix Analysis and Applications vol. 26 640–659 (2005) -- [10.1137/S0895479803438523](https://doi.org/10.1137/S0895479803438523)
- Baker, G. A. & Dougalis, V. A. The Effect of Quadrature Errors on Finite Element Approximations for Second Order Hyperbolic Equations. SIAM Journal on Numerical Analysis vol. 13 577–598 (1976) -- [10.1137/0713049](https://doi.org/10.1137/0713049)
- Beattie, C. & Gugercin, S. Interpolatory projection methods for structure-preserving model reduction. Systems &amp; Control Letters vol. 58 225–232 (2009) -- [10.1016/j.sysconle.2008.10.016](https://doi.org/10.1016/j.sysconle.2008.10.016)
- Brouwer, J., Gasser, I. & Herty, M. Gas Pipeline Models Revisited: Model Hierarchies, Nonisothermal Models, and Simulations of Networks. Multiscale Modeling &amp; Simulation vol. 9 601–623 (2011) -- [10.1137/100813580](https://doi.org/10.1137/100813580)
- Chapelle, D., Gariah, A. & Sainte-Marie, J. Galerkin approximation with proper orthogonal decomposition : new error estimates and illustrative examples. ESAIM: Mathematical Modelling and Numerical Analysis vol. 46 731–757 (2012) -- [10.1051/m2an/2011053](https://doi.org/10.1051/m2an/2011053)
- Emmrich, E. & Mehrmann, V. Operator Differential-Algebraic Equations Arising in Fluid Dynamics. Computational Methods in Applied Mathematics vol. 13 443–470 (2013) -- [10.1515/cmam-2013-0018](https://doi.org/10.1515/cmam-2013-0018)
- Freund, R. W. Krylov-subspace methods for reduced-order modeling in circuit simulation. Journal of Computational and Applied Mathematics vol. 123 395–421 (2000) -- [10.1016/S0377-0427(00)00396-4](https://doi.org/10.1016/S0377-0427(00)00396-4)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Gugercin, S., Stykel, T. & Wyatt, S. Model Reduction of Descriptor Systems by Interpolatory Projection Methods. SIAM Journal on Scientific Computing vol. 35 B1010–B1033 (2013) -- [10.1137/130906635](https://doi.org/10.1137/130906635)
- [Harkort, C. & Deutscher, J. Stability and passivity preserving Petrov–Galerkin approximation of linear infinite-dimensional systems. Automatica vol. 48 1347–1352 (2012)](stability-and-passivity-preserving-petrov-galerkin-approximation-of-linear-infinite-dimensional-systems) -- [10.1016/j.automatica.2012.04.010](https://doi.org/10.1016/j.automatica.2012.04.010)
- Kunisch, K. & Volkwein, S. Galerkin proper orthogonal decomposition methods for parabolic problems. Numerische Mathematik vol. 90 117–148 (2001) -- [10.1007/s002110100282](https://doi.org/10.1007/s002110100282)
- Kunisch, K. & Volkwein, S. Galerkin Proper Orthogonal Decomposition Methods for a General Equation in Fluid Dynamics. SIAM Journal on Numerical Analysis vol. 40 492–515 (2002) -- [10.1137/S0036142900382612](https://doi.org/10.1137/S0036142900382612)
- Mehrmann, V. & Watkins, D. Structure-Preserving Methods for Computing Eigenpairs of Large Sparse Skew-Hamiltonian/Hamiltonian Pencils. SIAM Journal on Scientific Computing vol. 22 1905–1925 (2001) -- [10.1137/S1064827500366434](https://doi.org/10.1137/S1064827500366434)
- Meyer, D. G. & Srinivasan, S. Balancing and model reduction for second-order form linear systems. IEEE Transactions on Automatic Control vol. 41 1632–1644 (1996) -- [10.1109/9.544000](https://doi.org/10.1109/9.544000)
- [Polyuga, R. V. Discussion on: “Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces”. European Journal of Control vol. 16 407–409 (2010)](discussion-on-passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.1016/S0947-3580(10)70672-5](https://doi.org/10.1016/S0947-3580(10)70672-5)
- [Polyuga, R. V. & van der Schaft, A. Structure preserving model reduction of port-Hamiltonian systems by moment matching at infinity. Automatica vol. 46 665–672 (2010)](structure-preserving-model-reduction-of-port-hamiltonian-systems-by-moment-matching-at-infinity) -- [10.1016/j.automatica.2010.01.018](https://doi.org/10.1016/j.automatica.2010.01.018)
- [Polyuga, R. V. & van der Schaft, A. Structure Preserving Moment Matching for Port-Hamiltonian Systems: Arnoldi and Lanczos. IEEE Transactions on Automatic Control vol. 56 1458–1462 (2011)](structure-preserving-moment-matching-for-port-hamiltonian-systems-arnoldi-and-lanczos) -- [10.1109/TAC.2011.2128650](https://doi.org/10.1109/TAC.2011.2128650)
- Salimbahrami, B. & Lohmann, B. Order reduction of large scale second-order systems using Krylov subspace methods. Linear Algebra and its Applications vol. 415 385–405 (2006) -- [10.1016/j.laa.2004.12.013](https://doi.org/10.1016/j.laa.2004.12.013)
- Salimbahrami, B., Lohmann, B. & Bunse-Gerstner, A. Passive reduced order modelling of second-order systems. Mathematical and Computer Modelling of Dynamical Systems vol. 14 407–420 (2008) -- [10.1080/13873950701844279](https://doi.org/10.1080/13873950701844279)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM Journal on Control and Optimization vol. 51 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Van Loan, C. Computing the CS and the generalized singular value decompositions. Numerische Mathematik vol. 46 479–491 (1985) -- [10.1007/BF01389653](https://doi.org/10.1007/BF01389653)
- Wu, Y., Hamroun, B., Gorrec, Y. L. & Maschke, B. Port Hamiltonian System in Descriptor Form for Balanced Reduction: Application to a Nanotweezer. IFAC Proceedings Volumes vol. 47 11404–11409 (2014) -- [10.3182/20140824-6-ZA-1003.01579](https://doi.org/10.3182/20140824-6-ZA-1003.01579)

