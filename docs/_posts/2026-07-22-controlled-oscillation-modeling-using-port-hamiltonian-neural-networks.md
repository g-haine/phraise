---
title: "Controlled oscillation modeling using port-Hamiltonian neural networks"
date: 2026-07-22 00:00:00 +0100
permalink: controlled-oscillation-modeling-using-port-hamiltonian-neural-networks
year: 2026
authors: M. Linares, G. Doras, T. Hélie, A. Roebel
category: articles
tags:
  - discrete gradient, jacobian regularization, physics-informed machine learning, port-hamiltonian neural networks
---
 
## Authors
[M. Linares](authors/m-linares), [G. Doras](authors/g-doras), [T. Hélie](authors/thomas-helie), [A. Roebel](authors/a-roebel)
 
## Abstract
Learning dynamical systems through purely data-driven methods is challenging as they do not learn the underlying conservation laws that enable them to correctly generalize. Existing port-Hamiltonian neural network methods have recently been successfully applied for modeling mechanical systems. However, even though these methods are designed on power-balance principles, they usually do not consider power-preserving discretizations and often rely on Runge-Kutta numerical methods. In this work, we propose to use a second-order discrete gradient method embedded in the learning of dynamical systems with port-Hamiltonian neural networks. Numerical results are provided for three systems deliberately selected to span different ranges of dynamical behavior under control: a baseline harmonic oscillator with quadratic energy storage; a Duffing oscillator, with a non-quadratic Hamiltonian offering amplitude-dependent effects; and a self-sustained oscillator, which can stabilize in a controlled limit cycle through the incorporation of a nonlinear dissipation. We show how the use of this discrete gradient method outperforms the performance of a Runge-Kutta method of the same order. Experiments are also carried out to compare two theoretically equivalent port-Hamiltonian systems formulations and to analyze the impact of regularizing the Jacobian of port-Hamiltonian neural networks during training.
 
## Keywords
discrete gradient, jacobian regularization, physics-informed machine learning, port-hamiltonian neural networks
 
## Citation
- **Journal:** Physica D: Nonlinear Phenomena
- **Year:** 2026
- **Volume:** 497
- **Issue:** 
- **Pages:** 135341
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.physd.2026.135341](https://doi.org/10.1016/j.physd.2026.135341)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Linares_2026,
  title={{Controlled oscillation modeling using port-Hamiltonian neural networks}},
  volume={497},
  ISSN={0167-2789},
  DOI={10.1016/j.physd.2026.135341},
  journal={Physica D: Nonlinear Phenomena},
  publisher={Elsevier BV},
  author={Linares, M. and Doras, G. and Hélie, T. and Roebel, A.},
  year={2026},
  pages={135341}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/controlled-oscillation-modeling-using-port-hamiltonian-neural-networks.bib)
 
