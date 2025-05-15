---
layout: post
title: "Port-Hamiltonian Modeling of Multiphysics Systems and Object-Oriented Implementation With the Modelica Language"
date: 2020-06-08 00:00:00 +0100
permalink: port-hamiltonian-modeling-of-multiphysics-systems-and-object-oriented-implementation-with-the-modelica-language
year: 2020
authors: Francisco M. Marquez, Pedro J. Zufiria, Luis J. Yebra
category: articles
---
 
## Authors
[Francisco M. Marquez](authors/francisco-m-marquez), [Pedro J. Zufiria](authors/pedro-j-zufiria), [Luis J. Yebra](authors/luis-j-yebra)
 
## Abstract
In this article we present the implementation in Modelica language of a library with the fundamental components for modeling a wide variety of multiphysics systems. Modelica is an object-oriented modeling language, which allows to make a simple, systematic and elegant design of the library. The mechanisms of inheritance and composition of Modelica facilitate the modeling and reuse of components in different domains of Physics. To model the behavior of each component in a systematic framework we have used the theory of port-Hamiltonian systems, formulated mainly by means of differential geometry. The port-Hamiltonian approach allows a methodical definition of complex systems by connecting simple systems that exchange energy through connection ports. To graphically represent the components of a system and their connections, we have employed slightly modified bond graphs symbols for easier reading. The general and systematic applicability of the library is illustrated via two examples framed in different domains of Physics: the mechanical Sun-Earth-Moon system where we perform an analysis of errors that justifies the employed system of units, and the electrical nonlinear Chua circuit, modeled by composition of port-Hamiltonian subsystems. Both derived models have been built and simulated based on the more general models of mechanical and electrical systems, which are also part of the library developed with the port-Hamiltonian approach.
 
## Citation
- **Journal:** IEEE Access
- **Year:** 2020
- **Volume:** 8
- **Issue:** 
- **Pages:** 105980--105996
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/access.2020.3000129](https://doi.org/10.1109/access.2020.3000129)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Marquez_2020,
  title={{Port-Hamiltonian Modeling of Multiphysics Systems and Object-Oriented Implementation With the Modelica Language}},
  volume={8},
  ISSN={2169-3536},
  DOI={10.1109/access.2020.3000129},
  journal={IEEE Access},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Marquez, Francisco M. and Zufiria, Pedro J. and Yebra, Luis J.},
  year={2020},
  pages={105980--105996}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-modeling-of-multiphysics-systems-and-object-oriented-implementation-with-the-modelica-language.bib)
 
