---
layout: post
title: "Port-Hamiltonian reduced order modelling of the 2D Maxwell equations"
date: 2025-06-26 00:00:00 +0100
permalink: port-hamiltonian-reduced-order-modelling-of-the-2d-maxwell-equations
year: 2025
authors: Mattéo Gouzien, Charles Poussot-Vassal, Ghislain Haine, Denis Matignon
category: articles
---
 
## Authors
[Mattéo Gouzien](authors/matteo-gouzien), [Charles Poussot-Vassal](authors/charles-poussot-vassal), [Ghislain Haine](authors/ghislain-haine), [Denis Matignon](authors/denis-matignon)
 
## Abstract
 Purpose This study aims to develop a systematic and efficient method for modeling and reducing the computational complexity of the Maxwell equations in 2D. By maintaining the port-Hamiltonian structure in both the full order model (FOM) and reduced-order model (ROM), this approach ensures that the essential dynamical properties are preserved. The ultimate goal is to create a reduced order model that is suitable for rapid simulations, control and analysis in electromagnetic applications, such as waveguides, which involve boundary control and observation, as well as interface discontinuities.   Design/methodology/approach This research introduces an ROM procedure for the 2D Maxwell equations within a port-Hamiltonian framework. Using a mixed finite element method, the high-fidelity FOM is generated, which retains the original structure of the Maxwell equations. Model reduction is then achieved through the Loewner framework, allowing for a low-complexity model that is computationally efficient while preserving the port-Hamiltonian properties. A lifting operator is employed to recover the FOM’s internal variables from the reduced model, validating the accuracy of the ROM in reproducing the FOM’s dynamic behavior.   Findings The proposed methodology effectively reduces the dimension of the Maxwell system by approximately 35 times, significantly decreasing computational time while maintaining high fidelity in the key output responses. Simulation results demonstrate that the reduced model accurately replicates the full order model’s dynamics and power balance. The approach also highlights the advantages of using a port-Hamiltonian structure for energy tracking, with ROMs exhibiting only minor discrepancies due to truncation. The findings validate the ROM as a reliable and efficient approximation of the original high-dimensional system, suitable for complex electromagnetic configurations.   Originality/value This work provides a novel approach to reducing the 2D Maxwell equations within a port-Hamiltonian framework, preserving essential structure and dynamical properties. By leveraging the Loewner framework with a unique focus on passivity preservation, the method offers a practical solution for efficient simulation and control in electromagnetic systems. This ROM methodology, with its reduced computational burden and enhanced accuracy, is valuable for applications in electromagnetic field simulations and control design, where high computational efficiency and structure preservation are critical [1]. 
 
## Citation
- **Journal:** COMPEL - The international journal for computation and mathematics in electrical and electronic engineering
- **Year:** 2025
- **Volume:** 
- **Issue:** 
- **Pages:** 
- **Publisher:** Emerald
- **DOI:** [10.1108/compel-10-2024-0421](https://doi.org/10.1108/compel-10-2024-0421)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gouzien_2025,
  title={{Port-Hamiltonian reduced order modelling of the 2D Maxwell equations}},
  ISSN={2054-5606},
  DOI={10.1108/compel-10-2024-0421},
  journal={COMPEL - The international journal for computation and mathematics in electrical and electronic engineering},
  publisher={Emerald},
  author={Gouzien, Mattéo and Poussot-Vassal, Charles and Haine, Ghislain and Matignon, Denis},
  year={2025}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-reduced-order-modelling-of-the-2d-maxwell-equations.bib)
 
