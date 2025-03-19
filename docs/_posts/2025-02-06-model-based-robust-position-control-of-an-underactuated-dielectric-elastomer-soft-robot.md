---
layout: post
title: "Model-Based Robust Position Control of an Underactuated Dielectric Elastomer Soft Robot"
date: 2025-02-06 00:00:00 +0100
permalink: model-based-robust-position-control-of-an-underactuated-dielectric-elastomer-soft-robot
year: 2025
authors: Giovanni Soleti, Paolo Roberto Massenio, Julian Kunze, Gianluca Rizzello
category: articles
---
 
## Authors
[Giovanni Soleti](authors/giovanni-soleti), [Paolo Roberto Massenio](authors/paolo-roberto-massenio), [Julian Kunze](authors/julian-kunze), [Gianluca Rizzello](authors/gianluca-rizzello)
 
## Abstract
Achieving accurate closed-loop position control of soft robots remains an ongoing research problem, due to the challenges posed by underactuation, elastic nonlinearities, and material creep. Although soft driving technologies relying on tendons and smart material transducers (e.g., dielectric elastomers, shape memory alloys) offer more ease of controllability compared to pneumatics, the corresponding controller design problem becomes even more challenging because of additional nonlinear effects. Those include a configuration-dependent actuation matrix, that stems from the kinematics of the actuation, and control input saturation, which is especially critical for smart material actuators. In this article, we investigate for the first time the closed-loop position control of a soft-robotic system driven by dielectric elastomer actuators. The objective is to regulate the robot state to a constant setpoint, accounting for the effects of open-loop instability, underactuation, control input saturation, and constant external disturbances. To achieve this goal, we propose a model-based feedback scheme, which combines a stabilizing energy-shaping controller with a robustifying PI-like law. After presenting the general theory, a linear matrix inequalities algorithm is proposed to practically address the controller design in spite of strong model nonlinearities. Experimental validation conducted on a prototype of the soft-robotic system confirms the effectiveness of the proposed control approach.
 
## Citation
- **Journal:** IEEE Transactions on Robotics
- **Year:** 2025
- **Volume:** 41
- **Issue:** 
- **Pages:** 1693--1710
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tro.2025.3539184](https://doi.org/10.1109/tro.2025.3539184)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Soleti_2025,
  title={{Model-Based Robust Position Control of an Underactuated Dielectric Elastomer Soft Robot}},
  volume={41},
  ISSN={1941-0468},
  DOI={10.1109/tro.2025.3539184},
  journal={IEEE Transactions on Robotics},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Soleti, Giovanni and Massenio, Paolo Roberto and Kunze, Julian and Rizzello, Gianluca},
  year={2025},
  pages={1693--1710}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/model-based-robust-position-control-of-an-underactuated-dielectric-elastomer-soft-robot.bib)
 