## References
- Cicirello A (2024) Physics-Enhanced Machine Learning: a position paper for dynamical systems investigations. J Phys: Conf Ser 2909(1):012034. https://doi.org/10.1088/1742-6596/2909/1/01203 -- [10.1088/1742-6596/2909/1/012034](https://doi.org/10.1088/1742-6596/2909/1/012034)
- Baxter J (2000) A Model of Inductive Bias Learning. jair 12:149–198. https://doi.org/10.1613/jair.73 -- [10.1613/jair.731](https://doi.org/10.1613/jair.731)
- Karniadakis GE, Kevrekidis IG, Lu L, Perdikaris P, Wang S, Yang L (2021) Physics-informed machine learning. Nat Rev Phys 3(6):422–440. https://doi.org/10.1038/s42254-021-00314- -- [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5)
- [Eidnes S, Stasik AJ, Sterud C, Bøhn E, Riemer-Sørensen S (2023) Pseudo-Hamiltonian neural networks with state-dependent external forces. Physica D: Nonlinear Phenomena 446:133673. https://doi.org/10.1016/j.physd.2023.13367](pseudo-hamiltonian-neural-networks-with-state-dependent-external-forces) -- [10.1016/j.physd.2023.133673](https://doi.org/10.1016/j.physd.2023.133673)
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.04 -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Meng C, Griesemer S, Cao D, Seo S, Liu Y (2025) When physics meets machine learning: a survey of physics-informed machine learning. Mach Learn Comput Sci Eng 1(1). https://doi.org/10.1007/s44379-025-00016- -- [10.1007/s44379-025-00016-0](https://doi.org/10.1007/s44379-025-00016-0)
- Khalil, (2002)
- Taylor, (2005)
- [Maschke BM, Van Der Schaft AJ, Breedveld PC (1992) An intrinsic hamiltonian formulation of network dynamics: non-standard poisson structures and gyrators. Journal of the Franklin Institute 329(5):923–966. https://doi.org/10.1016/s0016-0032(92)90049-](an-intrinsic-hamiltonian-formulation-of-network-dynamics-non-standard-poisson-structures-and-gyrators) -- [10.1016/s0016-0032(92)90049-m](https://doi.org/10.1016/s0016-0032(92)90049-m)
- Duindam, (2009)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Chaigne, (2016)
- [Aoues S, Cardoso-Ribeiro FL, Matignon D, Alazard D (2019) Modeling and Control of a Rotating Flexible Spacecraft: A Port-Hamiltonian Approach. IEEE Trans Contr Syst Technol 27(1):355–362. https://doi.org/10.1109/tcst.2017.277124](modeling-and-control-of-a-rotating-flexible-spacecraft-a-port-hamiltonian-approach) -- [10.1109/tcst.2017.2771244](https://doi.org/10.1109/tcst.2017.2771244)
- [Cardoso-Ribeiro FL, Haine G, Le Gorrec Y, Matignon D, Ramirez H (2024) Port-Hamiltonian formulations for the modeling, simulation and control of fluids. Computers &amp; Fluids 283:106407. https://doi.org/10.1016/j.compfluid.2024.10640](port-hamiltonian-formulations-for-the-modeling-simulation-and-control-of-fluids) -- [10.1016/j.compfluid.2024.106407](https://doi.org/10.1016/j.compfluid.2024.106407)
- Roze, Time-space formulation of a conservative string subject to finite transformations. IFAC-Pap. (2024)
- Hairer, Geometric Numerical Integration. (2006)
- Quispel GRW, Turner GS (1996) Discrete gradient methods for solving ODEs numerically while preserving a first integral. J Phys A: Math Gen 29(13):L341–L349. https://doi.org/10.1088/0305-4470/29/13/00 -- [10.1088/0305-4470/29/13/006](https://doi.org/10.1088/0305-4470/29/13/006)
- [Gonzalez O (1996) Time integration and discrete Hamiltonian systems. J Nonlinear Sci 6(5):449–467. https://doi.org/10.1007/bf0244016](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- Celledoni E, Eidnes S, Myhr HN (2025) Learning dynamical systems from noisy data with inverse-explicit integrators. Physica D: Nonlinear Phenomena 472:134471. https://doi.org/10.1016/j.physd.2024.13447 -- [10.1016/j.physd.2024.134471](https://doi.org/10.1016/j.physd.2024.134471)
- Chang, Reversible architectures for arbitrarily deep residual neural networks. (2018)
- Chen, Neural ordinary differential equations. (2018)
- Dupont, Augmented neural ODEs. (2019)
- Li Deng (2012) The MNIST Database of Handwritten Digit Images for Machine Learning Research [Best of the Web]. IEEE Signal Process Mag 29(6):141–142. https://doi.org/10.1109/msp.2012.221147 -- [10.1109/msp.2012.2211477](https://doi.org/10.1109/msp.2012.2211477)
- Finlay, How to train your neural ODE: the world of Jacobian and kinetic regularization. (2020)
- Josias, Jacobian norm regularisation and conditioning in neural ODEs. (2022)
- Takeru, Spectral normalization for generative adversarial networks. (2018)
- Greydanus, Hamiltonian neural networks. Adv. Neural Inf. Process. Syst. (2019)
- [Desai SA, Mattheakis M, Sondak D, Protopapas P, Roberts SJ (2021) Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Phys Rev E 104(3). https://doi.org/10.1103/physreve.104.03431](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Cherifi K, El Messaoudi A, Gernandt H, Roschkowski M (2025) Nonlinear Port-Hamiltonian System Identification from Input-State-Output Dat -- [10.2139/ssrn.5097694](https://doi.org/10.2139/ssrn.5097694)
- [Roth FJ, Klein DK, Kannapinn M, Peters J, Weeger O (2025) Stable Port-Hamiltonian Neural Networks. Advances in Neural Information Processing Systems 38 56483–5650](stable-port-hamiltonian-neural-networks) -- [10.52202/085713-1693](https://doi.org/10.52202/085713-1693)
- DiPietro, Sparse symplectically integrated neural networks. Adv. Neural Inf. Process. Syst. (2020)
- Van der Schaft, (2000)
- Muller, Power-balanced modelling of circuits as skew gradient systems. (2018)
- Press, (2007)
- [Schwerdtner P, Moser T, Mehrmann V, Voigt M (2023) Optimization-based model order reduction of port-Hamiltonian descriptor systems. Systems &amp; Control Letters 182:105655. https://doi.org/10.1016/j.sysconle.2023.10565](optimization-based-model-order-reduction-of-port-hamiltonian-descriptor-systems) -- [10.1016/j.sysconle.2023.105655](https://doi.org/10.1016/j.sysconle.2023.105655)
- Zhu, On numerical integration in neural ordinary differential equations. (2022)
- Neary, Compositional learning of dynamical system models using port-Hamiltonian neural networks. (2023)
- Hélie, Modèle passif minimal d’instrument musical auto-oscillant à configuration variable en temps. (2025)
- Ortega, Energy shaping control revisited. (2007)
- Eidnes S, Lye KO (2024) Pseudo-Hamiltonian neural networks for learning partial differential equations. Journal of Computational Physics 500:112738. https://doi.org/10.1016/j.jcp.2023.11273 -- [10.1016/j.jcp.2023.112738](https://doi.org/10.1016/j.jcp.2023.112738)
- Lopes, (2016)
- Hadamard, Sur les problèmes aux dérivées partielles et leur signification physique. Princet. Univ. Bull. (1902)
- Hirsch, (1974)
- Golub, Matrix Computations. (2013)
- Trefethen, (1997)
- Iserles, A First Course in the Numerical Analysis of Differential Equations. (2009)
- Strogatz, (2024)

