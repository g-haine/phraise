---
title: "Adaptive Passivity-Based Control for DC Motor Speed Regulation in DC-DC Converter-Fed Systems"
date: 2025-07-24 00:00:00 +0100
permalink: adaptive-passivity-based-control-for-dc-motor-speed-regulation-in-dc-dc-converter-fed-systems
year: 2025
authors: Diego Montoya Acevedo, Ignacio Parraguez-Garrido, Walter Gil-González, Oscar Danilo Montoya, Catalina González-Castaño
category: articles
---
 
## Authors
[Diego Montoya Acevedo](authors/diego-a-montoya-acevedo), [Ignacio Parraguez-Garrido](authors/ignacio-parraguez-garrido), [Walter Gil-González](authors/walter-julian-gil-gonzalez), [Oscar Danilo Montoya](authors/oscar-danilo-montoya), [Catalina González-Castaño](authors/catalina-gonzalez-castano)
 
## Abstract
This paper presents a unified adaptive passivity-based control strategy using incremental modeling to regulate the angular speed of a DC series motor driven by DC-DC converters operating in both buck and boost configurations. The proposed approach leverages an incremental port-Hamiltonian framework to design control laws that ensure the global asymptotic stability of the closed-loop system. To address the challenge posed by unknown load torques, a nonlinear disturbance observer is incorporated, allowing for the real-time estimation required for an accurate computation of equilibrium points and reference tracking. These theoretical developments are validated through experimental implementation and compared against an inverse optimal control (IOC) strategy. The results show that the proposed IDA-PBC significantly outperforms the IOC in terms of transient response, tracking accuracy, and disturbance rejection. In the buck configuration, the IDA-PBC reduces the rise time by up to 50.24% and completely eliminates the overshoot. Similarly, in the boost configuration, the rise time is improved by 20.63%, with enhanced stability and lower phase lag under sinusoidal tracking. These findings confirm the robustness and effectiveness of the proposed control strategy for real-time applications in electromechanical systems.
 
## Citation
- **Journal:** IEEE Access
- **Year:** 2025
- **Volume:** 13
- **Issue:** 
- **Pages:** 131957--131966
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/access.2025.3592594](https://doi.org/10.1109/access.2025.3592594)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Acevedo_2025,
  title={{Adaptive Passivity-Based Control for DC Motor Speed Regulation in DC-DC Converter-Fed Systems}},
  volume={13},
  ISSN={2169-3536},
  DOI={10.1109/access.2025.3592594},
  journal={IEEE Access},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Acevedo, Diego Montoya and Parraguez-Garrido, Ignacio and Gil-González, Walter and Montoya, Oscar Danilo and González-Castaño, Catalina},
  year={2025},
  pages={131957--131966}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/adaptive-passivity-based-control-for-dc-motor-speed-regulation-in-dc-dc-converter-fed-systems.bib)
 
