---
title: "A linearly-implicit energy-momentum preserving scheme for geometrically nonlinear mechanics based on non-canonical Hamiltonian formulations"
date: 2025-07-16 00:00:00 +0100
permalink: a-linearly-implicit-energy-momentum-preserving-scheme-for-geometrically-nonlinear-mechanics-based-on-non-canonical-hamiltonian-formulations
year: 2025
authors: Andrea Brugnoli, Denis Matignon, Joseph Morlier
category: articles
---
 
## Authors
[Andrea Brugnoli](authors/andrea-brugnoli), [Denis Matignon](authors/denis-matignon), [Joseph Morlier](authors/joseph-morlier)
 
## Abstract
This work presents a novel formulation and numerical strategy for the simulation of geometrically nonlinear structures. First, a non-canonical Hamiltonian (Poisson) formulation is introduced by including the dynamics of the stress tensor. This framework is developed for von-Kármán nonlinearities in beams and plates, as well as geometrically nonlinear elasticity with Saint-Venant material behavior. In the case of plates, both negligible and non-negligible membrane inertia are considered. For the former case the two-dimensional elasticity complex is leveraged to express the dynamics in terms of the Airy stress function. The finite element discretization employs a mixed approach, combining a conforming approximation for displacement and velocity fields with a discontinuous stress tensor representation. A staggered, linear implicit time integration scheme is proposed, establishing connections with existing explicit-implicit energy-preserving methods. The stress degrees of freedom are statically condensed, reducing the computational complexity to solving a system with a positive definite matrix. The integration strategy preserves energy and angular momentum exactly. The methodology is validated through numerical experiments on the Duffing oscillator, a von-Kármán beam, and a column undergoing finite deformations. Comparisons with fully implicit energy-preserving method and the leapfrog scheme demonstrate that the proposed approach achieves superior accuracy while maintaining energy stability. Additionally, it enables larger time steps compared to explicit schemes and exhibits computational efficiency comparable to the leapfrog method.
 
## Citation
- **Journal:** Nonlinear Dynamics
- **Year:** 2025
- **Volume:** 
- **Issue:** 
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s11071-025-11601-6](https://doi.org/10.1007/s11071-025-11601-6)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Brugnoli_2025,
  title={{A linearly-implicit energy-momentum preserving scheme for geometrically nonlinear mechanics based on non-canonical Hamiltonian formulations}},
  ISSN={1573-269X},
  DOI={10.1007/s11071-025-11601-6},
  journal={Nonlinear Dynamics},
  publisher={Springer Science and Business Media LLC},
  author={Brugnoli, Andrea and Matignon, Denis and Morlier, Joseph},
  year={2025}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-linearly-implicit-energy-momentum-preserving-scheme-for-geometrically-nonlinear-mechanics-based-on-non-canonical-hamiltonian-formulations.bib)
 
