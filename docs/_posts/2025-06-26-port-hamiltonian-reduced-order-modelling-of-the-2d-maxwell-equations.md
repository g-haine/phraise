---
title: "Port-Hamiltonian reduced order modelling of the 2D Maxwell equations"
date: 2025-06-26 00:00:00 +0100
permalink: port-hamiltonian-reduced-order-modelling-of-the-2d-maxwell-equations
year: 2026
authors: Mattéo Gouzien, Charles Poussot-Vassal, Ghislain Haine, Denis Matignon
category: articles
---
 
## Authors
[Mattéo Gouzien](authors/matteo-gouzien), [Charles Poussot-Vassal](authors/charles-poussot-vassal), [Ghislain Haine](authors/ghislain-haine), [Denis Matignon](authors/denis-matignon)
 
## Abstract
                    Purpose                    This study aims to develop a systematic and efficient method for modeling and reducing the computational complexity of the Maxwell equations in 2D. By maintaining the port-Hamiltonian structure in both the full order model (FOM) and reduced-order model (ROM), this approach ensures that the essential dynamical properties are preserved. The ultimate goal is to create a reduced order model that is suitable for rapid simulations, control and analysis in electromagnetic applications, such as waveguides, which involve boundary control and observation, as well as interface discontinuities.                                                        Design/methodology/approach                    This research introduces an ROM procedure for the 2D Maxwell equations within a port-Hamiltonian framework. Using a mixed finite element method, the high-fidelity FOM is generated, which retains the original structure of the Maxwell equations. Model reduction is then achieved through the Loewner framework, allowing for a low-complexity model that is computationally efficient while preserving the port-Hamiltonian properties. A lifting operator is employed to recover the FOM’s internal variables from the reduced model, validating the accuracy of the ROM in reproducing the FOM’s dynamic behavior.                                                        Findings                    The proposed methodology effectively reduces the dimension of the Maxwell system by approximately 35 times, significantly decreasing computational time while maintaining high fidelity in the key output responses. Simulation results demonstrate that the reduced model accurately replicates the full order model’s dynamics and power balance. The approach also highlights the advantages of using a port-Hamiltonian structure for energy tracking, with ROMs exhibiting only minor discrepancies due to truncation. The findings validate the ROM as a reliable and efficient approximation of the original high-dimensional system, suitable for complex electromagnetic configurations.                                                        Originality/value                    This work provides a novel approach to reducing the 2D Maxwell equations within a port-Hamiltonian framework, preserving essential structure and dynamical properties. By leveraging the Loewner framework with a unique focus on passivity preservation, the method offers a practical solution for efficient simulation and control in electromagnetic systems. This ROM methodology, with its reduced computational burden and enhanced accuracy, is valuable for applications in electromagnetic field simulations and control design, where high computational efficiency and structure preservation are critical [1].                  
 
## Citation
- **Journal:** COMPEL - The international journal for computation and mathematics in electrical and electronic engineering
- **Year:** 2026
- **Volume:** 45
- **Issue:** 3
- **Pages:** 389--411
- **Publisher:** Emerald
- **DOI:** [10.1108/compel-10-2024-0421](https://doi.org/10.1108/compel-10-2024-0421)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gouzien_2025,
  title={{Port-Hamiltonian reduced order modelling of the 2D Maxwell equations}},
  volume={45},
  ISSN={2054-5606},
  DOI={10.1108/compel-10-2024-0421},
  number={3},
  journal={COMPEL - The international journal for computation and mathematics in electrical and electronic engineering},
  publisher={Emerald},
  author={Gouzien, Mattéo and Poussot-Vassal, Charles and Haine, Ghislain and Matignon, Denis},
  year={2025},
  pages={389--411}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-reduced-order-modelling-of-the-2d-maxwell-equations.bib)
 
