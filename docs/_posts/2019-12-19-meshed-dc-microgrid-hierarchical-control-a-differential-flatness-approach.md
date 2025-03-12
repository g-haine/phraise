---
layout: post
title: "Meshed DC microgrid hierarchical control: A differential flatness approach"
date: 2019-12-19 00:00:00 +0100
permalink: meshed-dc-microgrid-hierarchical-control-a-differential-flatness-approach
year: 2020
authors: I. Zafeiratou, I. Prodan, L. Lefèvre, L. Piétrac
category: articles
tags:
  - DC microgrid
  - Meshed topology
  - Port-Hamiltonian systems
  - Differential flatness
  - Hierarchical control
  - Power balancing
---
 
## Authors
[I. Zafeiratou](authors/i-zafeiratou), [I. Prodan](authors/ionela-prodan), [L. Lefèvre](authors/laurent-lefevre), [L. Piétrac](authors/l-pietrac)
 
## Abstract
In this paper, a meshed DC microgrid control architecture whose goal is to manage load balancing and efficient power distribution is introduced. A novel combination of port-Hamiltonian (PH) modeling with differential flatness and B-splines parametrization is introduced and shown to improve the microgrid's performance. A three layer supervision structure is considered: (i) B-spline parametrized flat output provide continuous profiles for load balancing and price reduction (high level); (ii) the profiles are tracked through a MPC implementation with stability guarantees (medium level); (iii) explicit switching laws applied to the DC/DC converters ensure appropriate power injection. Each level functions at a different time-scale (from slow to fast), and the control laws are chosen appropriately. The effectiveness of the proposed approach is evaluated by simulations over a DC microgrid composed by a collection of solar panels (PV), an energy storage system (ES), a utility grid (UG) and a consumers’ demand.
 
## Keywords
DC microgrid; Meshed topology; Port-Hamiltonian systems; Differential flatness; Hierarchical control; Power balancing
 
## Citation
- **Journal:** Electric Power Systems Research
- **Year:** 2020
- **Volume:** 180
- **Issue:** 
- **Pages:** 106133
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.epsr.2019.106133](https://doi.org/10.1016/j.epsr.2019.106133)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Zafeiratou_2020,
  title={{Meshed DC microgrid hierarchical control: A differential flatness approach}},
  volume={180},
  ISSN={0378-7796},
  DOI={10.1016/j.epsr.2019.106133},
  journal={Electric Power Systems Research},
  publisher={Elsevier BV},
  author={Zafeiratou, I. and Prodan, I. and Lefèvre, L. and Piétrac, L.},
  year={2020},
  pages={106133}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/meshed-dc-microgrid-hierarchical-control-a-differential-flatness-approach.bib)
 
