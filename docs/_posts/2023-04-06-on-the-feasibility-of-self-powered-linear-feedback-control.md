---
layout: post
title: "On the Feasibility of Self-Powered Linear Feedback Control"
date: 2023-04-06 00:00:00 +0100
permalink: on-the-feasibility-of-self-powered-linear-feedback-control
year: 2024
authors: Connor H. Ligeikis, Jeffrey T. Scruggs
category: articles
---
 
## Authors
[Connor H. Ligeikis](authors/connor-h-ligeikis), [Jeffrey T. Scruggs](authors/jeffrey-t-scruggs)
 
## Abstract
A control system is called self-powered if the only energy it requires for operation is that which it absorbs from the plant. For a linear feedback law to be feasible for a self-powered control system, its feedback signal must be colocated with the control inputs, and its input–output mapping must satisfy an associated passivity constraint. The imposition of such a feedback law can be viewed equivalently as the imposition of a linear passive shunt admittance at the actuation ports of the plant. In this article, we consider the use of actively-controlled electronics to impose a self-powered linear feedback law. To be feasible, it is insufficient that the imposed admittance be passive, because parasitic losses must additionally be overcome. We derive sufficient feasibility conditions, which explicitly account for these losses. In the finite-dimensional, time-invariant case, the feasibility condition distills to a more conservative version of the positive-real lemma, which is parametrized by various loss parameters. Three examples are given, in which this condition is used to determine the least-efficient loss parameters necessary to realize a desired feedback law.
 
## Citation
- **Journal:** IEEE Transactions on Automatic Control
- **Year:** 2024
- **Volume:** 69
- **Issue:** 1
- **Pages:** 113--128
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tac.2023.3264706](https://doi.org/10.1109/tac.2023.3264706)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Ligeikis_2024,
  title={{On the Feasibility of Self-Powered Linear Feedback Control}},
  volume={69},
  ISSN={2334-3303},
  DOI={10.1109/tac.2023.3264706},
  number={1},
  journal={IEEE Transactions on Automatic Control},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Ligeikis, Connor H. and Scruggs, Jeffrey T.},
  year={2024},
  pages={113--128}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-the-feasibility-of-self-powered-linear-feedback-control.bib)
 
