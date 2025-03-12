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
[Lukas Ecker](authors/lukas-ecker), [Tobias Malzer](authors/tobias-malzer), [Arne Wahrburg](authors/arne-wahrburg), [Markus Schöberl](authors/markus-schoberl)
 
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
 
[Download the bib file]({{ site.baseurl }}/assets/bib/observer-design-for-a-single-mast-stacker-crane.bib)
 
## References
- [Rams, H., Schoberl, M. & Schlacher, K. Optimal Motion Planning and Energy-Based Control of a Single Mast Stacker Crane. IEEE Transactions on Control Systems Technology vol. 26 1449–1457 (2018)](optimal-motion-planning-and-energy-based-control-of-a-single-mast-stacker-crane) -- [10.1109/tcst.2017.2710953](https://doi.org/10.1109/tcst.2017.2710953)
- Rams, H. & Schoberl, M. On structural invariants in the energy based control of port-Hamiltonian systems with second-order Hamiltonian. 2017 American Control Conference (ACC) 1139–1144 (2017) doi:10.23919/acc.2017.7963106 -- [10.23919/acc.2017.7963106](https://doi.org/10.23919/acc.2017.7963106)
- Staudecker, M., Schlacher, K. & Hansl, R. Passivity Based Control and Time Optimal Trajectory Planning of a Single Mast Stacker Crane. IFAC Proceedings Volumes vol. 41 875–880 (2008) -- [10.3182/20080706-5-kr-1001.00150](https://doi.org/10.3182/20080706-5-kr-1001.00150)
- Simon, D. Optimal State Estimation. (2006) doi:10.1002/0470045345 -- [10.1002/0470045345](https://doi.org/10.1002/0470045345)
- Bachmayer, M., Ulbrich, H. & Rudolph, J. Flatness-based control of a horizontally moving erected beam with a point mass. Mathematical and Computer Modelling of Dynamical Systems vol. 17 49–69 (2011) -- [10.1080/13873954.2010.537517](https://doi.org/10.1080/13873954.2010.537517)
- Smyshlyaev, A. & Krstic, M. Backstepping observers for a class of parabolic PDEs. Systems &amp; Control Letters vol. 54 613–625 (2005) -- [10.1016/j.sysconle.2004.11.001](https://doi.org/10.1016/j.sysconle.2004.11.001)
- Schaum, A., Moreno, J. A. & Meurer, T. Dissipativity-based observer design for a class of coupled 1-D semi-linear parabolic PDE systems. IFAC-PapersOnLine vol. 49 98–103 (2016) -- [10.1016/j.ifacol.2016.07.425](https://doi.org/10.1016/j.ifacol.2016.07.425)
- Stürzer, D., Arnold, A. & Kugi, A. Closed-loop stability analysis of a gantry crane with heavy chain and payload. International Journal of Control vol. 91 1931–1943 (2017) -- [10.1080/00207179.2017.1335439](https://doi.org/10.1080/00207179.2017.1335439)
- [Malzer, T., Rams, H., Kolar, B. & Schoberl, M. Stability Analysis of the Observer Error of an In-Domain Actuated Vibrating String. IEEE Control Systems Letters vol. 5 1237–1242 (2021)](stability-analysis-of-the-observer-error-of-an-in-domain-actuated-vibrating-string) -- [10.1109/lcsys.2020.3025414](https://doi.org/10.1109/lcsys.2020.3025414)
- Schoberl, M. & Siuka, A. Analysis and comparison of port-Hamiltonian formulations for field theories - demonstrated by means of the Mindlin plate. 2013 European Control Conference (ECC) 548–553 (2013) doi:10.23919/ecc.2013.6669137 -- [10.23919/ecc.2013.6669137](https://doi.org/10.23919/ecc.2013.6669137)
- [Le Gorrec, Y., Zwart, H. & Maschke, B. Dirac structures and Boundary Control Systems associated with Skew-Symmetric Differential Operators. SIAM Journal on Control and Optimization vol. 44 1864–1892 (2005)](dirac-structures-and-boundary-control-systems-associated-with-skew-symmetric-differential-operators) -- [10.1137/040611677](https://doi.org/10.1137/040611677)
- [Toledo, J., Ramirez, H., Wu, Y. & Gorrec, Y. L. Passive observers for distributed port-Hamiltonian systems. IFAC-PapersOnLine vol. 53 7587–7592 (2020)](passive-observers-for-distributed-port-hamiltonian-systems) -- [10.1016/j.ifacol.2020.12.1356](https://doi.org/10.1016/j.ifacol.2020.12.1356)
- Ennsbrunner, H. & Schlacher, K. On the geometrical representation and interconnection of infinite dimensional port controlled Hamiltonian systems. Proceedings of the 44th IEEE Conference on Decision and Control 5263–5268 doi:10.1109/cdc.2005.1582998 -- [10.1109/cdc.2005.1582998](https://doi.org/10.1109/cdc.2005.1582998)
- [Schöberl, M. & Siuka, A. Jet bundle formulation of infinite-dimensional port-Hamiltonian systems using differential operators. Automatica vol. 50 607–613 (2014)](jet-bundle-formulation-of-infinite-dimensional-port-hamiltonian-systems-using-differential-operators) -- [10.1016/j.automatica.2013.11.035](https://doi.org/10.1016/j.automatica.2013.11.035)
- Staudecker, M. (2010). Regelung einer elastischen mechanischen Struktur am Beispiel eines Regalbediengeräts für Hochregallager. Ph.D. thesis, JKU, Linz.
- Li, T.-J. & Liu, A.-K. International Mathematics Research Notices vol. 1999 335 (1999) -- [10.1155/s1073792899000173](https://doi.org/10.1155/s1073792899000173)
- Luo, Z.-H., Guo, B.-Z. & Morgul, O. Stability and Stabilization of Infinite Dimensional Systems with Applications. Communications and Control Engineering (Springer London, 1999). doi:10.1007/978-1-4471-0419-3 -- [10.1007/978-1-4471-0419-3](https://doi.org/10.1007/978-1-4471-0419-3)
- Miletić, M., Stürzer, D. & Arnold, A. An Euler-Bernoulli beam with nonlinear damping and a nonlinear spring at the tip. Discrete and Continuous Dynamical Systems - Series B vol. 20 3029–3055 (2015) -- [10.3934/dcdsb.2015.20.3029](https://doi.org/10.3934/dcdsb.2015.20.3029)
- Jensen, A., Coopmans, C. & Chen, Y. Basics and guidelines of complementary filters for small UAS navigation. 2013 International Conference on Unmanned Aircraft Systems (ICUAS) 500–507 (2013) doi:10.1109/icuas.2013.6564726 -- [10.1109/icuas.2013.6564726](https://doi.org/10.1109/icuas.2013.6564726)
- [Gorrec, Y. L., Zwart, H. & Ramirez, H. Asymptotic stability of an Euler-Bernoulli beam coupled to non-linear spring-damper systems. IFAC-PapersOnLine vol. 50 5580–5585 (2017)](asymptotic-stability-of-an-euler-bernoulli-beam-coupled-to-non-linear-spring-damper-systems) -- [10.1016/j.ifacol.2017.08.1102](https://doi.org/10.1016/j.ifacol.2017.08.1102)

