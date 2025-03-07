---
layout: post
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
[Siyuan Dai](authors/siyuan_dai), [Zhenkai Zhang](authors/zhenkai_zhang), [Xenofon Koutsoukos](authors/xenofon_koutsoukos)
 
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
 
## References
- Byrnes, C., Lin, W.: Losslessness, feedback equivalence, and the global stabilization of discrete-time nonlinear systems. IEEE Trans. Autom. Control 39(1), 83–98 (1994) -- [10.1109/9.273341](https://doi.org/10.1109/9.273341)
- CarSim: Mechanical: Simulation. Michigan, Ann Arbor (2013)
- [Cervera, J., van der Schaft, A., Baños, A.: Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica 43(2), 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- Costa-Castello, R., Fossas, E.: On preserving passivity in sampled-data linear systems. In: Proceedings of the 2006 American Control Conference, Minneapolis, USA, pp. 4373–4378 (2006) -- [10.1109/ACC.2006.1657407](https://doi.org/10.1109/ACC.2006.1657407)
- Dai, S.: Compositional modeling and design of cyber-physical systems using port-Hamiltonian systems. Doctoral dissertation, Vanderbilt University. Retrieved from 
 http://etd.library.vanderbilt.edu/available/etd-08042016-123306/unrestricted/Dai.pdf
 
 (2016)
- Dai, S., Koutsoukos, X.: Model-based automotive control design using port-Hamiltonian systems. In: International Conference on Complex Systems Engineering (ICCSE 2015), University of Connecticut, November 9–10 (2015) -- [10.1109/ComplexSys.2015.7385987](https://doi.org/10.1109/ComplexSys.2015.7385987)
- [Dai, S., Koutsoukos, X.: Safety analysis of automotive control systems using multi-modal port-Hamiltonian systems. In: 19th ACM International Conference on Hybrid Systems: Computation and Control (HSCC 2016), Vienna, Austria, April 12–14 (2016)](safety-analysis-of-automotive-control-systems-using-multi-modal-port-hamiltonian-systems) -- [10.1145/2883817.2883845](https://doi.org/10.1145/2883817.2883845)
- Derler, P., et al.: Modeling cyber-physical systems. Proc. IEEE 100(1), 13–28 (2012) -- [10.1109/JPROC.2011.2160929](https://doi.org/10.1109/JPROC.2011.2160929)
- Dirksz, D., Scherpen, J.: Port-Hamiltonian and power-based integral type control of a manipulator system. In: 18th IFAC World Congress, Italy, Milan (2011) -- [10.3182/20110828-6-IT-1002.01030](https://doi.org/10.3182/20110828-6-IT-1002.01030)
- [Donaire, A., Junco, S.: Derivation of input-state-output port-Hamiltonian systems from bond graphs. Simul. Model. Pract. Theory 17, 137–151 (2009)](derivation-of-input-state-output-port-hamiltonian-systems-from-bond-graphs) -- [10.1016/j.simpat.2008.02.007](https://doi.org/10.1016/j.simpat.2008.02.007)
- [Duindam, V., Macchelli, A., Stramigioli, S., Bruyninckx, H.: Modeling and Control of Complex Physical Systems: The Port-Hamiltonian Approach. Springer, Berlin (2009)](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Eyisi, E., Zhang, Z., Koutsoukos, X., Porter, J., Karsai, G., Sztipanovits, J.: Model-based control design and integration of cyber-physical system: an adaptive cruise control case study. J. Control Sci. Eng. 2013, 678016 (2013). 
 https://doi.org/10.1155/2013/678016 -- [10.1155/2013/678016](https://doi.org/10.1155/2013/678016)
- Fujimoto, K., Sugie, T.: Canonical transformation and stabilization of generalized Hamiltonian systems. Syst. Control Lett. 42, 217–227 (2001) -- [10.1016/S0167-6911(00)00091-8](https://doi.org/10.1016/S0167-6911(00)00091-8)
- Fujimoto, K., Sugie, T.: Freedom in coordinate transformation for exact linearization and its application to transient behavior improvement. In: Proceedings of the 35th IEEE Conference on Decision and Control, pp. 84–89 (1996)
- Generic Modeling Environment. 
 http://repo.isis.vanderbilt.edu/downloads?tool=GME
- Golo, G., van der Schaft, A., Beedveld, P., Mascheke, B.: Hamiltonian formulation of bond graphs. In: Johansson, R., Rantzer, A. (eds.) Nonlinear and Hybrid Systems in Automotive Control, pp. 351–372. Springer, London (2003)
- Hooke, R., Jeeves, T.: Direct search solution of numerical and statistical problems. J. Assoc. Comput. Mach. 7, 212–229 (1969)
- Jiyang, K.K., Kum, K., Kang, J., Sung, W.: A floating-point to fixed-point C converter for fixed-point digital signal processors. In: Second SUIF Compiler Workshop (1997)
- Karsai, G., Sztipanovits, J., Ledeczi, A., Bapty, T.: Model-integrated development of embedded software. Proc. IEEE 91, 1 (2003) -- [10.1109/JPROC.2002.805824](https://doi.org/10.1109/JPROC.2002.805824)
- Khalil, H.K.: Nonlinear Systems, 3rd edn. Prentice Hall, Upper Saddle River (2002). ISBN 0-13-067389-7
- Kirschke-Biller, F.: AUTOSAR—a global standard. In: 4th AUTOSAR Open Conference, Paris, France (June 11, 2012)
- Lee, L.: Cyber-physical systems: design challenges. In: International Symposium on Object, Component, and Service-Oriented Real-Time Distributed Computing (ISORC), Orlando. FL, USA (2008) -- [10.1109/ISORC.2008.25](https://doi.org/10.1109/ISORC.2008.25)
- MATLAB, Version 7.10.0 (R2010a). The Mathworks Inc., Natick (2010)
- Oishi, Y.: Passivity degradation under the discretization with the zero-order hold and the ideal sampler. In: 49th IEEE Conference on Decision and Control, December 15–17, Atlanta, GA, USA (2010) -- [10.1109/CDC.2010.5717886](https://doi.org/10.1109/CDC.2010.5717886)
- Ortega, R., Garcia-Canseco, E.: Interconnection and damping assignment passivity-based control: a survey. Eur. J. Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Ortega, R., Jiang, Z.P., Hill, D.J.: Passivity-based control of nonlinear systems: a tutorial. In: Proceedings of the American Control Conference, Albuquerque, NM (1997) -- [10.1109/ACC.1997.611933](https://doi.org/10.1109/ACC.1997.611933)
- Porter, J., Hemingway, G., Nine, H., et al.: The ESMoL language and tools for high-confidence distributed control systems design—part 1: language, framework, and analysis. Technical report ISIS-10-109, Vanderbilt University (2010)
- Porter, J., Karsai, G., Sztipanovits, J.: Towards a time-triggered schedule calculation tool to support model-based embedded software design. In: Proceedings of the Seventh ACM International Conference on Embedded Software, Grenoble, France, October 12–16, pp. 167–176 (2009) -- [10.1145/1629335.1629358](https://doi.org/10.1145/1629335.1629358)
- Rajamani, R.: Vehicle Dynamics and Control. Springer, Berlin (2006). ISBN:978-0-387-26396-0
- [Sakai, S., Stramigioli, S.: Port-Hamiltonian approaches to motion generation for mechanical systems. In: IEEE International Conference on Robotics and Automation, Rome, Italy (2007)](port-hamiltonian-approaches-to-motion-generation-for-mechanical-systems) -- [10.1109/ROBOT.2007.363607](https://doi.org/10.1109/ROBOT.2007.363607)
- Simko, G., Levendovsky, T., Maroti, M., Sztipanovits, J.: Towards a Theory of Cyber-Physical Systems Modeling. CyPhy, Philadelphia (2013)
- [Stramigioli, S., Secchi, C., van der Schaft, A.J., Fantuzzi, C.: Sampled data systems passivity and discrete port-Hamiltonian systems. IEEE Trans. Robot. 21(4), 574–587 (2005)](sampled-data-systems-passivity-and-discrete-port-hamiltonian-systems) -- [10.1109/TRO.2004.842330](https://doi.org/10.1109/TRO.2004.842330)
- Sztipanovits, J.: Composition of cyber-physical systems. In: Proceedings of the 14th Annual IEEE International Conference and Workshops on the Engineering of Computer-Based Systems, Washington, DC, USA (2007) -- [10.1109/ECBS.2007.25](https://doi.org/10.1109/ECBS.2007.25)
- Sztipanovits, J., et al.: Toward a science of cyber-physical system integration. Proc. IEEE 100(1), 29–44 (2012) -- [10.1109/JPROC.2011.2161529](https://doi.org/10.1109/JPROC.2011.2161529)
- TTEthernet. 
 http://www.tttech.com/en/products/ttethernet/
- van der Schaft, A.J., Maschke, B.M.J.: Mathematical modeling of constrained Hamiltonian systems. In: Proceedings of the Third IFAC Symposium on Nonlinear Control Systems (1995) -- [10.1016/S1474-6670(17)46900-X](https://doi.org/10.1016/S1474-6670(17)46900-X)
- van der Schaft, A.: Port-Hamiltonian systems: an introductory survey. In: Proceedings of the International Congress of Mathematicians (2006)
- van der Schaft, A.: Port-Hamiltonian systems: network modeling and control of nonlinear physical systems. In: Advanced Dynamics and Control of Structures, pp. 127–167, Springer, Vienna (2004). ISBN: 978-3-7091-2774-2
- Wu, P., McCourt, M., Antsaklis, P.J.: Experimentally determining passivity indices: theory and simulation. Technical report of the ISIS Group (2013)
- Yu, H., Antsaklis, P.J.: A passivity measure of systems in cascade based on passivity indices. In: 49th IEEE Conference on Decision and Control (2010) -- [10.1109/CDC.2010.5717648](https://doi.org/10.1109/CDC.2010.5717648)
- Zhang, Z., Eyisi, E., Koutsoukos, X., Porter, J., Karsai, G., Sztipanovits, J.: Co-simulation framework for design of time-triggered cyber physical systems. In: Proceedings of the ACM/IEEE 4th International Conference on Cyber-Physical Systems, Philadelphia, PA, USA (2013) -- [10.1145/2502524.2502541](https://doi.org/10.1145/2502524.2502541)
- Zhao, J., Hill, D.J.: Dissipativity theory for switched systems. IEEE Trans. Autom. Control 53(4), 941–953 (2008) -- [10.1109/TAC.2008.920237](https://doi.org/10.1109/TAC.2008.920237)
- Zhu, F., Yu, H., McCourt, M.J., Antsaklis, P.J.: Passivity and stability of switched systems under quantization. In: Conference on Hybrid Systems Computation and Control, April 17–19, Beijing, China (2012) -- [10.1145/2185632.2185668](https://doi.org/10.1145/2185632.2185668)

