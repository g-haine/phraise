---
title: "Energy-based Neural Network Controllers for DC-DC Converters"
date: 2025-08-19 00:00:00 +0100
permalink: energy-based-neural-network-controllers-for-dc-dc-converters
year: 2025
authors: Kamakshi Tatkare, Brian Johnson
category: proceedings
---
 
## Authors
[Kamakshi Tatkare](authors/kamakshi-tatkare), [Brian Johnson](authors/brian-johnson)
 
## Abstract
In this paper, our objective is to use notions of system energy to formulate closed-loop dc-dc converter controls that are nonlinear and satisfy passivity properties that guarantee stability. Port-Hamiltonian models are a particular form of models which can be used to describe the total energy in a converter, much like a Lyapunov function. In our approach, we first formulate a port-Hamiltonian model that represents the desired closed-loop dynamics we seek. However, the solution to this model is generally quite difficult for even the simplest of converters. To bypass this challenge, we offer a framework where a neural-network-based controller is trained to estimate the solution to this design problem. Essentially, our objective is to ensure that the energy dynamics of the dc-dc converter with a neural network as a controller closely match that of the target port-Hamiltonian model. This method circumvents the mathematical difficulties encountered when attempting to solve the closed-loop port-Hamiltonian model directly and gives a generalized framework. Our paper illustrates this approach and its versatile application towards boost, buck, buck-boost, and Ćuk converters.
 
## Citation
- **Journal:** 2025 IEEE 26th Workshop on Control and Modeling for Power Electronics (COMPEL)
- **Year:** 2025
- **Volume:** 
- **Issue:** 
- **Pages:** 1--8
- **Publisher:** IEEE
- **DOI:** [10.1109/compel57166.2025.11121236](https://doi.org/10.1109/compel57166.2025.11121236)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Tatkare_2025,
  title={{Energy-based Neural Network Controllers for DC-DC Converters}},
  DOI={10.1109/compel57166.2025.11121236},
  booktitle={{2025 IEEE 26th Workshop on Control and Modeling for Power Electronics (COMPEL)}},
  publisher={IEEE},
  author={Tatkare, Kamakshi and Johnson, Brian},
  year={2025},
  pages={1--8}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/energy-based-neural-network-controllers-for-dc-dc-converters.bib)
 
