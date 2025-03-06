---
layout: post
title: "Semi-discrete entropy-preserving surface reconstruction schemes for the shallow water equations: Analysis of physical structures"
date: 2024-04-06 00:00:00 +0100
permalink: semi-discrete-entropy-preserving-surface-reconstruction-schemes-for-the-shallow-water-equations-analysis-of-physical-structures
year: 2024
authors: Jian Dong, Xu Qian
category:
  - articles
tags:
  - riemann-state reconstructions
  - saint-venant systems
  - entropy conditions
  - physical-structure-preserving
---
 
## Authors
[Jian Dong](authors/jian_dong), [Xu Qian](authors/xu_qian)
 
## Abstract
We aim to introduce a new variant of hydrostatic reconstruction scheme, which is physical-structure-preserving and semi-discrete entropy-preserving for shallow water equations with a discontinuous bottom topography, based on novel surface reconstructions (NSR). The NSR is used to define approximate Riemann states with respect to the water depth and the velocity to compute consistent numerical fluxes across the cell interface and the upwind interface source term. This work is motivated by path-conservative surface reconstructions (Dong (2023) [19]), in which the conditions to satisfy the entropy inequality are complicated. We propose the NSR scheme to satisfy the entropy inequality without the corresponding complicated conditions. A key advantage of the NSR scheme is to preserve the physical structure of the water surface in the sense that when the water surface is continuous, then the defined approximate Riemann state should inherit this property. The physical-structure-preserving property is indispensable for obtaining a more accurate discretized source term and avoiding artificial “waterfall” effects. We prove that the NSR scheme satisfies a semi-discrete entropy condition and can guarantee the water depth to be nonnegative, and maintain the stationary state. We show several computed results to compare the NSR scheme with the hydrostatic reconstruction scheme based on subcell reconstructions and the path-conservative surface reconstruction scheme. We also extend the NSR scheme for pollutant transport in shallow water based on adaptive moving triangular meshes. Finally, several numerical results obtained by the adaptive NSR scheme for pollutant transport in shallow water are shown.
 
## Keywords
Riemann-state reconstructions; Saint-Venant systems; Entropy conditions; Physical-structure-preserving
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2024
- **Volume:** 508
- **Issue:** 
- **Pages:** 112995
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2024.112995](https://doi.org/10.1016/j.jcp.2024.112995)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Dong_2024,
  title={{Semi-discrete entropy-preserving surface reconstruction schemes for the shallow water equations: Analysis of physical structures}},
  volume={508},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2024.112995},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Dong, Jian and Qian, Xu},
  year={2024},
  pages={112995}
}
{% endraw %}
{% endhighlight %}
 
