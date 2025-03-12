---
layout: post
title: "Discrete conservation properties for shallow water flows using mixed mimetic spectral elements"
date: 2017-12-20 00:00:00 +0100
permalink: discrete-conservation-properties-for-shallow-water-flows-using-mixed-mimetic-spectral-elements
year: 2018
authors: D. Lee, A. Palha, M. Gerritsma
category: articles
tags:
  - Mimetic
  - Spectral elements
  - High order
  - Shallow water
  - Energy and potential enstrophy conservation
---
 
## Authors
[D. Lee](authors/d-lee), [A. Palha](authors/a-palha), [M. Gerritsma](authors/m-gerritsma)
 
## Abstract
A mixed mimetic spectral element method is applied to solve the rotating shallow water equations. The mixed method uses the recently developed spectral element histopolation functions, which exactly satisfy the fundamental theorem of calculus with respect to the standard Lagrange basis functions in one dimension. These are used to construct tensor product solution spaces which satisfy the generalized Stokes theorem, as well as the annihilation of the gradient operator by the curl and the curl by the divergence. This allows for the exact conservation of first order moments (mass, vorticity), as well as higher moments (energy, potential enstrophy), subject to the truncation error of the time stepping scheme. The continuity equation is solved in the strong form, such that mass conservation holds point wise, while the momentum equation is solved in the weak form such that vorticity is globally conserved. While mass, vorticity and energy conservation hold for any quadrature rule, potential enstrophy conservation is dependent on exact spatial integration. The method possesses a weak form statement of geostrophic balance due to the compatible nature of the solution spaces and arbitrarily high order spatial error convergence.
 
## Keywords
Mimetic; Spectral elements; High order; Shallow water; Energy and potential enstrophy conservation
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2018
- **Volume:** 357
- **Issue:** 
- **Pages:** 282--304
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2017.12.022](https://doi.org/10.1016/j.jcp.2017.12.022)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Lee_2018,
  title={{Discrete conservation properties for shallow water flows using mixed mimetic spectral elements}},
  volume={357},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2017.12.022},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Lee, D. and Palha, A. and Gerritsma, M.},
  year={2018},
  pages={282--304}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/discrete-conservation-properties-for-shallow-water-flows-using-mixed-mimetic-spectral-elements.bib)
 
