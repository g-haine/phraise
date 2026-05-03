---
title: "Analysis of thruster degradation effects on the posture control of a remotely operated vehicle"
date: 2026-01-29 00:00:00 +0100
permalink: analysis-of-thruster-degradation-effects-on-the-posture-control-of-a-remotely-operated-vehicle
year: 2026
authors: Paulina Gutiérrez-León, J Alejandro Vázquez-Santacruz, Hugo Rodríguez-Cortés, Rogelio de J Portillo-Vélez
category: articles
---
 
## Authors
[Paulina Gutiérrez-León](authors/paulina-gutierrez-leon), [J Alejandro Vázquez-Santacruz](authors/j-alejandro-vazquez-santacruz), [Hugo Rodríguez-Cortés](authors/hugo-rodriguez-cortes), [Rogelio de J Portillo-Vélez](authors/rogelio-de-j-portillo-velez)
 
## Abstract
                  This paper presents an analysis of mobility on an over-actuated Remotely Operated Vehicle (ROV) that becomes under-actuated due to multiple actuator faults of different types of degradation. The analysis is developed on a regulation control problem, including modeling and robust control design. The dynamic model is formulated using a Port-Hamiltonian formalism, emphasizing energy conservation and passivity. The control strategy is developed through a Control by Interconnection (CbI) structure to regulate the ROV posture as an interconnected energy-based system. Singular Value Decomposition (SVD) is employed to assess mobility effectiveness in each spatial direction. Quadratic Programming (QP) is used for realistic control allocation under actuator constraints and fault conditions, highlighting the direction with reduced effectiveness for improving performance in a complete posture regulation task. The simulation results validate control allocation based on QP, demonstrating its robustness in maintaining ROV stability and achieving posture regulation under various fault scenarios. It has been shown that the ROV topology under study supports two individual thruster faults and still achieves a 3D target, and the resulting reduced directions can be enhanced by QP allocation; for instance, yaw error is improved by nearly 50% compared with the SVD method, demonstrating its ability to redistribute control forces efficiently while preserving closed-loop stability. Furthermore, computational performance analysis confirms the approach’s real-time feasibility for experimental implementation, with the QP solver operating at about 1 ms per iteration.
 
## Citation
- **Journal:** Engineering Research Express
- **Year:** 2026
- **Volume:** 8
- **Issue:** 3
- **Pages:** 035229
- **Publisher:** IOP Publishing
- **DOI:** [10.1088/2631-8695/ae3f7f](https://doi.org/10.1088/2631-8695/ae3f7f)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Guti_rrez_Le_n_2026,
  title={{Analysis of thruster degradation effects on the posture control of a remotely operated vehicle}},
  volume={8},
  ISSN={2631-8695},
  DOI={10.1088/2631-8695/ae3f7f},
  number={3},
  journal={Engineering Research Express},
  publisher={IOP Publishing},
  author={Gutiérrez-León, Paulina and Vázquez-Santacruz, J Alejandro and Rodríguez-Cortés, Hugo and de J Portillo-Vélez, Rogelio},
  year={2026},
  pages={035229}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/analysis-of-thruster-degradation-effects-on-the-posture-control-of-a-remotely-operated-vehicle.bib)
 
