---
title: "Explicit and Implicit IDA-PBC Design and Implementation for a Portal Crane"
date: 2021-04-15 00:00:00 +0100
permalink: explicit-and-implicit-ida-pbc-design-and-implementation-for-a-portal-crane
year: 2020
authors: Enrique J. Vidal, Oscar B. Cieza, Johann Reger
category: proceedings
tags:
  - IDA-PBC
  - Port-Hamiltonian systems
  - Implicit systems
  - Passivity
  - Portal crane
---
 
## Authors
[Enrique J. Vidal](authors/enrique-j-vidal), [Oscar B. Cieza](authors/oscar-b-cieza), [Johann Reger](authors/johann-reger)
 
## Abstract
The interconnection and damping assignment passivity-based control (IDA-PBC) is well-known for regulating the behavior of nonlinear systems. In underactuated mechanical systems (UMSs), its application requires the satisfaction of matching conditions, which in many cases demands to solve partial differential equations (PDEs). Only recently, the IDA-PBC method has been extended to UMSs in implicit representation, where the system dynamics are described by a set of differential-algebraic equations. In some system classes, this implicit model allows to circumvent the PDE obstacle and to construct an output-feedback law. This paper discusses the design and real-system implementation of the total energy shaping IDA-PBC with an optimal local performance for a portal crane system in implicit port-Hamiltonian representation. The implicit controller is compared with the simplified (explicit) IDA-PBC, introduced by Xue and Zhiyong (2017), which also shapes the total energy and avoids PDEs.
 
## Keywords
IDA-PBC; Port-Hamiltonian systems; Implicit systems; Passivity; Portal crane
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2020
- **Volume:** 53
- **Issue:** 2
- **Pages:** 5592--5597
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2020.12.1572](https://doi.org/10.1016/j.ifacol.2020.12.1572)
- **Note:** 21st IFAC World Congress- Berlin, Germany, 11–17 July 2020
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Vidal_2020,
  title={{Explicit and Implicit IDA-PBC Design and Implementation for a Portal Crane}},
  volume={53},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2020.12.1572},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Vidal, Enrique J. and Cieza, Oscar B. and Reger, Johann},
  year={2020},
  pages={5592--5597}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/explicit-and-implicit-ida-pbc-design-and-implementation-for-a-portal-crane.bib)
 
## References
- Banavar, R., Kazi, F., Ortega, R., and Manjarekar, N. (2006). The IDA-PBC methodology applied to a gantry crane. In Proceedings of the Mathematical Theory of Networks and Systems, 143–147.
- [Castaños, F. & Gromov, D. Passivity-based control of implicit port-Hamiltonian systems with holonomic constraints. Systems &amp; Control Letters vol. 94 11–18 (2016)](passivity-based-control-of-implicit-port-hamiltonian-systems-with-holonomic-constraints) -- [10.1016/j.sysconle.2016.04.004](https://doi.org/10.1016/j.sysconle.2016.04.004)
- [Castaños, F., Gromov, D., Hayward, V. & Michalska, H. Implicit and explicit representations of continuous-time port-Hamiltonian systems. Systems &amp; Control Letters vol. 62 324–330 (2013)](implicit-and-explicit-representations-of-continuous-time-port-hamiltonian-systems) -- [10.1016/j.sysconle.2013.01.007](https://doi.org/10.1016/j.sysconle.2013.01.007)
- [Cieza, O. B. & Reger, J. IDA-PBC for Underactuated Mechanical Systems in Implicit Port-Hamiltonian Representation. 2019 18th European Control Conference (ECC) (2019) doi:10.23919/ecc.2019.8795994](ida-pbc-for-underactuated-mechanical-systems-in-implicit-port-hamiltonian-representation) -- [10.23919/ecc.2019.8795994](https://doi.org/10.23919/ecc.2019.8795994)
- Donaire, A. et al. Shaping the energy of mechanical systems without solving partial differential equations. 2015 American Control Conference (ACC) 1351–1356 (2015) doi:10.1109/acc.2015.7170921 -- [10.1109/acc.2015.7170921](https://doi.org/10.1109/acc.2015.7170921)
- Donaire, A., Ortega, R. & Romero, J. G. Simultaneous interconnection and damping assignment passivity-based control of mechanical systems using dissipative forces. Systems &amp; Control Letters vol. 94 118–126 (2016) -- [10.1016/j.sysconle.2016.05.006](https://doi.org/10.1016/j.sysconle.2016.05.006)
- [Macchelli, A. Passivity-Based Control of Implicit Port-Hamiltonian Systems. SIAM Journal on Control and Optimization vol. 52 2422–2448 (2014)](passivity-based-control-of-implicit-port-hamiltonian-systems) -- [10.1137/130918228](https://doi.org/10.1137/130918228)
- Ortega, R., Spong, M. W., Gomez-Estern, F. & Blankenstein, G. Stabilization of a class of underactuated mechanical systems via interconnection and damping assignment. IEEE Transactions on Automatic Control vol. 47 1218–1233 (2002) -- [10.1109/tac.2002.800770](https://doi.org/10.1109/tac.2002.800770)
- [Ryalat, M. & Laila, D. S. A simplified IDA-PBC design for underactuated mechanical systems with applications. European Journal of Control vol. 27 1–16 (2016)](a-simplified-ida-pbc-design-for-underactuated-mechanical-systems-with-applications) -- [10.1016/j.ejcon.2015.12.001](https://doi.org/10.1016/j.ejcon.2015.12.001)
- Singhal, R., Patayane, R. & Banavar, R. N. Tracking a Trajectory for a Gantry Crane: Comparison Between IDA-PBC and Direct Lyapunov Approach. 2006 IEEE International Conference on Industrial Technology 1788–1793 (2006) doi:10.1109/icit.2006.372495 -- [10.1109/icit.2006.372495](https://doi.org/10.1109/icit.2006.372495)
- Spong, M. W. Partial feedback linearization of underactuated mechanical systems. Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS’94) vol. 1 314–321 -- [10.1109/iros.1994.407375](https://doi.org/10.1109/iros.1994.407375)
- Xue, L. & Zhiyong, G. Control of underactuated bridge cranes: A simplified IDA-PBC approach. 2017 11th Asian Control Conference (ASCC) 717–722 (2017) doi:10.1109/ascc.2017.8287258 -- [10.1109/ascc.2017.8287258](https://doi.org/10.1109/ascc.2017.8287258)

