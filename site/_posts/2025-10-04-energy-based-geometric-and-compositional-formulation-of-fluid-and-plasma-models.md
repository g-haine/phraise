---
title: "Energy-based, geometric, and compositional formulation of fluid and plasma models"
date: 2025-10-04 00:00:00 +0100
permalink: energy-based-geometric-and-compositional-formulation-of-fluid-and-plasma-models
year: 2026
authors: Markus Lohmayer, Michael Kraus, Sigrid Leyendecker
category: articles
tags:
  - bond graphs, compositionality, exterior calculus, generic formalism, graphical syntax, magnetohydrodynamics, metriplectic systems, modeling language, multiphysics, navier-stokes-fourier fluid, nonequilibrium thermodynamics, port-hamiltonian systems, undirected wiring diagrams
---
 
## Authors
[Markus Lohmayer](authors/markus-lohmayer), [Michael Kraus](authors/michael-kraus), [Sigrid Leyendecker](authors/sigrid-leyendecker)
 
## Abstract
Fluid dynamics plays a crucial role in various multiphysics applications, including energy systems, electronics cooling, and biomedical engineering. Developing models for complex, coupled systems can be challenging and time-consuming. In particular, ensuring the consistent integration of models from diverse physical domains requires meticulous attention. Considering the example of (electro-)magneto-hydrodynamics (on a fixed spatial domain and with linear polarization and magnetization), this article demonstrates how relatively complex models can be composed from simpler parts by means of a formal language for multiphysics modeling. The Exergetic Port-Hamiltonian Systems (EPHS) modeling language features a simple graphical syntax for expressing the energy-based interconnection of subsystems. This reduces cognitive load and facilitates communication, especially in multidisciplinary environments. As the example demonstrates, existing models can be easily integrated as subsystems of new models. Specifically, an ideal fluid model is used as a subsystem of a Navier-Stokes-Fourier fluid model, which in turn is reused as a subsystem of a magneto-hydrodynamics model. The energy-based, compositional approach simplifies understanding complex models, and it makes it easy to encapsulate, reuse, and replace their constituents. Moreover, structural properties of EPHS guarantee fundamental properties of thermodynamic systems, such as conservation of energy, non-negative entropy production, and Onsager reciprocal relations.
 
## Keywords
bond graphs, compositionality, exterior calculus, generic formalism, graphical syntax, magnetohydrodynamics, metriplectic systems, modeling language, multiphysics, navier-stokes-fourier fluid, nonequilibrium thermodynamics, port-hamiltonian systems, undirected wiring diagrams
 
## Citation
- **Journal:** Communications in Nonlinear Science and Numerical Simulation
- **Year:** 2026
- **Volume:** 152
- **Issue:** 
- **Pages:** 109384
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.cnsns.2025.109384](https://doi.org/10.1016/j.cnsns.2025.109384)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Lohmayer_2026,
  title={{Energy-based, geometric, and compositional formulation of fluid and plasma models}},
  volume={152},
  ISSN={1007-5704},
  DOI={10.1016/j.cnsns.2025.109384},
  journal={Communications in Nonlinear Science and Numerical Simulation},
  publisher={Elsevier BV},
  author={Lohmayer, Markus and Kraus, Michael and Leyendecker, Sigrid},
  year={2026},
  pages={109384}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/energy-based-geometric-and-compositional-formulation-of-fluid-and-plasma-models.bib)
 
