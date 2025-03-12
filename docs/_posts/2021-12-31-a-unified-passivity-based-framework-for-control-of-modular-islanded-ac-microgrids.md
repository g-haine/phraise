---
layout: post
title: "A Unified Passivity-Based Framework for Control of Modular Islanded AC Microgrids"
date: 2021-12-31 00:00:00 +0100
permalink: a-unified-passivity-based-framework-for-control-of-modular-islanded-ac-microgrids
year: 2022
authors: Felix Strehle, Pulkit Nahata, Albertus Johannes Malan, Soren Hohmann, Giancarlo Ferrari-Trecate
category: articles
---
 
## Authors
[Felix Strehle](authors/felix-strehle), [Pulkit Nahata](authors/pulkit-nahata), [Albertus Johannes Malan](authors/albertus-johannes-malan), [Soren Hohmann](authors/soren-hohmann), [Giancarlo Ferrari-Trecate](authors/giancarlo-ferrari-trecate)
 
## Abstract
Voltage and frequency control in an islanded ac microgrid (ImG) amounts to stabilizing an a priori unknown ImG equilibrium induced by loads and changes in topology. This article puts forth a unified control framework, which, while guaranteeing such stability, allows for modular ImGs interconnecting multiple subsystems, that is, dynamic \\( RLC \\) lines, nonlinear constant impedance, current, power (ZIP) and exponential (EXP) loads, and inverter-based distributed generation units (DGUs) controlled with different types of primary controllers. The underlying idea of the framework is based on the equilibrium-independent passivity (EIP) of the ImG subsystems, which enables stability certificates of ImG equilibria without explicit knowledge of these equilibria. In order to render DGUs EIP, we propose a decentralized controller synthesis algorithm based on port-Hamiltonian systems (PHSs). We also show that EIP, being the key to stability, provides a general framework, which can embrace other solutions available in the literature. Furthermore, we provide a novel argument based on LaSalle’s theorem for proving asymptotic voltage and frequency stability. Finally, we analyze the impact of actuator saturation on the stability results by exploiting the inherent EIP properties of the PHS DGU model. Theoretical findings are backed up by realistic simulations based on the medium-voltage CIGRE benchmark network.
 
## Citation
- **Journal:** IEEE Transactions on Control Systems Technology
- **Year:** 2022
- **Volume:** 30
- **Issue:** 5
- **Pages:** 1960--1976
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tcst.2021.3136489](https://doi.org/10.1109/tcst.2021.3136489)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Strehle_2022,
  title={{A Unified Passivity-Based Framework for Control of Modular Islanded AC Microgrids}},
  volume={30},
  ISSN={2374-0159},
  DOI={10.1109/tcst.2021.3136489},
  number={5},
  journal={IEEE Transactions on Control Systems Technology},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Strehle, Felix and Nahata, Pulkit and Malan, Albertus Johannes and Hohmann, Soren and Ferrari-Trecate, Giancarlo},
  year={2022},
  pages={1960--1976}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-unified-passivity-based-framework-for-control-of-modular-islanded-ac-microgrids.bib)
 