## References
- Laschi, C. & Cianchetti, M. Soft Robotics: New Perspectives for Robot Bodyware and Control. Frontiers in Bioengineering and Biotechnology vol. 2 (2014) -- [10.3389/fbioe.2014.00003](https://doi.org/10.3389/fbioe.2014.00003)
- Whitesides, G. M. Soft Robotics. Angewandte Chemie International Edition vol. 57 4258–4273 (2018) -- [10.1002/anie.201800907](https://doi.org/10.1002/anie.201800907)
- Kim, D. et al. Review of machine learning methods in soft robotics. PLOS ONE vol. 16 e0246102 (2021) -- [10.1371/journal.pone.0246102](https://doi.org/10.1371/journal.pone.0246102)
- Chin, K., Hellebrekers, T. & Majidi, C. Machine Learning for Soft Robotic Sensing and Control. Advanced Intelligent Systems vol. 2 (2020) -- [10.1002/aisy.201900171](https://doi.org/10.1002/aisy.201900171)
- Della Santina, C., Duriez, C. & Rus, D. Model-Based Control of Soft Robots: A Survey of the State of the Art and Open Challenges. IEEE Control Systems vol. 43 30–65 (2023) -- [10.1109/mcs.2023.3253419](https://doi.org/10.1109/mcs.2023.3253419)
- Della Santina, C., Katzschmann, R. K., Biechi, A. & Rus, D. Dynamic control of soft robots interacting with the environment. 2018 IEEE International Conference on Soft Robotics (RoboSoft) 46–53 (2018) doi:10.1109/robosoft.2018.8404895 -- [10.1109/robosoft.2018.8404895](https://doi.org/10.1109/robosoft.2018.8404895)
- Khan, A. H., Shao, Z., Li, S., Wang, Q. & Guan, N. Which is the best PID variant for pneumatic soft robots an experimental study. IEEE/CAA Journal of Automatica Sinica vol. 7 451–460 (2020) -- [10.1109/jas.2020.1003045](https://doi.org/10.1109/jas.2020.1003045)
- Thuruthel, T. G., Falotico, E., Manti, M. & Laschi, C. Stable Open Loop Control of Soft Robotic Manipulators. IEEE Robotics and Automation Letters vol. 3 1292–1298 (2018) -- [10.1109/lra.2018.2797241](https://doi.org/10.1109/lra.2018.2797241)
- Shao, X. et al. Model-Based Control for Soft Robots With System Uncertainties and Input Saturation. IEEE Transactions on Industrial Electronics vol. 71 7435–7444 (2024) -- [10.1109/tie.2023.3303636](https://doi.org/10.1109/tie.2023.3303636)
- Pustina, P., Borja, P., Santina, C. D. & De Luca, A. P-satI-D Shape Regulation of Soft Robots. IEEE Robotics and Automation Letters vol. 8 1–8 (2023) -- [10.1109/lra.2022.3221304](https://doi.org/10.1109/lra.2022.3221304)
- Ortega, R., Romero, J. G., Borja, P. & Donaire, A. PID Passivity‐Based Control of Nonlinear Systems with Applications. (2021) doi:10.1002/9781119694199 -- [10.1002/9781119694199](https://doi.org/10.1002/9781119694199)
- [Franco, E., Garriga Casanovas, A. & Donaire, A. Energy shaping control with integral action for soft continuum manipulators. Mechanism and Machine Theory vol. 158 104250 (2021)](energy-shaping-control-with-integral-action-for-soft-continuum-manipulators) -- [10.1016/j.mechmachtheory.2021.104250](https://doi.org/10.1016/j.mechmachtheory.2021.104250)
- Arpenti, P., Franco, E. & Donaire, A. Integral passivity-based control of an underactuated hydraulic soft manipulator with uncertain nonlinear stiffness. IFAC-PapersOnLine vol. 58 13–18 (2024) -- [10.1016/j.ifacol.2024.08.249](https://doi.org/10.1016/j.ifacol.2024.08.249)
- Franco, E., Casanovas, A. G., Rodriguez y Baena, F. & Astolfi, A. Model based adaptive control for a soft robotic manipulator. 2019 IEEE 58th Conference on Decision and Control (CDC) 1019–1024 (2019) doi:10.1109/cdc40024.2019.9029449 -- [10.1109/cdc40024.2019.9029449](https://doi.org/10.1109/cdc40024.2019.9029449)
- Deutschmann, B., Dietrich, A. & Ott, C. Position control of an underactuated continuum mechanism using a reduced nonlinear model. 2017 IEEE 56th Annual Conference on Decision and Control (CDC) 5223–5230 (2017) doi:10.1109/cdc.2017.8264433 -- [10.1109/cdc.2017.8264433](https://doi.org/10.1109/cdc.2017.8264433)
- Spong, M. W. Partial feedback linearization of underactuated mechanical systems. Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS’94) vol. 1 314–321 -- [10.1109/iros.1994.407375](https://doi.org/10.1109/iros.1994.407375)
- Ortega, R., Loría, A., Nicklasson, P. J. & Sira-Ramírez, H. Passivity-Based Control of Euler-Lagrange Systems. Communications and Control Engineering (Springer London, 1998). doi:10.1007/978-1-4471-3603-3 -- [10.1007/978-1-4471-3603-3](https://doi.org/10.1007/978-1-4471-3603-3)
- Pustina, P., Santina, C. D., Boyer, F., De Luca, A. & Renda, F. Input Decoupling of Lagrangian Systems via Coordinate Transformation: General Characterization and Its Application to Soft Robotics. IEEE Transactions on Robotics vol. 40 2098–2110 (2024) -- [10.1109/tro.2024.3370089](https://doi.org/10.1109/tro.2024.3370089)
- Stölzle, M., Rus, D. & Della Santina, C. An Experimental Study of Model-Based Control for Planar Handed Shearing Auxetics Robots. Springer Proceedings in Advanced Robotics 153–167 (2024) doi:10.1007/978-3-031-63596-0_14 -- [10.1007/978-3-031-63596-0_14](https://doi.org/10.1007/978-3-031-63596-0_14)
- Franco, E. & Borja, P. Integral IDA-PBC of Underactuated Mechanical Systems with Actuator Dynamics and Uncertain Coupling. IFAC-PapersOnLine vol. 58 19–24 (2024) -- [10.1016/j.ifacol.2024.08.250](https://doi.org/10.1016/j.ifacol.2024.08.250)
- Xavier, M. S. et al. Soft Pneumatic Actuators: A Review of Design, Fabrication, Modeling, Sensing, Control and Applications. IEEE Access vol. 10 59442–59485 (2022) -- [10.1109/access.2022.3179589](https://doi.org/10.1109/access.2022.3179589)
- Zaidi, S., Maselli, M., Laschi, C. & Cianchetti, M. Actuation Technologies for Soft Robot Grippers and Manipulators: A Review. Current Robotics Reports vol. 2 355–369 (2021) -- [10.1007/s43154-021-00054-5](https://doi.org/10.1007/s43154-021-00054-5)
- Yang, H., Xu, M., Li, W. & Zhang, S. Design and Implementation of a Soft Robotic Arm Driven by SMA Coils. IEEE Transactions on Industrial Electronics vol. 66 6108–6116 (2019) -- [10.1109/tie.2018.2872005](https://doi.org/10.1109/tie.2018.2872005)
- Kubo, K. et al. Simultaneous 3D Forming and Patterning Method of Realizing Soft IPMC Robots. 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 8815–8822 (2020) doi:10.1109/iros45743.2020.9341062 -- [10.1109/iros45743.2020.9341062](https://doi.org/10.1109/iros45743.2020.9341062)
- Zari, E. et al. A Reinforced Light-Responsive Hydrogel for Soft Robotics Actuation. 2024 IEEE 7th International Conference on Soft Robotics (RoboSoft) 270–275 (2024) doi:10.1109/robosoft60065.2024.10521980 -- [10.1109/robosoft60065.2024.10521980](https://doi.org/10.1109/robosoft60065.2024.10521980)
- O’Halloran, A., O’Malley, F. & McHugh, P. A review on dielectric elastomer actuators, technology, applications, and challenges. Journal of Applied Physics vol. 104 (2008) -- [10.1063/1.2981642](https://doi.org/10.1063/1.2981642)
- Plante, J.-S. & Dubowsky, S. On the properties of dielectric elastomer actuators and their design implications. Smart Materials and Structures vol. 16 S227–S236 (2007) -- [10.1088/0964-1726/16/2/s05](https://doi.org/10.1088/0964-1726/16/2/s05)
- Gupta, U., Qin, L., Wang, Y., Godaba, H. & Zhu, J. Soft robots based on dielectric elastomer actuators: a review. Smart Materials and Structures vol. 28 103002 (2019) -- [10.1088/1361-665x/ab3a77](https://doi.org/10.1088/1361-665x/ab3a77)
- Shintake, J., Cacucciolo, V., Floreano, D. & Shea, H. Soft Robotic Grippers. Advanced Materials vol. 30 (2018) -- [10.1002/adma.201707035](https://doi.org/10.1002/adma.201707035)
- Yang, Y. et al. Muscle-inspired soft robots based on bilateral dielectric elastomer actuators. Microsystems &amp; Nanoengineering vol. 9 (2023) -- [10.1038/s41378-023-00592-2](https://doi.org/10.1038/s41378-023-00592-2)
- Feng, W. et al. A large-strain and ultrahigh energy density dielectric elastomer for fast moving soft robot. Nature Communications vol. 15 (2024) -- [10.1038/s41467-024-48243-y](https://doi.org/10.1038/s41467-024-48243-y)
- Duduta, M., Clarke, D. R. & Wood, R. J. A high speed soft robot based on dielectric elastomer actuators. 2017 IEEE International Conference on Robotics and Automation (ICRA) 4346–4351 (2017) doi:10.1109/icra.2017.7989501 -- [10.1109/icra.2017.7989501](https://doi.org/10.1109/icra.2017.7989501)
- Ren, Z. et al. A High‐Lift Micro‐Aerial‐Robot Powered by Low‐Voltage and Long‐Endurance Dielectric Elastomer Actuators. Advanced Materials vol. 34 (2022) -- [10.1002/adma.202106757](https://doi.org/10.1002/adma.202106757)
- Pelrine, R. et al. &lt;title&gt;Dielectric elastomer artificial muscle actuators: toward biomimetic motion&lt;/title&gt; SPIE Proceedings vol. 4695 126–137 (2002) -- [10.1117/12.475157](https://doi.org/10.1117/12.475157)
- Suo, Z. Theory of dielectric elastomers. Acta Mechanica Solida Sinica vol. 23 549–578 (2010) -- [10.1016/s0894-9166(11)60004-9](https://doi.org/10.1016/s0894-9166(11)60004-9)
- Patrick, L., Gabor, K. & Silvain, M. Characterization of dielectric elastomer actuators based on a hyperelastic film model. Sensors and Actuators A: Physical vol. 135 748–757 (2007) -- [10.1016/j.sna.2006.08.006](https://doi.org/10.1016/j.sna.2006.08.006)
- Gu, G.-Y., Gupta, U., Zhu, J., Zhu, L.-M. & Zhu, X. Modeling of Viscoelastic Electromechanical Behavior in a Soft Dielectric Elastomer Actuator. IEEE Transactions on Robotics vol. 33 1263–1271 (2017) -- [10.1109/tro.2017.2706285](https://doi.org/10.1109/tro.2017.2706285)
- Gisby, T. A., Calius, E. P., Xie, S. & Anderson, I. A. An adaptive control method for dielectric elastomer devices. SPIE Proceedings vol. 6927 69271C (2008) -- [10.1117/12.776503](https://doi.org/10.1117/12.776503)
- Branz, F. & Francesconi, A. Modelling and control of double-cone dielectric elastomer actuator. Smart Materials and Structures vol. 25 095040 (2016) -- [10.1088/0964-1726/25/9/095040](https://doi.org/10.1088/0964-1726/25/9/095040)
- Hoffstadt, T. & Maas, J. Adaptive Sliding-Mode Position Control for Dielectric Elastomer Actuators. IEEE/ASME Transactions on Mechatronics vol. 22 2241–2251 (2017) -- [10.1109/tmech.2017.2730589](https://doi.org/10.1109/tmech.2017.2730589)
- Rizzello, G., Serafino, P., Naso, D. & Seelecke, S. Towards Sensorless Soft Robotics: Self-Sensing Stiffness Control of Dielectric Elastomer Actuators. IEEE Transactions on Robotics vol. 36 174–188 (2020) -- [10.1109/tro.2019.2944592](https://doi.org/10.1109/tro.2019.2944592)
- Huang, P., Wu, J., Zhang, P., Wang, Y. & Su, C.-Y. Dynamic Modeling and Tracking Control for Dielectric Elastomer Actuator With a Model Predictive Controller. IEEE Transactions on Industrial Electronics vol. 69 1819–1828 (2022) -- [10.1109/tie.2021.3063976](https://doi.org/10.1109/tie.2021.3063976)
- Bernat, J. & Kolota, J. Active Disturbance Rejection Control for Dielectric Electroactive Polymer Actuator. IEEE Access vol. 9 95218–95227 (2021) -- [10.1109/access.2021.3094271](https://doi.org/10.1109/access.2021.3094271)
- Zou, J. et al. A Generalized Motion Control Framework of Dielectric Elastomer Actuators: Dynamic Modeling, Sliding-Mode Control and Experimental Evaluation. IEEE Transactions on Robotics vol. 40 919–935 (2024) -- [10.1109/tro.2023.3338973](https://doi.org/10.1109/tro.2023.3338973)
- Cao, C., Wu, C., Li, X., Wang, L. & Gao, X. A Quad‐Unit Dielectric Elastomer Actuator for Programmable Two‐Dimensional Trajectories. Advanced Intelligent Systems vol. 6 (2024) -- [10.1002/aisy.202300865](https://doi.org/10.1002/aisy.202300865)
- Massenio, P. R., Prechtl, J., Naso, D. & Rizzello, G. Nonlinear Optimal Control of a Soft Robotic Structure Actuated by Dielectric Elastomer Artificial Muscles. 2022 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM) 644–649 (2022) doi:10.1109/aim52237.2022.9863262 -- [10.1109/aim52237.2022.9863262](https://doi.org/10.1109/aim52237.2022.9863262)
- Chi, Y. et al. Bistable and Multistable Actuators for Soft Robots: Structures, Materials, and Functionalities. Advanced Materials vol. 34 (2022) -- [10.1002/adma.202110384](https://doi.org/10.1002/adma.202110384)
- Baltes, M., Kunze, J., Prechtl, J., Seelecke, S. & Rizzello, G. A bi-stable soft robotic bendable module driven by silicone dielectric elastomer actuators: design, characterization, and parameter study. Smart Materials and Structures vol. 31 114002 (2022) -- [10.1088/1361-665x/ac96df](https://doi.org/10.1088/1361-665x/ac96df)
- Hajiesmaili, E. & Clarke, D. R. Dielectric elastomer actuators. Journal of Applied Physics vol. 129 (2021) -- [10.1063/5.0043959](https://doi.org/10.1063/5.0043959)
- [Soleti, G., Prechtl, J., Massenio, P. R., Baltes, M. & Rizzello, G. Energy based control of a bi-stable and underactuated soft robotic system based on dielectric elastomer actuators*. IFAC-PapersOnLine vol. 56 7796–7801 (2023)](energy-based-control-of-a-bi-stable-and-underactuated-soft-robotic-system-based-on-dielectric-elastomer-actuators) -- [10.1016/j.ifacol.2023.10.1153](https://doi.org/10.1016/j.ifacol.2023.10.1153)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Awtar, S. & Sen, S. A Generalized Constraint Model for Two-Dimensional Beam Flexures: Nonlinear Strain Energy Formulation. Journal of Mechanical Design vol. 132 (2010) -- [10.1115/1.4002006](https://doi.org/10.1115/1.4002006)
- Khalil, Control of Nonlinear Systems (2002)
- Prechtl, J., Baltes, M., Flaßkamp, K. & Rizzello, G. Sensorless Proprioception in Multi-DoF Dielectric Elastomer Soft Robots via System-Level Self-Sensing. IEEE/ASME Transactions on Mechatronics vol. 29 4365–4376 (2024) -- [10.1109/tmech.2024.3375923](https://doi.org/10.1109/tmech.2024.3375923)

