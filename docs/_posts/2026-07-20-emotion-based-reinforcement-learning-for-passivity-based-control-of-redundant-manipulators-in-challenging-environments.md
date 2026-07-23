---
title: "Emotion-Based Reinforcement Learning for Passivity-Based Control of Redundant Manipulators in Challenging Environments"
date: 2026-07-20 00:00:00 +0100
permalink: emotion-based-reinforcement-learning-for-passivity-based-control-of-redundant-manipulators-in-challenging-environments
year: 2026
authors: Rami Al-Khulaidi, Tien-Fu Lu, Steven Grainger, Rini Akmeliawati
category: articles
tags:
  - bio-inspired control, emotion-based learning, finite-state machine, passivity-based control, redundant manipulator, reinforcement learning
---
 
## Authors
[Rami Al-Khulaidi](authors/rami-al-khulaidi), [Tien-Fu Lu](authors/tien-fu-lu), [Steven Grainger](authors/steven-grainger), [Rini Akmeliawati](authors/rini-akmeliawati)
 
## Abstract
Controlling redundant manipulators in unstructured environments like agricultural settings is challenging due to high nonlinearities and the need for both precision and stability. This paper presents a novel intelligent control architecture that integrates a stable-by-design Passivity-Based Control (PBC) law with a bio-inspired reinforcement learning tuner. The core novelty lies in our Human Learning Behaviour (HLB) model, which, unlike conventional reward shaping, employs a finite-state machine to dynamically modulate the exploration strategy of a Deep Deterministic Policy Gradient (DDPG) agent. This state machine transitions between discrete states, framed as artificial emotions (e.g., Joy, Fear), based on real-time performance indicators. Each state directly adjusts the agent's exploration noise, enabling it to learn more efficiently by exploring aggressively when performance is poor and exploiting known good policies when performance is high. This adaptive tuner intelligently adjusts the proportional (Kp) and differential (KD) gains of the PBC law, which is derived from a Port-Controlled Hamiltonian (PCH) model to ensure the underlying manipulator dynamics remain stable for any positive-definite gains selected by the learning agent. Validated on an 8-DOF manipulator in simulated, obstacle-rich agricultural scenarios, the HLB-driven controller demonstrated a 77–80% improvement in trajectory tracking and a 30.7% reduction in energy consumption compared to fixed-gain and standard DDPG baselines, while maintaining a final tracking error of approximately 10⁻⁴ radians. The results confirm that our FSM-based adaptive exploration strategy yields a highly precise, energy-efficient, and robust intelligent control system suitable for complex robotic applications.
 
## Keywords
bio-inspired control, emotion-based learning, finite-state machine, passivity-based control, redundant manipulator, reinforcement learning
 
## Citation
- **Journal:** Applied Soft Computing
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 115997
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.asoc.2026.115997](https://doi.org/10.1016/j.asoc.2026.115997)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Al_Khulaidi_2026,
  title={{Emotion-Based Reinforcement Learning for Passivity-Based Control of Redundant Manipulators in Challenging Environments}},
  ISSN={1568-4946},
  DOI={10.1016/j.asoc.2026.115997},
  journal={Applied Soft Computing},
  publisher={Elsevier BV},
  author={Al-Khulaidi, Rami and Lu, Tien-Fu and Grainger, Steven and Akmeliawati, Rini},
  year={2026},
  pages={115997}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/emotion-based-reinforcement-learning-for-passivity-based-control-of-redundant-manipulators-in-challenging-environments.bib)
 