## References
- Gorji, S. A., Sahebi, H. G., Ektesabi, M. & Rad, A. B. Topologies and Control Schemes of Bidirectional DC–DC Power Converters: An Overview. IEEE Access 7, 117997–118019 (2019) -- [10.1109/access.2019.2937239](https://doi.org/10.1109/access.2019.2937239)
- Coelho, S., Monteiro, V. & Afonso, J. L. Topological Advances in Isolated DC–DC Converters: High-Efficiency Design for Renewable Energy Integration. Sustainability 17, 2336 (2025) -- [10.3390/su17062336](https://doi.org/10.3390/su17062336)
- Muhammad Hilal Mthboob, ALRikabi, H. & A. Aljazaery, I. A concepts and techniques related to the DC motor speed control system design: Systematic Review. WJCMS 2, 59–73 (2023) -- [10.31185/wjcm.121](https://doi.org/10.31185/wjcm.121)
- Elp, H. E., Altug, H. & İnan, R. Designing a Brushed DC Motor Driver with a Novel Adaptive Learning Algorithm for the Automotive Industry. Electronics 13, 4344 (2024) -- [10.3390/electronics13224344](https://doi.org/10.3390/electronics13224344)
- Modern Electric, Hybrid Electric, and Fuel Cell Vehicles, Third Edition. (CRC Press, 2018). doi:10.1201/9780429504884 -- [10.1201/9780429504884](https://doi.org/10.1201/9780429504884)
- Kaźmierkowski, Control in Power Electronics: Selected Problems (2002)
- Linares-Flores, J., Barahona-Avalos, J. L., Sira-Ramirez, H. & Contreras-Ordaz, M. A. Robust Passivity-Based Control of a Buck–Boost-Converter/DC-Motor System: An Active Disturbance Rejection Approach. IEEE Trans. on Ind. Applicat. 48, 2362–2371 (2012) -- [10.1109/tia.2012.2227098](https://doi.org/10.1109/tia.2012.2227098)
- Khalid, M. Passivity-Based Nonlinear Control Approach for Efficient Energy Management in Fuel Cell Hybrid Electric Vehicles. IEEE Access 12, 84169–84188 (2024) -- [10.1109/access.2024.3412888](https://doi.org/10.1109/access.2024.3412888)
- Putting energy back in control. IEEE Control Syst. 21, 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- [van der Schaft, A. J. Port-Hamiltonian Differential-Algebraic Systems. Surveys in Differential-Algebraic Equations I 173–226 (2013) doi:10.1007/978-3-642-34928-7_5](port-hamiltonian-differential-algebraic-systems) -- [10.1007/978-3-642-34928-7_5](https://doi.org/10.1007/978-3-642-34928-7_5)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Serra, F. M. & De Angelo, C. H. IDA-PBC controller design for grid connected Front End Converters under non-ideal grid conditions. Electric Power Systems Research 142, 12–19 (2017) -- [10.1016/j.epsr.2016.08.041](https://doi.org/10.1016/j.epsr.2016.08.041)
- Gil-González, W. & Montoya, O. D. Passivity-based PI control of a SMES system to support power in electrical grids: A bilinear approach. Journal of Energy Storage 18, 459–466 (2018) -- [10.1016/j.est.2018.05.020](https://doi.org/10.1016/j.est.2018.05.020)
- Belkhier, Y., Fredj, S., Rashid, H. & Benbouzid, M. Robust nonlinear control of permanent magnet synchronous motor drives: An evolutionary algorithm optimized passivity-based control approach with a high-order sliding mode observer. Engineering Applications of Artificial Intelligence 145, 110256 (2025) -- [10.1016/j.engappai.2025.110256](https://doi.org/10.1016/j.engappai.2025.110256)
- [Meshram, R. V. et al. Port-Controlled Phasor Hamiltonian Modeling and IDA-PBC Control of Solid-State Transformer. IEEE Trans. Contr. Syst. Technol. 27, 161–174 (2019)](port-controlled-phasor-hamiltonian-modeling-and-ida-pbc-control-of-solid-state-transformer) -- [10.1109/tcst.2017.2761866](https://doi.org/10.1109/tcst.2017.2761866)
- Krstic, Nonlinear and Adaptive Control Design (1995)
- Ding, S., Chen, W.-H., Mei, K. & Murray-Smith, D. J. Disturbance Observer Design for Nonlinear Systems Represented by Input–Output Models. IEEE Trans. Ind. Electron. 67, 1222–1232 (2020) -- [10.1109/tie.2019.2898585](https://doi.org/10.1109/tie.2019.2898585)
- [Montoya, O. D., Serra, F. M. & Espinosa-Pérez, G. On the Equivalence Between PI-PBC and IOC Designs: An Application Involving Three-Phase Front-End Converters. IEEE Trans. Circuits Syst. II 71, 241–245 (2024)](on-the-equivalence-between-pi-pbc-and-ioc-designs-an-application-involving-three-phase-front-end-converters) -- [10.1109/tcsii.2023.3299203](https://doi.org/10.1109/tcsii.2023.3299203)
- Ortega, R., Romero, J. G., Borja, P. & Donaire, A. PID Passivity‐Based Control of Nonlinear Systems with Applications. (2021) doi:10.1002/9781119694199 -- [10.1002/9781119694199](https://doi.org/10.1002/9781119694199)
- Riffo, S., Gil-González, W., Montoya, O. D., Restrepo, C. & Muñoz, J. Adaptive Sensorless PI+Passivity-Based Control of a Boost Converter Supplying an Unknown CPL. Mathematics 10, 4321 (2022) -- [10.3390/math10224321](https://doi.org/10.3390/math10224321)
- Montoya, O. D., Serra, F. M., Gil-González, W., Asensio, E. M. & Bosso, J. E. An IDA-PBC Design with Integral Action for Output Voltage Regulation in an Interleaved Boost Converter for DC Microgrid Applications. Actuators 11, 5 (2021) -- [10.3390/act11010005](https://doi.org/10.3390/act11010005)
- Serra, F. M., Magaldi, G. L., Martin Fernandez, L. L., Larregay, G. O. & De Angelo, C. H. IDA-PBC controller of a DC-DC boost converter for continuous and discontinuous conduction mode. IEEE Latin Am. Trans. 16, 52–58 (2018) -- [10.1109/tla.2018.8291454](https://doi.org/10.1109/tla.2018.8291454)
- Kazimierczuk, M. K. Pulse‐Width Modulated DC‐DC Power Converters. (2008) doi:10.1002/9780470694640 -- [10.1002/9780470694640](https://doi.org/10.1002/9780470694640)
- Montoya-Acevedo, D., Gil-González, W., Montoya, O. D., Restrepo, C. & González-Castaño, C. Adaptive Speed Control for a DC Motor Using DC/DC Converters: An Inverse Optimal Control Approach. IEEE Access 12, 154503–154513 (2024) -- [10.1109/access.2024.3482982](https://doi.org/10.1109/access.2024.3482982)
- Yildiz, A. B. & Bilgin, M. Z. Speed Control of Averaged DC Motor Drive System by Using Neuro-PID Controller. Lecture Notes in Computer Science 1075–1082 (2006) doi:10.1007/11892960_129 -- [10.1007/11892960_129](https://doi.org/10.1007/11892960_129)
- Guerrero, E. et al. DC Motor Speed Control through Parallel DC/DC Buck Converters. IEEE Latin Am. Trans. 15, 819–826 (2017) -- [10.1109/tla.2017.7910194](https://doi.org/10.1109/tla.2017.7910194)
- Suriadi et al. DC motor speed control using boost converter DC-DC chopper type based on the PID controller. IOP Conf. Ser.: Earth Environ. Sci. 1356, 012083 (2024) -- [10.1088/1755-1315/1356/1/012083](https://doi.org/10.1088/1755-1315/1356/1/012083)
- Sira-Ramirez, H., Perez-Moreno, R. A., Ortega, R. & Garcia-Esteban, M. Passivity-based controllers for the stabilization of Dc-to-Dc Power converters. Automatica 33, 499–513 (1997) -- [10.1016/s0005-1098(96)00207-5](https://doi.org/10.1016/s0005-1098(96)00207-5)
- Barman, S., Samanta, S., Mishra, J. P., Roy, P. & Roy, B. K. Design and Implementation of an IDA-PBC for a Grid Connected Inverter used in a Photovoltaic System. IFAC-PapersOnLine 51, 680–685 (2018) -- [10.1016/j.ifacol.2018.05.114](https://doi.org/10.1016/j.ifacol.2018.05.114)
- Montoya, O. D., Gil-González, W., Garcés, A. & Espinosa-Pérez, G. Indirect IDA-PBC for active and reactive power support in distribution networks using SMES systems with PWM-CSC. Journal of Energy Storage 17, 261–271 (2018) -- [10.1016/j.est.2018.03.004](https://doi.org/10.1016/j.est.2018.03.004)
- Thounthong, P. et al. Improved Adaptive Hamiltonian Control Law for Constant Power Load Stability Issue in DC Microgrid: Case Study for Multiphase Interleaved Fuel Cell Boost Converter. Sustainability 13, 8093 (2021) -- [10.3390/su13148093](https://doi.org/10.3390/su13148093)

