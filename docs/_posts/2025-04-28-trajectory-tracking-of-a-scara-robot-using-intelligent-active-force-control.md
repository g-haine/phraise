---
title: "Trajectory tracking of a SCARA robot using intelligent active force control"
date: 2025-04-28 00:00:00 +0100
permalink: trajectory-tracking-of-a-scara-robot-using-intelligent-active-force-control
year: 2025
authors: Hanyi Huang, Adetokunbo Arogbonlo, Samson Yu, Lee Chung Kwek, Chee Peng Lim
category: articles
tags:
  - active force control, adaptive neuro-fuzzy inference system, inertia matrix, reinforcement learning, scara
---
 
## Authors
[Hanyi Huang](authors/hanyi-huang), [Adetokunbo Arogbonlo](authors/adetokunbo-arogbonlo), [Samson Yu](authors/samson-yu), [Lee Chung Kwek](authors/lee-chung-kwek), [Chee Peng Lim](authors/chee-peng-lim)
 
## Abstract
Trajectory tracking with disturbance rejection is a challenging problem in robotics, particularly in applications involving selective compliance articulated robot arms (SCARA). In this paper, we address the trajectory tracking problem with the presence of disturbances in applying SCARA, by designing controllers with active force control (AFC)-based control methods. AFC has shown potential in disturbance rejection, and its per efficiency of the designed controllers, we integrated different machine learning techniques into the AFC controller, including iterative learning (IL), adaptive neuro-fuzzy inference system (ANFIS) and reinforcement learning (RL). Two case studies were conducted and compared with two different benchmark controllers to validate intelligent AFC-based controllers: a port-controlled Hamiltonian (PCH) control and a hybrid proportional-integral-derivative (PID) control. The results demonstrate that the AFC-based controllers consistently outperform the benchmark methods. Specifically, in Case 1, the AFC-RL controller achieves a 99.99% improvement in root mean square error for joint 1 compared to the hybrid PID control. In Case 2, the AFC-RL controller outperforms the AFC-IL controller in trajectory tracking accuracy by 98.71%. Also, disturbance rejection ability was tested on the AFC-based controllers with various types of disturbances. Among the three AFC-based controllers, AFC-RL shows the best performance. The findings highlight the potential of integrating machine learning into AFC for more accurate and efficient robotic control.
 
## Keywords
active force control, adaptive neuro-fuzzy inference system, inertia matrix, reinforcement learning, scara
 
## Citation
- **Journal:** Neural Computing and Applications
- **Year:** 2025
- **Volume:** 37
- **Issue:** 19
- **Pages:** 13345--13370
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s00521-025-11200-x](https://doi.org/10.1007/s00521-025-11200-x)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Huang_2025,
  title={{Trajectory tracking of a SCARA robot using intelligent active force control}},
  volume={37},
  ISSN={1433-3058},
  DOI={10.1007/s00521-025-11200-x},
  number={19},
  journal={Neural Computing and Applications},
  publisher={Springer Science and Business Media LLC},
  author={Huang, Hanyi and Arogbonlo, Adetokunbo and Yu, Samson and Kwek, Lee Chung and Lim, Chee Peng},
  year={2025},
  pages={13345--13370}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/trajectory-tracking-of-a-scara-robot-using-intelligent-active-force-control.bib)
 
