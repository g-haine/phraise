---
layout: post
title: "A 3D SPH-based entirely Lagrangian meshfree hydroelastic FSI solver for anisotropic composite structures"
date: 2022-08-04 00:00:00 +0100
permalink: a-3d-sph-based-entirely-lagrangian-meshfree-hydroelastic-fsi-solver-for-anisotropic-composite-structures
year: 2022
authors: Abbas Khayyer, Yuma Shimizu, Hitoshi Gotoh, Shunsuke Hattori
category: journal-article
tag: Hydroelastic fluid-structure interaction; Incompressible sph; Hamiltonian sph; Anisotropic materials; Composite structures; Three-dimensional simulations
---
 
## Authors
[Abbas Khayyer](authors/abbas-khayyer), [Yuma Shimizu](authors/yuma-shimizu), [Hitoshi Gotoh](authors/hitoshi-gotoh), [Shunsuke Hattori](authors/shunsuke-hattori)
 
## Abstract
This paper presents the first 3D entirely Lagrangian meshfree hydroelastic FSI (Fluid-Structure Interaction) solver for reproduction of incompressible fluid flows interacting with anisotropic/isotropic composite elastic structures as well as the first Hamiltonian SPH for anisotropic structures. To achieve this development, we have carefully (i) reformulated the HSPH (Hamiltonian Smoothed Particle Hydrodynamics) isotropic structure model with consideration of material anisotropy of structures, (ii) extended the 2D HSPH structure model and corresponding ISPH-HSPH FSI solver for 3D composite structures and their interactions with incompressible fluids. Regarding the advancement (i), the reformulation from isotropic to anisotropic structure model has been conducted through a careful revisit on the basis of stress-strain responses. The fourth-order elasticity tensor and transformation (rotation) of coordinate systems are considered for development of the anisotropic HSPH structure model. Then, the 3D HSPH structure model for anisotropic/composite structures is coupled with a refined projection-based Incompressible SPH (ISPH) fluid model. The proposed structure model and FSI solver are capable of handling large material anisotropies and discontinuities at material interfaces without use of any artificial stabilizers/smoothing schemes. Validations are conducted coherently. First, the newly proposed anisotropic HSPH structure model is verified through both 2D/3D classical benchmark tests with exact theoretical solutions. Then, followed by validations of HSPH for 3D composites, the corresponding coupled ISPH-HSPH FSI solver is applied to two hydroelastic FSI tests including slamming of an anisotropic composite hull.
 
## Keywords
Hydroelastic fluid-structure interaction; Incompressible sph; Hamiltonian sph; Anisotropic materials; Composite structures; Three-dimensional simulations
 
## Citation
- **Journal:** Applied Mathematical Modelling
- **Year:** 2022
- **Volume:** 112
- **Issue:** 
- **Pages:** 560--613
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.apm.2022.07.031](https://doi.org/10.1016/j.apm.2022.07.031)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Khayyer_2022,
  title={{A 3D SPH-based entirely Lagrangian meshfree hydroelastic FSI solver for anisotropic composite structures}},
  volume={112},
  ISSN={0307-904X},
  DOI={10.1016/j.apm.2022.07.031},
  journal={Applied Mathematical Modelling},
  publisher={Elsevier BV},
  author={Khayyer, Abbas and Shimizu, Yuma and Gotoh, Hitoshi and Hattori, Shunsuke},
  year={2022},
  pages={560--613}
}
{% endraw %}
{% endhighlight %}
 
