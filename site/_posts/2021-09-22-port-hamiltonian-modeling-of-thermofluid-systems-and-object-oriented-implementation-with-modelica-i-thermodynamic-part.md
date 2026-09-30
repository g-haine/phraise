---
title: "Port-Hamiltonian Modeling of Thermofluid Systems and Object-Oriented Implementation With Modelica I: Thermodynamic Part"
date: 2021-09-22 00:00:00 +0100
permalink: port-hamiltonian-modeling-of-thermofluid-systems-and-object-oriented-implementation-with-modelica-i-thermodynamic-part
year: 2021
authors: Francisco M. Marquez, Pedro J. Zufiria, Luis J. Yebra
category: articles
---
 
## Authors
[Francisco M. Marquez](authors/francisco-m-marquez), [Pedro J. Zufiria](authors/pedro-j-zufiria), [Luis J. Yebra](authors/luis-j-yebra)
 
## Abstract
In this paper, we present the physical foundations and the development of the thermodynamic part of a Modelica library with the fundamental components for modeling thermofluid systems. We have chosen Modelica because it is an object-oriented modeling language that allows an elegant design of the library, with a top-down conception that starts from very general components where we model the thermodynamic properties common to all simple substances and descend by inheritance to model the properties of each particular substance. To model the behavior of each component, we have used: classical thermodynamics to define the equilibrium states, the local equilibrium hypothesis of Classical Irreversible Thermodynamics to model the changes of state, and the port-Hamiltonian approach to obtain the equations of the system dynamics. With this formulation, we implement the thermodynamic behavior of ideal gases (including monatomic gases as a particular case), the 2073 substances defined for the CEA (Chemical Equilibrium with Applications) NASA Glenn computer program, the IAPWS Formulation 1995 for the Thermodynamic Properties of Water Substance for General and Scientific Use, and the Syltherm 800 HTF (Heat Transfer Fluid). We also define graphical symbols for each library component that facilitate modeling complex systems with simple drag-and-drop manipulations, component connection, and parameter selection. These symbols are a slightly modified version of those used in bond graphs to facilitate their reading and the representation of the structure of complex systems. We also show the modeling, simulation, and comparison for accuracy, performance, and scalability of some thermodynamic systems implemented with the Modelica Standard Library (MSL) and the proposed library.
 
## Citation
- **Journal:** IEEE Access
- **Year:** 2021
- **Volume:** 9
- **Issue:** 
- **Pages:** 131496--131519
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/access.2021.3115038](https://doi.org/10.1109/access.2021.3115038)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Marquez_2021,
  title={{Port-Hamiltonian Modeling of Thermofluid Systems and Object-Oriented Implementation With Modelica I: Thermodynamic Part}},
  volume={9},
  ISSN={2169-3536},
  DOI={10.1109/access.2021.3115038},
  journal={IEEE Access},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Marquez, Francisco M. and Zufiria, Pedro J. and Yebra, Luis J.},
  year={2021},
  pages={131496--131519}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-modeling-of-thermofluid-systems-and-object-oriented-implementation-with-modelica-i-thermodynamic-part.bib)
 