## References
- Thuburn, J. Some conservation issues for the dynamical cores of NWP and climate models. Journal of Computational Physics vol. 227 3715–3730 (2008) -- [10.1016/j.jcp.2006.08.016](https://doi.org/10.1016/j.jcp.2006.08.016)
- [Palha, A. & Gerritsma, M. A mass, energy, enstrophy and vorticity conserving (MEEVC) mimetic spectral element discretization for the 2D incompressible Navier–Stokes equations. Journal of Computational Physics vol. 328 200–220 (2017)](a-mass-energy-enstrophy-and-vorticity-conserving-meevc-mimetic-spectral-element-discretization-for-the-2d-incompressible-navier-stokes-equations) -- [10.1016/j.jcp.2016.10.009](https://doi.org/10.1016/j.jcp.2016.10.009)
- Cotter, C. J. & Shipton, J. Mixed finite elements for numerical weather prediction. Journal of Computational Physics vol. 231 7076–7091 (2012) -- [10.1016/j.jcp.2012.05.020](https://doi.org/10.1016/j.jcp.2012.05.020)
- McRae, A. T. T. & Cotter, C. J. Energy‐ and enstrophy‐conserving schemes for the shallow‐water equations, based on mimetic finite elements. Quarterly Journal of the Royal Meteorological Society vol. 140 2223–2234 (2014) -- [10.1002/qj.2291](https://doi.org/10.1002/qj.2291)
- Natale, Compatible finite element spaces for geophysical fluid dynamics. Dyn. Stat. Climate Syst. (2016)
- Arakawa, A. & Lamb, V. R. A Potential Enstrophy and Energy Conserving Scheme for the Shallow Water Equations. Monthly Weather Review vol. 109 18–36 (1981) -- [10.1175/1520-0493(1981)109<0018:apeaec>2.0.co;2](https://doi.org/10.1175/1520-0493(1981)109<0018:apeaec>2.0.co;2)
- Salmon, R. Poisson-Bracket Approach to the Construction of Energy- and Potential-Enstrophy-Conserving Algorithms for the Shallow-Water Equations. Journal of the Atmospheric Sciences vol. 61 2016–2036 (2004) -- [10.1175/1520-0469(2004)061<2016:pattco>2.0.co;2](https://doi.org/10.1175/1520-0469(2004)061<2016:pattco>2.0.co;2)
- Salmon, R. A General Method for Conserving Energy and Potential Enstrophy in Shallow-Water Models. Journal of the Atmospheric Sciences vol. 64 515–531 (2007) -- [10.1175/jas3837.1](https://doi.org/10.1175/jas3837.1)
- Cotter, C. J. & Thuburn, J. A finite element exterior calculus framework for the rotating shallow-water equations. Journal of Computational Physics vol. 257 1506–1526 (2014) -- [10.1016/j.jcp.2013.10.008](https://doi.org/10.1016/j.jcp.2013.10.008)
- Taylor, M. A. & Fournier, A. A compatible and conservative spectral element method on unstructured grids. Journal of Computational Physics vol. 229 5879–5895 (2010) -- [10.1016/j.jcp.2010.04.008](https://doi.org/10.1016/j.jcp.2010.04.008)
- Gerritsma, Edge functions for spectral element methods. (2011)
- Kreeft, J. & Gerritsma, M. Mixed mimetic spectral element method for Stokes flow: A pointwise divergence-free solution. Journal of Computational Physics vol. 240 284–309 (2013) -- [10.1016/j.jcp.2012.10.043](https://doi.org/10.1016/j.jcp.2012.10.043)
- Vallis, (2006)
- Thuburn, J., Ringler, T. D., Skamarock, W. C. & Klemp, J. B. Numerical representation of geostrophic modes on arbitrarily structured C-grids. Journal of Computational Physics vol. 228 8321–8335 (2009) -- [10.1016/j.jcp.2009.08.006](https://doi.org/10.1016/j.jcp.2009.08.006)
- Kreeft,
- Hiemstra, R. R., Toshniwal, D., Huijsmans, R. H. M. & Gerritsma, M. I. High order geometric methods with exact conservation properties. Journal of Computational Physics vol. 257 1444–1471 (2014) -- [10.1016/j.jcp.2013.09.027](https://doi.org/10.1016/j.jcp.2013.09.027)
- Brezzi, Mixed and Hybrid Finite Element Methods. (1991)
- Boffi, Mixed Finite Element Methods and Applications. (2013)
- Arnold, D. N., Boffi, D. & Bonizzoni, F. Finite element differential forms on curvilinear cubic meshes and their approximation properties. Numerische Mathematik vol. 129 1–20 (2014) -- [10.1007/s00211-014-0631-3](https://doi.org/10.1007/s00211-014-0631-3)
- Arnold, D. & Awanou, G. Finite element differential forms on cubical meshes. Mathematics of Computation vol. 83 1551–1570 (2013) -- [10.1090/s0025-5718-2013-02783-4](https://doi.org/10.1090/s0025-5718-2013-02783-4)
- Arnold, D. N., Boffi, D. & Falk, R. S. QuadrilateralH(div) Finite Elements. SIAM Journal on Numerical Analysis vol. 42 2429–2451 (2005) -- [10.1137/s0036142903431924](https://doi.org/10.1137/s0036142903431924)
- Bossavit, Computational electromagnetism and geometry: (1) Network equations. J. Jpn. Soc. Appl. Electromagn. (1999)
- Bossavit, Computational electromagnetism and geometry: (2) Network constitutive laws. J. Jpn. Soc. Appl. Electromagn. (1999)
- Bossavit, Computational electromagnetism and geometry: (3) Convergence. J. Jpn. Soc. Appl. Electromagn. (1999)
- Bossavit, Computational electromagnetism and geometry: (4) From degrees of freedom to fields. J. Jpn. Soc. Appl. Electromagn. (2000)
- Bossavit, Computational electromagnetism and geometry: (5) The “Galerkin Hodge”. J. Jpn. Soc. Appl. Electromagn. (2000)
- Arnold, D. N., Falk, R. S. & Winther, R. Finite element exterior calculus, homological techniques, and applications. Acta Numerica vol. 15 1–155 (2006) -- [10.1017/s0962492906210018](https://doi.org/10.1017/s0962492906210018)
- Arnold, D., Falk, R. & Winther, R. Finite element exterior calculus: from Hodge theory to numerical stability. Bulletin of the American Mathematical Society vol. 47 281–354 (2010) -- [10.1090/s0273-0979-10-01278-4](https://doi.org/10.1090/s0273-0979-10-01278-4)
- Palha, A., Rebelo, P. P., Hiemstra, R., Kreeft, J. & Gerritsma, M. Physics-compatible discretization techniques on single and dual grids, with application to the Poisson equation of volume forms. Journal of Computational Physics vol. 257 1394–1422 (2014) -- [10.1016/j.jcp.2013.08.005](https://doi.org/10.1016/j.jcp.2013.08.005)
- Robidoux,
- Abraham, Manifolds, Tensor Analysis, and Applications. (2001)
- Frankel, (2004)
- Sadourny, R. & Basdevant, C. Parameterization of Subgrid Scale Barotropic and Baroclinic Eddies in Quasi-geostrophic Models: Anticipated Potential Vorticity Method. Journal of the Atmospheric Sciences vol. 42 1353–1363 (1985) -- [10.1175/1520-0469(1985)042<1353:possba>2.0.co;2](https://doi.org/10.1175/1520-0469(1985)042<1353:possba>2.0.co;2)
- Eldred, C. & Randall, D. Total energy and potential enstrophy conserving schemes for the shallow water equations using Hamiltonian methods – Part 1: Derivation and properties. Geoscientific Model Development vol. 10 791–810 (2017) -- [10.5194/gmd-10-791-2017](https://doi.org/10.5194/gmd-10-791-2017)
- Karniadakis, (2005)
- Melvin, T., Staniforth, A. & Thuburn, J. Dispersion analysis of the spectral element method. Quarterly Journal of the Royal Meteorological Society vol. 138 1934–1947 (2012) -- [10.1002/qj.1906](https://doi.org/10.1002/qj.1906)

