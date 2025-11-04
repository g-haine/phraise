---
title: "Modeling and Control of PRP-Gantry Crane Systems via Neural IDA-PBC"
date: 2025-05-05 00:00:00 +0100
permalink: modeling-and-control-of-prp-gantry-crane-systems-via-neural-ida-pbc
year: 2025
authors: Steven Bandong, Bayu Jayawardhana, Santiago Sanchez-Escalonilla Plaza, Yul Yunazwin Nazaruddin, Endra Joelianto
category: articles
---
 
## Authors
[Steven Bandong](authors/steven-bandong), [Bayu Jayawardhana](authors/bayu-jayawardhana), [Santiago Sanchez-Escalonilla Plaza](authors/santiago-sanchez-escalonilla-plaza), [Yul Yunazwin Nazaruddin](authors/yul-yunazwin-nazaruddin), [Endra Joelianto](authors/endra-joelianto)
 
## Abstract
In this paper, we present a novel underactuated gantry crane (GC) systems where an extra degree-of-freedom actuation is introduced to control the trolley position and its sway angle during motion. The proposed gantry crane systems resembles a prismatic-revolute-prismatic (PRP) robotic configuration where the revolute joint corresponds to the sway angle which is not actuated. Firstly, an energy-based modeling of the PRP-GC systems is presented where both Euler-Lagrange and port-controlled Hamiltonian formalisms are used. Secondly, we present the design of a Neural Interconnection and Damping Assignment Passivity-Based Controller (N-IDA-PBC) that allows for an automated learning of an IDA-PBC controller, where the solutions to the corresponding IDA-PBC matching PDE are not trivial for underactuated systems. Finally, the efficacy of the proposed N-IDA-PBC is evaluated through Monte Carlo simulations, where the neural networks training of N-IDA-PBC uses \\( 3,000 \\) randomly generated data points and \\( 20,000 \\) samples of Monte-Carlo simulation are performed, taking into account uncertainties in the systems’ parameters, including initial states, physical damping, and payload masses. The Monte-Carlo simulations show that the trained N-IDA-PBC is able to regulate the trolley position and sway angle to the set-point position and it is robust against parameter uncertainties.
 
## Citation
- **Journal:** IEEE Transactions on Intelligent Transportation Systems
- **Year:** 2025
- **Volume:** 26
- **Issue:** 8
- **Pages:** 11754--11766
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tits.2025.3563314](https://doi.org/10.1109/tits.2025.3563314)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Bandong_2025,
  title={{Modeling and Control of PRP-Gantry Crane Systems via Neural IDA-PBC}},
  volume={26},
  ISSN={1558-0016},
  DOI={10.1109/tits.2025.3563314},
  number={8},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Bandong, Steven and Jayawardhana, Bayu and Sanchez-Escalonilla Plaza, Santiago and Yunazwin Nazaruddin, Yul and Joelianto, Endra},
  year={2025},
  pages={11754--11766}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/modeling-and-control-of-prp-gantry-crane-systems-via-neural-ida-pbc.bib)
 