## References
- Lasseter, B. Microgrids [distributed power generation]. 2001 IEEE Power Engineering Society Winter Meeting. Conference Proceedings (Cat. No.01CH37194) (2001) doi:10.1109/pesw.2001.917020 -- [10.1109/pesw.2001.917020](https://doi.org/10.1109/pesw.2001.917020)
- Schiffer, J. et al. A survey on modeling of microgrids—From fundamental physics to phasors and voltage sources. Automatica vol. 74 135–150 (2016) -- [10.1016/j.automatica.2016.07.036](https://doi.org/10.1016/j.automatica.2016.07.036)
- Olivares, D. E. et al. Trends in Microgrid Control. IEEE Transactions on Smart Grid vol. 5 1905–1919 (2014) -- [10.1109/tsg.2013.2295514](https://doi.org/10.1109/tsg.2013.2295514)
- Guerrero, J. M., Chandorkar, M., Lee, T.-L. & Loh, P. C. Advanced Control Architectures for Intelligent Microgrids—Part I: Decentralized and Hierarchical Control. IEEE Transactions on Industrial Electronics vol. 60 1254–1262 (2013) -- [10.1109/tie.2012.2194969](https://doi.org/10.1109/tie.2012.2194969)
- Farrokhabadi, M. et al. Microgrid Stability Definitions, Analysis, and Examples. IEEE Transactions on Power Systems vol. 35 13–29 (2020) -- [10.1109/tpwrs.2019.2925703](https://doi.org/10.1109/tpwrs.2019.2925703)
- Dorfler, F., Bolognani, S., Simpson-Porco, J. W. & Grammatico, S. Distributed Control and Optimization for Autonomous Power Grids. 2019 18th European Control Conference (ECC) 2436–2453 (2019) doi:10.23919/ecc.2019.8795974 -- [10.23919/ecc.2019.8795974](https://doi.org/10.23919/ecc.2019.8795974)
- Dorfler, F., Simpson-Porco, J. W. & Bullo, F. Plug-and-play control and optimization in microgrids. 53rd IEEE Conference on Decision and Control 211–216 (2014) doi:10.1109/cdc.2014.7039383 -- [10.1109/cdc.2014.7039383](https://doi.org/10.1109/cdc.2014.7039383)
- [Schiffer, J., Ortega, R., Astolfi, A., Raisch, J. & Sezi, T. Conditions for stability of droop-controlled inverter-based microgrids. Automatica vol. 50 2457–2469 (2014)](conditions-for-stability-of-droop-controlled-inverter-based-microgrids) -- [10.1016/j.automatica.2014.08.009](https://doi.org/10.1016/j.automatica.2014.08.009)
- Simpson-Porco, J. W., Dorfler, F. & Bullo, F. Voltage Stabilization in Microgrids via Quadratic Droop Control. IEEE Transactions on Automatic Control vol. 62 1239–1253 (2017) -- [10.1109/tac.2016.2585094](https://doi.org/10.1109/tac.2016.2585094)
- Zhong, Q.-C. Robust Droop Controller for Accurate Proportional Load Sharing Among Inverters Operated in Parallel. IEEE Transactions on Industrial Electronics vol. 60 1281–1290 (2013) -- [10.1109/tie.2011.2146221](https://doi.org/10.1109/tie.2011.2146221)
- Kolluri, R. R. et al. Stability and active power sharing in droop controlled inverter interfaced microgrids: Effect of clock mismatches. Automatica vol. 93 469–475 (2018) -- [10.1016/j.automatica.2018.03.025](https://doi.org/10.1016/j.automatica.2018.03.025)
- Simpson-Porco, J. W., Dörfler, F. & Bullo, F. Synchronization and power sharing for droop-controlled inverters in islanded microgrids. Automatica vol. 49 2603–2611 (2013) -- [10.1016/j.automatica.2013.05.018](https://doi.org/10.1016/j.automatica.2013.05.018)
- Etemadi, A. H., Davison, E. J. & Iravani, R. A Decentralized Robust Control Strategy for Multi-DER Microgrids—Part I: Fundamental Concepts. IEEE Transactions on Power Delivery vol. 27 1843–1853 (2012) -- [10.1109/tpwrd.2012.2202920](https://doi.org/10.1109/tpwrd.2012.2202920)
- Etemadi, A. H., Davison, E. J. & Iravani, R. A Decentralized Robust Control Strategy for Multi-DER Microgrids—Part II: Performance Evaluation. IEEE Transactions on Power Delivery vol. 27 1854–1861 (2012) -- [10.1109/tpwrd.2012.2202921](https://doi.org/10.1109/tpwrd.2012.2202921)
- Babazadeh, M. & Karimi, H. A Robust Two-Degree-of-Freedom Control Strategy for an Islanded Microgrid. IEEE Transactions on Power Delivery vol. 28 1339–1347 (2013) -- [10.1109/tpwrd.2013.2254138](https://doi.org/10.1109/tpwrd.2013.2254138)
- Riverso, S., Sarzo, F. & Ferrari-Trecate, G. Plug-and-Play Voltage and Frequency Control of Islanded Microgrids With Meshed Topology. IEEE Transactions on Smart Grid vol. 6 1176–1184 (2015) -- [10.1109/tsg.2014.2381093](https://doi.org/10.1109/tsg.2014.2381093)
- Tucci, M. & Ferrari-Trecate, G. Voltage and frequency control in AC islanded microgrids: a scalable, line-independent design algorithm. IFAC-PapersOnLine vol. 50 13922–13927 (2017) -- [10.1016/j.ifacol.2017.08.2212](https://doi.org/10.1016/j.ifacol.2017.08.2212)
- Sadabadi, M. S., Shafiee, Q. & Karimi, A. Plug-and-Play Voltage Stabilization in Inverter-Interfaced Microgrids via a Robust Control Strategy. IEEE Transactions on Control Systems Technology vol. 25 781–791 (2017) -- [10.1109/tcst.2016.2583378](https://doi.org/10.1109/tcst.2016.2583378)
- Nahata, P. & Ferrari-Treeate, G. Passivity-based Voltage and Frequency Stabilization in AC microgrids. 2019 18th European Control Conference (ECC) 1890–1895 (2019) doi:10.23919/ecc.2019.8796119 -- [10.23919/ecc.2019.8796119](https://doi.org/10.23919/ecc.2019.8796119)
- Strehle, F., Malan, A. J., Krebs, S. & Hohmann, S. A Port-Hamiltonian Approach to Plug-and-Play Voltage and Frequency Control in Islanded Inverter-Based AC Microgrids. 2019 IEEE 58th Conference on Decision and Control (CDC) 4648–4655 (2019) doi:10.1109/cdc40024.2019.9029272 -- [10.1109/cdc40024.2019.9029272](https://doi.org/10.1109/cdc40024.2019.9029272)
- Watson, J. D., Ojo, Y., Laib, K. & Lestas, I. A Scalable Control Design for Grid-Forming Inverters in Microgrids. IEEE Transactions on Smart Grid vol. 12 4726–4739 (2021) -- [10.1109/tsg.2021.3105730](https://doi.org/10.1109/tsg.2021.3105730)
- Shafiee-Rad, M., Shafiee, Q., Sadabadi, M. S. & Jahed-Motlagh, M. R. Decentralized Voltage Stabilization and Robust Performance Satisfaction of Islanded Inverter-Interfaced Microgrids. IEEE Systems Journal vol. 15 1893–1904 (2021) -- [10.1109/jsyst.2020.2994406](https://doi.org/10.1109/jsyst.2020.2994406)
- Watson, J., Ojo, Y., Lestas, I. & Spanias, C. Stability of power networks with grid-forming converters. 2019 IEEE Milan PowerTech 1–6 (2019) doi:10.1109/ptc.2019.8810506 -- [10.1109/ptc.2019.8810506](https://doi.org/10.1109/ptc.2019.8810506)
- Miao, X. & Ilic, M. D. Modeling and Distributed Control of Microgrids: A Negative Feedback Approach. 2019 IEEE 58th Conference on Decision and Control (CDC) 1937–1944 (2019) doi:10.1109/cdc40024.2019.9029420 -- [10.1109/cdc40024.2019.9029420](https://doi.org/10.1109/cdc40024.2019.9029420)
- [Fiaz, S., Zonetti, D., Ortega, R., Scherpen, J. M. A. & van der Schaft, A. J. A port-Hamiltonian approach to power network modeling and analysis. European Journal of Control vol. 19 477–485 (2013)](a-port-hamiltonian-approach-to-power-network-modeling-and-analysis) -- [10.1016/j.ejcon.2013.09.002](https://doi.org/10.1016/j.ejcon.2013.09.002)
- [van der Schaft, A. & Stegink, T. Perspectives in modeling for control of power networks. Annual Reviews in Control vol. 41 119–132 (2016)](perspectives-in-modeling-for-control-of-power-networks) -- [10.1016/j.arcontrol.2016.04.017](https://doi.org/10.1016/j.arcontrol.2016.04.017)
- Gui, Y., Wei, B., Li, M., Guerrero, J. M. & Vasquez, J. C. Passivity-based coordinated control for islanded AC microgrid. Applied Energy vol. 229 551–561 (2018) -- [10.1016/j.apenergy.2018.07.115](https://doi.org/10.1016/j.apenergy.2018.07.115)
- [Monshizadeh, P., Machado, J. E., Ortega, R. & van der Schaft, A. Power-controlled Hamiltonian systems: Application to electrical systems with constant power loads. Automatica vol. 109 108527 (2019)](power-controlled-hamiltonian-systems-application-to-electrical-systems-with-constant-power-loads) -- [10.1016/j.automatica.2019.108527](https://doi.org/10.1016/j.automatica.2019.108527)
- Spanias, C., Aristidou, P. & Michaelides, M. A Passivity-Based Framework for Stability Analysis and Control Including Power Network Dynamics. IEEE Systems Journal vol. 15 5000–5010 (2021) -- [10.1109/jsyst.2020.3007582](https://doi.org/10.1109/jsyst.2020.3007582)
- Cucuzzella, M., Trip, S., Ferrara, A. & Scherpen, J. Cooperative Voltage Control in AC Microgrids. 2018 IEEE Conference on Decision and Control (CDC) 6723–6728 (2018) doi:10.1109/cdc.2018.8618898 -- [10.1109/cdc.2018.8618898](https://doi.org/10.1109/cdc.2018.8618898)
- Perez, M., Ortega, R. & Espinoza, J. Passivity-Based PI Control of Switched Power Converters. IEEE Transactions on Control Systems Technology vol. 12 881–890 (2004) -- [10.1109/tcst.2004.833628](https://doi.org/10.1109/tcst.2004.833628)
- Zhong, Q.-C. & Stefanello, M. Port-hamiltonian control of power electronic converters to achieve passivity. 2017 IEEE 56th Annual Conference on Decision and Control (CDC) 5092–5097 (2017) doi:10.1109/cdc.2017.8264413 -- [10.1109/cdc.2017.8264413](https://doi.org/10.1109/cdc.2017.8264413)
- Serra, F. M., De Angelo, C. H. & Forchetti, D. G. IDA-PBC control of a DC–AC converter for sinusoidal three-phase voltage generation. International Journal of Electronics vol. 104 93–110 (2016) -- [10.1080/00207217.2016.1191087](https://doi.org/10.1080/00207217.2016.1191087)
- Tucci, A scalable, line-independent control design algorithm for voltage and frequency stabilization in AC islanded microgrids. arXiv (2018)
- Hines, G. H., Arcak, M. & Packard, A. K. Equilibrium-independent passivity: A new definition and numerical certification. Automatica vol. 47 1949–1956 (2011) -- [10.1016/j.automatica.2011.05.011](https://doi.org/10.1016/j.automatica.2011.05.011)
- Bürger, M., Zelazo, D. & Allgöwer, F. Duality and network theory in passivity-based cooperative control. Automatica vol. 50 2051–2061 (2014) -- [10.1016/j.automatica.2014.06.002](https://doi.org/10.1016/j.automatica.2014.06.002)
- Arcak, M., Meissen, C. & Packard, A. Networks of Dissipative Systems. SpringerBriefs in Electrical and Computer Engineering (Springer International Publishing, 2016). doi:10.1007/978-3-319-29928-0 -- [10.1007/978-3-319-29928-0](https://doi.org/10.1007/978-3-319-29928-0)
- van der Schaft, A. L2-Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer International Publishing, 2017). doi:10.1007/978-3-319-49992-5 -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- Bobtsov, A., Ortega, R., Nikolaev, N. & He, W. A globally stable practically implementable PI passivity‐based controller for switched power converters. International Journal of Adaptive Control and Signal Processing vol. 35 2155–2174 (2021) -- [10.1002/acs.3312](https://doi.org/10.1002/acs.3312)
- Strehle, F., Malan, A. J., Krebs, S. & Hohmann, S. Passivity Conditions for Plug-and-Play Operation of Nonlinear Static AC Loads. IFAC-PapersOnLine vol. 53 12237–12243 (2020) -- [10.1016/j.ifacol.2020.12.1128](https://doi.org/10.1016/j.ifacol.2020.12.1128)
- Strunz, Benchmark systems for network integration of renewable and distributed energy resources. (2014)
- Jayawardhana, B., Ortega, R., García-Canseco, E. & Castaños, F. Passivity of nonlinear incremental systems: Application to PI stabilization of nonlinear RLC circuits. Systems &amp; Control Letters vol. 56 618–622 (2007) -- [10.1016/j.sysconle.2007.03.011](https://doi.org/10.1016/j.sysconle.2007.03.011)
- Stan, G.-B. & Sepulchre, R. Analysis of Interconnected Oscillators by Dissipativity Theory. IEEE Transactions on Automatic Control vol. 52 256–270 (2007) -- [10.1109/tac.2006.890471](https://doi.org/10.1109/tac.2006.890471)
- Simpson-Porco, J. W. Equilibrium-Independent Dissipativity With Quadratic Supply Rates. IEEE Transactions on Automatic Control vol. 64 1440–1455 (2019) -- [10.1109/tac.2018.2838664](https://doi.org/10.1109/tac.2018.2838664)
- Akagi, H., Watanabe, E. H. & Aredes, M. Instantaneous Power Theory and Applications to Power Conditioning. (2006) doi:10.1002/0470118938 -- [10.1002/0470118938](https://doi.org/10.1002/0470118938)
- Machowski, Power System Dynamics: Stability and Control (2008)
- Baimel, D., Belikov, J., Guerrero, J. M. & Levron, Y. Dynamic Modeling of Networks, Microgrids, and Renewable Sources in the dq0 Reference Frame: A Survey. IEEE Access vol. 5 21323–21335 (2017) -- [10.1109/access.2017.2758523](https://doi.org/10.1109/access.2017.2758523)
- Farrokhabadi, Microgrid stability definitions, analysis, and modeling. (2018)
- Kundur, Power System Stability and Control (1994)
- Borutzky, Bond Graph Methodology—Development and Analysis of Multidisciplinay Dynamic System Models (2010)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Pfeifer, M. et al. Explicit Port-Hamiltonian Formulation of Bond Graphs with Dependent Storages. IFAC-PapersOnLine vol. 53 5579–5585 (2020)](explicit-port-hamiltonian-formulation-of-bond-graphs-with-dependent-storages) -- [10.1016/j.ifacol.2020.12.1570](https://doi.org/10.1016/j.ifacol.2020.12.1570)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- [Kotyczka, P. Local linear dynamics assignment in IDA-PBC. Automatica vol. 49 1037–1044 (2013)](local-linear-dynamics-assignment-in-ida-pbc) -- [10.1016/j.automatica.2013.01.028](https://doi.org/10.1016/j.automatica.2013.01.028)
- [Donaire, A. & Junco, S. On the addition of integral action to port-controlled Hamiltonian systems. Automatica vol. 45 1910–1916 (2009)](on-the-addition-of-integral-action-to-port-controlled-hamiltonian-systems) -- [10.1016/j.automatica.2009.04.006](https://doi.org/10.1016/j.automatica.2009.04.006)
- Nahata, P., Soloperto, R., Tucci, M., Martinelli, A. & Ferrari-Trecate, G. A passivity-based approach to voltage stabilization in DC microgrids with ZIP loads. Automatica vol. 113 108770 (2020) -- [10.1016/j.automatica.2019.108770](https://doi.org/10.1016/j.automatica.2019.108770)
- Nahata, P., Bella, A. L., Scattolini, R. & Ferrari-Trecate, G. Hierarchical Control in Islanded DC Microgrids With Flexible Structures. IEEE Transactions on Control Systems Technology vol. 29 2379–2392 (2021) -- [10.1109/tcst.2020.3038495](https://doi.org/10.1109/tcst.2020.3038495)
- Åström, Advanced PID control (2006)