## References
- Interpolatory methods for model reduction. Computational Science and Engineering (2020)
- Chapter a tutorial introduction to the Loewner framework for model reduction. Model Reduction and Approximation Theory and Algorithms (2016)
- Mathematical Foundations of Computational Electromagnetism (2018)
- Bartel, A. & Günther, M. PDAEs in Refined Electrical Network Modeling. SIAM Rev. 60, 56–91 (2018) -- [10.1137/17m1113643](https://doi.org/10.1137/17m1113643)
- Port-Hamiltonian systems’ modelling in electrical engineering. Scientific Computing in Electrical Engineering (2024)
- [Benner, P., Goyal, P. & Van Dooren, P. Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters 143, 104741 (2020)](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- Benner, P., Gugercin, S. & Willcox, K. A Survey of Projection-Based Model Reduction Methods for Parametric Dynamical Systems. SIAM Rev. 57, 483–531 (2015) -- [10.1137/130932715](https://doi.org/10.1137/130932715)
- Bundschuh, J., Ruppert, M. G. & Späck-Leigsnering, Y. Pyrit: A finite element based field simulation software written in Python. COMPEL 42, 1007–1020 (2023) -- [10.1108/compel-01-2023-0013](https://doi.org/10.1108/compel-01-2023-0013)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information 38, 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- [Cardoso-Ribeiro, F. L., Haine, G., Le Gorrec, Y., Matignon, D. & Ramirez, H. Port-Hamiltonian formulations for the modeling, simulation and control of fluids. Computers &amp; Fluids 283, 106407 (2024)](port-hamiltonian-formulations-for-the-modeling-simulation-and-control-of-fluids) -- [10.1016/j.compfluid.2024.106407](https://doi.org/10.1016/j.compfluid.2024.106407)
- [Cherifi, K. & Brugnoli, A. Application of data-driven realizations to port-Hamiltonian flexible structures. IFAC-PapersOnLine 54, 180–185 (2021)](application-of-data-driven-realizations-to-port-hamiltonian-flexible-structures) -- [10.1016/j.ifacol.2021.11.075](https://doi.org/10.1016/j.ifacol.2021.11.075)
- Electric circuit element boundary conditions in the finite element method for full-wave passive electromagnetic devices. Journal of Mathematics in Industry (2022)
- Clemens, M. & Weil, T. Discrete Electromagnetism with the Finite Integration Technique. PIER 32, 65–87 (2001) -- [10.2528/pier00080103](https://doi.org/10.2528/pier00080103)
- Condon, M. Simulation of nonuniform transmission lines. COMPEL 43, 1–13 (2023) -- [10.1108/compel-01-2023-0042](https://doi.org/10.1108/compel-01-2023-0042)
- [Farle, O., Klis, D., Jochum, M., Floch, O. & Dyczij-Edlinger, R. A port-hamiltonian finite-element formulation for the maxwell equations. 2013 International Conference on Electromagnetics in Advanced Applications (ICEAA) 324–327 (2013) doi:10.1109/iceaa.2013.6632246](a-port-hamiltonian-finite-element-formulation-for-the-maxwell-equations) -- [10.1109/iceaa.2013.6632246](https://doi.org/10.1109/iceaa.2013.6632246)
- [Ferraro, G., Fournié, M. & Haine, G. Simulation and control of interactions in multi-physics, a Python package for port-Hamiltonian systems. IFAC-PapersOnLine 58, 119–124 (2024)](simulation-and-control-of-interactions-in-multi-physics-a-python-package-for-port-hamiltonian-systems) -- [10.1016/j.ifacol.2024.08.267](https://doi.org/10.1016/j.ifacol.2024.08.267)
- [Gernandt, H., Haller, F. E., Reis, T. & Schaft, A. J. van der. Port-Hamiltonian formulation of nonlinear electrical circuits. Journal of Geometry and Physics 159, 103959 (2021)](port-hamiltonian-formulation-of-nonlinear-electrical-circuits) -- [10.1016/j.geomphys.2020.103959](https://doi.org/10.1016/j.geomphys.2020.103959)
- Data-driven modeling and control of large-scale dynamical systems in the Loewner framework. Handbook of Numerical Analysis (2022)
- [Haine, G. & Matignon, D. Incompressible Navier-Stokes Equation as port-Hamiltonian systems: velocity formulation versus vorticity formulation. IFAC-PapersOnLine 54, 161–166 (2021)](incompressible-navier-stokes-equation-as-port-hamiltonian-systems-velocity-formulation-versus-vorticity-formulation) -- [10.1016/j.ifacol.2021.11.072](https://doi.org/10.1016/j.ifacol.2021.11.072)
- [Haine, G., Matignon, D. & Monteghetti, F. Structure-preserving discretization of Maxwell’s equations as a port-Hamiltonian system. IFAC-PapersOnLine 55, 424–429 (2022)](structure-preserving-discretization-of-maxwell-s-equations-as-a-port-hamiltonian-system) -- [10.1016/j.ifacol.2022.11.090](https://doi.org/10.1016/j.ifacol.2022.11.090)
- [Ghislain Haine, G. H., Denis Matignon, D. M. & Anass Serhani, A. S. Numerical Analysis of a Structure-Preserving Space-Discretization for an Anisotropic and Heterogeneous Boundary Controlled $N$-Dimensional Wave Equation as a Port-Hamiltonian System. IJNAM 20, 92–133 (2023)](numerical-analysis-of-a-structure-preserving-space-discretization-for-an-anisotropic-and-heterogeneous-boundary-controlled-n-dimensional-wave-equation-as-a-port-hamiltonian-system) -- [10.4208/ijnam2023-1005](https://doi.org/10.4208/ijnam2023-1005)
- [Marquez, F. M., Zufiria, P. J. & Yebra, L. J. Port-Hamiltonian Modeling of Multiphysics Systems and Object-Oriented Implementation With the Modelica Language. IEEE Access 8, 105980–105996 (2020)](port-hamiltonian-modeling-of-multiphysics-systems-and-object-oriented-implementation-with-the-modelica-language) -- [10.1109/access.2020.3000129](https://doi.org/10.1109/access.2020.3000129)
- A framework for the solution of the generalized realization problem. Linear Algebra and Its Applications (2007)
- [Mehrmann, V. & Van Dooren, P. M. Optimal Robustness of Port-Hamiltonian Systems. SIAM J. Matrix Anal. Appl. 41, 134–151 (2020)](optimal-robustness-of-port-hamiltonian-systems) -- [10.1137/19m1259092](https://doi.org/10.1137/19m1259092)
- Finite Element Methods for Maxwell’s Equations (2003)
- [Payen, G., Matignon, D. & Haine, G. Modelling and structure-preserving discretization of Maxwell’s equations as port-Hamiltonian system. IFAC-PapersOnLine 53, 7581–7586 (2020)](modelling-and-structure-preserving-discretization-of-maxwell-s-equations-as-port-hamiltonian-system) -- [10.1016/j.ifacol.2020.12.1355](https://doi.org/10.1016/j.ifacol.2020.12.1355)
- Data-driven port-Hamiltonian structured identification for non-strictly passive systems. Proc. European Control Conference (ECC) (2023)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37, 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- [Toledo-Zucco, J.-P., Matignon, D. & Poussot-Vassal, C. Scattering-Passive Structure-Preserving Finite Element Method for the Boundary Controlled Transport Equation with a Moving Mesh. IFAC-PapersOnLine 58, 292–297 (2024)](scattering-passive-structure-preserving-finite-element-method-for-the-boundary-controlled-transport-equation-with-a-moving-mesh) -- [10.1016/j.ifacol.2024.08.296](https://doi.org/10.1016/j.ifacol.2024.08.296)
- [Toledo-Zucco, J.-P., Matignon, D., Poussot-Vassal, C. & Le Gorrec, Y. Structure-preserving discretization and model order reduction of boundary-controlled 1D port-Hamiltonian systems. Systems &amp; Control Letters 194, 105947 (2024)](structure-preserving-discretization-and-model-order-reduction-of-boundary-controlled-1d-port-hamiltonian-systems) -- [10.1016/j.sysconle.2024.105947](https://doi.org/10.1016/j.sysconle.2024.105947)
- Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics (2002)
- Weiss, G. & Staffans, O. J. Maxwell’s Equations as a Scattering Passive Linear System. SIAM J. Control Optim. 51, 3722–3756 (2013) -- [10.1137/120869444](https://doi.org/10.1137/120869444)

