---
layout: post
title: "Observer design for a single mast stacker crane"
date: 2021-09-08 00:00:00 +0100
permalink: observer-design-for-a-single-mast-stacker-crane
year: 2021
authors: Lukas Ecker, Tobias Malzer, Arne Wahrburg, Markus Schöberl
category: articles
---
 
## Authors
[Lukas Ecker](authors/lukas_ecker), [Tobias Malzer](authors/tobias_malzer), [Arne Wahrburg](authors/arne_wahrburg), [Markus Schöberl](authors/markus_schoberl)
 
## Abstract
This contribution is concerned with the design of observers for a single mast stacker crane, which is used, e. g., for storage and removal of loads in automated warehouses. As the mast of such stacker cranes is typically a lightweight construction, the system under consideration is described by ordinary as well as partial differential equations, i. e., the system exhibits a mixed finite-/infinite-dimensional character. We will present two different observer designs, an Extended Kalman Filter based on a finite-dimensional system approximation, using the Rayleigh-Ritz method and an approach exploiting the port-Hamiltonian system representation for the mixed finite-/infinite-dimensional scenario where in particular the observer-error system should be formulated in the port-Hamiltonian framework. The mixed-dimensional observer and the Kalman Filter are employed to estimate the deflection of the beam based on signals acquired by an inertial measurement unit at the beam tip. Such an approach considerably simplifies mechatronic integration as it renders strain-gauges at the base of the mast obsolete. Finally, measurement results demonstrate the capability of these approaches for monitoring and vibration-rejection purposes.
 
## Citation
- **Journal:** at - Automatisierungstechnik
- **Year:** 2021
- **Volume:** 69
- **Issue:** 9
- **Pages:** 806--816
- **Publisher:** Walter de Gruyter GmbH
- **DOI:** [10.1515/auto-2021-0018](https://doi.org/10.1515/auto-2021-0018)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Ecker_2021,
  title={{Observer design for a single mast stacker crane}},
  volume={69},
  ISSN={0178-2312},
  DOI={10.1515/auto-2021-0018},
  number={9},
  journal={at - Automatisierungstechnik},
  publisher={Walter de Gruyter GmbH},
  author={Ecker, Lukas and Malzer, Tobias and Wahrburg, Arne and Schöberl, Markus},
  year={2021},
  pages={806--816}
}
{% endraw %}
{% endhighlight %}
 
