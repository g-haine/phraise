---
title: "Comparative Performance Analysis of the DC-AC Converter Control System Based on Linear Robust or Nonlinear PCH Controllers and Reinforcement Learning Agent"
date: 2022-12-07 00:00:00 +0100
permalink: comparative-performance-analysis-of-the-dc-ac-converter-control-system-based-on-linear-robust-or-nonlinear-pch-controllers-and-reinforcement-learning-agent
year: 2022
authors: Marcel Nicola, Claudiu-Ionel Nicola
category: articles
---
 
## Authors
[Marcel Nicola](authors/marcel-nicola), [Claudiu-Ionel Nicola](authors/claudiu-ionel-nicola)
 
## Abstract
Starting from the general topology and the main elements that connect a microgrid represented by a DC power source to the main grid, this article presents the performance of the control system of a DC-AC converter. The main elements of this topology are the voltage source inverter represented by a DC-AC converter and the network filters. The active Insulated Gate Bipolar Transistor (IGBT) or Metal–Oxide–Semiconductor Field-Effect Transistor (MOSFET) elements of the DC-AC converter are controlled by robust linear or nonlinear Port Controlled Hamiltonian (PCH) controllers. The outputs of these controllers are modulation indices which are inputs to a Pulse-Width Modulation (PWM) system that provides the switching signals for the active elements of the DC-AC converter. The purpose of the DC-AC converter control system is to maintain ud and uq voltages to the prescribed reference values where there is a variation of the three-phase load, which may be of balanced/unbalanced or nonlinear type. The controllers are classic PI, robust or nonlinear PCH, and their performance is improved by the use of a properly trained Reinforcement Learning-Twin Delayed Deep Deterministic Policy Gradient (RL-TD3) agent. The performance of the DC-AC converter control systems is compared using performance indices such as steady-state error, error ripple and Total Harmonic Distortion (THD) current value. Numerical simulations are performed in Matlab/Simulink and conclude the superior performance of the nonlinear PCH controller and the improvement of the performance of each controller presented by using an RL-TD3 agent, which provides correction signals to improve the performance of the DC-AC converter control systems when it is properly trained.
 
## Citation
- **Journal:** Sensors
- **Year:** 2022
- **Volume:** 22
- **Issue:** 23
- **Pages:** 9535
- **Publisher:** MDPI AG
- **DOI:** [10.3390/s22239535](https://doi.org/10.3390/s22239535)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Nicola_2022,
  title={{Comparative Performance Analysis of the DC-AC Converter Control System Based on Linear Robust or Nonlinear PCH Controllers and Reinforcement Learning Agent}},
  volume={22},
  ISSN={1424-8220},
  DOI={10.3390/s22239535},
  number={23},
  journal={Sensors},
  publisher={MDPI AG},
  author={Nicola, Marcel and Nicola, Claudiu-Ionel},
  year={2022},
  pages={9535}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/comparative-performance-analysis-of-the-dc-ac-converter-control-system-based-on-linear-robust-or-nonlinear-pch-controllers-and-reinforcement-learning-agent.bib)
 
