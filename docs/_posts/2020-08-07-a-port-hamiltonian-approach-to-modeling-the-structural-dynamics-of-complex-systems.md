---
layout: post
title: "A port-Hamiltonian approach to modeling the structural dynamics of complex systems"
date: 2020-08-07 00:00:00 +0100
permalink: a-port-hamiltonian-approach-to-modeling-the-structural-dynamics-of-complex-systems
year: 2021
authors: Alexander Warsewa, Michael Böhm, Oliver Sawodny, Cristina Tarín
category: articles
tags:
  - Port-Hamiltonian systems
  - Modeling
  - Finite element
  - Structural dynamics
  - Adaptive structures
---
 
## Authors
[Alexander Warsewa](authors/alexander-warsewa), [Michael Böhm](authors/michael-bohm), [Oliver Sawodny](authors/oliver-sawodny), [Cristina Tarín](authors/cristina-tarin)
 
## Abstract
With this contribution, we give a complete and comprehensive framework for modeling the dynamics of complex mechanical structures as port-Hamiltonian systems. This is motivated by research on the potential of lightweight construction using active load-bearing elements integrated into the structure. Such adaptive structures are of high complexity and very heterogeneous in nature. Port-Hamiltonian systems theory provides a promising approach for their modeling and control. Subsystem dynamics can be formulated in a domain-independent way and interconnected by means of power flows. The modular approach is also suitable for robust decentralized control schemes. Starting from a distributed-parameter port-Hamiltonian formulation of beam dynamics, we show the application of an existing structure-preserving mixed finite element method to arrive at finite-dimensional approximations. In contrast to the modeling of single bodies with a single boundary, we consider complex structures composed of many simple elements interconnected at the boundary. This is analogous to the usual way of modeling civil engineering structures which has not been transferred to port-Hamiltonian systems before. A block diagram representation of the interconnected systems is used to generate coupling constraints which leads to differential algebraic equations of index one. After the elimination of algebraic constraints, systems in input-state-output (ISO) port-Hamiltonian form are obtained. Port-Hamiltonian system models for the considered class of systems can also be constructed from the mass and stiffness matrices obtained via conventional finite element methods. We show how this relates to the presented approach and discuss the differences, promoting a better understanding across engineering disciplines. A Matlab framework is available on http://github.com/awarsewa/ph_fem/ to facilitate the application of the methods to different problems.
 
## Keywords
Port-Hamiltonian systems; Modeling; Finite element; Structural dynamics; Adaptive structures
 
## Citation
- **Journal:** Applied Mathematical Modelling
- **Year:** 2021
- **Volume:** 89
- **Issue:** 
- **Pages:** 1528--1546
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.apm.2020.07.038](https://doi.org/10.1016/j.apm.2020.07.038)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Warsewa_2021,
  title={{A port-Hamiltonian approach to modeling the structural dynamics of complex systems}},
  volume={89},
  ISSN={0307-904X},
  DOI={10.1016/j.apm.2020.07.038},
  journal={Applied Mathematical Modelling},
  publisher={Elsevier BV},
  author={Warsewa, Alexander and Böhm, Michael and Sawodny, Oliver and Tarín, Cristina},
  year={2021},
  pages={1528--1546}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-port-hamiltonian-approach-to-modeling-the-structural-dynamics-of-complex-systems.bib)
 