## References
- Lohmayer M., Lynch O., Leyendecker S.. Exergetic port-Hamiltonian systems modeling language. 2025. 10.48550/ARXIV.2402.17640.
- Lohmayer, Exergetic port-Hamiltonian systems for multibody dynamics. Multibody Syst Dyn (2024)
- Lohmayer M.. EPHS.jl – a compositional, energy-based software framework for modeling mechanical, electromagnetic, and thermodynamic systems. 2025. https://MarkusLohmayer.github.io/EPHS.jl.
- Tonti E (2014) Why starting from differential equations for computational physics? Journal of Computational Physics 257:1260–1290. https://doi.org/10.1016/j.jcp.2013.08.016 -- [10.1016/j.jcp.2013.08.016](https://doi.org/10.1016/j.jcp.2013.08.016)
- Hirani, (2003)
- Arnold D, Falk R, Winther R (2010) Finite element exterior calculus: from Hodge theory to numerical stability. Bull Amer Math Soc 47(2):281–354. https://doi.org/10.1090/s0273-0979-10-01278-4 -- [10.1090/s0273-0979-10-01278-4](https://doi.org/10.1090/s0273-0979-10-01278-4)
- Pavlov D, Mullen P, Tong Y, Kanso E, Marsden JE, Desbrun M (2011) Structure-preserving discretization of incompressible fluids. Physica D: Nonlinear Phenomena 240(6):443–458. https://doi.org/10.1016/j.physd.2010.10.012 -- [10.1016/j.physd.2010.10.012](https://doi.org/10.1016/j.physd.2010.10.012)
- Couéraud B., Gay-Balmaz F.. Variational discretization of the Navier-Stokes-Fourier system. 2022. 10.48550/arXiv.2202.03502.
- Karnopp, (2012)
- Borutzky, (2010)
- Morrison PJ (1986) A paradigm for joined Hamiltonian and dissipative systems. Physica D: Nonlinear Phenomena 18(1–3):410–419. https://doi.org/10.1016/0167-2789(86)90209-5 -- [10.1016/0167-2789(86)90209-5](https://doi.org/10.1016/0167-2789(86)90209-5)
- Öttinger, (2005)
- Pavelka, (2018)
- Modeling and control of complex physical systems. (2009)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Spivak D.I.. The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits. 2013. 10.48550/ARXIV.1305.0297.
- Fong, (2019)
- Myers D.J.. Categorical systems theory. http://davidjaz.com/Papers/DynamicalBook.pdf; 2023.
- Arnold V (1966) Sur la géométrie différentielle des groupes de Lie de dimension infinie et ses applications à l’hydrodynamique des fluides parfaits. Annales de l’Institut Fourier 16(1):319–361. https://doi.org/10.5802/aif.233 -- [10.5802/aif.233](https://doi.org/10.5802/aif.233)
- Arnold, Hamiltonian nature of the Euler equations in the dynamics of a rigid body and of an ideal fluid. Usp Mat Nauk (1969)
- Marsden J, Abraham R (1970) Hamiltonian mechanics on Lie groups and hydrodynamics. Proceedings of Symposia in Pure Mathematics 237–244 -- [10.1090/pspum/016/9980](https://doi.org/10.1090/pspum/016/9980)
- Ebin DG, Marsden J (1970) Groups of Diffeomorphisms and the Motion of an Incompressible Fluid. The Annals of Mathematics 92(1):102. https://doi.org/10.2307/1970699 -- [10.2307/1970699](https://doi.org/10.2307/1970699)
- Marsden, (1999)
- Marsden JE, Ratiu T, Weinstein A (1984) Reduction and Hamiltonian structures on duals of semidirect product Lie algebras. Contemporary Mathematics 55–100 -- [10.1090/conm/028/751975](https://doi.org/10.1090/conm/028/751975)
- Marsden JE, Raţiu T, Weinstein A (1984) Semidirect products and reduction in mechanics. Trans Amer Math Soc 281(1):147–177. https://doi.org/10.1090/s0002-9947-1984-0719663-1 -- [10.1090/s0002-9947-1984-0719663-1](https://doi.org/10.1090/s0002-9947-1984-0719663-1)
- [van der Schaft AJ, Maschke BM (2002) Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42(1–2):166–194. https://doi.org/10.1016/s0393-0440(01)00083-3](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- van der Schaft, Fluid dynamical systems as Hamiltonian boundary control systems. (2001)
- Rashad, Port-Hamiltonian modeling of ideal fluid flow: part I. Foundations and kinetic energy. J Geom Phys (2021)
- Rashad, Port-Hamiltonian modeling of ideal fluid flow: part II. Compressible and incompressible flow. J Geom Phys (2021)
- [Califano F, Rashad R, Schuller FP, Stramigioli S (2021) Geometric and energy-aware decomposition of the Navier–Stokes equations: A port-Hamiltonian approach. Physics of Fluids 33(4). https://doi.org/10.1063/5.0048359](geometric-and-energy-aware-decomposition-of-the-navier-stokes-equations-a-port-hamiltonian-approach) -- [10.1063/5.0048359](https://doi.org/10.1063/5.0048359)
- Lohmayer, Exergetic port-Hamiltonian systems: Navier-Stokes-Fourier fluid. (2022)
- [Lohmayer M, Kotyczka P, Leyendecker S (2021) Exergetic port-Hamiltonian systems: modelling basics. Mathematical and Computer Modelling of Dynamical Systems 27(1):489–521. https://doi.org/10.1080/13873954.2021.1979592](exergetic-port-hamiltonian-systems-modelling-basics) -- [10.1080/13873954.2021.1979592](https://doi.org/10.1080/13873954.2021.1979592)
- Grmela M, Öttinger HC (1997) Dynamics and thermodynamics of complex fluids.  I. Development of a general formalism. Phys Rev E 56(6):6620–6632. https://doi.org/10.1103/physreve.56.6620 -- [10.1103/physreve.56.6620](https://doi.org/10.1103/physreve.56.6620)
- [Marsden JE, Weinstein A (1982) The Hamiltonian structure of the Maxwell-Vlasov equations. Physica D: Nonlinear Phenomena 4(3):394–406. https://doi.org/10.1016/0167-2789(82)90043-4](the-hamiltonian-structure-of-the-maxwell-vlasov-equations) -- [10.1016/0167-2789(82)90043-4](https://doi.org/10.1016/0167-2789(82)90043-4)
- Hirvijoki E, Burby JW, Brizard AJ (2022) Metriplectic foundations of gyrokinetic Vlasov–Maxwell–Landau theory. Physics of Plasmas 29(6). https://doi.org/10.1063/5.0091727 -- [10.1063/5.0091727](https://doi.org/10.1063/5.0091727)
- Spencer RG, Kaufman AN (1982) Hamiltonian structure of two-fluid plasma dynamics. Phys Rev A 25(4):2437–2439. https://doi.org/10.1103/physreva.25.2437 -- [10.1103/physreva.25.2437](https://doi.org/10.1103/physreva.25.2437)
- Morrison PJ, Greene JM (1980) Noncanonical Hamiltonian Density Formulation of Hydrodynamics and Ideal Magnetohydrodynamics. Phys Rev Lett 45(10):790–794. https://doi.org/10.1103/physrevlett.45.790 -- [10.1103/physrevlett.45.790](https://doi.org/10.1103/physrevlett.45.790)
- Gilbert AD, Vanneste J (2020) A geometric look at MHD and the Braginsky dynamo. Geophysical & Astrophysical Fluid Dynamics 115(4):436–471. https://doi.org/10.1080/03091929.2020.1839896 -- [10.1080/03091929.2020.1839896](https://doi.org/10.1080/03091929.2020.1839896)
- Materassi M, Tassi E (2012) Metriplectic framework for dissipative magneto-hydrodynamics. Physica D: Nonlinear Phenomena 241(6):729–734. https://doi.org/10.1016/j.physd.2011.12.013 -- [10.1016/j.physd.2011.12.013](https://doi.org/10.1016/j.physd.2011.12.013)
- Coquinot B, Morrison PJ (2020) A general metriplectic framework with application to dissipative extended magnetohydrodynamics. J Plasma Phys 86(3). https://doi.org/10.1017/s0022377820000392 -- [10.1017/s0022377820000392](https://doi.org/10.1017/s0022377820000392)
- Gilbert AD, Vanneste J (2023) A Geometric Look at Momentum Flux and Stress in Fluid Mechanics. J Nonlinear Sci 33(2). https://doi.org/10.1007/s00332-023-09887-0 -- [10.1007/s00332-023-09887-0](https://doi.org/10.1007/s00332-023-09887-0)
- Kanso E, Arroyo M, Tong Y, Yavari A, Marsden JG, Desbrun M (2007) On the geometric character of stress in continuum mechanics. Z angew Math Phys 58(5):843–856. https://doi.org/10.1007/s00033-007-6141-8 -- [10.1007/s00033-007-6141-8](https://doi.org/10.1007/s00033-007-6141-8)
- Arnold DN, Hu K (2021) Complexes from Complexes. Found Comput Math 21(6):1739–1774. https://doi.org/10.1007/s10208-021-09498-9 -- [10.1007/s10208-021-09498-9](https://doi.org/10.1007/s10208-021-09498-9)
- Crane K.. Discrete Differential Geometry (lecture series). 2021. https://www.youtube.com/playlist?list=PL9_jI1bdZmz0hIrNCMQW1YmZysAiIYSSS.
- Lee, (2012)
- Abraham, (1988)
- Burke, (1985)
- Ramanan, (2005)
- Öttinger HC (2006) Nonequilibrium thermodynamics for open systems. Phys Rev E 73(3). https://doi.org/10.1103/physreve.73.036126 -- [10.1103/physreve.73.036126](https://doi.org/10.1103/physreve.73.036126)

