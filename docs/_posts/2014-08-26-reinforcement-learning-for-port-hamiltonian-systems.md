---
layout: post
title: "Reinforcement Learning for Port-Hamiltonian Systems"
date: 2014-08-26 00:00:00 +0100
permalink: reinforcement-learning-for-port-hamiltonian-systems
year: 2015
authors: Olivier Sprangers, Robert Babuska, Subramanya P. Nageshrao, Gabriel A. D. Lopes
category: journal-article
---
 
## Authors
**Olivier Sprangers, Robert Babuska, Subramanya P. Nageshrao, Gabriel A. D. Lopes**
 
## Abstract
Passivity-based control (PBC) for port-Hamiltonian systems provides an intuitive way of achieving stabilization by rendering a system passive with respect to a desired storage function. However, in most instances the control law is obtained without any performance considerations and it has to be calculated by solving a complex partial differential equation (PDE). In order to address these issues we introduce a reinforcement learning (RL) approach into the energy-balancing passivity-based control (EB-PBC) method, which is a form of PBC in which the closed-loop energy is equal to the difference between the stored and supplied energies. We propose a technique to parameterize EB-PBC that preserves the systems's PDE matching conditions, does not require the specification of a global desired Hamiltonian, includes performance criteria, and is robust. The parameters of the control law are found by using actor-critic (AC) RL, enabling the search for near-optimal control policies satisfying a desired closed-loop energy landscape. The advantage is that the solutions learned can be interpreted in terms of energy shaping and damping injection, which makes it possible to numerically assess stability using passivity theory. From the RL perspective, our proposal allows for the class of port-Hamiltonian systems to be incorporated in the AC framework, speeding up the learning thanks to the resulting parameterization of the policy. The method has been successfully applied to the pendulum swing-up problem in simulations and real-life experiments.
 
## Citation
- **Journal:** IEEE Transactions on Cybernetics
- **Year:** 2015
- **Volume:** 45
- **Issue:** 5
- **Pages:** 1017--1027
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/TCYB.2014.2343194](https://doi.org/10.1109/TCYB.2014.2343194)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Sprangers_2015,
  title={{Reinforcement Learning for Port-Hamiltonian Systems}},
  volume={45},
  ISSN={2168-2275},
  DOI={10.1109/tcyb.2014.2343194},
  number={5},
  journal={IEEE Transactions on Cybernetics},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Sprangers, Olivier and Babuska, Robert and Nageshrao, Subramanya P. and Lopes, Gabriel A. D.},
  year={2015},
  pages={1017--1027}
}
{% endraw %}
{% endhighlight %}
 
## References
- [10.1016/j.automatica.2010.08.001](https://doi.org/10.1016/j.automatica.2010.08.001)
- [10.1016/j.automatica.2007.10.040](https://doi.org/10.1016/j.automatica.2007.10.040)
- [10.1109/87.748155](https://doi.org/10.1109/87.748155)
- [10.1109/TAC.2003.817908](https://doi.org/10.1109/TAC.2003.817908)
- [10.1109/ACC.2009.5160232](https://doi.org/10.1109/ACC.2009.5160232)
- [10.1002/acs.714](https://doi.org/10.1002/acs.714)
- [10.1109/TIE.2013.2273477](https://doi.org/10.1109/TIE.2013.2273477)
- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [10.3182/20120829-3-IT-4022.00046](https://doi.org/10.3182/20120829-3-IT-4022.00046)
- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- [10.1137/S0363012901385691](https://doi.org/10.1137/S0363012901385691)
- [Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/TAC.2008.2006930](https://doi.org/10.1109/TAC.2008.2006930)
- [10.1109/TSMCB.2011.2170565](https://doi.org/10.1109/TSMCB.2011.2170565)
- [10.1016/0005-1098(89)90054-X](https://doi.org/10.1016/0005-1098(89)90054-X)
- [10.1109/CDC.2012.6426427](https://doi.org/10.1109/CDC.2012.6426427)
- [10.1016/0034-4877(94)90038-8](https://doi.org/10.1016/0034-4877(94)90038-8)
- [10.1109/TSMCC.2012.2218595](https://doi.org/10.1109/TSMCC.2012.2218595)
- [10.1109/TSMC.1983.6313077](https://doi.org/10.1109/TSMC.1983.6313077)

