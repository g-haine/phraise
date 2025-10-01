---
title: "Pseudo-Hamiltonian neural networks with state-dependent external forces"
date: 2023-02-01 00:00:00 +0100
permalink: pseudo-hamiltonian-neural-networks-with-state-dependent-external-forces
year: 2023
authors: Sølve Eidnes, Alexander J. Stasik, Camilla Sterud, Eivind Bøhn, Signe Riemer-Sørensen
category: articles
tags:
  - Pseudo-Hamiltonian neural networks
  - Physics-informed machine learning
  - Hybrid machine learning
---
 
## Authors
[Sølve Eidnes](authors/solve-eidnes), [Alexander J. Stasik](authors/alexander-j-stasik), [Camilla Sterud](authors/camilla-sterud), [Eivind Bøhn](authors/eivind-bohn), [Signe Riemer-Sørensen](authors/signe-riemer-sorensen)
 
## Abstract
Hybrid machine learning based on Hamiltonian formulations has recently been successfully demonstrated for simple mechanical systems, both energy conserving and not energy conserving. We introduce a pseudo-Hamiltonian formulation that is a generalization of the Hamiltonian formulation via the port-Hamiltonian formulation, and show that pseudo-Hamiltonian neural network models can be used to learn external forces acting on a system. We argue that this property is particularly useful when the external forces are state dependent, in which case it is the pseudo-Hamiltonian structure that facilitates the separation of internal and external forces. Numerical results are provided for a forced and damped mass–spring system and a tank system of higher complexity, and a symmetric fourth-order integration scheme is introduced for improved training on sparse and noisy data.
 
## Keywords
Pseudo-Hamiltonian neural networks; Physics-informed machine learning; Hybrid machine learning
 
## Citation
- **Journal:** Physica D: Nonlinear Phenomena
- **Year:** 2023
- **Volume:** 446
- **Issue:** 
- **Pages:** 133673
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.physd.2023.133673](https://doi.org/10.1016/j.physd.2023.133673)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Eidnes_2023,
  title={{Pseudo-Hamiltonian neural networks with state-dependent external forces}},
  volume={446},
  ISSN={0167-2789},
  DOI={10.1016/j.physd.2023.133673},
  journal={Physica D: Nonlinear Phenomena},
  publisher={Elsevier BV},
  author={Eidnes, Sølve and Stasik, Alexander J. and Sterud, Camilla and Bøhn, Eivind and Riemer-Sørensen, Signe},
  year={2023},
  pages={133673}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/pseudo-hamiltonian-neural-networks-with-state-dependent-external-forces.bib)
 