## References
- Öttinger HC (2005) Beyond Equilibrium Thermodynamics. Wiley -- [10.1002/0471727903](https://doi.org/10.1002/0471727903)
- OSTER G, PERELSON A, KATCHALSKY A (1971) Network Thermodynamics. Nature 234(5329):393–399. https://doi.org/10.1038/234393a0 -- [10.1038/234393a0](https://doi.org/10.1038/234393a0)
- Morrison PJ (1986) A paradigm for joined Hamiltonian and dissipative systems. Physica D: Nonlinear Phenomena 18(1-3):410–419. https://doi.org/10.1016/0167-2789(86)90209-5 -- [10.1016/0167-2789(86)90209-5](https://doi.org/10.1016/0167-2789(86)90209-5)
- Morrison PJ (1984) Bracket formulation for irreversible classical fields. Physics Letters A 100(8):423–427. https://doi.org/10.1016/0375-9601(84)90635-2 -- [10.1016/0375-9601(84)90635-2](https://doi.org/10.1016/0375-9601(84)90635-2)
- Mohr PJ, Taylor BN (2000) CODATA recommended values of the fundamental physical constants: 1998. Rev Mod Phys 72(2):351–495. https://doi.org/10.1103/revmodphys.72.351 -- [10.1103/revmodphys.72.351](https://doi.org/10.1103/revmodphys.72.351)
- mcbride, NASA Glenn coefficients for calculating thermodynamic properties of individual species. (2002)
- Onsager L (1931) Reciprocal Relations in Irreversible Processes. II. Phys Rev 38(12):2265–2279. https://doi.org/10.1103/physrev.38.2265 -- [10.1103/physrev.38.2265](https://doi.org/10.1103/physrev.38.2265)
- Onsager L (1931) Reciprocal Relations in Irreversible Processes. I. Phys Rev 37(4):405–426. https://doi.org/10.1103/physrev.37.405 -- [10.1103/physrev.37.405](https://doi.org/10.1103/physrev.37.405)
- olsson, Modelica - A Unified Object-Oriented Language for Systems Modeling Language Specification Version 3 3 (2021)
- Mwesigye A, Bello-Ochende T, Meyer JP (2013) Numerical investigation of entropy generation in a parabolic trough receiver at different concentration ratios. Energy 53:114–127. https://doi.org/10.1016/j.energy.2013.03.006 -- [10.1016/j.energy.2013.03.006](https://doi.org/10.1016/j.energy.2013.03.006)
- [Marquez FM, Zufiria PJ, Yebra LJ (2020) Port-Hamiltonian Modeling of Multiphysics Systems and Object-Oriented Implementation With the Modelica Language. IEEE Access 8:105980–105996. https://doi.org/10.1109/access.2020.3000129](port-hamiltonian-modeling-of-multiphysics-systems-and-object-oriented-implementation-with-the-modelica-language) -- [10.1109/access.2020.3000129](https://doi.org/10.1109/access.2020.3000129)
- landau, Statistical Physics Part 1 of Course of Theoretical Physics (1980)
- Materassi M (2016) Entropy as a Metric Generator of Dissipation in Complete Metriplectic Systems. Entropy 18(8):304. https://doi.org/10.3390/e18080304 -- [10.3390/e18080304](https://doi.org/10.3390/e18080304)
- Alberty RA (2001) Use of Legendre transforms in chemical thermodynamics (IUPAC Technical Report). Pure and Applied Chemistry 73(8):1349–1380. https://doi.org/10.1351/pac200173081349 -- [10.1351/pac200173081349](https://doi.org/10.1351/pac200173081349)
- abraham, Foundations of Mechanics (1978)
- golo, Hamiltonian formulation of bond graphs. Nonlinear and Hybrid Systems in Automotive Control (2003)
- Revised release on the IAPWS formulation 1995 for the thermodynamic properties of ordinary water substance for general and scientific use. IAPWS (2018)
- Revised release on the IAPWS industrial formulation 1997 for the thermodynamic properties of water and steam. IAPWS (2012)
- Karnopp DC, Margolis DL, Rosenberg RC (2012) System Dynamics. Wiley -- [10.1002/9781118152812](https://doi.org/10.1002/9781118152812)
- Jou D, Lebon G (2010) Extended Irreversible Thermodynamics. Springer Netherlands, Dordrecht -- [10.1007/978-90-481-3074-0](https://doi.org/10.1007/978-90-481-3074-0)
- koga, Solution Thermodynamics and its Application to Aqueous Solutions A Differential Approach (2007)
- Kaufman AN (1984) Dissipative hamiltonian systems: A unifying principle. Physics Letters A 100(8):419–422. https://doi.org/10.1016/0375-9601(84)90634-0 -- [10.1016/0375-9601(84)90634-0](https://doi.org/10.1016/0375-9601(84)90634-0)
- [van der Schaft A (2017) L2-Gain and Passivity Techniques in Nonlinear Control. Springer International Publishing, Cham](l2-gain-and-passivity-techniques-in-nonlinear-control) -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- [Van der Schaft A, Maschke B (2018) Geometry of Thermodynamic Processes. Entropy 20(12):925. https://doi.org/10.3390/e20120925](geometry-of-thermodynamic-processes) -- [10.3390/e20120925](https://doi.org/10.3390/e20120925)
- zimmer, The Modelica multi-bond graph library. Proc 5th Int Modelica Conf (2006)
- Wagner W, Pruß A (2002) The IAPWS Formulation 1995 for the Thermodynamic Properties of Ordinary Water Substance for General and Scientific Use. Journal of Physical and Chemical Reference Data 31(2):387–535. https://doi.org/10.1063/1.1461829 -- [10.1063/1.1461829](https://doi.org/10.1063/1.1461829)
- Wagner W, Cooper JR, Dittmann A, Kijima J, Kretzschmar H-J, Kruse A, Maresˇ R, Oguchi K, Sato H, Sto¨cker I, Sˇifner O, Takaishi Y, Tanishita I, Tru¨benbach J, Willkommen T (2000) The IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam. Journal of Engineering for Gas Turbines and Power 122(1):150–184. https://doi.org/10.1115/1.483186 -- [10.1115/1.483186](https://doi.org/10.1115/1.483186)
- cellier, The Modelica bond braph library. Proc 4th Int Modelica Conf (2005)
- [Courant TJ (1990) Dirac manifolds. Trans Amer Math Soc 319(2):631–661. https://doi.org/10.1090/s0002-9947-1990-0998124-1](dirac-manifolds) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- paynter, Analysis and Design of Engineering Systems (1961)
- de groot, Non-equilibrium thermodynamics (1962)
- de la Calle A, Cellier FE, Yebra LJ, Dormido S (2013) Improvements in BondLib, the Modelica Bond Graph Library. In: 2013 8th EUROSIM Congress on Modelling and Simulation. IEEE, pp 282–287 -- [10.1109/eurosim.2013.58](https://doi.org/10.1109/eurosim.2013.58)
- [Donaire A, Junco S (2009) Derivation of Input-State-Output Port-Hamiltonian Systems from bond graphs. Simulation Modelling Practice and Theory 17(1):137–151. https://doi.org/10.1016/j.simpat.2008.02.007](derivation-of-input-state-output-port-hamiltonian-systems-from-bond-graphs) -- [10.1016/j.simpat.2008.02.007](https://doi.org/10.1016/j.simpat.2008.02.007)
- SYLTHERM 800 Heat Transfer Fluid (1997)
- [Duindam V, Macchelli A, Stramigioli S, Bruyninckx H (2009) Modeling and Control of Complex Physical Systems. Springer Berlin Heidelberg, Berlin, Heidelberg](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- elmqvist, Object-oriented modeling of thermo-fluid systems. Proc 3rd Int Modelica Conf (2003)
- fritzson, Principles of Object-Oriented Modeling and Simulation with Modelica 3 3 A Cyber-Physical Approach (2015)
- Fritzson P, Pop A, Abdelhak K, Ashgar A, Bachmann B, Braun W, Bouskela D, Braun R, Buffoni L, Casella F, Castro R, Franke R, Fritzson D, Gebremedhin M, Heuermann A, Lie B, Mengist A, Mikelsons L, Moudgalya K, Ochel L, Palanisamy A, Ruge V, Schamai W, Sjölund M, Thiele B, Tinnerholm J, Östlund P (2020) The OpenModelica Integrated Environment for Modeling, Simulation, and Model-Based Development. MIC 41(4):241–295. https://doi.org/10.4173/mic.2020.4.1 -- [10.4173/mic.2020.4.1](https://doi.org/10.4173/mic.2020.4.1)
- borutzky, Bond Graph Methodology–Development and Analysis of Multidisciplinary Dynamic System Models (2010)
- Bonilla J, Yebra LJ, Dormido S (2011) A heuristic method to minimise the chattering problem in dynamic mathematical two-phase flow models. Mathematical and Computer Modelling 54(5-6):1549–1560. https://doi.org/10.1016/j.mcm.2011.04.026 -- [10.1016/j.mcm.2011.04.026](https://doi.org/10.1016/j.mcm.2011.04.026)
- callen, Thermodynamics (1960)
- Borutzky W (ed) (2011) Bond Graph Modelling of Engineering Systems. Springer New York, New York, NY -- [10.1007/978-1-4419-9368-7](https://doi.org/10.1007/978-1-4419-9368-7)
- Cellier FE (1991) Continuous System Modeling. Springer New York, New York, NY -- [10.1007/978-1-4757-3922-0](https://doi.org/10.1007/978-1-4757-3922-0)
- callen, Thermodynamics and an Introduction to Thermostatistics (1985)
- van der Schaft A (2000) L2 - Gain and Passivity Techniques in Nonlinear Control. Springer London, London -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- cellier, ThermoBondLib—A new modelica library for modeling convective flows. Proc 6th Int Modelica Conf (2008)
- Thompson EA, Thompson EA, Taylor BN (2008) Guide for the use of the International System of Units (SI). National Institute of Standards and Technology, Gaithersburg, MD -- [10.6028/nist.sp.811e2008](https://doi.org/10.6028/nist.sp.811e2008)
- thoma, Modelling and Simulation in Thermal and Chemical Engineering A Bond Graph Approach (2000)
- tschoegl, Fundamentals Equilibrium Steady-State Thermodynamics (2000)
- Truesdell C (1984) Rational Thermodynamics. Springer New York, New York, NY -- [10.1007/978-1-4612-5206-1](https://doi.org/10.1007/978-1-4612-5206-1)
- [Pfeifer M, Caspart S, Hampel S, Muller C, Krebs S, Hohmann S (2020) Explicit port-Hamiltonian formulation of multi-bond graphs for an automated model generation. Automatica 120:109121. https://doi.org/10.1016/j.automatica.2020.109121](explicit-port-hamiltonian-formulation-of-multi-bond-graphs-for-an-automated-model-generation) -- [10.1016/j.automatica.2020.109121](https://doi.org/10.1016/j.automatica.2020.109121)
- Perelson AS (1975) Network thermodynamics. An overview. Biophysical Journal 15(7):667–685. https://doi.org/10.1016/s0006-3495(75)85847-4 -- [10.1016/s0006-3495(75)85847-4](https://doi.org/10.1016/s0006-3495(75)85847-4)
- [Rashad R, Califano F, van der Schaft AJ, Stramigioli S (2020) Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37(4):1400–1422. https://doi.org/10.1093/imamci/dnaa018](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- prigogine, Introduction to thermodynamics of irreversible processes (1967)

