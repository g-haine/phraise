---
layout: post
title: "Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control"
date: 2024-07-15 00:00:00 +0100
permalink: port-hamiltonian-neural-ode-networks-on-lie-groups-for-robot-dynamics-learning-and-control
year: 2024
authors: Thai Duong, Abdullah Altawaitan, Jason Stanley, Nikolay Atanasov
category:
  - articles
---
 
## Authors
[Thai Duong](authors/thai_duong), [Abdullah Altawaitan](authors/abdullah_altawaitan), [Jason Stanley](authors/jason_stanley), [Nikolay Atanasov](authors/nikolay_atanasov)
 
## Abstract
Accurate models of robot dynamics are critical for safe and stable control and generalization to novel operational conditions. Hand-designed models, however, may be insufficiently accurate, even after careful parameter tuning. This motivates the use of machine learning techniques to approximate the robot dynamics over a training set of state-control trajectories. The dynamics of many robots are described in terms of their generalized coordinates on a matrix Lie group, e.g., on \( \text{SE}(3) \) for ground, aerial, and underwater vehicles, and generalized velocity, and satisfy conservation of energy principles. This article proposes a port-Hamiltonian formulation over a Lie group of the structure of a neural ordinary differential equation (ODE) network to approximate the robot dynamics. In contrast to a black-box ODE network, our formulation embeds energy conservation principle and Lie group's constraints in the dynamics model and explicitly accounts for energy-dissipation effect such as friction and drag forces in the dynamics model. We develop energy shaping and damping injection control for the learned, potentially under-actuated Hamiltonian dynamics to enable a unified approach for stabilization and trajectory tracking with various robot platforms.
 
## Citation
- **Journal:** IEEE Transactions on Robotics
- **Year:** 2024
- **Volume:** 40
- **Issue:** 
- **Pages:** 3695--3715
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/TRO.2024.3428433](https://doi.org/10.1109/TRO.2024.3428433)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Duong_2024,
  title={{Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control}},
  volume={40},
  ISSN={1941-0468},
  DOI={10.1109/tro.2024.3428433},
  journal={IEEE Transactions on Robotics},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Duong, Thai and Altawaitan, Abdullah and Stanley, Jason and Atanasov, Nikolay},
  year={2024},
  pages={3695--3715}
}
{% endraw %}
{% endhighlight %}
 
