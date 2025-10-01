---
title: "An improved Riemann SPH-Hamiltonian SPH coupled solver for hydroelastic fluid-structure interactions"
date: 2023-11-09 00:00:00 +0100
permalink: an-improved-riemann-sph-hamiltonian-sph-coupled-solver-for-hydroelastic-fluid-structure-interactions
year: 2024
authors: Abbas Khayyer, Hitoshi Gotoh, Yuma Shimizu, Takafumi Gotoh
category: articles
tags:
  - Smoothed particle hydrodynamics
  - Riemann SPH
  - Hamiltonian SPH
  - Fluid-structure interaction
  - Enhanced schemes
---
 
## Authors
[Abbas Khayyer](authors/abbas-khayyer), [Hitoshi Gotoh](authors/hitoshi-gotoh), [Yuma Shimizu](authors/yuma-shimizu), [Takafumi Gotoh](authors/takafumi-gotoh)
 
## Abstract
The paper presents a novel Lagrangian meshfree computational solver for simulation of hydroelastic fluid-elastic structure interaction (FSI) problems. An explicit Smoothed Particle Hydrodynamics (SPH) method, referred to as Riemann SPH, is adopted as the fluid model, and a SPH method within the Hamiltonian framework, namely Hamiltonian SPH (HSPH), is considered as the structure model. A two-way coupling between fluid and structure models is performed in a consistent manner, resulting in a coupled RSPH-HSPH hydroelastic FSI solver. For enhancement of accuracy and robustness of the proposed FSI solver, four refined schemes are incorporated for the fluid and structure models. These four refined schemes include (i) a novel dissipation limiter in the fluid's continuity equation for enforcing the volume conservation, (ii) a refined reconstruction of the quantities in Riemann SPH in the presence of a potential field, (iii) a modified velocity-divergence error mitigation term in the fluid's momentum equation for enhanced satisfaction of the incompressibility condition, and (iv) a Riemann diffusion term in the structural momentum equation for enhanced stability and robustness. Validations of the proposed FSI solver are carried out through a series of fluid, structure and FSI benchmark tests.
 
## Keywords
Smoothed particle hydrodynamics; Riemann SPH; Hamiltonian SPH; Fluid-structure interaction; Enhanced schemes
 
## Citation
- **Journal:** Engineering Analysis with Boundary Elements
- **Year:** 2024
- **Volume:** 158
- **Issue:** 
- **Pages:** 332--355
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.enganabound.2023.10.018](https://doi.org/10.1016/j.enganabound.2023.10.018)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Khayyer_2024,
  title={{An improved Riemann SPH-Hamiltonian SPH coupled solver for hydroelastic fluid-structure interactions}},
  volume={158},
  ISSN={0955-7997},
  DOI={10.1016/j.enganabound.2023.10.018},
  journal={Engineering Analysis with Boundary Elements},
  publisher={Elsevier BV},
  author={Khayyer, Abbas and Gotoh, Hitoshi and Shimizu, Yuma and Gotoh, Takafumi},
  year={2024},
  pages={332--355}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/an-improved-riemann-sph-hamiltonian-sph-coupled-solver-for-hydroelastic-fluid-structure-interactions.bib)
 
