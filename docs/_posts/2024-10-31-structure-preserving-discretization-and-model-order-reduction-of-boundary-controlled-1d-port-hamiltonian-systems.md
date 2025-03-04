---
layout: post
title: "Structure-preserving discretization and model order reduction of boundary-controlled 1D port-Hamiltonian systems"
date: 2024-10-31 00:00:00 +0100
permalink: structure-preserving-discretization-and-model-order-reduction-of-boundary-controlled-1d-port-hamiltonian-systems
year: 2024
authors: Jesus-Pablo Toledo-Zucco, Denis Matignon, Charles Poussot-Vassal, Yann Le Gorrec
category: journal-article
tag: Distributed port-Hamiltonian systems; Finite element method; Loewner framework; Structure-preserving discretization methods
---
 
## Authors
[Jesus-Pablo Toledo-Zucco](authors/jesus-pablo-toledo-zucco), [Denis Matignon](authors/denis-matignon), [Charles Poussot-Vassal](authors/charles-poussot-vassal), [Yann Le Gorrec](authors/yann-le-gorrec)
 
## Abstract
This paper presents a systematic methodology for the discretization and reduction of a class of one-dimensional Partial Differential Equations (PDEs) with inputs and outputs collocated at the spatial boundaries. The class of system that we consider is known as Boundary-Controlled Port-Hamiltonian Systems (BC-PHSs) and covers a wide class of Hyperbolic PDEs with a large type of boundary inputs and outputs. This is, for instance, the case of waves and beams with Neumann, Dirichlet, or mixed boundary conditions. Based on a Partitioned Finite Element Method (PFEM), we develop a numerical scheme for the structure-preserving spatial discretization for the class of one-dimensional BC-PHSs. We show that if the initial PDE is passive (or Impedance Energy Preserving), the discretized model also is. In addition and since the discretized model or Full Order Model (FOM) can be of large dimension, we recall the standard Loewner framework for the Model Order Reduction (MOR) using frequency domain interpolation. We recall the main steps to produce a Reduced Order Model (ROM) that approaches the FOM in a given range of frequencies. We summarize the steps to follow in order to obtain a ROM that preserves the passive structure as well. Finally, we provide a constructive way to build a projector that allows to recover the physical meaning of the state variables from the ROM to the FOM. We use the one-dimensional wave equation and the Timoshenko beam as examples to show the versatility of the proposed approach.
 
## Keywords
Distributed port-Hamiltonian systems; Finite element method; Loewner framework; Structure-preserving discretization methods
 
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
  journal={Systems &amp; Control Letters},
  publisher={Elsevier BV},
  author={Toledo-Zucco, Jesus-Pablo and Matignon, Denis and Poussot-Vassal, Charles and Le Gorrec, Yann},
  year={2024},
  pages={105947}
}
{% endraw %}
{% endhighlight %}
 