## References
- Group, Container Port Traffic (Teu: 20-Foot Equivalent Units) (2023)
- Sánchez, R. J. et al. Port Efficiency and International Trade: Port Efficiency as a Determinant of Maritime Transport Costs. Marit Econ Logist 5, 199–218 (2003) -- [10.1057/palgrave.mel.9100073](https://doi.org/10.1057/palgrave.mel.9100073)
- Pratama, G. A., Sunaryo & Ardiani, G. A. SAFETY MANAGEMENT ON LOADING PROCESS WITH RUBBER TYRED GANTRY CRANE: CASE STUDY AT PORT OF TANJUNG PRIOK. RJOAS 66, 150–164 (2017) -- [10.18551/rjoas.2017-06.18](https://doi.org/10.18551/rjoas.2017-06.18)
- Fadda, P. et al. Multidisciplinary Study of Biological Parameters and Fatigue Evolution in Quay Crane Operators. Procedia Manufacturing 3, 3301–3308 (2015) -- [10.1016/j.promfg.2015.07.410](https://doi.org/10.1016/j.promfg.2015.07.410)
- Budiyanto, M. A. & Fernanda, H. Risk Assessment of Work Accident in Container Terminals Using the Fault Tree Analysis Method. JMSE 8, 466 (2020) -- [10.3390/jmse8060466](https://doi.org/10.3390/jmse8060466)
- Fancello, Processing and analysis of ship-to-shore gantry crane operator performance curves in container terminals. J. Maritime Res. (2008)
- Sawodny, O., Aschemann, H. & Lahres, S. An automated gantry crane as a large workspace robot. Control Engineering Practice 10, 1323–1338 (2002) -- [10.1016/s0967-0661(02)00097-7](https://doi.org/10.1016/s0967-0661(02)00097-7)
- Guo, P., Wang, L., Xue, C. & Wang, Y. Dispatching Rules for Scheduling Twin Automated Gantry Cranes in an Automated Railroad Container Terminal. Arab J Sci Eng 45, 2205–2217 (2019) -- [10.1007/s13369-019-04176-z](https://doi.org/10.1007/s13369-019-04176-z)
- Kim, N., Jung, M., Yoon, I., Park, M. & Ahn, C. R. Reinforcement Learning-Based Transportation and Sway Suppression Methods for Gantry Cranes in Simulated Environment. 2022 Winter Simulation Conference (WSC) 2377–2385 (2022) doi:10.1109/wsc57314.2022.10015415 -- [10.1109/wsc57314.2022.10015415](https://doi.org/10.1109/wsc57314.2022.10015415)
- Kemme, N. State-of-the-Art Yard Crane Scheduling and Stacking. Operations Research/Computer Science Interfaces Series 383–413 (2020) doi:10.1007/978-3-030-39990-0_17 -- [10.1007/978-3-030-39990-0_17](https://doi.org/10.1007/978-3-030-39990-0_17)
- Xin, J., Meng, C., D’Ariano, A., Wang, D. & Negenborn, R. R. Mixed-Integer Nonlinear Programming for Energy-Efficient Container Handling: Formulation and Customized Genetic Algorithm. IEEE Trans. Intell. Transport. Syst. 23, 10542–10555 (2022) -- [10.1109/tits.2021.3094815](https://doi.org/10.1109/tits.2021.3094815)
- Liu, Z., Sun, N., Yang, T. & Fang, Y. Optimal Collaborative Motion Planning of Dual Boom Cranes for Transporting Payloads to Desired Positions and Attitudes. IEEE Trans. Intell. Transport. Syst. 24, 6096–6110 (2023) -- [10.1109/tits.2023.3259003](https://doi.org/10.1109/tits.2023.3259003)
- Kim, Anti-sway control of container cranes: Inclinometer, observer, and state feedback. Int. J. Control, Autom., Syst. (2004)
- Solihin, M. I., Wahyudi & Legowo, A. Fuzzy-tuned PID Anti-swing Control of Automatic Gantry Crane. Journal of Vibration and Control 16, 127–145 (2009) -- [10.1177/1077546309103421](https://doi.org/10.1177/1077546309103421)
- Hussien, The effects of auto-tuned method in PID and PD control scheme for gantry crane system. Int. J. Soft Comput. Eng. (2015)
- Almutairi, N. B. & Zribi, M. Fuzzy Controllers for a Gantry Crane System with Experimental Verifications. Mathematical Problems in Engineering 2016, 1–17 (2016) -- [10.1155/2016/1965923](https://doi.org/10.1155/2016/1965923)
- Bandong, S., Kirana, R. C., Nazaruddin, Y. Y. & Joelianto, E. Optimal Gantry Crane PID Controller Based on LQR With Prescribed Degree of Stability by Means of GA, PSO, and SA. 2022 7th International Conference on Electric Vehicular Technology (ICEVT) 46–51 (2022) doi:10.1109/icevt55516.2022.9925018 -- [10.1109/icevt55516.2022.9925018](https://doi.org/10.1109/icevt55516.2022.9925018)
- Bandong, S., Nazaruddin, Y. Y. & Joelianto, E. Optimal RTGC Controller using Robust PID H∞ Integral-Backstepping under Payload Mass and Rope Length Uncertainties. 2022 17th International Conference on Control, Automation, Robotics and Vision (ICARCV) 18–23 (2022) doi:10.1109/icarcv57592.2022.10004328 -- [10.1109/icarcv57592.2022.10004328](https://doi.org/10.1109/icarcv57592.2022.10004328)
- Huang, X., Wu, W., Yan, W., Lou, X. & Ni, H. RETRACTED ARTICLE: Sliding-mode control of gantry crane system with recursive least square parameters identification. J Ambient Intell Human Comput 15, 181–181 (2021) -- [10.1007/s12652-021-03010-5](https://doi.org/10.1007/s12652-021-03010-5)
- Fang, Y., Dixon, W. E., Dawson, D. M. & Zergeroglu, E. Nonlinear coupling control laws for an underactuated overhead crane system. IEEE/ASME Trans. Mechatron. 8, 418–423 (2003) -- [10.1109/tmech.2003.816822](https://doi.org/10.1109/tmech.2003.816822)
- Dankadai, N. K., Mohd Faudzi, A. A., Bature, A., Babani, S. & Faruk, M. I. Position Control of a 2D Nonlinear Gantry Crane System Using Model Predictive Controller. AMM 735, 282–288 (2015) -- [10.4028/www.scientific.net/amm.735.282](https://doi.org/10.4028/www.scientific.net/amm.735.282)
- Man, Y. & Liu, Y. Positioning and antiswing control of overhead crane systems: A supervisory scheme. Journal of the Franklin Institute 360, 14329–14343 (2023) -- [10.1016/j.jfranklin.2023.10.038](https://doi.org/10.1016/j.jfranklin.2023.10.038)
- Zhang, J., Zhao, C. & Ding, J. Deep reinforcement learning with domain randomization for overhead crane control with payload mass variations. Control Engineering Practice 141, 105689 (2023) -- [10.1016/j.conengprac.2023.105689](https://doi.org/10.1016/j.conengprac.2023.105689)
- Ma, L., Lou, X. & Jia, J. Neural-network-based boundary control for a gantry crane system with unknown friction and output constraint. Neurocomputing 518, 271–281 (2023) -- [10.1016/j.neucom.2022.11.010](https://doi.org/10.1016/j.neucom.2022.11.010)
- Otto, E., Maksakov, A., Golovin, I. & Palis, S. Neural network based adaptive control of gantry cranes. IFAC-PapersOnLine 56, 8091–8096 (2023) -- [10.1016/j.ifacol.2023.10.963](https://doi.org/10.1016/j.ifacol.2023.10.963)
- Plaza, Total energy shaping with neural interconnection and damping assignment-passivity based control. Proc. Learn. Dyn. Control Conf.
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Guerrero-Sanchez, M.-E. et al. Filtered Observer-Based IDA-PBC Control for Trajectory Tracking of a Quadrotor. IEEE Access 9, 114821–114835 (2021) -- [10.1109/access.2021.3104798](https://doi.org/10.1109/access.2021.3104798)
- Jeung, Y.-C., Lee, D.-C., Dragicevic, T. & Blaabjerg, F. Design of Passivity-Based Damping Controller for Suppressing Power Oscillations in DC Microgrids. IEEE Trans. Power Electron. 36, 4016–4028 (2021) -- [10.1109/tpel.2020.3024716](https://doi.org/10.1109/tpel.2020.3024716)
- Hichem, H., Abdellah, M., Abderrazak, T. A., Abdelkader, B. & Ramzi, S. A wind turbine sensorless automatic control systems, analysis, modelling and development of IDA-PBC method. IJPEDS 11, 45 (2020) -- [10.11591/ijpeds.v11.i1.pp45-55](https://doi.org/10.11591/ijpeds.v11.i1.pp45-55)
- Lv, C., Yu, H., Chen, J., Zhao, N. & Chi, J. Trajectory tracking control for unmanned surface vessel with input saturation and disturbances via robust state error IDA-PBC approach. Journal of the Franklin Institute 359, 1899–1924 (2022) -- [10.1016/j.jfranklin.2022.01.036](https://doi.org/10.1016/j.jfranklin.2022.01.036)
- Lapique, M. et al. Enhanced IDA-PBC Applied to a Three-Phase PWM Rectifier for Stable Interfacing Between AC and DC Microgrids Embedded in More Electrical Aircraft. IEEE Trans. Ind. Electron. 70, 995–1004 (2023) -- [10.1109/tie.2022.3150079](https://doi.org/10.1109/tie.2022.3150079)
- Gandarilla, I., Santibáñez, V., Sandoval, J. & Campa, R. Joint position regulation of a class of underactuated mechanical systems affected by LuGre dynamic friction via the IDA-PBC method. International Journal of Control 95, 1419–1431 (2020) -- [10.1080/00207179.2020.1857440](https://doi.org/10.1080/00207179.2020.1857440)
- [Romdlony, M. Z. & Jayawardhana, B. Passivity-Based Control with Guaranteed Safety via Interconnection and Damping Assignment. IFAC-PapersOnLine 48, 74–79 (2015)](passivity-based-control-with-guaranteed-safety-via-interconnection-and-damping-assignment) -- [10.1016/j.ifacol.2015.11.155](https://doi.org/10.1016/j.ifacol.2015.11.155)
- Sanchez-Escalonilla, S., Reyes-Baez, R. & Jayawardhana, B. Stabilization of Underactuated Systems of Degree One via Neural Interconnection and Damping Assignment – Passivity Based Control. 2022 IEEE 61st Conference on Decision and Control (CDC) 2463–2468 (2022) doi:10.1109/cdc51059.2022.9993241 -- [10.1109/cdc51059.2022.9993241](https://doi.org/10.1109/cdc51059.2022.9993241)
- Franco, E. & Borja, P. Integral IDA-PBC of Underactuated Mechanical Systems with Actuator Dynamics and Uncertain Coupling. IFAC-PapersOnLine 58, 19–24 (2024) -- [10.1016/j.ifacol.2024.08.250](https://doi.org/10.1016/j.ifacol.2024.08.250)
- [Franco, E. Integral passivity‐based control of underactuated mechanical systems with actuator dynamics and constant disturbances. Intl J Robust &amp; Nonlinear 33, 10024–10045 (2023)](integral-passivity-based-control-of-underactuated-mechanical-systems-with-actuator-dynamics-and-constant-disturbances) -- [10.1002/rnc.6885](https://doi.org/10.1002/rnc.6885)
- Harandi, M. R. J. & Taghirad, H. D. On the matching equations of kinetic energy shaping in IDA-PBC. Journal of the Franklin Institute 358, 8639–8655 (2021) -- [10.1016/j.jfranklin.2021.08.034](https://doi.org/10.1016/j.jfranklin.2021.08.034)
- Jensen, P. S. Finite difference techniques for variable grids. Computers &amp; Structures 2, 17–29 (1972) -- [10.1016/0045-7949(72)90020-x](https://doi.org/10.1016/0045-7949(72)90020-x)
- Taylor, C. & Hood, P. A numerical solution of the Navier-Stokes equations using the finite element technique. Computers &amp; Fluids 1, 73–100 (1973) -- [10.1016/0045-7930(73)90027-3](https://doi.org/10.1016/0045-7930(73)90027-3)
- Eymard, R., Gallouët, T. & Herbin, R. Finite volume methods. Handbook of Numerical Analysis 713–1018 (2000) doi:10.1016/s1570-8659(00)07005-8 -- [10.1016/s1570-8659(00)07005-8](https://doi.org/10.1016/s1570-8659(00)07005-8)
- Raissi, M., Perdikaris, P. & Karniadakis, G. E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378, 686–707 (2019) -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Nicodemus, J., Kneifl, J., Fehr, J. & Unger, B. Physics-informed Neural Networks-based Model Predictive Control for Multi-link Manipulators. IFAC-PapersOnLine 55, 331–336 (2022) -- [10.1016/j.ifacol.2022.09.117](https://doi.org/10.1016/j.ifacol.2022.09.117)
- Ramesan Santhi, L. & Beebi M, L. Position Control and Anti-Swing Control of Overhead Crane Using LQR. IJSER 3, 26–30 (2015) -- [10.70729/ijser15384](https://doi.org/10.70729/ijser15384)
- Omar, H. M. & Nayfeh, A. H. A Simple Adaptive Feedback Controller for Tower Cranes. Volume 6C: 18th Biennial Conference on Mechanical Vibration and Noise 2611–2621 (2001) doi:10.1115/detc2001/vib-21606 -- [10.1115/detc2001/vib-21606](https://doi.org/10.1115/detc2001/vib-21606)
- Vlada, Consideration of various moving loads models in structural dynamics of large gantry cranes. Faculty Mech. Eng. (2013)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. FnT in Systems and Control 1, 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Wang, H., Liu, Y. & Wang, S. Dense velocity reconstruction from particle image velocimetry/particle tracking velocimetry using a physics-informed neural network. Physics of Fluids 34, (2022) -- [10.1063/5.0078143](https://doi.org/10.1063/5.0078143)
- Sanchez-Escalonilla, Robust neural IDA-PBC: Passivity-based stabilization under approximations. arXiv:2409.16008 (2024)

