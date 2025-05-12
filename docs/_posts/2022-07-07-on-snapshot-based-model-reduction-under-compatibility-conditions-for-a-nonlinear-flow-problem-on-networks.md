---
layout: post
title: "On Snapshot-Based Model Reduction Under Compatibility Conditions for a Nonlinear Flow Problem on Networks"
date: 2022-07-07 00:00:00 +0100
permalink: on-snapshot-based-model-reduction-under-compatibility-conditions-for-a-nonlinear-flow-problem-on-networks
year: 2022
authors: Björn Liljegren-Sailer, Nicole Marheineke
category: articles
tags:
  - Structure-preserving
  - Nonlinear model reduction
  - Proper orthogonal decomposition
  - Empirical quadrature
  - Gas networks
  - 35L60
  - 35R02
  - 65N12
---
 
## Authors
[Björn Liljegren-Sailer](authors/bjorn-liljegren-sailer), [Nicole Marheineke](authors/nicole-marheineke)
 
## Abstract
This paper is on the construction of structure-preserving, online-efficient reduced models for the barotropic Euler equations with a friction term on networks. The nonlinear flow problem finds broad application in the context of gas distribution networks. We propose a snapshot-based reduction approach that consists of a mixed variational Galerkin approximation combined with quadrature-type complexity reduction. Its main feature is that certain compatibility conditions are assured during the training phase, which make our approach structure-preserving. The resulting reduced models are locally mass conservative and inherit an energy bound and port-Hamiltonian structure. We also derive a wellposedness result for them. In the training phase, the compatibility conditions pose challenges, we face constrained data approximation problems as opposed to the unconstrained training problems in the conventional reduction methods. The training of our model order reduction consists of a principal component analysis under a compatibility constraint and, notably, yields reduced models that fulfill an optimality condition for the snapshot data. The training of our quadrature-type complexity reduction involves a semi-definite program with combinatorial aspects, which we approach by a greedy procedure. Efficient algorithmic implementations are presented. The robustness and good performance of our structure-preserving reduced models are showcased at the example of gas network simulations.
 
## Keywords
Structure-preserving; Nonlinear model reduction; Proper orthogonal decomposition; Empirical quadrature; Gas networks; 35L60; 35R02; 65N12
 
## Citation
- **Journal:** Journal of Scientific Computing
- **Year:** 2022
- **Volume:** 92
- **Issue:** 2
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10915-022-01901-z](https://doi.org/10.1007/s10915-022-01901-z)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Liljegren_Sailer_2022,
  title={{On Snapshot-Based Model Reduction Under Compatibility Conditions for a Nonlinear Flow Problem on Networks}},
  volume={92},
  ISSN={1573-7691},
  DOI={10.1007/s10915-022-01901-z},
  number={2},
  journal={Journal of Scientific Computing},
  publisher={Springer Science and Business Media LLC},
  author={Liljegren-Sailer, Björn and Marheineke, Nicole},
  year={2022}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-snapshot-based-model-reduction-under-compatibility-conditions-for-a-nonlinear-flow-problem-on-networks.bib)
 