## References
- Heravi, Development of a field robot platform for mechanical weed control in greenhouse cultivation of cucumber. Agricultural Robots: Fundamentals and Applications (2018)
- Xiong, An autonomous strawberry-harvesting robot: Design, development, integration, and field evaluation. Journal of Field Robotics (2019)
- Endo G, Horigome A, Takata A (2019) Super Dragon: A 10-m-Long-Coupled Tendon-Driven Articulated Manipulator. IEEE Robot Autom Lett 4(2):934–941. https://doi.org/10.1109/lra.2019.289485 -- [10.1109/lra.2019.2894855](https://doi.org/10.1109/lra.2019.2894855)
- Tang L, Wang J, Zheng Y, Gu G, Zhu L, Zhu X (2017) Design of a cable-driven hyper-redundant robot with experimental validation. International Journal of Advanced Robotic Systems 14(5):172988141773445. https://doi.org/10.1177/172988141773445 -- [10.1177/1729881417734458](https://doi.org/10.1177/1729881417734458)
- Tang J, Zhang Y, Huang F, Li J, Chen Z, Song W, Zhu S, Gu J (2019) Design and Kinematic Control of the Cable-Driven Hyper-Redundant Manipulator for Potential Underwater Applications. Applied Sciences 9(6):1142. https://doi.org/10.3390/app906114 -- [10.3390/app9061142](https://doi.org/10.3390/app9061142)
- Duarte, Chaotic phenomena and performance optimization in the trajectory control of redundant manipulators. Recent Advances in Mechatronics (1998)
- Duarte, A chaos perspective in the trajectory control of redundant manipulators. IEEE International Conference on Intelligent Engineering Systems (1999)
- Duarte, Motion chaos in the pseudoinverse control of redundant robots. 6th International Workshop on Advanced Motion Control (2000)
- Abbasi V, Azria B, Tabarah E, Menon V, Phillips E, Bedirian M (2004) Improved 7-DOF Control of ISS Robotic Manipulators. Space OPS 2004 Conferenc -- [10.2514/6.2004-610-407](https://doi.org/10.2514/6.2004-610-407)
- Yahya S, Moghavvemi M, Mohamed HAF (2011) Geometrical approach of planar hyper-redundant manipulators: Inverse kinematics, path planning and workspace. Simulation Modelling Practice and Theory 19(1):406–422. https://doi.org/10.1016/j.simpat.2010.08.00 -- [10.1016/j.simpat.2010.08.001](https://doi.org/10.1016/j.simpat.2010.08.001)
- Tenreiro Machado JA, Lopes AM (2017) A fractional perspective on the trajectory control of redundant and hyper-redundant robot manipulators. Applied Mathematical Modelling 46:716–726. https://doi.org/10.1016/j.apm.2016.11.00 -- [10.1016/j.apm.2016.11.005](https://doi.org/10.1016/j.apm.2016.11.005)
- Choudhury A, Genin J (1989) Kinematics of an n-Degree- of-Freedom Multi-Link Robotic System. The International Journal of Robotics Research 8(6):132–140. https://doi.org/10.1177/02783649890080060 -- [10.1177/027836498900800609](https://doi.org/10.1177/027836498900800609)
- [Ortega R, van der Schaft A, Castanos F, Astolfi A (2008) Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans Automat Contr 53(11):2527–2542. https://doi.org/10.1109/tac.2008.200693](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- Byrnes CI, Isidori A, Willems JC (1991) Passivity, feedback equivalence, and the global stabilization of minimum phase nonlinear systems. IEEE Trans Automat Contr 36(11):1228–1240. https://doi.org/10.1109/9.10093 -- [10.1109/9.100932](https://doi.org/10.1109/9.100932)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- [Rashad R, Califano F, van der Schaft AJ, Stramigioli S (2020) Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information 37(4):1400–1422. https://doi.org/10.1093/imamci/dnaa01](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Duindam, (2009)
- Tai, Virtual-to-real deep reinforcement learning. IEEE/RSJ IROS (2017)
- Liang, Learning to learn faster from human feedback with language model predictive control (2024)
- Hu Z, Jin X (2023) Adaptive formation control architectures for a team of quadrotors with multiple performance and safety constraints. Intl J Robust &amp; Nonlinear 33(14):8183–8204. https://doi.org/10.1002/rnc.682 -- [10.1002/rnc.6824](https://doi.org/10.1002/rnc.6824)
- Yao Z, Liang X, Jiang G-P, Yao J (2023) Model-Based Reinforcement Learning Control of Electrohydraulic Position Servo Systems. IEEE/ASME Trans Mechatron 28(3):1446–1455. https://doi.org/10.1109/tmech.2022.321911 -- [10.1109/tmech.2022.3219115](https://doi.org/10.1109/tmech.2022.3219115)
- Yao Z, Xu F, Jiang G-P, Yao J (2024) Data-Driven Control of Hydraulic Manipulators by Reinforcement Learning. IEEE/ASME Trans Mechatron 29(4):2673–2684. https://doi.org/10.1109/tmech.2023.333607 -- [10.1109/tmech.2023.3336070](https://doi.org/10.1109/tmech.2023.3336070)
- Yao Z, Liang X, Wang S, Yao J (2025) Model-Data Hybrid Driven Control of Hydraulic Euler–Lagrange Systems. IEEE/ASME Trans Mechatron 30(1):131–143. https://doi.org/10.1109/tmech.2024.339012 -- [10.1109/tmech.2024.3390129](https://doi.org/10.1109/tmech.2024.3390129)
- van der Schaft, Port-Hamiltonian systems: network modeling and control of nonlinear physical systems. (2004)
- Huang, A Momentum Recurrent Neural Network for Sparse Motion Planning of Redundant Manipulators With Majorization-Minimization. IEEE Transactions on Neural Networks and Learning Systems (2025)
- Wu, eMotions: A Large-Scale Dataset and Audio-Visual Fusion Network for Emotion Analysis in Short-form Videos (2025)
- Gao, EEmo-Bench: A Benchmark for Multi-modal Large Language Models on Image Evoked Emotion Assessment. (2025)
- Spong, (2006)
- Nho Cho C, Jung H, Son J, Gi Kim K (2015) A Modular Control Scheme for Hyper-Redundant Robots. International Journal of Advanced Robotic Systems 12(7). https://doi.org/10.5772/6060 -- [10.5772/60602](https://doi.org/10.5772/60602)
- da Graça Marcos M, Tenreiro Machado JA, Azevedo-Perdicoúlis T-P (2009) Trajectory planning of redundant manipulators using genetic algorithms. Communications in Nonlinear Science and Numerical Simulation 14(7):2858–2869. https://doi.org/10.1016/j.cnsns.2008.10.01 -- [10.1016/j.cnsns.2008.10.014](https://doi.org/10.1016/j.cnsns.2008.10.014)
- Menasri R, Nakib A, Daachi B, Oulhadj H, Siarry P (2015) A trajectory planning of redundant manipulators based on bilevel optimization. Applied Mathematics and Computation 250:934–947. https://doi.org/10.1016/j.amc.2014.10.10 -- [10.1016/j.amc.2014.10.101](https://doi.org/10.1016/j.amc.2014.10.101)
- Ayten KK, Sahinkaya MN, Dumlu A (2017) Real time optimum trajectory generation for redundant/hyper-redundant serial industrial manipulators. International Journal of Advanced Robotic Systems 14(6):172988141773724. https://doi.org/10.1177/172988141773724 -- [10.1177/1729881417737241](https://doi.org/10.1177/1729881417737241)
- Chembuly VVMJS, Voruganti HK (2018) Trajectory Planning of Redundant Manipulators Moving along Constrained Path and Avoiding Obstacles. Procedia Computer Science 133:627–634. https://doi.org/10.1016/j.procs.2018.07.09 -- [10.1016/j.procs.2018.07.094](https://doi.org/10.1016/j.procs.2018.07.094)
- Bagheri M, Naseradinmousavi P (2017) Novel analytical and experimental trajectory optimization of a 7-DOF baxter robot: global design sensitivity and step size analyses. Int J Adv Manuf Technol 93(9–12):4153–4167. https://doi.org/10.1007/s00170-017-0877- -- [10.1007/s00170-017-0877-x](https://doi.org/10.1007/s00170-017-0877-x)
- Guo D, Feng Q, Cai J (2019) Acceleration-Level Obstacle Avoidance of Redundant Manipulators. IEEE Access 7:183040–183048. https://doi.org/10.1109/access.2019.296039 -- [10.1109/access.2019.2960399](https://doi.org/10.1109/access.2019.2960399)
- Ayten KK, Sahinkaya MN, Dumlu A (2017) Real time optimum trajectory generation for redundant/hyper-redundant serial industrial manipulators. International Journal of Advanced Robotic Systems 14(6):172988141773724. https://doi.org/10.1177/172988141773724 -- [10.1177/1729881417737241](https://doi.org/10.1177/1729881417737241)
- Chembuly VVMJS, Voruganti HK (2018) Trajectory Planning of Redundant Manipulators Moving along Constrained Path and Avoiding Obstacles. Procedia Computer Science 133:627–634. https://doi.org/10.1016/j.procs.2018.07.09 -- [10.1016/j.procs.2018.07.094](https://doi.org/10.1016/j.procs.2018.07.094)
- Guo, (2016)
- Guo D, Zhang Y (2012) A New Inequality-Based Obstacle-Avoidance MVN Scheme and Its Application to Redundant Robot Manipulators. IEEE Trans Syst, Man, Cybern C 42(6):1326–1340. https://doi.org/10.1109/tsmcc.2012.218386 -- [10.1109/tsmcc.2012.2183868](https://doi.org/10.1109/tsmcc.2012.2183868)
- Guo D, Zhang Y (2014) Acceleration-Level Inequality-Based MAN Scheme for Obstacle Avoidance of Redundant Robot Manipulators. IEEE Trans Ind Electron 61(12):6903–6914. https://doi.org/10.1109/tie.2014.233103 -- [10.1109/tie.2014.2331036](https://doi.org/10.1109/tie.2014.2331036)
- [Aula A, Akmeliawati R, Ahmad S, Altalmas TM, Sidek SN (2013) Towards Port-Hamiltonian Approach for Modeling and Control of Two-wheeled Wheelchair. IOP Conf Ser: Mater Sci Eng 53:012074. https://doi.org/10.1088/1757-899x/53/1/01207](towards-port-hamiltonian-approach-for-modeling-and-control-of-two-wheeled-wheelchair) -- [10.1088/1757-899x/53/1/012074](https://doi.org/10.1088/1757-899x/53/1/012074)
- Astolfi A, Ortega R, Sepulchre R (2001) Passivity-based Control of Non-linear Systems. Control of Complex Systems 39–7 -- [10.1007/978-1-4471-0349-3_3](https://doi.org/10.1007/978-1-4471-0349-3_3)
- [Sprangers O, Babuska R, Nageshrao SP, Lopes GAD (2015) Reinforcement Learning for Port-Hamiltonian Systems. IEEE Trans Cybern 45(5):1017–1027. https://doi.org/10.1109/tcyb.2014.234319](reinforcement-learning-for-port-hamiltonian-systems) -- [10.1109/tcyb.2014.2343194](https://doi.org/10.1109/tcyb.2014.2343194)
- Yüksel, Reshaping the physical properties of a quadrotor through IDA-PBC. IEEE ICRA (2014)
- [Schenk C, Yüksel B, Secchi C, Bülthoff HH (2018) Port Hamiltonian Modeling of a Cable Driven Robot. IFAC-PapersOnLine 51(3):161–168. https://doi.org/10.1016/j.ifacol.2018.06.04](port-hamiltonian-modeling-of-a-cable-driven-robot) -- [10.1016/j.ifacol.2018.06.047](https://doi.org/10.1016/j.ifacol.2018.06.047)
- Huerta H, Vazquez N (2020) Spin-Coater Machine Control Via Passivity With Sliding Modes. IEEE Access 8:9760–9769. https://doi.org/10.1109/access.2020.296518 -- [10.1109/access.2020.2965188](https://doi.org/10.1109/access.2020.2965188)
- Zhao, Distributed formation control with relaxed communication for port-Hamiltonian systems. IEEE Transactions on Automatic Control (2025)
- Li, Physical intelligence-driven human-robot interaction. IEEE Transactions on Robotics (2025)
- [Duong T, Altawaitan A, Stanley J, Atanasov N (2024) Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control. IEEE Trans Robot 40:3695–3715. https://doi.org/10.1109/tro.2024.342843](port-hamiltonian-neural-ode-networks-on-lie-groups-for-robot-dynamics-learning-and-control) -- [10.1109/tro.2024.3428433](https://doi.org/10.1109/tro.2024.3428433)
- Arpenti, Integral passivity-based control for underactuated soft continuum manipulators. IEEE Robotics and Automation Letters (2024)
- Sweatland, Passivity-based optimization with safety guarantees. IEEE Control Systems Letters (2025)
- Zhang, Passivity-based twisting sliding mode control for series elastic actuators. IEEE Transactions on Robotics (2025)
- LaValle, (2006)
- Kavraki LE, Svestka P, Latombe J-C, Overmars MH (1996) Probabilistic roadmaps for path planning in high-dimensional configuration spaces. IEEE Trans Robot Automat 12(4):566–580. https://doi.org/10.1109/70.50843 -- [10.1109/70.508439](https://doi.org/10.1109/70.508439)
- Khatib O (1986) Real-Time Obstacle Avoidance for Manipulators and Mobile Robots. The International Journal of Robotics Research 5(1):90–98. https://doi.org/10.1177/02783649860050010 -- [10.1177/027836498600500106](https://doi.org/10.1177/027836498600500106)
- Rimon E, Koditschek DE (1992) Exact robot navigation using artificial potential functions. IEEE Trans Robot Automat 8(5):501–518. https://doi.org/10.1109/70.16377 -- [10.1109/70.163777](https://doi.org/10.1109/70.163777)