## References
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3)
- [Le Gorrec, Y., Zwart, H. & Maschke, B. Dirac structures and Boundary Control Systems associated with Skew-Symmetric Differential Operators. SIAM Journal on Control and Optimization vol. 44 1864–1892 (2005)](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- [Seslija, M., van der Schaft, A. & Scherpen, J. M. A. Discrete exterior geometry approach to structure-preserving discretization of distributed-parameter port-Hamiltonian systems. Journal of Geometry and Physics vol. 62 1509–1531 (2012)](discrete-exterior-geometry-approach-to-structure-preserving-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.geomphys.2012.02.006](https://doi.org/10.1016/j.geomphys.2012.02.006)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- [Kotyczka, P. Finite Volume Structure-Preserving Discretization of 1D Distributed-Parameter Port-Hamiltonian Systems. IFAC-PapersOnLine vol. 49 298–303 (2016)](finite-volume-structure-preserving-discretization-of-1d-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.ifacol.2016.07.457](https://doi.org/10.1016/j.ifacol.2016.07.457)
- [Trenchant, V., Ramirez, H., Le Gorrec, Y. & Kotyczka, P. Finite differences on staggered grids preserving the port-Hamiltonian structure with application to an acoustic duct. Journal of Computational Physics vol. 373 673–697 (2018)](finite-differences-on-staggered-grids-preserving-the-port-hamiltonian-structure-with-application-to-an-acoustic-duct) -- [10.1016/j.jcp.2018.06.051](https://doi.org/10.1016/j.jcp.2018.06.051)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A structure-preserving Partitioned Finite Element Method for the 2D wave equation ⁎ ⁎This work is supported by the project ANR-16-CE92-0028, entitled Interconnected Infinite-Dimensional systems for Heterogeneous Media, INFIDHEM, financed by the French National Research Agency (ANR). Further information is available at https://websites.isae-supaero.fr/infidhem/the-project/. IFAC-PapersOnLine vol. 51 119–124 (2018)](a-structure-preserving-partitioned-finite-element-method-for-the-2d-wave-equation) -- [10.1016/j.ifacol.2018.06.033](https://doi.org/10.1016/j.ifacol.2018.06.033)
- [Serhani, A., Matignon, D. & Haine, G. Partitioned Finite Element Method for port-Hamiltonian systems with Boundary Damping: Anisotropic Heterogeneous 2D wave equations. IFAC-PapersOnLine vol. 52 96–101 (2019)](partitioned-finite-element-method-for-port-hamiltonian-systems-with-boundary-damping-anisotropic-heterogeneous-2d-wave-equations) -- [10.1016/j.ifacol.2019.08.017](https://doi.org/10.1016/j.ifacol.2019.08.017)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information vol. 38 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Applied Mathematical Modelling vol. 75 940–960 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Haine, G., Matignon, D. & Monteghetti, F. Structure-preserving discretization of Maxwell’s equations as a port-Hamiltonian system. IFAC-PapersOnLine vol. 55 424–429 (2022)](structure-preserving-discretization-of-maxwell-s-equations-as-a-port-hamiltonian-system) -- [10.1016/j.ifacol.2022.11.090](https://doi.org/10.1016/j.ifacol.2022.11.090)
- [Brugnoli, A., Cardoso-Ribeiro, F. L., Haine, G. & Kotyczka, P. Partitioned finite element method for structured discretization with mixed boundary conditions. IFAC-PapersOnLine vol. 53 7557–7562 (2020)](partitioned-finite-element-method-for-structured-discretization-with-mixed-boundary-conditions) -- [10.1016/j.ifacol.2020.12.1351](https://doi.org/10.1016/j.ifacol.2020.12.1351)
- [Brugnoli, A., Haine, G. & Matignon, D. Explicit structure-preserving discretization of port-Hamiltonian systems with mixed boundary control. IFAC-PapersOnLine vol. 55 418–423 (2022)](explicit-structure-preserving-discretization-of-port-hamiltonian-systems-with-mixed-boundary-control) -- [10.1016/j.ifacol.2022.11.089](https://doi.org/10.1016/j.ifacol.2022.11.089)
- Mayo, A. J. & Antoulas, A. C. A framework for the solution of the generalized realization problem. Linear Algebra and its Applications vol. 425 634–662 (2007) -- [10.1016/j.laa.2007.03.008](https://doi.org/10.1016/j.laa.2007.03.008)
- Antoulas, A. C., Lefteriu, S. & Ionita, A. C. Chapter 8: A Tutorial Introduction to the Loewner Framework for Model Reduction. Model Reduction and Approximation 335–376 (2017) doi:10.1137/1.9781611974829.ch8 -- [10.1137/1.9781611974829.ch8](https://doi.org/10.1137/1.9781611974829.ch8)
- [Benner, P., Goyal, P. & Van Dooren, P. Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters vol. 143 104741 (2020)](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- [Cherifi, K. & Brugnoli, A. Application of data-driven realizations to port-Hamiltonian flexible structures. IFAC-PapersOnLine vol. 54 180–185 (2021)](application-of-data-driven-realizations-to-port-hamiltonian-flexible-structures) -- [10.1016/j.ifacol.2021.11.075](https://doi.org/10.1016/j.ifacol.2021.11.075)
- [Moreschini, A., Simard, J. D. & Astolfi, A. Data-driven model reduction for port-Hamiltonian and network systems in the Loewner framework. Automatica vol. 169 111836 (2024)](data-driven-model-reduction-for-port-hamiltonian-and-network-systems-in-the-loewner-framework) -- [10.1016/j.automatica.2024.111836](https://doi.org/10.1016/j.automatica.2024.111836)
- [Macchelli, A., Le Gorrec, Y. & Ramirez, H. Exponential Stabilization of Port-Hamiltonian Boundary Control Systems via Energy Shaping. IEEE Transactions on Automatic Control vol. 65 4440–4447 (2020)](exponential-stabilization-of-port-hamiltonian-boundary-control-systems-via-energy-shaping) -- [10.1109/TAC.2020.3004798](https://doi.org/10.1109/TAC.2020.3004798)
- Willems, J. C. Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Archive for Rational Mechanics and Analysis vol. 45 352–393 (1972) -- [10.1007/BF00276494](https://doi.org/10.1007/BF00276494)
- Sorensen, D. C. Passivity preserving model reduction via interpolation of spectral zeros. Systems &amp; Control Letters vol. 54 347–360 (2005) -- [10.1016/j.sysconle.2004.07.006](https://doi.org/10.1016/j.sysconle.2004.07.006)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/S0962492922000083](https://doi.org/10.1017/S0962492922000083)
- Antoulas, A. C. On the Construction of Passive Models from Frequency Response Data (Konstruktion passiver Modelle auf der Basis von Frequenzbereichsdaten). auto vol. 56 447–452 (2008) -- [10.1524/auto.2008.0722](https://doi.org/10.1524/auto.2008.0722)