## References
- Antoulas, Computational Science and Engineering (2020)
- Antoulas, Model Reduction and Approximation Theory and Algorithms (2016)
- Assous F, Ciarlet P, Labrunie S (2018) Mathematical Foundations of Computational Electromagnetism. Springer International Publishin -- [10.1007/978-3-319-70842-3](https://doi.org/10.1007/978-3-319-70842-3)
- Bartel A, Günther M (2018) PDAEs in Refined Electrical Network Modeling. SIAM Rev 60(1):56–91. https://doi.org/10.1137/17m111364 -- [10.1137/17m1113643](https://doi.org/10.1137/17m1113643)
- [Bartel A, Clemens M, Günther M, Jacob B, Reis T (2024) Port-Hamiltonian Systems’ Modelling in Electrical Engineering. Mathematics in Industry 133–14](port-hamiltonian-systems-modelling-in-electrical-engineering) -- [10.1007/978-3-031-54517-7_15](https://doi.org/10.1007/978-3-031-54517-7_15)
- [Benner P, Goyal P, Van Dooren P (2020) Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters 143:104741. https://doi.org/10.1016/j.sysconle.2020.10474](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- Benner P, Gugercin S, Willcox K (2015) A Survey of Projection-Based Model Reduction Methods for Parametric Dynamical Systems. SIAM Rev 57(4):483–531. https://doi.org/10.1137/13093271 -- [10.1137/130932715](https://doi.org/10.1137/130932715)
- Bundschuh J, Ruppert MG, Späck-Leigsnering Y (2023) Pyrit: A finite element based field simulation software written in Python. COMPEL 42(5):1007–1020. https://doi.org/10.1108/compel-01-2023-001 -- [10.1108/compel-01-2023-0013](https://doi.org/10.1108/compel-01-2023-0013)
- [Cardoso-Ribeiro FL, Matignon D, Lefèvre L (2020) A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information 38(2):493–533. https://doi.org/10.1093/imamci/dnaa03](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- [Cardoso-Ribeiro FL, Haine G, Le Gorrec Y, Matignon D, Ramirez H (2024) Port-Hamiltonian formulations for the modeling, simulation and control of fluids. Computers &amp; Fluids 283:106407. https://doi.org/10.1016/j.compfluid.2024.10640](port-hamiltonian-formulations-for-the-modeling-simulation-and-control-of-fluids) -- [10.1016/j.compfluid.2024.106407](https://doi.org/10.1016/j.compfluid.2024.106407)
- [Cherifi K, Brugnoli A (2021) Application of data-driven realizations to port-Hamiltonian flexible structures. IFAC-PapersOnLine 54(19):180–185. https://doi.org/10.1016/j.ifacol.2021.11.07](application-of-data-driven-realizations-to-port-hamiltonian-flexible-structures) -- [10.1016/j.ifacol.2021.11.075](https://doi.org/10.1016/j.ifacol.2021.11.075)
- Ciuprina G, Ioan D, Sabariego RV (2022) Electric circuit element boundary conditions in the finite element method for full-wave passive electromagnetic devices. JMathIndustry 12(1). https://doi.org/10.1186/s13362-022-00122- -- [10.1186/s13362-022-00122-1](https://doi.org/10.1186/s13362-022-00122-1)
- Clemens M, Weil T (2001) Discrete Electromagnetism with the Finite Integration Technique. PIER 32:65–87. https://doi.org/10.2528/pier0008010 -- [10.2528/pier00080103](https://doi.org/10.2528/pier00080103)
- Condon M (2023) Simulation of nonuniform transmission lines. COMPEL 43(1):1–13. https://doi.org/10.1108/compel-01-2023-004 -- [10.1108/compel-01-2023-0042](https://doi.org/10.1108/compel-01-2023-0042)
- [Farle O, Klis D, Jochum M, Floch O, Dyczij-Edlinger R (2013) A port-hamiltonian finite-element formulation for the maxwell equations. 2013 International Conference on Electromagnetics in Advanced Applications (ICEAA) 324–32](a-port-hamiltonian-finite-element-formulation-for-the-maxwell-equations) -- [10.1109/iceaa.2013.6632246](https://doi.org/10.1109/iceaa.2013.6632246)
- [Ferraro G, Fournié M, Haine G (2024) Simulation and control of interactions in multi-physics, a Python package for port-Hamiltonian systems. IFAC-PapersOnLine 58(6):119–124. https://doi.org/10.1016/j.ifacol.2024.08.26](simulation-and-control-of-interactions-in-multi-physics-a-python-package-for-port-hamiltonian-systems) -- [10.1016/j.ifacol.2024.08.267](https://doi.org/10.1016/j.ifacol.2024.08.267)
- [Gernandt H, Haller FE, Reis T, Schaft AJ van der (2021) Port-Hamiltonian formulation of nonlinear electrical circuits. Journal of Geometry and Physics 159:103959. https://doi.org/10.1016/j.geomphys.2020.10395](port-hamiltonian-formulation-of-nonlinear-electrical-circuits) -- [10.1016/j.geomphys.2020.103959](https://doi.org/10.1016/j.geomphys.2020.103959)
- Gosea, Data-driven modeling and control of large-scale dynamical systems in the Loewner framework. Handbook of Numerical Analysis (2022)
- [Haine G, Matignon D (2021) Incompressible Navier-Stokes Equation as port-Hamiltonian systems: velocity formulation versus vorticity formulation. IFAC-PapersOnLine 54(19):161–166. https://doi.org/10.1016/j.ifacol.2021.11.07](incompressible-navier-stokes-equation-as-port-hamiltonian-systems-velocity-formulation-versus-vorticity-formulation) -- [10.1016/j.ifacol.2021.11.072](https://doi.org/10.1016/j.ifacol.2021.11.072)
- [Haine G, Matignon D, Monteghetti F (2022) Structure-preserving discretization of Maxwell’s equations as a port-Hamiltonian system. IFAC-PapersOnLine 55(30):424–429. https://doi.org/10.1016/j.ifacol.2022.11.09](structure-preserving-discretization-of-maxwell-s-equations-as-a-port-hamiltonian-system) -- [10.1016/j.ifacol.2022.11.090](https://doi.org/10.1016/j.ifacol.2022.11.090)
- [Haine G, Matignon D, Serhani A (2023) Numerical Analysis of a Structure-Preserving Space-Discretization for an Anisotropic and Heterogeneous Boundary Controlled $N$-Dimensional Wave Equation as a Port-Hamiltonian System. IJNAM 20(1):92–133. https://doi.org/10.4208/ijnam2023-100](numerical-analysis-of-a-structure-preserving-space-discretization-for-an-anisotropic-and-heterogeneous-boundary-controlled-n-dimensional-wave-equation-as-a-port-hamiltonian-system) -- [10.4208/ijnam2023-1005](https://doi.org/10.4208/ijnam2023-1005)
- [Marquez FM, Zufiria PJ, Yebra LJ (2020) Port-Hamiltonian Modeling of Multiphysics Systems and Object-Oriented Implementation With the Modelica Language. IEEE Access 8:105980–105996. https://doi.org/10.1109/access.2020.300012](port-hamiltonian-modeling-of-multiphysics-systems-and-object-oriented-implementation-with-the-modelica-language) -- [10.1109/access.2020.3000129](https://doi.org/10.1109/access.2020.3000129)
- Mayo AJ, Antoulas AC (2007) A framework for the solution of the generalized realization problem. Linear Algebra and its Applications 425(2–3):634–662. https://doi.org/10.1016/j.laa.2007.03.00 -- [10.1016/j.laa.2007.03.008](https://doi.org/10.1016/j.laa.2007.03.008)
- [Mehrmann V, Van Dooren PM (2020) Optimal Robustness of Port-Hamiltonian Systems. SIAM J Matrix Anal Appl 41(1):134–151. https://doi.org/10.1137/19m125909](optimal-robustness-of-port-hamiltonian-systems) -- [10.1137/19m1259092](https://doi.org/10.1137/19m1259092)
- Monk P (2003) Finite Element Methods for Maxwell’s Equation -- [10.1093/acprof:oso/9780198508885.001.0001](https://doi.org/10.1093/acprof:oso/9780198508885.001.0001)
- [Payen G, Matignon D, Haine G (2020) Modelling and structure-preserving discretization of Maxwell’s equations as port-Hamiltonian system. IFAC-PapersOnLine 53(2):7581–7586. https://doi.org/10.1016/j.ifacol.2020.12.135](modelling-and-structure-preserving-discretization-of-maxwell-s-equations-as-port-hamiltonian-system) -- [10.1016/j.ifacol.2020.12.1355](https://doi.org/10.1016/j.ifacol.2020.12.1355)
- Poussot-Vassal, Data-driven port-Hamiltonian structured identification for non-strictly passive systems. Proc. European Control Conference (ECC) (2023)
- [Rashad R, Califano F, van der Schaft AJ, Stramigioli S (2020) Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37(4):1400–1422. https://doi.org/10.1093/imamci/dnaa01](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- [Toledo-Zucco J-P, Matignon D, Poussot-Vassal C (2024) Scattering-Passive Structure-Preserving Finite Element Method for the Boundary Controlled Transport Equation with a Moving Mesh. IFAC-PapersOnLine 58(6):292–297. https://doi.org/10.1016/j.ifacol.2024.08.29](scattering-passive-structure-preserving-finite-element-method-for-the-boundary-controlled-transport-equation-with-a-moving-mesh) -- [10.1016/j.ifacol.2024.08.296](https://doi.org/10.1016/j.ifacol.2024.08.296)
- [Toledo-Zucco J-P, Matignon D, Poussot-Vassal C, Le Gorrec Y (2024) Structure-preserving discretization and model order reduction of boundary-controlled 1D port-Hamiltonian systems. Systems &amp; Control Letters 194:105947. https://doi.org/10.1016/j.sysconle.2024.10594](structure-preserving-discretization-and-model-order-reduction-of-boundary-controlled-1d-port-hamiltonian-systems) -- [10.1016/j.sysconle.2024.105947](https://doi.org/10.1016/j.sysconle.2024.105947)
- [van der Schaft AJ, Maschke BM (2002) Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42(1–2):166–194. https://doi.org/10.1016/s0393-0440(01)00083-](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- Weiss G, Staffans OJ (2013) Maxwell’s Equations as a Scattering Passive Linear System. SIAM J Control Optim 51(5):3722–3756. https://doi.org/10.1137/12086944 -- [10.1137/120869444](https://doi.org/10.1137/120869444)