## References
- Korkmaz, S. A review of active structural control: challenges for engineering informatics. Computers &amp; Structures vol. 89 2113–2132 (2011) -- [10.1016/j.compstruc.2011.07.010](https://doi.org/10.1016/j.compstruc.2011.07.010)
- Sobek, W. Ultraleichtbau. Stahlbau vol. 83 784–789 (2014) -- [10.1002/stab.201410211](https://doi.org/10.1002/stab.201410211)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Zwart, Distributed-Parameter port-Hamiltonian Systems. CIMPA (2009)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- Quarteroni, (2008)
- Schwertassek, (2017)
- Hughes, (2012)
- Talasila, The wave equation as a port-Hamiltonian system and a finite dimensional approximation. (2002)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Bassi, An algorithm to discretize one-dimensional distributed port-Hamiltonian systems. (2007)
- Baaiu, A., Couenne, F., Lefevre, L., Le Gorrec, Y. & Tayakout, M. Structure-preserving infinite dimensional model reduction: Application to adsorption processes. Journal of Process Control vol. 19 394–404 (2009) -- [10.1016/j.jprocont.2008.07.002](https://doi.org/10.1016/j.jprocont.2008.07.002)
- [Moulla, R., Lefévre, L. & Maschke, B. Pseudo-spectral methods for the spatial symplectic reduction of open systems of conservation laws. Journal of Computational Physics vol. 231 1272–1292 (2012)](pseudo-spectral-methods-for-the-spatial-symplectic-reduction-of-open-systems-of-conservation-laws) -- [10.1016/j.jcp.2011.10.008](https://doi.org/10.1016/j.jcp.2011.10.008)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Pommier-Budinger, V. Piezoelectric beam with distributed control ports: a power-preserving discretization using weak formulation.. IFAC-PapersOnLine vol. 49 290–297 (2016)](piezoelectric-beam-with-distributed-control-ports-a-power-preserving-discretization-using-weak-formulation) -- [10.1016/j.ifacol.2016.07.456](https://doi.org/10.1016/j.ifacol.2016.07.456)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics vol. 361 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A structure-preserving Partitioned Finite Element Method for the 2D wave equation. IFAC-PapersOnLine vol. 51 119–124 (2018)](a-structure-preserving-partitioned-finite-element-method-for-the-2d-wave-equation) -- [10.1016/j.ifacol.2018.06.033](https://doi.org/10.1016/j.ifacol.2018.06.033)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Applied Mathematical Modelling vol. 75 940–960 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part II: Kirchhoff model for thin plates. Applied Mathematical Modelling vol. 75 961–981 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-ii-kirchhoff-model-for-thin-plates) -- [10.1016/j.apm.2019.04.036](https://doi.org/10.1016/j.apm.2019.04.036)
- Li, R., Tian, Y., Wang, P., Shi, Y. & Wang, B. New analytic free vibration solutions of rectangular thin plates resting on multiple point supports. International Journal of Mechanical Sciences vol. 110 53–61 (2016) -- [10.1016/j.ijmecsci.2016.03.002](https://doi.org/10.1016/j.ijmecsci.2016.03.002)
- Li, R. et al. New analytic buckling solutions of rectangular thin plates with all edges free. International Journal of Mechanical Sciences vol. 144 67–73 (2018) -- [10.1016/j.ijmecsci.2018.05.041](https://doi.org/10.1016/j.ijmecsci.2018.05.041)
- Li, R., Zheng, X., Yang, Y., Huang, M. & Huang, X. Hamiltonian system-based new analytic free vibration solutions of cylindrical shell panels. Applied Mathematical Modelling vol. 76 900–917 (2019) -- [10.1016/j.apm.2019.07.020](https://doi.org/10.1016/j.apm.2019.07.020)
- [Le Gorrec, Y., Zwart, H. & Maschke, B. Dirac structures and Boundary Control Systems associated with Skew-Symmetric Differential Operators. SIAM Journal on Control and Optimization vol. 44 1864–1892 (2005)](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- [Macchelli, A. & Melchiorri, C. Modeling and Control of the Timoshenko Beam. The Distributed Port Hamiltonian Approach. SIAM Journal on Control and Optimization vol. 43 743–767 (2004)](modeling-and-control-of-the-timoshenko-beam-the-distributed-port-hamiltonian-approach) -- [10.1137/s0363012903429530](https://doi.org/10.1137/s0363012903429530)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Pommier-Budinger, V. Modeling of a Fluid-structure coupled system using port-Hamiltonian formulation. IFAC-PapersOnLine vol. 48 217–222 (2015)](modeling-of-a-fluid-structure-coupled-system-using-port-hamiltonian-formulation) -- [10.1016/j.ifacol.2015.10.242](https://doi.org/10.1016/j.ifacol.2015.10.242)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information vol. 38 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Schnell, (2006)
- Van der Schaft, Port-Hamiltonian differential-algebraic systems. (2013)
- Cardoso Ribeiro, (2016)
- [Wu, Y., Hamroun, B., Gorrec, Y. L. & Maschke, B. Port Hamiltonian System in Descriptor Form for Balanced Reduction: Application to a Nanotweezer. IFAC Proceedings Volumes vol. 47 11404–11409 (2014)](port-hamiltonian-system-in-descriptor-form-for-balanced-reduction-application-to-a-nanotweezer) -- [10.3182/20140824-6-za-1003.01579](https://doi.org/10.3182/20140824-6-za-1003.01579)
- Böhm, Input modeling for active structural elements extending the established FE-workflow for modeling of adaptive structures. (2020)
- [Kugi, A. & Kemmetmüller, W. New Energy-based Nonlinear Controller for Hydraulic Piston Actuators. European Journal of Control vol. 10 163–173 (2004)](new-energy-based-nonlinear-controller-for-hydraulic-piston-actuators) -- [10.3166/ejc.10.163-173](https://doi.org/10.3166/ejc.10.163-173)
- Kugi, Energy based modelling of lumped-parameter hydraulic systems. (2003)
- Duindam, (2009)