## References
- Gosselin, C., Isaksson, M., Marlow, K. & Laliberte, T. Workspace and Sensitivity Analysis of a Novel Nonredundant Parallel SCARA Robot Featuring Infinite Tool Rotation. IEEE Robot. Autom. Lett. 1, 776–783 (2016) -- [10.1109/lra.2016.2527064](https://doi.org/10.1109/lra.2016.2527064)
- Lapierre, M. P. & Gosselin, C. A Parallel SCARA Robot With Low-Impedance Backdrivability and a Remotely Operated Gripper With Unlimited Rotation. IEEE Robot. Autom. Lett. 9, 3980–3987 (2024) -- [10.1109/lra.2024.3374170](https://doi.org/10.1109/lra.2024.3374170)
- Jin, G., Yu, X., Chen, Y. & Li, J. SCARA+ System: Bin Picking System of Revolution-Symmetry Objects. IEEE Trans. Ind. Electron. 71, 10976–10986 (2024) -- [10.1109/tie.2023.3344841](https://doi.org/10.1109/tie.2023.3344841)
- Lu, W. et al. A New Position Detection and Status Monitoring System for Joint of SCARA. IEEE/ASME Trans. Mechatron. 26, 1613–1623 (2021) -- [10.1109/tmech.2020.3025902](https://doi.org/10.1109/tmech.2020.3025902)
- Cao, F. et al. A Novel 5-DOF welding robot based on SCARA. 2015 IEEE 10th Conference on Industrial Electronics and Applications (ICIEA) 2016–2019 (2015) doi:10.1109/iciea.2015.7334444 -- [10.1109/iciea.2015.7334444](https://doi.org/10.1109/iciea.2015.7334444)
- He, Y. et al. Dynamic Modeling, Simulation, and Experimental Verification of a Wafer Handling SCARA Robot With Decoupling Servo Control. IEEE Access 7, 47143–47153 (2019) -- [10.1109/access.2019.2909657](https://doi.org/10.1109/access.2019.2909657)
- Q Chen, IEEE Trans Instrum Meas (2024)
- Z Chen, IEEE Trans Instrum Meas (2022)
- Visioli, A. & Legnani, G. On the trajectory tracking control of industrial SCARA robot manipulators. IEEE Trans. Ind. Electron. 49, 224–232 (2002) -- [10.1109/41.982266](https://doi.org/10.1109/41.982266)
- Na, J., Jing, B., Huang, Y., Gao, G. & Zhang, C. Unknown System Dynamics Estimator for Motion Control of Nonlinear Robotic Systems. IEEE Trans. Ind. Electron. 67, 3850–3859 (2020) -- [10.1109/tie.2019.2920604](https://doi.org/10.1109/tie.2019.2920604)
- Rossomando, F. G. & Soria, C. M. Discrete-time sliding mode neuro-adaptive controller for SCARA robot arm. Neural Comput &amp; Applic 28, 3837–3850 (2016) -- [10.1007/s00521-016-2242-7](https://doi.org/10.1007/s00521-016-2242-7)
- [Chi, J., Yu, H. & Yu, J. Hybrid Tracking Control of 2-DOF SCARA Robot via Port-Controlled Hamiltonian and Backstepping. IEEE Access 6, 17354–17360 (2018)](hybrid-tracking-control-of-2-dof-scara-robot-via-port-controlled-hamiltonian-and-backstepping) -- [10.1109/access.2018.2820681](https://doi.org/10.1109/access.2018.2820681)
- Zhen, S. et al. A Novel Practical Robust Control Inheriting PID for SCARA Robot. IEEE Access 8, 227409–227419 (2020) -- [10.1109/access.2020.3045789](https://doi.org/10.1109/access.2020.3045789)
- Wang, B., Brogliato, B., Acary, V., Boubakir, A. & Plestan, F. Experimental Comparisons Between Implicit and Explicit Implementations of Discrete-Time Sliding Mode Controllers: Toward Input and Output Chattering Suppression. IEEE Trans. Contr. Syst. Technol. 23, 2071–2075 (2015) -- [10.1109/tcst.2015.2396473](https://doi.org/10.1109/tcst.2015.2396473)
- [Zhang, Q., Sun, W. & Qiao, C. Adaptive Fuzzy Control of Switched Port-Controlled Hamiltonian Systems with Input Saturation. Int. J. Fuzzy Syst. 27, 326–337 (2024)](adaptive-fuzzy-control-of-switched-port-controlled-hamiltonian-systems-with-input-saturation) -- [10.1007/s40815-024-01783-3](https://doi.org/10.1007/s40815-024-01783-3)
- Hewit, J. R. & Burdess, J. S. Fast dynamic decoupled control for robotics, using active force control. Mechanism and Machine Theory 16, 535–542 (1981) -- [10.1016/0094-114x(81)90025-2](https://doi.org/10.1016/0094-114x(81)90025-2)
- Priyandoko, G., Mailah, M. & Jamaluddin, H. Vehicle active suspension system using skyhook adaptive neuro active force control. Mechanical Systems and Signal Processing 23, 855–868 (2009) -- [10.1016/j.ymssp.2008.07.014](https://doi.org/10.1016/j.ymssp.2008.07.014)
- Noshadi, A., Mailah, M. & Zolfagharian, A. Intelligent active force control of a 3-RRR parallel manipulator incorporating fuzzy resolved acceleration control. Applied Mathematical Modelling 36, 2370–2383 (2012) -- [10.1016/j.apm.2011.08.033](https://doi.org/10.1016/j.apm.2011.08.033)
- Abdelmaksoud, S. I., Mailah, M. & Abdallah, A. M. Robust Intelligent Self-Tuning Active Force Control of a Quadrotor With Improved Body Jerk Performance. IEEE Access 8, 150037–150050 (2020) -- [10.1109/access.2020.3015101](https://doi.org/10.1109/access.2020.3015101)
- Abdelmaksoud, S. I., Mailah, M. & Abdallah, A. M. Practical Real-Time Implementation of a Disturbance Rejection Control Scheme for a Twin-Rotor Helicopter System Using Intelligent Active Force Control. IEEE Access 9, 4886–4901 (2021) -- [10.1109/access.2020.3046728](https://doi.org/10.1109/access.2020.3046728)
- Ali, M. A. H. et al. A novel inertia moment estimation algorithm collaborated with Active Force Control scheme for wheeled mobile robot control in constrained environments. Expert Systems with Applications 183, 115454 (2021) -- [10.1016/j.eswa.2021.115454](https://doi.org/10.1016/j.eswa.2021.115454)
- Kwek, L. C., Wong, E. K., Loo, C. K. & Rao, M. V. C. Application of Active Force Control and Iterative Learning in a 5-Link Biped Robot. Journal of Intelligent and Robotic Systems 37, 143–162 (2003) -- [10.1023/a:1024187206507](https://doi.org/10.1023/a:1024187206507)
- Huang, H., Arogbonlo, A., Yu, S., Chung Kwek, L. & Peng Lim, C. Adaptive neuro-fuzzy inference system based active force control with iterative learning for trajectory tracking of a biped robot. International Journal of Systems Science 56, 1171–1188 (2024) -- [10.1080/00207721.2024.2420069](https://doi.org/10.1080/00207721.2024.2420069)
- Huang, H., Arogbonlo, A., Yu, S. & Kwek, L. C. Reinforcement Learning Integrated Active Force Control for Five-link Biped Robots. 2024 IEEE International Systems Conference (SysCon) 1–6 (2024) doi:10.1109/syscon61195.2024.10553408 -- [10.1109/syscon61195.2024.10553408](https://doi.org/10.1109/syscon61195.2024.10553408)
- KWEK, L. C., LOO, C. K., WONG, E. K. & RAO, M. V. C. EVOLUTIONARY ACTIVE FORCE CONTROL OF A 5-LINK BIPED ROBOT. Computational Intelligent Systems for Applied Research 503–510 (2002) doi:10.1142/9789812777102_0061 -- [10.1142/9789812777102_0061](https://doi.org/10.1142/9789812777102_0061)
- Nazarov, N. A. & Tolcheev, V. O. Study of Web of Science Samples Using Neural Network Classifiers. Pattern Recognit. Image Anal. 34, 509–514 (2024) -- [10.1134/s1054661824700287](https://doi.org/10.1134/s1054661824700287)
- Tu, J. V. Advantages and disadvantages of using artificial neural networks versus logistic regression for predicting medical outcomes. Journal of Clinical Epidemiology 49, 1225–1231 (1996) -- [10.1016/s0895-4356(96)00002-9](https://doi.org/10.1016/s0895-4356(96)00002-9)
- Jang, J.-S. R. ANFIS: adaptive-network-based fuzzy inference system. IEEE Trans. Syst., Man, Cybern. 23, 665–685 (1993) -- [10.1109/21.256541](https://doi.org/10.1109/21.256541)
- Al-Hmouz, A., Jun Shen, Al-Hmouz, R. & Jun Yan. Modeling and Simulation of an Adaptive Neuro-Fuzzy Inference System (ANFIS) for Mobile Learning. IEEE Trans. Learning Technol. 5, 226–237 (2012) -- [10.1109/tlt.2011.36](https://doi.org/10.1109/tlt.2011.36)
- Yadav, M., Tandel, B. & Ahammed, M. M. Advanced soft computing techniques in modeling noise pollution health impacts. Current Trends and Advances in Computer-Aided Intelligent Environmental Data Engineering 337–352 (2022) doi:10.1016/b978-0-323-85597-6.00014-8 -- [10.1016/b978-0-323-85597-6.00014-8](https://doi.org/10.1016/b978-0-323-85597-6.00014-8)
- Janardhana, K. et al. ANFIS modeling of biodiesels’ physical and engine characteristics: A review. Heat Trans 50, 8052–8079 (2021) -- [10.1002/htj.22266](https://doi.org/10.1002/htj.22266)
- Liu, Y. & Zhang, Y. Iterative Local ANFIS-Based Human Welder Intelligence Modeling and Control in Pipe GTAW Process: A Data-Driven Approach. IEEE/ASME Trans. Mechatron. 20, 1079–1088 (2015) -- [10.1109/tmech.2014.2363050](https://doi.org/10.1109/tmech.2014.2363050)
- Ghose, D. K., Tanaya, K., Sahoo, A. & Kumar, U. Performance Evaluation of hybrid ANFIS model for Flood Prediction. 2022 8th International Conference on Advanced Computing and Communication Systems (ICACCS) 772–777 (2022) doi:10.1109/icaccs54159.2022.9785002 -- [10.1109/icaccs54159.2022.9785002](https://doi.org/10.1109/icaccs54159.2022.9785002)
- Khan, S. A., Equbal, Md. D. & Islam, T. A comprehensive comparative study of DGA based transformer fault diagnosis using fuzzy logic and ANFIS models. IEEE Trans. Dielect. Electr. Insul. 22, 590–596 (2015) -- [10.1109/tdei.2014.004478](https://doi.org/10.1109/tdei.2014.004478)
- Cao, H. Q., Nguyen, H. X., Nguyen, T. T., Nguyen, V. Q. & Jeon, J. W. Robot Calibration Method Based on Extended Kalman Filter–Dual Quantum Behaved Particle Swarm Optimization and Adaptive Neuro-Fuzzy Inference System. IEEE Access 9, 132558–132568 (2021) -- [10.1109/access.2021.3115120](https://doi.org/10.1109/access.2021.3115120)
- Kamil, F. & Moghrabiah, M. Y. Multilayer Decision-Based Fuzzy Logic Model to Navigate Mobile Robot in Unknown Dynamic Environments. Fuzzy Information and Engineering 14, 51–73 (2021) -- [10.1080/16168658.2021.2019432](https://doi.org/10.1080/16168658.2021.2019432)
- Juston, M. F. R., Dekhterman, S. R., Norris, W. R., Nottage, D. & Soylemezoglu, A. Hierarchical Rule-Base Reduction-Based ANFIS With Online Optimization Through DDPG. IEEE Trans. Fuzzy Syst. 32, 6350–6362 (2024) -- [10.1109/tfuzz.2024.3449147](https://doi.org/10.1109/tfuzz.2024.3449147)
- Li, T.-H. S. et al. Fuzzy Double Deep Q-Network-Based Gait Pattern Controller for Humanoid Robots. IEEE Trans. Fuzzy Syst. 30, 147–161 (2022) -- [10.1109/tfuzz.2020.3033141](https://doi.org/10.1109/tfuzz.2020.3033141)
- Mahmud, M., Kaiser, M. S., Hussain, A. & Vassanelli, S. Applications of Deep Learning and Reinforcement Learning to Biological Data. IEEE Trans. Neural Netw. Learning Syst. 29, 2063–2079 (2018) -- [10.1109/tnnls.2018.2790388](https://doi.org/10.1109/tnnls.2018.2790388)
- Kiumarsi, B., Vamvoudakis, K. G., Modares, H. & Lewis, F. L. Optimal and Autonomous Control Using Reinforcement Learning: A Survey. IEEE Trans. Neural Netw. Learning Syst. 29, 2042–2062 (2018) -- [10.1109/tnnls.2017.2773458](https://doi.org/10.1109/tnnls.2017.2773458)
- Ho, Y.-H. & Cheng, T.-C. Adaptive road shoulder traffic control with reinforcement learning approach. Neural Comput &amp; Applic 37, 24499–24515 (2023) -- [10.1007/s00521-023-09134-3](https://doi.org/10.1007/s00521-023-09134-3)
- Tzafestas, S., Raibert, M. & Tzafestas, C. Robust sliding-mode control applied to a 5-link biped robot. J Intell Robot Syst 15, 67–133 (1996) -- [10.1007/bf00435728](https://doi.org/10.1007/bf00435728)
- Evolutionary and Swarm Intelligence Algorithms. Studies in Computational Intelligence (Springer International Publishing, 2019). doi:10.1007/978-3-319-91341-4 -- [10.1007/978-3-319-91341-4](https://doi.org/10.1007/978-3-319-91341-4)
- Fang, X. & Xie, L. Distributed Formation Maneuver Control Using Complex Laplacian. IEEE Trans. Automat. Contr. 69, 1850–1857 (2024) -- [10.1109/tac.2023.3327932](https://doi.org/10.1109/tac.2023.3327932)

