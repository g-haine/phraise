---
layout: post
title: "Learning port-Hamiltonian Systems—Algorithms"
date: 2023-04-08 00:00:00 +0100
permalink: learning-port-hamiltonian-systems-algorithms
year: 2023
authors: V. Salnikov, A. Falaize, D. Lozienko
category: articles
tags:
  - symplectic structures
  - Poisson geometry
  - port-Hamiltonian systems
---
 
## Authors
[V. Salnikov](authors/v-salnikov), [A. Falaize](authors/antoine-falaize), [D. Lozienko](authors/d-lozienko)
 
## Abstract
 In this article we study the possibilities of recovering the structure of port-Hamiltonian systems starting from “unlabelled” ordinary differential equations describing mechanical systems. The algorithm we suggest solves the problem in two phases. It starts by constructing the connectivity structure of the system using machine learning methods – producing thus a graph of interconnected subsystems. Then this graph is enhanced by recovering the Hamiltonian structure of each subsystem as well as the corresponding ports. This second phase relies heavily on results from symplectic and Poisson geometry that we briefly sketch. And the precise solutions can be constructed using methods of computer algebra and symbolic computations. The algorithm permits to extend the port-Hamiltonian formalism to generic ordinary differential equations, hence introducing eventually a new concept of normal forms of ODEs.
 
## Keywords
symplectic structures; Poisson geometry; port-Hamiltonian systems
 
## Citation
- **Journal:** Computational Mathematics and Mathematical Physics
- **Year:** 2023
- **Volume:** 63
- **Issue:** 1
- **Pages:** 126--134
- **Publisher:** Pleiades Publishing Ltd
- **DOI:** [10.1134/S0965542523010104](https://doi.org/10.1134/S0965542523010104)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Salnikov_2023,
  title={{Learning port-Hamiltonian Systems—Algorithms}},
  volume={63},
  ISSN={1555-6662},
  DOI={10.1134/s0965542523010104},
  number={1},
  journal={Computational Mathematics and Mathematical Physics},
  publisher={Pleiades Publishing Ltd},
  author={Salnikov, V. and Falaize, A. and Lozienko, D.},
  year={2023},
  pages={126--134}
}
{% endraw %}
{% endhighlight %}
 
## References
- V. Salnikov, A. Hamdouni, and D. Loziienko, “Generalized and graded geometry for mechanics: A comprehensive introduction,” Math. Mech. Complex Syst. 9 (1), 59–75 (2021). -- [10.2140/memocs.2021.9.59](https://doi.org/10.2140/memocs.2021.9.59)
- L. Verlet, “Computer 'experiments' on classical fluids,” Phys. Rev. 159, 98–103 (1967). -- [10.1103/PhysRev.159.98](https://doi.org/10.1103/PhysRev.159.98)
- H. Yoshida, “Construction of higher order symplectic integrators,” Phys. Lett. A 150 (5–7), 262–268 (1990). -- [10.1016/0375-9601(90)90092-3](https://doi.org/10.1016/0375-9601(90)90092-3)
- O. Cosserat, “Symplectic groupoids for Poisson integrators” Preprint (2022). arXiv:2205.04838 -- [10.1016/j.geomphys.2023.104751](https://doi.org/10.1016/j.geomphys.2023.104751)
- H. M. Paynter, Analysis and Design of Engineering Systems (MIT, Cambridge, Massachusetts, 1961).
- B. M. Maschke, A. J. van der Schaft, and P. C. Breedveld, “An intrinsic Hamiltonian formulation of network dynamics: Non-standard Poisson structures and gyrators,” J. Franklin Inst. 329 (5), 923–966 (1992). -- [10.1016/S0016-0032(92)90049-M](https://doi.org/10.1016/S0016-0032(92)90049-M)
- [A. van der Schaft, “Port-Hamiltonian systems: An introductory survey,” Proceedings of the International Congress of Mathematicians, Madrid, 2006 (2006), Vol. 3, pp. 1339–1365.](port-hamiltonian-systems-an-introductory-survey) -- [10.4171/022-3/65](https://doi.org/10.4171/022-3/65)
- O. Cosserat, C. Laurent-Gengoux, A. Kotov, L. Ryvkin, and V. Salnikov, “On Dirac structures admitting a variational approach,” Preprint (2021). arXiv:2109.00313
- A. Falaize, PhD Thesis (Télécommun. Électron. de Paris, Univ. Pierre et Marie Curie, Paris, 2016).
- V. Salnikov and A. Hamdouni, “Differential geometry and mechanics: A source for computer algebra,” Program. Comput. Software 46 (2), 126–132 (2020). -- [10.1134/S0361768820020097](https://doi.org/10.1134/S0361768820020097)
- V. Salnikov, A. Falaize, and D. Loziienko, “Learning port-Hamiltonian systems: Applications” (in preparation).
- V. I. Arnold, Mathematical Methods of Classical Mechanics (Springer, Berlin, 1989). -- [10.1007/978-1-4757-2063-1](https://doi.org/10.1007/978-1-4757-2063-1)
- A. Cannas Da Silva and A. Weinstein, Geometric Models for Noncommutative Algebras (Am. Math. Soc., Providence, R.I., 2000).
- A. Falaize and T. Hélie, “Passive guaranteed simulation of analog audio circuits: A port-Hamiltonian approach,” Appl. Sci. Appl. Acoust. 6 (10), 273 (2016).
- [A. Falaize and T. Hélie, “Passive simulation of the nonlinear port-Hamiltonian modeling of a Rhodes Piano,” J. Sound Vib. 390, 289–309 (2017).](passive-simulation-of-the-nonlinear-port-hamiltonian-modeling-of-a-rhodes-piano) -- [10.1016/j.jsv.2016.11.008](https://doi.org/10.1016/j.jsv.2016.11.008)
- C. A. Evripidou, P. Kassotakis, and P. Vanhaecke, “Integrable deformations of the Bogoyavlenskij–Itoh Lotka–Volterra systems,” J. Regular Chaotic Dyn. 22, 721–739 (2017). -- [10.1134/S1560354717060090](https://doi.org/10.1134/S1560354717060090)
- T. Leclercq and E. de Langre, “Vortex-induced vibrations of cylinders bent by the flow,” J. Fluids Struct. 80, 77–93 (2018). -- [10.1016/j.jfluidstructs.2018.03.008](https://doi.org/10.1016/j.jfluidstructs.2018.03.008)
- V. Salnikov and A. Hamdouni, “Geometric integrators in mechanics—the need for computer algebra tools,” Proceedings of the Third International Conference “Computer Algebra” (Moscow, Russia, 2019), pp. 40–46. -- [10.1134/S0361768820020097](https://doi.org/10.1134/S0361768820020097)

