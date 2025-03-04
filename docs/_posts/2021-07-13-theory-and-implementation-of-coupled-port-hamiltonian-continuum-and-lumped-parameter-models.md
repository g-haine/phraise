---
layout: post
title: "Theory and Implementation of Coupled Port-Hamiltonian Continuum and Lumped Parameter Models"
date: 2021-07-13 00:00:00 +0100
permalink: theory-and-implementation-of-coupled-port-hamiltonian-continuum-and-lumped-parameter-models
year: 2021
authors: Finbar J. Argus, Chris P. Bradley, Peter J. Hunter
category: journal-article
tag: Port-Hamiltonian; Modelling; PDE; FEniCS; Hamiltonian; Finite element; Galerkin; Symplectic; Lumped parameter; Continuum; Monolithic; Bond graph; 65P10; 35L05, 74F99, 65M60
---
 
## Authors
[Finbar J. Argus](authors/finbar-j-argus), [Chris P. Bradley](authors/chris-p-bradley), [Peter J. Hunter](authors/peter-j-hunter)
 
## Abstract
A continuous Galerkin finite element method that allows mixed boundary conditions without the need for Lagrange multipliers or user-defined parameters is developed. A mixed coupling of Lagrange and Raviart-Thomas basis functions are used. The method is proven to have a Hamiltonian-conserving spatial discretisation and a symplectic time discretisation. The energy residual is therefore guaranteed to be bounded for general problems and exactly conserved for linear problems. The linear 2D wave equation is discretised and modelled by making use of a port-Hamiltonian framework. This model is verified against an analytic solution and shown to have standard order of convergence for the temporal and spatial discretisation. The error growth over time is shown to grow linearly for this symplectic method, which agrees with theoretical results. A modal analysis is performed which verifies that the eigenvalues of the model accurately converge to the exact eigenvalues, as the mesh is refined. The port-Hamiltonian framework allows boundary coupling with bond-graph or, more generally, lumped parameter models, therefore unifying the two fields of lumped parameter modelling and continuum modelling of Hamiltonian systems. The wave domain discretisation is shown to be equivalent to a coupling of canonical port-Hamiltonian forms. This feature allows the model to have mixed boundary conditions as well as to have mixed causality interconnections with other port-Hamiltonian models. A model of the 2D wave equation is coupled, in a monolithic manner, with a lumped parameter model of an electromechanical linear actuator. The combined model is also verified to conserve energy exactly.
 
## Keywords
Port-Hamiltonian; Modelling; PDE; FEniCS; Hamiltonian; Finite element; Galerkin; Symplectic; Lumped parameter; Continuum; Monolithic; Bond graph; 65P10; 35L05, 74F99, 65M60
 
## Citation
- **Journal:** Journal of Elasticity
- **Year:** 2021
- **Volume:** 145
- **Issue:** 1-2
- **Pages:** 339--382
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10659-021-09846-4](https://doi.org/10.1007/s10659-021-09846-4)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Argus_2021,
  title={{Theory and Implementation of Coupled Port-Hamiltonian Continuum and Lumped Parameter Models}},
  volume={145},
  ISSN={1573-2681},
  DOI={10.1007/s10659-021-09846-4},
  number={1–2},
  journal={Journal of Elasticity},
  publisher={Springer Science and Business Media LLC},
  author={Argus, Finbar J. and Bradley, Chris P. and Hunter, Peter J.},
  year={2021},
  pages={339--382}
}
{% endraw %}
{% endhighlight %}
 