## References
- Rajak, D. K., Pagar, D. D., Kumar, R. & Pruncu, C. I. Recent progress of reinforcement materials: a comprehensive overview of composite materials. Journal of Materials Research and Technology vol. 8 6354–6374 (2019) -- [10.1016/j.jmrt.2019.09.068](https://doi.org/10.1016/j.jmrt.2019.09.068)
- Butler, R. et al. High-performance dune modules for solving large-scale, strongly anisotropic elliptic problems with applications to aerospace composites. Computer Physics Communications vol. 249 106997 (2020) -- [10.1016/j.cpc.2019.106997](https://doi.org/10.1016/j.cpc.2019.106997)
- Shafei, E., Faroughi, S. & Reali, A. Geometrically nonlinear vibration of anisotropic composite beams using isogeometric third-order shear deformation theory. Composite Structures vol. 252 112627 (2020) -- [10.1016/j.compstruct.2020.112627](https://doi.org/10.1016/j.compstruct.2020.112627)
- Kim, D. et al. Topology optimization of functionally graded anisotropic composite structures using homogenization design method. Computer Methods in Applied Mechanics and Engineering vol. 369 113220 (2020) -- [10.1016/j.cma.2020.113220](https://doi.org/10.1016/j.cma.2020.113220)
- Schwartzentruber, J., Spelt, J. K. & Papini, M. Modelling of delamination due to hydraulic shock when piercing anisotropic carbon-fiber laminates using an abrasive waterjet. International Journal of Machine Tools and Manufacture vol. 132 81–95 (2018) -- [10.1016/j.ijmachtools.2018.05.001](https://doi.org/10.1016/j.ijmachtools.2018.05.001)
- Lezgy-Nazargah, M., Shariyat, M. & Beheshti-Aval, S. B. A refined high-order global-local theory for finite element bending and vibration analyses of laminated composite beams. Acta Mechanica vol. 217 219–242 (2010) -- [10.1007/s00707-010-0391-9](https://doi.org/10.1007/s00707-010-0391-9)
- Khdeir, A. A. & Aldraihem, O. J. Free vibration of sandwich beams with soft core. Composite Structures vol. 154 179–189 (2016) -- [10.1016/j.compstruct.2016.07.045](https://doi.org/10.1016/j.compstruct.2016.07.045)
- Khandelwal, R. P., Chakrabarti, A. & Bhargava, P. An efficient FE model based on combined theory for the analysis of soft core sandwich plate. Computational Mechanics vol. 51 673–697 (2012) -- [10.1007/s00466-012-0745-3](https://doi.org/10.1007/s00466-012-0745-3)
- Mouritz, A. P., Gellert, E., Burchill, P. & Challis, K. Review of advanced composite structures for naval ships and submarines. Composite Structures vol. 53 21–42 (2001) -- [10.1016/S0263-8223(00)00175-6](https://doi.org/10.1016/S0263-8223(00)00175-6)
- Gotoh, H. & Khayyer, A. On the state-of-the-art of particle methods for coastal and ocean engineering. Coastal Engineering Journal vol. 60 79–103 (2018) -- [10.1080/21664250.2018.1436243](https://doi.org/10.1080/21664250.2018.1436243)
- Gotoh, H. & Khayyer, A. Current achievements and future perspectives for projection-based particle methods with applications in ocean engineering. Journal of Ocean Engineering and Marine Energy vol. 2 251–278 (2016) -- [10.1007/s40722-016-0049-3](https://doi.org/10.1007/s40722-016-0049-3)
- Joubert, J. C. et al. 3D gradient corrected SPH for fully resolved particle–fluid interactions. Applied Mathematical Modelling vol. 78 816–840 (2020) -- [10.1016/j.apm.2019.09.030](https://doi.org/10.1016/j.apm.2019.09.030)
- Tang, Y., Chen, S. & Jiang, Q. A conservative SPH scheme using exact projection with semi-analytical boundary method for free-surface flows. Applied Mathematical Modelling vol. 82 607–635 (2020) -- [10.1016/j.apm.2020.01.073](https://doi.org/10.1016/j.apm.2020.01.073)
- Xue, T., Zhang, X. & Tamma, K. K. A non-local heat transport model in solids with discontinuities via Lagrangian particle method. Applied Mathematical Modelling vol. 88 208–223 (2020) -- [10.1016/j.apm.2020.06.058](https://doi.org/10.1016/j.apm.2020.06.058)
- Tsurudome, C., Liang, D., Shimizu, Y., Khayyer, A. & Gotoh, H. Incompressible SPH simulation of solitary wave propagation on permeable beaches. Journal of Hydrodynamics vol. 32 664–671 (2020) -- [10.1007/s42241-020-0042-0](https://doi.org/10.1007/s42241-020-0042-0)
- Serroukh, H. K., Mabssout, M. & Herreros, M. I. Updated Lagrangian Taylor-SPH method for large deformation in dynamic problems. Applied Mathematical Modelling vol. 80 238–256 (2020) -- [10.1016/j.apm.2019.11.046](https://doi.org/10.1016/j.apm.2019.11.046)
- Tsuruta, N., Gotoh, H., Suzuki, K., Ikari, H. & Shimosako, K. Development of PARISPHERE as the particle-based numerical wave flume for coastal engineering problems. Coastal Engineering Journal vol. 61 41–62 (2019) -- [10.1080/21664250.2018.1560683](https://doi.org/10.1080/21664250.2018.1560683)
- Harada, E., Ikari, H., Khayyer, A. & Gotoh, H. Numerical simulation for swash morphodynamics by DEM–MPS coupling model. Coastal Engineering Journal vol. 61 2–14 (2018) -- [10.1080/21664250.2018.1554203](https://doi.org/10.1080/21664250.2018.1554203)
- Tazaki, T., Harada, E. & Gotoh, H. Vertical sorting process in oscillating water tank using DEM-MPS coupling model. Coastal Engineering vol. 165 103765 (2021) -- [10.1016/j.coastaleng.2020.103765](https://doi.org/10.1016/j.coastaleng.2020.103765)
- Fourey, G., Hermange, C., Le Touzé, D. & Oger, G. An efficient FSI coupling strategy between Smoothed Particle Hydrodynamics and Finite Element methods. Computer Physics Communications vol. 217 66–81 (2017) -- [10.1016/j.cpc.2017.04.005](https://doi.org/10.1016/j.cpc.2017.04.005)
- Zheng, Z., Duan, G., Mitsume, N., Chen, S. & Yoshimura, S. An explicit MPS/FEM coupling algorithm for three-dimensional fluid-structure interaction analysis. Engineering Analysis with Boundary Elements vol. 121 192–206 (2020) -- [10.1016/j.enganabound.2020.10.002](https://doi.org/10.1016/j.enganabound.2020.10.002)
- Long, T., Huang, C., Hu, D. & Liu, M. Coupling edge-based smoothed finite element method with smoothed particle hydrodynamics for fluid structure interaction problems. Ocean Engineering vol. 225 108772 (2021) -- [10.1016/j.oceaneng.2021.108772](https://doi.org/10.1016/j.oceaneng.2021.108772)
- Khayyer, A., Gotoh, H., Falahaty, H. & Shimizu, Y. Towards development of enhanced fully-Lagrangian mesh-free computational methods for fluid-structure interaction. Journal of Hydrodynamics vol. 30 49–61 (2018) -- [10.1007/s42241-018-0005-x](https://doi.org/10.1007/s42241-018-0005-x)
- Sun, P.-N., Le Touzé, D., Oger, G. & Zhang, A.-M. An accurate FSI-SPH modeling of challenging fluid-structure interaction problems in two and three dimensions. Ocean Engineering vol. 221 108552 (2021) -- [10.1016/j.oceaneng.2020.108552](https://doi.org/10.1016/j.oceaneng.2020.108552)
- Zhang, C. et al. SPHinXsys: An open-source meshless, multi-resolution and multi-physics library. Software Impacts vol. 6 100033 (2020) -- [10.1016/j.simpa.2020.100033](https://doi.org/10.1016/j.simpa.2020.100033)
- Khayyer, A., Tsuruta, N., Shimizu, Y. & Gotoh, H. Multi-resolution MPS for incompressible fluid-elastic structure interactions in ocean engineering. Applied Ocean Research vol. 82 397–414 (2019) -- [10.1016/j.apor.2018.10.020](https://doi.org/10.1016/j.apor.2018.10.020)
- Zhang, C. et al. SPHinXsys: An open-source multi-physics and multi-resolution library based on smoothed particle hydrodynamics. Computer Physics Communications vol. 267 108066 (2021) -- [10.1016/j.cpc.2021.108066](https://doi.org/10.1016/j.cpc.2021.108066)
- [Khayyer, A., Shimizu, Y., Gotoh, H. & Nagashima, K. A coupled incompressible SPH-Hamiltonian SPH solver for hydroelastic FSI corresponding to composite structures. Applied Mathematical Modelling vol. 94 242–271 (2021)](a-coupled-incompressible-sph-hamiltonian-sph-solver-for-hydroelastic-fsi-corresponding-to-composite-structures) -- [10.1016/j.apm.2021.01.011](https://doi.org/10.1016/j.apm.2021.01.011)
- Gingold, R. A. & Monaghan, J. J. Smoothed particle hydrodynamics: theory and application to non-spherical stars. Monthly Notices of the Royal Astronomical Society vol. 181 375–389 (1977) -- [10.1093/mnras/181.3.375](https://doi.org/10.1093/mnras/181.3.375)
- Qin, Z. & Batra, R. C. Local slamming impact of sandwich composite hulls. International Journal of Solids and Structures vol. 46 2011–2035 (2009) -- [10.1016/j.ijsolstr.2008.04.019](https://doi.org/10.1016/j.ijsolstr.2008.04.019)
- Das, K. & Batra, R. C. Local water slamming impact on sandwich composite hulls. Journal of Fluids and Structures vol. 27 523–551 (2011) -- [10.1016/j.jfluidstructs.2011.02.001](https://doi.org/10.1016/j.jfluidstructs.2011.02.001)
- Li, Z. et al. Experimental and numerical study of basalt fiber reinforced polymer strip strengthened autoclaved aerated concrete masonry walls under vented gas explosions. Engineering Structures vol. 152 901–919 (2017) -- [10.1016/j.engstruct.2017.09.055](https://doi.org/10.1016/j.engstruct.2017.09.055)
- Chiquito, M., Castedo, R., Santos, A. P., López, L. M. & Pérez-Caldentey, A. Numerical modelling and experimental validation of the behaviour of brick masonry walls subjected to blast loading. International Journal of Impact Engineering vol. 148 103760 (2021) -- [10.1016/j.ijimpeng.2020.103760](https://doi.org/10.1016/j.ijimpeng.2020.103760)
- Valencia, A. & Baeza, F. Numerical simulation of fluid–structure interaction in stenotic arteries considering two layer nonlinear anisotropic structural model. International Communications in Heat and Mass Transfer vol. 36 137–142 (2009) -- [10.1016/j.icheatmasstransfer.2008.10.006](https://doi.org/10.1016/j.icheatmasstransfer.2008.10.006)
- Wu, M. C. H. et al. An anisotropic constitutive model for immersogeometric fluid–structure interaction analysis of bioprosthetic heart valves. Journal of Biomechanics vol. 74 23–31 (2018) -- [10.1016/j.jbiomech.2018.04.012](https://doi.org/10.1016/j.jbiomech.2018.04.012)
- Liao, Y., Martins, J. R. R. A. & Young, Y. L. Sweep and anisotropy effects on the viscous hydroelastic response of composite hydrofoils. Composite Structures vol. 230 111471 (2019) -- [10.1016/j.compstruct.2019.111471](https://doi.org/10.1016/j.compstruct.2019.111471)
- Akcabay, D. T. & Young, Y. L. Material anisotropy and sweep effects on the hydroelastic response of lifting surfaces. Composite Structures vol. 242 112140 (2020) -- [10.1016/j.compstruct.2020.112140](https://doi.org/10.1016/j.compstruct.2020.112140)
- Liu, K. & Liu, W. Application of Discrete Element Method for Continuum Dynamic Problems. Archive of Applied Mechanics vol. 76 229–243 (2006) -- [10.1007/s00419-006-0018-8](https://doi.org/10.1007/s00419-006-0018-8)
- Owen, B. et al. Vector-based discrete element method for solid elastic materials. Computer Physics Communications vol. 254 107353 (2020) -- [10.1016/j.cpc.2020.107353](https://doi.org/10.1016/j.cpc.2020.107353)
- Chorin, A. J. Numerical solution of the Navier-Stokes equations. Mathematics of Computation vol. 22 745–762 (1968) -- [10.1090/S0025-5718-1968-0242392-2](https://doi.org/10.1090/S0025-5718-1968-0242392-2)
- Wendland, H. Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree. Advances in Computational Mathematics vol. 4 389–396 (1995) -- [10.1007/BF02123482](https://doi.org/10.1007/BF02123482)
- Khayyer, A. & Gotoh, H. Modified Moving Particle Semi-implicit methods for the prediction of 2D wave impact pressure. Coastal Engineering vol. 56 419–440 (2009) -- [10.1016/j.coastaleng.2008.10.004](https://doi.org/10.1016/j.coastaleng.2008.10.004)
- Khayyer, A. & Gotoh, H. A higher order Laplacian model for enhancement and stabilization of pressure calculation by the MPS method. Applied Ocean Research vol. 32 124–131 (2010) -- [10.1016/j.apor.2010.01.001](https://doi.org/10.1016/j.apor.2010.01.001)
- Khayyer, A. & Gotoh, H. Enhancement of stability and accuracy of the moving particle semi-implicit method. Journal of Computational Physics vol. 230 3093–3118 (2011) -- [10.1016/j.jcp.2011.01.009](https://doi.org/10.1016/j.jcp.2011.01.009)
- Tsuruta, N., Khayyer, A. & Gotoh, H. A short note on Dynamic Stabilization of Moving Particle Semi-implicit method. Computers &amp; Fluids vol. 82 158–164 (2013) -- [10.1016/j.compfluid.2013.05.001](https://doi.org/10.1016/j.compfluid.2013.05.001)
- Khayyer, A. et al. Development of a projection-based SPH method for numerical wave flume with porous media of variable porosity. Coastal Engineering vol. 140 1–22 (2018) -- [10.1016/j.coastaleng.2018.05.003](https://doi.org/10.1016/j.coastaleng.2018.05.003)
- Khayyer, A., Gotoh, H., Shimizu, Y. & Gotoh, K. On enhancement of energy conservation properties of projection-based particle methods. European Journal of Mechanics - B/Fluids vol. 66 20–37 (2017) -- [10.1016/j.euromechflu.2017.01.014](https://doi.org/10.1016/j.euromechflu.2017.01.014)
- Shimizu, Y., Gotoh, H. & Khayyer, A. An MPS-based particle method for simulation of multiphase flows characterized by high density ratios by incorporation of space potential particle concept. Computers &amp; Mathematics with Applications vol. 76 1108–1129 (2018) -- [10.1016/j.camwa.2018.06.002](https://doi.org/10.1016/j.camwa.2018.06.002)
- Shimizu, Y., Khayyer, A., Gotoh, H. & Nagashima, K. An enhanced multiphase ISPH-based method for accurate modeling of oil spill. Coastal Engineering Journal vol. 62 625–646 (2020) -- [10.1080/21664250.2020.1815362](https://doi.org/10.1080/21664250.2020.1815362)
- Khayyer, A., Gotoh, H., Falahaty, H. & Shimizu, Y. An enhanced ISPH–SPH coupled method for simulation of incompressible fluid–elastic structure interactions. Computer Physics Communications vol. 232 139–164 (2018) -- [10.1016/j.cpc.2018.05.012](https://doi.org/10.1016/j.cpc.2018.05.012)
- Antoci, C., Gallati, M. & Sibilla, S. Numerical simulation of fluid–structure interaction by SPH. Computers &amp; Structures vol. 85 879–890 (2007) -- [10.1016/j.compstruc.2007.01.002](https://doi.org/10.1016/j.compstruc.2007.01.002)
- SUGIMOTO, F., KAWABE, K., YAMASHITA, S. & HONGO, K. A Method for Estimating Directions of Elastic Principal Axes and Coefficients of Compliance in Orthotropic Rock. Shigen-to-Sozai vol. 111 289–294 (1995) -- [10.2473/shigentosozai.111.289](https://doi.org/10.2473/shigentosozai.111.289)
- Fatehi, R. & Manzari, M. T. Error estimation in smoothed particle hydrodynamics and a new scheme for second derivatives. Computers &amp; Mathematics with Applications vol. 61 482–498 (2011) -- [10.1016/j.camwa.2010.11.028](https://doi.org/10.1016/j.camwa.2010.11.028)
- Duan, G., Yamaji, A., Koshizuka, S. & Chen, B. The truncation and stabilization error in multiphase moving particle semi-implicit method based on corrective matrix: Which is dominant? Computers &amp; Fluids vol. 190 254–273 (2019) -- [10.1016/j.compfluid.2019.06.023](https://doi.org/10.1016/j.compfluid.2019.06.023)
- Batra, R. C. & Zhang, G. M. Analysis of adiabatic shear bands in elasto-thermo-viscoplastic materials by modified smoothed-particle hydrodynamics (MSPH) method. Journal of Computational Physics vol. 201 172–190 (2004) -- [10.1016/j.jcp.2004.05.007](https://doi.org/10.1016/j.jcp.2004.05.007)
- Nasar, A. M. A. et al. High-order consistent SPH with the pressure projection method in 2-D and 3-D. Journal of Computational Physics vol. 444 110563 (2021) -- [10.1016/j.jcp.2021.110563](https://doi.org/10.1016/j.jcp.2021.110563)
- Sibilla, S. An algorithm to improve consistency in Smoothed Particle Hydrodynamics. Computers &amp; Fluids vol. 118 148–158 (2015) -- [10.1016/j.compfluid.2015.06.012](https://doi.org/10.1016/j.compfluid.2015.06.012)
- Nasar, A. M. A. et al. High-order velocity and pressure wall boundary conditions in Eulerian incompressible SPH. Journal of Computational Physics vol. 434 109793 (2021) -- [10.1016/j.jcp.2020.109793](https://doi.org/10.1016/j.jcp.2020.109793)
- Duan, G., Matsunaga, T., Yamaji, A., Koshizuka, S. & Sakai, M. Imposing accurate wall boundary conditions in corrective‐matrix‐based moving particle semi‐implicit method for free surface flow. International Journal for Numerical Methods in Fluids vol. 93 148–175 (2020) -- [10.1002/fld.4878](https://doi.org/10.1002/fld.4878)
- Sladek, J., Sladek, V. & Zhang, Ch. Stress analysis in anisotropic functionally graded materials by the MLPG method. Engineering Analysis with Boundary Elements vol. 29 597–609 (2005) -- [10.1016/j.enganabound.2005.01.011](https://doi.org/10.1016/j.enganabound.2005.01.011)
- ZHANG, J. J., TAN, C. L. & AFAGH, F. F. TREATMENT OF BODY-FORCE VOLUME INTEGRALS IN BEM BY EXACT TRANSFORMATION FOR 2-D ANISOTROPIC ELASTICITY. International Journal for Numerical Methods in Engineering vol. 40 89–109 (1997) -- [10.1002/(SICI)1097-0207(19970115)40:1<89::AID-NME53>3.0.CO;2-3](https://doi.org/10.1002/(SICI)1097-0207(19970115)40:1<89::AID-NME53>3.0.CO;2-3)
- Peng, X.-L. & Li, X.-F. Elastic analysis of rotating functionally graded polar orthotropic disks. International Journal of Mechanical Sciences vol. 60 84–91 (2012) -- [10.1016/j.ijmecsci.2012.04.014](https://doi.org/10.1016/j.ijmecsci.2012.04.014)
- Schclar, N. A. & Partridge, P. W. 3D anisotropic elasticity with BEM using the isotropic fundamental solution. Engineering Analysis with Boundary Elements vol. 11 137–144 (1993) -- [10.1016/0955-7997(93)90033-H](https://doi.org/10.1016/0955-7997(93)90033-H)
- Ogasawara, T., Ayabe, S., Ishida, Y., Aoki, T. & Kubota, Y. Heat-resistant sandwich structure with carbon fiber-polyimide composite faces and a carbon foam core. Composites Part A: Applied Science and Manufacturing vol. 114 352–359 (2018) -- [10.1016/j.compositesa.2018.08.030](https://doi.org/10.1016/j.compositesa.2018.08.030)
- Fukuda, H., Itohiya, G., Kataoka, A. & Tashiro, S. Evaluation of Bending Rigidity of CFRP Skin-Foamed Core Sandwich Beams. Journal of Sandwich Structures &amp; Materials vol. 6 75–92 (2004) -- [10.1177/1099636204030054](https://doi.org/10.1177/1099636204030054)
- Gray, J. P., Monaghan, J. J. & Swift, R. P. SPH elastic dynamics. Computer Methods in Applied Mechanics and Engineering vol. 190 6641–6662 (2001) -- [10.1016/S0045-7825(01)00254-7](https://doi.org/10.1016/S0045-7825(01)00254-7)
- Barut, A., Madenci, E., Heinrich, J. & Tessler, A. Analysis of thick sandwich construction by a {3,2}-order theory. International Journal of Solids and Structures vol. 38 6063–6077 (2001) -- [10.1016/S0020-7683(00)00367-X](https://doi.org/10.1016/S0020-7683(00)00367-X)
- SCOLAN, Y.-M. & KOROBKIN, A. A. Three-dimensional theory of water impact. Part 1. Inverse Wagner problem. Journal of Fluid Mechanics vol. 440 293–326 (2001) -- [10.1017/S002211200100475X](https://doi.org/10.1017/S002211200100475X)
- Hohe, J. & Librescu, L. A nonlinear theory for doubly curved anisotropic sandwich shells with transversely compressible core. International Journal of Solids and Structures vol. 40 1059–1088 (2003) -- [10.1016/S0020-7683(02)00656-X](https://doi.org/10.1016/S0020-7683(02)00656-X)
- Khayyer, A., Shimizu, Y., Gotoh, H. & Hattori, S. Multi-resolution ISPH-SPH for accurate and efficient simulation of hydroelastic fluid-structure interactions in ocean engineering. Ocean Engineering vol. 226 108652 (2021) -- [10.1016/j.oceaneng.2021.108652](https://doi.org/10.1016/j.oceaneng.2021.108652)
- Shimizu, Y., Khayyer, A. & Gotoh, H. An SPH-based fully-Lagrangian meshfree implicit FSI solver with high-order discretization terms. Engineering Analysis with Boundary Elements vol. 137 160–181 (2022) -- [10.1016/j.enganabound.2021.10.023](https://doi.org/10.1016/j.enganabound.2021.10.023)

