---
layout: post
title: "On the velocity-stress formulation for geometrically nonlinear elastodynamics and its structure-preserving discretization"
date: 2024-11-07 00:00:00 +0100
permalink: on-the-velocity-stress-formulation-for-geometrically-nonlinear-elastodynamics-and-its-structure-preserving-discretization
year: 2024
authors: Tobias Thoma, Paul Kotyczka, Herbert Egger
category:
  - articles
---
 
## Authors
[Tobias Thoma](authors/tobias_thoma), [Paul Kotyczka](authors/paul_kotyczka), [Herbert Egger](authors/herbert_egger)
 
## Abstract
We consider the dynamics of an elastic continuum under large deformation but small strain. Such systems can be described by the equations of geometrically nonlinear elastodynamics in combination with the St. Venant-Kirchhoff material law. The velocity-stress formulation of the problem turns out to have a formal port-Hamiltonian structure. In contrast to the linear case, the operators of the problem are modulated by the displacement field which can be handled as a passive variable and integrated along with the velocities. A weak formulation of the problem is derived and essential boundary conditions are incorporated via Lagrange multipliers. This variational formulation explicitly encodes the transfer between kinetic and potential energy in the interior as well as across the boundary, thus leading to a global power balance and ensuring passivity of the system. The particular geometric structure of the weak formulation can be preserved under Galerkin approximation via appropriate mixed finite elements. In addition, a fully discrete power balance can be obtained by appropriate time discretization. The main properties of the system and its discretization are shown theoretically and demonstrated by numerical tests.
 
## Citation
- **Journal:** Mathematical and Computer Modelling of Dynamical Systems
- **Year:** 2024
- **Volume:** 30
- **Issue:** 1
- **Pages:** 701--720
- **Publisher:** Informa UK Limited
- **DOI:** [10.1080/13873954.2024.2397486](https://doi.org/10.1080/13873954.2024.2397486)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Thoma_2024,
  title={{On the velocity-stress formulation for geometrically nonlinear elastodynamics and its structure-preserving discretization}},
  volume={30},
  ISSN={1744-5051},
  DOI={10.1080/13873954.2024.2397486},
  number={1},
  journal={Mathematical and Computer Modelling of Dynamical Systems},
  publisher={Informa UK Limited},
  author={Thoma, Tobias and Kotyczka, Paul and Egger, Herbert},
  year={2024},
  pages={701--720}
}
{% endraw %}
{% endhighlight %}
 
