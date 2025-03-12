---
layout: post
title: "An implicit SPH-based structure model for accurate Fluid–Structure Interaction simulations with hourglass control scheme"
date: 2022-07-30 00:00:00 +0100
permalink: an-implicit-sph-based-structure-model-for-accurate-fluid-structure-interaction-simulations-with-hourglass-control-scheme
year: 2022
authors: Yuma Shimizu, Abbas Khayyer, Hitoshi Gotoh
category: articles
tags:
  - Smoothed Particle Hydrodynamics
  - Implicit structure model
  - Hourglass control
  - Fluid–Structure Interaction
---
 
## Authors
[Yuma Shimizu](authors/yuma-shimizu), [Abbas Khayyer](authors/abbas-khayyer), [Hitoshi Gotoh](authors/hitoshi-gotoh)
 
## Abstract
This work is dedicated to development of an implicit SPH (Smoothed Particle Hydrodynamics)-based structure model as well as its integrated purely Lagrangian meshfree hydroelastic FSI (Fluid–Structure Interaction) solver for consistent, accurate and stable modeling of FSI problems. The implicit structure model is established in the context of Hamiltonian mechanics under the assumption of linear elastic solid. Four refined schemes are introduced for improved accuracy, consistency, efficiency and stability: two formerly developed schemes, [i] HT (High-order implicit Time integration) scheme, [ii] HD (High-order Discretization) operator scheme; as well as the novel two schemes newly proposed in this work, namely [iii] IPC (Iterative Predictor–Corrector) calculation procedures to minimize errors related to an imprecise assumption on rotation matrix and [iv] IHC (Implicit Hourglass Control) scheme for stabilizing simulation by suppressing spurious zero-energy modes. An enhanced particle-based FSI solver is formulated within a unified SPH framework by integrating a refined ISPH (Incompressible SPH) fluid model and the proposed implicit structure model, which allows consistent fluid–structure time coupling adopting the equivalent time step sizes in both phases. The proposed implicit structure model and FSI solver are configured in two-dimensions and validated with several 2D structure and FSI benchmark tests showing that our proposed implicit framework could provide almost consistent robustness, accuracy and efficiency with respect to the explicit one.
 
## Keywords
Smoothed Particle Hydrodynamics; Implicit structure model; Hourglass control; Fluid–Structure Interaction
 
## Citation
- **Journal:** European Journal of Mechanics - B/Fluids
- **Year:** 2022
- **Volume:** 96
- **Issue:** 
- **Pages:** 122--145
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.euromechflu.2022.07.007](https://doi.org/10.1016/j.euromechflu.2022.07.007)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Shimizu_2022,
  title={{An implicit SPH-based structure model for accurate Fluid–Structure Interaction simulations with hourglass control scheme}},
  volume={96},
  ISSN={0997-7546},
  DOI={10.1016/j.euromechflu.2022.07.007},
  journal={European Journal of Mechanics - B/Fluids},
  publisher={Elsevier BV},
  author={Shimizu, Yuma and Khayyer, Abbas and Gotoh, Hitoshi},
  year={2022},
  pages={122--145}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/an-implicit-sph-based-structure-model-for-accurate-fluid-structure-interaction-simulations-with-hourglass-control-scheme.bib)
 
