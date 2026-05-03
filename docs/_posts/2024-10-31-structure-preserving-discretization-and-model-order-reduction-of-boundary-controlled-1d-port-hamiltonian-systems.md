---
title: "Structure-preserving discretization and model order reduction of boundary-controlled 1D port-Hamiltonian systems"
date: 2024-10-31 00:00:00 +0100
permalink: structure-preserving-discretization-and-model-order-reduction-of-boundary-controlled-1d-port-hamiltonian-systems
year: 2024
authors: Jesus-Pablo Toledo-Zucco, Denis Matignon, Charles Poussot-Vassal, Yann Le Gorrec
category: articles
tags:
  - distributed port-hamiltonian systems, finite element method, loewner framework, structure-preserving discretization methods
---
 
## Authors
[Jesus-Pablo Toledo-Zucco](authors/jesus-pablo-toledo-zucco), [Denis Matignon](authors/denis-matignon), [Charles Poussot-Vassal](authors/charles-poussot-vassal), [Yann Le Gorrec](authors/yann-le-gorrec)
 
## Abstract
This paper presents a systematic methodology for the discretization and reduction of a class of one-dimensional Partial Differential Equations (PDEs) with inputs and outputs collocated at the spatial boundaries. The class of system that we consider is known as Boundary-Controlled Port-Hamiltonian Systems (BC-PHSs) and covers a wide class of Hyperbolic PDEs with a large type of boundary inputs and outputs. This is, for instance, the case of waves and beams with Neumann, Dirichlet, or mixed boundary conditions. Based on a Partitioned Finite Element Method (PFEM), we develop a numerical scheme for the structure-preserving spatial discretization for the class of one-dimensional BC-PHSs. We show that if the initial PDE is passive (or Impedance Energy Preserving), the discretized model also is. In addition and since the discretized model or Full Order Model (FOM) can be of large dimension, we recall the standard Loewner framework for the Model Order Reduction (MOR) using frequency domain interpolation. We recall the main steps to produce a Reduced Order Model (ROM) that approaches the FOM in a given range of frequencies. We summarize the steps to follow in order to obtain a ROM that preserves the passive structure as well. Finally, we provide a constructive way to build a projector that allows to recover the physical meaning of the state variables from the ROM to the FOM. We use the one-dimensional wave equation and the Timoshenko beam as examples to show the versatility of the proposed approach.
 
## Keywords
distributed port-hamiltonian systems, finite element method, loewner framework, structure-preserving discretization methods
 
## Citation
- **Journal:** Systems &amp; Control Letters
- **Year:** 2024
- **Volume:** 194
- **Issue:** 
- **Pages:** 105947
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.sysconle.2024.105947](https://doi.org/10.1016/j.sysconle.2024.105947)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Toledo_Zucco_2024,
  title={{Structure-preserving discretization and model order reduction of boundary-controlled 1D port-Hamiltonian systems}},
  volume={194},
  ISSN={0167-6911},
  DOI={10.1016/j.sysconle.2024.105947},
  journal={Systems \&amp; Control Letters},
  publisher={Elsevier BV},
  author={Toledo-Zucco, Jesus-Pablo and Matignon, Denis and Poussot-Vassal, Charles and Le Gorrec, Yann},
  year={2024},
  pages={105947}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/structure-preserving-discretization-and-model-order-reduction-of-boundary-controlled-1d-port-hamiltonian-systems.bib)
 
