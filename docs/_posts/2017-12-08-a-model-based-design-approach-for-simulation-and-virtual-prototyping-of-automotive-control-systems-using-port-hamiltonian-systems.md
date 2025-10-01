---
title: "A model-based design approach for simulation and virtual prototyping of automotive control systems using port-Hamiltonian systems"
date: 2017-12-08 00:00:00 +0100
permalink: a-model-based-design-approach-for-simulation-and-virtual-prototyping-of-automotive-control-systems-using-port-hamiltonian-systems
year: 2019
authors: Siyuan Dai, Zhenkai Zhang, Xenofon Koutsoukos
category: articles
tags:
  - Cyber–physical systems
  - Model-based design
  - Port-Hamiltonian systems
  - Passivity
  - Automotive control software
---
 
## Authors
[Siyuan Dai](authors/siyuan-dai), [Zhenkai Zhang](authors/zhenkai-zhang), [Xenofon Koutsoukos](authors/xenofon-koutsoukos)
 
## Abstract
Cyber–physical systems (CPS) such as automotive control systems consist of various interacting cyber and physical components. Heterogeneous domains, composition of multiple components, complex dynamics, and nonlinearities result in significant challenges for design, modeling, and simulation of CPS. Model-based design can be used to address such challenges, but it is very important to use physically accurate heterogeneous models that can be composed to represent the overall system behavior. Further, it is important to preserve the properties derived from analyses based on the mathematical models in the control system implementation in order to reduce costly testing and design changes late in the development cycle. This paper proposes a model-based design methodology for automotive control software using port-Hamiltonian systems (PHS). PHS are used to model the vehicle dynamics, speed and steering control systems, and the interactions between physical and cyber components. Passivity analysis is used to design the controllers and ensure system stability. More importantly, the proposed approach guarantees that passivity is preserved after time-discretization and quantization of the controllers. The models are then used for code generation and compilation, scheduling, and software deployment, ensuring that passivity is preserved by the control system implementation. We evaluate the methodology using an automotive control design case study implemented on a hardware-in-the-loop simulation platform and present simulation results to demonstrate its effectiveness.
 
## Keywords
Cyber–physical systems; Model-based design; Port-Hamiltonian systems; Passivity; Automotive control software
 
## Citation
- **Journal:** Software &amp; Systems Modeling
- **Year:** 2019
- **Volume:** 18
- **Issue:** 3
- **Pages:** 1637--1653
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10270-017-0646-1](https://doi.org/10.1007/s10270-017-0646-1)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Dai_2017,
  title={{A model-based design approach for simulation and virtual prototyping of automotive control systems using port-Hamiltonian systems}},
  volume={18},
  ISSN={1619-1374},
  DOI={10.1007/s10270-017-0646-1},
  number={3},
  journal={Software &amp; Systems Modeling},
  publisher={Springer Science and Business Media LLC},
  author={Dai, Siyuan and Zhang, Zhenkai and Koutsoukos, Xenofon},
  year={2017},
  pages={1637--1653}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-model-based-design-approach-for-simulation-and-virtual-prototyping-of-automotive-control-systems-using-port-hamiltonian-systems.bib)
 
