---
title: "A domain decomposition strategy for natural imposition of mixed boundary conditions in port-Hamiltonian systems"
date: 2026-01-17 00:00:00 +0100
permalink: a-domain-decomposition-strategy-for-natural-imposition-of-mixed-boundary-conditions-in-port-hamiltonian-systems
year: 2026
authors: Sjoerd De Jong, Andrea Brugnoli, Ramy Rashad, Yi Zhang, Stefano Stramigioli
category: articles
tags:
  - finite element exterior calculus, geometrically exact beams, mechanical vibrations, mixed boundary conditions, port-hamiltonian systems, shear locking
---
 
## Authors
[Sjoerd De Jong](authors/sjoerd-de-jong), [Andrea Brugnoli](authors/andrea-brugnoli), [Ramy Rashad](authors/ramy-rashad), [Yi Zhang](authors/yi-zhang), [Stefano Stramigioli](authors/stefano-stramigioli)
 
## Abstract
In this contribution, a finite element scheme to impose mixed boundary conditions without introducing Lagrange multipliers is presented for hyperbolic systems described as port-Hamiltonian systems. The strategy relies on finite element exterior calculus and domain decomposition to interconnect two systems with dual input-output behavior. The spatial domain is split into two parts by introducing an arbitrary interface. Each subdomain is discretized with a mixed finite element formulation that introduces a uniform boundary condition in a natural way as the input. In each subdomain the finite element spaces are selected from a finite element subcomplex to obtain a stable discretization. The two systems are then interconnected together by making use of a feedback interconnection. This is achieved by discretizing the boundary inputs using appropriate spaces that couple the two formulations. The final systems include all boundary conditions explicitly and do not contain any Lagrange multiplier. Time integration is performed using the implicit midpoint or Störmer-Verlet scheme. The method can also be applied to semilinear systems containing algebraic nonlinearities. The proposed strategy is tested on different examples: geometrically exact intrinsic beam model, the wave equation, membrane elastodynamics and the Mindlin plate. Numerical tests assess the conservation properties of the scheme, the effectiveness of the methodology and its robustness against shear locking phenomena.
 
## Keywords
finite element exterior calculus, geometrically exact beams, mechanical vibrations, mixed boundary conditions, port-hamiltonian systems, shear locking
 
## Citation
- **Journal:** Applied Mathematical Modelling
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 116775
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.apm.2026.116775](https://doi.org/10.1016/j.apm.2026.116775)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{De_Jong_2026,
  title={{A domain decomposition strategy for natural imposition of mixed boundary conditions in port-Hamiltonian systems}},
  ISSN={0307-904X},
  DOI={10.1016/j.apm.2026.116775},
  journal={Applied Mathematical Modelling},
  publisher={Elsevier BV},
  author={De Jong, Sjoerd and Brugnoli, Andrea and Rashad, Ramy and Zhang, Yi and Stramigioli, Stefano},
  year={2026},
  pages={116775}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-domain-decomposition-strategy-for-natural-imposition-of-mixed-boundary-conditions-in-port-hamiltonian-systems.bib)
 
