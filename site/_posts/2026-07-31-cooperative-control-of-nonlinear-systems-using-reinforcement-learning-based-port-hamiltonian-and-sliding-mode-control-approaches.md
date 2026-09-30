---
title: "Cooperative control of nonlinear systems using reinforcement learning based port-Hamiltonian and sliding mode control approaches"
date: 2026-07-31 00:00:00 +0100
permalink: cooperative-control-of-nonlinear-systems-using-reinforcement-learning-based-port-hamiltonian-and-sliding-mode-control-approaches
year: 2026
authors: Aiyun Zhu, Haisheng Yu, Tao Xu
category: articles
tags:
  - cooperative control, nonlinear systems, port-hamiltonian systems, reinforcement learning, sliding mode control
---
 
## Authors
[Aiyun Zhu](authors/aiyun-zhu), [Haisheng Yu](authors/haisheng-yu), [Tao Xu](authors/tao-xu)
 
## Abstract
This paper proposes a dual-subsystem cooperative control architecture for a class of affine nonlinear systems. By employing a cooperative weighting function that satisfies the convex combination mechanism, the architecture achieves deep integration of reinforcement learning-based port-Hamiltonian (RL-PH) control and RL-based sliding mode control (RL-SMC). Specifically, the first subsystem aims to enhance steady-state performance. By parameterizing damping injection and additional energy, a reinforcement learning algorithm is adopted to online tune the unknown parameters. This approach not only avoids the complexity of solving the Hamilton–Jacobi–Bellman partial differential equation within the PH framework, but also realizes optimal PH control. The second subsystem focuses on improving transient performance. By constructing a cost function associated with the sliding surface, the conventional SMC is transformed into an optimal control problem, which is approximated by a critic neural network (NN). Furthermore, a nested updating law is meticulously designed to strictly guarantee the asymptotic stability of the NN weight estimation error. Finally, a Gaussian function-based cooperative mechanism is constructed to achieve the seamless fusion of the two control laws. Experimental results demonstrate that the proposed strategy significantly outperforms the standalone RL-PH or RL-SMC methods in terms of both steady-state accuracy and dynamic response speed.
 
## Keywords
cooperative control, nonlinear systems, port-hamiltonian systems, reinforcement learning, sliding mode control
 
## Citation
- **Journal:** Neurocomputing
- **Year:** 2026
- **Volume:** 702
- **Issue:** 
- **Pages:** 134597
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.neucom.2026.134597](https://doi.org/10.1016/j.neucom.2026.134597)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Zhu_2026,
  title={{Cooperative control of nonlinear systems using reinforcement learning based port-Hamiltonian and sliding mode control approaches}},
  volume={702},
  ISSN={0925-2312},
  DOI={10.1016/j.neucom.2026.134597},
  journal={Neurocomputing},
  publisher={Elsevier BV},
  author={Zhu, Aiyun and Yu, Haisheng and Xu, Tao},
  year={2026},
  pages={134597}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/cooperative-control-of-nonlinear-systems-using-reinforcement-learning-based-port-hamiltonian-and-sliding-mode-control-approaches.bib)
 