## References
- Hamilton, On a general method in dynamics. Philos. Trans. R. Soc. (1834)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Greydanus, Hamiltonian neural networks. (2019)
- [Desai, S. A., Mattheakis, M., Sondak, D., Protopapas, P. & Roberts, S. J. Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Physical Review E vol. 104 (2021)](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Duong, Hamiltonian-based neural ODE networks on the SE(3) manifold for dynamics learning and control. (2021)
- Duong, (2021)
- Jin, Learning Poisson systems and trajectories of autonomous systems via Poisson neural networks. IEEE Trans. Neural Netw. Learn. Syst. (2022)
- Chen, Neural symplectic form: Learning Hamiltonian equations on general coordinate systems. Adv. Neural Inf. Process. Syst. (2021)
- Finzi, Simplifying Hamiltonian and Lagrangian neural networks via explicit constraints. Adv. Neural Inf. Process. Syst. (2020)
- Celledoni, E., Leone, A., Murari, D. & Owren, B. Learning Hamiltonians of constrained mechanical systems. Journal of Computational and Applied Mathematics vol. 417 114608 (2023) -- [10.1016/j.cam.2022.114608](https://doi.org/10.1016/j.cam.2022.114608)
- McLachlan, R. I., Quispel, G. R. W. & Robidoux, N. Geometric integration using discrete gradients. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 357 1021–1045 (1999) -- [10.1098/rsta.1999.0363](https://doi.org/10.1098/rsta.1999.0363)
- Van Der Schaft, Port-Hamiltonian systems: an introductory survey. (2006)
- [Beattie, C. A., Mehrmann, V. & Van Dooren, P. Robust port-Hamiltonian representations of passive systems. Automatica vol. 100 182–186 (2019)](robust-port-hamiltonian-representations-of-passive-systems) -- [10.1016/j.automatica.2018.11.013](https://doi.org/10.1016/j.automatica.2018.11.013)
- [Cherifi, K. An overview on recent machine learning techniques for Port Hamiltonian systems. Physica D: Nonlinear Phenomena vol. 411 132620 (2020)](an-overview-on-recent-machine-learning-techniques-for-port-hamiltonian-systems) -- [10.1016/j.physd.2020.132620](https://doi.org/10.1016/j.physd.2020.132620)
- [Benner, P., Goyal, P. & Van Dooren, P. Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters vol. 143 104741 (2020)](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- [Cherifi, K., Goyal, P. & Benner, P. A non-intrusive method to inferring linear port-Hamiltonian realizations using time-domain data. ETNA - Electronic Transactions on Numerical Analysis vol. 56 102–116 (2022)](a-non-intrusive-method-to-inferring-linear-port-hamiltonian-realizations-using-time-domain-data) -- [10.1553/etna_vol56s102](https://doi.org/10.1553/etna_vol56s102)
- Morandin, (2022)
- Grmela, M. & Öttinger, H. C. Dynamics and thermodynamics of complex fluids.  I. Development of a general formalism. Physical Review E vol. 56 6620–6632 (1997) -- [10.1103/physreve.56.6620](https://doi.org/10.1103/physreve.56.6620)
- Öttinger, H. C. & Grmela, M. Dynamics and thermodynamics of complex fluids.  II. Illustrations of a general formalism. Physical Review E vol. 56 6633–6655 (1997) -- [10.1103/physreve.56.6633](https://doi.org/10.1103/physreve.56.6633)
- Zhang, GFINNs: GENERIC formalism informed neural networks for deterministic and stochastic dynamical systems. Philos. Trans. Roy. Soc. A (2022)
- Matsubara, Deep energy-based modeling of discrete-time physics. (2020)
- Kingma, (2014)
- Jin, P., Zhang, Z., Zhu, A., Tang, Y. & Karniadakis, G. E. SympNets: Intrinsic structure-preserving symplectic networks for identifying Hamiltonian systems. Neural Networks vol. 132 166–179 (2020) -- [10.1016/j.neunet.2020.08.017](https://doi.org/10.1016/j.neunet.2020.08.017)
- David, (2021)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM Journal on Control and Optimization vol. 51 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- De Persis, C. & Kallesoe, C. S. Pressure Regulation in Nonlinear Hydraulic Networks by Positive and Quantized Controls. IEEE Transactions on Control Systems Technology vol. 19 1371–1383 (2011) -- [10.1109/tcst.2010.2094619](https://doi.org/10.1109/tcst.2010.2094619)
- Hairer, (2006)
- van Bokhoven, W. M. G. Efficient higher order implicit one-step methods for integration of stiff differential equations. BIT Numerical Mathematics vol. 20 34–43 (1980) -- [10.1007/bf01933583](https://doi.org/10.1007/bf01933583)
- CASH, J. R. & SINGHAL, A. Mono-implicit Runge—Kutta Formulae for the Numerical Integration of Stiff Differential Systems. IMA Journal of Numerical Analysis vol. 2 211–227 (1982) -- [10.1093/imanum/2.2.211](https://doi.org/10.1093/imanum/2.2.211)
- DiPietro, Sparse symplectically integrated neural networks. Adv. Neural Inf. Process. Syst. (2020)
- Desai, S. A., Mattheakis, M. & Roberts, S. J. Variational integrator graph networks for learning energy-conserving dynamical systems. Physical Review E vol. 104 (2021) -- [10.1103/physreve.104.035310](https://doi.org/10.1103/physreve.104.035310)
- Lee, Structure-preserving sparse identification of nonlinear dynamics for data-driven modeling. (2022)
- Cardoso-Ribeiro, Port-Hamiltonian modeling, discretization and feedback control of a circular water tank. (2019)
- [Brugnoli, A., Haine, G., Serhani, A. & Vasseur, X. Numerical Approximation of Port-Hamiltonian Systems for Hyperbolic or Parabolic PDEs with Boundary Control. Journal of Applied Mathematics and Physics vol. 09 1278–1321 (2021)](numerical-approximation-of-port-hamiltonian-systems-for-hyperbolic-or-parabolic-pdes-with-boundary-control) -- [10.4236/jamp.2021.96088](https://doi.org/10.4236/jamp.2021.96088)

