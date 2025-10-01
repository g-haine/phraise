---
title: "Safety analysis of integrated adaptive cruise and lane keeping control using multi-modal port-Hamiltonian systems"
date: 2019-10-01 00:00:00 +0100
permalink: safety-analysis-of-integrated-adaptive-cruise-and-lane-keeping-control-using-multi-modal-port-hamiltonian-systems
year: 2020
authors: Siyuan Dai, Xenofon Koutsoukos
category: articles
tags:
  - Passivity
  - Safety analysis
  - Port-Hamiltonian systems
  - Automotive systems
  - Discretization
  - Quantization
---
 
## Authors
[Siyuan Dai](authors/siyuan-dai), [Xenofon Koutsoukos](authors/xenofon-koutsoukos)
 
## Abstract
A modern vehicle can be viewed as a complex cyber–physical system (CPS) where the vehicle dynamics interact with the software control systems. Adaptive cruise control (ACC) and lane keeping control (LKC), in particular, are foundational features for semi-autonomous and autonomous driving. Safety analysis of such systems is extremely important for realizing vehicle autonomy. Ensuring safety in such complex CPS is very challenging, especially in the presence of interactions between multiple subsystems, nonlinearities, hybrid dynamics, and disturbances. This paper presents an approach for safety analysis of automotive control systems using multi-modal port-Hamiltonian systems. The approach uses the Hamiltonian function as a barrier between the energy levels of the safe and unsafe states and employs passivity to prove that trajectories cannot cross this barrier. The approach is applied to the safety analysis of a vehicle dynamics composed with ACC and LKC. The goal is to ensure that the host vehicle will not collide with a lead vehicle and will not skid off of the road. The control design is implemented and evaluated using a hardware-in-the-loop simulation platform. The experimental results demonstrate the safety analysis approach including the impact of implementation effects such as discretization and quantization.
 
## Keywords
Passivity; Safety analysis; Port-Hamiltonian systems; Automotive systems; Discretization; Quantization
 
## Citation
- **Journal:** Nonlinear Analysis: Hybrid Systems
- **Year:** 2020
- **Volume:** 35
- **Issue:** 
- **Pages:** 100816
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.nahs.2019.100816](https://doi.org/10.1016/j.nahs.2019.100816)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Dai_2020,
  title={{Safety analysis of integrated adaptive cruise and lane keeping control using multi-modal port-Hamiltonian systems}},
  volume={35},
  ISSN={1751-570X},
  DOI={10.1016/j.nahs.2019.100816},
  journal={Nonlinear Analysis: Hybrid Systems},
  publisher={Elsevier BV},
  author={Dai, Siyuan and Koutsoukos, Xenofon},
  year={2020},
  pages={100816}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/safety-analysis-of-integrated-adaptive-cruise-and-lane-keeping-control-using-multi-modal-port-hamiltonian-systems.bib)
 
