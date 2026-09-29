---
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
- Lee JM (2012) Introduction to Smooth Manifolds. Springer New York, New York, NY -- [10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5)
- Kennedy MP (1993) Three steps to chaos. II. A Chua's circuit primer. IEEE Trans Circuits Syst I 40(10):657–674. https://doi.org/10.1109/81.246141 -- [10.1109/81.246141](https://doi.org/10.1109/81.246141)
- Kennedy MP (1993) Three steps to chaos. I. Evolution. IEEE Trans Circuits Syst I 40(10):640–656. https://doi.org/10.1109/81.246140 -- [10.1109/81.246140](https://doi.org/10.1109/81.246140)
- Karnopp DC, Margolis DL, Rosenberg RC (2012) System Dynamics. Wiley -- [10.1002/9781118152812](https://doi.org/10.1002/9781118152812)
- paynter, Analysis and Design of Engineering Systems (1961)
- maks, A spinor approach to port-Hamiltonian systems. Proc 19th Int Symp Math Theory Netw Syst (MTNS) (2010)
- Luzum B, Capitaine N, Fienga A, Folkner W, Fukushima T, Hilton J, Hohenkerk C, Krasinsky G, Petit G, Pitjeva E, Soffel M, Wallace P (2011) The IAU 2009 system of astronomical constants: the report of the IAU working group on numerical standards for Fundamental Astronomy. Celest Mech Dyn Astr 110(4):293–304. https://doi.org/10.1007/s10569-011-9352-4 -- [10.1007/s10569-011-9352-4](https://doi.org/10.1007/s10569-011-9352-4)
- Lieb EH, Yngvason J (1999) The physics and mathematics of the second law of thermodynamics. Physics Reports 310(1):1–96. https://doi.org/10.1016/s0370-1573(98)00082-9 -- [10.1016/s0370-1573(98)00082-9](https://doi.org/10.1016/s0370-1573(98)00082-9)
- Cellier FE (1992) Hierarchical non-linear bond graphs: a unified methodology for modeling complex physical systems. SIMULATION 58(4):230–248. https://doi.org/10.1177/003754979205800404 -- [10.1177/003754979205800404](https://doi.org/10.1177/003754979205800404)
- cellier, The Modelica bond graph library. Proc 4th Int Modelica Conf (2005)
- tellegen, The network element. Philips Res Rep (1948)
- [Cervera J, van der Schaft AJ, Baños A (2007) Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica 43(2):212–225. https://doi.org/10.1016/j.automatica.2006.08.014](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- chua, The genesis of Chua’s circuit. Int J Electron Commun (1992)
- [Courant TJ (1990) Dirac manifolds. Trans Amer Math Soc 319(2):631–661. https://doi.org/10.1090/s0002-9947-1990-0998124-1](dirac-manifolds) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- dai, Compositional design of cyber-physical systems using port-Hamiltonian systems. (2016)
- [Dai S, Lattmann Z, Koutsoukos X (2015) Compositional Design of Cyber-Physical Systems Using Port-Hamiltonian Systems. In: Cyber-Physical Systems. CRC Press, pp 33–59](compositional-design-of-cyber-physical-systems-using-port-hamiltonian-systems0) -- [10.1201/b19290-4](https://doi.org/10.1201/b19290-4)
- [Dalsmo M, van der Schaft A (1998) On Representations and Integrability of Mathematical Structures in Energy-Conserving Physical Systems. SIAM J Control Optim 37(1):54–91. https://doi.org/10.1137/s0363012996312039](on-representations-and-integrability-of-mathematical-structures-in-energy-conserving-physical-systems) -- [10.1137/s0363012996312039](https://doi.org/10.1137/s0363012996312039)
- Dymola–Dynamic Modeling Laboratory–User Manual 1B Developing and Simulating a Model (2019)
- calle, Improvements in BondLib, the modelica bond graph library. Proceedings of EuroSim Congress on Modeling and Simulation (2013)
- åström, Evolution of continuoustime modeling and simulation. Proc 12th Eur Simulation Multiconf (EMS) (1998)
- Husemoller D (1994) Fibre Bundles. Springer New York, New York, NY -- [10.1007/978-1-4757-2261-1](https://doi.org/10.1007/978-1-4757-2261-1)
- Modelica—A Unified Object-Oriented Language for Systems Modeling Language Specification Version 3 4 (2017)
- Holm DD, Schmah T, Stoica C, Ellis DCP (2009) Geometric Mechanics and Symmetry. Oxford University PressOxford -- [10.1093/oso/9780199212903.001.0001](https://doi.org/10.1093/oso/9780199212903.001.0001)
- borutzky, Bond Graph Methodology Development and Analysis of Multidisciplinary Dynamic System Models (2010)
- [Batlle C, Massana I, Simo E (2011) Representation of a general composition of Dirac structures. In: IEEE Conference on Decision and Control and European Control Conference. IEEE, pp 5199–5204](representation-of-a-general-composition-of-dirac-structures) -- [10.1109/cdc.2011.6160588](https://doi.org/10.1109/cdc.2011.6160588)
- RESOLUTION B2: On the re-definition of the astronomical unit of length. Proc 28th Gen Assem Int Astronomical Union (IAU) (2012)
- brenan, Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations (1996)
- Breedveld PC (1985) Multibond graph elements in physical systems theory. Journal of the Franklin Institute 319(1-2):1–36. https://doi.org/10.1016/0016-0032(85)90062-6 -- [10.1016/0016-0032(85)90062-6](https://doi.org/10.1016/0016-0032(85)90062-6)
- Arnold VI (1989) Mathematical Methods of Classical Mechanics. Springer New York, New York, NY -- [10.1007/978-1-4757-2063-1](https://doi.org/10.1007/978-1-4757-2063-1)
- brewer, Bond graphs of microeconomic systems (1977)
- abraham, Foundations of Mechanics (2008)
- Willems J (2007) The Behavioral Approach to Open and Interconnected Systems. IEEE Control Syst Mag 27(99):x1–x1. https://doi.org/10.1109/mcs.2007.4339280 -- [10.1109/mcs.2007.4339280](https://doi.org/10.1109/mcs.2007.4339280)
- [Delvenne J-C, Sandberg H (2014) Finite-time thermodynamics of port-Hamiltonian systems. Physica D: Nonlinear Phenomena 267:123–132. https://doi.org/10.1016/j.physd.2013.07.017](finite-time-thermodynamics-of-port-hamiltonian-systems) -- [10.1016/j.physd.2013.07.017](https://doi.org/10.1016/j.physd.2013.07.017)
- Willems JC (1991) Paradigms and puzzles in the theory of dynamical systems. IEEE Trans Automat Contr 36(3):259–294. https://doi.org/10.1109/9.73561 -- [10.1109/9.73561](https://doi.org/10.1109/9.73561)
- zimmer, The Modelica multi-bond graph library. Proc 5th Int Modelica Conf (2006)
- dorfman, Dirac Structures and Integrability of Nonlinear Evolution Equations (1993)
- Wong YK (2001) Application of Bond Graph Models to Economics. International Journal of Modelling and Simulation 21(3):181–190. https://doi.org/10.1080/02286203.2001.11442201 -- [10.1080/02286203.2001.11442201](https://doi.org/10.1080/02286203.2001.11442201)
- [Donaire A, Junco S (2009) Derivation of Input-State-Output Port-Hamiltonian Systems from bond graphs. Simulation Modelling Practice and Theory 17(1):137–151. https://doi.org/10.1016/j.simpat.2008.02.007](derivation-of-input-state-output-port-hamiltonian-systems-from-bond-graphs) -- [10.1016/j.simpat.2008.02.007](https://doi.org/10.1016/j.simpat.2008.02.007)
- van der Schaft A (2000) L2 - Gain and Passivity Techniques in Nonlinear Control. Springer London, London -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- elmqvist, A structured model language for large continuous systems. (1978)
- Thoma JU (1975) Entropy and mass flow for energy conversion. Journal of the Franklin Institute 299(2):89–96. https://doi.org/10.1016/0016-0032(75)90131-3 -- [10.1016/0016-0032(75)90131-3](https://doi.org/10.1016/0016-0032(75)90131-3)
- [Duindam V, Macchelli A, Stramigioli S, Bruyninckx H (2009) Modeling and Control of Complex Physical Systems. Springer Berlin Heidelberg, Berlin, Heidelberg](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2-3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- golo, Hamiltonian formulation of bond graphs. Nonlinear and Hybrid Systems in Automotive Control (2003)
- schaft, Port-Hamiltonian systems. Modeling and Control of Complex Physical Systems The Port-Hamiltonian Approach (2009)
- fritzson, Principles of Object-Oriented Modeling and Simulation with Modelica 3 3 A Cyber-Physical Approach (2015)