## References
- Fossen TI (2011) Handbook of Marine Craft Hydrodynamics and Motion Contro -- [10.1002/9781119994138](https://doi.org/10.1002/9781119994138)
- (2006) Diagnosis and Fault-Tolerant Control. Springer Berlin Heidelber -- [10.1007/978-3-540-35653-0](https://doi.org/10.1007/978-3-540-35653-0)
- Johansen TA, Fossen TI (2013) Control allocation—A survey. Automatica 49(5):1087–1103. https://doi.org/10.1016/j.automatica.2013.01.03 -- [10.1016/j.automatica.2013.01.035](https://doi.org/10.1016/j.automatica.2013.01.035)
- Garus, Optimization of thrust allocation in propulsion system of underwater vehicle. Int. J. Appl. Math. Comput. Sci. (2004)
- Baldini A, Fasano A, Felicetti R, Freddi A, Longhi S, Monteriù A (2018) A Model-based Active Fault Tolerant Control Scheme for a Remotely Operated Vehicle. IFAC-PapersOnLine 51(24):798–805. https://doi.org/10.1016/j.ifacol.2018.09.66 -- [10.1016/j.ifacol.2018.09.666](https://doi.org/10.1016/j.ifacol.2018.09.666)
- Baldini A, Felicetti R, Freddi A, Longhi S, Monteriù A (2022) Actuator fault tolerant control via active fault diagnosis for a remotely operated vehicle. IFAC-PapersOnLine 55(6):310–316. https://doi.org/10.1016/j.ifacol.2022.07.14 -- [10.1016/j.ifacol.2022.07.147](https://doi.org/10.1016/j.ifacol.2022.07.147)
- Jiang J, Li BH, Ding ML (2023) An Adaptive Fault-Tolerant Control Algorithm for Underwater Vehicle Propulsion System. J Phys: Conf Ser 2419(1):012103. https://doi.org/10.1088/1742-6596/2419/1/01210 -- [10.1088/1742-6596/2419/1/012103](https://doi.org/10.1088/1742-6596/2419/1/012103)
- Hosseinnajad A, Loueipour M (2021) Design of a Robust Observer-based DP Control System for an ROV with Unknown Dynamics Including Thruster Allocation. 2021 7th International Conference on Control, Instrumentation and Automation (ICCIA) 1– -- [10.1109/iccia52082.2021.9403543](https://doi.org/10.1109/iccia52082.2021.9403543)
- Dong J, Duan X (2023) A Robust Control via a Fuzzy System with PID for the ROV. Sensors 23(2):821. https://doi.org/10.3390/s2302082 -- [10.3390/s23020821](https://doi.org/10.3390/s23020821)
- Li H, Lin X (2024) Robust fault-tolerant control for dynamic positioning of ships with prescribed performance. Ocean Engineering 298:117314. https://doi.org/10.1016/j.oceaneng.2024.11731 -- [10.1016/j.oceaneng.2024.117314](https://doi.org/10.1016/j.oceaneng.2024.117314)
- Liu F, Ma Z, Mu B, Duan C, Chen R, Qin Y, Pu H, Luo J (2023) Review on fault-tolerant control of unmanned underwater vehicles. Ocean Engineering 285:115471. https://doi.org/10.1016/j.oceaneng.2023.11547 -- [10.1016/j.oceaneng.2023.115471](https://doi.org/10.1016/j.oceaneng.2023.115471)
- Mai VT, Jani F, Alattas KA, Ghaderpour E, Mohammadzadeh A (2025) A Robust Finite-Time Fault-Tolerant Tracking Control for Quadrotor Attitude System With Stochastic Actuator Faults and Input Delays. IEEE Access 13:64627–64637. https://doi.org/10.1109/access.2025.355918 -- [10.1109/access.2025.3559180](https://doi.org/10.1109/access.2025.3559180)
- Feng H, Tao Y, Feng J, Zhang Y, Xue H, Wang T, Xu X, Chen P (2025) Fault-Tolerant Collaborative Control of Four-Wheel-Drive Electric Vehicle for One or More In-Wheel Motors’ Faults. Sensors 25(5):1540. https://doi.org/10.3390/s2505154 -- [10.3390/s25051540](https://doi.org/10.3390/s25051540)
- Wang X, Zhou Y, Liu M (2025) Active fault tolerant control based on adaptive iterative learning observer against time-varying faults in thrusters of autonomous underwater vehicle. Ocean Engineering 331:121266. https://doi.org/10.1016/j.oceaneng.2025.12126 -- [10.1016/j.oceaneng.2025.121266](https://doi.org/10.1016/j.oceaneng.2025.121266)
- Song S, Jiang Y, Song X, Stojanovic V (2025) Composite neural learning-based adaptive actuator failure compensation control for full-state constrained autonomous surface vehicle. Neural Comput &amp; Applic 37(8):6369–6381. https://doi.org/10.1007/s00521-024-10651- -- [10.1007/s00521-024-10651-y](https://doi.org/10.1007/s00521-024-10651-y)
- {"status":"error" -- [10.1109/tfuzz.2023.3334567](https://doi.org/10.1109/tfuzz.2023.3334567)
- Keymasi-Khalaji A, Haghjoo M (2024) Passivity-based stabilizing controller for an underwater robot. Ocean Engineering 302:117656. https://doi.org/10.1016/j.oceaneng.2024.11765 -- [10.1016/j.oceaneng.2024.117656](https://doi.org/10.1016/j.oceaneng.2024.117656)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Borja P, Ortega R (2026) Introduction to Passivity-Based Control. Encyclopedia of Systems and Control Engineering 161–17 -- [10.1016/b978-0-443-14081-5.00031-3](https://doi.org/10.1016/b978-0-443-14081-5.00031-3)
- [Ma L, Pang S, He Y, Wu Y, Li Y, Zhou W (2025) Passivity-Based Sliding Mode Control for the Robust Trajectory Tracking of Unmanned Surface Vessels Under External Disturbances and Model Uncertainty. JMSE 13(2):364. https://doi.org/10.3390/jmse1302036](passivity-based-sliding-mode-control-for-the-robust-trajectory-tracking-of-unmanned-surface-vessels-under-external-disturbances-and-model-uncertainty) -- [10.3390/jmse13020364](https://doi.org/10.3390/jmse13020364)
- [Ortega R, van der Schaft A, Castanos F, Astolfi A (2008) Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans Automat Contr 53(11):2527–2542. https://doi.org/10.1109/tac.2008.200693](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- [Donaire A, Romero JG, Perez T (2017) Trajectory tracking passivity-based control for marine vehicles subject to disturbances. Journal of the Franklin Institute 354(5):2167–2182. https://doi.org/10.1016/j.jfranklin.2017.01.01](trajectory-tracking-passivity-based-control-for-marine-vehicles-subject-to-disturbances) -- [10.1016/j.jfranklin.2017.01.012](https://doi.org/10.1016/j.jfranklin.2017.01.012)
- [Perez T, Donaire A, Renton C, Valentinis F (2013) Energy-based Motion Control of Marine Vehicles using Interconnection and Damping Assignment Passivity-based Control – A Survey. IFAC Proceedings Volumes 46(33):316–327. https://doi.org/10.3182/20130918-4-jp-3022.0007](energy-based-motion-control-of-marine-vehicles-using-interconnection-and-damping-assignment-passivity-based-control-a-survey) -- [10.3182/20130918-4-jp-3022.00072](https://doi.org/10.3182/20130918-4-jp-3022.00072)
- [Pham TH, Vu NMT, Prodan I, Lefèvre L (2022) A combined Control by Interconnection—Model Predictive Control design for constrained Port-Hamiltonian systems. Systems &amp; Control Letters 167:105336. https://doi.org/10.1016/j.sysconle.2022.10533](a-combined-control-by-interconnection-model-predictive-control-design-for-constrained-port-hamiltonian-systems) -- [10.1016/j.sysconle.2022.105336](https://doi.org/10.1016/j.sysconle.2022.105336)
- [Ferguson J, Zhou L, Ahmed S, Scherpen JMA (2024) On the Control-by-Interconnection interpretation of integral control for port-Hamiltonian systems. IFAC-PapersOnLine 58(6):1–6. https://doi.org/10.1016/j.ifacol.2024.08.24](on-the-control-by-interconnection-interpretation-of-integral-control-for-port-hamiltonian-systems) -- [10.1016/j.ifacol.2024.08.247](https://doi.org/10.1016/j.ifacol.2024.08.247)
- Hosseinnajad A, Loueipour M (2023) Fault tolerant control system for an ROV based on a novel integral sliding mode control and a state and fault observer in the presence of thruster limitations. Ocean Engineering 280:114687. https://doi.org/10.1016/j.oceaneng.2023.11468 -- [10.1016/j.oceaneng.2023.114687](https://doi.org/10.1016/j.oceaneng.2023.114687)
- Akmal M, Yusoff M, Arshad MR (2012) Active Fault Tolerant Control of a Remotely Operated Vehicle Propulsion System. Procedia Engineering 41:622–628. https://doi.org/10.1016/j.proeng.2012.07.22 -- [10.1016/j.proeng.2012.07.221](https://doi.org/10.1016/j.proeng.2012.07.221)
- Capocci R, Omerdic E, Dooly G, Toal D (2018) Fault-Tolerant Control for ROVs Using Control Reallocation and Power Isolation. JMSE 6(2):40. https://doi.org/10.3390/jmse602004 -- [10.3390/jmse6020040](https://doi.org/10.3390/jmse6020040)
- Ramírez Hernández K, Gutiérrez León P, Vázquez Santacruz JA, Portillo Vélez R de J (2025) Analysis of ROV mobility under optimal thruster mechanism configuration. J Mech Sci Technol 39(1):47–56. https://doi.org/10.1007/s12206-024-1205- -- [10.1007/s12206-024-1205-7](https://doi.org/10.1007/s12206-024-1205-7)
- Fossen, (1994)
- Gutiérrez-León P, Vasquez-Santacruz JA, Velez RP- (2024) Dynamic model based control for trajectory following for an inspection-class ROV. 2024 IEEE International Conference on Engineering Veracruz (ICEV) 1– -- [10.1109/icev63254.2024.10766000](https://doi.org/10.1109/icev63254.2024.10766000)
- Cortes, (2002)
- {"status":"error" -- [10.1007/3-540-30773-2](https://doi.org/10.1007/3-540-30773-2)
- Delgado-Reyes G, Valdez-Martínez JS, Hernández-Pérez MÁ, Pérez-Daniel KR, García-Ramírez PJ (2022) Quadrotor Real-Time Simulation: A Temporary Computational Complexity-Based Approach. Mathematics 10(12):2032. https://doi.org/10.3390/math1012203 -- [10.3390/math10122032](https://doi.org/10.3390/math10122032)
- Baldini A, Felicetti R, Freddi A, Longhi S, Monteriu A, Fasano A (2018) Fault Detection, Diagnosis and Fault Tolerant Output Control for a Remotely Operated Vehicle. 2018 14th IEEE/ASME International Conference on Mechatronic and Embedded Systems and Applications (MESA) 1– -- [10.1109/mesa.2018.8449159](https://doi.org/10.1109/mesa.2018.8449159)

