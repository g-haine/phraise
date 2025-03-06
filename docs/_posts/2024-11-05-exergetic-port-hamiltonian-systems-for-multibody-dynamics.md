---
layout: post
title: "Exergetic port-Hamiltonian systems for multibody dynamics"
date: 2024-11-05 00:00:00 +0100
permalink: exergetic-port-hamiltonian-systems-for-multibody-dynamics
year: 2024
authors: Markus Lohmayer, Giuseppe Capobianco, Sigrid Leyendecker
category:
  - articles
tags:
  - compositionality
  - modeling language
  - multibody systems
  - multiphysics
  - rigid body dynamics
  - thermodynamic consistency
  - variational principle
---
 
## Authors
[Markus Lohmayer](authors/markus_lohmayer), [Giuseppe Capobianco](authors/giuseppe_capobianco), [Sigrid Leyendecker](authors/sigrid_leyendecker)
 
## Abstract
Multibody dynamics simulation plays an important role in various fields, including mechanical engineering, robotics, and biomechanics. Setting up computational models however becomes increasingly challenging as systems grow in size and complexity. Especially the consistent combination of models across different physical domains still requires significant effort. This motivates the study of formal languages that enable a compositional approach to modeling multiphysical systems with basic guarantees. The paper shows how multibody systems, or more precisely assemblies of rigid bodies connected by lower kinematic pairs, can be described as Exergetic Port-Hamiltonian Systems (EPHS). The EPHS modeling language features a straightforward graphical syntax for expressing the energy-based interconnection of hierarchically nested subsystems. This reduces cognitive load and facilitates clearer communication among experts, nonexperts, and computational tools. Hierarchical nesting of systems enables abstraction of lower-level details and promotes the reuse of models at different levels of complexity. At the lowest level, there are three basic kinds of systems, representing energy storage and reversible/irreversible energy exchange. The structured approach guarantees fundamental properties of macroscopic systems, such as conservation of energy and nonnegative entropy production. In combination with the compositional syntax, this makes building and modifying models simpler and less error-prone.
 
## Keywords
Compositionality; Modeling language; Multibody systems; Multiphysics; Rigid body dynamics; Thermodynamic consistency; Variational principle
 
## Citation
- **Journal:** Multibody System Dynamics
- **Year:** 2024
- **Volume:** 
- **Issue:** 
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s11044-024-10038-w](https://doi.org/10.1007/s11044-024-10038-w)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Lohmayer_2024,
  title={{Exergetic port-Hamiltonian systems for multibody dynamics}},
  ISSN={1573-272X},
  DOI={10.1007/s11044-024-10038-w},
  journal={Multibody System Dynamics},
  publisher={Springer Science and Business Media LLC},
  author={Lohmayer, Markus and Capobianco, Giuseppe and Leyendecker, Sigrid},
  year={2024}
}
{% endraw %}
{% endhighlight %}
 