## References
- Rams, H., Schöberl, M. and Schlacher, K. (2017). Optimal Motion Planning and Energy-Based Control of a Single Mast Stacker Crane. IEEE Transactions on Control Systems Technology, 26(4), 1449–1457. -- [10.1109/TCST.2017.2710953](https://doi.org/10.1109/TCST.2017.2710953)
- Rams, H. and Schöberl, M. (2017). On structural invariants in the energy based control of port-Hamiltonian systems with second-order Hamiltonian. In American Control Conference (ACC), 1139–1144. -- [10.23919/ACC.2017.7963106](https://doi.org/10.23919/ACC.2017.7963106)
- Staudecker, M., Schlacher, K. and Hansl, R. (2008). Passivity based control and time optimal trajectory planning of a single mast stacker crane. IFAC Proceedings Volumes, 41(2), 875–880. -- [10.3182/20080706-5-KR-1001.00150](https://doi.org/10.3182/20080706-5-KR-1001.00150)
- Simon, D. (2006). Optimal State Estimation: Kalman, H∞, and Nonlinear Approaches. John Wiley & Sons. -- [10.1002/0470045345](https://doi.org/10.1002/0470045345)
- Bachmayer, M., Ulbrich, H. and Rudolph, J. (2011). Flatness-based control of a horizontally moving erected beam with a point mass. Mathematical and Computer Modelling of Dynamical Systems, 17(1). -- [10.1080/13873954.2010.537517](https://doi.org/10.1080/13873954.2010.537517)
- Smyshlyaev, A. and Kristic, M. (2005). Backstepping observers for a class of parabolic PDEs. Systems and Control Letters, 54, 613–625. -- [10.1016/j.sysconle.2004.11.001](https://doi.org/10.1016/j.sysconle.2004.11.001)
- Schaum, A., Moreno, J.A. and Meurer, T. (2016). Dissipativity-based observer design for a class of coupled 1-D semi-linear parabolic PDE systems. In Proceedings of the 2nd IFAC Workshop on Control of Systems Governed by Partial Differential Equations (CPDE). IFAC-PapersOnLine, 49(8), 98–103. -- [10.1016/j.ifacol.2016.07.425](https://doi.org/10.1016/j.ifacol.2016.07.425)
- Stürzer, D., Arnold, A. and Kugi, A. (2018). Closed-loop Stability Analysis of a Gantry Crane with Heavy Chain. Int. J. Control, 91(8), 1931–1943. -- [10.1080/00207179.2017.1335439](https://doi.org/10.1080/00207179.2017.1335439)
- Malzer, T., Rams, H., Kolar, B. and Schöberl, M. (2021). Stability Analysis of the Observer Error of an In-Domain Actuated Vibrating String. IEEE Control Systems Letters, 5(4), 1237–1242. -- [10.1109/LCSYS.2020.3025414](https://doi.org/10.1109/LCSYS.2020.3025414)
- Schöberl, M. and Siuka, A. (2013). Analysis and Comparison of Port-Hamiltonian Formulations for Field Theories – demonstrated by means of the Mindlin plate. In Proceedings of the European Control Conference (ECC), 548–553. -- [10.23919/ECC.2013.6669137](https://doi.org/10.23919/ECC.2013.6669137)
- [Le Gorrec, Y., Zwart, H.J. and Maschke, B. (2005). Dirac structures and boundary control systems associated with skew-symmetric differential operators. SIAM J. Control Optim., 44, 1864–1892.](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- [Toledo, J., Ramirez, H., Wu, Y. and Le Gorrec, Y. (2020). Passive observers for distributed port-Hamiltonian systems. In Proceedings of the 21st IFAC World Congress, Berlin, Germany. IFAC-PapersOnLine, 53(2), 7587–7592.](passive-observers-for-distributed-port-hamiltonian-systems) -- [10.1016/j.ifacol.2020.12.1356](https://doi.org/10.1016/j.ifacol.2020.12.1356)
- Ennsbrunner, H. and Schlacher, K. (2005). On the Geometrical Representation and Interconnection of Infinite Dimensional Port Controlled Hamiltonian Systems. In Proceedings of the 44th IEEE Conference on Decision and Control and the European Control Conf., 5263–5268. -- [10.1109/CDC.2005.1582998](https://doi.org/10.1109/CDC.2005.1582998)
- [Schöberl, M. and Siuka, A. (2014). Jet bundle formulation of infinite-dimensional port-Hamiltonian systems using differential operators. Automatica, 50(2), 607–613.](jet-bundle-formulation-of-infinite-dimensional-port-hamiltonian-systems-using-differential-operators) -- [10.1016/j.automatica.2013.11.035](https://doi.org/10.1016/j.automatica.2013.11.035)
- Staudecker, M. (2010). Regelung einer elastischen mechanischen Struktur am Beispiel eines Regalbediengeräts für Hochregallager. Ph.D. thesis, JKU, Linz.
- Liu, Z. and Zheng, S. (1999). Semigroups Associated with Dissipative Systems. Research Notes in Mathematics Series. Chapman and Hall/CRC. -- [10.1155/S1073792899000173](https://doi.org/10.1155/S1073792899000173)
- Luo, Z.H., Guo, B.Z. and Morgul, O. (1998). Stability and Stabilization of Infinite Dimensional Systems with Applications. Springer. -- [10.1007/978-1-4471-0419-3](https://doi.org/10.1007/978-1-4471-0419-3)
- Miletić, M., Stürzer, D. and Arnold, A. (2015). An Euler-Bernoulli beam with nonlinear damping and a nonlinear spring at the tip. Discrete & Continuous Dynamical Systems, 20(9), 3029–3055. -- [10.3934/dcdsb.2015.20.3029](https://doi.org/10.3934/dcdsb.2015.20.3029)
- Jensen, A., Coopmans, C. and Chen, Y. (2013). Basics and Guidelines of Complementary Filters for Small UAS Navigation. In International Conference on Unmanned Aircraft Systems (ICUAS). -- [10.1109/ICUAS.2013.6564726](https://doi.org/10.1109/ICUAS.2013.6564726)
- [Le Gorrec, Y., Zwart, H.J. and Ramirez, H. (2017). Asymptotic stability of an Euler-Bernoulli beam coupled to non-linear spring-damper systems. IFAC-PapersOnLine, 50(1), 5580–5585.](asymptotic-stability-of-an-euler-bernoulli-beam-coupled-to-non-linear-spring-damper-systems) -- [10.1016/j.ifacol.2017.08.1102](https://doi.org/10.1016/j.ifacol.2017.08.1102)