## References
- [van der Schaft AJ, Maschke BM (2002) Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42(1–2):166–194. https://doi.org/10.1016/s0393-0440(01)00083-](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- [Le Gorrec Y, Zwart H, Maschke B (2005) Dirac structures and Boundary Control Systems associated with Skew-Symmetric Differential Operators. SIAM J Control Optim 44(5):1864–1892. https://doi.org/10.1137/04061167](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- [Rashad R, Califano F, van der Schaft AJ, Stramigioli S (2020) Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37(4):1400–1422. https://doi.org/10.1093/imamci/dnaa01](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- [Seslija M, van der Schaft A, Scherpen JMA (2012) Discrete exterior geometry approach to structure-preserving discretization of distributed-parameter port-Hamiltonian systems. Journal of Geometry and Physics 62(6):1509–1531. https://doi.org/10.1016/j.geomphys.2012.02.00](discrete-exterior-geometry-approach-to-structure-preserving-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.geomphys.2012.02.006](https://doi.org/10.1016/j.geomphys.2012.02.006)
- [Golo G, Talasila V, van der Schaft A, Maschke B (2004) Hamiltonian discretization of boundary control systems. Automatica 40(5):757–771. https://doi.org/10.1016/j.automatica.2003.12.01](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- [Kotyczka P (2016) Finite Volume Structure-Preserving Discretization of 1D Distributed-Parameter Port-Hamiltonian Systems. IFAC-PapersOnLine 49(8):298–303. https://doi.org/10.1016/j.ifacol.2016.07.45](finite-volume-structure-preserving-discretization-of-1d-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.ifacol.2016.07.457](https://doi.org/10.1016/j.ifacol.2016.07.457)
- [Trenchant V, Ramirez H, Le Gorrec Y, Kotyczka P (2018) Finite differences on staggered grids preserving the port-Hamiltonian structure with application to an acoustic duct. Journal of Computational Physics 373:673–697. https://doi.org/10.1016/j.jcp.2018.06.05](finite-differences-on-staggered-grids-preserving-the-port-hamiltonian-structure-with-application-to-an-acoustic-duct) -- [10.1016/j.jcp.2018.06.051](https://doi.org/10.1016/j.jcp.2018.06.051)
- [Cardoso-Ribeiro FL, Matignon D, Lefèvre L (2018) A structure-preserving Partitioned Finite Element Method for the 2D wave equation ⁎ ⁎This work is supported by the project ANR-16-CE92-0028, entitled Interconnected Infinite-Dimensional systems for Heterogeneous Media, INFIDHEM, financed by the French National Research Agency (ANR). Further information is available at https://websites.isae-supaero.fr/infidhem/the-project/. IFAC-PapersOnLine 51(3):119–124. https://doi.org/10.1016/j.ifacol.2018.06.03](a-structure-preserving-partitioned-finite-element-method-for-the-2d-wave-equation) -- [10.1016/j.ifacol.2018.06.033](https://doi.org/10.1016/j.ifacol.2018.06.033)
- [Serhani A, Matignon D, Haine G (2019) Partitioned Finite Element Method for port-Hamiltonian systems with Boundary Damping: Anisotropic Heterogeneous 2D wave equations. IFAC-PapersOnLine 52(2):96–101. https://doi.org/10.1016/j.ifacol.2019.08.01](partitioned-finite-element-method-for-port-hamiltonian-systems-with-boundary-damping-anisotropic-heterogeneous-2d-wave-equations) -- [10.1016/j.ifacol.2019.08.017](https://doi.org/10.1016/j.ifacol.2019.08.017)
- [Cardoso-Ribeiro FL, Matignon D, Lefèvre L (2020) A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information 38(2):493–533. https://doi.org/10.1093/imamci/dnaa03](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- [Brugnoli A, Alazard D, Pommier-Budinger V, Matignon D (2019) Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Applied Mathematical Modelling 75:940–960. https://doi.org/10.1016/j.apm.2019.04.03](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Haine G, Matignon D, Monteghetti F (2022) Structure-preserving discretization of Maxwell’s equations as a port-Hamiltonian system. IFAC-PapersOnLine 55(30):424–429. https://doi.org/10.1016/j.ifacol.2022.11.09](structure-preserving-discretization-of-maxwell-s-equations-as-a-port-hamiltonian-system) -- [10.1016/j.ifacol.2022.11.090](https://doi.org/10.1016/j.ifacol.2022.11.090)
- [Brugnoli A, Cardoso-Ribeiro FL, Haine G, Kotyczka P (2020) Partitioned finite element method for structured discretization with mixed boundary conditions. IFAC-PapersOnLine 53(2):7557–7562. https://doi.org/10.1016/j.ifacol.2020.12.135](partitioned-finite-element-method-for-structured-discretization-with-mixed-boundary-conditions) -- [10.1016/j.ifacol.2020.12.1351](https://doi.org/10.1016/j.ifacol.2020.12.1351)
- [Brugnoli A, Haine G, Matignon D (2022) Explicit structure-preserving discretization of port-Hamiltonian systems with mixed boundary control. IFAC-PapersOnLine 55(30):418–423. https://doi.org/10.1016/j.ifacol.2022.11.08](explicit-structure-preserving-discretization-of-port-hamiltonian-systems-with-mixed-boundary-control) -- [10.1016/j.ifacol.2022.11.089](https://doi.org/10.1016/j.ifacol.2022.11.089)
- Mayo AJ, Antoulas AC (2007) A framework for the solution of the generalized realization problem. Linear Algebra and its Applications 425(2–3):634–662. https://doi.org/10.1016/j.laa.2007.03.00 -- [10.1016/j.laa.2007.03.008](https://doi.org/10.1016/j.laa.2007.03.008)
- Antoulas AC, Lefteriu S, Ionita AC (2017) Chapter 8: A Tutorial Introduction to the Loewner Framework for Model Reduction. Model Reduction and Approximation 335–37 -- [10.1137/1.9781611974829.ch8](https://doi.org/10.1137/1.9781611974829.ch8)
- [Benner P, Goyal P, Van Dooren P (2020) Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters 143:104741. https://doi.org/10.1016/j.sysconle.2020.10474](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- Poussot-Vassal, Data-driven port-Hamiltonian structured identification for non-strictly passive systems. (2023)
- [Cherifi K, Brugnoli A (2021) Application of data-driven realizations to port-Hamiltonian flexible structures. IFAC-PapersOnLine 54(19):180–185. https://doi.org/10.1016/j.ifacol.2021.11.07](application-of-data-driven-realizations-to-port-hamiltonian-flexible-structures) -- [10.1016/j.ifacol.2021.11.075](https://doi.org/10.1016/j.ifacol.2021.11.075)
- [Moreschini A, Simard JD, Astolfi A (2024) Data-driven model reduction for port-Hamiltonian and network systems in the Loewner framework. Automatica 169:111836. https://doi.org/10.1016/j.automatica.2024.11183](data-driven-model-reduction-for-port-hamiltonian-and-network-systems-in-the-loewner-framework) -- [10.1016/j.automatica.2024.111836](https://doi.org/10.1016/j.automatica.2024.111836)
- Villegas, (2007)
- [Macchelli A, Le Gorrec Y, Ramirez H (2020) Exponential Stabilization of Port-Hamiltonian Boundary Control Systems via Energy Shaping. IEEE Trans Automat Contr 65(10):4440–4447. https://doi.org/10.1109/tac.2020.300479](exponential-stabilization-of-port-hamiltonian-boundary-control-systems-via-energy-shaping) -- [10.1109/tac.2020.3004798](https://doi.org/10.1109/tac.2020.3004798)
- Willems JC (1972) Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Arch Rational Mech Anal 45(5):352–393. https://doi.org/10.1007/bf0027649 -- [10.1007/bf00276494](https://doi.org/10.1007/bf00276494)
- Beattie, (2022)
- Sorensen DC (2005) Passivity preserving model reduction via interpolation of spectral zeros. Systems &amp; Control Letters 54(4):347–360. https://doi.org/10.1016/j.sysconle.2004.07.00 -- [10.1016/j.sysconle.2004.07.006](https://doi.org/10.1016/j.sysconle.2004.07.006)
- [Gugercin S, Polyuga RV, Beattie C, van der Schaft A (2012) Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9):1963–1974. https://doi.org/10.1016/j.automatica.2012.05.05](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Mehrmann V, Unger B (2023) Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica 32:395–515. https://doi.org/10.1017/s096249292200008](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- Gosea, Model reduction of linear and nonlinear systems in the Loewner framework: A summary. (2015)
- Antoulas AC (2008) On the Construction of Passive Models from Frequency Response Data (Konstruktion passiver Modelle auf der Basis von Frequenzbereichsdaten). auto 56(8):447–452. https://doi.org/10.1524/auto.2008.072 -- [10.1524/auto.2008.0722](https://doi.org/10.1524/auto.2008.0722)