## References
- Byrnes, C. I. & Wei Lin. Losslessness, feedback equivalence, and the global stabilization of discrete-time nonlinear systems. IEEE Transactions on Automatic Control vol. 39 83–98 (1994) -- [10.1109/9.273341](https://doi.org/10.1109/9.273341)
- CarSim: Mechanical: Simulation. Michigan, Ann Arbor (2013)
- [Cervera, J., van der Schaft, A. J. & Baños, A. Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica vol. 43 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- Costa-Castello, R. & Fossas, E. On preserving passivity in sampled-data linear systems. 2006 American Control Conference 6 pp. (2006) doi:10.1109/acc.2006.1657407 -- [10.1109/acc.2006.1657407](https://doi.org/10.1109/acc.2006.1657407)
- Dai, S.: Compositional modeling and design of cyber-physical systems using port-Hamiltonian systems. Doctoral dissertation, Vanderbilt University. (2016)
- [Dai, S. & Koutsoukos, X. Model-based automotive control design using port-Hamiltonian systems. 2015 International Conference on Complex Systems Engineering (ICCSE) 1–6 (2015) doi:10.1109/complexsys.2015.7385987](model-based-automotive-control-design-using-port-hamiltonian-systems) -- [10.1109/complexsys.2015.7385987](https://doi.org/10.1109/complexsys.2015.7385987)
- [Dai, S. & Koutsoukos, X. Safety Analysis of Automotive Control Systems Using Multi-Modal Port-Hamiltonian Systems. Proceedings of the 19th International Conference on Hybrid Systems: Computation and Control 105–114 (2016) doi:10.1145/2883817.2883845](safety-analysis-of-automotive-control-systems-using-multi-modal-port-hamiltonian-systems) -- [10.1145/2883817.2883845](https://doi.org/10.1145/2883817.2883845)
- Derler, P., Lee, E. A. & Vincentelli, A. S. Modeling Cyber–Physical Systems. Proceedings of the IEEE vol. 100 13–28 (2012) -- [10.1109/jproc.2011.2160929](https://doi.org/10.1109/jproc.2011.2160929)
- [Dirksz, D. A. & Scherpen, J. M. A. Port-Hamiltonian and power-based integral type control of a manipulator system. IFAC Proceedings Volumes vol. 44 13450–13455 (2011)](port-hamiltonian-and-power-based-integral-type-control-of-a-manipulator-system) -- [10.3182/20110828-6-it-1002.01030](https://doi.org/10.3182/20110828-6-it-1002.01030)
- [Donaire, A. & Junco, S. Derivation of Input-State-Output Port-Hamiltonian Systems from bond graphs. Simulation Modelling Practice and Theory vol. 17 137–151 (2009)](derivation-of-input-state-output-port-hamiltonian-systems-from-bond-graphs) -- [10.1016/j.simpat.2008.02.007](https://doi.org/10.1016/j.simpat.2008.02.007)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Eyisi, E. et al. Model-Based Control Design and Integration of Cyberphysical Systems: An Adaptive Cruise Control Case Study. Journal of Control Science and Engineering vol. 2013 1–15 (2013) -- [10.1155/2013/678016](https://doi.org/10.1155/2013/678016)
- Fujimoto, K. & Sugie, T. Canonical transformation and stabilization of generalized Hamiltonian systems. Systems &amp; Control Letters vol. 42 217–227 (2001) -- [10.1016/s0167-6911(00)00091-8](https://doi.org/10.1016/s0167-6911(00)00091-8)
- Fujimoto, K., Sugie, T.: Freedom in coordinate transformation for exact linearization and its application to transient behavior improvement. In: Proceedings of the 35th IEEE Conference on Decision and Control, pp. 84–89 (1996)
- Generic Modeling Environment.
- G Golo. Golo, G., van der Schaft, A., Beedveld, P., Mascheke, B.: Hamiltonian formulation of bond graphs. In: Johansson, R., Rantzer, A. (eds.) Nonlinear and Hybrid Systems in Automotive Control, pp. 351–372. Springer, London (2003) (2003)
- R Hooke. Hooke, R., Jeeves, T.: Direct search solution of numerical and statistical problems. J. Assoc. Comput. Mach. 7, 212–229 (1969) (1969)
- Jiyang, K.K., Kum, K., Kang, J., Sung, W.: A floating-point to fixed-point C converter for fixed-point digital signal processors. In: Second SUIF Compiler Workshop (1997)
- Karsai, G., Sztipanovits, J., Ledeczi, A. & Bapty, T. Model-integrated development of embedded software. Proceedings of the IEEE vol. 91 145–164 (2003) -- [10.1109/jproc.2002.805824](https://doi.org/10.1109/jproc.2002.805824)
- HK Khalil. Khalil, H.K.: Nonlinear Systems, 3rd edn. Prentice Hall, Upper Saddle River (2002). ISBN 0-13-067389-7 (2002)
- Kirschke-Biller, F.: AUTOSAR—a global standard. In: 4th AUTOSAR Open Conference, Paris, France (June 11, 2012)
- Lee, E. A. Cyber Physical Systems: Design Challenges. 2008 11th IEEE International Symposium on Object and Component-Oriented Real-Time Distributed Computing (ISORC) 363–369 (2008) doi:10.1109/isorc.2008.25 -- [10.1109/isorc.2008.25](https://doi.org/10.1109/isorc.2008.25)
- MATLAB, Version 7.10.0 (R2010a). The Mathworks Inc., Natick (2010)
- Oishi, Y. Passivity degradation under the discretization with the zero-order hold and the ideal sampler. 49th IEEE Conference on Decision and Control (CDC) 7613–7617 (2010) doi:10.1109/cdc.2010.5717886 -- [10.1109/cdc.2010.5717886](https://doi.org/10.1109/cdc.2010.5717886)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Ortega, R., Jiang, Z. P. & Hill, D. J. Passivity-based control of nonlinear systems: a tutorial. Proceedings of the 1997 American Control Conference (Cat. No.97CH36041) 2633–2637 vol.5 (1997) doi:10.1109/acc.1997.611933 -- [10.1109/acc.1997.611933](https://doi.org/10.1109/acc.1997.611933)
- Porter, J., Hemingway, G., Nine, H., et al.: The ESMoL language and tools for high-confidence distributed control systems design—part 1: language, framework, and analysis. Technical report ISIS-10-109, Vanderbilt University (2010)
- Porter, J., Karsai, G. & Sztipanovits, J. Towards a time-triggered schedule calculation tool to support model-based embedded software design. Proceedings of the seventh ACM international conference on Embedded software 167–176 (2009) doi:10.1145/1629335.1629358 -- [10.1145/1629335.1629358](https://doi.org/10.1145/1629335.1629358)
- R Rajamani. Rajamani, R.: Vehicle Dynamics and Control. Springer, Berlin (2006). ISBN:978-0-387-26396-0 (2006)
- [Sakai, S. & Stramigioli, S. Port-Hamiltonian approaches to motion generation for mechanical systems. Proceedings 2007 IEEE International Conference on Robotics and Automation 1948–1953 (2007) doi:10.1109/robot.2007.363607](port-hamiltonian-approaches-to-motion-generation-for-mechanical-systems) -- [10.1109/robot.2007.363607](https://doi.org/10.1109/robot.2007.363607)
- G Simko. Simko, G., Levendovsky, T., Maroti, M., Sztipanovits, J.: Towards a Theory of Cyber-Physical Systems Modeling. CyPhy, Philadelphia (2013) (2013)
- [Stramigioli, S., Secchi, C., van der Schaft, A. J. & Fantuzzi, C. Sampled data systems passivity and discrete port-Hamiltonian systems. IEEE Transactions on Robotics vol. 21 574–587 (2005)](sampled-data-systems-passivity-and-discrete-port-hamiltonian-systems) -- [10.1109/tro.2004.842330](https://doi.org/10.1109/tro.2004.842330)
- Sztipanovits, J. Composition of Cyber-Physical Systems. 14th Annual IEEE International Conference and Workshops on the Engineering of Computer-Based Systems (ECBS’07) 3–6 (2007) doi:10.1109/ecbs.2007.25 -- [10.1109/ecbs.2007.25](https://doi.org/10.1109/ecbs.2007.25)
- Sztipanovits, J. et al. Toward a Science of Cyber–Physical System Integration. Proceedings of the IEEE vol. 100 29–44 (2012) -- [10.1109/jproc.2011.2161529](https://doi.org/10.1109/jproc.2011.2161529)
- TTEthernet.
- Van der schaft, A. J. & Maschke, B. M. Mathematical Modeling of Constrained Hamiltonian Systems. IFAC Proceedings Volumes vol. 28 637–642 (1995) -- [10.1016/s1474-6670(17)46900-x](https://doi.org/10.1016/s1474-6670(17)46900-x)
- van der Schaft, A.: Port-Hamiltonian systems: an introductory survey. In: Proceedings of the International Congress of Mathematicians (2006)
- van der Schaft, A.: Port-Hamiltonian systems: network modeling and control of nonlinear physical systems. In: Advanced Dynamics and Control of Structures, pp. 127–167, Springer, Vienna (2004). ISBN: 978-3-7091-2774-2
- Wu, P., McCourt, M., Antsaklis, P.J.: Experimentally determining passivity indices: theory and simulation. Technical report of the ISIS Group (2013)
- Yu, H. & Antsaklis, P. J. A passivity measure of systems in cascade based on passivity indices. 49th IEEE Conference on Decision and Control (CDC) 2186–2191 (2010) doi:10.1109/cdc.2010.5717648 -- [10.1109/cdc.2010.5717648](https://doi.org/10.1109/cdc.2010.5717648)
- Zhang, Z. et al. Co-simulation framework for design of time-triggered cyber physical systems. Proceedings of the ACM/IEEE 4th International Conference on Cyber-Physical Systems 119–128 (2013) doi:10.1145/2502524.2502541 -- [10.1145/2502524.2502541](https://doi.org/10.1145/2502524.2502541)
- Zhao, J. & Hill, D. J. Dissipativity Theory for Switched Systems. IEEE Transactions on Automatic Control vol. 53 941–953 (2008) -- [10.1109/tac.2008.920237](https://doi.org/10.1109/tac.2008.920237)
- Zhu, F., Yu, H., McCourt, M. J. & Antsaklis, P. J. Passivity and stability of switched systems under quantization. Proceedings of the 15th ACM international conference on Hybrid Systems: Computation and Control 237–244 (2012) doi:10.1145/2185632.2185668 -- [10.1145/2185632.2185668](https://doi.org/10.1145/2185632.2185668)