## References
- Arnold, D. N. & Lee, J. J. Mixed Methods for Elastodynamics with Weak Symmetry. SIAM Journal on Numerical Analysis vol. 52 2743–2769 (2014) -- [10.1137/13095032X](https://doi.org/10.1137/13095032X)
- Ayachit U. 2015. The paraview guide: updated for paraview version 4.3. Kitware.
- Bécache, E., Joly, P. & Tsogka, C. A New Family of Mixed Finite Elements for the Linear Elastodynamic Problem. SIAM Journal on Numerical Analysis vol. 39 2109–2132 (2002) -- [10.1137/S0036142999359189](https://doi.org/10.1137/S0036142999359189)
- Bonet, J. & Wood, R. D. Nonlinear Continuum Mechanics for Finite Element Analysis. (2008) doi:10.1017/cbo9780511755446 -- [10.1017/CBO9780511755446](https://doi.org/10.1017/CBO9780511755446)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Applied Mathematical Modelling vol. 75 940–960 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part II: Kirchhoff model for thin plates. Applied Mathematical Modelling vol. 75 961–981 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-ii-kirchhoff-model-for-thin-plates) -- [10.1016/j.apm.2019.04.036](https://doi.org/10.1016/j.apm.2019.04.036)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian flexible multibody dynamics. Multibody System Dynamics vol. 51 343–375 (2020)](port-hamiltonian-flexible-multibody-dynamics) -- [10.1007/s11044-020-09758-6](https://doi.org/10.1007/s11044-020-09758-6)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. A Port-Hamiltonian formulation of linear thermoelasticity and its mixed finite element discretization. Journal of Thermal Stresses vol. 44 643–661 (2021)](a-port-hamiltonian-formulation-of-linear-thermoelasticity-and-its-mixed-finite-element-discretization) -- [10.1080/01495739.2021.1917322](https://doi.org/10.1080/01495739.2021.1917322)
- Brugnoli A, Matignon D. 2022. A port-Hamiltonian formulation for the full von-Kármán plate model. 10th European Nonlinear Dynamics Conference (ENOC); Jul 2022; Lyon, France.
- [Brugnoli, A., Rashad, R., Califano, F., Stramigioli, S. & Matignon, D. Mixed finite elements for port-Hamiltonian models of von Kármán beams. IFAC-PapersOnLine vol. 54 186–191 (2021)](mixed-finite-elements-for-port-hamiltonian-models-of-von-karman-beams) -- [10.1016/j.ifacol.2021.11.076](https://doi.org/10.1016/j.ifacol.2021.11.076)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information vol. 38 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Cohen, G. C. Higher-Order Numerical Methods for Transient Wave Equations. Scientific Computation (Springer Berlin Heidelberg, 2002). doi:10.1007/978-3-662-04823-8 -- [10.1007/978-3-662-04823-8](https://doi.org/10.1007/978-3-662-04823-8)
- Court, S. & Kunisch, K. Almost global existence of weak solutions for the nonlinear elastodynamics system for a class of strain energies. Advances in Differential Equations vol. 23 (2018) -- [10.57262/ade/1508983364](https://doi.org/10.57262/ade/1508983364)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [Egger, H., Habrich, O. & Shashkov, V. On the Energy Stable Approximation of Hamiltonian and Gradient Systems. Computational Methods in Applied Mathematics vol. 21 335–349 (2020)](on-the-energy-stable-approximation-of-hamiltonian-and-gradient-systems) -- [10.1515/cmam-2020-0025](https://doi.org/10.1515/cmam-2020-0025)
- [Falaize, A. & Hélie, T. Passive Guaranteed Simulation of Analog Audio Circuits: A Port-Hamiltonian Approach. Applied Sciences vol. 6 273 (2016)](passive-guaranteed-simulation-of-analog-audio-circuits-a-port-hamiltonian-approach) -- [10.3390/app6100273](https://doi.org/10.3390/app6100273)
- [Farle, O., Klis, D., Jochum, M., Floch, O. & Dyczij-Edlinger, R. A port-hamiltonian finite-element formulation for the maxwell equations. 2013 International Conference on Electromagnetics in Advanced Applications (ICEAA) 324–327 (2013) doi:10.1109/iceaa.2013.6632246](a-port-hamiltonian-finite-element-formulation-for-the-maxwell-equations) -- [10.1109/ICEAA.2013.6632246](https://doi.org/10.1109/ICEAA.2013.6632246)
- Festa, G. & Vilotte, J.-P. The Newmark scheme as velocity-stress time-staggering: an efficient PML implementation for spectral element simulations of elastodynamics. Geophysical Journal International vol. 161 789–812 (2005) -- [10.1111/j.1365-246X.2005.02601.x](https://doi.org/10.1111/j.1365-246X.2005.02601.x)
- Geveci, T. On the application of mixed finite element methods to the wave equations. ESAIM: Mathematical Modelling and Numerical Analysis vol. 22 243–250 (1988) -- [10.1051/m2an/1988220202431](https://doi.org/10.1051/m2an/1988220202431)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Jacob B, Zwart HJ. 2012. Linear port-Hamiltonian systems on infinite-dimensional spaces. Operator Theory: Adv And Appl. 223. Birkhäuser/Springer, Basel.
- Joly, P. Variational Methods for Time-Dependent Wave Propagation Problems. Lecture Notes in Computational Science and Engineering 201–264 (2003) doi:10.1007/978-3-642-55483-4_6 -- [10.1007/978-3-642-55483-4_6](https://doi.org/10.1007/978-3-642-55483-4_6)
- Kinon PL, Thoma T, Betsch P, Kotyczka P. 2023. Port-Hamiltonian formulation and structure-preserving discretization of hyperelastic strings. ECCOMAS Thematic Conference on Multibody Dynamics, Lisboa.
- [Kotyczka, P. & Lefèvre, L. Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters vol. 133 104530 (2019)](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics vol. 361 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- Kuchta, M. Assembly of Multiscale Linear PDE Operators. Lecture Notes in Computational Science and Engineering 641–650 (2020) doi:10.1007/978-3-030-55874-1_63 -- [10.1007/978-3-030-55874-1_63](https://doi.org/10.1007/978-3-030-55874-1_63)
- Kunkel, P. & Mehrmann, V. Differential-Algebraic Equations. EMS Textbooks in Mathematics (2006) doi:10.4171/017 -- [10.4171/017](https://doi.org/10.4171/017)
- [Le Gorrec, Y., Zwart, H. & Maschke, B. Dirac structures and Boundary Control Systems associated with Skew-Symmetric Differential Operators. SIAM Journal on Control and Optimization vol. 44 1864–1892 (2005)](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- Leis, R. Initial Boundary Value Problems in Mathematical Physics. (Vieweg+Teubner Verlag, 1986). doi:10.1007/978-3-663-10649-4 -- [10.1007/978-3-663-10649-4](https://doi.org/10.1007/978-3-663-10649-4)
- Automated Solution of Differential Equations by the Finite Element Method. Lecture Notes in Computational Science and Engineering (Springer Berlin Heidelberg, 2012). doi:10.1007/978-3-642-23099-8 -- [10.1007/978-3-642-23099-8](https://doi.org/10.1007/978-3-642-23099-8)
- [Macchelli, A., Melchiorri, C. & Stramigioli, S. Port-Based Modeling and Simulation of Mechanical Systems With Rigid and Flexible Links. IEEE Transactions on Robotics vol. 25 1016–1029 (2009)](port-based-modeling-and-simulation-of-mechanical-systems-with-rigid-and-flexible-links) -- [10.1109/TRO.2009.2026504](https://doi.org/10.1109/TRO.2009.2026504)
- Makridakis, Ch. G. On mixed finite element methods for linear elastodynamics. Numerische Mathematik vol. 61 235–260 (1992) -- [10.1007/BF01385506](https://doi.org/10.1007/BF01385506)
- [Maschke, B. M. & van der Schaft, A. J. Port-Controlled Hamiltonian Systems: Modelling Origins and Systemtheoretic Properties. IFAC Proceedings Volumes vol. 25 359–365 (1992)](port-controlled-hamiltonian-systems-modelling-origins-and-systemtheoretic-properties-92) -- [10.1016/S1474-6670(17)52308-3](https://doi.org/10.1016/S1474-6670(17)52308-3)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/S0962492922000083](https://doi.org/10.1017/S0962492922000083)
- Rashad, R., Brugnoli, A., Califano, F., Luesink, E. & Stramigioli, S. Intrinsic Nonlinear Elasticity: An Exterior Calculus Formulation. Journal of Nonlinear Science vol. 33 (2023) -- [10.1007/s00332-023-09945-7](https://doi.org/10.1007/s00332-023-09945-7)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Scovazzi, G., Song, T. & Zeng, X. A velocity/stress mixed stabilized nodal finite element for elastodynamics: Analysis and computations with strongly and weakly enforced boundary conditions. Computer Methods in Applied Mechanics and Engineering vol. 325 532–576 (2017) -- [10.1016/j.cma.2017.07.018](https://doi.org/10.1016/j.cma.2017.07.018)
- [Thoma, T. & Kotyczka, P. Port-Hamiltonian FE models for filaments. IFAC-PapersOnLine vol. 55 353–358 (2022)](port-hamiltonian-fe-models-for-filaments) -- [10.1016/j.ifacol.2022.11.078](https://doi.org/10.1016/j.ifacol.2022.11.078)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3)
- [Wang, M. & Kotyczka, P. Trajectory control of an elastic beam based on port-Hamiltonian numerical models. at - Automatisierungstechnik vol. 69 457–471 (2021)](trajectory-control-of-an-elastic-beam-based-on-port-hamiltonian-numerical-models) -- [10.1515/auto-2020-0159](https://doi.org/10.1515/auto-2020-0159)
- [Warsewa, A., Böhm, M., Sawodny, O. & Tarín, C. A port-Hamiltonian approach to modeling the structural dynamics of complex systems. Applied Mathematical Modelling vol. 89 1528–1546 (2021)](a-port-hamiltonian-approach-to-modeling-the-structural-dynamics-of-complex-systems) -- [10.1016/j.apm.2020.07.038](https://doi.org/10.1016/j.apm.2020.07.038)
- Wriggers P. 2008. Nonlinear finite element methods. Berlin: Springer-Verlag.
- Zhang, B., Yang, Y. & Feng, M. Mixed virtual element methods for elastodynamics with weak symmetry. Journal of Computational and Applied Mathematics vol. 353 49–71 (2019) -- [10.1016/j.cam.2018.12.020](https://doi.org/10.1016/j.cam.2018.12.020)