## References
- Lacarbonara, W. Nonlinear Structural Mechanics. (Springer US, 2013). doi:10.1007/978-1-4419-1276-3 -- [10.1007/978-1-4419-1276-3](https://doi.org/10.1007/978-1-4419-1276-3)
- Touzé, C., Vizzaccaro, A. & Thomas, O. Model order reduction methods for geometrically nonlinear structures: a review of nonlinear techniques. Nonlinear Dyn 105, 1141–1190 (2021) -- [10.1007/s11071-021-06693-9](https://doi.org/10.1007/s11071-021-06693-9)
- Patil, M. J. & Hodges, D. H. On the importance of aerodynamic and structural geometrical nonlinearities in aeroelastic behavior of high-aspect-ratio wings. Journal of Fluids and Structures 19, 905–915 (2004) -- [10.1016/j.jfluidstructs.2004.04.012](https://doi.org/10.1016/j.jfluidstructs.2004.04.012)
- Kerschen, G., Peeters, M., Golinval, J. C. & Stéphan, C. Nonlinear Modal Analysis of a Full-Scale Aircraft. Journal of Aircraft 50, 1409–1419 (2013) -- [10.2514/1.c031918](https://doi.org/10.2514/1.c031918)
- Manolas, D. I., Riziotis, V. A. & Voutsinas, S. G. Assessing the Importance of Geometric Nonlinear Effects in the Prediction of Wind Turbine Blade Loads. Journal of Computational and Nonlinear Dynamics 10, (2015) -- [10.1115/1.4027684](https://doi.org/10.1115/1.4027684)
- Chaigne, A., Touzé, C. & Thomas, O. Nonlinear vibrations and chaos in gongs and cymbals. Acoust. Sci. &amp; Tech. 26, 403–409 (2005) -- [10.1250/ast.26.403](https://doi.org/10.1250/ast.26.403)
- Jossic, M. et al. Effects of internal resonances in the pitch glide of Chinese gongs. The Journal of the Acoustical Society of America 144, 431–442 (2018) -- [10.1121/1.5038114](https://doi.org/10.1121/1.5038114)
- Lazarus, A., Thomas, O. & Deü, J.-F. Finite element reduced order models for nonlinear vibrations of piezoelectric layered beams with applications to NEMS. Finite Elements in Analysis and Design 49, 35–51 (2012) -- [10.1016/j.finel.2011.08.019](https://doi.org/10.1016/j.finel.2011.08.019)
- Gobat, G. et al. Reduced order modelling and experimental validation of a MEMS gyroscope test-structure exhibiting 1:2 internal resonance. Sci Rep 11, (2021) -- [10.1038/s41598-021-95793-y](https://doi.org/10.1038/s41598-021-95793-y)
- Bertails, F. et al. Super-helices for predicting the dynamics of natural hair. ACM Trans. Graph. 25, 1180–1187 (2006) -- [10.1145/1141911.1142012](https://doi.org/10.1145/1141911.1142012)
- Bilbao, S. Numerical Sound Synthesis. (2009) doi:10.1002/9780470749012 -- [10.1002/9780470749012](https://doi.org/10.1002/9780470749012)
- Vizzaccaro, A., Shen, Y., Salles, L., Blahoš, J. & Touzé, C. Direct computation of nonlinear mapping via normal form for reduced-order models of finite element nonlinear structures. Computer Methods in Applied Mechanics and Engineering 384, 113957 (2021) -- [10.1016/j.cma.2021.113957](https://doi.org/10.1016/j.cma.2021.113957)
- Jain, S. & Haller, G. How to compute invariant manifolds and their reduced dynamics in high-dimensional finite element models. Nonlinear Dyn 107, 1417–1450 (2021) -- [10.1007/s11071-021-06957-4](https://doi.org/10.1007/s11071-021-06957-4)
- Artola, M., Wynn, A. & Palacios, R. Modal-Based Nonlinear Model Predictive Control for 3-D Very Flexible Structures. IEEE Trans. Automat. Contr. 67, 2145–2160 (2022) -- [10.1109/tac.2021.3071326](https://doi.org/10.1109/tac.2021.3071326)
- Ducceschi, M. & Bilbao, S. Simulation of the geometrically exact nonlinear string via energy quadratisation. Journal of Sound and Vibration 534, 117021 (2022) -- [10.1016/j.jsv.2022.117021](https://doi.org/10.1016/j.jsv.2022.117021)
- Lipnikov, K., Manzini, G. & Shashkov, M. Mimetic finite difference method. Journal of Computational Physics 257, 1163–1227 (2014) -- [10.1016/j.jcp.2013.07.031](https://doi.org/10.1016/j.jcp.2013.07.031)
- de Borst, R., Crisfield, M. A., Remmers, J. J. C. & Verhoosel, C. V. Non‐Linear Finite Element Analysis of Solids and Structures. (2012) doi:10.1002/9781118375938 -- [10.1002/9781118375938](https://doi.org/10.1002/9781118375938)
- Newmark, N. M. A Method of Computation for Structural Dynamics. J. Engrg. Mech. Div. 85, 67–94 (1959) -- [10.1061/jmcea3.0000098](https://doi.org/10.1061/jmcea3.0000098)
-  -- [10.1002/1097-0207(20001210)49:10<1295::aid-nme993>3.0.co;2-w](https://doi.org/10.1002/1097-0207(20001210)49:10<1295::aid-nme993>3.0.co;2-w)
- Simo, J. C. & Tarnow, N. The discrete energy-momentum method. Conserving algorithms for nonlinear elastodynamics. Z. angew. Math. Phys. 43, 757–792 (1992) -- [10.1007/bf00913408](https://doi.org/10.1007/bf00913408)
- McLachlan, R. I., Quispel, G. R. W. & Robidoux, N. Geometric integration using discrete gradients. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences 357, 1021–1045 (1999) -- [10.1098/rsta.1999.0363](https://doi.org/10.1098/rsta.1999.0363)
- Franke, M. et al. A novel mixed and energy‐momentum consistent framework for coupled nonlinear thermo‐electro‐elastodynamics. Numerical Meth Engineering 124, 2135–2170 (2023) -- [10.1002/nme.7209](https://doi.org/10.1002/nme.7209)
- Yang, X. Linear, first and second-order, unconditionally energy stable numerical schemes for the phase field model of homopolymer blends. Journal of Computational Physics 327, 294–316 (2016) -- [10.1016/j.jcp.2016.09.029](https://doi.org/10.1016/j.jcp.2016.09.029)
- Shen, J., Xu, J. & Yang, J. The scalar auxiliary variable (SAV) approach for gradient flows. Journal of Computational Physics 353, 407–416 (2018) -- [10.1016/j.jcp.2017.10.021](https://doi.org/10.1016/j.jcp.2017.10.021)
- Bilbao, S., Ducceschi, M. & Zama, F. Explicit exactly energy-conserving methods for Hamiltonian systems. Journal of Computational Physics 472, 111697 (2023) -- [10.1016/j.jcp.2022.111697](https://doi.org/10.1016/j.jcp.2022.111697)
- Sherman, J. & Morrison, W. J. Adjustment of an Inverse Matrix Corresponding to a Change in One Element of a Given Matrix. Ann. Math. Statist. 21, 124–127 (1950) -- [10.1214/aoms/1177729893](https://doi.org/10.1214/aoms/1177729893)
- [Brugnoli, A., Rashad, R., Califano, F., Stramigioli, S. & Matignon, D. Mixed finite elements for port-Hamiltonian models of von Kármán beams. IFAC-PapersOnLine 54, 186–191 (2021)](mixed-finite-elements-for-port-hamiltonian-models-of-von-karman-beams) -- [10.1016/j.ifacol.2021.11.076](https://doi.org/10.1016/j.ifacol.2021.11.076)
- Kröner, E. Allgemeine Kontinuumstheorie der Versetzungen und Eigenspannungen. Arch. Rational Mech. Anal. 4, 273–334 (1959) -- [10.1007/bf00281393](https://doi.org/10.1007/bf00281393)
- [Thoma, T., Kotyczka, P. & Egger, H. On the velocity-stress formulation for geometrically nonlinear elastodynamics and its structure-preserving discretization. Mathematical and Computer Modelling of Dynamical Systems 30, 701–720 (2024)](on-the-velocity-stress-formulation-for-geometrically-nonlinear-elastodynamics-and-its-structure-preserving-discretization) -- [10.1080/13873954.2024.2397486](https://doi.org/10.1080/13873954.2024.2397486)
- [Kinon, P. L., Thoma, T., Betsch, P. & Kotyczka, P. Discrete nonlinear elastodynamics in a port‐Hamiltonian framework. Proc Appl Math and Mech 23, (2023)](discrete-nonlinear-elastodynamics-in-a-port-hamiltonian-framework) -- [10.1002/pamm.202300144](https://doi.org/10.1002/pamm.202300144)
- [Kinon, P. L., Betsch, P. & Eugster, S. R. Energy-momentum-consistent simulation of planar geometrically exact beams in a port-Hamiltonian framework. Multibody Syst Dyn (2025) doi:10.1007/s11044-025-10087-9](energy-momentum-consistent-simulation-of-planar-geometrically-exact-beams-in-a-port-hamiltonian-framework0) -- [10.1007/s11044-025-10087-9](https://doi.org/10.1007/s11044-025-10087-9)
- Strogatz, S. H. Nonlinear Dynamics and Chaos. (CRC Press, 2018). doi:10.1201/9780429492563 -- [10.1201/9780429492563](https://doi.org/10.1201/9780429492563)
- Bilbao, S., Thomas, O., Touzé, C. & Ducceschi, M. Conservative numerical methods for the Full von Kármán plate equations. Numerical Methods Partial 31, 1948–1970 (2015) -- [10.1002/num.21974](https://doi.org/10.1002/num.21974)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part I: Mindlin model for thick plates. Applied Mathematical Modelling 75, 940–960 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V. & Matignon, D. Port-Hamiltonian formulation and symplectic discretization of plate models Part II: Kirchhoff model for thin plates. Applied Mathematical Modelling 75, 961–981 (2019)](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-ii-kirchhoff-model-for-thin-plates) -- [10.1016/j.apm.2019.04.036](https://doi.org/10.1016/j.apm.2019.04.036)
- Bilbao, S. A family of conservative finite difference schemes for the dynamical von Karman plate equations. Numerical Methods Partial 24, 193–216 (2007) -- [10.1002/num.20260](https://doi.org/10.1002/num.20260)
- Sifakis, E. & Barbic, J. FEM simulation of 3D deformable solids. ACM SIGGRAPH 2012 Courses 1–50 (2012) doi:10.1145/2343483.2343501 -- [10.1145/2343483.2343501](https://doi.org/10.1145/2343483.2343501)
- [Hairer, E., Lubich, C. & Wanner, G. Geometric numerical integration illustrated by the Störmer–Verlet method. Acta Numerica 12, 399–450 (2003)](geometric-numerical-integration-illustrated-by-the-stormer-verlet-method) -- [10.1017/s0962492902000144](https://doi.org/10.1017/s0962492902000144)
- Rathgeber, F. et al. Firedrake. ACM Trans. Math. Softw. 43, 1–27 (2016) -- [10.1145/2998441](https://doi.org/10.1145/2998441)
- Gibson, T. H., Mitchell, L., Ham, D. A. & Cotter, C. J. Slate: extending Firedrake’s domain-specific abstraction to hybridized solvers for geoscience and beyond. Geosci. Model Dev. 13, 735–761 (2020) -- [10.5194/gmd-13-735-2020](https://doi.org/10.5194/gmd-13-735-2020)
- Wathen, A. J. Preconditioning. Acta Numerica 24, 329–376 (2015) -- [10.1017/s0962492915000021](https://doi.org/10.1017/s0962492915000021)
- Scovazzi, G., Carnes, B., Zeng, X. & Rossi, S. A simple, stable, and accurate linear tetrahedral finite element for transient, nearly, and fully incompressible solid dynamics: a dynamic variational multiscale approach. Numerical Meth Engineering 106, 799–839 (2015) -- [10.1002/nme.5138](https://doi.org/10.1002/nme.5138)