## References
- Lohmayer, M., Lynch, O., Leyendecker, S.: Exergetic Port-Hamiltonian Systems Modeling Language (2024). https://doi.org/10.48550/ARXIV.2402.17640 -- [10.48550/ARXIV.2402.17640](https://doi.org/10.48550/ARXIV.2402.17640)
- Sonneville, V., Brüls, O.: A formulation on the special Euclidean group for dynamic analysis of multibody SYstems. J. Comput. Nonlinear Dyn. 9(4) (2014). https://doi.org/10.1115/1.4026569 -- [10.1115/1.4026569](https://doi.org/10.1115/1.4026569)
- Sonneville, V.: A geometric local frame approach for flexible multibody systems. Ph.D. thesis, Université de Liège (2015)
- Stramigioli, S.: Modeling and IPC Control of Interactive Mechanical Systems — a Coordinate-Free Approach. Springer, London (2001). https://doi.org/10.1007/bfb0110400 -- [10.1007/bfb0110400](https://doi.org/10.1007/bfb0110400)
- Macchelli, A., Melchiorri, C.: Port-based simulation of flexible multi-body systems. IFAC Proc. Vol. 41(2), 15672–15677 (2008). https://doi.org/10.3182/20080706-5-kr-1001.02650 -- [10.3182/20080706-5-kr-1001.02650](https://doi.org/10.3182/20080706-5-kr-1001.02650)
- Yoshimura, H., Marsden, J.E.: Dirac structures in Lagrangian mechanics, part II: variational structures. J. Geom. Phys. 57(1), 209–250 (2006). https://doi.org/10.1016/j.geomphys.2006.02.012 -- [10.1016/j.geomphys.2006.02.012](https://doi.org/10.1016/j.geomphys.2006.02.012)
- Bou-Rabee, N., Marsden, J.E.: Hamilton–Pontryagin integrators on Lie groups, part I: introduction and structure-preserving properties. Found. Comput. Math. 9(2), 197–219 (2008). https://doi.org/10.1007/s10208-008-9030-4 -- [10.1007/s10208-008-9030-4](https://doi.org/10.1007/s10208-008-9030-4)
- [Jacobs, H.O., Yoshimura, H.: Tensor products of Dirac structures and interconnection in Lagrangian mechanics. J. Geom. Mech. 6(1), 67–98 (2014). https://doi.org/10.3934/jgm.2014.6.67](tensor-products-of-dirac-structures-and-interconnection-in-lagrangian-mechanics) -- [10.3934/jgm.2014.6.67](https://doi.org/10.3934/jgm.2014.6.67)
- Gay-Balmaz, F., Yoshimura, H.: A Lagrangian variational formulation for nonequilibrium thermodynamics, part I: discrete systems. J. Geom. Phys. 111, 169–193 (2017). https://doi.org/10.1016/j.geomphys.2016.08.018 -- [10.1016/j.geomphys.2016.08.018](https://doi.org/10.1016/j.geomphys.2016.08.018)
- Gay-Balmaz, F., Yoshimura, H.: Dirac structures and variational formulation of port-Dirac systems in nonequilibrium thermodynamics. IMA J. Math. Control Inf. 37(4), 1298–1347 (2020). https://doi.org/10.1093/imamci/dnaa015 -- [10.1093/imamci/dnaa015](https://doi.org/10.1093/imamci/dnaa015)
- Lee, J.M.: Introduction to Smooth Manifolds, 2nd edn. Springer, New York (2012). https://doi.org/10.1007/978-1-4419-9982-5 -- [10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5)
- Marsden, J.E., Ratiu, T.S.: Introduction to Mechanics and Symmetry. Springer, New York (1999). https://doi.org/10.1007/978-0-387-21792-5 -- [10.1007/978-0-387-21792-5](https://doi.org/10.1007/978-0-387-21792-5)
- Abraham, R., Marsden, J.E., Ratiu, T.: Manifolds, Tensor Analysis, and Applications, 2nd edn. Springer, New York (1988). https://doi.org/10.1007/978-1-4612-1029-0 -- [10.1007/978-1-4612-1029-0](https://doi.org/10.1007/978-1-4612-1029-0)
- Brüls, O., Arnold, M., Cardona, A.: Two Lie group formulations for dynamic multibody systems with large rotations. In: Volume 4: 8th International Conference on Multibody Systems, Nonlinear Dynamics, and Control, Parts A and B, ASMEDC (2011). https://doi.org/10.1115/detc2011-48132 -- [10.1115/detc2011-48132](https://doi.org/10.1115/detc2011-48132)
- Müller, A., Terze, Z.: The significance of the configuration space Lie group for the constraint satisfaction in numerical time integration of multibody systems. Mech. Mach. Theory 82, 173–202 (2014). https://doi.org/10.1016/j.mechmachtheory.2014.06.014 -- [10.1016/j.mechmachtheory.2014.06.014](https://doi.org/10.1016/j.mechmachtheory.2014.06.014)
- Marsden, J.E., Ratiu, T., Weinstein, A.: Reduction and Hamiltonian structures on duals of semidirect product Lie algebras. Contemp. Math. 28, 55–100 (1984) -- [10.1090/conm/028/751975](https://doi.org/10.1090/conm/028/751975)
- Marsden, J.E., Ratiu, T., Raugel, G.: Symplectic connections and the linearisation of Hamiltonian systems. Proc. R. Soc. Edinb., Sect. A, Math. 117(3–4), 329–380 (1991). https://doi.org/10.1017/s030821050002477x -- [10.1017/s030821050002477x](https://doi.org/10.1017/s030821050002477x)
- Bloch, A., Krishnaprasad, P.S., Marsden, J.E., Ratiu, T.S.: The Euler–Poincaré equations and double bracket dissipation. Commun. Math. Phys. 175(1), 1–42 (1996). https://doi.org/10.1007/bf02101622 -- [10.1007/bf02101622](https://doi.org/10.1007/bf02101622)