## References
- pfeifer, Automated generation of explicit port-Hamiltonian models from multi-bond graphs. arXiv 1909 02848 (2019)
- petzold, Description of DASSL: A differential/algebraic system solver. (1982)
- Lee, J. M. Introduction to Smooth Manifolds. Graduate Texts in Mathematics (Springer New York, 2012). doi:10.1007/978-1-4419-9982-5 -- [10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5)
- Kennedy, M. P. Three steps to chaos. II. A Chua’s circuit primer. IEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications vol. 40 657–674 (1993) -- [10.1109/81.246141](https://doi.org/10.1109/81.246141)
- Kennedy, M. P. Three steps to chaos. I. Evolution. IEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications vol. 40 640–656 (1993) -- [10.1109/81.246140](https://doi.org/10.1109/81.246140)
- Karnopp, D. C., Margolis, D. L. & Rosenberg, R. C. System Dynamics. (2012) doi:10.1002/9781118152812 -- [10.1002/9781118152812](https://doi.org/10.1002/9781118152812)
- paynter, Analysis and Design of Engineering Systems (1961)
- maks, A spinor approach to port-Hamiltonian systems. Proc 19th Int Symp Math Theory Netw Syst (MTNS) (2010)
- Luzum, B. et al. The IAU 2009 system of astronomical constants: the report of the IAU working group on numerical standards for Fundamental Astronomy. Celestial Mechanics and Dynamical Astronomy vol. 110 293–304 (2011) -- [10.1007/s10569-011-9352-4](https://doi.org/10.1007/s10569-011-9352-4)
- Lieb, E. H. & Yngvason, J. The physics and mathematics of the second law of thermodynamics. Physics Reports vol. 310 1–96 (1999) -- [10.1016/s0370-1573(98)00082-9](https://doi.org/10.1016/s0370-1573(98)00082-9)
- Cellier, F. E. Hierarchical non-linear bond graphs: a unified methodology for modeling complex physical systems. SIMULATION vol. 58 230–248 (1992) -- [10.1177/003754979205800404](https://doi.org/10.1177/003754979205800404)
- cellier, The Modelica bond graph library. Proc 4th Int Modelica Conf (2005)
- tellegen, The network element. Philips Res Rep (1948)
- [Cervera, J., van der Schaft, A. J. & Baños, A. Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica vol. 43 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- chua, The genesis of Chua&#x2019;s circuit. Int J Electron Commun (1992)
- [Courant, T. J. Dirac manifolds. Transactions of the American Mathematical Society vol. 319 631–661 (1990)](dirac-manifolds) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- dai, Compositional design of cyber-physical systems using port-Hamiltonian systems. (2016)
- [Dai, S., Lattmann, Z. & Koutsoukos, X. Compositional Design of Cyber-Physical Systems Using Port-Hamiltonian Systems. Cyber-Physical Systems 33–59 (2015) doi:10.1201/b19290-4](compositional-design-of-cyber-physical-systems-using-port-hamiltonian-systems0) -- [10.1201/b19290-4](https://doi.org/10.1201/b19290-4)
- [Dalsmo, M. & van der Schaft, A. On Representations and Integrability of Mathematical Structures in Energy-Conserving Physical Systems. SIAM Journal on Control and Optimization vol. 37 54–91 (1998)](on-representations-and-integrability-of-mathematical-structures-in-energy-conserving-physical-systems) -- [10.1137/s0363012996312039](https://doi.org/10.1137/s0363012996312039)
- Dymola&#x2013;Dynamic Modeling Laboratory&#x2013;User Manual 1B Developing and Simulating a Model (2019)
- calle, Improvements in BondLib, the modelica bond graph library. Proceedings of EuroSim Congress on Modeling and Simulation (2013)
- åström, Evolution of continuoustime modeling and simulation. Proc 12th Eur Simulation Multiconf (EMS) (1998)
- Husemoller, D. Fibre Bundles. Graduate Texts in Mathematics (Springer New York, 1994). doi:10.1007/978-1-4757-2261-1 -- [10.1007/978-1-4757-2261-1](https://doi.org/10.1007/978-1-4757-2261-1)
- Modelica&#x2014;A Unified Object-Oriented Language for Systems Modeling Language Specification Version 3 4 (2017)
- Holm, D. D., Schmah, T., Stoica, C. & Ellis, D. C. P. Geometric Mechanics and Symmetry. (2009) doi:10.1093/oso/9780199212903.001.0001 -- [10.1093/oso/9780199212903.001.0001](https://doi.org/10.1093/oso/9780199212903.001.0001)
- borutzky, Bond Graph Methodology Development and Analysis of Multidisciplinary Dynamic System Models (2010)
- [Batlle, C., Massana, I. & Simo, E. Representation of a general composition of Dirac structures. IEEE Conference on Decision and Control and European Control Conference 5199–5204 (2011) doi:10.1109/cdc.2011.6160588](representation-of-a-general-composition-of-dirac-structures) -- [10.1109/cdc.2011.6160588](https://doi.org/10.1109/cdc.2011.6160588)
- RESOLUTION B2: On the re-definition of the astronomical unit of length. Proc 28th Gen Assem Int Astronomical Union (IAU) (2012)
- brenan, Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations (1996)
- Breedveld, P. C. Multibond graph elements in physical systems theory. Journal of the Franklin Institute vol. 319 1–36 (1985) -- [10.1016/0016-0032(85)90062-6](https://doi.org/10.1016/0016-0032(85)90062-6)
- Arnold, V. I. Mathematical Methods of Classical Mechanics. Graduate Texts in Mathematics (Springer New York, 1989). doi:10.1007/978-1-4757-2063-1 -- [10.1007/978-1-4757-2063-1](https://doi.org/10.1007/978-1-4757-2063-1)
- brewer, Bond graphs of microeconomic systems (1977)
- abraham, Foundations of Mechanics (2008)
- Willems, J. The Behavioral Approach to Open and Interconnected Systems. IEEE Control Systems Magazine vol. 27 x1–x1 (2007) -- [10.1109/mcs.2007.4339280](https://doi.org/10.1109/mcs.2007.4339280)
- [Delvenne, J.-C. & Sandberg, H. Finite-time thermodynamics of port-Hamiltonian systems. Physica D: Nonlinear Phenomena vol. 267 123–132 (2014)](finite-time-thermodynamics-of-port-hamiltonian-systems) -- [10.1016/j.physd.2013.07.017](https://doi.org/10.1016/j.physd.2013.07.017)
- Willems, J. C. Paradigms and puzzles in the theory of dynamical systems. IEEE Transactions on Automatic Control vol. 36 259–294 (1991) -- [10.1109/9.73561](https://doi.org/10.1109/9.73561)
- zimmer, The Modelica multi-bond graph library. Proc 5th Int Modelica Conf (2006)
- dorfman, Dirac Structures and Integrability of Nonlinear Evolution Equations (1993)
- Wong, Y. K. Application of Bond Graph Models to Economics. International Journal of Modelling and Simulation vol. 21 181–190 (2001) -- [10.1080/02286203.2001.11442201](https://doi.org/10.1080/02286203.2001.11442201)
- [Donaire, A. & Junco, S. Derivation of Input-State-Output Port-Hamiltonian Systems from bond graphs. Simulation Modelling Practice and Theory vol. 17 137–151 (2009)](derivation-of-input-state-output-port-hamiltonian-systems-from-bond-graphs) -- [10.1016/j.simpat.2008.02.007](https://doi.org/10.1016/j.simpat.2008.02.007)
- van der Schaft, A. L2 - Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer London, 2000). doi:10.1007/978-1-4471-0507-7 -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- elmqvist, A structured model language for large continuous systems. (1978)
- Thoma, J. U. Entropy and mass flow for energy conversion. Journal of the Franklin Institute vol. 299 89–96 (1975) -- [10.1016/0016-0032(75)90131-3](https://doi.org/10.1016/0016-0032(75)90131-3)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- golo, Hamiltonian formulation of bond graphs. Nonlinear and Hybrid Systems in Automotive Control (2003)
- schaft, Port-Hamiltonian systems. Modeling and Control of Complex Physical Systems The Port-Hamiltonian Approach (2009)
- fritzson, Principles of Object-Oriented Modeling and Simulation with Modelica 3 3 A Cyber-Physical Approach (2015)