## References
- KOSHIZUKA, S. Current Achievements and Future Perspectives on Particle Simulation Technologies for Fluid Dynamics and Heat Transfer. Journal of Nuclear Science and Technology vol. 48 155–168 (2011) -- [10.1080/18811248.2011.9711690](https://doi.org/10.1080/18811248.2011.9711690)
- Gotoh, H. & Khayyer, A. On the state-of-the-art of particle methods for coastal and ocean engineering. Coastal Engineering Journal vol. 60 79–103 (2018) -- [10.1080/21664250.2018.1436243](https://doi.org/10.1080/21664250.2018.1436243)
- Gingold, R. A. & Monaghan, J. J. Smoothed particle hydrodynamics: theory and application to non-spherical stars. Monthly Notices of the Royal Astronomical Society vol. 181 375–389 (1977) -- [10.1093/mnras/181.3.375](https://doi.org/10.1093/mnras/181.3.375)
- Koshizuka, S. & Oka, Y. Moving-Particle Semi-Implicit Method for Fragmentation of Incompressible Fluid. Nuclear Science and Engineering vol. 123 421–434 (1996) -- [10.13182/nse96-a24205](https://doi.org/10.13182/nse96-a24205)
- Ye, T., Pan, D., Huang, C. & Liu, M. Smoothed particle hydrodynamics (SPH) for complex fluid flows: Recent developments in methodology and applications. Physics of Fluids vol. 31 (2019) -- [10.1063/1.5068697](https://doi.org/10.1063/1.5068697)
- Lyu, H.-G. et al. SPHydro: Promoting smoothed particle hydrodynamics method toward extensive applications in ocean engineering. Physics of Fluids vol. 35 (2023) -- [10.1063/5.0133782](https://doi.org/10.1063/5.0133782)
- Luo, M., Khayyer, A. & Lin, P. Particle methods in ocean and coastal engineering. Applied Ocean Research vol. 114 102734 (2021) -- [10.1016/j.apor.2021.102734](https://doi.org/10.1016/j.apor.2021.102734)
- Domínguez, J. M. et al. DualSPHysics: from fluid dynamics to multiphysics problems. Computational Particle Mechanics vol. 9 867–895 (2021) -- [10.1007/s40571-021-00404-2](https://doi.org/10.1007/s40571-021-00404-2)
- Shimizu, Y., Khayyer, A., Gotoh, H. & Nagashima, K. An enhanced multiphase ISPH-based method for accurate modeling of oil spill. Coastal Engineering Journal vol. 62 625–646 (2020) -- [10.1080/21664250.2020.1815362](https://doi.org/10.1080/21664250.2020.1815362)
- Tsuruta, N., Gotoh, H., Suzuki, K., Ikari, H. & Shimosako, K. Development of PARISPHERE as the particle-based numerical wave flume for coastal engineering problems. Coastal Engineering Journal vol. 61 41–62 (2019) -- [10.1080/21664250.2018.1560683](https://doi.org/10.1080/21664250.2018.1560683)
- Tazaki, T., Harada, E. & Gotoh, H. Grain-scale investigation of swash zone sediment transport on a gravel beach using DEM-MPS coupled scheme. Coastal Engineering Journal vol. 65 347–368 (2023) -- [10.1080/21664250.2023.2202958](https://doi.org/10.1080/21664250.2023.2202958)
- Vacondio, R. et al. Grand challenges for Smoothed Particle Hydrodynamics numerical schemes. Computational Particle Mechanics vol. 8 575–588 (2020) -- [10.1007/s40571-020-00354-1](https://doi.org/10.1007/s40571-020-00354-1)
- Xie, F., Zhao, W. & Wan, D. Overview of Moving Particle Semi-implicit Techniques for Hydrodynamic Problems in Ocean Engineering. Journal of Marine Science and Application vol. 21 1–22 (2022) -- [10.1007/s11804-022-00284-9](https://doi.org/10.1007/s11804-022-00284-9)
- He, M., Liang, D., Ren, B., Li, J. & Shao, S. Wave interactions with multi-float structures: SPH model, experimental validation, and parametric study. Coastal Engineering vol. 184 104333 (2023) -- [10.1016/j.coastaleng.2023.104333](https://doi.org/10.1016/j.coastaleng.2023.104333)
- Zhang, Z. L., Khalid, M. S. U., Long, T., Liu, M. B. & Shu, C. Improved element-particle coupling strategy with δ-SPH and particle shifting for modeling sloshing with rigid or deformable structures. Applied Ocean Research vol. 114 102774 (2021) -- [10.1016/j.apor.2021.102774](https://doi.org/10.1016/j.apor.2021.102774)
- Tang, Y., Jiang, Q. & Zhou, C. A Lagrangian-based SPH-DEM model for fluid–solid interaction with free surface flow in two dimensions. Applied Mathematical Modelling vol. 62 436–460 (2018) -- [10.1016/j.apm.2018.06.013](https://doi.org/10.1016/j.apm.2018.06.013)
- El Rahi, J. et al. Numerical investigation of wave-induced flexible vegetation dynamics in 3D using a coupling between DualSPHysics and the FEA module of Project Chrono. Ocean Engineering vol. 285 115227 (2023) -- [10.1016/j.oceaneng.2023.115227](https://doi.org/10.1016/j.oceaneng.2023.115227)
- Ng, K. C., Low, W. C., Chen, H., Tafuni, A. & Nakayama, A. A three-dimensional fluid-structure interaction model based on SPH and lattice-spring method for simulating complex hydroelastic problems. Ocean Engineering vol. 260 112026 (2022) -- [10.1016/j.oceaneng.2022.112026](https://doi.org/10.1016/j.oceaneng.2022.112026)
- Chen, C., Shi, W.-K., Shen, Y.-M., Chen, J.-Q. & Zhang, A.-M. A multi-resolution SPH-FEM method for fluid–structure interactions. Computer Methods in Applied Mechanics and Engineering vol. 401 115659 (2022) -- [10.1016/j.cma.2022.115659](https://doi.org/10.1016/j.cma.2022.115659)
- Xue, B., Wang, S.-P., Peng, Y.-X. & Zhang, A.-M. A novel coupled Riemann SPH–RKPM model for the simulation of weakly compressible fluid–structure interaction problems. Ocean Engineering vol. 266 112447 (2022) -- [10.1016/j.oceaneng.2022.112447](https://doi.org/10.1016/j.oceaneng.2022.112447)
- Xu, Y., Yu, C., Liu, F. & Liu, Q. A coupled NMM-SPH method for fluid-structure interaction problems. Applied Mathematical Modelling vol. 76 466–478 (2019) -- [10.1016/j.apm.2019.06.020](https://doi.org/10.1016/j.apm.2019.06.020)
- Sun, W.-K., Zhang, L.-W. & Liew, K. M. A coupled SPH-PD model for fluid–structure interaction in an irregular channel flow considering the structural failure. Computer Methods in Applied Mechanics and Engineering vol. 401 115573 (2022) -- [10.1016/j.cma.2022.115573](https://doi.org/10.1016/j.cma.2022.115573)
- Zhang, Z., Shu, C., Khalid, M. S. U., Yuan, Z. & Liu, W. Investigations on the hydroelastic slamming of deformable wedges by using the smoothed particle element method. Journal of Fluids and Structures vol. 114 103732 (2022) -- [10.1016/j.jfluidstructs.2022.103732](https://doi.org/10.1016/j.jfluidstructs.2022.103732)
- Zhang, Z., Shu, C., Liu, Y., Liu, W. & Khalid, M. S. U. An improved M-SPEM for modeling complex hydroelastic fluid-structure interaction problems. Journal of Computational Physics vol. 488 112233 (2023) -- [10.1016/j.jcp.2023.112233](https://doi.org/10.1016/j.jcp.2023.112233)
- Gotoh, H., Khayyer, A. & Shimizu, Y. Entirely Lagrangian meshfree computational methods for hydroelastic fluid-structure interactions in ocean engineering—Reliability, adaptivity and generality. Applied Ocean Research vol. 115 102822 (2021) -- [10.1016/j.apor.2021.102822](https://doi.org/10.1016/j.apor.2021.102822)
- Khayyer, A., Gotoh, H. & Shimizu, Y. On systematic development of FSI solvers in the context of particle methods. Journal of Hydrodynamics vol. 34 395–407 (2022) -- [10.1007/s42241-022-0042-3](https://doi.org/10.1007/s42241-022-0042-3)
- Liu, M. & Zhang, Z. Smoothed particle hydrodynamics (SPH) for modeling fluid-structure interactions. Science China Physics, Mechanics &amp; Astronomy vol. 62 (2019) -- [10.1007/s11433-018-9357-0](https://doi.org/10.1007/s11433-018-9357-0)
- Marrone, S. et al. δ-SPH model for simulating violent impact flows. Computer Methods in Applied Mechanics and Engineering vol. 200 1526–1542 (2011) -- [10.1016/j.cma.2010.12.016](https://doi.org/10.1016/j.cma.2010.12.016)
- Inutsuka, S. Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. Journal of Computational Physics vol. 179 238–267 (2002) -- [10.1006/jcph.2002.7053](https://doi.org/10.1006/jcph.2002.7053)
- Shao, S. & Lo, E. Y. M. Incompressible SPH method for simulating Newtonian and non-Newtonian flows with a free surface. Advances in Water Resources vol. 26 787–800 (2003) -- [10.1016/s0309-1708(03)00030-7](https://doi.org/10.1016/s0309-1708(03)00030-7)
- Rafiee, A. & Thiagarajan, K. P. An SPH projection method for simulating fluid-hypoelastic structure interaction. Computer Methods in Applied Mechanics and Engineering vol. 198 2785–2795 (2009) -- [10.1016/j.cma.2009.04.001](https://doi.org/10.1016/j.cma.2009.04.001)
- Gray, J. P., Monaghan, J. J. & Swift, R. P. SPH elastic dynamics. Computer Methods in Applied Mechanics and Engineering vol. 190 6641–6662 (2001) -- [10.1016/s0045-7825(01)00254-7](https://doi.org/10.1016/s0045-7825(01)00254-7)
- Bonet, J. & Kulasegaram, S. Alternative Total Lagrangian Formulations for Corrected Smooth Particle Hydrodynamics (CSPH) Methods in Large Strain Dynamic Problems. Revue Européenne des Éléments Finis vol. 11 893–912 (2002) -- [10.3166/reef.11.893-912](https://doi.org/10.3166/reef.11.893-912)
- [Khayyer, A., Shimizu, Y., Gotoh, H. & Nagashima, K. A coupled incompressible SPH-Hamiltonian SPH solver for hydroelastic FSI corresponding to composite structures. Applied Mathematical Modelling vol. 94 242–271 (2021)](a-coupled-incompressible-sph-hamiltonian-sph-solver-for-hydroelastic-fsi-corresponding-to-composite-structures) -- [10.1016/j.apm.2021.01.011](https://doi.org/10.1016/j.apm.2021.01.011)
- Rider, W. J. A review of approximate riemann solvers with Godunov’s method in lagrangian coordinates. Computers &amp; Fluids vol. 23 397–413 (1994) -- [10.1016/0045-7930(94)90047-7](https://doi.org/10.1016/0045-7930(94)90047-7)
- Zhang, C. et al. SPHinXsys: An open-source multi-physics and multi-resolution library based on smoothed particle hydrodynamics. Computer Physics Communications vol. 267 108066 (2021) -- [10.1016/j.cpc.2021.108066](https://doi.org/10.1016/j.cpc.2021.108066)
- Pilloton, C., Bardazzi, A., Colagrossi, A. & Marrone, S. SPH method for long-time simulations of sloshing flows in LNG tanks. European Journal of Mechanics - B/Fluids vol. 93 65–92 (2022) -- [10.1016/j.euromechflu.2022.01.002](https://doi.org/10.1016/j.euromechflu.2022.01.002)
- Zhang, C., Hu, X. Y. & Adams, N. A. A weakly compressible SPH method based on a low-dissipation Riemann solver. Journal of Computational Physics vol. 335 605–620 (2017) -- [10.1016/j.jcp.2017.01.027](https://doi.org/10.1016/j.jcp.2017.01.027)
- Zhang, C., Zhu, Y., Wu, D., Adams, N. A. & Hu, X. Smoothed particle hydrodynamics: Methodology development and recent achievement. Journal of Hydrodynamics vol. 34 767–805 (2022) -- [10.1007/s42241-022-0052-1](https://doi.org/10.1007/s42241-022-0052-1)
- Meng, Z.-F., Wang, P.-P., Zhang, A.-M., Ming, F.-R. & Sun, P.-N. A multiphase SPH model based on Roe’s approximate Riemann solver for hydraulic flows with complex interface. Computer Methods in Applied Mechanics and Engineering vol. 365 112999 (2020) -- [10.1016/j.cma.2020.112999](https://doi.org/10.1016/j.cma.2020.112999)
- Suzuki, Y. & Koshizuka, S. A Hamiltonian particle method for non‐linear elastodynamics. International Journal for Numerical Methods in Engineering vol. 74 1344–1373 (2007) -- [10.1002/nme.2222](https://doi.org/10.1002/nme.2222)
- Khayyer, A., Gotoh, H., Shimizu, Y. & Nishijima, Y. A 3D Lagrangian meshfree projection-based solver for hydroelastic Fluid–Structure​ Interactions. Journal of Fluids and Structures vol. 105 103342 (2021) -- [10.1016/j.jfluidstructs.2021.103342](https://doi.org/10.1016/j.jfluidstructs.2021.103342)
- O'connor, A fluid-structure interaction model for free-surface flows and flexible structures using smoothed particle hydrodynamics on a GPU. J Fluid Struct (2021)
- Zhan, L., Peng, C., Zhang, B. & Wu, W. A stabilized TL–WC SPH approach with GPU acceleration for three-dimensional fluid–structure interaction. Journal of Fluids and Structures vol. 86 329–353 (2019) -- [10.1016/j.jfluidstructs.2019.02.002](https://doi.org/10.1016/j.jfluidstructs.2019.02.002)
- Khayyer, A., Shimizu, Y., Gotoh, H. & Hattori, S. Multi-resolution ISPH-SPH for accurate and efficient simulation of hydroelastic fluid-structure interactions in ocean engineering. Ocean Engineering vol. 226 108652 (2021) -- [10.1016/j.oceaneng.2021.108652](https://doi.org/10.1016/j.oceaneng.2021.108652)
- Belytschko, T., Guo, Y., Kam Liu, W. & Ping Xiao, S. A unified stability analysis of meshless particle methods. International Journal for Numerical Methods in Engineering vol. 48 1359–1400 (2000) -- [10.1002/1097-0207(20000730)48:9<1359::aid-nme829>3.0.co;2-u](https://doi.org/10.1002/1097-0207(20000730)48:9<1359::aid-nme829>3.0.co;2-u)
- Vignjevic, R., Campbell, J. & Libersky, L. A treatment of zero-energy modes in the smoothed particle hydrodynamics method. Computer Methods in Applied Mechanics and Engineering vol. 184 67–85 (2000) -- [10.1016/s0045-7825(99)00441-7](https://doi.org/10.1016/s0045-7825(99)00441-7)
- Monaghan, J. J. & Gingold, R. A. Shock simulation by the particle method SPH. Journal of Computational Physics vol. 52 374–389 (1983) -- [10.1016/0021-9991(83)90036-0](https://doi.org/10.1016/0021-9991(83)90036-0)
- Tsuruta, N., Khayyer, A. & Gotoh, H. A short note on Dynamic Stabilization of Moving Particle Semi-implicit method. Computers &amp; Fluids vol. 82 158–164 (2013) -- [10.1016/j.compfluid.2013.05.001](https://doi.org/10.1016/j.compfluid.2013.05.001)
- Wendland, H. Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree. Advances in Computational Mathematics vol. 4 389–396 (1995) -- [10.1007/bf02123482](https://doi.org/10.1007/bf02123482)
- Antuono, M., Colagrossi, A. & Marrone, S. Numerical diffusive terms in weakly-compressible SPH schemes. Computer Physics Communications vol. 183 2570–2580 (2012) -- [10.1016/j.cpc.2012.07.006](https://doi.org/10.1016/j.cpc.2012.07.006)
- Monaghan, J. J. Simulating Free Surface Flows with SPH. Journal of Computational Physics vol. 110 399–406 (1994) -- [10.1006/jcph.1994.1034](https://doi.org/10.1006/jcph.1994.1034)
- Shimizu, Y., Khayyer, A. & Gotoh, H. An SPH-based fully-Lagrangian meshfree implicit FSI solver with high-order discretization terms. Engineering Analysis with Boundary Elements vol. 137 160–181 (2022) -- [10.1016/j.enganabound.2021.10.023](https://doi.org/10.1016/j.enganabound.2021.10.023)
- [Khayyer, A., Shimizu, Y., Gotoh, H. & Hattori, S. A 3D SPH-based entirely Lagrangian meshfree hydroelastic FSI solver for anisotropic composite structures. Applied Mathematical Modelling vol. 112 560–613 (2022)](a-3d-sph-based-entirely-lagrangian-meshfree-hydroelastic-fsi-solver-for-anisotropic-composite-structures) -- [10.1016/j.apm.2022.07.031](https://doi.org/10.1016/j.apm.2022.07.031)
- Shimizu, Y., Gotoh, H., Khayyer, A. & Kita, K. Fundamental Investigation on the Applicability of a Higher-Order Consistent ISPH Method. International Journal of Offshore and Polar Engineering vol. 32 275–284 (2022) -- [10.17736/ijope.2022.jc868](https://doi.org/10.17736/ijope.2022.jc868)
- Duan, G., Yamaji, A., Koshizuka, S. & Chen, B. The truncation and stabilization error in multiphase moving particle semi-implicit method based on corrective matrix: Which is dominant? Computers &amp; Fluids vol. 190 254–273 (2019) -- [10.1016/j.compfluid.2019.06.023](https://doi.org/10.1016/j.compfluid.2019.06.023)
- Sun, P. N., Le Touzé, D. & Zhang, A.-M. Study of a complex fluid-structure dam-breaking benchmark problem using a multi-phase SPH method with APR. Engineering Analysis with Boundary Elements vol. 104 240–258 (2019) -- [10.1016/j.enganabound.2019.03.033](https://doi.org/10.1016/j.enganabound.2019.03.033)
- Adami, S., Hu, X. Y. & Adams, N. A. A generalized wall boundary condition for smoothed particle hydrodynamics. Journal of Computational Physics vol. 231 7057–7075 (2012) -- [10.1016/j.jcp.2012.05.005](https://doi.org/10.1016/j.jcp.2012.05.005)
- Green, M. D., Vacondio, R. & Peiró, J. A smoothed particle hydrodynamics numerical scheme with a consistent diffusion term for the continuity equation. Computers &amp; Fluids vol. 179 632–644 (2019) -- [10.1016/j.compfluid.2018.11.020](https://doi.org/10.1016/j.compfluid.2018.11.020)
- Meng, Z.-F., Zhang, A.-M., Wang, P.-P. & Ming, F.-R. A shock-capturing scheme with a novel limiter for compressible flows solved by smoothed particle hydrodynamics. Computer Methods in Applied Mechanics and Engineering vol. 386 114082 (2021) -- [10.1016/j.cma.2021.114082](https://doi.org/10.1016/j.cma.2021.114082)
- Sun, P. N., Colagrossi, A., Marrone, S., Antuono, M. & Zhang, A.-M. A consistent approach to particle shifting in the<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll" id="d1e1386" altimg="si213.gif"><mml:mi>δ</mml:mi></mml:math>-<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll" id="d1e1391" altimg="si6.gif"><mml:mi mathvariant="bold-italic">Plus</mml:mi></mml:math>-SPH model. Computer Methods in Applied Mechanics and Engineering vol. 348 912–934 (2019) -- [10.1016/j.cma.2019.01.045](https://doi.org/10.1016/j.cma.2019.01.045)
- Antuono, M., Colagrossi, A., Marrone, S. & Molteni, D. Free-surface flows solved by means of SPH schemes with numerical diffusive terms. Computer Physics Communications vol. 181 532–549 (2010) -- [10.1016/j.cpc.2009.11.002](https://doi.org/10.1016/j.cpc.2009.11.002)
- Fourtakas, G., Dominguez, J. M., Vacondio, R. & Rogers, B. D. Local uniform stencil (LUST) boundary condition for arbitrary 3-D boundaries in parallel smoothed particle hydrodynamics (SPH) models. Computers &amp; Fluids vol. 190 346–361 (2019) -- [10.1016/j.compfluid.2019.06.009](https://doi.org/10.1016/j.compfluid.2019.06.009)
- Wen, H., Ren, B. & Yu, X. An improved SPH model for turbulent hydrodynamics of a 2D oscillating water chamber. Ocean Engineering vol. 150 152–166 (2018) -- [10.1016/j.oceaneng.2017.12.047](https://doi.org/10.1016/j.oceaneng.2017.12.047)
- Khayyer, A., Shimizu, Y., Gotoh, T. & Gotoh, H. Enhanced resolution of the continuity equation in explicit weakly compressible SPH simulations of incompressible free‐surface fluid flows. Applied Mathematical Modelling vol. 116 84–121 (2023) -- [10.1016/j.apm.2022.10.037](https://doi.org/10.1016/j.apm.2022.10.037)
- Sun, P. N., Pilloton, C., Antuono, M. & Colagrossi, A. Inclusion of an acoustic damper term in weakly-compressible SPH models. Journal of Computational Physics vol. 483 112056 (2023) -- [10.1016/j.jcp.2023.112056](https://doi.org/10.1016/j.jcp.2023.112056)
- [Shimizu, Y., Khayyer, A. & Gotoh, H. An implicit SPH-based structure model for accurate Fluid–Structure Interaction simulations with hourglass control scheme. European Journal of Mechanics - B/Fluids vol. 96 122–145 (2022)](an-implicit-sph-based-structure-model-for-accurate-fluid-structure-interaction-simulations-with-hourglass-control-scheme) -- [10.1016/j.euromechflu.2022.07.007](https://doi.org/10.1016/j.euromechflu.2022.07.007)
- Ganzenmüller, G. C. An hourglass control algorithm for Lagrangian Smooth Particle Hydrodynamics. Computer Methods in Applied Mechanics and Engineering vol. 286 87–106 (2015) -- [10.1016/j.cma.2014.12.005](https://doi.org/10.1016/j.cma.2014.12.005)
- Zhang, C. et al. An artificial damping method for total Lagrangian SPH method with application in biomechanics. Engineering Analysis with Boundary Elements vol. 143 1–13 (2022) -- [10.1016/j.enganabound.2022.05.022](https://doi.org/10.1016/j.enganabound.2022.05.022)
- Khayyer, A., Gotoh, H., Falahaty, H. & Shimizu, Y. Towards development of enhanced fully-Lagrangian mesh-free computational methods for fluid-structure interaction. Journal of Hydrodynamics vol. 30 49–61 (2018) -- [10.1007/s42241-018-0005-x](https://doi.org/10.1007/s42241-018-0005-x)
- Khayyer, A. & Gotoh, H. A higher order Laplacian model for enhancement and stabilization of pressure calculation by the MPS method. Applied Ocean Research vol. 32 124–131 (2010) -- [10.1016/j.apor.2010.01.001](https://doi.org/10.1016/j.apor.2010.01.001)
- Monaghan, J. J. & Rafiee, A. A simple SPH algorithm for multi‐fluid flow with high density ratios. International Journal for Numerical Methods in Fluids vol. 71 537–561 (2012) -- [10.1002/fld.3671](https://doi.org/10.1002/fld.3671)
- Wu, G. X. & Eatock Taylor, R. Finite element analysis of two-dimensional non-linear transient water waves. Applied Ocean Research vol. 16 363–372 (1994) -- [10.1016/0141-1187(94)00029-8](https://doi.org/10.1016/0141-1187(94)00029-8)
- Antuono, M., Marrone, S., Colagrossi, A. & Bouscasse, B. Energy balance in the <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si3.gif" display="inline" overflow="scroll"><mml:mi>δ</mml:mi></mml:math>-SPH scheme. Computer Methods in Applied Mechanics and Engineering vol. 289 209–226 (2015) -- [10.1016/j.cma.2015.02.004](https://doi.org/10.1016/j.cma.2015.02.004)
- Meng, Z.-F., Zhang, A.-M., Yan, J.-L., Wang, P.-P. & Khayyer, A. A hydroelastic fluid–structure interaction solver based on the Riemann-SPH method. Computer Methods in Applied Mechanics and Engineering vol. 390 114522 (2022) -- [10.1016/j.cma.2021.114522](https://doi.org/10.1016/j.cma.2021.114522)
- Fourey, G., Hermange, C., Le Touzé, D. & Oger, G. An efficient FSI coupling strategy between Smoothed Particle Hydrodynamics and Finite Element methods. Computer Physics Communications vol. 217 66–81 (2017) -- [10.1016/j.cpc.2017.04.005](https://doi.org/10.1016/j.cpc.2017.04.005)
- Liao, K., Hu, C. & Sueyoshi, M. Free surface flow impacting on an elastic structure: Experiment versus numerical simulation. Applied Ocean Research vol. 50 192–208 (2015) -- [10.1016/j.apor.2015.02.002](https://doi.org/10.1016/j.apor.2015.02.002)
- Liao, Numerical simulation of free surface flow impacting on an elastic plate. (2014)
- Idelsohn, S. R., Marti, J., Souto-Iglesias, A. & Oñate, E. Interaction between an elastic structure and free-surface flows: experimental versus numerical comparisons using the PFEM. Computational Mechanics vol. 43 125–132 (2008) -- [10.1007/s00466-008-0245-7](https://doi.org/10.1007/s00466-008-0245-7)
- Cercos-Pita, J. L., Dalrymple, R. A. & Herault, A. Diffusive terms for the conservation of mass equation in SPH. Applied Mathematical Modelling vol. 40 8722–8736 (2016) -- [10.1016/j.apm.2016.05.016](https://doi.org/10.1016/j.apm.2016.05.016)
- Ren, Y., Khayyer, A., Lin, P. & Hu, X. Numerical modeling of sloshing flow interaction with an elastic baffle using SPHinXsys. Ocean Engineering vol. 267 113110 (2023) -- [10.1016/j.oceaneng.2022.113110](https://doi.org/10.1016/j.oceaneng.2022.113110)
- Zhang, C., Zhu, Y., Lyu, X. & Hu, X. An efficient and generalized solid boundary condition for SPH: Applications to multi-phase flow and fluid–structure interaction. European Journal of Mechanics - B/Fluids vol. 94 276–292 (2022) -- [10.1016/j.euromechflu.2022.03.011](https://doi.org/10.1016/j.euromechflu.2022.03.011)
- Sun, Y. et al. A conservative particle splitting and merging technique with dynamic pattern and minimum density error. Engineering Analysis with Boundary Elements vol. 150 246–258 (2023) -- [10.1016/j.enganabound.2023.02.018](https://doi.org/10.1016/j.enganabound.2023.02.018)
- Zhang, C., Rezavand, M. & Hu, X. Dual-criteria time stepping for weakly compressible smoothed particle hydrodynamics. Journal of Computational Physics vol. 404 109135 (2020) -- [10.1016/j.jcp.2019.109135](https://doi.org/10.1016/j.jcp.2019.109135)
- Zhang, G. et al. A<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" id="d1e1106" altimg="si210.svg"><mml:mi>δ</mml:mi></mml:math>SPH–SPIM coupled method for fluid–structure interaction problems. Journal of Fluids and Structures vol. 101 103210 (2021) -- [10.1016/j.jfluidstructs.2020.103210](https://doi.org/10.1016/j.jfluidstructs.2020.103210)
- Szymczak, Energy-losses in nonclassical free-surface flows. Fluid Mec A (1994)
- Meringolo, D. D., Colagrossi, A., Marrone, S. & Aristodemo, F. On the filtering of acoustic components in weakly-compressible SPH simulations. Journal of Fluids and Structures vol. 70 1–23 (2017) -- [10.1016/j.jfluidstructs.2017.01.005](https://doi.org/10.1016/j.jfluidstructs.2017.01.005)
- Martínez-Estévez, I. et al. Coupling an SPH-based solver with an FEA structural solver to simulate free surface flows interacting with flexible structures. Computer Methods in Applied Mechanics and Engineering vol. 410 115989 (2023) -- [10.1016/j.cma.2023.115989](https://doi.org/10.1016/j.cma.2023.115989)
- Greco, A two-dimensional study of green-water loading. (2001)
- Paik, K.-J. & Carrica, P. M. Fluid–structure interaction for an elastic structure interacting with free surface in a rolling tank. Ocean Engineering vol. 84 201–212 (2014) -- [10.1016/j.oceaneng.2014.04.016](https://doi.org/10.1016/j.oceaneng.2014.04.016)
- Lind, S. J., Xu, R., Stansby, P. K. & Rogers, B. D. Incompressible smoothed particle hydrodynamics for free-surface flows: A generalised diffusion-based algorithm for stability and validations for impulsive flows and propagating waves. Journal of Computational Physics vol. 231 1499–1523 (2012) -- [10.1016/j.jcp.2011.10.027](https://doi.org/10.1016/j.jcp.2011.10.027)
- Khayyer, A., Gotoh, H. & Shimizu, Y. Comparative study on accuracy and conservation properties of two particle regularization schemes and proposal of an optimized particle shifting scheme in ISPH context. Journal of Computational Physics vol. 332 236–256 (2017) -- [10.1016/j.jcp.2016.12.005](https://doi.org/10.1016/j.jcp.2016.12.005)
- Lyu, H.-G., Sun, P.-N., Huang, X.-T., Chen, S.-H. & Zhang, A.-M. On removing the numerical instability induced by negative pressures in SPH simulations of typical fluid–structure interaction problems in ocean engineering. Applied Ocean Research vol. 117 102938 (2021) -- [10.1016/j.apor.2021.102938](https://doi.org/10.1016/j.apor.2021.102938)
- Huang, C., Long, T., Li, S. M. & Liu, M. B. A kernel gradient-free SPH method with iterative particle shifting technology for modeling low-Reynolds flows around airfoils. Engineering Analysis with Boundary Elements vol. 106 571–587 (2019) -- [10.1016/j.enganabound.2019.06.010](https://doi.org/10.1016/j.enganabound.2019.06.010)
- Low, W. C., Ng, K. C. & Ng, H. K. A SPH-lattice spring method for modelling Fluid Structure Interaction involving composite body and free surface. Computational Particle Mechanics vol. 10 1587–1612 (2023) -- [10.1007/s40571-023-00576-z](https://doi.org/10.1007/s40571-023-00576-z)
- Lee, C. H., Refachinho de Campos, P. R., Gil, A. J., Giacomini, M. & Bonet, J. An entropy-stable updated reference Lagrangian smoothed particle hydrodynamics algorithm for thermo-elasticity and thermo-visco-plasticity. Computational Particle Mechanics vol. 10 1493–1531 (2023) -- [10.1007/s40571-023-00564-3](https://doi.org/10.1007/s40571-023-00564-3)
- Michel, J., Antuono, M., Oger, G. & Marrone, S. Energy balance in quasi-Lagrangian Riemann-based SPH schemes. Computer Methods in Applied Mechanics and Engineering vol. 410 116015 (2023) -- [10.1016/j.cma.2023.116015](https://doi.org/10.1016/j.cma.2023.116015)

