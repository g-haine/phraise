---
layout: post
title: "Discontinuous Galerkin Finite Element Methods for Linear Port-Hamiltonian Dynamical Systems"
date: 2025-05-19 00:00:00 +0100
permalink: discontinuous-galerkin-finite-element-methods-for-linear-port-hamiltonian-dynamical-systems
year: 2025
authors: Xiaoyu Cheng, J. J. W. van der Vegt, Yan Xu, H. J. Zwart
category: articles
tags:
  - Port-Hamiltonian systems
  - Dirac structure
  - Discontinuous Galerkin methods
  - Exterior calculus
---
 
## Authors
[Xiaoyu Cheng](authors/xiaoyu-cheng), [J. J. W. van der Vegt](authors/jaap-j-w-van-der-vegt), [Yan Xu](authors/yan-xu), [H. J. Zwart](authors/hans-zwart)
 
## Abstract
In this paper, we present discontinuous Galerkin (DG) finite element discretizations for a class of linear hyperbolic port-Hamiltonian dynamical systems. The key point in constructing a port-Hamiltonian system is a Stokes-Dirac structure. Instead of following the traditional approach of defining the strong form of the Dirac structure, we define a Dirac structure in weak form, specifically in the input-state-output form. This is implemented within broken Sobolev spaces on a tessellation with polyhedral elements. After that, we state the weak port-Hamiltonian formulation and prove that it relates to a Poisson bracket. In our work, a crucial aspect of constructing the above-mentioned Dirac structure is that we provide a conservative relation between the boundary ports. Next, we state DG discretizations of the port-Hamiltonian system by using the weak form of the Dirac structure and broken polynomial spaces of differential forms, and we provide a priori error estimates for the structure-preserving port-Hamiltonian discontinuous Galerkin (PHDG) discretizations. The accuracy and capability of the methods developed in this paper are demonstrated by presenting several numerical experiments.
 
## Keywords
Port-Hamiltonian systems; Dirac structure; Discontinuous Galerkin methods; Exterior calculus
 
## Citation
- **Journal:** Journal of Scientific Computing
- **Year:** 2025
- **Volume:** 104
- **Issue:** 1
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10915-025-02926-w](https://doi.org/10.1007/s10915-025-02926-w)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Cheng_2025,
  title={{Discontinuous Galerkin Finite Element Methods for Linear Port-Hamiltonian Dynamical Systems}},
  volume={104},
  ISSN={1573-7691},
  DOI={10.1007/s10915-025-02926-w},
  number={1},
  journal={Journal of Scientific Computing},
  publisher={Springer Science and Business Media LLC},
  author={Cheng, Xiaoyu and van der Vegt, J. J. W. and Xu, Yan and Zwart, H. J.},
  year={2025}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/discontinuous-galerkin-finite-element-methods-for-linear-port-hamiltonian-dynamical-systems.bib)
 