## References
- Banerjee S, Verghese GC (2001) Nonlinear Phenomena in Power Electronic -- [10.1109/9780470545393](https://doi.org/10.1109/9780470545393)
- [Tõnso M, Kaparin V, Belikov J (2023) Port-Hamiltonian framework in power systems domain: A survey. Energy Reports 10:2918–2930. https://doi.org/10.1016/j.egyr.2023.09.07](port-hamiltonian-framework-in-power-systems-domain-a-survey) -- [10.1016/j.egyr.2023.09.077](https://doi.org/10.1016/j.egyr.2023.09.077)
- Rodriguez H, Ortega R, Escobar G A new family of energy-based non-linear controllers for switched power converters. ISIE 2001. 2001 IEEE International Symposium on Industrial Electronics Proceedings (Cat. No.01TH8570) 2:723–72 -- [10.1109/isie.2001.931555](https://doi.org/10.1109/isie.2001.931555)
- [Yong Wang, Haisheng Yu, Jinpeng Yu (2008) The modeling and control of Buck-Boost converter based on energy-shaping theory. 2008 IEEE International Conference on Industrial Technology 1–](the-modeling-and-control-of-buck-boost-converter-based-on-energy-shaping-theory) -- [10.1109/icit.2008.4608311](https://doi.org/10.1109/icit.2008.4608311)
- [Pang S, Nahid-Mobarakeh B, Pierfederici S, Huangfu Y, Luo G, Gao F (2021) Toward Stabilization of Constant Power Loads Using IDA-PBC for Cascaded LC Filter DC/DC Converters. IEEE J Emerg Sel Topics Power Electron 9(2):1302–1314. https://doi.org/10.1109/jestpe.2019.294533](toward-stabilization-of-constant-power-loads-using-ida-pbc-for-cascaded-i-lc-i-filter-dc-dc-converters) -- [10.1109/jestpe.2019.2945331](https://doi.org/10.1109/jestpe.2019.2945331)
- [Gil-Gonzalez W, Montoya O, Herrera-Orozco A, Serra F (2020) Adaptive IDA-PBC Applied to On-Board Boost Converter Supplying a Constant Power Load. 2020 IEEE ANDESCON 1–](adaptive-ida-pbc-applied-to-on-board-boost-converter-supplying-a-constant-power-load) -- [10.1109/andescon50619.2020.9272078](https://doi.org/10.1109/andescon50619.2020.9272078)
- Hassan MA, Su C-L, Pou J, Sulligoi G, Almakhles D, Bosich D, Guerrero JM (2022) DC Shipboard Microgrids With Constant Power Loads: A Review of Advanced Nonlinear Control Strategies and Stabilization Techniques. IEEE Trans Smart Grid 13(5):3422–3438. https://doi.org/10.1109/tsg.2022.316826 -- [10.1109/tsg.2022.3168267](https://doi.org/10.1109/tsg.2022.3168267)
- Yuliang Tang, Haisheng Yu, Zongwei Zou (2008) Hamiltonian modeling and energy-shaping control of three-phase ac/dc voltage-source converters. 2008 IEEE International Conference on Automation and Logistics 591–59 -- [10.1109/ical.2008.4636219](https://doi.org/10.1109/ical.2008.4636219)
- [Serra FM, De Angelo CH, Forchetti DG (2012) IDA-PBC control of a three-phase front-end converter. IECON 2012 - 38th Annual Conference on IEEE Industrial Electronics Society 5203–520](ida-pbc-control-of-a-three-phase-front-end-converter) -- [10.1109/iecon.2012.6388969](https://doi.org/10.1109/iecon.2012.6388969)
- Khefifi N, Houari A, Machmoum M, Ghanes M, Ait-Ahmed M (2019) Control of grid forming inverter based on robust IDA-PBC for power quality enhancement. Sustainable Energy, Grids and Networks 20:100276. https://doi.org/10.1016/j.segan.2019.10027 -- [10.1016/j.segan.2019.100276](https://doi.org/10.1016/j.segan.2019.100276)
- [Meng Y, Shang S, Zhang H, Cui Y, Wang X (2017) IDA‐PB control with integral action of Y‐connected modular multilevel converter for fractional frequency transmission application. IET Generation Trans &amp;amp; Dist 12(14):3385–3397. https://doi.org/10.1049/iet-gtd.2017.057](ida-pb-control-with-integral-action-of-y-connected-modular-multilevel-converter-for-fractional-frequency-transmission-application) -- [10.1049/iet-gtd.2017.0573](https://doi.org/10.1049/iet-gtd.2017.0573)
- [Meshram RV, Bhagwat M, Khade S, Wagh SR, Stankovic AM, Singh NM (2019) Port-Controlled Phasor Hamiltonian Modeling and IDA-PBC Control of Solid-State Transformer. IEEE Trans Contr Syst Technol 27(1):161–174. https://doi.org/10.1109/tcst.2017.276186](port-controlled-phasor-hamiltonian-modeling-and-ida-pbc-control-of-solid-state-transformer) -- [10.1109/tcst.2017.2761866](https://doi.org/10.1109/tcst.2017.2761866)
- Blankenstein G, Ortega R, Van Der Schaft AJ (2002) The matching conditions of controlled Lagrangians and IDA-passivity based control. International Journal of Control 75(9):645–665. https://doi.org/10.1080/0020717021013593 -- [10.1080/00207170210135939](https://doi.org/10.1080/00207170210135939)
- Sanchez Escalonilla Plaza, Total energy shaping with neural interconnection and damping assignment - Passivity based control. Annual Learning for Dynamics and Control Conference
- Viola G, Ortega R, Banavar R, Acosta JA, Astolfi A (2007) Total Energy Shaping Control of Mechanical Systems: Simplifying the Matching Equations Via Coordinate Changes. IEEE Trans Automat Contr 52(6):1093–1099. https://doi.org/10.1109/tac.2007.89906 -- [10.1109/tac.2007.899064](https://doi.org/10.1109/tac.2007.899064)
- Beckers, Physics-informed learning for passivity-based tracking control. (2025)
- Nageshrao SP, Lopes GAD, Jeltsema D, Babuška R (2014) Interconnection and Damping Assignment Control via Reinforcement Learning. IFAC Proceedings Volumes 47(3):1760–1765. https://doi.org/10.3182/20140824-6-za-1003.0170 -- [10.3182/20140824-6-za-1003.01705](https://doi.org/10.3182/20140824-6-za-1003.01705)
- [Desai SA, Mattheakis M, Sondak D, Protopapas P, Roberts SJ (2021) Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Phys Rev E 104(3). https://doi.org/10.1103/physreve.104.03431](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- [Nageshrao SP, Lopes GAD, Jeltsema D, Babuska R (2016) Port-Hamiltonian Systems in Adaptive and Learning Control: A Survey. IEEE Trans Automat Contr 61(5):1223–1238. https://doi.org/10.1109/tac.2015.245849](port-hamiltonian-systems-in-adaptive-and-learning-control-a-survey) -- [10.1109/tac.2015.2458491](https://doi.org/10.1109/tac.2015.2458491)
- Ortega, Passivity-based control of euler-lagrange systems: Mechanical, electrical and electromechanical. Mechanical, Electrical and Electromechanical Applications (2013)
- [Maschke BM, van der Schaft AJ (1992) Port-Controlled Hamiltonian Systems: Modelling Origins and Systemtheoretic Properties. IFAC Proceedings Volumes 25(13):359–365. https://doi.org/10.1016/s1474-6670(17)52308-](port-controlled-hamiltonian-systems-modelling-origins-and-systemtheoretic-properties) -- [10.1016/s1474-6670(17)52308-3](https://doi.org/10.1016/s1474-6670(17)52308-3)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Ortega R, van der Schaft AJ, Maschke BM (1999) Stabilization of port-controlled Hamiltonian systems via energy balancing. Lecture Notes in Control and Information Sciences 239–26](stabilization-of-port-controlled-hamiltonian-systems-via-energy-balancing) -- [10.1007/1-84628-577-1_13](https://doi.org/10.1007/1-84628-577-1_13)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Khalil, Nonlinear systems (2002)
- Kolmogorov AN (1963) On the representation of continuous functions of many variables by superposition of continuous functions of one variable and addition. American Mathematical Society Translations: Series 2 55–5 -- [10.1090/trans2/028/04](https://doi.org/10.1090/trans2/028/04)
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.04 -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Karniadakis GE, Kevrekidis IG, Lu L, Perdikaris P, Wang S, Yang L (2021) Physics-informed machine learning. Nat Rev Phys 3(6):422–440. https://doi.org/10.1038/s42254-021-00314- -- [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5)
- Sanchez-Escalonilla S, Reyes-Baez R, Jayawardhana B (2022) Stabilization of Underactuated Systems of Degree One via Neural Interconnection and Damping Assignment – Passivity Based Control. 2022 IEEE 61st Conference on Decision and Control (CDC) 2463–246 -- [10.1109/cdc51059.2022.9993241](https://doi.org/10.1109/cdc51059.2022.9993241)
- Wang J, Huang J, Yau SST (2000) Approximate nonlinear output regulation based on the universal approximation theorem. Int J Robust Nonlinear Control 10(5):439–456. https://doi.org/10.1002/(sici)1099-1239(20000430)10:5<439::aid-rnc480>3.0.co;2- -- [10.1002/(sici)1099-1239(20000430)10:5<439::aid-rnc480>3.0.co;2-3](https://doi.org/10.1002/(sici)1099-1239(20000430)10:5<439::aid-rnc480>3.0.co;2-3)
- Sanchez-Escalonilla, Robust neural ida-pbc: passivity-based stabilization under approximations. (2024)
- Mckay MD, Beckman RJ, Conover WJ (2000) A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output From a Computer Code. Technometrics 42(1):55–61. https://doi.org/10.1080/00401706.2000.1048597 -- [10.2307/1271432](https://doi.org/10.2307/1271432)
- Kingma, Adam: A method for stochastic optimization. (2014)

