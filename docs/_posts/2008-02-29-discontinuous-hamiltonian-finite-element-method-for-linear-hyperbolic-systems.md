---
layout: post
title: "Discontinuous Hamiltonian Finite Element Method for Linear Hyperbolic Systems"
date: 2008-02-29 00:00:00 +0100
permalink: discontinuous-hamiltonian-finite-element-method-for-linear-hyperbolic-systems
year: 2008
authors: Yan Xu, Jaap J. W. van der Vegt, Onno Bokhove
category: articles
tags:
  - Rotating shallow water equations
  - Acoustic equations
  - Maxwell equations
  - Hamiltonian dynamics
  - Discontinuous Galerkin method
  - Numerical flux
---
 
## Authors
[Yan Xu](authors/yan-xu), [Jaap J. W. van der Vegt](authors/jaap-j-w-van-der-vegt), [Onno Bokhove](authors/onno-bokhove)
 
## Abstract
We develop a Hamiltonian discontinuous finite element discretization of a generalized Hamiltonian system for linear hyperbolic systems, which include the rotating shallow water equations, the acoustic and Maxwell equations. These equations have a Hamiltonian structure with a bilinear Poisson bracket, and as a consequence the phase-space structure, “mass” and energy are preserved. We discretize the bilinear Poisson bracket in each element with discontinuous elements and introduce numerical fluxes via integration by parts while preserving the skew-symmetry of the bracket. This automatically results in a mass and energy conservative discretization. When combined with a symplectic time integration method, energy is approximately conserved and shows no drift. For comparison, the discontinuous Galerkin method for this problem is also used. A variety numerical examples is shown to illustrate the accuracy and capability of the new method.
 
## Keywords
Rotating shallow water equations; Acoustic equations; Maxwell equations; Hamiltonian dynamics; Discontinuous Galerkin method; Numerical flux
 
## Citation
- **Journal:** Journal of Scientific Computing
- **Year:** 2008
- **Volume:** 35
- **Issue:** 2-3
- **Pages:** 241--265
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10915-008-9191-y](https://doi.org/10.1007/s10915-008-9191-y)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Xu_2008,
  title={{Discontinuous Hamiltonian Finite Element Method for Linear Hyperbolic Systems}},
  volume={35},
  ISSN={1573-7691},
  DOI={10.1007/s10915-008-9191-y},
  number={2–3},
  journal={Journal of Scientific Computing},
  publisher={Springer Science and Business Media LLC},
  author={Xu, Yan and van der Vegt, Jaap J. W. and Bokhove, Onno},
  year={2008},
  pages={241--265}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/discontinuous-hamiltonian-finite-element-method-for-linear-hyperbolic-systems.bib)
 
## References
- Bokhove, O. & Oliver, M. Parcel Eulerian–Lagrangian fluid dynamics of rotating geophysical flows. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences vol. 462 2575–2592 (2006) -- [10.1098/rspa.2006.1656](https://doi.org/10.1098/rspa.2006.1656)
- B. Cockburn, Math. Comput. (1990)
- Cockburn, B. & Shu, C.-W. The Runge–Kutta Discontinuous Galerkin Method for Conservation Laws V. Journal of Computational Physics vol. 141 199–224 (1998) -- [10.1006/jcph.1998.5892](https://doi.org/10.1006/jcph.1998.5892)
- Hairer, E., Wanner, G. & Lubich, C. Geometric Numerical Integration. Springer Series in Computational Mathematics (Springer Berlin Heidelberg, 2002). doi:10.1007/978-3-662-05018-7 -- [10.1007/978-3-662-05018-7](https://doi.org/10.1007/978-3-662-05018-7)
- [Hairer, E., Lubich, C. & Wanner, G. Geometric numerical integration illustrated by the Störmer–Verlet method. Acta Numerica vol. 12 399–450 (2003)](geometric-numerical-integration-illustrated-by-the-stormer-verlet-method) -- [10.1017/s0962492902000144](https://doi.org/10.1017/s0962492902000144)
- Huttunen, T., Monk, P., Collino, F. & Kaipio, J. P. The Ultra-Weak Variational Formulation for Elastic Wave Problems. SIAM Journal on Scientific Computing vol. 25 1717–1742 (2004) -- [10.1137/s1064827503422233](https://doi.org/10.1137/s1064827503422233)
- H. Lamb, Hydrodynamics (1975)
- J. Lighthill, Waves in Fluids (1978)
- J.E. Marsden, Texts in Applied Mathematics (1994)
- Morrison, P. J. Hamiltonian description of the ideal fluid. Reviews of Modern Physics vol. 70 467–521 (1998) -- [10.1103/revmodphys.70.467](https://doi.org/10.1103/revmodphys.70.467)
- Salmon, R. Lectures on Geophysical Fluid Dynamics. (1998) doi:10.1093/oso/9780195108088.001.0001 -- [10.1093/oso/9780195108088.001.0001](https://doi.org/10.1093/oso/9780195108088.001.0001)
- Shu, C.-W. & Osher, S. Efficient implementation of essentially non-oscillatory shock-capturing schemes. Journal of Computational Physics vol. 77 439–471 (1988) -- [10.1016/0021-9991(88)90177-5](https://doi.org/10.1016/0021-9991(88)90177-5)
- Yan, J. & Shu, C.-W. Journal of Scientific Computing vol. 17 27–47 (2002) -- [10.1023/a:1015132126817](https://doi.org/10.1023/a:1015132126817)

