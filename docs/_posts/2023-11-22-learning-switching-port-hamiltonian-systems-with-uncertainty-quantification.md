---
layout: post
title: "Learning Switching Port-Hamiltonian Systems with Uncertainty Quantification"
date: 2023-11-22 00:00:00 +0100
permalink: learning-switching-port-hamiltonian-systems-with-uncertainty-quantification
year: 2023
authors: Thomas Beckers, Tom Z. Jiahao, George J. Pappas
category: proceedings
tags:
  - Bayesian methods
  - Nonparametric methods
  - Grey box modelling
  - Mechatronic systems
  - Uncertainty quantification
---
 
## Authors
[Thomas Beckers](authors/thomas-beckers), [Tom Z. Jiahao](authors/tom-z-jiahao), [George J. Pappas](authors/george-j-pappas)
 
## Abstract
Switching physical systems are ubiquitous in modern control applications, for instance, locomotion behavior of robots and animals, power converters with switches and diodes. The dynamics and switching conditions are often hard to obtain or even inaccessible in case of a-priori unknown environments and nonlinear components. Black-box neural networks can learn to approximately represent switching dynamics, but typically require a large amount of data, neglect the underlying axioms of physics, and lack of uncertainty quantification. We propose a Gaussian process based learning approach enhanced by switching Port-Hamiltonian systems (GP-SPHS) to learn physical plausible system dynamics and identify the switching condition. The Bayesian nature of Gaussian processes uses collected data to form a distribution over all possible switching policies and dynamics that allows for uncertainty quantification. Furthermore, the proposed approach preserves the compositional nature of Port-Hamiltonian systems. A simulation with a hopping robot validates the effectiveness of the proposed approach.
 
## Keywords
Bayesian methods; Nonparametric methods; Grey box modelling; Mechatronic systems; Uncertainty quantification
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2023
- **Volume:** 56
- **Issue:** 2
- **Pages:** 525--532
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2023.10.1621](https://doi.org/10.1016/j.ifacol.2023.10.1621)
- **Note:** 22nd IFAC World Congress- Yokohama, Japan, July 9-14, 2023
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Beckers_2023,
  title={{Learning Switching Port-Hamiltonian Systems with Uncertainty Quantification}},
  volume={56},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2023.10.1621},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Beckers, Thomas and Jiahao, Tom Z. and Pappas, George J.},
  year={2023},
  pages={525--532}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/learning-switching-port-hamiltonian-systems-with-uncertainty-quantification.bib)
 
## References
- Adler, R. J. The Geometry of Random Fields. (2010) doi:10.1137/1.9780898718980 -- [10.1137/1.9780898718980](https://doi.org/10.1137/1.9780898718980)
- Anderson, R. B., Marshall, J. A., L’Afflitto, A. & Dotterweich, J. M. Model Reference Adaptive Control of Switched Dynamical Systems with Applications to Aerial Robotics. Journal of Intelligent &amp; Robotic Systems vol. 100 1265–1281 (2020) -- [10.1007/s10846-020-01260-7](https://doi.org/10.1007/s10846-020-01260-7)
- Beckers, Equilibrium distributions and stability analysis of Gaussian process state space models. (2016)
- Beckers, Gaussian process port-Hamiltonian systems: Bayesian learning with physics prior. (2022)
- Bhouri, Gaussian processes meet NeuralODEs: a Bayesian framework for learning the dynamics of partially observed systems from scarce and noisy data. Philosophical Transactions of the Royal Society A (2022)
- Brogliato, (1999)
- [Cervera, J., van der Schaft, A. J. & Baños, A. Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica vol. 43 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- Chen, Neural ordinary differential equations. Advances in Neural Information Processing Systems (2018)
- [Desai, S. A., Mattheakis, M., Sondak, D., Protopapas, P. & Roberts, S. J. Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Physical Review E vol. 104 (2021)](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Greydanus, Hamiltonian neural networks. Advances in Neural Information Processing Systems (2019)
- Hou, Z.-S. & Wang, Z. From model-based control to data-driven control: Survey, classification and perspective. Information Sciences vol. 235 3–35 (2013) -- [10.1016/j.ins.2012.07.014](https://doi.org/10.1016/j.ins.2012.07.014)
- Jiahao, T. Z., Hsieh, M. A. & Forgoston, E. Knowledge-based learning of nonlinear dynamics and chaos. Chaos: An Interdisciplinary Journal of Nonlinear Science vol. 31 (2021) -- [10.1063/5.0065617](https://doi.org/10.1063/5.0065617)
- Karniadakis, G. E. et al. Physics-informed machine learning. Nature Reviews Physics vol. 3 422–440 (2021) -- [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5)
- Maschke, Port-controlled Hamiltonian systems: modelling origins and systemtheoretic properties. (1993)
- [Nageshrao, S. P., Lopes, G. A. D., Jeltsema, D. & Babuska, R. Port-Hamiltonian Systems in Adaptive and Learning Control: A Survey. IEEE Transactions on Automatic Control vol. 61 1223–1238 (2016)](port-hamiltonian-systems-in-adaptive-and-learning-control-a-survey) -- [10.1109/tac.2015.2458491](https://doi.org/10.1109/tac.2015.2458491)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Rasmussen, (2006)
- Rath, K., Albert, C. G., Bischl, B. & von Toussaint, U. Symplectic Gaussian process regression of maps in Hamiltonian systems. Chaos: An Interdisciplinary Journal of Nonlinear Science vol. 31 (2021) -- [10.1063/5.0048129](https://doi.org/10.1063/5.0048129)
- Ridderbusch, Learning ODE models with qualitative structure using Gaussian processes. (2021)
- Van Der Schaft, A state transfer principle for switching port-Hamiltonian systems. (2009)
- Van der Schaft, (2000)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Williams, C. K. I. & Barber, D. Bayesian classification with Gaussian processes. IEEE Transactions on Pattern Analysis and Machine Intelligence vol. 20 1342–1351 (1998) -- [10.1109/34.735807](https://doi.org/10.1109/34.735807)
- Wilson, Kernel interpolation for scalable structured Gaussian processes (KISS-GP). (2015)
- Wilson, Efficiently sampling functions from Gaussian process posteriors. (2020)
- Wu, X., Zhang, K., Cheng, M. & Xin, X. A switched dynamical system approach towards the economic dispatch of renewable hybrid power systems. International Journal of Electrical Power &amp; Energy Systems vol. 103 440–457 (2018) -- [10.1016/j.ijepes.2018.06.016](https://doi.org/10.1016/j.ijepes.2018.06.016)