## References
- [Ponce C, Ramirez H, Le Gorrec Y (2025) Reduced-order energy shaping control of large-scale linear port-Hamiltonian systems. Automatica 171:111934. https://doi.org/10.1016/j.automatica.2024.11193](reduced-order-energy-shaping-control-of-large-scale-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2024.111934](https://doi.org/10.1016/j.automatica.2024.111934)
- [Ortega R, van der Schaft A, Castanos F, Astolfi A (2008) Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans Automat Contr 53(11):2527–2542. https://doi.org/10.1109/tac.2008.200693](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- [Liu N, Wu Y, Le Gorrec Y, Lefèvre L, Ramirez H (2024) Reduced order in domain control of distributed parameter port-Hamiltonian systems via energy shaping. Automatica 161:111500. https://doi.org/10.1016/j.automatica.2023.11150](reduced-order-in-domain-control-of-distributed-parameter-port-hamiltonian-systems-via-energy-shaping) -- [10.1016/j.automatica.2023.111500](https://doi.org/10.1016/j.automatica.2023.111500)
- Mattioni M, Moreschini A, Monaco S, Normand-Cyrot D (2022) Discrete-time energy-balance passivity-based control. Automatica 146:110662. https://doi.org/10.1016/j.automatica.2022.11066 -- [10.1016/j.automatica.2022.110662](https://doi.org/10.1016/j.automatica.2022.110662)
- [Yu H, Yu J, Wu H, Li H (2013) Energy-shaping and integral control of the three-tank liquid level system. Nonlinear Dyn 73(4):2149–2156. https://doi.org/10.1007/s11071-013-0930-](energy-shaping-and-integral-control-of-the-three-tank-liquid-level-system) -- [10.1007/s11071-013-0930-8](https://doi.org/10.1007/s11071-013-0930-8)
- [Yu H, Yu J, Liu J, Song Q (2012) Nonlinear control of induction motors based on state error PCH and energy-shaping principle. Nonlinear Dyn 72(1–2):49–59. https://doi.org/10.1007/s11071-012-0689-](nonlinear-control-of-induction-motors-based-on-state-error-pch-and-energy-shaping-principle) -- [10.1007/s11071-012-0689-3](https://doi.org/10.1007/s11071-012-0689-3)
- [Zhu A, Yu H, Gao X (2024) Cooperative control of NN super twisting sliding mode and EPH methods for uncertain nonlinear systems. Journal of the Franklin Institute 361(3):1186–1210. https://doi.org/10.1016/j.jfranklin.2023.12.04](cooperative-control-of-nn-super-twisting-sliding-mode-and-eph-methods-for-uncertain-nonlinear-systems) -- [10.1016/j.jfranklin.2023.12.049](https://doi.org/10.1016/j.jfranklin.2023.12.049)
- [Kumar L, Dhillon SS (2023) Tracking control design for fractional order systems: A passivity-based port-Hamiltonian framework. ISA Transactions 138:1–9. https://doi.org/10.1016/j.isatra.2023.03.02](tracking-control-design-for-fractional-order-systems-a-passivity-based-port-hamiltonian-framework) -- [10.1016/j.isatra.2023.03.024](https://doi.org/10.1016/j.isatra.2023.03.024)
- [Fu B, Wang X, Wang Q (2021) Protocol design for group output consensus of disturbed port-controlled Hamiltonian multi-agent systems. Journal of the Franklin Institute 358(18):9867–9889. https://doi.org/10.1016/j.jfranklin.2021.10.00](protocol-design-for-group-output-consensus-of-disturbed-port-controlled-hamiltonian-multi-agent-systems) -- [10.1016/j.jfranklin.2021.10.006](https://doi.org/10.1016/j.jfranklin.2021.10.006)
- [Azimi SM, Lotfifard S (2024) Unified Damping Assignment Passivity Based Controller for Power Conversion Units of Solar Power Plants. IEEE Trans Energy Convers 39(4):2258–2268. https://doi.org/10.1109/tec.2024.340614](unified-damping-assignment-passivity-based-controller-for-power-conversion-units-of-solar-power-plants) -- [10.1109/tec.2024.3406147](https://doi.org/10.1109/tec.2024.3406147)
- [Breiten T, Hinsen D, Unger B (2024) Toward a Class of Port-Hamiltonian Systems With Time-Delays. IEEE Trans Automat Contr 69(12):8924–8930. https://doi.org/10.1109/tac.2024.346433](toward-a-class-of-port-hamiltonian-systems-with-time-delays) -- [10.1109/tac.2024.3464332](https://doi.org/10.1109/tac.2024.3464332)
- [Sun J, Xing X, Zhang R, Zhang C (2025) An Enhanced Transient Angle Stability Scheme of VSG Based on the PCH Theory. IEEE Trans Ind Electron 72(4):3861–3871. https://doi.org/10.1109/tie.2024.345448](an-enhanced-transient-angle-stability-scheme-of-vsg-based-on-the-pch-theory) -- [10.1109/tie.2024.3454485](https://doi.org/10.1109/tie.2024.3454485)
- Grondman I, Vaandrager M, Busoniu L, Babuska R, Schuitema E (2012) Efficient Model Learning Methods for Actor–Critic Control. IEEE Trans Syst, Man, Cybern B 42(3):591–602. https://doi.org/10.1109/tsmcb.2011.217056 -- [10.1109/tsmcb.2011.2170565](https://doi.org/10.1109/tsmcb.2011.2170565)
- [Nageshrao SP, Lopes GAD, Jeltsema D, Babuška R (2014) Passivity-based reinforcement learning control of a 2-DOF manipulator arm. Mechatronics 24(8):1001–1007. https://doi.org/10.1016/j.mechatronics.2014.10.00](passivity-based-reinforcement-learning-control-of-a-2-dof-manipulator-arm) -- [10.1016/j.mechatronics.2014.10.005](https://doi.org/10.1016/j.mechatronics.2014.10.005)
- [Sprangers O, Babuska R, Nageshrao SP, Lopes GAD (2015) Reinforcement Learning for Port-Hamiltonian Systems. IEEE Trans Cybern 45(5):1017–1027. https://doi.org/10.1109/tcyb.2014.234319](reinforcement-learning-for-port-hamiltonian-systems) -- [10.1109/tcyb.2014.2343194](https://doi.org/10.1109/tcyb.2014.2343194)
- [Nageshrao SP, Lopes GAD, Jeltsema D, Babuska R (2016) Port-Hamiltonian Systems in Adaptive and Learning Control: A Survey. IEEE Trans Automat Contr 61(5):1223–1238. https://doi.org/10.1109/tac.2015.245849](port-hamiltonian-systems-in-adaptive-and-learning-control-a-survey) -- [10.1109/tac.2015.2458491](https://doi.org/10.1109/tac.2015.2458491)
- [Sebastián E, Duong T, Atanasov N, Montijano E, Sagüés C (2025) Physics-Informed Multiagent Reinforcement Learning for Distributed Multirobot Problems. IEEE Trans Robot 41:4499–4517. https://doi.org/10.1109/tro.2025.358283](physics-informed-multiagent-reinforcement-learning-for-distributed-multirobot-problems) -- [10.1109/tro.2025.3582836](https://doi.org/10.1109/tro.2025.3582836)
- Zhao X, Yang H, Xia W, Wang X (2017) Adaptive Fuzzy Hierarchical Sliding-Mode Control for a Class of MIMO Nonlinear Time-Delay Systems With Input Saturation. IEEE Trans Fuzzy Syst 25(5):1062–1077. https://doi.org/10.1109/tfuzz.2016.259427 -- [10.1109/tfuzz.2016.2594273](https://doi.org/10.1109/tfuzz.2016.2594273)
- Zhao X, Yang H, Zong G (2017) Adaptive Neural Hierarchical Sliding Mode Control of Nonstrict-Feedback Nonlinear Systems and an Application to Electronic Circuits. IEEE Trans Syst Man Cybern, Syst 47(7):1394–1404. https://doi.org/10.1109/tsmc.2016.261388 -- [10.1109/tsmc.2016.2613885](https://doi.org/10.1109/tsmc.2016.2613885)
- Li J, Yan X-G, Niu Y (2024) Finite-Time Boundedness of Interconnected System Using Decentralized Output-Feedback Sliding Mode Control. IEEE Trans Automat Contr 69(11):7847–7854. https://doi.org/10.1109/tac.2024.339909 -- [10.1109/tac.2024.3399092](https://doi.org/10.1109/tac.2024.3399092)
- Wu Y, Wang Y-Y, Xie X-P, Wu Z-G, Yan H-C (2024) Adaptive Reinforcement Learning Strategy-Based Sliding Mode Control of Uncertain Euler–Lagrange Systems With Prescribed Performance Guarantees: Autonomous Underwater Vehicles-Based Verification. IEEE Trans Fuzzy Syst 32(11):6160–6171. https://doi.org/10.1109/tfuzz.2024.344171 -- [10.1109/tfuzz.2024.3441714](https://doi.org/10.1109/tfuzz.2024.3441714)
- Nguyen V-T, Giap H-B, Su S-F, Van M, La D-V, Bui T-L (2025) Design and Experiment of Interval Type-2 Fuzzy Hierarchical Sliding-Mode Control for Pendubot With Uncertainties. IEEE/ASME Trans Mechatron 30(4):2562–2573. https://doi.org/10.1109/tmech.2024.345701 -- [10.1109/tmech.2024.3457015](https://doi.org/10.1109/tmech.2024.3457015)
- Li Y, Zhang Z (2025) High-Order Nonsingular Fast Integral Terminal Sliding Mode Control With Perturbation Estimation for a Class of Nonlinear Hysteresis Systems. IEEE Trans Ind Electron 72(2):2045–2055. https://doi.org/10.1109/tie.2024.342965 -- [10.1109/tie.2024.3429652](https://doi.org/10.1109/tie.2024.3429652)
- Yang P, Zhang S, Yu X, Feng N, Xing Y, He W (2025) Neural networks-based terminal sliding mode fault tolerant control to quadruped robots with actuator fault. Neurocomputing 647:130457. https://doi.org/10.1016/j.neucom.2025.13045 -- [10.1016/j.neucom.2025.130457](https://doi.org/10.1016/j.neucom.2025.130457)
- Ovalle L, Gonzalez A, Fridman L, Laghrouche S, Obeid H (2025) Analysis of barrier function based adaptive sliding mode control in the presence of deterministic noise. Automatica 171:111946. https://doi.org/10.1016/j.automatica.2024.11194 -- [10.1016/j.automatica.2024.111946](https://doi.org/10.1016/j.automatica.2024.111946)
- Li J, Zhao Z, Qin X (2024) Adaptive sliding mode control using a novel fully feedback recurrent neural network for quad-rotor UAVs. Neurocomputing 610:128592. https://doi.org/10.1016/j.neucom.2024.12859 -- [10.1016/j.neucom.2024.128592](https://doi.org/10.1016/j.neucom.2024.128592)
- Zhang H, Yu J, Shi P, Hu S, Zhao L (2025) Adaptive continuous fractional-order nonsingular terminal sliding mode control based on neural network for PMLM system with actuator saturation. Neurocomputing 646:130468. https://doi.org/10.1016/j.neucom.2025.13046 -- [10.1016/j.neucom.2025.130468](https://doi.org/10.1016/j.neucom.2025.130468)
- Chen W-H, Xu W, Zheng WX (2024) Sliding-mode-based impulsive control for a class of time-delay systems with input disturbance. Automatica 164:111633. https://doi.org/10.1016/j.automatica.2024.11163 -- [10.1016/j.automatica.2024.111633](https://doi.org/10.1016/j.automatica.2024.111633)
- Wang Y, Zhang M, Tian S, Lu C, Wu M, Sato D (2024) An Adaptive Integral Sliding Mode Control-Based Amplitude and Phase Compensation Repetitive Control Method. IEEE Trans Ind Electron 71(12):16644–16653. https://doi.org/10.1109/tie.2024.340118 -- [10.1109/tie.2024.3401183](https://doi.org/10.1109/tie.2024.3401183)
- Deng Y, Moulay E, Léchappé V, Chen Z, Liang B, Plestan F (2024) Robust Nonsingular Predefined-Time Terminal Sliding Mode Control for Perturbed Chains of Integrators. IEEE Trans Automat Contr 69(12):8946–8953. https://doi.org/10.1109/tac.2024.342655 -- [10.1109/tac.2024.3426554](https://doi.org/10.1109/tac.2024.3426554)
- Chen Y, Liang J, Wu Y, Miao Z, Zhang H, Wang Y (2023) Adaptive Sliding-Mode Disturbance Observer-Based Finite-Time Control for Unmanned Aerial Manipulator With Prescribed Performance. IEEE Trans Cybern 53(5):3263–3276. https://doi.org/10.1109/tcyb.2022.316803 -- [10.1109/tcyb.2022.3168030](https://doi.org/10.1109/tcyb.2022.3168030)
- Li J, Yuan L, Chai T, Lewis FL (2023) Consensus of Nonlinear Multiagent Systems With Uncertainties Using Reinforcement Learning Based Sliding Mode Control. IEEE Trans Circuits Syst I 70(1):424–434. https://doi.org/10.1109/tcsi.2022.320610 -- [10.1109/tcsi.2022.3206102](https://doi.org/10.1109/tcsi.2022.3206102)
- Yan Y, Zhang H, Sun J, Wang Y (2024) Sliding Mode Control Based on Reinforcement Learning for T-S Fuzzy Fractional-Order Multiagent System With Time-Varying Delays. IEEE Trans Neural Netw Learning Syst 35(8):10368–10379. https://doi.org/10.1109/tnnls.2023.324107 -- [10.1109/tnnls.2023.3241070](https://doi.org/10.1109/tnnls.2023.3241070)
- Zhao B, Liu D, Alippi C (2021) Sliding-Mode Surface-Based Approximate Optimal Control for Uncertain Nonlinear Systems With Asymptotically Stable Critic Structure. IEEE Trans Cybern 51(6):2858–2869. https://doi.org/10.1109/tcyb.2019.296201 -- [10.1109/tcyb.2019.2962011](https://doi.org/10.1109/tcyb.2019.2962011)
- Wang T, Wang H, Xu N, Zhang L, Alharbi KH (2023) Sliding-mode surface-based decentralized event-triggered control of partially unknown interconnected nonlinear systems via reinforcement learning. Information Sciences 641:119070. https://doi.org/10.1016/j.ins.2023.11907 -- [10.1016/j.ins.2023.119070](https://doi.org/10.1016/j.ins.2023.119070)
- Zhang H, Wang H, Niu B, Zhang L, Ahmad AM (2021) Sliding-mode surface-based adaptive actor-critic optimal control for switched nonlinear systems with average dwell time. Information Sciences 580:756–774. https://doi.org/10.1016/j.ins.2021.08.06 -- [10.1016/j.ins.2021.08.062](https://doi.org/10.1016/j.ins.2021.08.062)
- Wan L, Smith S, Pan Y-J, Witrant E (2026) Adaptive Task Space Nonsingular Terminal Super-Twisting Sliding Mode Control of a 7-DOF Robotic Manipulator. IEEE Trans Ind Electron 73(1):1352–1363. https://doi.org/10.1109/tie.2025.360052 -- [10.1109/tie.2025.3600520](https://doi.org/10.1109/tie.2025.3600520)
- Zhang, A robust MPCC strategy with improved super-twisting observer-based nonsingular integral terminal sliding-mode speed controller for IPMSM. IEEE Trans. Transp. Electrif. (2026)

