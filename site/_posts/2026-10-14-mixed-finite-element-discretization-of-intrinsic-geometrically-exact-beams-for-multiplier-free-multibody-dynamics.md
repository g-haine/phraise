---
title: "Mixed finite element discretization of intrinsic geometrically exact beams for multiplier-free multibody dynamics"
date: 2026-10-14 00:00:00 +0100
permalink: mixed-finite-element-discretization-of-intrinsic-geometrically-exact-beams-for-multiplier-free-multibody-dynamics
year: 2026
authors: Andrea Brugnoli, Phi L. Kinon, Francesco Sanfedino, Peter Betsch, Olivier A. Bauchau
category: articles
tags:
  - geometrically exact beams, mixed finite elements, multibody dynamics, port-hamiltonian systems, structure preserving discretization
---
 
## Authors
[Andrea Brugnoli](authors/andrea-brugnoli), [Phi L. Kinon](authors/philipp-l-kinon), [Francesco Sanfedino](authors/francesco-sanfedino), [Peter Betsch](authors/peter-betsch), [Olivier A. Bauchau](authors/olivier-a-bauchau)
 
## Abstract
The Reissner-Simo and Hodges models are two equivalent continuous descriptions of finite-strain beam dynamics. The Reissner-Simo formulation uses displacements and rotations, while the Hodges formulation is intrinsic and avoids both variables. Although equivalent in theory, the two approaches behave differently after discretization and offer distinct numerical advantages. In this work, we develop a structure-preserving discretization of the intrinsic planar beam formulation. Because the intrinsic equations involve linear differential operators, both kinematic and dynamic boundary conditions can be imposed naturally using mixed finite elements. The resulting formulation also enables multibody systems to be assembled without algebraic constraints, avoiding the stiff differential-algebraic equations typically introduced by kinematic constraints. We demonstrate the approach on different examples, also showing that closed kinematic loops can be modeled without algebraic constraints. The resulting interconnected systems retain a port-Hamiltonian structure, with all nonlinearities confined to the interconnection operator. This structure allows exact energy preservation when combined with implicit midpoint time integration. Furthermore the scheme appears to require less Newton iterations compared to existing energy preserving scheme.
 
## Keywords
geometrically exact beams, mixed finite elements, multibody dynamics, port-hamiltonian systems, structure preserving discretization
 
## Citation
- **Journal:** Mechanism and Machine Theory
- **Year:** 2026
- **Volume:** 231
- **Issue:** 
- **Pages:** 106654
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.mechmachtheory.2026.106654](https://doi.org/10.1016/j.mechmachtheory.2026.106654)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Brugnoli_2026,
  title={{Mixed finite element discretization of intrinsic geometrically exact beams for multiplier-free multibody dynamics}},
  volume={231},
  ISSN={0094-114X},
  DOI={10.1016/j.mechmachtheory.2026.106654},
  journal={Mechanism and Machine Theory},
  publisher={Elsevier BV},
  author={Brugnoli, Andrea and Kinon, Phi L. and Sanfedino, Francesco and Betsch, Peter and Bauchau, Olivier A.},
  year={2026},
  pages={106654}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/mixed-finite-element-discretization-of-intrinsic-geometrically-exact-beams-for-multiplier-free-multibody-dynamics.bib)
 