## References
- Azeem, A. et al. Deterioration of Electrical Load Forecasting Models in a Smart Grid Environment. Sensors 22, 4363 (2022) -- [10.3390/s22124363](https://doi.org/10.3390/s22124363)
- Fotopoulou, M., Rakopoulos, D. & Blanas, O. Day Ahead Optimal Dispatch Schedule in a Smart Grid Containing Distributed Energy Resources and Electric Vehicles. Sensors 21, 7295 (2021) -- [10.3390/s21217295](https://doi.org/10.3390/s21217295)
- Das, P. P., Chatterjee, D. & Kadavelugu, A. K. Control Technique for Transformerless Regenerative Testing of Grid-Connected Power Converters. 2022 IEEE Applied Power Electronics Conference and Exposition (APEC) (2022) doi:10.1109/apec43599.2022.9773450 -- [10.1109/apec43599.2022.9773450](https://doi.org/10.1109/apec43599.2022.9773450)
- Tricarico, T. et al. Control Design, Stability Analysis and Experimental Validation of New Application of an Interleaved Converter Operating as a Power Interface in Hybrid Microgrids. Energies 12, 437 (2019) -- [10.3390/en12030437](https://doi.org/10.3390/en12030437)
- Reich, D. & Oriti, G. Rightsizing the Design of a Hybrid Microgrid. Energies 14, 4273 (2021) -- [10.3390/en14144273](https://doi.org/10.3390/en14144273)
- Aouichak, I. et al. A Bidirectional Grid-Connected DC–AC Converter for Autonomous and Intelligent Electricity Storage in the Residential Sector. Energies 15, 1194 (2022) -- [10.3390/en15031194](https://doi.org/10.3390/en15031194)
- Wu, C., Liu, Y., Zhou, T. & Cao, S. A Multistage Current Charging Method for Energy Storage Device of Microgrid Considering Energy Consumption and Capacity of Lithium Battery. Energies 15, 4526 (2022) -- [10.3390/en15134526](https://doi.org/10.3390/en15134526)
- Bui, V.-H., Nguyen, X. Q., Hussain, A. & Su, W. Optimal Sizing of Energy Storage System for Operation of Wind Farms Considering Grid-Code Constraints. Energies 14, 5478 (2021) -- [10.3390/en14175478](https://doi.org/10.3390/en14175478)
- Sayed, K. et al. A Review of DC-AC Converters for Electric Vehicle Applications. Energies 15, 1241 (2022) -- [10.3390/en15031241](https://doi.org/10.3390/en15031241)
- Huu, D. N. A Novel Adaptive Control Approach Based on Available Headroom of the VSC-HVDC for Enhancement of the AC Voltage Stability. Energies 14, 3222 (2021) -- [10.3390/en14113222](https://doi.org/10.3390/en14113222)
- Rasool, M. A. U., Khan, M. M., Ahmed, Z. & Saeed, M. A. Analysis of an H∞ Robust Control for a Three-Phase Voltage Source Inverter. Inventions 4, 18 (2019) -- [10.3390/inventions4010018](https://doi.org/10.3390/inventions4010018)
- Mahmud, M. R. & Pota, H. R. Robust Nonlinear Controller Design for DC–AC Converter in Grid-Connected Fuel Cell System. IEEE J. Emerg. Sel. Top. Ind. Electron. 3, 342–351 (2022) -- [10.1109/jestie.2021.3088394](https://doi.org/10.1109/jestie.2021.3088394)
- Dyga, Ł., Alhasheem, M., Davari, P. & Rymarski, Z. Robustness of Model-Predictive and Passivity-Based Control in the Three-Phase DC/AC Converter Application. Applied Sciences 12, 4329 (2022) -- [10.3390/app12094329](https://doi.org/10.3390/app12094329)
- Hornik, T. & Zhong, Q.-C. A Current-Control Strategy for Voltage-Source Inverters in Microgrids Based on $H^{\infty }$ and Repetitive Control. IEEE Trans. Power Electron. 26, 943–952 (2011) -- [10.1109/tpel.2010.2089471](https://doi.org/10.1109/tpel.2010.2089471)
- Nicola, M. & Nicola, C.-I. Improved Performance for the DC-AC Converters Control System Based on Robust Controller and Reinforcement Learning Agent. 2022 International Conference on Electrical, Computer, Communications and Mechatronics Engineering (ICECCME) (2022) doi:10.1109/iceccme55909.2022.9988458 -- [10.1109/iceccme55909.2022.9988458](https://doi.org/10.1109/iceccme55909.2022.9988458)
- Kamal, T., Karabacak, M., Perić, V. S., Hassan, S. Z. & Fernández-Ramírez, L. M. Novel Improved Adaptive Neuro-Fuzzy Control of Inverter and Supervisory Energy Management System of a Microgrid. Energies 13, 4721 (2020) -- [10.3390/en13184721](https://doi.org/10.3390/en13184721)
- [Gil-González, W., Montoya, O. D., Restrepo, C. & Hernández, J. C. Sensorless Adaptive Voltage Control for Classical DC-DC Converters Feeding Unknown Loads: A Generalized PI Passivity-Based Approach. Sensors 21, 6367 (2021)](sensorless-adaptive-voltage-control-for-classical-dc-dc-converters-feeding-unknown-loads-a-generalized-pi-passivity-based-approach) -- [10.3390/s21196367](https://doi.org/10.3390/s21196367)
- Magaldi, G. L., Serra, F. M., de Angelo, C. H., Montoya, O. D. & Giral-Ramírez, D. A. Voltage Regulation of an Isolated DC Microgrid with a Constant Power Load: A Passivity-based Control Design. Electronics 10, 2085 (2021) -- [10.3390/electronics10172085](https://doi.org/10.3390/electronics10172085)
- [Zhao, Y., Yu, H. & Wang, S. Development of Optimized Cooperative Control Based on Feedback Linearization and Error Port-Controlled Hamiltonian for Permanent Magnet Synchronous Motor. IEEE Access 9, 141036–141047 (2021)](development-of-optimized-cooperative-control-based-on-feedback-linearization-and-error-port-controlled-hamiltonian-for-permanent-magnet-synchronous-motor) -- [10.1109/access.2021.3119625](https://doi.org/10.1109/access.2021.3119625)
- Serra, F. M., Fernández, L. M., Montoya, O. D., Gil-González, W. & Hernández, J. C. Nonlinear Voltage Control for Three-Phase DC-AC Converters in Hybrid Systems: An Application of the PI-PBC Method. Electronics 9, 847 (2020) -- [10.3390/electronics9050847](https://doi.org/10.3390/electronics9050847)
- [Nicola, M. & Nicola, C.-I. Improved Performance for the DC-AC Converters Control System Based on PCH Controller and Reinforcement Learning Agent. 2022 4th Global Power, Energy and Communication Conference (GPECOM) (2022) doi:10.1109/gpecom55404.2022.9815661](improved-performance-for-the-dc-ac-converters-control-system-based-on-pch-controller-and-reinforcement-learning-agent) -- [10.1109/gpecom55404.2022.9815661](https://doi.org/10.1109/gpecom55404.2022.9815661)
- Brandimarte, P. From Shortest Paths to Reinforcement Learning. EURO Advanced Tutorials on Operational Research (Springer International Publishing, 2021). doi:10.1007/978-3-030-61867-4 -- [10.1007/978-3-030-61867-4](https://doi.org/10.1007/978-3-030-61867-4)
- Nicola, M., Nicola, C.-I. & Selișteanu, D. Improvement of the Control of a Grid Connected Photovoltaic System Based on Synergetic and Sliding Mode Controllers Using a Reinforcement Learning Deep Deterministic Policy Gradient Agent. Energies 15, 2392 (2022) -- [10.3390/en15072392](https://doi.org/10.3390/en15072392)

