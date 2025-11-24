---
title: "Evaluation of a Port-Hamiltonian Controller for an altazimutal Liquid Mirror Telescope Using ROS and Gazebo"
date: 2025-11-18 00:00:00 +0100
permalink: evaluation-of-a-port-hamiltonian-controller-for-an-altazimutal-liquid-mirror-telescope-using-ros-and-gazebo
year: 2025
authors: Juan Cristobal Alcaraz Tapia, Carlos E. Castañeda, Héctor Vargas-Rodríguez
category: articles
---
 
## Authors
[Juan Cristobal Alcaraz Tapia](authors/juan-cristobal-alcaraz-tapia), [Carlos E. Castañeda](authors/carlos-e-castaneda), [Héctor Vargas-Rodríguez](authors/hector-vargas-rodriguez)
 
## Abstract
This study evaluates the performance and robustness of a port-Hamiltonian controller for the links of a liquid mirror telescope and a PI controller for the rotation of its liquid mirror, using ROS2 and Gazebo. The telescope links track a star’s apparent daily motion, while the liquid mirror achieves the required angular speed for a desired focal length. These references are computed based on the star’s name and focal length input. The telescope’s physical properties, including dimensions, masses, inertia, and 3D models, are stored in a Unified Robot Description Format (URDF) file, enabling Gazebo to initialize accurate simulations. Joint information—state interfaces (angular position and speed) and command interfaces (effort)—is also defined in the URDF. Controller configurations, including gains, bounds, and control parameters, are stored in a YAML file, ensuring seamless integration with Gazebo. The evaluation encompasses key performance metrics. For the two-link telescope, tracking accuracy, settling time, control effort, and energy efficiency are analyzed. For the liquid mirror, the primary focus is on tracking precision. The port-Hamiltonian controller’s performance is compared to inverse dynamics and super-twisting sliding mode controllers. Results show that the port-Hamiltonian controller achieves a favorable balance between accuracy and energy efficiency, exhibiting smoother control actions that reduce energy consumption and actuator wear. Its stability under varying conditions ensures high precision for astronomical observations. Furthermore, ROS2 and Gazebo provide a risk-free environment for extensive testing, facilitating a smooth transition to real-world implementation.
 
## Citation
- **Journal:** WSEAS TRANSACTIONS ON SYSTEMS AND CONTROL
- **Year:** 2025
- **Volume:** 20
- **Issue:** 
- **Pages:** 471--486
- **Publisher:** World Scientific and Engineering Academy and Society (WSEAS)
- **DOI:** [10.37394/23203.2025.20.47](https://doi.org/10.37394/23203.2025.20.47)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Tapia_2025,
  title={{Evaluation of a Port-Hamiltonian Controller for an altazimutal Liquid Mirror Telescope Using ROS and Gazebo}},
  volume={20},
  ISSN={1991-8763},
  DOI={10.37394/23203.2025.20.47},
  journal={WSEAS TRANSACTIONS ON SYSTEMS AND CONTROL},
  publisher={World Scientific and Engineering Academy and Society (WSEAS)},
  author={Tapia, Juan Cristobal Alcaraz and Castañeda, Carlos E. and Vargas-Rodríguez, Héctor},
  year={2025},
  pages={471--486}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/evaluation-of-a-port-hamiltonian-controller-for-an-altazimutal-liquid-mirror-telescope-using-ros-and-gazebo.bib)
 