## References
- Desoer, C. A. & Vidyasagar, M. Feedback Systems. (2009) doi:10.1137/1.9780898719055 -- [10.1137/1.9780898719055](https://doi.org/10.1137/1.9780898719055)
- Miller, D. W., Hall, S. R. & von Flotow, A. H. Optimal control of power flow at structural junctions. Journal of Sound and Vibration vol. 140 475–497 (1990) -- [10.1016/0022-460x(90)90762-o](https://doi.org/10.1016/0022-460x(90)90762-o)
- Elliott, S. J., Joseph, P., Nelson, P. A. & Johnson, M. E. Power output minimization and power absorption in the active control of sound. The Journal of the Acoustical Society of America vol. 90 2501–2512 (1991) -- [10.1121/1.402054](https://doi.org/10.1121/1.402054)
- MacMartin, D. G. & Hall, S. R. Control of uncertain structures using an H(infinity) power flow approach. Journal of Guidance, Control, and Dynamics vol. 14 521–530 (1991) -- [10.2514/3.20671](https://doi.org/10.2514/3.20671)
- Jolly, M. R. & Margolis, D. L. Assessing the Potential for Energy Regeneration in Dynamic Subsystems. Journal of Dynamic Systems, Measurement, and Control vol. 119 265–270 (1997) -- [10.1115/1.2801243](https://doi.org/10.1115/1.2801243)
- SHARP, S. J., NELSON, P. A. & KOOPMANN, G. H. A THEORETICAL INVESTIGATION OF OPTIMAL POWER ABSORPTION AS A NOISE CONTROL TECHNIQUE. Journal of Sound and Vibration vol. 251 927–935 (2002) -- [10.1006/jsvi.2001.3907](https://doi.org/10.1006/jsvi.2001.3907)
- Kelkar, A. G. & Joshi, S. M. Control of Elastic Systems via Passivity-Based Methods. Journal of Vibration and Control vol. 10 1699–1735 (2004) -- [10.1177/1077546304042066](https://doi.org/10.1177/1077546304042066)
- Gosavi, S. V. & Kelkar, A. G. Modelling, Identification, and Passivity-Based Robust Control of Piezo-actuated Flexible Beam. Journal of Vibration and Acoustics vol. 126 260–271 (2004) -- [10.1115/1.1687392](https://doi.org/10.1115/1.1687392)
- Zilletti, M., Gardonio, P. & Elliott, S. J. Optimisation of a velocity feedback controller to minimise kinetic energy and maximise power dissipation. Journal of Sound and Vibration vol. 333 4405–4414 (2014) -- [10.1016/j.jsv.2014.04.036](https://doi.org/10.1016/j.jsv.2014.04.036)
- Ortega, R., Spong, M. W., Gomez-Estern, F. & Blankenstein, G. Stabilization of a class of underactuated mechanical systems via interconnection and damping assignment. IEEE Transactions on Automatic Control vol. 47 1218–1233 (2002) -- [10.1109/tac.2002.800770](https://doi.org/10.1109/tac.2002.800770)
- Albu-Schäffer, A., Ott, C. & Hirzinger, G. A Unified Passivity-based Control Framework for Position, Torque and                 Impedance Control of Flexible Joint Robots. The International Journal of Robotics Research vol. 26 23–39 (2007) -- [10.1177/0278364907073776](https://doi.org/10.1177/0278364907073776)
- Secchi, Control of Interactive Robotic Interfaces: A. Port-Hamiltonian Approach (2007)
- Hatanaka, T., Chopra, N. & Spong, M. W. Passivity-based control of robots: Historical perspective and contemporary issues. 2015 54th IEEE Conference on Decision and Control (CDC) 2450–2452 (2015) doi:10.1109/cdc.2015.7402575 -- [10.1109/cdc.2015.7402575](https://doi.org/10.1109/cdc.2015.7402575)
- Ott, C., Albu-Schaffer, A., Kugi, A. & Hirzinger, G. On the Passivity-Based Impedance Control of Flexible Joint Robots. IEEE Transactions on Robotics vol. 24 416–429 (2008) -- [10.1109/tro.2008.915438](https://doi.org/10.1109/tro.2008.915438)
- Chevva, K., Sun, F., Blanc, A. & Mendoza, J. Active vibration control using minimum actuation power. Journal of Sound and Vibration vol. 340 1–21 (2015) -- [10.1016/j.jsv.2014.06.019](https://doi.org/10.1016/j.jsv.2014.06.019)
- Putting energy back in control. IEEE Control Systems vol. 21 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Beattie, C. A., Mehrmann, V. & Van Dooren, P. Robust port-Hamiltonian representations of passive systems. Automatica vol. 100 182–186 (2019)](robust-port-hamiltonian-representations-of-passive-systems) -- [10.1016/j.automatica.2018.11.013](https://doi.org/10.1016/j.automatica.2018.11.013)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- [Borja, P., Ortega, R. & Scherpen, J. M. A. New Results on Stabilization of Port-Hamiltonian Systems via PID Passivity-Based Control. IEEE Transactions on Automatic Control vol. 66 625–636 (2021)](new-results-on-stabilization-of-port-hamiltonian-systems-via-pid-passivity-based-control) -- [10.1109/tac.2020.2986731](https://doi.org/10.1109/tac.2020.2986731)
- Brogliato, B., Maschke, B., Lozano, R. & Egeland, O. Dissipative Systems Analysis and Control. Communications and Control Engineering (Springer London, 2007). doi:10.1007/978-1-84628-517-2 -- [10.1007/978-1-84628-517-2](https://doi.org/10.1007/978-1-84628-517-2)
- Smith, M. C. Synthesis of mechanical networks: the inerter. IEEE Transactions on Automatic Control vol. 47 1648–1662 (2002) -- [10.1109/tac.2002.803532](https://doi.org/10.1109/tac.2002.803532)
- Newcomb, Linear Multiport Synthesis (1966)
- Brune, O. Synthesis of a Finite Two‐terminal Network whose Driving‐point Impedance is a Prescribed Function of Frequency. Journal of Mathematics and Physics vol. 10 191–236 (1931) -- [10.1002/sapm1931101191](https://doi.org/10.1002/sapm1931101191)
- Darlington, S. Synthesis of Reactance 4‐Poles Which Produce Prescribed Insertion Loss Characteristics: Including Special Applications To Filter Design. Journal of Mathematics and Physics vol. 18 257–353 (1939) -- [10.1002/sapm1939181257](https://doi.org/10.1002/sapm1939181257)
- Hughes, T. H., Morelli, A. & Smith, M. C. Electrical Network Synthesis: A Survey of Recent Work. Lecture Notes in Control and Information Sciences - Proceedings 281–293 (2018) doi:10.1007/978-3-319-67068-3_21 -- [10.1007/978-3-319-67068-3_21](https://doi.org/10.1007/978-3-319-67068-3_21)
- Taylor, J. Strictly positive-real functions and the Lefschetz-Kalman Yakubovich (LKY) lemma. IEEE Transactions on Circuits and Systems vol. 21 310–311 (1974) -- [10.1109/tcs.1974.1083816](https://doi.org/10.1109/tcs.1974.1083816)
- Zuo, L. & Nayfeh, S. A. Structured H2 Optimization of Vehicle Suspensions Based on Multi-Wheel Models. Vehicle System Dynamics vol. 40 351–371 (2003) -- [10.1076/vesd.40.5.351.17914](https://doi.org/10.1076/vesd.40.5.351.17914)
- Chen, M. Z. Q. & Smith, M. C. Restricted Complexity Network Realizations for Passive Mechanical Control. IEEE Transactions on Automatic Control vol. 54 2290–2301 (2009) -- [10.1109/tac.2009.2028953](https://doi.org/10.1109/tac.2009.2028953)
- Lozano-Leal, R. & Joshi, S. M. On the design of the dissipative LQG-type controllers. Proceedings of the 27th IEEE Conference on Decision and Control 1645–1646 doi:10.1109/cdc.1988.194606 -- [10.1109/cdc.1988.194606](https://doi.org/10.1109/cdc.1988.194606)
- Papageorgiou, C. & Smith, M. C. Positive real synthesis using matrix inequalities for mechanical networks: application to vehicle suspension. IEEE Transactions on Control Systems Technology vol. 14 423–435 (2006) -- [10.1109/tcst.2005.863663](https://doi.org/10.1109/tcst.2005.863663)
- Geromel, J. C. & Gapski, P. B. Synthesis of positive real ℋ/sub 2/ controllers. IEEE Transactions on Automatic Control vol. 42 988–992 (1997) -- [10.1109/9.599979](https://doi.org/10.1109/9.599979)
- Damaren, C. J. Optimal strictly positive real controllers using direct optimization. Journal of the Franklin Institute vol. 343 271–278 (2006) -- [10.1016/j.jfranklin.2005.12.004](https://doi.org/10.1016/j.jfranklin.2005.12.004)
- Bridgeman, L. J. & Forbes, J. R. Conic-sector-based control to circumvent passivity violations. International Journal of Control vol. 87 1467–1477 (2014) -- [10.1080/00207179.2013.845693](https://doi.org/10.1080/00207179.2013.845693)
- Warner, E. C. & Scruggs, J. T. Control of vibratory networks with passive and regenerative systems. 2015 American Control Conference (ACC) 5502–5508 (2015) doi:10.1109/acc.2015.7172200 -- [10.1109/acc.2015.7172200](https://doi.org/10.1109/acc.2015.7172200)
- Forbes, J. R. Synthesis of strictly positive real ℋ2 controllers using dilated LMIs. International Journal of Control vol. 92 2584–2590 (2018) -- [10.1080/00207179.2018.1453615](https://doi.org/10.1080/00207179.2018.1453615)
- Fleming, A. J., Behrens, S. & Moheimani, S. O. R. Synthetic impedance for implementation ofpiezoelectric shunt-damping circuits. Electronics Letters vol. 36 1525–1526 (2000) -- [10.1049/el:20001083](https://doi.org/10.1049/el:20001083)
- Moheimani, S. O. R. A survey of recent innovations in vibration damping and control using shunted piezoelectric transducers. IEEE Transactions on Control Systems Technology vol. 11 482–494 (2003) -- [10.1109/tcst.2003.813371](https://doi.org/10.1109/tcst.2003.813371)
- Sugino, C., Ruzzene, M. & Erturk, A. Design and Analysis of Piezoelectric Metamaterial Beams With Synthetic Impedance Shunt Circuits. IEEE/ASME Transactions on Mechatronics vol. 23 2144–2155 (2018) -- [10.1109/tmech.2018.2863257](https://doi.org/10.1109/tmech.2018.2863257)
- Nakano, K., Suda, Y. & Nakadai, S. Self-powered active vibration control using a single electric actuator. Journal of Sound and Vibration vol. 260 213–235 (2003) -- [10.1016/s0022-460x(02)00980-x](https://doi.org/10.1016/s0022-460x(02)00980-x)
- Nakano, K. Combined Type Self-Powered Active Vibration Control of Truck Cabins. Vehicle System Dynamics vol. 41 449–473 (2004) -- [10.1080/00423110512331383858](https://doi.org/10.1080/00423110512331383858)
- Khoshnoud, F. et al. Energy Regeneration From Suspension Dynamic Modes and Self-Powered Actuation. IEEE/ASME Transactions on Mechatronics vol. 20 2513–2524 (2015) -- [10.1109/tmech.2015.2392551](https://doi.org/10.1109/tmech.2015.2392551)
- Choi, Y.-T. & Wereley, N. M. Self-Powered Magnetorheological Dampers. Journal of Vibration and Acoustics vol. 131 (2009) -- [10.1115/1.3142882](https://doi.org/10.1115/1.3142882)
- Tang, X. & Zuo, L. Self-powered Active Control of Structures with TMDs. Conference Proceedings of the Society for Experimental Mechanics Series 227–238 (2011) doi:10.1007/978-1-4419-9716-6_21 -- [10.1007/978-1-4419-9716-6_21](https://doi.org/10.1007/978-1-4419-9716-6_21)
- Asai, T. & Scruggs, J. T. Nonlinear stochastic control of self-powered variable-damping vibration control systems. 2016 American Control Conference (ACC) 442–448 (2016) doi:10.1109/acc.2016.7524954 -- [10.1109/acc.2016.7524954](https://doi.org/10.1109/acc.2016.7524954)
- Jolly, M. R. & Margolis, D. L. Regenerative Systems for Vibration Control. Journal of Vibration and Acoustics vol. 119 208–215 (1997) -- [10.1115/1.2889705](https://doi.org/10.1115/1.2889705)
- Margolis, D. Energy Regenerative Actuator for Motion Control With Application to Fluid Power Systems. Journal of Dynamic Systems, Measurement, and Control vol. 127 33–40 (2004) -- [10.1115/1.1870038](https://doi.org/10.1115/1.1870038)
- Anubi, O. M. & Clemen, L. Energy-regenerative model predictive control. Journal of the Franklin Institute vol. 352 2152–2170 (2015) -- [10.1016/j.jfranklin.2015.02.025](https://doi.org/10.1016/j.jfranklin.2015.02.025)
- Clemen, L., Anubi, O. M. & Margolis, D. On the Regenerative Capabilities of Electrodynamic Dampers Using Bond Graphs and Model Predictive Control. Journal of Dynamic Systems, Measurement, and Control vol. 138 (2016) -- [10.1115/1.4032505](https://doi.org/10.1115/1.4032505)
- Liu, Y., Zuo, L. & Tang, X. Regenerative Vibration Control of Tall Buildings Using Model Predictive Control. Volume 1: Aerial Vehicles; Aerospace Control; Alternative Energy; Automotive Control Systems; Battery Systems; Beams and Flexible Structures; Biologically-Inspired Control and its Applications; Bio-Medical and Bio-Mechanical Systems; Biomedical Robots and Rehab; Bipeds and Locomotion; Control Design Methods for Adv. Powertrain Systems and Components; Control of Adv. Combustion Engines, Building Energy Systems, Mechanical Systems; Control, Monitoring, and Energy Harvesting of Vibratory Systems (2013) doi:10.1115/dscc2013-3988 -- [10.1115/dscc2013-3988](https://doi.org/10.1115/dscc2013-3988)
- Shen, W., Zhu, S., Xu, Y.-L. & Zhu, H. Energy regenerative tuned mass dampers in high-rise buildings. Structural Control and Health Monitoring vol. 25 e2072 (2017) -- [10.1002/stc.2072](https://doi.org/10.1002/stc.2072)
- Onoda, J., Makihara, K. & Minesugi, K. Energy-Recycling Semi-Active Method for Vibration Suppression with Piezoelectric Transducers. AIAA Journal vol. 41 711–719 (2003) -- [10.2514/2.2002](https://doi.org/10.2514/2.2002)
- Onoda, J. & Makihara, K. Performance of Simple and Sophisticated Control in Energy-recycling Semi-active Vibration Suppression. Journal of Vibration and Control vol. 14 417–436 (2008) -- [10.1177/1077546307080027](https://doi.org/10.1177/1077546307080027)
- Laschowski, B., McPhee, J. & Andrysek, J. Lower-Limb Prostheses and Exoskeletons With Energy Regeneration: Mechatronic Design and Optimization Review. Journal of Mechanisms and Robotics vol. 11 (2019) -- [10.1115/1.4043460](https://doi.org/10.1115/1.4043460)
- Goldfarb, M., Barth, E. J., Gogola, M. A. & Wehrmeyer, J. A. Design and energetic characterization of a liquid-propellant-powered actuator for self-powered robots. IEEE/ASME Transactions on Mechatronics vol. 8 254–262 (2003) -- [10.1109/tmech.2003.812842](https://doi.org/10.1109/tmech.2003.812842)
- Richter, H. A Framework for Control of Robots With Energy Regeneration. Journal of Dynamic Systems, Measurement, and Control vol. 137 (2015) -- [10.1115/1.4030391](https://doi.org/10.1115/1.4030391)
- Carabin, G., Wehrle, E. & Vidoni, R. A Review on Energy-Saving Optimization Methods for Robotic and Automatic Systems. Robotics vol. 6 39 (2017) -- [10.3390/robotics6040039](https://doi.org/10.3390/robotics6040039)
- Khalaf, P. & Richter, H. On Global, Closed-Form Solutions to Parametric Optimization Problems for Robots With Energy Regeneration. Journal of Dynamic Systems, Measurement, and Control vol. 140 (2017) -- [10.1115/1.4037653](https://doi.org/10.1115/1.4037653)
- Richter, H., Simon, D. & Bogert, A. van den. Semiactive Virtual Control Method for Robots with Regenerative Energy-Storing Joints. IFAC Proceedings Volumes vol. 47 10244–10250 (2014) -- [10.3182/20140824-6-za-1003.00332](https://doi.org/10.3182/20140824-6-za-1003.00332)
- Khalaf, P. & Richter, H. Trajectory Optimization of Robots With Regenerative Drive Systems: Numerical and Experimental Results. IEEE Transactions on Robotics vol. 36 501–516 (2020) -- [10.1109/tro.2019.2923920](https://doi.org/10.1109/tro.2019.2923920)
- Ligeikis, C. & Scruggs, J. Feasibility and Synthesis of Finite-Dimensional, Linear Time-Invariant Synthetic Admittances for Self-Powered Systems. 2021 60th IEEE Conference on Decision and Control (CDC) 2440–2447 (2021) doi:10.1109/cdc45484.2021.9683340 -- [10.1109/cdc45484.2021.9683340](https://doi.org/10.1109/cdc45484.2021.9683340)
- Ven, On fluid compressibility in switch-mode hydraulic circuits part 1: Modeling and analysis. J. Dyn. Syst., Meas., Control (2013)
- Ven, On fluid compressibility in switch-mode hydraulic circuits part II: Experimental results. J. Dyn. Syst., Meas., Control (2013)
- Christen, T. & Carlen, M. W. Theory of Ragone plots. Journal of Power Sources vol. 91 210–216 (2000) -- [10.1016/s0378-7753(00)00474-2](https://doi.org/10.1016/s0378-7753(00)00474-2)
- Kanwal, R. P. Linear Integral Equations. (Springer New York, 2013). doi:10.1007/978-1-4614-6012-1 -- [10.1007/978-1-4614-6012-1](https://doi.org/10.1007/978-1-4614-6012-1)
- Anderson, Netw. Anal. and Synth.: A Modern Syst. Theory Approach (2013)
- Linear robust control. Control Engineering Practice vol. 3 1788 (1995) -- [10.1016/0967-0661(95)90063-2](https://doi.org/10.1016/0967-0661(95)90063-2)
- Forbes, J. R. & Damaren, C. J. Passive linear time-varying systems: State-space realizations, stability in feedback, and controller synthesis. Proceedings of the 2010 American Control Conference 1097–1104 (2010) doi:10.1109/acc.2010.5530792 -- [10.1109/acc.2010.5530792](https://doi.org/10.1109/acc.2010.5530792)
- Forbes, J. R. & Damaren, C. J. Linear Time-Varying Passivity-Based Attitude Control Employing Magnetic and Mechanical Actuation. Journal of Guidance, Control, and Dynamics vol. 34 1363–1372 (2011) -- [10.2514/1.51899](https://doi.org/10.2514/1.51899)
- Nonlinear Systems. Numerical Algorithms 168–183 (2015) doi:10.1201/b18657-16 -- [10.1201/b18657-16](https://doi.org/10.1201/b18657-16)
- Ligeikis, C. & Scruggs, J. Nonlinear Feedback Controllers for Self-Powered Systems with Non-Ideal Energy Storage Subsystems. 2021 American Control Conference (ACC) 1748–1753 (2021) doi:10.23919/acc50511.2021.9483323 -- [10.23919/acc50511.2021.9483323](https://doi.org/10.23919/acc50511.2021.9483323)
- Lin, Y. K. & Yong, Y. Evolutionary Kanai‐Tajimi Earthquake Models. Journal of Engineering Mechanics vol. 113 1119–1137 (1987) -- [10.1061/(asce)0733-9399(1987)113:8(1119)](https://doi.org/10.1061/(asce)0733-9399(1987)113:8(1119))
- strm, Introduction to Stochastic Control Theory (2012)
- Trumpf, J. Observers for linear time-varying systems. Linear Algebra and its Applications vol. 425 303–312 (2007) -- [10.1016/j.laa.2007.01.015](https://doi.org/10.1016/j.laa.2007.01.015)
- Dastjerdi, A. A., Vinagre, B. M., Chen, Y. & HosseinNia, S. H. Linear fractional order controllers; A survey in the frequency domain. Annual Reviews in Control vol. 47 51–70 (2019) -- [10.1016/j.arcontrol.2019.03.008](https://doi.org/10.1016/j.arcontrol.2019.03.008)