## References
- Afkham, B. M. & Hesthaven, J. S. Structure Preserving Model Reduction of Parametric Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 39 A2616–A2644 (2017) -- [10.1137/17m1111991](https://doi.org/10.1137/17m1111991)
- [Maboudi Afkham, B. & Hesthaven, J. S. Structure-Preserving Model-Reduction of Dissipative Hamiltonian Systems. Journal of Scientific Computing vol. 81 3–21 (2018)](structure-preserving-model-reduction-of-dissipative-hamiltonian-systems) -- [10.1007/s10915-018-0653-6](https://doi.org/10.1007/s10915-018-0653-6)
- S Ali, Comput. Math (2020)
- An, S. S., Kim, T. & James, D. L. Optimizing cubature for efficient integration of subspace deformations. ACM Transactions on Graphics vol. 27 1–10 (2008) -- [10.1145/1409060.1409118](https://doi.org/10.1145/1409060.1409118)
- Antonelli, P. & Marcati, P. The Quantum Hydrodynamics System in Two Space Dimensions. Archive for Rational Mechanics and Analysis vol. 203 499–527 (2011) -- [10.1007/s00205-011-0454-7](https://doi.org/10.1007/s00205-011-0454-7)
- Barrault, M., Maday, Y., Nguyen, N. C. & Patera, A. T. An ‘empirical interpolation’ method: application to efficient reduced-basis discretization of partial differential equations. Comptes Rendus. Mathématique vol. 339 667–672 (2004) -- [10.1016/j.crma.2004.08.006](https://doi.org/10.1016/j.crma.2004.08.006)
- A Ben-Israel, Generalized Inverses: Theory and Applications (2001)
- Dimension Reduction of Large-Scale Systems. Lecture Notes in Computational Science and Engineering (Springer Berlin Heidelberg, 2005). doi:10.1007/3-540-27909-1 -- [10.1007/3-540-27909-1](https://doi.org/10.1007/3-540-27909-1)
- Boffi, D. et al. Mixed Finite Elements, Compatibility Conditions, and Applications. Lecture Notes in Mathematics (Springer Berlin Heidelberg, 2008). doi:10.1007/978-3-540-78319-0 -- [10.1007/978-3-540-78319-0](https://doi.org/10.1007/978-3-540-78319-0)
- Brouwer, J., Gasser, I. & Herty, M. Gas Pipeline Models Revisited: Model Hierarchies, Nonisothermal Models, and Simulations of Networks. Multiscale Modeling &amp; Simulation vol. 9 601–623 (2011) -- [10.1137/100813580](https://doi.org/10.1137/100813580)
- P Buchfink, Math. Comp. Appl (2019)
- Carlberg, K., Bou‐Mosleh, C. & Farhat, C. Efficient non‐linear model reduction via a least‐squares Petrov–Galerkin projection and compressive tensor approximations. International Journal for Numerical Methods in Engineering vol. 86 155–181 (2010) -- [10.1002/nme.3050](https://doi.org/10.1002/nme.3050)
- Carlberg, K., Tuminaro, R. & Boggs, P. Preserving Lagrangian Structure in Nonlinear Model Reduction with Application to Structural Dynamics. SIAM Journal on Scientific Computing vol. 37 B153–B184 (2015) -- [10.1137/140959602](https://doi.org/10.1137/140959602)
- Celledoni, E. et al. Preserving energy resp. dissipation in numerical PDEs using the “Average Vector Field” method. Journal of Computational Physics vol. 231 6770–6789 (2012) -- [10.1016/j.jcp.2012.06.022](https://doi.org/10.1016/j.jcp.2012.06.022)
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- Chaturantabut, S. & Sorensen, D. C. Nonlinear Model Reduction via Discrete Empirical Interpolation. SIAM Journal on Scientific Computing vol. 32 2737–2764 (2010) -- [10.1137/090766498](https://doi.org/10.1137/090766498)
- Chaturantabut, S. & Sorensen, D. C. A State Space Error Estimate for POD-DEIM Nonlinear Model Reduction. SIAM Journal on Numerical Analysis vol. 50 46–63 (2012) -- [10.1137/110822724](https://doi.org/10.1137/110822724)
- [Christiansen, S. H., Munthe-Kaas, H. Z. & Owren, B. Topics in structure-preserving discretization. Acta Numerica vol. 20 1–119 (2011)](topics-in-structure-preserving-discretization) -- [10.1017/s096249291100002x](https://doi.org/10.1017/s096249291100002x)
- Domschke, P., Dua, A., Stolwijk, J. J., Lang, J. & Mehrmann, V. Adaptive refinement strategies for the simulation of gas flow in networks using a model hierarchy. ETNA - Electronic Transactions on Numerical Analysis vol. 48 97–113 (2018) -- [10.1553/etna_vol48s97](https://doi.org/10.1553/etna_vol48s97)
- P Domschke, Appl. Math. Comput. (2015)
- Egger, H. A Robust Conservative Mixed Finite Element Method for Isentropic Compressible Flow on Pipe Networks. SIAM Journal on Scientific Computing vol. 40 A108–A129 (2018) -- [10.1137/16m1094373](https://doi.org/10.1137/16m1094373)
- Egger, H. & Kugler, T. Damped wave systems on networks: exponential stability and uniform approximations. Numerische Mathematik vol. 138 839–867 (2017) -- [10.1007/s00211-017-0924-4](https://doi.org/10.1007/s00211-017-0924-4)
- [Egger, H., Kugler, T., Liljegren-Sailer, B., Marheineke, N. & Mehrmann, V. On Structure-Preserving Model Reduction for Damped Wave Propagation in Transport Networks. SIAM Journal on Scientific Computing vol. 40 A331–A365 (2018)](on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks) -- [10.1137/17m1125303](https://doi.org/10.1137/17m1125303)
- Fareed, H., Singler, J. R., Zhang, Y. & Shen, J. Incremental proper orthogonal decomposition for PDE simulation data. Computers &amp; Mathematics with Applications vol. 75 1942–1960 (2018) -- [10.1016/j.camwa.2017.09.012](https://doi.org/10.1016/j.camwa.2017.09.012)
- Farhat, C., Avery, P., Chapman, T. & Cortial, J. Dimensional reduction of nonlinear finite element dynamic models with finite rotations and energy‐based mesh sampling and weighting for computational efficiency. International Journal for Numerical Methods in Engineering vol. 98 625–662 (2014) -- [10.1002/nme.4668](https://doi.org/10.1002/nme.4668)
- Fisher, T. C. & Carpenter, M. H. High-order entropy stable finite difference schemes for nonlinear conservation laws: Finite domains. Journal of Computational Physics vol. 252 518–557 (2013) -- [10.1016/j.jcp.2013.06.014](https://doi.org/10.1016/j.jcp.2013.06.014)
- [Giesselmann, J., Lattanzio, C. & Tzavaras, A. E. Relative Energy for the Korteweg Theory and Related Hamiltonian Flows in Gas Dynamics. Archive for Rational Mechanics and Analysis vol. 223 1427–1484 (2016)](relative-energy-for-the-korteweg-theory-and-related-hamiltonian-flows-in-gas-dynamics) -- [10.1007/s00205-016-1063-2](https://doi.org/10.1007/s00205-016-1063-2)
- Gotsman, C. & Toledo, S. On the Computation of Null Spaces of Sparse Rectangular Matrices. SIAM Journal on Matrix Analysis and Applications vol. 30 445–463 (2008) -- [10.1137/050638369](https://doi.org/10.1137/050638369)
- Grundel, S. et al. Model Order Reduction of Differential Algebraic Equations Arising from the Simulation of Gas Transport Networks. Differential-Algebraic Equations Forum 183–205 (2014) doi:10.1007/978-3-662-44926-4_9 -- [10.1007/978-3-662-44926-4_9](https://doi.org/10.1007/978-3-662-44926-4_9)
- Hartman, P. Ordinary Differential Equations. (2002) doi:10.1137/1.9780898719222 -- [10.1137/1.9780898719222](https://doi.org/10.1137/1.9780898719222)
- Hernández, J. A., Caicedo, M. A. & Ferrer, A. Dimensional hyper-reduction of nonlinear finite element models via empirical cubature. Computer Methods in Applied Mechanics and Engineering vol. 313 687–722 (2017) -- [10.1016/j.cma.2016.10.022](https://doi.org/10.1016/j.cma.2016.10.022)
- Herrán-González, A., De La Cruz, J. M., De Andrés-Toro, B. & Risco-Martín, J. L. Modeling and simulation of a gas distribution pipeline network. Applied Mathematical Modelling vol. 33 1584–1600 (2009) -- [10.1016/j.apm.2008.02.012](https://doi.org/10.1016/j.apm.2008.02.012)
- Hesthaven, J. S., Rozza, G. & Stamm, B. Certified Reduced Basis Methods for Parametrized Partial Differential Equations. SpringerBriefs in Mathematics (Springer International Publishing, 2016). doi:10.1007/978-3-319-22470-1 -- [10.1007/978-3-319-22470-1](https://doi.org/10.1007/978-3-319-22470-1)
- C Himpe, J. Ind. Math (2021)
- Karper, T. K. Convergent finite differences for 1D viscous isentropic flow in Eulerian coordinates. Discrete and Continuous Dynamical Systems - Series S vol. 7 993–1023 (2014) -- [10.3934/dcdss.2014.7.993](https://doi.org/10.3934/dcdss.2014.7.993)
- Evaluating Gas Network Capacities. (2015) doi:10.1137/1.9781611973693 -- [10.1137/1.9781611973693](https://doi.org/10.1137/1.9781611973693)
- [Kotyczka, P. & Lefèvre, L. Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters vol. 133 104530 (2019)](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- Kunisch, K. & Volkwein, S. Galerkin proper orthogonal decomposition methods for parabolic problems. Numerische Mathematik vol. 90 117–148 (2001) -- [10.1007/s002110100282](https://doi.org/10.1007/s002110100282)
- Kunisch, K. & Volkwein, S. Galerkin Proper Orthogonal Decomposition Methods for a General Equation in Fluid Dynamics. SIAM Journal on Numerical Analysis vol. 40 492–515 (2002) -- [10.1137/s0036142900382612](https://doi.org/10.1137/s0036142900382612)
- LeVeque, R. J. Finite Volume Methods for Hyperbolic Problems. (2002) doi:10.1017/cbo9780511791253 -- [10.1017/cbo9780511791253](https://doi.org/10.1017/cbo9780511791253)
- Liljegren-Sailer, B. Code for paper ‘On port-Hamiltonian approximation of a nonlinear flow problem on networks’. Preprint at https://doi.org/10.5281/ZENODO.6372667 (2022) -- [10.5281/zenodo.6372667](https://doi.org/10.5281/zenodo.6372667)
- [Liljegren-Sailer, B. & Marheineke, N. On Port-Hamiltonian Approximation of a Nonlinear Flow Problem on Networks. SIAM Journal on Scientific Computing vol. 44 B834–B859 (2022)](on-port-hamiltonian-approximation-of-a-nonlinear-flow-problem-on-networks) -- [10.1137/21m1443480](https://doi.org/10.1137/21m1443480)
- Nguyen, T. T., Idier, J., Soussen, C. & Djermoune, E.-H. Non-Negative Orthogonal Greedy Algorithms. IEEE Transactions on Signal Processing vol. 67 5643–5658 (2019) -- [10.1109/tsp.2019.2943225](https://doi.org/10.1109/tsp.2019.2943225)
- Peng, L. & Mohseni, K. Symplectic Model Reduction of Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 A1–A27 (2016) -- [10.1137/140978922](https://doi.org/10.1137/140978922)
- Qiu, Y. et al. Efficient numerical methods for gas network modeling and simulation. Networks &amp; Heterogeneous Media vol. 15 653–679 (2020) -- [10.3934/nhm.2020018](https://doi.org/10.3934/nhm.2020018)
- Rockafellar, R. T. & Wets, R. J. B. Variational Analysis. Grundlehren der mathematischen Wissenschaften (Springer Berlin Heidelberg, 1998). doi:10.1007/978-3-642-02431-3 -- [10.1007/978-3-642-02431-3](https://doi.org/10.1007/978-3-642-02431-3)
- Rozza, G., Huynh, D. B. P. & Manzoni, A. Reduced basis approximation and a posteriori error estimation for Stokes flows in parametrized geometries: roles of the inf-sup stability constants. Numerische Mathematik vol. 125 115–152 (2013) -- [10.1007/s00211-013-0534-8](https://doi.org/10.1007/s00211-013-0534-8)
- Schmidt, M. et al. GasLib—A Library of Gas Network Instances. Data vol. 2 40 (2017) -- [10.3390/data2040040](https://doi.org/10.3390/data2040040)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control vol. 16 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)

