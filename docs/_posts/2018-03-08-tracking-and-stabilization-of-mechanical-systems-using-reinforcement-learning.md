---
layout: post
title: "Tracking and stabilization of mechanical systems using reinforcement learning"
date: 2018-03-08 00:00:00 +0100
permalink: tracking-and-stabilization-of-mechanical-systems-using-reinforcement-learning
year: 2018
authors: S Bhuvaneswari, Ramkrishna Pasumarthy, Balaraman Ravindran, Arun D. Mahindrakar
category: proceedings
---
 
## Authors
[S Bhuvaneswari](authors/s-bhuvaneswari), [Ramkrishna Pasumarthy](authors/ramkrishna-pasumarthy), [Balaraman Ravindran](authors/balaraman-ravindran), [Arun D. Mahindrakar](authors/arun-d-mahindrakar)
 
## Abstract
The Interconnection and Damping Assignment Passivity Based Control (IDA-PBC) is a well-known method for control of complex physical systems in the port-Hamiltonian framework. Improvising on top of IDA-PBC which just focuses on stability, the memristive port-Hamiltonian control addresses performance concerns in the control task by providing a state-modulated damping term to IDA-PBC via a memristor element. The control way of implementing the memristive IDA-PBC first requires solving a set of Partial Differential Equations (PDEs) and then choosing a suitable memristance function for the system, out of which the former is a challenging math problem and the latter is a design problem. This paper employs reinforcement learning to learn the memristive IDA-PBC law and in the process, avoids the challenging task of solving PDEs, automates the design of the memristance function and also respects some physical system-level constraints which are not accounted for by the control way of solving IDA-PBC.
 
## Citation
- **Journal:** 2018 Indian Control Conference (ICC)
- **Year:** 2018
- **Volume:** 
- **Issue:** 
- **Pages:** 206--211
- **Publisher:** IEEE
- **DOI:** [10.1109/indiancc.2018.8307979](https://doi.org/10.1109/indiancc.2018.8307979)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Bhuvaneswari_2018,
  title={{Tracking and stabilization of mechanical systems using reinforcement learning}},
  DOI={10.1109/indiancc.2018.8307979},
  booktitle={{2018 Indian Control Conference (ICC)}},
  publisher={IEEE},
  author={Bhuvaneswari, S and Pasumarthy, Ramkrishna and Ravindran, Balaraman and Mahindrakar, Arun D.},
  year={2018},
  pages={206--211}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/tracking-and-stabilization-of-mechanical-systems-using-reinforcement-learning.bib)
 
## References
- sutton, Introduction to Reinforcement Learning (1998)
- Reinforcement learning is direct adaptive optimal control. IEEE Control Syst. 12, 19–22 (1992) -- [10.1109/37.126844](https://doi.org/10.1109/37.126844)
- konidaris, Value function approximation in reinforcement learning using the fourier basis. Twenty-Fifth AAAI Conference on Artificial Intelligence (0)
- [Nageshrao, S. P., Lopes, G. A. D., Jeltsema, D. & Babuška, R. Passivity-based reinforcement learning control of a 2-DOF manipulator arm. Mechatronics 24, 1001–1007 (2014)](passivity-based-reinforcement-learning-control-of-a-2-dof-manipulator-arm) -- [10.1016/j.mechatronics.2014.10.005](https://doi.org/10.1016/j.mechatronics.2014.10.005)
- Feedback instruments user manual (0)
- [Sprangers, O., Babuska, R., Nageshrao, S. P. & Lopes, G. A. D. Reinforcement Learning for Port-Hamiltonian Systems. IEEE Trans. Cybern. 45, 1017–1027 (2015)](reinforcement-learning-for-port-hamiltonian-systems) -- [10.1109/tcyb.2014.2343194](https://doi.org/10.1109/tcyb.2014.2343194)
- ekbote, Sliding Mode control of a Twin Rotor Multiple Input Multiple Output system. Project M report (2010)
- pasumarthy, Energy and power based perspective of memristive controllers. Decision and Control (CDC) 2013 IEEE 52nd Annual Conference on (0)
- [Dòria-Cerezo, A., van der Heijden, L. & Scherpen, J. M. A. Memristive port-Hamiltonian control: Path-dependent damping injection in control of mechanical systems. European Journal of Control 19, 454–460 (2013)](memristive-port-hamiltonian-control-path-dependent-damping-injection-in-control-of-mechanical-systems) -- [10.1016/j.ejcon.2013.09.006](https://doi.org/10.1016/j.ejcon.2013.09.006)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Acosta, J. A., Ortega, R., Astolfi, A. & Mahindrakar, A. D. Interconnection and damping assignment passivity-based control of mechanical systems with underactuation degree one. IEEE Trans. Automat. Contr. 50, 1936–1955 (2005) -- [10.1109/tac.2005.860292](https://doi.org/10.1109/tac.2005.860292)
- gomez-estern, Stabilization of a class of underactuated mechanical systems via total energy shaping. Decision and Control 2001 Proceedings of the 40th IEEE Conference on (2001)

