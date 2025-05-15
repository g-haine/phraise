---
layout: post
title: "An Object-Oriented Library for Heat Transfer Modelling and Simulation in Open Cell Foams"
date: 2021-04-15 00:00:00 +0100
permalink: an-object-oriented-library-for-heat-transfer-modelling-and-simulation-in-open-cell-foams
year: 2020
authors: Tobias M. Scheuermann, Paul Kotyczka, Christian Martens, Haithem Louati, Bernhard Maschke, Marie-Line Zanota, Isabelle Pitault
category: proceedings
tags:
  - Port-Hamiltonian systems
  - metallic foam
  - cell method
  - distributed parameter systems
  - discrete modeling
  - geometric discretization
  - process systems
  - simulation
---
 
## Authors
[Tobias M. Scheuermann](authors/tobias-m-scheuermann), [Paul Kotyczka](authors/paul-kotyczka), [Christian Martens](authors/christian-martens), [Haithem Louati](authors/haithem-louati), [Bernhard Maschke](authors/bernhard-maschke), [Marie-Line Zanota](authors/marie-line-zanota), [Isabelle Pitault](authors/isabelle-pitault)
 
## Abstract
Metallic open cell foams have multiple applications in industry, e.g. as catalyst supports in chemical processes. Their regular or heterogeneous microscopic structure determines the macroscopic thermodynamic and chemical properties. We present an object-oriented python library that generates state space models for simulation and control from the microscopic foam data, which can be imported from the image processing tool iMorph. The foam topology and the 3D geometric data are the basis for discrete modeling of the balance laws using the cell method. While the material structure imposes a primal chain complex to define discrete thermodynamic driving forces, the internal energy balance is evaluated on a second chain complex, which is constructed by topological duality. The heat exchange between the solid and the fluid phase is described based on the available surface data. We illustrate in detail the construction of the dual chain complexes, and we show how the structured discrete model directly maps to the software objects of the python code. As a test case, we present simulation results for a foam with a Kelvin cell structure, and compare them to a surrogate finite element model with homogeneous parameters.
 
## Keywords
Port-Hamiltonian systems; metallic foam; cell method; distributed parameter systems; discrete modeling; geometric discretization; process systems; simulation
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2020
- **Volume:** 53
- **Issue:** 2
- **Pages:** 7575--7580
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2020.12.1354](https://doi.org/10.1016/j.ifacol.2020.12.1354)
- **Note:** 21st IFAC World Congress- Berlin, Germany, 11–17 July 2020
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Scheuermann_2020,
  title={{An Object-Oriented Library for Heat Transfer Modelling and Simulation in Open Cell Foams}},
  volume={53},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2020.12.1354},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Scheuermann, Tobias M. and Kotyczka, Paul and Martens, Christian and Louati, Haithem and Maschke, Bernhard and Zanota, Marie-Line and Pitault, Isabelle},
  year={2020},
  pages={7575--7580}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/an-object-oriented-library-for-heat-transfer-modelling-and-simulation-in-open-cell-foams.bib)
 
## References
- Alnæs, The FEniCS project version 1.5. Archive of Numerical Software (2015)
- Alotto, (2013)
- Arnold, (1989)
- Duindam, (2009)
- Flanders, (1989)
- Frey, Open cell foam catalysts for CO2 methanation: Presentation of coating procedures and in situ exothermicity reaction study by infrared thermography. Catalysis Today (2016)
- Jänich, (2001)
- [Kotyczka, P. & Maschke, B. Discrete port-Hamiltonian formulation and numerical approximation for systems of two conservation laws. at - Automatisierungstechnik vol. 65 308–322 (2017)](discrete-port-hamiltonian-formulation-and-numerical-approximation-for-systems-of-two-conservation-laws) -- [10.1515/auto-2016-0098](https://doi.org/10.1515/auto-2016-0098)
- Quintard, M., Kaviany, M. & Whitaker, S. Two-medium treatment of heat transfer in porous media: numerical results for effective properties. Advances in Water Resources vol. 20 77–94 (1997) -- [10.1016/s0309-1708(96)00024-3](https://doi.org/10.1016/s0309-1708(96)00024-3)
- [Scheuermann, T. M. et al. Numerical Approximation of Heat Transfer on Heterogenous Media. PAMM vol. 19 (2019)](numerical-approximation-of-heat-transfer-on-heterogenous-media) -- [10.1002/pamm.201900372](https://doi.org/10.1002/pamm.201900372)
- [Seslija, M., Scherpen, J. M. A. & van der Schaft, A. Explicit simplicial discretization of distributed-parameter port-Hamiltonian systems. Automatica vol. 50 369–377 (2014)](explicit-simplicial-discretization-of-distributed-parameter-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.11.020](https://doi.org/10.1016/j.automatica.2013.11.020)
- Tonti, A direct discrete formulation of field laws: the cell method. Computer Modeling in Engineering and Sciences (2001)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM Journal on Control and Optimization vol. 51 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)