## References
- Luo, M., Khayyer, A. & Lin, P. Particle methods in ocean and coastal engineering. Applied Ocean Research vol. 114 102734 (2021) -- [10.1016/j.apor.2021.102734](https://doi.org/10.1016/j.apor.2021.102734)
- Gotoh, H. & Khayyer, A. On the state-of-the-art of particle methods for coastal and ocean engineering. Coastal Engineering Journal vol. 60 79–103 (2018) -- [10.1080/21664250.2018.1436243](https://doi.org/10.1080/21664250.2018.1436243)
- Shimizu, Y., Gotoh, H. & Khayyer, A. An MPS-based particle method for simulation of multiphase flows characterized by high density ratios by incorporation of space potential particle concept. Computers &amp; Mathematics with Applications vol. 76 1108–1129 (2018) -- [10.1016/j.camwa.2018.06.002](https://doi.org/10.1016/j.camwa.2018.06.002)
- Vahabi, M., Hadavandmirzaei, H., Kamkari, B. & Safari, H. Interaction of a pair of in-line bubbles ascending in an Oldroyd-B liquid: A numerical study. European Journal of Mechanics - B/Fluids vol. 85 413–429 (2021) -- [10.1016/j.euromechflu.2020.11.004](https://doi.org/10.1016/j.euromechflu.2020.11.004)
- Tsuruta, N., Gotoh, H., Suzuki, K., Ikari, H. & Shimosako, K. Development of PARISPHERE as the particle-based numerical wave flume for coastal engineering problems. Coastal Engineering Journal vol. 61 41–62 (2019) -- [10.1080/21664250.2018.1560683](https://doi.org/10.1080/21664250.2018.1560683)
- Colagrossi, A., Nikolov, G., Durante, D., Marrone, S. & Souto-Iglesias, A. Viscous flow past a cylinder close to a free surface: Benchmarks with steady, periodic and metastable responses, solved by meshfree and mesh-based schemes. Computers &amp; Fluids vol. 181 345–363 (2019) -- [10.1016/j.compfluid.2019.01.007](https://doi.org/10.1016/j.compfluid.2019.01.007)
- Harada, E., Ikari, H., Khayyer, A. & Gotoh, H. Numerical simulation for swash morphodynamics by DEM–MPS coupling model. Coastal Engineering Journal vol. 61 2–14 (2018) -- [10.1080/21664250.2018.1554203](https://doi.org/10.1080/21664250.2018.1554203)
- Monaghan, J. J. On the integration of the SPH equations for a dusty fluid with high drag. European Journal of Mechanics - B/Fluids vol. 79 454–462 (2020) -- [10.1016/j.euromechflu.2019.10.006](https://doi.org/10.1016/j.euromechflu.2019.10.006)
- Tazaki, T., Harada, E. & Gotoh, H. Vertical sorting process in oscillating water tank using DEM-MPS coupling model. Coastal Engineering vol. 165 103765 (2021) -- [10.1016/j.coastaleng.2020.103765](https://doi.org/10.1016/j.coastaleng.2020.103765)
- Gingold, R. A. & Monaghan, J. J. Smoothed particle hydrodynamics: theory and application to non-spherical stars. Monthly Notices of the Royal Astronomical Society vol. 181 375–389 (1977) -- [10.1093/mnras/181.3.375](https://doi.org/10.1093/mnras/181.3.375)
- Koshizuka, S. & Oka, Y. Moving-Particle Semi-Implicit Method for Fragmentation of Incompressible Fluid. Nuclear Science and Engineering vol. 123 421–434 (1996) -- [10.13182/nse96-a24205](https://doi.org/10.13182/nse96-a24205)
- Hermange, C., Oger, G., Le Chenadec, Y. & Le Touzé, D. A 3D SPH–FE coupling for FSI problems and its application to tire hydroplaning simulations on rough ground. Computer Methods in Applied Mechanics and Engineering vol. 355 558–590 (2019) -- [10.1016/j.cma.2019.06.033](https://doi.org/10.1016/j.cma.2019.06.033)
- Long, T., Huang, C., Hu, D. & Liu, M. Coupling edge-based smoothed finite element method with smoothed particle hydrodynamics for fluid structure interaction problems. Ocean Engineering vol. 225 108772 (2021) -- [10.1016/j.oceaneng.2021.108772](https://doi.org/10.1016/j.oceaneng.2021.108772)
- Zhang, G. et al. A<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" id="d1e1106" altimg="si210.svg"><mml:mi>δ</mml:mi></mml:math>SPH–SPIM coupled method for fluid–structure interaction problems. Journal of Fluids and Structures vol. 101 103210 (2021) -- [10.1016/j.jfluidstructs.2020.103210](https://doi.org/10.1016/j.jfluidstructs.2020.103210)
- Zheng, Z., Duan, G., Mitsume, N., Chen, S. & Yoshimura, S. An explicit MPS/FEM coupling algorithm for three-dimensional fluid-structure interaction analysis. Engineering Analysis with Boundary Elements vol. 121 192–206 (2020) -- [10.1016/j.enganabound.2020.10.002](https://doi.org/10.1016/j.enganabound.2020.10.002)
- Zhang, G., Zhao, W. & Wan, D. Partitioned MPS-FEM method for free-surface flows interacting with deformable structures. Applied Ocean Research vol. 114 102775 (2021) -- [10.1016/j.apor.2021.102775](https://doi.org/10.1016/j.apor.2021.102775)
- Khayyer, A., Gotoh, H., Falahaty, H. & Shimizu, Y. Towards development of enhanced fully-Lagrangian mesh-free computational methods for fluid-structure interaction. Journal of Hydrodynamics vol. 30 49–61 (2018) -- [10.1007/s42241-018-0005-x](https://doi.org/10.1007/s42241-018-0005-x)
- Gotoh, H., Khayyer, A. & Shimizu, Y. Entirely Lagrangian meshfree computational methods for hydroelastic fluid-structure interactions in ocean engineering—Reliability, adaptivity and generality. Applied Ocean Research vol. 115 102822 (2021) -- [10.1016/j.apor.2021.102822](https://doi.org/10.1016/j.apor.2021.102822)
- Amini, Y., Emdad, H. & Farid, M. A new model to solve fluid–hypo-elastic solid interaction using the smoothed particle hydrodynamics (SPH) method. European Journal of Mechanics - B/Fluids vol. 30 184–194 (2011) -- [10.1016/j.euromechflu.2010.09.010](https://doi.org/10.1016/j.euromechflu.2010.09.010)
- Khayyer, A., Tsuruta, N., Shimizu, Y. & Gotoh, H. Multi-resolution MPS for incompressible fluid-elastic structure interactions in ocean engineering. Applied Ocean Research vol. 82 397–414 (2019) -- [10.1016/j.apor.2018.10.020](https://doi.org/10.1016/j.apor.2018.10.020)
- Khayyer, A., Shimizu, Y., Gotoh, H. & Hattori, S. Multi-resolution ISPH-SPH for accurate and efficient simulation of hydroelastic fluid-structure interactions in ocean engineering. Ocean Engineering vol. 226 108652 (2021) -- [10.1016/j.oceaneng.2021.108652](https://doi.org/10.1016/j.oceaneng.2021.108652)
- Sun, P.-N., Le Touzé, D., Oger, G. & Zhang, A.-M. An accurate FSI-SPH modeling of challenging fluid-structure interaction problems in two and three dimensions. Ocean Engineering vol. 221 108552 (2021) -- [10.1016/j.oceaneng.2020.108552](https://doi.org/10.1016/j.oceaneng.2020.108552)
- Zhang, C. et al. SPHinXsys: An open-source multi-physics and multi-resolution library based on smoothed particle hydrodynamics. Computer Physics Communications vol. 267 108066 (2021) -- [10.1016/j.cpc.2021.108066](https://doi.org/10.1016/j.cpc.2021.108066)
- Zhan, L., Peng, C., Zhang, B. & Wu, W. A stabilized TL–WC SPH approach with GPU acceleration for three-dimensional fluid–structure interaction. Journal of Fluids and Structures vol. 86 329–353 (2019) -- [10.1016/j.jfluidstructs.2019.02.002](https://doi.org/10.1016/j.jfluidstructs.2019.02.002)
- O’Connor, J. & Rogers, B. D. A fluid–structure interaction model for free-surface flows and flexible structures using smoothed particle hydrodynamics on a GPU. Journal of Fluids and Structures vol. 104 103312 (2021) -- [10.1016/j.jfluidstructs.2021.103312](https://doi.org/10.1016/j.jfluidstructs.2021.103312)
- Peer, A., Gissler, C., Band, S. & Teschner, M. An Implicit SPH Formulation for Incompressible Linearly Elastic Solids. Computer Graphics Forum vol. 37 135–148 (2017) -- [10.1111/cgf.13317](https://doi.org/10.1111/cgf.13317)
- Ganzenmüller, G. C. An hourglass control algorithm for Lagrangian Smooth Particle Hydrodynamics. Computer Methods in Applied Mechanics and Engineering vol. 286 87–106 (2015) -- [10.1016/j.cma.2014.12.005](https://doi.org/10.1016/j.cma.2014.12.005)
- [Khayyer, A., Shimizu, Y., Gotoh, H. & Nagashima, K. A coupled incompressible SPH-Hamiltonian SPH solver for hydroelastic FSI corresponding to composite structures. Applied Mathematical Modelling vol. 94 242–271 (2021)](a-coupled-incompressible-sph-hamiltonian-sph-solver-for-hydroelastic-fsi-corresponding-to-composite-structures) -- [10.1016/j.apm.2021.01.011](https://doi.org/10.1016/j.apm.2021.01.011)
- Shao, S. & Lo, E. Y. M. Incompressible SPH method for simulating Newtonian and non-Newtonian flows with a free surface. Advances in Water Resources vol. 26 787–800 (2003) -- [10.1016/s0309-1708(03)00030-7](https://doi.org/10.1016/s0309-1708(03)00030-7)
- Shimizu, Y., Khayyer, A. & Gotoh, H. An SPH-based fully-Lagrangian meshfree implicit FSI solver with high-order discretization terms. Engineering Analysis with Boundary Elements vol. 137 160–181 (2022) -- [10.1016/j.enganabound.2021.10.023](https://doi.org/10.1016/j.enganabound.2021.10.023)
- Chorin, A. J. Numerical solution of the Navier-Stokes equations. Mathematics of Computation vol. 22 745–762 (1968) -- [10.1090/s0025-5718-1968-0242392-2](https://doi.org/10.1090/s0025-5718-1968-0242392-2)
- Wendland, H. Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree. Advances in Computational Mathematics vol. 4 389–396 (1995) -- [10.1007/bf02123482](https://doi.org/10.1007/bf02123482)
- Gotoh, H. & Khayyer, A. Current achievements and future perspectives for projection-based particle methods with applications in ocean engineering. Journal of Ocean Engineering and Marine Energy vol. 2 251–278 (2016) -- [10.1007/s40722-016-0049-3](https://doi.org/10.1007/s40722-016-0049-3)
- Khayyer, A., Gotoh, H., Shimizu, Y. & Gotoh, K. On enhancement of energy conservation properties of projection-based particle methods. European Journal of Mechanics - B/Fluids vol. 66 20–37 (2017) -- [10.1016/j.euromechflu.2017.01.014](https://doi.org/10.1016/j.euromechflu.2017.01.014)
- Khayyer, A. & Gotoh, H. Modified Moving Particle Semi-implicit methods for the prediction of 2D wave impact pressure. Coastal Engineering vol. 56 419–440 (2009) -- [10.1016/j.coastaleng.2008.10.004](https://doi.org/10.1016/j.coastaleng.2008.10.004)
- Khayyer, A. & Gotoh, H. A higher order Laplacian model for enhancement and stabilization of pressure calculation by the MPS method. Applied Ocean Research vol. 32 124–131 (2010) -- [10.1016/j.apor.2010.01.001](https://doi.org/10.1016/j.apor.2010.01.001)
- Khayyer, A. & Gotoh, H. Enhancement of stability and accuracy of the moving particle semi-implicit method. Journal of Computational Physics vol. 230 3093–3118 (2011) -- [10.1016/j.jcp.2011.01.009](https://doi.org/10.1016/j.jcp.2011.01.009)
- Tsuruta, N., Khayyer, A. & Gotoh, H. A short note on Dynamic Stabilization of Moving Particle Semi-implicit method. Computers &amp; Fluids vol. 82 158–164 (2013) -- [10.1016/j.compfluid.2013.05.001](https://doi.org/10.1016/j.compfluid.2013.05.001)
- Khayyer, A. et al. Development of a projection-based SPH method for numerical wave flume with porous media of variable porosity. Coastal Engineering vol. 140 1–22 (2018) -- [10.1016/j.coastaleng.2018.05.003](https://doi.org/10.1016/j.coastaleng.2018.05.003)
- Shimizu, Y., Khayyer, A., Gotoh, H. & Nagashima, K. An enhanced multiphase ISPH-based method for accurate modeling of oil spill. Coastal Engineering Journal vol. 62 625–646 (2020) -- [10.1080/21664250.2020.1815362](https://doi.org/10.1080/21664250.2020.1815362)
- Ikari, H., Yamano, T. & Gotoh, H. Multiphase particle method using an elastoplastic solid phase model for the diffusion of dumped sand from a split hopper. Computers &amp; Fluids vol. 208 104639 (2020) -- [10.1016/j.compfluid.2020.104639](https://doi.org/10.1016/j.compfluid.2020.104639)
- Suzuki, Y. & Koshizuka, S. A Hamiltonian particle method for non‐linear elastodynamics. International Journal for Numerical Methods in Engineering vol. 74 1344–1373 (2007) -- [10.1002/nme.2222](https://doi.org/10.1002/nme.2222)
- Gotoh, (2018)
- Khayyer, A., Gotoh, H., Shimizu, Y. & Nishijima, Y. A 3D Lagrangian meshfree projection-based solver for hydroelastic Fluid–Structure​ Interactions. Journal of Fluids and Structures vol. 105 103342 (2021) -- [10.1016/j.jfluidstructs.2021.103342](https://doi.org/10.1016/j.jfluidstructs.2021.103342)
- Becker, Corotated SPH for deformable solids. (2009)
- Sifakis, FEM simulation of 3D deformable solids: a practitioner’s guide to theory, discretization and model reduction. (2012)
- Müller, M., Heidelberger, B., Teschner, M. & Gross, M. Meshless deformations based on shape matching. ACM Transactions on Graphics vol. 24 471–478 (2005) -- [10.1145/1073204.1073216](https://doi.org/10.1145/1073204.1073216)
- Khayyer, A., Gotoh, H., Falahaty, H. & Shimizu, Y. An enhanced ISPH–SPH coupled method for simulation of incompressible fluid–elastic structure interactions. Computer Physics Communications vol. 232 139–164 (2018) -- [10.1016/j.cpc.2018.05.012](https://doi.org/10.1016/j.cpc.2018.05.012)
- Antoci, C., Gallati, M. & Sibilla, S. Numerical simulation of fluid–structure interaction by SPH. Computers &amp; Structures vol. 85 879–890 (2007) -- [10.1016/j.compstruc.2007.01.002](https://doi.org/10.1016/j.compstruc.2007.01.002)
- Shimizu, Y. & Gotoh, H. Toward Enhancement of MPS Method for Ocean Engineering: Effect of Time-Integration Schemes. International Journal of Offshore and Polar Engineering vol. 26 378–384 (2016) -- [10.17736/ijope.2016.mk46](https://doi.org/10.17736/ijope.2016.mk46)
- Vignjevic, R., Campbell, J. & Libersky, L. A treatment of zero-energy modes in the smoothed particle hydrodynamics method. Computer Methods in Applied Mechanics and Engineering vol. 184 67–85 (2000) -- [10.1016/s0045-7825(99)00441-7](https://doi.org/10.1016/s0045-7825(99)00441-7)
- Xiao, S. P. & Belytschko, T. Material stability analysis of particle methods. Advances in Computational Mathematics vol. 23 171–190 (2005) -- [10.1007/s10444-004-1817-5](https://doi.org/10.1007/s10444-004-1817-5)
- Randles, P. W. & Libersky, L. D. Normalized SPH with stress points. International Journal for Numerical Methods in Engineering vol. 48 1445–1462 (2000) -- [10.1002/1097-0207(20000810)48:10<1445::aid-nme831>3.0.co;2-9](https://doi.org/10.1002/1097-0207(20000810)48:10<1445::aid-nme831>3.0.co;2-9)
- Kondo, M., Suzuki, Y. & Koshizuka, S. Suppressing local particle oscillations in the Hamiltonian particle method for elasticity. International Journal for Numerical Methods in Engineering vol. 81 1514–1528 (2009) -- [10.1002/nme.2744](https://doi.org/10.1002/nme.2744)
- Duan, G., Yamaji, A., Koshizuka, S. & Chen, B. The truncation and stabilization error in multiphase moving particle semi-implicit method based on corrective matrix: Which is dominant? Computers &amp; Fluids vol. 190 254–273 (2019) -- [10.1016/j.compfluid.2019.06.023](https://doi.org/10.1016/j.compfluid.2019.06.023)
- Gray, J. P., Monaghan, J. J. & Swift, R. P. SPH elastic dynamics. Computer Methods in Applied Mechanics and Engineering vol. 190 6641–6662 (2001) -- [10.1016/s0045-7825(01)00254-7](https://doi.org/10.1016/s0045-7825(01)00254-7)
- Fourey, G., Hermange, C., Le Touzé, D. & Oger, G. An efficient FSI coupling strategy between Smoothed Particle Hydrodynamics and Finite Element methods. Computer Physics Communications vol. 217 66–81 (2017) -- [10.1016/j.cpc.2017.04.005](https://doi.org/10.1016/j.cpc.2017.04.005)
- Scolan, Y.-M. Hydroelastic behaviour of a conical shell impacting on a quiescent-free surface of an incompressible liquid. Journal of Sound and Vibration vol. 277 163–203 (2004) -- [10.1016/j.jsv.2003.08.051](https://doi.org/10.1016/j.jsv.2003.08.051)
- Idelsohn, S. R., Marti, J., Souto-Iglesias, A. & Oñate, E. Interaction between an elastic structure and free-surface flows: experimental versus numerical comparisons using the PFEM. Computational Mechanics vol. 43 125–132 (2008) -- [10.1007/s00466-008-0245-7](https://doi.org/10.1007/s00466-008-0245-7)
- Landau, (1970)
- Timoshenko, (1959)
- Lind, S. J., Xu, R., Stansby, P. K. & Rogers, B. D. Incompressible smoothed particle hydrodynamics for free-surface flows: A generalised diffusion-based algorithm for stability and validations for impulsive flows and propagating waves. Journal of Computational Physics vol. 231 1499–1523 (2012) -- [10.1016/j.jcp.2011.10.027](https://doi.org/10.1016/j.jcp.2011.10.027)
- Khayyer, A., Gotoh, H. & Shimizu, Y. A projection-based particle method with optimized particle shifting for multiphase flows with large density ratios and discontinuous density fields. Computers &amp; Fluids vol. 179 356–371 (2019) -- [10.1016/j.compfluid.2018.10.018](https://doi.org/10.1016/j.compfluid.2018.10.018)
- Luo, M. et al. Consistent Particle Method simulation of solitary wave impinging on and overtopping a seawall. Engineering Analysis with Boundary Elements vol. 103 160–171 (2019) -- [10.1016/j.enganabound.2019.03.012](https://doi.org/10.1016/j.enganabound.2019.03.012)
- Sun, P. N., Le Touzé, D. & Zhang, A.-M. Study of a complex fluid-structure dam-breaking benchmark problem using a multi-phase SPH method with APR. Engineering Analysis with Boundary Elements vol. 104 240–258 (2019) -- [10.1016/j.enganabound.2019.03.033](https://doi.org/10.1016/j.enganabound.2019.03.033)
- Rafiee, A., Dutykh, D. & Dias, F. Numerical Simulation of Wave Impact on a Rigid Wall Using a Two–phase Compressible SPH Method. Procedia IUTAM vol. 18 123–137 (2015) -- [10.1016/j.piutam.2015.11.013](https://doi.org/10.1016/j.piutam.2015.11.013)
- Fonty, T., Ferrand, M., Leroy, A. & Violeau, D. Air Entrainment Modeling in the SPH Method: A Two-Phase Mixture Formulation with Open Boundaries. Flow, Turbulence and Combustion vol. 105 1149–1195 (2020) -- [10.1007/s10494-020-00165-7](https://doi.org/10.1007/s10494-020-00165-7)
- Vignjevic, R., DeVuyst, T. & Campbell, J. The nonlocal, local and mixed forms of the SPH method. Computer Methods in Applied Mechanics and Engineering vol. 387 114164 (2021) -- [10.1016/j.cma.2021.114164](https://doi.org/10.1016/j.cma.2021.114164)
- Hwang, S.-C., Park, J.-C., Gotoh, H., Khayyer, A. & Kang, K.-J. Numerical simulations of sloshing flows with elastic baffles by using a particle-based fluid–structure interaction analysis method. Ocean Engineering vol. 118 227–241 (2016) -- [10.1016/j.oceaneng.2016.04.006](https://doi.org/10.1016/j.oceaneng.2016.04.006)