## References
- Ljung, L. System Identification. Wiley Encyclopedia of Electrical and Electronics Engineering (1999) doi:10.1002/047134608x.w1046 -- [10.1002/047134608X.W1046](https://doi.org/10.1002/047134608X.W1046)
- Nguyen-Tuong, D. & Peters, J. Model learning for robot control: a survey. Cognitive Processing vol. 12 319–340 (2011) -- [10.1007/s10339-011-0404-1](https://doi.org/10.1007/s10339-011-0404-1)
- Williams, G. et al. Information theoretic MPC for model-based reinforcement learning. 2017 IEEE International Conference on Robotics and Automation (ICRA) 1714–1721 (2017) doi:10.1109/icra.2017.7989202 -- [10.1109/ICRA.2017.7989202](https://doi.org/10.1109/ICRA.2017.7989202)
- Lutter, M. & Peters, J. Combining physics and deep learning to learn continuous-time dynamics models. The International Journal of Robotics Research vol. 42 83–107 (2023) -- [10.1177/02783649231169492](https://doi.org/10.1177/02783649231169492)
- Roehrl, M. A., Runkler, T. A., Brandtstetter, V., Tokic, M. & Obermayer, S. Modeling System Dynamics with Physics-Informed Neural Networks Based on Lagrangian Mechanics. IFAC-PapersOnLine vol. 53 9195–9200 (2020) -- [10.1016/j.ifacol.2020.12.2182](https://doi.org/10.1016/j.ifacol.2020.12.2182)
- Hall, B. C. Lie Groups, Lie Algebras, and Representations. Graduate Texts in Mathematics 333–366 (2013) doi:10.1007/978-1-4614-7116-5_16 -- [10.1007/978-1-4614-7116-5_16](https://doi.org/10.1007/978-1-4614-7116-5_16)
- Lynch, K. M. & Park, F. C. Modern Robotics. (2017) doi:10.1017/9781316661239 -- [10.1017/9781316661239](https://doi.org/10.1017/9781316661239)
- Wotte, Y. P., Califano, F. & Stramigioli, S. Optimal potential shaping on SE(3) via neural ordinary differential equations on Lie groups. The International Journal of Robotics Research vol. 43 2221–2244 (2024) -- [10.1177/02783649241256044](https://doi.org/10.1177/02783649241256044)
- Lurie, A. I. Analytical Mechanics. (Springer Berlin Heidelberg, 2002). doi:10.1007/978-3-540-45677-3 -- [10.1007/978-3-540-45677-3](https://doi.org/10.1007/978-3-540-45677-3)
- Holm, D. D. Geometric Mechanics. (IMPERIAL COLLEGE PRESS, 2008). doi:10.1142/p557 -- [10.1142/p557](https://doi.org/10.1142/p557)
- Bertalan, T., Dietrich, F., Mezić, I. & Kevrekidis, I. G. On learning Hamiltonian systems from data. Chaos: An Interdisciplinary Journal of Nonlinear Science vol. 29 (2019) -- [10.1063/1.5128231](https://doi.org/10.1063/1.5128231)
- Willard, J., Jia, X., Xu, S., Steinbach, M. & Kumar, V. Integrating Scientific Knowledge with Machine Learning for Engineering and Environmental Systems. ACM Computing Surveys vol. 55 1–37 (2022) -- [10.1145/3514228](https://doi.org/10.1145/3514228)
- Maciejewski, A. J. Hamiltonian formalism for Euler parameters. Celestial Mechanics vol. 37 47–57 (1985) -- [10.1007/BF01230340](https://doi.org/10.1007/BF01230340)
- Shivarama, R. & Fahrenthold, E. P. Hamilton’s Equations With Euler Parameters for Rigid Body Dynamics Modeling. Journal of Dynamic Systems, Measurement, and Control vol. 126 124–130 (2004) -- [10.1115/1.1649977](https://doi.org/10.1115/1.1649977)
- Duong, T. & Atanasov, N. Hamiltonian-based Neural ODE Networks on the SE(3) Manifold For Dynamics Learning and Control. Robotics: Science and Systems XVII (2021) doi:10.15607/rss.2021.xvii.086 -- [10.15607/RSS.2021.XVII.086](https://doi.org/10.15607/RSS.2021.XVII.086)
- Song, Y., Romero, A., Müller, M., Koltun, V. & Scaramuzza, D. Reaching the limit in autonomous racing: Optimal control versus reinforcement learning. Science Robotics vol. 8 (2023) -- [10.1126/scirobotics.adg1462](https://doi.org/10.1126/scirobotics.adg1462)
- Salzmann, T. et al. Real-Time Neural MPC: Deep Learning Model Predictive Control for Quadrotors and Agile Robotic Platforms. IEEE Robotics and Automation Letters vol. 8 2397–2404 (2023) -- [10.1109/LRA.2023.3246839](https://doi.org/10.1109/LRA.2023.3246839)
- Scaramuzza, D. & Kaufmann, E. Learning Agile, Vision-Based Drone Flight: From Simulation to Reality. Springer Proceedings in Advanced Robotics 11–18 (2023) doi:10.1007/978-3-031-25555-7_2 -- [10.1007/978-3-031-25555-7_2](https://doi.org/10.1007/978-3-031-25555-7_2)
- Loquercio, A. et al. Learning high-speed flight in the wild. Science Robotics vol. 6 (2021) -- [10.1126/scirobotics.abg5810](https://doi.org/10.1126/scirobotics.abg5810)
- Ibarz, J. et al. How to train your robot with deep reinforcement learning: lessons we have learned. The International Journal of Robotics Research vol. 40 698–721 (2021) -- [10.1177/0278364920987859](https://doi.org/10.1177/0278364920987859)
- Nghiem, T. X. et al. Physics-Informed Machine Learning for Modeling and Control of Dynamical Systems. 2023 American Control Conference (ACC) 3735–3750 (2023) doi:10.23919/acc55779.2023.10155901 -- [10.23919/ACC55779.2023.10155901](https://doi.org/10.23919/ACC55779.2023.10155901)
- Thorpe, A. J., Neary, C., Djeumou, F., K. Oishi, M. M. & Topcu, U. Physics-Informed Kernel Embeddings: Integrating Prior System Knowledge with Data-Driven Control. 2024 American Control Conference (ACC) 3130–3137 (2024) doi:10.23919/acc60939.2024.10644707 -- [10.23919/ACC60939.2024.10644707](https://doi.org/10.23919/ACC60939.2024.10644707)
- Ruthotto, L. & Haber, E. Deep Neural Networks Motivated by Partial Differential Equations. Journal of Mathematical Imaging and Vision vol. 62 352–364 (2019) -- [10.1007/s10851-019-00903-1](https://doi.org/10.1007/s10851-019-00903-1)
- Lutter, M., Listmann, K. & Peters, J. Deep Lagrangian Networks for end-to-end learning of energy-based control for under-actuated systems. 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 7718–7725 (2019) doi:10.1109/iros40897.2019.8968268 -- [10.1109/IROS40897.2019.8968268](https://doi.org/10.1109/IROS40897.2019.8968268)
- [Beckers, T., Seidman, J., Perdikaris, P. & Pappas, G. J. Gaussian Process Port-Hamiltonian Systems: Bayesian Learning with Physics Prior. 2022 IEEE 61st Conference on Decision and Control (CDC) 1447–1453 (2022) doi:10.1109/cdc51059.2022.9992733](gaussian-process-port-hamiltonian-systems-bayesian-learning-with-physics-prior) -- [10.1109/CDC51059.2022.9992733](https://doi.org/10.1109/CDC51059.2022.9992733)
- Beckers, T. Data-Driven Bayesian Control of Port-Hamiltonian Systems. 2023 62nd IEEE Conference on Decision and Control (CDC) (2023) doi:10.1109/cdc49753.2023.10384219 -- [10.1109/CDC49753.2023.10384219](https://doi.org/10.1109/CDC49753.2023.10384219)
- Leimkuhler, B. & Reich, S. Simulating Hamiltonian Dynamics. (2005) doi:10.1017/cbo9780511614118 -- [10.1017/cbo9780511614118](https://doi.org/10.1017/cbo9780511614118)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Marsden, J. E. & West, M. Discrete mechanics and variational integrators. Acta Numerica vol. 10 357–514 (2001) -- [10.1017/S096249290100006X](https://doi.org/10.1017/S096249290100006X)
- Borrelli, F., Bemporad, A. & Morari, M. Predictive Control for Linear and Hybrid Systems. (2017) doi:10.1017/9781139061759 -- [10.1017/9781139061759](https://doi.org/10.1017/9781139061759)
- Ortega, R., Spong, M. W., Gomez-Estern, F. & Blankenstein, G. Stabilization of a class of underactuated mechanical systems via interconnection and damping assignment. IEEE Transactions on Automatic Control vol. 47 1218–1233 (2002) -- [10.1109/TAC.2002.800770](https://doi.org/10.1109/TAC.2002.800770)
- Acosta, J. A., Sanchez, M. I. & Ollero, A. Robust control of underactuated Aerial Manipulators via IDA-PBC. 53rd IEEE Conference on Decision and Control 673–678 (2014) doi:10.1109/cdc.2014.7039459 -- [10.1109/CDC.2014.7039459](https://doi.org/10.1109/CDC.2014.7039459)
- Cieza, O. B. & Reger, J. IDA-PBC for Underactuated Mechanical Systems in Implicit Port-Hamiltonian Representation. 2019 18th European Control Conference (ECC) (2019) doi:10.23919/ecc.2019.8795994 -- [10.23919/ECC.2019.8795994](https://doi.org/10.23919/ECC.2019.8795994)
- Wang, Z. & Goldsmith, P. Modified energy-balancing-based control for the tracking problem. IET Control Theory &amp; Applications vol. 2 310–322 (2008) -- [10.1049/iet-cta:20070124](https://doi.org/10.1049/iet-cta:20070124)
- Souza, C., Raffo, G. V. & Castelan, E. B. Passivity Based Control of a Quadrotor UAV. IFAC Proceedings Volumes vol. 47 3196–3201 (2014) -- [10.3182/20140824-6-ZA-1003.02335](https://doi.org/10.3182/20140824-6-ZA-1003.02335)
- Galimberti, C. L., Furieri, L., Xu, L. & Ferrari-Trecate, G. Hamiltonian Deep Neural Networks Guaranteeing Nonvanishing Gradients by Design. IEEE Transactions on Automatic Control vol. 68 3155–3162 (2023) -- [10.1109/TAC.2023.3239430](https://doi.org/10.1109/TAC.2023.3239430)
- Sebastián, E., Duong, T., Atanasov, N., Montijano, E. & Sagüés, C. LEMURS: Learning Distributed Multi-Robot Interactions. 2023 IEEE International Conference on Robotics and Automation (ICRA) 7713–7719 (2023) doi:10.1109/icra48891.2023.10161328 -- [10.1109/ICRA48891.2023.10161328](https://doi.org/10.1109/ICRA48891.2023.10161328)
- Marsden, J. E. & Ratiu, T. S. Introduction to Mechanics and Symmetry. Texts in Applied Mathematics (Springer New York, 1994). doi:10.1007/978-1-4612-2682-6 -- [10.1007/978-1-4612-2682-6](https://doi.org/10.1007/978-1-4612-2682-6)
- Zhou, Y., Barnes, C., Lu, J., Yang, J. & Li, H. On the Continuity of Rotation Representations in Neural Networks. 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 5738–5746 (2019) doi:10.1109/cvpr.2019.00589 -- [10.1109/CVPR.2019.00589](https://doi.org/10.1109/CVPR.2019.00589)
- Barfoot, T. D. State Estimation for Robotics. (2017) doi:10.1017/9781316671528 -- [10.1017/9781316671528](https://doi.org/10.1017/9781316671528)
- Hemingway, E. G. & O’Reilly, O. M. Perspectives on Euler angle singularities, gimbal lock, and the orthogonality of applied forces and applied moments. Multibody System Dynamics vol. 44 31–56 (2018) -- [10.1007/s11044-018-9620-0](https://doi.org/10.1007/s11044-018-9620-0)
- Faessler, M., Franchi, A. & Scaramuzza, D. Differential Flatness of Quadrotor Dynamics Subject to Rotor Drag for Accurate Tracking of High-Speed Trajectories. IEEE Robotics and Automation Letters vol. 3 620–626 (2018) -- [10.1109/LRA.2017.2776353](https://doi.org/10.1109/LRA.2017.2776353)
- [Forni, P., Jeltsema, D. & Lopes, G. A. D. Port-Hamiltonian Formulation of Rigid-Body Attitude Control. IFAC-PapersOnLine vol. 48 164–169 (2015)](port-hamiltonian-formulation-of-rigid-body-attitude-control) -- [10.1016/j.ifacol.2015.10.233](https://doi.org/10.1016/j.ifacol.2015.10.233)
- [Rashad, R., Califano, F. & Stramigioli, S. Port-Hamiltonian Passivity-Based Control on SE(3) of a Fully Actuated UAV for Aerial Physical Interaction Near-Hovering. IEEE Robotics and Automation Letters vol. 4 4378–4385 (2019)](port-hamiltonian-passivity-based-control-on-se-3-of-a-fully-actuated-uav-for-aerial-physical-interaction-near-hovering) -- [10.1109/LRA.2019.2932864](https://doi.org/10.1109/LRA.2019.2932864)
- Delmerico, J. & Scaramuzza, D. A Benchmark Comparison of Monocular Visual-Inertial Odometry Algorithms for Flying Robots. 2018 IEEE International Conference on Robotics and Automation (ICRA) 2502–2509 (2018) doi:10.1109/icra.2018.8460664 -- [10.1109/ICRA.2018.8460664](https://doi.org/10.1109/ICRA.2018.8460664)
- Mohamed, S. A. S. et al. A Survey on Odometry for Autonomous Navigation Systems. IEEE Access vol. 7 97466–97486 (2019) -- [10.1109/ACCESS.2019.2929133](https://doi.org/10.1109/ACCESS.2019.2929133)
- Dormand, J. R. & Prince, P. J. A family of embedded Runge-Kutta formulae. Journal of Computational and Applied Mathematics vol. 6 19–26 (1980) -- [10.1016/0771-050X(80)90013-3](https://doi.org/10.1016/0771-050X(80)90013-3)
- Iserles, A., Munthe-Kaas, H. Z., Nørsett, S. P. & Zanna, A. Lie-group methods. Acta Numerica vol. 9 215–365 (2000) -- [10.1017/S0962492900002154](https://doi.org/10.1017/S0962492900002154)
- Lee, T., Leok, M. & McClamroch, N. H. Geometric tracking control of a quadrotor UAV on SE(3). 49th IEEE Conference on Decision and Control (CDC) 5420–5425 (2010) doi:10.1109/cdc.2010.5717652 -- [10.1109/CDC.2010.5717652](https://doi.org/10.1109/CDC.2010.5717652)
- Meier, L., Honegger, D. & Pollefeys, M. PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms. 2015 IEEE International Conference on Robotics and Automation (ICRA) 6235–6240 (2015) doi:10.1109/icra.2015.7140074 -- [10.1109/ICRA.2015.7140074](https://doi.org/10.1109/ICRA.2015.7140074)
- Boumal, N. An Introduction to Optimization on Smooth Manifolds. (2023) doi:10.1017/9781009166164 -- [10.1017/9781009166164](https://doi.org/10.1017/9781009166164)