## References
- Ahumada, C., Cardenas, R., Saez, D. & Guerrero, J. M. Secondary Control Strategies for Frequency Restoration in Islanded Microgrids With Consideration of Communication Delays. IEEE Transactions on Smart Grid vol. 7 1430–1441 (2016) -- [10.1109/tsg.2015.2461190](https://doi.org/10.1109/tsg.2015.2461190)
- Baghaee, H. R., Mirsalim, M. & Gharehpetian, G. B. Performance Improvement of Multi-DER Microgrid for Small- and Large-Signal Disturbances and Nonlinear Loads: Novel Complementary Control Loop and Fuzzy Controller in a Hierarchical Droop-Based Control Scheme. IEEE Systems Journal vol. 12 444–451 (2018) -- [10.1109/jsyst.2016.2580617](https://doi.org/10.1109/jsyst.2016.2580617)
- Biegler, L. T. & Zavala, V. M. Large-scale nonlinear programming using IPOPT: An integrating framework for enterprise-wide dynamic optimization. Computers &amp; Chemical Engineering vol. 33 575–582 (2009) -- [10.1016/j.compchemeng.2008.08.006](https://doi.org/10.1016/j.compchemeng.2008.08.006)
- Bouzid, A. E. M. et al. A novel Decoupled Trigonometric Saturated droop controller for power sharing in islanded low-voltage microgrids. Electric Power Systems Research vol. 168 146–161 (2019) -- [10.1016/j.epsr.2018.11.016](https://doi.org/10.1016/j.epsr.2018.11.016)
- CIAT entreprise, U. T. C, (2014)
- Cortes, C. A., Contreras, S. F. & Shahidehpour, M. Microgrid Topology Planning for Enhancing the Reliability of Active Distribution Networks. IEEE Transactions on Smart Grid vol. 9 6369–6377 (2018) -- [10.1109/tsg.2017.2709699](https://doi.org/10.1109/tsg.2017.2709699)
- Department of Energy Office of Energy Efficiency & Renewable Energy, (2017)
- Drgoňa, J., Picard, D., Kvasnica, M. & Helsen, L. Approximate model predictive building control via machine learning. Applied Energy vol. 218 199–216 (2018) -- [10.1016/j.apenergy.2018.02.156](https://doi.org/10.1016/j.apenergy.2018.02.156)
- Duindam, (2009)
- Escobar, G., van der Schaft, A. J. & Ortega, R. A Hamiltonian viewpoint in the modeling of switching power converters. Automatica vol. 35 445–452 (1999) -- [10.1016/s0005-1098(98)00196-4](https://doi.org/10.1016/s0005-1098(98)00196-4)
- FLIESS, M., LÉVINE, J., MARTIN, P. & ROUCHON, P. Flatness and defect of non-linear systems: introductory theory and examples. International Journal of Control vol. 61 1327–1361 (1995) -- [10.1080/00207179508921959](https://doi.org/10.1080/00207179508921959)
- Franke, On the computation of flat outputs for nonlinear control systems. (2013)
- Hernández, J. C., Sanchez-Sutil, F. & Muñoz-Rodríguez, F. J. Design criteria for the optimal sizing of a hybrid energy storage system in PV household-prosumers to maximize self-consumption and self-sufficiency. Energy vol. 186 115827 (2019) -- [10.1016/j.energy.2019.07.157](https://doi.org/10.1016/j.energy.2019.07.157)
- Iovine, Power management for a dc microgrid integrating renewables and storages. Control Eng. Pract. (2018)
- Karnopp, (2012)
- Basir Khan, M. R., Jidin, R. & Pasupuleti, J. Multi-agent based distributed control architecture for microgrid energy management and optimization. Energy Conversion and Management vol. 112 288–307 (2016) -- [10.1016/j.enconman.2016.01.011](https://doi.org/10.1016/j.enconman.2016.01.011)
- Kofman, E., Haimovich, H. & Seron, M. M. A systematic method to obtain ultimate bounds for perturbed systems. International Journal of Control vol. 80 167–178 (2007) -- [10.1080/00207170600611265](https://doi.org/10.1080/00207170600611265)
- Kotyczka, (2018)
- Langson, W., Chryssochoos, I., Raković, S. V. & Mayne, D. Q. Robust model predictive control using tubes. Automatica vol. 40 125–133 (2004) -- [10.1016/j.automatica.2003.08.009](https://doi.org/10.1016/j.automatica.2003.08.009)
- Levine, (2009)
- Liu, L., Meng, X. & Liu, C. A review of maximum power point tracking methods of PV power system at uniform and partial shading. Renewable and Sustainable Energy Reviews vol. 53 1500–1507 (2016) -- [10.1016/j.rser.2015.09.065](https://doi.org/10.1016/j.rser.2015.09.065)
- Löfberg, Yalmip: a toolbox for modeling and optimization in matlab. (2004)
- Lotfi, H. & Khodaei, A. Hybrid AC/DC microgrid planning. Energy vol. 118 37–46 (2017) -- [10.1016/j.energy.2016.12.015](https://doi.org/10.1016/j.energy.2016.12.015)
- Lou, G., Gu, W., Xu, Y., Cheng, M. & Liu, W. Distributed MPC-Based Secondary Voltage Control Scheme for Autonomous Droop-Controlled Microgrids. IEEE Transactions on Sustainable Energy vol. 8 792–804 (2017) -- [10.1109/tste.2016.2620283](https://doi.org/10.1109/tste.2016.2620283)
- Mahmoud, M. S., Azher Hussain, S. & Abido, M. A. Modeling and control of microgrid: An overview. Journal of the Franklin Institute vol. 351 2822–2859 (2014) -- [10.1016/j.jfranklin.2014.01.016](https://doi.org/10.1016/j.jfranklin.2014.01.016)
- Manwell, J. F. & McGowan, J. G. Lead acid battery storage model for hybrid energy systems. Solar Energy vol. 50 399–405 (1993) -- [10.1016/0038-092x(93)90060-2](https://doi.org/10.1016/0038-092x(93)90060-2)
- Mayne, D. Q. Model predictive control: Recent developments and future promise. Automatica vol. 50 2967–2986 (2014) -- [10.1016/j.automatica.2014.10.128](https://doi.org/10.1016/j.automatica.2014.10.128)
- Mazumder, S. K., Tahir, M. & Acharya, K. Master–Slave Current-Sharing Control of a Parallel DC–DC Converter System Over an RF Communication Interface. IEEE Transactions on Industrial Electronics vol. 55 59–66 (2008) -- [10.1109/tie.2007.896138](https://doi.org/10.1109/tie.2007.896138)
- Mortaz, E. & Valenzuela, J. Microgrid energy scheduling using storage from electric vehicles. Electric Power Systems Research vol. 143 554–562 (2017) -- [10.1016/j.epsr.2016.10.062](https://doi.org/10.1016/j.epsr.2016.10.062)
- National Renewable Energy Laboratory, (2016)
- Olaru, S., De Doná, J. A., Seron, M. M. & Stoican, F. Positive invariant sets for fault tolerant multisensor control schemes. International Journal of Control vol. 83 2622–2640 (2010) -- [10.1080/00207179.2010.535215](https://doi.org/10.1080/00207179.2010.535215)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Parisio, A., Rikos, E. & Glielmo, L. A Model Predictive Control Approach to Microgrid Operation Optimization. IEEE Transactions on Control Systems Technology vol. 22 1813–1827 (2014) -- [10.1109/tcst.2013.2295737](https://doi.org/10.1109/tcst.2013.2295737)
- Parisio, A., Rikos, E. & Glielmo, L. Stochastic model predictive control for economic/environmental operation management of microgrids: An experimental case study. Journal of Process Control vol. 43 24–37 (2016) -- [10.1016/j.jprocont.2016.04.008](https://doi.org/10.1016/j.jprocont.2016.04.008)
- Pham, (2015)
- [Polyuga, R. V. & van der Schaft, A. Structure preserving model reduction of port-Hamiltonian systems by moment matching at infinity. Automatica vol. 46 665–672 (2010)](structure-preserving-model-reduction-of-port-hamiltonian-systems-by-moment-matching-at-infinity) -- [10.1016/j.automatica.2010.01.018](https://doi.org/10.1016/j.automatica.2010.01.018)
- Prodan, I. & Zio, E. A model predictive control framework for reliable microgrid energy management. International Journal of Electrical Power &amp; Energy Systems vol. 61 399–409 (2014) -- [10.1016/j.ijepes.2014.03.017](https://doi.org/10.1016/j.ijepes.2014.03.017)
- [Schiffer, J., Fridman, E., Ortega, R. & Raisch, J. Stability of a class of delayed port-Hamiltonian systems with application to microgrids with distributed rotational and electronic generation. Automatica vol. 74 71–79 (2016)](stability-of-a-class-of-delayed-port-hamiltonian-systems-with-application-to-microgrids-with-distributed-rotational-and-electronic-generation) -- [10.1016/j.automatica.2016.07.022](https://doi.org/10.1016/j.automatica.2016.07.022)
- Shafiee, Q., Guerrero, J. M. & Vasquez, J. C. Distributed Secondary Control for Islanded Microgrids—A Novel Approach. IEEE Transactions on Power Electronics vol. 29 1018–1031 (2014) -- [10.1109/tpel.2013.2259506](https://doi.org/10.1109/tpel.2013.2259506)
- Siad, S. B., Malkawi, A., Damm, G., Lopes, L. & Dol, L. G. Nonlinear control of a DC MicroGrid for the integration of distributed generation based on different time scales. International Journal of Electrical Power &amp; Energy Systems vol. 111 93–100 (2019) -- [10.1016/j.ijepes.2019.03.073](https://doi.org/10.1016/j.ijepes.2019.03.073)
- Simpson-Porco, J. W. et al. Secondary Frequency and Voltage Control of Islanded Microgrids via Distributed Averaging. IEEE Transactions on Industrial Electronics vol. 62 7025–7038 (2015) -- [10.1109/tie.2015.2436879](https://doi.org/10.1109/tie.2015.2436879)
- Stoican, Constrained trajectory generation for uav systems using a b-spline parametrization. (2017)
- Suryawan, (2012)
- Takagi, T. & Sugeno, M. Fuzzy identification of systems and its applications to modeling and control. IEEE Transactions on Systems, Man, and Cybernetics vol. SMC-15 116–132 (1985) -- [10.1109/tsmc.1985.6313399](https://doi.org/10.1109/tsmc.1985.6313399)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Vu, T. V. et al. Robust adaptive droop control for DC microgrids. Electric Power Systems Research vol. 146 95–106 (2017) -- [10.1016/j.epsr.2017.01.021](https://doi.org/10.1016/j.epsr.2017.01.021)
- Wang, B. et al. Hybrid energy storage system using bidirectional single-inductor multiple-port converter with model predictive control in DC microgrids. Electric Power Systems Research vol. 173 38–47 (2019) -- [10.1016/j.epsr.2019.03.015](https://doi.org/10.1016/j.epsr.2019.03.015)
- Wang, P., Lu, X., Yang, X., Wang, W. & Xu, D. An Improved Distributed Secondary Control Method for DC Microgrids With Enhanced Dynamic Current Sharing Performance. IEEE Transactions on Power Electronics vol. 31 6658–6673 (2016) -- [10.1109/tpel.2015.2499310](https://doi.org/10.1109/tpel.2015.2499310)
- Xie, X., Yue, D., Zhang, H. & Peng, C. Control Synthesis of Discrete-Time T–S Fuzzy Systems: Reducing the Conservatism Whilst Alleviating the Computational Burden. IEEE Transactions on Cybernetics vol. 47 2480–2491 (2017) -- [10.1109/tcyb.2016.2582747](https://doi.org/10.1109/tcyb.2016.2582747)
- [Zafeiratou, I., Nguyen, D. V. A., Prodan, I., Lefèvre, L. & Piétrac, L. Flatness-based hierarchical control of a meshed DC microgrid. IFAC-PapersOnLine vol. 51 222–227 (2018)](flatness-based-hierarchical-control-of-a-meshed-dc-microgrid) -- [10.1016/j.ifacol.2018.11.017](https://doi.org/10.1016/j.ifacol.2018.11.017)
- [Zafeiratou, I., Prodan, I., Lefèvre, L. & Piétrac, L. Dynamical modelling of a DC microgrid using a port-Hamiltonian formalism. IFAC-PapersOnLine vol. 51 469–474 (2018)](dynamical-modelling-of-a-dc-microgrid-using-a-port-hamiltonian-formalism) -- [10.1016/j.ifacol.2018.03.079](https://doi.org/10.1016/j.ifacol.2018.03.079)

