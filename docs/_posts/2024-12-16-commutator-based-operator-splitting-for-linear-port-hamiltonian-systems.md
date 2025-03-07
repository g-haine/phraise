---
layout: post
title: "Commutator-based operator splitting for linear port-Hamiltonian systems"
date: 2024-12-16 00:00:00 +0100
permalink: commutator-based-operator-splitting-for-linear-port-hamiltonian-systems
year: 2025
authors: Marius Mönch, Nicole Marheineke
category: articles
tags:
  - Operator splitting schemes
  - Port-Hamiltonian systems
  - Dissipation inequality
  - Commutator-based methods
  - Force gradient
  - Structure-preservation
---
 
## Authors
[Marius Mönch](authors/marius_monch), [Nicole Marheineke](authors/nicole_marheineke)
 
## Abstract
In this paper, we develop high-order splitting methods for linear port-Hamiltonian systems, focusing on preserving their intrinsic structure, particularly the dissipation inequality. Port-Hamiltonian systems are characterized by their ability to describe energy-conserving and dissipative processes, which is essential for the accurate simulation of physical systems. For autonomous systems, we introduce an energy-associated decomposition that exploits the system's energy properties. We present splitting schemes up to order six. In the non-autonomous case, we employ a port-based splitting. This special technique makes it possible to set up methods of arbitrary even order. Both splitting approaches are based on the properties of the commutator and ensure that the numerical schemes not only preserve the structure of the system but also faithfully fulfill the dissipation inequality. The proposed approaches are validated through theoretical analysis and numerical experiments.
 
## Keywords
Operator splitting schemes; Port-Hamiltonian systems; Dissipation inequality; Commutator-based methods; Force gradient; Structure-preservation
 
## Citation
- **Journal:** Applied Numerical Mathematics
- **Year:** 2025
- **Volume:** 210
- **Issue:** 
- **Pages:** 25--38
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.apnum.2024.12.007](https://doi.org/10.1016/j.apnum.2024.12.007)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{M_nch_2025,
  title={{Commutator-based operator splitting for linear port-Hamiltonian systems}},
  volume={210},
  ISSN={0168-9274},
  DOI={10.1016/j.apnum.2024.12.007},
  journal={Applied Numerical Mathematics},
  publisher={Elsevier BV},
  author={Mönch, Marius and Marheineke, Nicole},
  year={2025},
  pages={25--38}
}
{% endraw %}
{% endhighlight %}
 