## References
- Borra EF (1987) Liquid mirror telescopes - Present and future. PASP 99:1229. https://doi.org/10.1086/13210 -- [10.1086/132108](https://doi.org/10.1086/132108)
- Hickson P, Borra EF, Cabanac R, Content R, Gibson BK, Walker GAH (1994) UBC/Laval 2.7 meter liquid mirror telescope. ApJ 436:L201. https://doi.org/10.1086/18766 -- [10.1086/187667](https://doi.org/10.1086/187667)
- Hickson P, Pfrommer T, Cabanac R, Crotts A, Johnson B, de Lapparent V, Lanzetta KM, Gromoll S, Mulrooney MK, Sivanandam S, Truax B (2007) The Large Zenith Telescope: A 6 m Liquid‐Mirror Telescope. PUBL ASTRON SOC PAC 119(854):444–455. https://doi.org/10.1086/51762 -- [10.1086/517621](https://doi.org/10.1086/517621)
- Kumar B, Pandey KL, Pandey SB, Hickson P, Borra EF, Anupama GC, Surdej J (2018) The zenithal 4-m International Liquid Mirror Telescope: a unique facility for supernova studies. Monthly Notices of the Royal Astronomical Society 476(2):2075–2085. https://doi.org/10.1093/mnras/sty29 -- [10.1093/mnras/sty298](https://doi.org/10.1093/mnras/sty298)
- Borra EF, Ritcey A, Artigau E (1999) Floating Mirrors. The Astrophysical Journal 516(2):L115–L118. https://doi.org/10.1086/31199 -- [10.1086/311999](https://doi.org/10.1086/311999)
- Gagné G, Borra EF, Ritcey AM (2007) Tiltable rotating liquid mirrors: a progress report. A&amp;A 479(2):597–602. https://doi.org/10.1051/0004-6361:2007871 -- [10.1051/0004-6361:20078714](https://doi.org/10.1051/0004-6361:20078714)
- Nayak M, Basu S, Iyer K (2024) Zenith: a DARPA liquid mirror technology development program. Photonic Instrumentation Engineering XI -- [10.1117/12.2693008](https://doi.org/10.1117/12.2693008)
- [Alcaraz Tapia JC, Castañeda CE, Vargas Rodriguez H, Esquivel P (2023) Design of a Port-Hamiltonian Control for an Alt-Azimuth Liquid–Mirror Telescope. Mathematics 11(16):3443. https://doi.org/10.3390/math1116344](design-of-a-port-hamiltonian-control-for-an-alt-azimuth-liquid-mirror-telescope) -- [10.3390/math11163443](https://doi.org/10.3390/math11163443)
- [Duindam V, Macchelli A, Stramigioli S, Bruyninckx H (2009) Port-Hamiltonian Systems. Modeling and Control of Complex Physical Systems 53–13](port-hamiltonian-systems0) -- [10.1007/978-3-642-03196-0_2](https://doi.org/10.1007/978-3-642-03196-0_2)
- [van der Schaft A (2007) Port-Hamiltonian systems: an introductory survey. Proceedings of the International Congress of Mathematicians Madrid, August 22–30, 2006 1339–136](port-hamiltonian-systems-an-introductory-survey) -- [10.4171/022-3/65](https://doi.org/10.4171/022-3/65)
- [Yaghmaei A, Yazdanpanah MJ (2017) Trajectory tracking for a class of contractive port Hamiltonian systems. Automatica 83:331–336. https://doi.org/10.1016/j.automatica.2017.06.03](trajectory-tracking-for-a-class-of-contractive-port-hamiltonian-systems) -- [10.1016/j.automatica.2017.06.039](https://doi.org/10.1016/j.automatica.2017.06.039)
- [Chi J, Yu H, Yu J (2018) Hybrid Tracking Control of 2-DOF SCARA Robot via Port-Controlled Hamiltonian and Backstepping. IEEE Access 6:17354–17360. https://doi.org/10.1109/access.2018.282068](hybrid-tracking-control-of-2-dof-scara-robot-via-port-controlled-hamiltonian-and-backstepping) -- [10.1109/access.2018.2820681](https://doi.org/10.1109/access.2018.2820681)
- [Zhao B, Yu H, Yu J, Liu X, Wu H (2018) Port-Controlled Hamiltonian and Sliding Mode Control of Gantry Robot Based on Induction Motor Drives. IEEE Access 6:43840–43849. https://doi.org/10.1109/access.2018.286263](port-controlled-hamiltonian-and-sliding-mode-control-of-gantry-robot-based-on-induction-motor-drives) -- [10.1109/access.2018.2862637](https://doi.org/10.1109/access.2018.2862637)
- Koenig N, Howard A Design and use paradigms for gazebo, an open-source multi-robot simulator. 2004 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (IEEE Cat. No.04CH37566) 3:2149–215 -- [10.1109/iros.2004.1389727](https://doi.org/10.1109/iros.2004.1389727)
- Friz JS, Cooper JR, Miksch C, Kalluri S (2023) Assessment of Sensor Data Accuracy within Gazebo/ROS for High-Precision Autonomous In-Space Robotic Operations. ASCEND 202 -- [10.2514/6.2023-4726](https://doi.org/10.2514/6.2023-4726)
- Sánchez-Montero M (2022) Automatically Annotated Dataset of a Ground Mobile Robot in Natural Environments via Gazebo Simulations. Dataset -- [10.24310/riuma.26015](https://doi.org/10.24310/riuma.26015)
- Aksu M, Michaloski JL, Proctor FM (2018) Virtual Experimental Investigation for Industrial Robotics in Gazebo Environment. Volume 2: Advanced Manufacturin -- [10.1115/imece2018-87686](https://doi.org/10.1115/imece2018-87686)
- van Leeuwen F (2009) The Hipparcos catalog. A&amp;A 500(1):505–506. https://doi.org/10.1051/0004-6361/20091220 -- [10.1051/0004-6361/200912202](https://doi.org/10.1051/0004-6361/200912202)
- Chang DE (2014) On the method of interconnection and damping assignment passivity-based control for the stabilization of mechanical systems. Regul Chaot Dyn 19(5):556–575. https://doi.org/10.1134/s156035471405004 -- [10.1134/s1560354714050049](https://doi.org/10.1134/s1560354714050049)
- Montoya-Morales J-R, Guerrero-Sánchez M-E, Valencia-Palomo G, Hernández-González O, López-Estrada F-R, Félix-Herrán LC (2025) Design and experimental validation of IDA-PBC-based flight control for quadrotors. Robotica 43(7):2376–2397. https://doi.org/10.1017/s026357472510171 -- [10.1017/s0263574725101719](https://doi.org/10.1017/s0263574725101719)
- Guerrero-Sánchez ME, Hernández-González O, Valencia-Palomo G, Mercado-Ravell DA, López-Estrada FR, Hoyo-Montaño JA (2021) Robust IDA-PBC for under-actuated systems with inertia matrix dependent of the unactuated coordinates: application to a UAV carrying a load. Nonlinear Dyn 105(4):3225–3238. https://doi.org/10.1007/s11071-021-06776- -- [10.1007/s11071-021-06776-7](https://doi.org/10.1007/s11071-021-06776-7)
- Yüksel B, Secchi C, Bülthoff HH, Franchi A (2019) Aerial physical interaction via IDA-PBC. The International Journal of Robotics Research 38(4):403–421. https://doi.org/10.1177/027836491983560 -- [10.1177/0278364919835605](https://doi.org/10.1177/0278364919835605)