## References
- Albu-Schaffer A, Eiberger O, Grebenstein M, Haddadin S, Ott C, Wimbock T, Wolf S, Hirzinger G (2008) Soft robotics. IEEE Robot Automat Mag 15(3):20–30. https://doi.org/10.1109/mra.2008.927979 -- [10.1109/mra.2008.927979](https://doi.org/10.1109/mra.2008.927979)
- Omisore OM, Han S, Xiong J, Li H, Li Z, Wang L (2022) A Review on Flexible Robotic Systems for Minimally Invasive Surgery. IEEE Trans Syst Man Cybern, Syst 52(1):631–644. https://doi.org/10.1109/tsmc.2020.3026174 -- [10.1109/tsmc.2020.3026174](https://doi.org/10.1109/tsmc.2020.3026174)
- Chang C-S, Hodges DH, Patil MJ (2008) Flight Dynamics of Highly Flexible Aircraft. Journal of Aircraft 45(2):538–545. https://doi.org/10.2514/1.30890 -- [10.2514/1.30890](https://doi.org/10.2514/1.30890)
- Chu Y-J, Lam H-F (2020) Comparative study of the performances of a bio-inspired flexible-bladed wind turbine and a rigid-bladed wind turbine in centimeter-scale. Energy 213:118835. https://doi.org/10.1016/j.energy.2020.118835 -- [10.1016/j.energy.2020.118835](https://doi.org/10.1016/j.energy.2020.118835)
- Chen R, Zhou L, Wu K, Liu L, Liu Y, Li X, Chen G, Zheng G, Luo J (2024) A general framework for designing compliant deployable mechanisms via geometrically exact beam theory. Mechanism and Machine Theory 202:105778. https://doi.org/10.1016/j.mechmachtheory.2024.105778 -- [10.1016/j.mechmachtheory.2024.105778](https://doi.org/10.1016/j.mechmachtheory.2024.105778)
- Reissner E (1972) On one-dimensional finite-strain beam theory: The plane problem. Journal of Applied Mathematics and Physics (ZAMP) 23(5):795–804. https://doi.org/10.1007/bf01602645 -- [10.1007/bf01602645](https://doi.org/10.1007/bf01602645)
- Simo JC (1985) A finite strain beam formulation. The three-dimensional dynamic problem. Part I. Computer Methods in Applied Mechanics and Engineering 49(1):55–70. https://doi.org/10.1016/0045-7825(85)90050-7 -- [10.1016/0045-7825(85)90050-7](https://doi.org/10.1016/0045-7825(85)90050-7)
- Hodges, Geometrically exact, intrinsic theory for dynamics of curved and twisted anisotropic beams. AIAA J. (2003) -- [10.2514/2.2054](https://doi.org/10.2514/2.2054)
- Rodriguez, (2021)
- Palacios R (2011) Nonlinear normal modes in an intrinsic theory of anisotropic beams. Journal of Sound and Vibration 330(8):1772–1792. https://doi.org/10.1016/j.jsv.2010.10.023 -- [10.1016/j.jsv.2010.10.023](https://doi.org/10.1016/j.jsv.2010.10.023)
- Artola M, Wynn A, Palacios R (2022) Modal-Based Nonlinear Model Predictive Control for 3-D Very Flexible Structures. IEEE Trans Automat Contr 67(5):2145–2160. https://doi.org/10.1109/tac.2021.3071326 -- [10.1109/tac.2021.3071326](https://doi.org/10.1109/tac.2021.3071326)
- [Ayala EP, Wu Y, Rabenorosoa K, Le Gorrec Y (2023) Energy-Based Modeling and Control of a Piezotube Actuated Optical Fiber. IEEE/ASME Trans Mechatron 28(1):385–395. https://doi.org/10.1109/tmech.2022.3199566](energy-based-modeling-and-control-of-a-piezotube-actuated-optical-fiber) -- [10.1109/tmech.2022.3199566](https://doi.org/10.1109/tmech.2022.3199566)
- Kinon, Energy-momentum-consistent simulation of planar geometrically exact beams in a port-Hamiltonian framework. Multibody Syst. Dyn. (2025)
- [Ljukovac S, Ibrahimbegovic A, Husic MC (2025) Nonlinear Dynamics and Control of Reissner’s 2D Geometrically Exact Beam by Distributed Port‐Hamiltonian System. Numerical Meth Engineering 126(16). https://doi.org/10.1002/nme.70103](nonlinear-dynamics-and-control-of-reissner-s-2d-geometrically-exact-beam-by-distributed-port-hamiltonian-system) -- [10.1002/nme.70103](https://doi.org/10.1002/nme.70103)
- Khaneh Masjedi P, Jangravi S, Reali A (2025) Isogeometric collocation for locking-free large deflection analysis of geometrically exact beams with intrinsic formulation. Computer Methods in Applied Mechanics and Engineering 446:118282. https://doi.org/10.1016/j.cma.2025.118282 -- [10.1016/j.cma.2025.118282](https://doi.org/10.1016/j.cma.2025.118282)
- Bauchau, (2011)
- Wynn A, Wang Y, Palacios R, Goulart PJ (2013) An energy-preserving description of nonlinear beam vibrations in modal coordinates. Journal of Sound and Vibration 332(21):5543–5558. https://doi.org/10.1016/j.jsv.2013.05.021 -- [10.1016/j.jsv.2013.05.021](https://doi.org/10.1016/j.jsv.2013.05.021)
- [Macchelli A, Melchiorri C, Stramigioli S (2009) Port-Based Modeling and Simulation of Mechanical Systems With Rigid and Flexible Links. IEEE Trans Robot 25(5):1016–1029. https://doi.org/10.1109/tro.2009.2026504](port-based-modeling-and-simulation-of-mechanical-systems-with-rigid-and-flexible-links) -- [10.1109/tro.2009.2026504](https://doi.org/10.1109/tro.2009.2026504)
- [Berger T, Hochdahl R, Reis T, Seifried R (2025) Port-Hamiltonian modeling of rigid multibody systems. Nonlinear Dyn 113(23):32037–32058. https://doi.org/10.1007/s11071-025-11776-y](port-hamiltonian-modeling-of-rigid-multibody-systems) -- [10.1007/s11071-025-11776-y](https://doi.org/10.1007/s11071-025-11776-y)
- [Kinon PL, Eugster SR, Betsch P (2026) Mixed formulation and structure-preserving discretization of Cosserat rod dynamics in a port-Hamiltonian framework. Computer Methods in Applied Mechanics and Engineering 458:118966. https://doi.org/10.1016/j.cma.2026.118966](mixed-formulation-and-structure-preserving-discretization-of-cosserat-rod-dynamics-in-a-port-hamiltonian-framework) -- [10.1016/j.cma.2026.118966](https://doi.org/10.1016/j.cma.2026.118966)
- [Kotyczka P, Lefèvre L (2019) Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems & Control Letters 133:104530. https://doi.org/10.1016/j.sysconle.2019.104530](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- [Brugnoli A, Matignon D, Morlier J (2025) A linearly-implicit energy-momentum preserving scheme for geometrically nonlinear mechanics based on non-canonical Hamiltonian formulations. Nonlinear Dyn 113(20):27539–27566. https://doi.org/10.1007/s11071-025-11601-6](a-linearly-implicit-energy-momentum-preserving-scheme-for-geometrically-nonlinear-mechanics-based-on-non-canonical-hamiltonian-formulations) -- [10.1007/s11071-025-11601-6](https://doi.org/10.1007/s11071-025-11601-6)
- [De Jong S, Brugnoli A, Rashad R, Zhang Y, Stramigioli S (2026) A domain decomposition strategy for natural imposition of mixed boundary conditions in port-Hamiltonian systems. Applied Mathematical Modelling 156:116775. https://doi.org/10.1016/j.apm.2026.116775](a-domain-decomposition-strategy-for-natural-imposition-of-mixed-boundary-conditions-in-port-hamiltonian-systems) -- [10.1016/j.apm.2026.116775](https://doi.org/10.1016/j.apm.2026.116775)
- Herrmann M, Castello D, Breuling J, Garcia IC, Greco L, Eugster SR (2026) A mixed Petrov-Galerkin Cosserat rod finite element formulation. Journal of Theoretical, Computational and Applied Mechanics. https://doi.org/10.46298/jtcam.16002 -- [10.46298/jtcam.16002](https://doi.org/10.46298/jtcam.16002)
- -conforming mixed Bézier FE-formulation for Kirchhoff–Love rods. Mathematics and Mechanics of Solids 29(4):645–685. https://doi.org/10.1177/10812865231204972 -- [10.1177/10812865231204972](https://doi.org/10.1177/10812865231204972)
- Kim JG, Kim YY (1998) A new higher-order hybrid-mixed curved beam element. Int J Numer Meth Engng 43(5):925–940. https://doi.org/10.1002/(sici)1097-0207(19981115)43:5<925::aid-nme457>3.0.co;2-m -- [10.1002/(sici)1097-0207(19981115)43:5<925::aid-nme457>3.0.co;2-m](https://doi.org/10.1002/(sici)1097-0207(19981115)43:5<925::aid-nme457>3.0.co;2-m)
- Santos HAFA, Pimenta PM, Moitinho de Almeida JP (2010) Hybrid and multi-field variational principles for geometrically exact three-dimensional beams. International Journal of Non-Linear Mechanics 45(8):809–820. https://doi.org/10.1016/j.ijnonlinmec.2010.06.003 -- [10.1016/j.ijnonlinmec.2010.06.003](https://doi.org/10.1016/j.ijnonlinmec.2010.06.003)
- [Thoma T, Kotyczka P, Egger H (2024) On the velocity-stress formulation for geometrically nonlinear elastodynamics and its structure-preserving discretization. Mathematical and Computer Modelling of Dynamical Systems 30(1):701–720. https://doi.org/10.1080/13873954.2024.2397486](on-the-velocity-stress-formulation-for-geometrically-nonlinear-elastodynamics-and-its-structure-preserving-discretization) -- [10.1080/13873954.2024.2397486](https://doi.org/10.1080/13873954.2024.2397486)
- Mehrmann, Structure-preserving discretization for port-Hamiltonian descriptor systems. (2019)
- Meier C, Popp A, Wall WA (2017) Geometrically Exact Finite Element Formulations for Slender Beams: Kirchhoff–Love Theory Versus Simo–Reissner Theory. Arch Computat Methods Eng 26(1):163–243. https://doi.org/10.1007/s11831-017-9232-5 -- [10.1007/s11831-017-9232-5](https://doi.org/10.1007/s11831-017-9232-5)
- [Macchelli A, Melchiorri C (2004) Modeling and Control of the Timoshenko Beam. The Distributed Port Hamiltonian Approach. SIAM J Control Optim 43(2):743–767. https://doi.org/10.1137/s0363012903429530](modeling-and-control-of-the-timoshenko-beam-the-distributed-port-hamiltonian-approach) -- [10.1137/s0363012903429530](https://doi.org/10.1137/s0363012903429530)
- [Cardoso-Ribeiro FL, Matignon D, Lefèvre L (2020) A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information 38(2):493–533. https://doi.org/10.1093/imamci/dnaa038](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- [Brugnoli A, Rashad R, Stramigioli S (2022) Dual field structure-preserving discretization of port-Hamiltonian systems using finite element exterior calculus. Journal of Computational Physics 471:111601. https://doi.org/10.1016/j.jcp.2022.111601](dual-field-structure-preserving-discretization-of-port-hamiltonian-systems-using-finite-element-exterior-calculus) -- [10.1016/j.jcp.2022.111601](https://doi.org/10.1016/j.jcp.2022.111601)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Finozzi A, Sanfedino F, Alazard D (2022) Parametric sub-structuring models of large space truss structures for structure/control co-design. Mechanical Systems and Signal Processing 180:109427. https://doi.org/10.1016/j.ymssp.2022.109427 -- [10.1016/j.ymssp.2022.109427](https://doi.org/10.1016/j.ymssp.2022.109427)
- Sanfedino F, Thiébaud G, Alazard D, Guercio N, Deslaef N (2022) Advances in fine line-of-sight control for large space flexible structures. Aerospace Science and Technology 130:107961. https://doi.org/10.1016/j.ast.2022.107961 -- [10.1016/j.ast.2022.107961](https://doi.org/10.1016/j.ast.2022.107961)
- Hesthaven JS, Warburton T (2008) Nodal Discontinuous Galerkin Methods. Springer New York -- [10.1007/978-0-387-72067-8](https://doi.org/10.1007/978-0-387-72067-8)
- [Brugnoli A, Alazard D, Pommier-Budinger V, Matignon D (2020) Port-Hamiltonian flexible multibody dynamics. Multibody Syst Dyn 51(3):343–375. https://doi.org/10.1007/s11044-020-09758-6](port-hamiltonian-flexible-multibody-dynamics) -- [10.1007/s11044-020-09758-6](https://doi.org/10.1007/s11044-020-09758-6)
- Simo JC, Vu-Quoc L (1986) On the Dynamics of Flexible Beams Under Large Overall Motions—The Plane Case: Part I. Journal of Applied Mechanics 53(4):849–854. https://doi.org/10.1115/1.3171870 -- [10.1115/1.3171870](https://doi.org/10.1115/1.3171870)
- Betsch P, Steinmann P (2001) Conservation properties of a time FE method—part II: Time‐stepping schemes for non‐linear elastodynamics. Numerical Meth Engineering 50(8):1931–1955. https://doi.org/10.1002/nme.103 -- [10.1002/nme.103](https://doi.org/10.1002/nme.103)
- J. Bradbury, R. Frostig, P. Hawkins, M.J. Johnson, C. Leary, D. Maclaurin, G. Necula, A. Paszke, J. VanderPlas, S. Wanderman-Milne, Q. Zhang, JAX: composable transformations of Python+NumPy programs, 2018. Version 0.2.5.
- Shabana, (2020)
- Stander N, Stein E (1996) An energy‐conserving planar finite beam element for dynamics of flexible mechanisms. Engineering Computations 13(6):60–85. https://doi.org/10.1108/02644409610128418 -- [10.1108/02644409610128418](https://doi.org/10.1108/02644409610128418)
- Brüls O, Cardona A, Arnold M (2012) Lie group generalized-α time integration of constrained flexible multibody systems. Mechanism and Machine Theory 48:121–137. https://doi.org/10.1016/j.mechmachtheory.2011.07.017 -- [10.1016/j.mechmachtheory.2011.07.017](https://doi.org/10.1016/j.mechmachtheory.2011.07.017)
- Yu Y, Ding X, Zhu JJ (2013) Attitude tracking control of a quadrotor UAV in the exponential coordinates. Journal of the Franklin Institute 350(8):2044–2068. https://doi.org/10.1016/j.jfranklin.2013.05.022 -- [10.1016/j.jfranklin.2013.05.022](https://doi.org/10.1016/j.jfranklin.2013.05.022)
- Müller A (2017) Screw and Lie group theory in multibody kinematics. Multibody Syst Dyn 43(1):37–70. https://doi.org/10.1007/s11044-017-9582-7 -- [10.1007/s11044-017-9582-7](https://doi.org/10.1007/s11044-017-9582-7)
- Todesco J, Brüls O (2023) Highly accurate differentiation of the exponential map and its tangent operator. Mechanism and Machine Theory 190:105451. https://doi.org/10.1016/j.mechmachtheory.2023.105451 -- [10.1016/j.mechmachtheory.2023.105451](https://doi.org/10.1016/j.mechmachtheory.2023.105451)
- Dopico, Direct and adjoint sensitivity analysis of ordinary differential equation multibody formulations. J. Comput. Nonlinear Dyn. (2014)
- Barfoot, (2024)