## References
- Gallardo, J. M., Parés, C. & Castro, M. On a well-balanced high-order finite volume scheme for shallow water equations with topography and dry areas. Journal of Computational Physics vol. 227 574–601 (2007) -- [10.1016/j.jcp.2007.08.007](https://doi.org/10.1016/j.jcp.2007.08.007)
- Bollermann, A., Chen, G., Kurganov, A. & Noelle, S. A Well-Balanced Reconstruction of Wet/Dry Fronts for the Shallow Water Equations. Journal of Scientific Computing vol. 56 267–290 (2013) -- [10.1007/s10915-012-9677-5](https://doi.org/10.1007/s10915-012-9677-5)
- Jin, S. A steady-state capturing method for hyperbolic systems with geometrical source terms. ESAIM: Mathematical Modelling and Numerical Analysis vol. 35 631–645 (2001) -- [10.1051/m2an:2001130](https://doi.org/10.1051/m2an:2001130)
- Audusse, E., Bouchut, F., Bristeau, M.-O., Klein, R. & Perthame, B. A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. SIAM Journal on Scientific Computing vol. 25 2050–2065 (2004) -- [10.1137/S1064827503431090](https://doi.org/10.1137/S1064827503431090)
- Bollermann, A., Noelle, S. & Lukáčová-Medvid’ová, M. Finite Volume Evolution Galerkin Methods for the Shallow Water Equations with Dry Beds. Communications in Computational Physics vol. 10 371–404 (2011) -- [10.4208/cicp.220210.020710a](https://doi.org/10.4208/cicp.220210.020710a)
- Xing, Y. & Shu, C.-W. High order well-balanced finite volume WENO schemes and discontinuous Galerkin methods for a class of hyperbolic systems with source terms. Journal of Computational Physics vol. 214 567–598 (2006) -- [10.1016/j.jcp.2005.10.005](https://doi.org/10.1016/j.jcp.2005.10.005)
- Dong, J. & Li, D. F. A new second-order modified hydrostatic reconstruction for the shallow water flows with a discontinuous topography. Applied Numerical Mathematics vol. 161 408–424 (2021) -- [10.1016/j.apnum.2020.11.019](https://doi.org/10.1016/j.apnum.2020.11.019)
- Noelle, S., Pankratz, N., Puppo, G. & Natvig, J. R. Well-balanced finite volume schemes of arbitrary order of accuracy for shallow water flows. Journal of Computational Physics vol. 213 474–499 (2006) -- [10.1016/j.jcp.2005.08.019](https://doi.org/10.1016/j.jcp.2005.08.019)
- Xing, Y., Zhang, X. & Shu, C.-W. Positivity-preserving high order well-balanced discontinuous Galerkin methods for the shallow water equations. Advances in Water Resources vol. 33 1476–1493 (2010) -- [10.1016/j.advwatres.2010.08.005](https://doi.org/10.1016/j.advwatres.2010.08.005)
- Chen, G. & Noelle, S. A New Hydrostatic Reconstruction Scheme Based on Subcell Reconstructions. SIAM Journal on Numerical Analysis vol. 55 758–784 (2017) -- [10.1137/15M1053074](https://doi.org/10.1137/15M1053074)
- Michel-Dansac, V., Berthon, C., Clain, S. & Foucher, F. A well-balanced scheme for the shallow-water equations with topography or Manning friction. Journal of Computational Physics vol. 335 115–154 (2017) -- [10.1016/j.jcp.2017.01.009](https://doi.org/10.1016/j.jcp.2017.01.009)
- Dong, J. & Li, D. F. A reliable second-order hydrostatic reconstruction for shallow water flows with the friction term and the bed source term. Journal of Computational and Applied Mathematics vol. 376 112871 (2020) -- [10.1016/j.cam.2020.112871](https://doi.org/10.1016/j.cam.2020.112871)
- Dong, J. A robust second-order surface reconstruction for shallow water flows with a discontinuous topography and a Manning friction. Advances in Computational Mathematics vol. 46 (2020) -- [10.1007/s10444-020-09783-1](https://doi.org/10.1007/s10444-020-09783-1)
- Kurganov, A. & Petrova, G. A Second-Order Well-Balanced Positivity Preserving Central-Upwind Scheme for the Saint-Venant System. Communications in Mathematical Sciences vol. 5 133–160 (2007) -- [10.4310/CMS.2007.v5.n1.a6](https://doi.org/10.4310/CMS.2007.v5.n1.a6)
- Liu, X., Albright, J., Epshteyn, Y. & Kurganov, A. Well-balanced positivity preserving central-upwind scheme with a novel wet/dry reconstruction on triangular grids for the Saint-Venant system. Journal of Computational Physics vol. 374 213–236 (2018) -- [10.1016/j.jcp.2018.07.038](https://doi.org/10.1016/j.jcp.2018.07.038)
- Chertock, A., Cui, S., Kurganov, A. & Wu, T. Well‐balanced positivity preserving central‐upwind scheme for the shallow water system with friction terms. International Journal for Numerical Methods in Fluids vol. 78 355–383 (2015) -- [10.1002/fld.4023](https://doi.org/10.1002/fld.4023)
- Dong, J. Surface reconstruction schemes for shallow water equations with a nonconservative product source term. Journal of Computational Physics vol. 473 111738 (2023) -- [10.1016/j.jcp.2022.111738](https://doi.org/10.1016/j.jcp.2022.111738)
- Castro, M. J., Morales de Luna, T. & Parés, C. Well-Balanced Schemes and Path-Conservative Numerical Methods. Handbook of Numerical Analysis 131–175 (2017) doi:10.1016/bs.hna.2016.10.002 -- [10.1016/bs.hna.2016.10.002](https://doi.org/10.1016/bs.hna.2016.10.002)
- Abgrall, R. & Karni, S. A comment on the computation of non-conservative products. Journal of Computational Physics vol. 229 2759–2763 (2010) -- [10.1016/j.jcp.2009.12.015](https://doi.org/10.1016/j.jcp.2009.12.015)
- Castro, M. J., LeFloch, P. G., Muñoz-Ruiz, M. L. & Parés, C. Why many theories of shock waves are necessary: Convergence error in formally path-consistent schemes. Journal of Computational Physics vol. 227 8107–8129 (2008) -- [10.1016/j.jcp.2008.05.012](https://doi.org/10.1016/j.jcp.2008.05.012)
- Delestre, O., Cordier, S., Darboux, F. & James, F. A limitation of the hydrostatic reconstruction technique for Shallow Water equations. Comptes Rendus. Mathématique vol. 350 677–681 (2012) -- [10.1016/j.crma.2012.08.004](https://doi.org/10.1016/j.crma.2012.08.004)
- Xia, X., Liang, Q., Ming, X. & Hou, J. An efficient and stable hydrodynamic model with novel source term discretization schemes for overland flow and flood simulations. Water Resources Research vol. 53 3730–3759 (2017) -- [10.1002/2016WR020055](https://doi.org/10.1002/2016WR020055)
- Xia, X. & Liang, Q. A new efficient implicit scheme for discretising the stiff friction terms in the shallow water equations. Advances in Water Resources vol. 117 87–97 (2018) -- [10.1016/j.advwatres.2018.05.004](https://doi.org/10.1016/j.advwatres.2018.05.004)
- Buttinger-Kreuzhuber, A., Horváth, Z., Noelle, S., Blöschl, G. & Waser, J. A fast second-order shallow water scheme on two-dimensional structured grids over abrupt topography. Advances in Water Resources vol. 127 89–108 (2019) -- [10.1016/j.advwatres.2019.03.010](https://doi.org/10.1016/j.advwatres.2019.03.010)
- Gallouët, T., Hérard, J. ‐M. & Seguin, N. Some recent finite volume schemes to compute Euler equations using real gas EOS. International Journal for Numerical Methods in Fluids vol. 39 1073–1138 (2002) -- [10.1002/fld.346](https://doi.org/10.1002/fld.346)
- LeFloch, P. G. & Mishra, S. Numerical methods with controlled dissipation for small-scale dependent shocks. Acta Numerica vol. 23 743–816 (2014) -- [10.1017/S0962492914000099](https://doi.org/10.1017/S0962492914000099)
- Audusse, E., Bouchut, F., Bristeau, M.-O. & Sainte-Marie, J. Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. Mathematics of Computation vol. 85 2815–2837 (2016) -- [10.1090/mcom/3099](https://doi.org/10.1090/mcom/3099)
- Bouchut, F. & Lhébrard, X. Convergence of the kinetic hydrostatic reconstruction scheme for the Saint Venant system with topography. Mathematics of Computation vol. 90 1119–1153 (2020) -- [10.1090/mcom/3600](https://doi.org/10.1090/mcom/3600)
- Berthon, C., Duran, A., Foucher, F., Saleh, K. & Zabsonré, J. D. D. Improvement of the Hydrostatic Reconstruction Scheme to Get Fully Discrete Entropy Inequalities. Journal of Scientific Computing vol. 80 924–956 (2019) -- [10.1007/s10915-019-00961-y](https://doi.org/10.1007/s10915-019-00961-y)
- Aleksyuk, A. I. & Belikov, V. V. The uniqueness of the exact solution of the Riemann problem for the shallow water equations with discontinuous bottom. Journal of Computational Physics vol. 390 232–248 (2019) -- [10.1016/j.jcp.2019.04.001](https://doi.org/10.1016/j.jcp.2019.04.001)
- M.S. Joe Sampson, Alan Easton, Moving boundary shallow water flow in parabolic bottom topography, ANZIAM J.
- Sampson, J., Easton, A. & Singh, M. Moving boundary shallow water flow above parabolic bottom topography. ANZIAM Journal vol. 47 373 (2006) -- [10.21914/anziamj.v47i0.1050](https://doi.org/10.21914/anziamj.v47i0.1050)
- J. Dong, X. Qian, Adaptive moving surface reconstruction schemes solving the ripa systems, a provable positivity-preserving parameter, submitted for publication.
- Chen, G., Tang, H. & Zhang, P. Second-Order Accurate Godunov Scheme for Multicomponent Flows on Moving Triangular Meshes. Journal of Scientific Computing vol. 34 64–86 (2007) -- [10.1007/s10915-007-9162-8](https://doi.org/10.1007/s10915-007-9162-8)
- Chertock, A. & Kurganov, A. On a hybrid finite-volume-particle method. ESAIM: Mathematical Modelling and Numerical Analysis vol. 38 1071–1091 (2004) -- [10.1051/m2an:2004051](https://doi.org/10.1051/m2an:2004051)
- Li, G., Gao, J. & Liang, Q. A well‐balanced weighted essentially non‐oscillatory scheme for pollutant transport in shallow water. International Journal for Numerical Methods in Fluids vol. 71 1566–1587 (2012) -- [10.1002/fld.3726](https://doi.org/10.1002/fld.3726)