## References
- Sztipanovits, J. et al. Toward a Science of Cyber–Physical System Integration. Proceedings of the IEEE vol. 100 29–44 (2012) -- [10.1109/jproc.2011.2161529](https://doi.org/10.1109/jproc.2011.2161529)
- van der Schaft, Port-Hamiltonian systems: Network modeling and control of nonlinear physical systems. (2004)
- van der Schaft, Port-Hamiltonian systems: An introductory survey. Proc. Int. Congr. Mathematicians (2006)
- Duindam, (2009)
- Khalil, (2002)
- Fujimoto, K. & Sugie, T. Canonical transformation and stabilization of generalized Hamiltonian systems. Systems &amp; Control Letters vol. 42 217–227 (2001) -- [10.1016/s0167-6911(00)00091-8](https://doi.org/10.1016/s0167-6911(00)00091-8)
- Prajna, S. Barrier certificates for nonlinear model validation. Automatica vol. 42 117–126 (2006) -- [10.1016/j.automatica.2005.08.007](https://doi.org/10.1016/j.automatica.2005.08.007)
- Sloth, C., Pappas, G. J. & Wisniewski, R. Compositional safety analysis using barrier certificates. Proceedings of the 15th ACM international conference on Hybrid Systems: Computation and Control 15–24 (2012) doi:10.1145/2185632.2185639 -- [10.1145/2185632.2185639](https://doi.org/10.1145/2185632.2185639)
- Prajna, Primal-dual tests for safety and reachability. (2005)
- Prajna, Safety verification of hybrid systems using barrier certificates. (2004)
- Prajna, S., Jadbabaie, A. & Pappas, G. J. A Framework for Worst-Case and Stochastic Safety Verification Using Barrier Certificates. IEEE Transactions on Automatic Control vol. 52 1415–1428 (2007) -- [10.1109/tac.2007.902736](https://doi.org/10.1109/tac.2007.902736)
- Rajamani, (2006)
- Nilsson, P. et al. Correct-by-Construction Adaptive Cruise Control: Two Approaches. IEEE Transactions on Control Systems Technology vol. 24 1294–1307 (2016) -- [10.1109/tcst.2015.2501351](https://doi.org/10.1109/tcst.2015.2501351)
- Ames, Control barrier function based quadratic programs with application to adaptive cruise control. Proc. IEEE Conf. Decis. Control (2015)
- Xu, X., Grizzle, J. W., Tabuada, P. & Ames, A. D. Correctness Guarantees for the Composition of Lane Keeping and Adaptive Cruise Control. IEEE Transactions on Automation Science and Engineering vol. 15 1216–1229 (2018) -- [10.1109/tase.2017.2760863](https://doi.org/10.1109/tase.2017.2760863)
- Smith, Interdependence quantification for compositional control synthesis with an application in vehicle safety systems. (2016)
- Weißmann, A., Görges, D. & Lin, X. Energy-optimal adaptive cruise control combining model predictive control and dynamic programming. Control Engineering Practice vol. 72 125–137 (2018) -- [10.1016/j.conengprac.2017.12.001](https://doi.org/10.1016/j.conengprac.2017.12.001)
- Magdici, S. & Althoff, M. Adaptive Cruise Control with Safety Guarantees for Autonomous Vehicles. IFAC-PapersOnLine vol. 50 5774–5781 (2017) -- [10.1016/j.ifacol.2017.08.418](https://doi.org/10.1016/j.ifacol.2017.08.418)
- Li, S., Li, K., Rajamani, R. & Wang, J. Model Predictive Multi-Objective Vehicular Adaptive Cruise Control. IEEE Transactions on Control Systems Technology vol. 19 556–566 (2011) -- [10.1109/tcst.2010.2049203](https://doi.org/10.1109/tcst.2010.2049203)
- Althoff, M., Althoff, D., Wollherr, D. & Buss, M. Safety verification of autonomous vehicles for coordinated evasive maneuvers. 2010 IEEE Intelligent Vehicles Symposium (2010) doi:10.1109/ivs.2010.5548121 -- [10.1109/ivs.2010.5548121](https://doi.org/10.1109/ivs.2010.5548121)
- Hafner, M. R. & Del Vecchio, D. Computational Tools for the Safety Control of a Class of Piecewise Continuous Systems with Imperfect Information on a Partial Order. SIAM Journal on Control and Optimization vol. 49 2463–2493 (2011) -- [10.1137/090761203](https://doi.org/10.1137/090761203)
- [Dai, S. & Koutsoukos, X. Model-based automotive control design using port-Hamiltonian systems. 2015 International Conference on Complex Systems Engineering (ICCSE) 1–6 (2015) doi:10.1109/complexsys.2015.7385987](model-based-automotive-control-design-using-port-hamiltonian-systems) -- [10.1109/complexsys.2015.7385987](https://doi.org/10.1109/complexsys.2015.7385987)
- Byrnes, C. I. & Wei Lin. Losslessness, feedback equivalence, and the global stabilization of discrete-time nonlinear systems. IEEE Transactions on Automatic Control vol. 39 83–98 (1994) -- [10.1109/9.273341](https://doi.org/10.1109/9.273341)
- [Dai, S. & Koutsoukos, X. Safety Analysis of Automotive Control Systems Using Multi-Modal Port-Hamiltonian Systems. Proceedings of the 19th International Conference on Hybrid Systems: Computation and Control 105–114 (2016) doi:10.1145/2883817.2883845](safety-analysis-of-automotive-control-systems-using-multi-modal-port-hamiltonian-systems) -- [10.1145/2883817.2883845](https://doi.org/10.1145/2883817.2883845)
- Eyisi, Model-based control design and integration of cyberphysical system: An adaptive cruise control case study. J. Control Sci. Eng. Special Issue Embed. Model-Based Control (2013)
- Porter, J., Karsai, G. & Sztipanovits, J. Towards a time-triggered schedule calculation tool to support model-based embedded software design. Proceedings of the seventh ACM international conference on Embedded software 167–176 (2009) doi:10.1145/1629335.1629358 -- [10.1145/1629335.1629358](https://doi.org/10.1145/1629335.1629358)
- Kottenstette, N., Hall, J. F., Koutsoukos, X., Sztipanovits, J. & Antsaklis, P. Design of Networked Control Systems Using Passivity. IEEE Transactions on Control Systems Technology vol. 21 649–665 (2013) -- [10.1109/tcst.2012.2189211](https://doi.org/10.1109/tcst.2012.2189211)
- Oishi, Y. Passivity degradation under the discretization with the zero-order hold and the ideal sampler. 49th IEEE Conference on Decision and Control (CDC) 7613–7617 (2010) doi:10.1109/cdc.2010.5717886 -- [10.1109/cdc.2010.5717886](https://doi.org/10.1109/cdc.2010.5717886)
- [Stramigioli, S., Secchi, C., van der Schaft, A. J. & Fantuzzi, C. Sampled data systems passivity and discrete port-Hamiltonian systems. IEEE Transactions on Robotics vol. 21 574–587 (2005)](sampled-data-systems-passivity-and-discrete-port-hamiltonian-systems) -- [10.1109/tro.2004.842330](https://doi.org/10.1109/tro.2004.842330)
- Costa-Castello, R. & Fossas, E. On preserving passivity in sampled-data linear systems. 2006 American Control Conference 6 pp. (2006) doi:10.1109/acc.2006.1657407 -- [10.1109/acc.2006.1657407](https://doi.org/10.1109/acc.2006.1657407)
- Zhu, F., Yu, H., McCourt, M. J. & Antsaklis, P. J. Passivity and stability of switched systems under quantization. Proceedings of the 15th ACM international conference on Hybrid Systems: Computation and Control 237–244 (2012) doi:10.1145/2185632.2185668 -- [10.1145/2185632.2185668](https://doi.org/10.1145/2185632.2185668)
- Yu, H. & Antsaklis, P. J. A passivity measure of systems in cascade based on passivity indices. 49th IEEE Conference on Decision and Control (CDC) 2186–2191 (2010) doi:10.1109/cdc.2010.5717648 -- [10.1109/cdc.2010.5717648](https://doi.org/10.1109/cdc.2010.5717648)
- Bao, (2007)
- Hooke, Direct search solution of numerical and statistical problems. J. Assoc. Comput. Mach. (1969)
- Wu, (2013)
- Ortega, Control by interconnection and standard passivity-based control of port-Hamiltonian systems. (2008)

