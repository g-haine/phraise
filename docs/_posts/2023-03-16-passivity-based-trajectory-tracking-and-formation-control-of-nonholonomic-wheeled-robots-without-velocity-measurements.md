---
title: "Passivity-Based Trajectory Tracking and Formation Control of Nonholonomic Wheeled Robots Without Velocity Measurements"
date: 2023-03-16 00:00:00 +0100
permalink: passivity-based-trajectory-tracking-and-formation-control-of-nonholonomic-wheeled-robots-without-velocity-measurements
year: 2023
authors: Ningbo Li, Pablo Borja, Jacquelien M. A. Scherpen, Arjan van der Schaft, Robert Mahony
category: articles
---
 
## Authors
[Ningbo Li](authors/ningbo-li), [Pablo Borja](authors/luis-pablo-borja), [Jacquelien M. A. Scherpen](authors/jacquelien-m-a-scherpen), [Arjan van der Schaft](authors/arjan-van-der-schaft), [Robert Mahony](authors/robert-mahony)
 
## Abstract
This note proposes a passivity-based control method for trajectory tracking and formation control of nonholonomic wheeled robots without velocity measurements. Coordinate transformations are used to incorporate the nonholonomic constraints, which are then avoided by controlling the front end of the robot rather than the center of the wheel axle into the differential equations. Starting from the passivity-based coordination design, the control goals are achieved via an internal controller for velocity tracking and heading control, and an external controller for formation in the port-Hamiltonian framework. This approach endows the resulting controller with a physical interpretation. To avoid unavailable velocity measurements or unreliable velocity estimations, we derive the distributed control law with only position measurements by introducing a dynamic extension. In addition, we prove that our approach is suitable not only for acyclic graphs but also for a class of nonacyclic graphs, namely, ring graphs. Simulations are provided to illustrate the effectiveness of the approach.
 
## Citation
- **Journal:** IEEE Transactions on Automatic Control
- **Year:** 2023
- **Volume:** 68
- **Issue:** 12
- **Pages:** 7951--7957
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tac.2023.3258320](https://doi.org/10.1109/tac.2023.3258320)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Li_2023,
  title={{Passivity-Based Trajectory Tracking and Formation Control of Nonholonomic Wheeled Robots Without Velocity Measurements}},
  volume={68},
  ISSN={2334-3303},
  DOI={10.1109/tac.2023.3258320},
  number={12},
  journal={IEEE Transactions on Automatic Control},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Li, Ningbo and Borja, Pablo and Scherpen, Jacquelien M. A. and van der Schaft, Arjan and Mahony, Robert},
  year={2023},
  pages={7951--7957}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/passivity-based-trajectory-tracking-and-formation-control-of-nonholonomic-wheeled-robots-without-velocity-measurements.bib)
 
