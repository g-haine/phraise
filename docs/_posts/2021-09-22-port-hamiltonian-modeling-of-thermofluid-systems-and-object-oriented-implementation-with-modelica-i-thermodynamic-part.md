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
- Öttinger, H. C. Beyond Equilibrium Thermodynamics. (2005) doi:10.1002/0471727903 -- [10.1002/0471727903](https://doi.org/10.1002/0471727903)
- OSTER, G., PERELSON, A. & KATCHALSKY, A. Network Thermodynamics. Nature vol. 234 393–399 (1971) -- [10.1038/234393a0](https://doi.org/10.1038/234393a0)
- Morrison, P. J. A paradigm for joined Hamiltonian and dissipative systems. Physica D: Nonlinear Phenomena vol. 18 410–419 (1986) -- [10.1016/0167-2789(86)90209-5](https://doi.org/10.1016/0167-2789(86)90209-5)
- Morrison, P. J. Bracket formulation for irreversible classical fields. Physics Letters A vol. 100 423–427 (1984) -- [10.1016/0375-9601(84)90635-2](https://doi.org/10.1016/0375-9601(84)90635-2)
- Mohr, P. J. & Taylor, B. N. CODATA recommended values of the fundamental physical constants: 1998. Reviews of Modern Physics vol. 72 351–495 (2000) -- [10.1103/revmodphys.72.351](https://doi.org/10.1103/revmodphys.72.351)
- mcbride, NASA Glenn coefficients for calculating thermodynamic properties of individual species. (2002)
- Onsager, L. Reciprocal Relations in Irreversible Processes. II. Physical Review vol. 38 2265–2279 (1931) -- [10.1103/physrev.38.2265](https://doi.org/10.1103/physrev.38.2265)
- Onsager, L. Reciprocal Relations in Irreversible Processes. I. Physical Review vol. 37 405–426 (1931) -- [10.1103/physrev.37.405](https://doi.org/10.1103/physrev.37.405)
- olsson, Modelica - A Unified Object-Oriented Language for Systems Modeling Language Specification Version 3 3 (2021)
- Mwesigye, A., Bello-Ochende, T. & Meyer, J. P. Numerical investigation of entropy generation in a parabolic trough receiver at different concentration ratios. Energy vol. 53 114–127 (2013) -- [10.1016/j.energy.2013.03.006](https://doi.org/10.1016/j.energy.2013.03.006)
- [Marquez, F. M., Zufiria, P. J. & Yebra, L. J. Port-Hamiltonian Modeling of Multiphysics Systems and Object-Oriented Implementation With the Modelica Language. IEEE Access vol. 8 105980–105996 (2020)](port-hamiltonian-modeling-of-multiphysics-systems-and-object-oriented-implementation-with-the-modelica-language) -- [10.1109/access.2020.3000129](https://doi.org/10.1109/access.2020.3000129)
- landau, Statistical Physics Part 1 of Course of Theoretical Physics (1980)
- Materassi, M. Entropy as a Metric Generator of Dissipation in Complete Metriplectic Systems. Entropy vol. 18 304 (2016) -- [10.3390/e18080304](https://doi.org/10.3390/e18080304)
- Alberty, R. A. Use of Legendre transforms in chemical thermodynamics (IUPAC Technical Report). Pure and Applied Chemistry vol. 73 1349–1380 (2001) -- [10.1351/pac200173081349](https://doi.org/10.1351/pac200173081349)
- abraham, Foundations of Mechanics (1978)
- golo, Hamiltonian formulation of bond graphs. Nonlinear and Hybrid Systems in Automotive Control (2003)
- Revised release on the IAPWS formulation 1995 for the thermodynamic properties of ordinary water substance for general and scientific use. IAPWS (2018)
- Revised release on the IAPWS industrial formulation 1997 for the thermodynamic properties of water and steam. IAPWS (2012)
- Karnopp, D. C., Margolis, D. L. & Rosenberg, R. C. System Dynamics. (2012) doi:10.1002/9781118152812 -- [10.1002/9781118152812](https://doi.org/10.1002/9781118152812)
- Jou, D. & Lebon, G. Extended Irreversible Thermodynamics. (Springer Netherlands, 2010). doi:10.1007/978-90-481-3074-0 -- [10.1007/978-90-481-3074-0](https://doi.org/10.1007/978-90-481-3074-0)
- koga, Solution Thermodynamics and its Application to Aqueous Solutions A Differential Approach (2007)
- Kaufman, A. N. Dissipative hamiltonian systems: A unifying principle. Physics Letters A vol. 100 419–422 (1984) -- [10.1016/0375-9601(84)90634-0](https://doi.org/10.1016/0375-9601(84)90634-0)
- [van der Schaft, A. L2-Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer International Publishing, 2017). doi:10.1007/978-3-319-49992-5](l2-gain-and-passivity-techniques-in-nonlinear-control) -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- [Van der Schaft, A. & Maschke, B. Geometry of Thermodynamic Processes. Entropy vol. 20 925 (2018)](geometry-of-thermodynamic-processes) -- [10.3390/e20120925](https://doi.org/10.3390/e20120925)
- zimmer, The Modelica multi-bond graph library. Proc 5th Int Modelica Conf (2006)
- Wagner, W. & Pruß, A. The IAPWS Formulation 1995 for the Thermodynamic Properties of Ordinary Water Substance for General and Scientific Use. Journal of Physical and Chemical Reference Data vol. 31 387–535 (2002) -- [10.1063/1.1461829](https://doi.org/10.1063/1.1461829)
- Wagner, W. et al. The IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam. Journal of Engineering for Gas Turbines and Power vol. 122 150–184 (2000) -- [10.1115/1.483186](https://doi.org/10.1115/1.483186)
- cellier, The Modelica bond braph library. Proc 4th Int Modelica Conf (2005)
- [Courant, T. J. Dirac manifolds. Transactions of the American Mathematical Society vol. 319 631–661 (1990)](dirac-manifolds) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- paynter, Analysis and Design of Engineering Systems (1961)
- de groot, Non-equilibrium thermodynamics (1962)
- de la Calle, A., Cellier, F. E., Yebra, L. J. & Dormido, S. Improvements in BondLib, the Modelica Bond Graph Library. 2013 8th EUROSIM Congress on Modelling and Simulation 282–287 (2013) doi:10.1109/eurosim.2013.58 -- [10.1109/eurosim.2013.58](https://doi.org/10.1109/eurosim.2013.58)
- [Donaire, A. & Junco, S. Derivation of Input-State-Output Port-Hamiltonian Systems from bond graphs. Simulation Modelling Practice and Theory vol. 17 137–151 (2009)](derivation-of-input-state-output-port-hamiltonian-systems-from-bond-graphs) -- [10.1016/j.simpat.2008.02.007](https://doi.org/10.1016/j.simpat.2008.02.007)
- SYLTHERM 800 Heat Transfer Fluid (1997)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- elmqvist, Object-oriented modeling of thermo-fluid systems. Proc 3rd Int Modelica Conf (2003)
- fritzson, Principles of Object-Oriented Modeling and Simulation with Modelica 3 3 A Cyber-Physical Approach (2015)
- Fritzson, P. et al. The OpenModelica Integrated Environment for Modeling, Simulation, and Model-Based Development. Modeling, Identification and Control: A Norwegian Research Bulletin vol. 41 241–295 (2020) -- [10.4173/mic.2020.4.1](https://doi.org/10.4173/mic.2020.4.1)
- borutzky, Bond Graph Methodology&#x2013;Development and Analysis of Multidisciplinary Dynamic System Models (2010)
- Bonilla, J., Yebra, L. J. & Dormido, S. A heuristic method to minimise the chattering problem in dynamic mathematical two-phase flow models. Mathematical and Computer Modelling vol. 54 1549–1560 (2011) -- [10.1016/j.mcm.2011.04.026](https://doi.org/10.1016/j.mcm.2011.04.026)
- callen, Thermodynamics (1960)
- Bond Graph Modelling of Engineering Systems. (Springer New York, 2011). doi:10.1007/978-1-4419-9368-7 -- [10.1007/978-1-4419-9368-7](https://doi.org/10.1007/978-1-4419-9368-7)
- Cellier, F. E. Continuous System Modeling. (Springer New York, 1991). doi:10.1007/978-1-4757-3922-0 -- [10.1007/978-1-4757-3922-0](https://doi.org/10.1007/978-1-4757-3922-0)
- callen, Thermodynamics and an Introduction to Thermostatistics (1985)
- van der Schaft, A. L2 - Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer London, 2000). doi:10.1007/978-1-4471-0507-7 -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- cellier, ThermoBondLib&#x2014;A new modelica library for modeling convective flows. Proc 6th Int Modelica Conf (2008)
- Thompson, E. A., Thompson, E. A. & Taylor, B. N. Guide for the Use of the International System of Units (SI). http://dx.doi.org/10.6028/NIST.SP.811e2008 (2008) doi:10.6028/nist.sp.811e2008 -- [10.6028/nist.sp.811e2008](https://doi.org/10.6028/nist.sp.811e2008)
- thoma, Modelling and Simulation in Thermal and Chemical Engineering A Bond Graph Approach (2000)
- tschoegl, Fundamentals Equilibrium Steady-State Thermodynamics (2000)
- Truesdell, C. Rational Thermodynamics. (Springer New York, 1984). doi:10.1007/978-1-4612-5206-1 -- [10.1007/978-1-4612-5206-1](https://doi.org/10.1007/978-1-4612-5206-1)
- [Pfeifer, M. et al. Explicit port-Hamiltonian formulation of multi-bond graphs for an automated model generation. Automatica vol. 120 109121 (2020)](explicit-port-hamiltonian-formulation-of-multi-bond-graphs-for-an-automated-model-generation) -- [10.1016/j.automatica.2020.109121](https://doi.org/10.1016/j.automatica.2020.109121)
- Perelson, A. S. Network thermodynamics. An overview. Biophysical Journal vol. 15 667–685 (1975) -- [10.1016/s0006-3495(75)85847-4](https://doi.org/10.1016/s0006-3495(75)85847-4)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- prigogine, Introduction to thermodynamics of irreversible processes (1967)