## References
- Alnæs, M., Blechta, J., Hake, J., Johansson, A., Kehlet, B., Logg, A., Richardson, C., Ring, J., Rognes, M.E., Wells, G.N.: The FEniCS Project Version 1.5. Arch. Numer. Softw. 3(100) (2015). https://doi.org/10.11588/ans.2015.100.20553 -- [10.11588/ans.2015.100.20553](https://doi.org/10.11588/ans.2015.100.20553)
- Bauer, W., Cotter, C.J.: Energy-enstrophy conserving compatible finite element schemes for the rotating shallow water equations with slip boundary conditions. J. Comput. Phys. 373, 171–187 (2018). https://doi.org/10.1016/j.jcp.2018.06.071 -- [10.1016/j.jcp.2018.06.071](https://doi.org/10.1016/j.jcp.2018.06.071)
- Bazilevs, Y., Hughes, T.J.: Weak imposition of Dirichlet boundary conditions in fluid mechanics. Comput. Fluids 36(1), 12–26 (2007). https://doi.org/10.1016/j.compfluid.2005.07.012 -- [10.1016/j.compfluid.2005.07.012](https://doi.org/10.1016/j.compfluid.2005.07.012)
- Brezzi, F., Fortin, M.: Mixed and hybrid finite element methods, SIAM Rev. 3 (1993). https://doi.org/10.1137/1035113 -- [10.1137/1035113](https://doi.org/10.1137/1035113)
- Brugnano, L., Frasca Caccia, G., Iavernaro, F.: Energy conservation issues in the numerical solution of the semilinear wave equation. Appl. Math. Comput. 270, 842–870 (2015). https://doi.org/10.1016/j.amc.2015.08.078 -- [10.1016/j.amc.2015.08.078](https://doi.org/10.1016/j.amc.2015.08.078)
- Brugnoli, A., Alazard, D., Pommier-Budinger, V., Matignon, D.: Interconnection of the Kirchhoff plate within the port-Hamiltonian framework. In: IEEE Conference on Decision and Control, vol. 58, pp. 6857–6862 (2019). https://doi.org/10.1109/CDC40024.2019.9029487 -- [10.1109/CDC40024.2019.9029487](https://doi.org/10.1109/CDC40024.2019.9029487)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V., Matignon, D.: Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Appl. Math. Model. 75, 940–960 (2019). https://doi.org/10.1016/j.apm.2019.04.035](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V., Matignon, D.: Port-Hamiltonian formulation and symplectic discretization of plate models Part II: Kirchhoff model for thin plates. Appl. Math. Model. 75, 961–981 (2019). https://doi.org/10.1016/j.apm.2019.04.036](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-ii-kirchhoff-model-for-thin-plates) -- [10.1016/j.apm.2019.04.036](https://doi.org/10.1016/j.apm.2019.04.036)
- Brugnoli, A., Cardoso-Ribeiro, F.L., Haine, G., Kotyczka, P.: Partitioned finite element method for power-preserving structured discretization with mixed boundary conditions. In: Proceedings of the 21st IFAC. World Congress, ??? (2020)
- [Cardoso-Ribeiro, F.L., Matignon, D., Lefèvre, L.: A structure-preserving Partitioned Finite Element Method for the 2D wave equation. IFAC-PapersOnLine 51(3), 119–124 (2018). https://doi.org/10.1016/j.ifacol.2018.06.033](a-structure-preserving-partitioned-finite-element-method-for-the-2d-wave-equation) -- [10.1016/j.ifacol.2018.06.033](https://doi.org/10.1016/j.ifacol.2018.06.033)
- [Cardoso-Ribeiro, F.L., Matignon, D., Lefèvre, L.: A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA J. Math. Control Inf. 38(2), 493–533 (2020). https://doi.org/10.1093/imamci/dnaa038](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Cockburn, B., Gopalakrishnan, J., Lazarov, R.: Unified hybridization of discontinuous Galerkin, mixed, and continuous Galerkin methods for second order elliptic problems. SIAM J. Numer. Anal. 47(2), 1319–1365 (2009). https://doi.org/10.1137/070706616 -- [10.1137/070706616](https://doi.org/10.1137/070706616)
- Duck, F.: Tissue non-linearity. J. Eng. Med. 224(2), 155–170 (2010). https://doi.org/10.1243/09544119JEIM574 -- [10.1243/09544119JEIM574](https://doi.org/10.1243/09544119JEIM574)
- [Duindam, V., Macchelli, A., Stramigioli, S., Bruyninckx, H.: Modeling and Control of Complex Physical Systems: The Port-Hamiltonian Approach (2009). https://doi.org/10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Eldred, C., Dubos, T., Kritsikis, E.: A quasi-Hamiltonian discretization of the thermal shallow water equations. J. Comput. Phys. 379, 1–31 (2019). https://doi.org/10.1016/j.jcp.2018.10.038 -- [10.1016/j.jcp.2018.10.038](https://doi.org/10.1016/j.jcp.2018.10.038)
- Gawthrop, P.J., Bevan, G.P.: Bond-graph modeling. IEEE Control Syst. Mag. 27(2), 24–45 (2007). https://doi.org/10.1109/MCS.2007.338279 -- [10.1109/MCS.2007.338279](https://doi.org/10.1109/MCS.2007.338279)
- [Golo, G., Talasila, V., Van der Schaft, A., Maschke, B.: Hamiltonian discretization of boundary control systems. Automatica 40(5), 757–771 (2004). https://doi.org/10.1016/j.automatica.2003.12.017](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Hairer, E., Lubich, C.: Symmetric multistep methods over long times. Numer. Math. 97(4), 699–723 (2004). https://doi.org/10.1007/s00211-004-0520-2 -- [10.1007/s00211-004-0520-2](https://doi.org/10.1007/s00211-004-0520-2)
- [Hairer, E., Lubich, C., Wanner, G.: Geometric numerical integration illustrated by the Störmer-Verlet method. Acta Numer. 12, 399–450 (2003). https://doi.org/10.1017/S0962492902000144](geometric-numerical-integration-illustrated-by-the-stormer-verlet-method) -- [10.1017/S0962492902000144](https://doi.org/10.1017/S0962492902000144)
- Hairer, E., Lubich, C., Wanner, G.: Geometric Numerical Integration - Structure-Preserving Algorithms for Ordinary Differential Equations (2006). https://doi.org/10.1007/3-540-30666-8 -- [10.1007/3-540-30666-8](https://doi.org/10.1007/3-540-30666-8)
- Joly, P.: Variational methods for time-dependent wave propagation problems. In: Topics in Computational Wave Propagation, pp. 201–264 (2003) -- [10.1007/978-3-642-55483-4_6](https://doi.org/10.1007/978-3-642-55483-4_6)
- Kotyczka, P.: Numerical Methods for Distributed Parameter Port-Hamiltonian Systems (2019). https://doi.org/10.14459/2019md1510230 -- [10.14459/2019md1510230](https://doi.org/10.14459/2019md1510230)
- [Kotyczka, P., Lefèvre, L.: Discrete-time port-Hamiltonian systems: a definition based on symplectic integration. Syst. Control Lett. 133, 104530 (2018)](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- [Kotyczka, P., Maschke, B., Lefèvre, L.: Weak form of Stokes-Dirac structures and geometric discretization of port-Hamiltonian systems. J. Comput. Phys. 361, 442–476 (2018). https://doi.org/10.1016/j.jcp.2018.02.006](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- Lindell, I., Sihvola, A.: General boundary conditions. Bound. Conditions Electromagn. 78(267), 101–141 (2019). https://doi.org/10.1002/9781119632429.ch5 -- [10.1002/9781119632429.ch5](https://doi.org/10.1002/9781119632429.ch5)
- Logg, A., Mardal, K.A., Wells, G.: Automated Solution of Differential Equations by the Finite Element Method: The FEniCS Book, vol. 84. Springer, ??? (2012). https://doi.org/10.1007/978-3-642-23099-8 -- [10.1007/978-3-642-23099-8](https://doi.org/10.1007/978-3-642-23099-8)
- McDonald, F., McLachlan, R.I., Moore, B.E., Quispel, G.R.: Travelling wave solutions of multisymplectic discretizations of semi-linear wave equations. J. Differ. Equ. Appl. 22(7), 913–940 (2016). https://doi.org/10.1080/10236198.2016.1162161 -- [10.1080/10236198.2016.1162161](https://doi.org/10.1080/10236198.2016.1162161)
- McLachlan, R.: Symplectic integration of Hamiltonian wave equations. Numer. Math. 66, 465–492 (1993). https://doi.org/10.1007/BF01385708 -- [10.1007/BF01385708](https://doi.org/10.1007/BF01385708)
- McLachlan, R.I., Stern, A.: Multisymplecticity of hybridizable discontinuous Galerkin methods. Found. Comput. Math. 20(1), 35–69 (2020). https://doi.org/10.1007/s10208-019-09415-1 -- [10.1007/s10208-019-09415-1](https://doi.org/10.1007/s10208-019-09415-1)
- Nitsche, J.: Über ein Variationsprinzip zur Lösung von Dirichlet-Problemen bei Verwendung von Teilräumen, die keinen Randbedingungen unterworfen sind. In: Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg, vol. 36, pp. 9–15 (1971). https://doi.org/10.1007/BF02995904 -- [10.1007/BF02995904](https://doi.org/10.1007/BF02995904)
- Ophir, J., Céspedes, I., Ponnekanti, H., Yazdi, Y., Li, X.: Elastography: a quantitative method for imaging the elasticity of biological tissues. Ultrason. Imag. 13(2), 111–134 (1991). https://doi.org/10.1177/016173469101300201 -- [10.1177/016173469101300201](https://doi.org/10.1177/016173469101300201)
- Polyanin, A.D.: Handbook of Linear Partial Differential Equations for Engineers and Scientists, vol. 40 (2002). https://doi.org/10.5860/choice.40-0964 -- [10.5860/choice.40-0964](https://doi.org/10.5860/choice.40-0964)
- Raviart, P.A., Thomas, J.M.: A mixed finite element method for 2nd order elliptic problems. In: Mathematical Aspects of Finite Element Methods, pp. 292–315. Springer, Berlin (1977). https://doi.org/10.1007/bfb0064470 -- [10.1007/bfb0064470](https://doi.org/10.1007/bfb0064470)
- Reich, S.: Multi-symplectic Runge-Kutta collocation methods for Hamiltonian wave equations. J. Comput. Phys. 157(2), 473–499 (2000). https://doi.org/10.1006/jcph.1999.6372 -- [10.1006/jcph.1999.6372](https://doi.org/10.1006/jcph.1999.6372)
- Sadjina, S., Kyllingstad, L.T., Skjong, S., Pedersen, E.: Energy conservation and power bonds in co-simulations: non-iterative adaptive step size control and error estimation. Eng. Comput. 33(3), 607–620 (2017). https://doi.org/10.1007/s00366-016-0492-8 -- [10.1007/s00366-016-0492-8](https://doi.org/10.1007/s00366-016-0492-8)
- [Sánchez, M.A., Ciuca, C., Nguyen, N.C., Peraire, J., Cockburn, B.: Symplectic Hamiltonian HDG methods for wave propagation phenomena. J. Comput. Phys. 350, 951–973 (2017). https://doi.org/10.1016/j.jcp.2017.09.010](symplectic-hamiltonian-hdg-methods-for-wave-propagation-phenomena) -- [10.1016/j.jcp.2017.09.010](https://doi.org/10.1016/j.jcp.2017.09.010)
- Scovazzi, G., Carnes, B.: Weak boundary conditions for wave propagation problems in confined domains: formulation and implementation using a variational multiscale method. Comput. Methods Appl. Mech. Eng. 221, 117–131 (2012). https://doi.org/10.1016/j.cma.2012.01.018 -- [10.1016/j.cma.2012.01.018](https://doi.org/10.1016/j.cma.2012.01.018)
- [Serhani, A., Matignon, D., Haine, G.: Partitioned finite element method for port-Hamiltonian systems with boundary damping: anisotropic heterogeneous 2D wave equations. IFAC-PapersOnLine 52, 96–101 (2019). https://doi.org/10.1016/j.ifacol.2019.08.017](partitioned-finite-element-method-for-port-hamiltonian-systems-with-boundary-damping-anisotropic-heterogeneous-2d-wave-equations) -- [10.1016/j.ifacol.2019.08.017](https://doi.org/10.1016/j.ifacol.2019.08.017)
- Süli, E., Mayers, D.F.: An Introduction to Numerical Analysis (2003) -- [10.1017/CBO9780511801181](https://doi.org/10.1017/CBO9780511801181)
- [Trenchant, V., Fares, Y., Ramirez, H., Gorrec, Y.L., Ouisse, M.: A port-Hamiltonian formulation of a 2D boundary controlled acoustic system. IFAC-PapersOnLine 28(13), 235–240 (2015). https://doi.org/10.1016/j.ifacol.2015.10.245](a-port-hamiltonian-formulation-of-a-2d-boundary-controlled-acoustic-system) -- [10.1016/j.ifacol.2015.10.245](https://doi.org/10.1016/j.ifacol.2015.10.245)
- [Trenchant, V., Ramirez, H., Le Gorrec, Y., Kotyczka, P.: Structure preserving spatial discretization of 2D hyperbolic systems using staggered grids finite difference. In: Proceedings of the American Control Conference, pp. 2491–2496 (2017). https://doi.org/10.23919/ACC.2017.7963327](structure-preserving-spatial-discretization-of-2d-hyperbolic-systems-using-staggered-grids-finite-difference) -- [10.23919/ACC.2017.7963327](https://doi.org/10.23919/ACC.2017.7963327)
- [Van Der Schaft, A., Jeltsema, D.: In: Port-Hamiltonian Systems Theory: An Introductory Overview, pp. 2–3 (2014). https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Van Der Schaft, A.J., Maschke, B.M.: Hamiltonian formulation of distributed-parameter systems with boundary energy flow. J. Geom. Phys. 42(1–2), 166–194 (2002). https://doi.org/10.1016/S0393-0440(01)00083-3](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3)
- [Vu, N.M.T., Lefèvre, L., Nouailletas, R., Brémond, S.: Symplectic spatial integration schemes for systems of balance equations. J. Process Control 51, 1–17 (2017). https://doi.org/10.1016/j.jprocont.2016.12.005](symplectic-spatial-integration-schemes-for-systems-of-balance-equations) -- [10.1016/j.jprocont.2016.12.005](https://doi.org/10.1016/j.jprocont.2016.12.005)
- Zhai, Z., Chen, Q.: Solution characters of iterative coupling between energy simulation and CFD programs. Energy Build. 35(5), 493–505 (2003). https://doi.org/10.1016/S0378-7788(02)00156-1 -- [10.1016/S0378-7788(02)00156-1](https://doi.org/10.1016/S0378-7788(02)00156-1)

