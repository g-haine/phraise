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
[Yan Xu](authors/yan_xu), [Jaap J. W. van der Vegt](authors/jaap_j_w_van_der_vegt), [Onno Bokhove](authors/onno_bokhove)
 
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
 
## References
- Bokhove, O., Oliver, M.: Parcel Eulerian-Lagrangian fluid dynamics for rotating geophysical flows. Proc. R. Soc. A. 462, 2563–2573 (2006) -- [10.1098/rspa.2006.1656](https://doi.org/10.1098/rspa.2006.1656)
- Blom, C.: Discontinuous Galerkin method on tetrahedral elements for aeroacoustic. Ph.D. Thesis, University of Twente, Enschede, The Netherlands (2003)
- Cockburn, B., Hou, S., Shu, C.-W.: The Runge-Kutta local projection discontinuous Galerkin finite element method for conservation laws IV: the multidimensional case. Math. Comput. 54, 545–581 (1990)
- Cockburn, B., Shu, C.-W.: The Runge-Kutta discontinuous Galerkin method for conservation laws V: multidimensional systems. J. Comput. Phys. 141, 199–224 (1998) -- [10.1006/jcph.1998.5892](https://doi.org/10.1006/jcph.1998.5892)
- Hairer, E., Lubich, C., Wanner, G.: Geometric Numerical Integration: Structure Preserving Algorithms for Ordinary Differential Equations. Springer, Heidelberg (2002) -- [10.1007/978-3-662-05018-7](https://doi.org/10.1007/978-3-662-05018-7)
- [Hairer, E., Lubich, C., Wanner, G.: Geometric numerical integration illustrated by the Störmer-Verlet method. Acta Numerica 12, 399–450 (2003)](geometric-numerical-integration-illustrated-by-the-stormer-verlet-method) -- [10.1017/S0962492902000144](https://doi.org/10.1017/S0962492902000144)
- Huttunen, T., Monk, P., Collino, F., Kaipio, J.P.: The ultra-weak variational formulation for elastic wave problems. SIAM J. Sci. Comput. 25, 1717–1742 (2004) -- [10.1137/S1064827503422233](https://doi.org/10.1137/S1064827503422233)
- Lamb, H.: Hydrodynamics, 6th edn. Cambridge University Press, London (1975)
- Lighthill, J.: Waves in Fluids. Cambridge University Press, London (1978)
- Marsden, J.E., Ratiu, T.S.: Introduction to mechanics and symmetry: a basic exposition of classical mechanical systems. In: Texts in Applied Mathematics, vol. 17. Springer, New York (1994)
- Morrison, P.J.: Hamiltonian description of the ideal fluid. Rev. Mod. Phys. 70, 467–521 (1998) -- [10.1103/RevModPhys.70.467](https://doi.org/10.1103/RevModPhys.70.467)
- Salmon, R.: Lectures on Geophysical Fluid Dynamics. Oxford University Press, Oxford (1998) -- [10.1093/oso/9780195108088.001.0001](https://doi.org/10.1093/oso/9780195108088.001.0001)
- Shu, C.-W., Osher, S.: Efficient implementation of essentially non-oscillatory shock-capturing schemes. J. Comput. Phys. 77, 439–471 (1988) -- [10.1016/0021-9991(88)90177-5](https://doi.org/10.1016/0021-9991(88)90177-5)
- Yan, J., Shu, C.-W.: Local discontinuous Galerkin methods for partial differential equations with higher order derivatives. J. Sci. Comput. 17, 27–47 (2002) -- [10.1023/A:1015132126817](https://doi.org/10.1023/A:1015132126817)