## References
- [Rashad R, Califano F, van der Schaft AJ, Stramigioli S (2020) Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37(4):1400–1422. https://doi.org/10.1093/imamci/dnaa01](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Bochev, A discourse on variational and geometric aspects of stability of discretizations. 33rd Computational Fluid Dynamics Lecture Series, VKI LS (2003)
- Arnold DN, Falk RS, Winther R (2006) Finite element exterior calculus, homological techniques, and applications. Acta Numerica 15:1–155. https://doi.org/10.1017/s096249290621001 -- [10.1017/s0962492906210018](https://doi.org/10.1017/s0962492906210018)
- [Christiansen SH, Munthe-Kaas HZ, Owren B (2011) Topics in structure-preserving discretization. Acta Numerica 20:1–119. https://doi.org/10.1017/s096249291100002](topics-in-structure-preserving-discretization) -- [10.1017/s096249291100002x](https://doi.org/10.1017/s096249291100002x)
- Bochev, Principles of mimetic discretizations of differential operators. (2006)
- Lipnikov K, Manzini G, Shashkov M (2014) Mimetic finite difference method. Journal of Computational Physics 257:1163–1227. https://doi.org/10.1016/j.jcp.2013.07.03 -- [10.1016/j.jcp.2013.07.031](https://doi.org/10.1016/j.jcp.2013.07.031)
- Hirani, (2003)
- [van der Schaft AJ, Maschke BM (2002) Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42(1–2):166–194. https://doi.org/10.1016/s0393-0440(01)00083-](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- Quarteroni, (2008)
- Bazilevs Y, Hughes TJR (2007) Weak imposition of Dirichlet boundary conditions in fluid mechanics. Computers &amp; Fluids 36(1):12–26. https://doi.org/10.1016/j.compfluid.2005.07.01 -- [10.1016/j.compfluid.2005.07.012](https://doi.org/10.1016/j.compfluid.2005.07.012)
- Eriksson G, Mattsson K (2022) Weak Versus Strong Wall Boundary Conditions for the Incompressible Navier-Stokes Equations. J Sci Comput 92(3). https://doi.org/10.1007/s10915-022-01941- -- [10.1007/s10915-022-01941-5](https://doi.org/10.1007/s10915-022-01941-5)
- Kunkel, (2006)
- [Seslija M, Scherpen JMA, van der Schaft A (2014) Explicit simplicial discretization of distributed-parameter port-Hamiltonian systems. Automatica 50(2):369–377. https://doi.org/10.1016/j.automatica.2013.11.02](explicit-simplicial-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.11.020](https://doi.org/10.1016/j.automatica.2013.11.020)
- [Kotyczka P, Maschke B, Lefèvre L (2018) Weak form of Stokes–Dirac structures and geometric discretization of port-Hamiltonian systems. Journal of Computational Physics 361:442–476. https://doi.org/10.1016/j.jcp.2018.02.00](weak-form-of-stokes-dirac-structures-and-geometric-discretization-of-port-hamiltonian-systems) -- [10.1016/j.jcp.2018.02.006](https://doi.org/10.1016/j.jcp.2018.02.006)
- [Cardoso-Ribeiro FL, Matignon D, Lefèvre L (2020) A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information 38(2):493–533. https://doi.org/10.1093/imamci/dnaa03](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Kumar, Port-Hamiltonian discontinuous Galerkin finite element methods. IMA Journal of Numerical Analysis (2024)
- Joly, (2003)
- [Brugnoli A, Rashad R, Stramigioli S (2022) Dual field structure-preserving discretization of port-Hamiltonian systems using finite element exterior calculus. Journal of Computational Physics 471:111601. https://doi.org/10.1016/j.jcp.2022.11160](dual-field-structure-preserving-discretization-of-port-hamiltonian-systems-using-finite-element-exterior-calculus) -- [10.1016/j.jcp.2022.111601](https://doi.org/10.1016/j.jcp.2022.111601)
- Zhang Y, Palha A, Gerritsma M, Rebholz LG (2022) A mass-, kinetic energy- and helicity-conserving mimetic dual-field discretization for three-dimensional incompressible Navier-Stokes equations, part I: Periodic domains. Journal of Computational Physics 451:110868. https://doi.org/10.1016/j.jcp.2021.11086 -- [10.1016/j.jcp.2021.110868](https://doi.org/10.1016/j.jcp.2021.110868)
- [Brugnoli A, Cardoso-Ribeiro FL, Haine G, Kotyczka P (2020) Partitioned finite element method for structured discretization with mixed boundary conditions. IFAC-PapersOnLine 53(2):7557–7562. https://doi.org/10.1016/j.ifacol.2020.12.135](partitioned-finite-element-method-for-structured-discretization-with-mixed-boundary-conditions) -- [10.1016/j.ifacol.2020.12.1351](https://doi.org/10.1016/j.ifacol.2020.12.1351)
- [Brugnoli A, Haine G, Matignon D (2022) Explicit structure-preserving discretization of port-Hamiltonian systems with mixed boundary control. IFAC-PapersOnLine 55(30):418–423. https://doi.org/10.1016/j.ifacol.2022.11.08](explicit-structure-preserving-discretization-of-port-hamiltonian-systems-with-mixed-boundary-control) -- [10.1016/j.ifacol.2022.11.089](https://doi.org/10.1016/j.ifacol.2022.11.089)
- [Kotyczka P, Lefèvre L (2019) Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters 133:104530. https://doi.org/10.1016/j.sysconle.2019.10453](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- [Courant TJ (1990) Dirac manifolds. Trans Amer Math Soc 319(2):631–661. https://doi.org/10.1090/s0002-9947-1990-0998124-](dirac-manifolds) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- Jerrold, Introduction to Mechanics and Symmetry: A Basic Exposition of Classical Mechanical Systems. (1999)
- [Brugnoli A, Mehrmann V (2024) On the discrete equivalence of Lagrangian, Hamiltonian and mixed finite element formulations for linear wave phenomena. IFAC-PapersOnLine 58(6):95–100. https://doi.org/10.1016/j.ifacol.2024.08.26](on-the-discrete-equivalence-of-lagrangian-hamiltonian-and-mixed-finite-element-formulations-for-linear-wave-phenomena) -- [10.1016/j.ifacol.2024.08.263](https://doi.org/10.1016/j.ifacol.2024.08.263)
- Palha A, Rebelo PP, Hiemstra R, Kreeft J, Gerritsma M (2014) Physics-compatible discretization techniques on single and dual grids, with application to the Poisson equation of volume forms. Journal of Computational Physics 257:1394–1422. https://doi.org/10.1016/j.jcp.2013.08.00 -- [10.1016/j.jcp.2013.08.005](https://doi.org/10.1016/j.jcp.2013.08.005)
- Hodges DH (2003) Geometrically Exact, Intrinsic Theory for Dynamics of Curved and Twisted Anisotropic Beams. AIAA Journal 41(6):1131–1137. https://doi.org/10.2514/2.205 -- [10.2514/2.2054](https://doi.org/10.2514/2.2054)
- [Thoma T, Kotyczka P, Egger H (2024) On the velocity-stress formulation for geometrically nonlinear elastodynamics and its structure-preserving discretization. Mathematical and Computer Modelling of Dynamical Systems 30(1):701–720. https://doi.org/10.1080/13873954.2024.239748](on-the-velocity-stress-formulation-for-geometrically-nonlinear-elastodynamics-and-its-structure-preserving-discretization) -- [10.1080/13873954.2024.2397486](https://doi.org/10.1080/13873954.2024.2397486)
- Hairer E, Hochbruck M, Iserles A, Lubich C (2006) Geometric Numerical Integration. Oberwolfach Rep 3(1):805–882. https://doi.org/10.4171/owr/2006/1 -- [10.4171/owr/2006/14](https://doi.org/10.4171/owr/2006/14)
- Geuzaine C, Remacle J (2009) Gmsh: A 3‐D finite element mesh generator with built‐in pre‐ and post‐processing facilities. Numerical Meth Engineering 79(11):1309–1331. https://doi.org/10.1002/nme.257 -- [10.1002/nme.2579](https://doi.org/10.1002/nme.2579)
- Rathgeber F, Ham DA, Mitchell L, Lange M, Luporini F, Mcrae ATT, Bercea G-T, Markall GR, Kelly PHJ (2016) Firedrake. ACM Trans Math Softw 43(3):1–27. https://doi.org/10.1145/299844 -- [10.1145/2998441](https://doi.org/10.1145/2998441)
- Hante S, Tumiotto D, Arnold M (2021) A Lie group variational integration approach to the full discretization of a constrained geometrically exact Cosserat beam model. Multibody Syst Dyn 54(1):97–123. https://doi.org/10.1007/s11044-021-09807- -- [10.1007/s11044-021-09807-8](https://doi.org/10.1007/s11044-021-09807-8)
- Badia S, Codina R, Espinoza H (2014) Stability, Convergence, and Accuracy of Stabilized Finite Element Methods for the Wave Equation in Mixed Form. SIAM J Numer Anal 52(4):1729–1752. https://doi.org/10.1137/13091870 -- [10.1137/130918708](https://doi.org/10.1137/130918708)
- Grote MJ, Schneebeli A, Schötzau D (2006) Discontinuous Galerkin Finite Element Method for the Wave Equation. SIAM J Numer Anal 44(6):2408–2431. https://doi.org/10.1137/05063194 -- [10.1137/05063194x](https://doi.org/10.1137/05063194x)
- Arnold DN, Winther R (2002) Mixed finite elements for elasticity. Numerische Mathematik 92(3):401–419. https://doi.org/10.1007/s00211010034 -- [10.1007/s002110100348](https://doi.org/10.1007/s002110100348)
- {"status":"error" -- [10.1016/0022-460x(80)90477-0](https://doi.org/10.1016/0022-460x(80)90477-0)

