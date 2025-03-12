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
- **DOI:** [10.1134/s0965542523010104](https://doi.org/10.1134/s0965542523010104)
 
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
 
[Download the bib file]({{ site.baseurl }}/assets/bib/learning-port-hamiltonian-systems-algorithms.bib)
 
## References
- Salnikov, V., Hamdouni, A. & Loziienko, D. Generalized and graded geometry for mechanics: a comprehensive introduction. Mathematics and Mechanics of Complex Systems vol. 9 59–75 (2021) -- [10.2140/memocs.2021.9.59](https://doi.org/10.2140/memocs.2021.9.59)
- Verlet, L. Computer ‘Experiments’ on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules. Physical Review vol. 159 98–103 (1967) -- [10.1103/physrev.159.98](https://doi.org/10.1103/physrev.159.98)
- Yoshida, H. Construction of higher order symplectic integrators. Physics Letters A vol. 150 262–268 (1990) -- [10.1016/0375-9601(90)90092-3](https://doi.org/10.1016/0375-9601(90)90092-3)
- Cosserat, O. Symplectic groupoids for Poisson integrators. Journal of Geometry and Physics vol. 186 104751 (2023) -- [10.1016/j.geomphys.2023.104751](https://doi.org/10.1016/j.geomphys.2023.104751)
- H. M. Paynter. H. M. Paynter, Analysis and Design of Engineering Systems (MIT, Cambridge, Massachusetts, 1961). (1961)
- Maschke, B. M., Van Der Schaft, A. J. & Breedveld, P. C. An intrinsic hamiltonian formulation of network dynamics: non-standard poisson structures and gyrators. Journal of the Franklin Institute vol. 329 923–966 (1992) -- [10.1016/s0016-0032(92)90049-m](https://doi.org/10.1016/s0016-0032(92)90049-m)
- [van der Schaft, A. Port-Hamiltonian systems: an introductory survey. Proceedings of the International Congress of Mathematicians Madrid, August 22–30, 2006 1339–1365 (2007) doi:10.4171/022-3/65](port-hamiltonian-systems-an-introductory-survey) -- [10.4171/022-3/65](https://doi.org/10.4171/022-3/65)
- O. Cosserat, C. Laurent-Gengoux, A. Kotov, L. Ryvkin, and V. Salnikov, “On Dirac structures admitting a variational approach,” Preprint (2021). arXiv:2109.00313
- A. Falaize, PhD Thesis (Télécommun. Électron. de Paris, Univ. Pierre et Marie Curie, Paris, 2016).
- [Salnikov, V. N. & Hamdouni, A. Differential Geometry and Mechanics: A Source for Computer Algebra Problems. Programming and Computer Software vol. 46 126–132 (2020)](differential-geometry-and-mechanics-a-source-for-computer-algebra-problems) -- [10.1134/s0361768820020097](https://doi.org/10.1134/s0361768820020097)
- V. Salnikov, A. Falaize, and D. Loziienko, “Learning port-Hamiltonian systems: Applications” (in preparation).
- Arnold, V. I. Mathematical Methods of Classical Mechanics. Graduate Texts in Mathematics (Springer New York, 1989). doi:10.1007/978-1-4757-2063-1 -- [10.1007/978-1-4757-2063-1](https://doi.org/10.1007/978-1-4757-2063-1)
- A. Cannas Da Silva. A. Cannas Da Silva and A. Weinstein, Geometric Models for Noncommutative Algebras (Am. Math. Soc., Providence, R.I., 2000). (2000)
- A. Falaize. A. Falaize and T. Hélie, “Passive guaranteed simulation of analog audio circuits: A port-Hamiltonian approach,” Appl. Sci. Appl. Acoust. 6 (10), 273 (2016). (2016)
- [Falaize, A. & Hélie, T. Passive simulation of the nonlinear port-Hamiltonian modeling of a Rhodes Piano. Journal of Sound and Vibration vol. 390 289–309 (2017)](passive-simulation-of-the-nonlinear-port-hamiltonian-modeling-of-a-rhodes-piano) -- [10.1016/j.jsv.2016.11.008](https://doi.org/10.1016/j.jsv.2016.11.008)
- Evripidou, C. A., Kassotakis, P. & Vanhaecke, P. Integrable deformations of the Bogoyavlenskij–Itoh Lotka–Volterra systems. Regular and Chaotic Dynamics vol. 22 721–739 (2017) -- [10.1134/s1560354717060090](https://doi.org/10.1134/s1560354717060090)
- Leclercq, T. & de Langre, E. Vortex-induced vibrations of cylinders bent by the flow. Journal of Fluids and Structures vol. 80 77–93 (2018) -- [10.1016/j.jfluidstructs.2018.03.008](https://doi.org/10.1016/j.jfluidstructs.2018.03.008)
- [Salnikov, V. N. & Hamdouni, A. Differential Geometry and Mechanics: A Source for Computer Algebra Problems. Programming and Computer Software vol. 46 126–132 (2020)](differential-geometry-and-mechanics-a-source-for-computer-algebra-problems) -- [10.1134/s0361768820020097](https://doi.org/10.1134/s0361768820020097)