## References
- Arnold, D., Falk, R. & Winther, R. Finite element exterior calculus: from Hodge theory to numerical stability. Bull. Amer. Math. Soc. 47, 281–354 (2010) -- [10.1090/s0273-0979-10-01278-4](https://doi.org/10.1090/s0273-0979-10-01278-4)
- Arnold, D. N. Spaces of Finite Element Differential Forms. Springer INdAM Series 117–140 (2013) doi:10.1007/978-88-470-2592-9_9 -- [10.1007/978-88-470-2592-9_9](https://doi.org/10.1007/978-88-470-2592-9_9)
- Arnold, D. & Awanou, G. Finite element differential forms on cubical meshes. Math. Comp. 83, 1551–1570 (2013) -- [10.1090/s0025-5718-2013-02783-4](https://doi.org/10.1090/s0025-5718-2013-02783-4)
- Arnold, D. N., Boffi, D. & Bonizzoni, F. Finite element differential forms on curvilinear cubic meshes and their approximation properties. Numer. Math. 129, 1–20 (2014) -- [10.1007/s00211-014-0631-3](https://doi.org/10.1007/s00211-014-0631-3)
- Arnold, D. N., Falk, R. S. & Winther, R. Finite element exterior calculus, homological techniques, and applications. Acta Numerica 15, 1–155 (2006) -- [10.1017/s0962492906210018](https://doi.org/10.1017/s0962492906210018)
- [Brugnoli, A., Rashad, R. & Stramigioli, S. Dual field structure-preserving discretization of port-Hamiltonian systems using finite element exterior calculus. Journal of Computational Physics 471, 111601 (2022)](dual-field-structure-preserving-discretization-of-port-hamiltonian-systems-using-finite-element-exterior-calculus) -- [10.1016/j.jcp.2022.111601](https://doi.org/10.1016/j.jcp.2022.111601)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information 38, 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- [Cervera, J., van der Schaft, A. J. & Baños, A. Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica 43, 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- B Cockburn, II. General framework. Math. Comp. (1989)
- Cockburn, B. & Shu, C.-W. Journal of Scientific Computing 16, 173–261 (2001) -- [10.1023/a:1012873910884](https://doi.org/10.1023/a:1012873910884)
- [Courant, T. J. Dirac manifolds. Trans. Amer. Math. Soc. 319, 631–661 (1990)](dirac-manifolds) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- Di Pietro, D. A. & Ern, A. Mathematical Aspects of Discontinuous Galerkin Methods. Mathématiques et Applications (Springer Berlin Heidelberg, 2012). doi:10.1007/978-3-642-22980-0 -- [10.1007/978-3-642-22980-0](https://doi.org/10.1007/978-3-642-22980-0)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- T Frankel, The Geometry of Physics: An introduction (2012)
- Hsiao, G. C. & Wendland, W. L. Boundary Integral Equations. Applied Mathematical Sciences (Springer Berlin Heidelberg, 2008). doi:10.1007/978-3-540-68545-6 -- [10.1007/978-3-540-68545-6](https://doi.org/10.1007/978-3-540-68545-6)
- Kalogiratou, Z., Monovasilis, Th. & Simos, T. E. Symplectic Partitioned Runge-Kutta Methods for the Numerical Integration of Periodic and Oscillatory Problems. Recent Advances in Computational and Applied Mathematics 169–208 (2011) doi:10.1007/978-90-481-9981-5_8 -- [10.1007/978-90-481-9981-5_8](https://doi.org/10.1007/978-90-481-9981-5_8)
- P Kotyczka, Numerical methods for distributed parameter port-Hamiltonian Systems (2019)
- [Kotyczka, P., Maschke, B. & Lefèvre, L. Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics 361, 442–476 (2018)](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- [Kumar, N., van der Vegt, J. J. W. & Zwart, H. J. Port-Hamiltonian discontinuous Galerkin finite element methods. IMA Journal of Numerical Analysis 45, 354–403 (2024)](port-hamiltonian-discontinuous-galerkin-finite-element-methods) -- [10.1093/imanum/drae008](https://doi.org/10.1093/imanum/drae008)
- Maschke, B. M. J. & van der Schaft, A. J. Interconnected mechanical systems, part II: the dynamics of spatial mechanical networks. Modelling and Control of Mechanical Systems 17–30 (1997) doi:10.1142/9781848160873_0002 -- [10.1142/9781848160873_0002](https://doi.org/10.1142/9781848160873_0002)
- Monk, P. Finite Element Methods for Maxwell’s Equations. (2003) doi:10.1093/acprof:oso/9780198508885.001.0001 -- [10.1093/acprof:oso/9780198508885.001.0001](https://doi.org/10.1093/acprof:oso/9780198508885.001.0001)
- BG Pachpatte, Inequalities for differential and integral equations (1998)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37, 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Schwarz, G. Hodge Decomposition—A Method for Solving Boundary Value Problems. Lecture Notes in Mathematics (Springer Berlin Heidelberg, 1995). doi:10.1007/bfb0095978 -- [10.1007/bfb0095978](https://doi.org/10.1007/bfb0095978)
- [Seslija, M., van der Schaft, A. & Scherpen, J. M. A. Discrete exterior geometry approach to structure-preserving discretization of distributed-parameter port-Hamiltonian systems. Journal of Geometry and Physics 62, 1509–1531 (2012)](discrete-exterior-geometry-approach-to-structure-preserving-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.geomphys.2012.02.006](https://doi.org/10.1016/j.geomphys.2012.02.006)
- Shu, C.-W. Total-Variation-Diminishing Time Discretizations. SIAM J. Sci. and Stat. Comput. 9, 1073–1084 (1988) -- [10.1137/0909073](https://doi.org/10.1137/0909073)
- Struwe, M. Semi-linear wave equations. Bull. Amer. Math. Soc. 26, 53–85 (1992) -- [10.1090/s0273-0979-1992-00225-2](https://doi.org/10.1090/s0273-0979-1992-00225-2)
- Sun, Z. & Xing, Y. Optimal error estimates of discontinuous Galerkin methods with generalized fluxes for wave equations on unstructured meshes. Math. Comp. 90, 1741–1772 (2021) -- [10.1090/mcom/3605](https://doi.org/10.1090/mcom/3605)
- [Thoma, T. & Kotyczka, P. Structure preserving discontinuous Galerkin approximation of one-dimensional port-Hamiltonian systems. IFAC-PapersOnLine 56, 6783–6788 (2023)](structure-preserving-discontinuous-galerkin-approximation-of-one-dimensional-port-hamiltonian-systems) -- [10.1016/j.ifacol.2023.10.386](https://doi.org/10.1016/j.ifacol.2023.10.386)
- [Trenchant, V., Hu, W., Ramirez, H. & Gorrec, Y. L. Structure Preserving Finite Differences in Polar Coordinates for Heat and Wave Equations. IFAC-PapersOnLine 51, 571–576 (2018)](structure-preserving-finite-differences-in-polar-coordinates-for-heat-and-wave-equations) -- [10.1016/j.ifacol.2018.03.096](https://doi.org/10.1016/j.ifacol.2018.03.096)
- [Trenchant, V., Ramirez, H., Le Gorrec, Y. & Kotyczka, P. Finite differences on staggered grids preserving the port-Hamiltonian structure with application to an acoustic duct. Journal of Computational Physics 373, 673–697 (2018)](finite-differences-on-staggered-grids-preserving-the-port-hamiltonian-structure-with-application-to-an-acoustic-duct) -- [10.1016/j.jcp.2018.06.051](https://doi.org/10.1016/j.jcp.2018.06.051)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. FnT in Systems and Control 1, 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- van der Schaft, A. & Maschke, B. Interconnected mechanical systems, part I: geometry of interconnection and implicit Hamiltonian systems. Modelling and Control of Mechanical Systems 1–15 (1997) doi:10.1142/9781848160873_0001 -- [10.1142/9781848160873_0001](https://doi.org/10.1142/9781848160873_0001)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42, 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- [Xu, Y., van der Vegt, J. J. W. & Bokhove, O. Discontinuous Hamiltonian Finite Element Method for Linear Hyperbolic Systems. J Sci Comput 35, 241–265 (2008)](discontinuous-hamiltonian-finite-element-method-for-linear-hyperbolic-systems) -- [10.1007/s10915-008-9191-y](https://doi.org/10.1007/s10915-008-9191-y)