## References
- Beard, R. W., Lawton, J. & Hadaegh, F. Y. A coordination architecture for spacecraft formation control. IEEE Transactions on Control Systems Technology vol. 9 777–790 (2001) -- [10.1109/87.960341](https://doi.org/10.1109/87.960341)
- Ren, W. & Beard, R. W. Distributed Consensus in Multi-Vehicle Cooperative Control. Communications and Control Engineering (Springer London, 2008). doi:10.1007/978-1-84800-015-5 -- [10.1007/978-1-84800-015-5](https://doi.org/10.1007/978-1-84800-015-5)
- Oh, K.-K., Park, M.-C. & Ahn, H.-S. A survey of multi-agent formation control. Automatica vol. 53 424–440 (2015) -- [10.1016/j.automatica.2014.10.022](https://doi.org/10.1016/j.automatica.2014.10.022)
- Antonelli, G., Arrichiello, F., Caccavale, F. & Marino, A. Decentralized time-varying formation control for multi-robot systems. The International Journal of Robotics Research vol. 33 1029–1043 (2014) -- [10.1177/0278364913519149](https://doi.org/10.1177/0278364913519149)
- Wang, R. Adaptive output-feedback time-varying formation tracking control for multi-agent systems with switching directed networks. Journal of the Franklin Institute vol. 357 551–568 (2020) -- [10.1016/j.jfranklin.2019.11.077](https://doi.org/10.1016/j.jfranklin.2019.11.077)
- Zhao, S., Li, Z. & Ding, Z. Bearing-Only Formation Tracking Control of Multiagent Systems. IEEE Transactions on Automatic Control vol. 64 4541–4554 (2019) -- [10.1109/tac.2019.2903290](https://doi.org/10.1109/tac.2019.2903290)
- Hernandez, T., Loria, A., Nuno, E. & Panteley, E. Consensus-based formation control of nonholonomic robots without velocity measurements. 2020 European Control Conference (ECC) 674–679 (2020) doi:10.23919/ecc51009.2020.9143841 -- [10.23919/ecc51009.2020.9143841](https://doi.org/10.23919/ecc51009.2020.9143841)
- Nuño, E., Loría, A., Hernández, T., Maghenem, M. & Panteley, E. Distributed consensus-formation of force-controlled nonholonomic robots with time-varying delays. Automatica vol. 120 109114 (2020) -- [10.1016/j.automatica.2020.109114](https://doi.org/10.1016/j.automatica.2020.109114)
- Maghenem, M. A., Loria, A. & Panteley, E. Cascades-Based Leader–Follower Formation Tracking and Stabilization of Multiple Nonholonomic Vehicles. IEEE Transactions on Automatic Control vol. 65 3639–3646 (2020) -- [10.1109/tac.2019.2952559](https://doi.org/10.1109/tac.2019.2952559)
- Roza, A., Maggiore, M. & Scardovi, L. A Smooth Distributed Feedback for Formation Control of Unicycles. IEEE Transactions on Automatic Control vol. 64 4998–5011 (2019) -- [10.1109/tac.2019.2904152](https://doi.org/10.1109/tac.2019.2904152)
- Dai, S.-L., He, S., Chen, X. & Jin, X. Adaptive Leader–Follower Formation Control of Nonholonomic Mobile Robots With Prescribed Transient and Steady-State Performance. IEEE Transactions on Industrial Informatics vol. 16 3662–3671 (2020) -- [10.1109/tii.2019.2939263](https://doi.org/10.1109/tii.2019.2939263)
- Poonawala, H. A., Satici, A. C. & Spong, M. W. Leader-follower formation control of nonholonomic wheeled mobile robots using only position measurements. 2013 9th Asian Control Conference (ASCC) 1–6 (2013) doi:10.1109/ascc.2013.6606313 -- [10.1109/ascc.2013.6606313](https://doi.org/10.1109/ascc.2013.6606313)
- Cheng, Y., Jia, R., Du, H., Wen, G. & Zhu, W. Robust finite‐time consensus formation control for multiple nonholonomic wheeled mobile robots via output feedback. International Journal of Robust and Nonlinear Control vol. 28 2082–2096 (2017) -- [10.1002/rnc.4002](https://doi.org/10.1002/rnc.4002)
- Yang, J., Xiao, F. & Chen, T. Event-triggered formation tracking control of nonholonomic mobile robots without velocity measurements. Automatica vol. 112 108671 (2020) -- [10.1016/j.automatica.2019.108671](https://doi.org/10.1016/j.automatica.2019.108671)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM Journal on Control and Optimization vol. 51 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Brockett, Asymptotic stability and feedback stabilization. Differ. Geometric Control Theory (1983)
- Lee, D. & Lui, K. Y. Passive Configuration Decomposition and Passivity-Based Control of Nonholonomic Mechanical Systems. IEEE Transactions on Robotics vol. 33 281–297 (2017) -- [10.1109/tro.2016.2629492](https://doi.org/10.1109/tro.2016.2629492)
- Samson, C. Time-varying Feedback Stabilization of Car-like Wheeled Mobile Robots. The International Journal of Robotics Research vol. 12 55–64 (1993) -- [10.1177/027836499301200104](https://doi.org/10.1177/027836499301200104)
- Van Der Schaft, A. J. & Maschke, B. M. On the Hamiltonian formulation of nonholonomic mechanical systems. Reports on Mathematical Physics vol. 34 225–233 (1994) -- [10.1016/0034-4877(94)90038-8](https://doi.org/10.1016/0034-4877(94)90038-8)
- Arcak, M. Passivity as a Design Tool for Group Coordination. IEEE Transactions on Automatic Control vol. 52 1380–1390 (2007) -- [10.1109/tac.2007.902733](https://doi.org/10.1109/tac.2007.902733)
- [Vos, E., van der Schaft, A. J. & Scherpen, J. M. A. Formation Control and Velocity Tracking for a Group of Nonholonomic Wheeled Robots. IEEE Transactions on Automatic Control vol. 61 2702–2707 (2016)](formation-control-and-velocity-tracking-for-a-group-of-nonholonomic-wheeled-robots) -- [10.1109/tac.2015.2504547](https://doi.org/10.1109/tac.2015.2504547)
- Panteley, E., Loria, A. & Teel, A. Relaxed persistency of excitation for uniform asymptotic stability. IEEE Transactions on Automatic Control vol. 46 1874–1886 (2001) -- [10.1109/9.975471](https://doi.org/10.1109/9.975471)
- [Dirksz, D. A. & Scherpen, J. M. A. On Tracking Control of Rigid-Joint Robots With Only Position Measurements. IEEE Transactions on Control Systems Technology vol. 21 1510–1513 (2013)](on-tracking-control-of-rigid-joint-robots-with-only-position-measurements) -- [10.1109/tcst.2012.2204886](https://doi.org/10.1109/tcst.2012.2204886)
- Loria, A. Observers are Unnecessary for Output-Feedback Control of Lagrangian Systems. IEEE Transactions on Automatic Control vol. 61 905–920 (2016) -- [10.1109/tac.2015.2446831](https://doi.org/10.1109/tac.2015.2446831)
- Wesselink, T. C., Borja, P. & Scherpen, J. M. A. Saturated control without velocity measurements for planar robots with flexible joints. 2019 IEEE 58th Conference on Decision and Control (CDC) 7093–7098 (2019) doi:10.1109/cdc40024.2019.9029741 -- [10.1109/cdc40024.2019.9029741](https://doi.org/10.1109/cdc40024.2019.9029741)
- [Nuno, E. & Ortega, R. Achieving Consensus of Euler–Lagrange Agents With Interconnecting Delays and Without Velocity Measurements via Passivity-Based Control. IEEE Transactions on Control Systems Technology vol. 26 222–232 (2018)](achieving-consensus-of-euler-lagrange-agents-with-interconnecting-delays-and-without-velocity-measurements-via-passivity-based-control) -- [10.1109/tcst.2017.2661822](https://doi.org/10.1109/tcst.2017.2661822)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Kokotovic, P. V. & Sussmann, H. J. A positive real condition for global stabilization of nonlinear systems. Systems &amp; Control Letters vol. 13 125–133 (1989) -- [10.1016/0167-6911(89)90029-7](https://doi.org/10.1016/0167-6911(89)90029-7)
- [Fujimoto, K., Sakurama, K. & Sugie, T. Trajectory tracking control of port-controlled Hamiltonian systems via generalized canonical transformations. Automatica vol. 39 2059–2069 (2003)](trajectory-tracking-control-of-port-controlled-hamiltonian-systems-via-generalized-canonical-transformations) -- [10.1016/j.automatica.2003.07.005](https://doi.org/10.1016/j.automatica.2003.07.005)
- Stacey, G. & Mahony, R. The Role of Symmetry in Rigidity Analysis: A Tool for Network Localization and Formation Control. IEEE Transactions on Automatic Control vol. 63 1313–1328 (2018) -- [10.1109/tac.2017.2747760](https://doi.org/10.1109/tac.2017.2747760)