## References
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/S0962492922000083](https://doi.org/10.1017/S0962492922000083)
- Blanes, S., Casas, F. & Murua, A. Splitting methods for differential equations. Acta Numerica vol. 33 1–161 (2024) -- [10.1017/S0962492923000077](https://doi.org/10.1017/S0962492923000077)
- McLachlan, R. I. & Quispel, G. R. W. Splitting methods. Acta Numerica vol. 11 341–434 (2002) -- [10.1017/S0962492902000053](https://doi.org/10.1017/S0962492902000053)
- Blanes, S. & Casas, F. On the necessity of negative coefficients for operator splitting schemes of order higher than two. Applied Numerical Mathematics vol. 54 23–37 (2005) -- [10.1016/j.apnum.2004.10.005](https://doi.org/10.1016/j.apnum.2004.10.005)
- Celledoni, E., Høiseth, E. H. & Ramzina, N. Passivity-preserving splitting methods for rigid body systems. Multibody System Dynamics vol. 44 251–275 (2018) -- [10.1007/s11044-018-9628-5](https://doi.org/10.1007/s11044-018-9628-5)
- Blanes, S., Casas, F. & Murua, A. Splitting methods with complex coefficients. SeMA Journal vol. 50 47–60 (2010) -- [10.1007/BF03322541](https://doi.org/10.1007/BF03322541)
- Castella, F., Chartier, P., Descombes, S. & Vilmart, G. Splitting methods with complex times for parabolic equations. BIT Numerical Mathematics vol. 49 487–508 (2009) -- [10.1007/s10543-009-0235-y](https://doi.org/10.1007/s10543-009-0235-y)
- Hansen, E. & Ostermann, A. High order splitting methods for analytic semigroups exist. BIT Numerical Mathematics vol. 49 527–542 (2009) -- [10.1007/s10543-009-0236-x](https://doi.org/10.1007/s10543-009-0236-x)
- Kieri, E. Stiff convergence of force-gradient operator splitting methods. Applied Numerical Mathematics vol. 94 33–45 (2015) -- [10.1016/j.apnum.2015.03.005](https://doi.org/10.1016/j.apnum.2015.03.005)
- Omelyan, I. P., Mryglod, I. M. & Folk, R. Construction of high-order force-gradient algorithms for integration of motion in classical and quantum systems. Physical Review E vol. 66 (2002) -- [10.1103/PhysRevE.66.026701](https://doi.org/10.1103/PhysRevE.66.026701)
- Chin, S. A. & Chen, C. R. Fourth order gradient symplectic integrator methods for solving the time-dependent Schrödinger equation. The Journal of Chemical Physics vol. 114 7338–7341 (2001) -- [10.1063/1.1362288](https://doi.org/10.1063/1.1362288)
- Chin, S. A. & Kidwell, D. W. Higher-order force gradient symplectic algorithms. Physical Review E vol. 62 8746–8752 (2000) -- [10.1103/PhysRevE.62.8746](https://doi.org/10.1103/PhysRevE.62.8746)
- Shcherbakov, D., Ehrhardt, M., Günther, M. & Peardon, M. Force-gradient nested multirate methods for Hamiltonian systems. Computer Physics Communications vol. 187 91–97 (2015) -- [10.1016/j.cpc.2014.10.014](https://doi.org/10.1016/j.cpc.2014.10.014)
- Shcherbakov, D. et al. Adapted Nested Force-Gradient Integrators: The Schwinger Model Case. Communications in Computational Physics vol. 21 1141–1153 (2017) -- [10.4208/cicp.OA-2016-0048](https://doi.org/10.4208/cicp.OA-2016-0048)
- Chin, S. A. Structure of positive decompositions of exponential operators. Physical Review E vol. 71 (2005) -- [10.1103/PhysRevE.71.016703](https://doi.org/10.1103/PhysRevE.71.016703)
- Blanes, S. & Casas, F. Splitting methods for non-autonomous separable dynamical systems. Journal of Physics A: Mathematical and General vol. 39 5405–5423 (2006) -- [10.1088/0305-4470/39/19/S05](https://doi.org/10.1088/0305-4470/39/19/S05)
- Blanes, S., Diele, F., Marangi, C. & Ragni, S. Splitting and composition methods for explicit time dependence in separable dynamical systems. Journal of Computational and Applied Mathematics vol. 235 646–659 (2010) -- [10.1016/j.cam.2010.06.018](https://doi.org/10.1016/j.cam.2010.06.018)
- Blanes, S. & Ponsoda, E. Time-averaging and exponential integrators for non-homogeneous linear IVPs and BVPs. Applied Numerical Mathematics vol. 62 875–894 (2012) -- [10.1016/j.apnum.2012.02.001](https://doi.org/10.1016/j.apnum.2012.02.001)
- Faou, E., Ostermann, A. & Schratz, K. Analysis of exponential splitting methods for inhomogeneous parabolic equations. IMA Journal of Numerical Analysis vol. 35 161–178 (2014) -- [10.1093/imanum/dru002](https://doi.org/10.1093/imanum/dru002)
- Ostermann, A. & Schratz, K. Error analysis of splitting methods for inhomogeneous evolution equations. Applied Numerical Mathematics vol. 62 1436–1446 (2012) -- [10.1016/j.apnum.2012.06.002](https://doi.org/10.1016/j.apnum.2012.06.002)
- McLachlan, R. I. On the Numerical Integration of Ordinary Differential Equations by Symmetric Composition Methods. SIAM Journal on Scientific Computing vol. 16 151–168 (1995) -- [10.1137/0916010](https://doi.org/10.1137/0916010)
- Mönch, M. & Marheineke, N. Fourth‐order force‐gradient splitting for linear port‐Hamiltonian systems. PAMM vol. 24 (2024) -- [10.1002/pamm.202400132](https://doi.org/10.1002/pamm.202400132)
- Suzuki, M. General theory of fractal path integrals with applications to many-body theories and statistical physics. Journal of Mathematical Physics vol. 32 400–407 (1991) -- [10.1063/1.529425](https://doi.org/10.1063/1.529425)
- Virtanen, P. et al. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nature Methods vol. 17 261–272 (2020) -- [10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2)
- Campos, C. M. & Sanz-Serna, J. M. Palindromic 3-stage splitting integrators, a roadmap. Journal of Computational Physics vol. 346 340–355 (2017) -- [10.1016/j.jcp.2017.06.006](https://doi.org/10.1016/j.jcp.2017.06.006)

