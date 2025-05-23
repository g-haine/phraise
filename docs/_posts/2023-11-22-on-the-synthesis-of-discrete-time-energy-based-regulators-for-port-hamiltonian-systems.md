---
layout: post
title: "On the Synthesis of Discrete-time Energy-based Regulators for Port-Hamiltonian Systems"
date: 2023-11-22 00:00:00 +0100
permalink: on-the-synthesis-of-discrete-time-energy-based-regulators-for-port-hamiltonian-systems
year: 2023
authors: Alessandro Macchelli
category: proceedings
tags:
  - sampled-data control
  - passivity-based control
  - digital implementation
  - port-Hamiltonian systems
---
 
## Authors
[Alessandro Macchelli](authors/alessandro-macchelli)
 
## Abstract
This paper aims at describing a synthesis procedure of discrete-time, energy-based regulators for continuous-time port-Hamiltonian systems. The methodology consists of three steps. The first twos deal with the definition of a discrete-time approximation of the plant to be successively employed in the development of the control law. Here, the focus is mainly on the last step, i.e. on how to interconnect digital controller and plant. The coupling is implemented via a zero-order hold and relies on the solution of an optimisation problem that determines the “best” and “minimal” correction to be applied to the nominal action to achieve the same performances obtained when the regulator is in closed-loop with the discrete-time model of the plant. This is the reference scenario used by the designer to develop and tune the control law. The procedure (time-discretisation, control design and coupling implementation) is illustrated in an example.
 
## Keywords
sampled-data control; passivity-based control; digital implementation; port-Hamiltonian systems
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2023
- **Volume:** 56
- **Issue:** 2
- **Pages:** 2889--2894
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2023.10.1407](https://doi.org/10.1016/j.ifacol.2023.10.1407)
- **Note:** 22nd IFAC World Congress- Yokohama, Japan, July 9-14, 2023
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Macchelli_2023,
  title={{On the Synthesis of Discrete-time Energy-based Regulators for Port-Hamiltonian Systems}},
  volume={56},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2023.10.1407},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Macchelli, Alessandro},
  year={2023},
  pages={2889--2894}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-the-synthesis-of-discrete-time-energy-based-regulators-for-port-hamiltonian-systems.bib)
 
## References
- [Aoues, S., Di Loreto, M., Eberard, D. & Marquis-Favre, W. Hamiltonian systems discrete-time approximation: Losslessness, passivity and composability. Systems &amp; Control Letters vol. 110 9–14 (2017)](hamiltonian-systems-discrete-time-approximation-losslessness-passivity-and-composability) -- [10.1016/j.sysconle.2017.10.003](https://doi.org/10.1016/j.sysconle.2017.10.003)
- Aoues, Discrete IDA-PBC control law for Newtonian mechanical port-Hamiltonian systems. (2015)
- Celledoni, Energy-preserving and passivity-consistent numerical discretization of port-Hamiltonian systems. arXiv:1706.08621 (2017)
- Costa-Castelló, R. & Fossas, E. On Preserving Passivity in Sampled-data Linear Systems. European Journal of Control vol. 13 583–590 (2007) -- [10.3166/ejc.13.583-590](https://doi.org/10.3166/ejc.13.583-590)
- Ehrhardt, A geometric integration approach to smooth optimisation: Foundations of the discrete gradient method. arXiv:1805.06444 (2020)
- Fujimoto, K. & Sugie, T. Canonical transformation and stabilization of generalized Hamiltonian systems. Systems &amp; Control Letters vol. 42 217–227 (2001) -- [10.1016/s0167-6911(00)00091-8](https://doi.org/10.1016/s0167-6911(00)00091-8)
- [Gonzalez, O. Time integration and discrete Hamiltonian systems. Journal of Nonlinear Science vol. 6 449–467 (1996)](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- Gonzalez, O. & Simo, J. C. On the stability of symplectic and energy-momentum algorithms for non-linear Hamiltonian systems with symmetry. Computer Methods in Applied Mechanics and Engineering vol. 134 197–222 (1996) -- [10.1016/0045-7825(96)01009-2](https://doi.org/10.1016/0045-7825(96)01009-2)
- Gören-Sümer, Gradient based discrete-time modeling and control of Hamiltonian systems. (2008)
- Gören-Sümer, A direct discrete-time IDA-PBC design method for a class of underactuated Hamiltonian systems. (2011)
- Harten, A., Lax, P. D. & Leer, B. van. On Upstream Differencing and Godunov-Type Schemes for Hyperbolic Conservation Laws. SIAM Review vol. 25 35–61 (1983) -- [10.1137/1025002](https://doi.org/10.1137/1025002)
- Khalil, (1996)
- Kotyczka, Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems & Control Letters (2019)
- [Kotyczka, P. & Thoma, T. Symplectic discrete-time energy-based control for nonlinear mechanical systems. Automatica vol. 133 109842 (2021)](symplectic-discrete-time-energy-based-control-for-nonlinear-mechanical-systems) -- [10.1016/j.automatica.2021.109842](https://doi.org/10.1016/j.automatica.2021.109842)
- [Macchelli, A. Trajectory Tracking for Discrete-Time Port-Hamiltonian Systems. IEEE Control Systems Letters vol. 6 3146–3151 (2022)](trajectory-tracking-for-discrete-time-port-hamiltonian-systems) -- [10.1109/lcsys.2022.3182845](https://doi.org/10.1109/lcsys.2022.3182845)
- Marsden, J. E. & West, M. Discrete mechanics and variational integrators. Acta Numerica vol. 10 357–514 (2001) -- [10.1017/s096249290100006x](https://doi.org/10.1017/s096249290100006x)
- Monaco, Nonlinear port controlled Hamiltonian systems under sampling. In Decision and Control. (2009)
- [Moreschini, A., Mattioni, M., Monaco, S. & Normand-Cyrot, D. Stabilization of Discrete Port-Hamiltonian Dynamics via Interconnection and Damping Assignment. IEEE Control Systems Letters vol. 5 103–108 (2021)](stabilization-of-discrete-port-hamiltonian-dynamics-via-interconnection-and-damping-assignment) -- [10.1109/lcsys.2020.3000705](https://doi.org/10.1109/lcsys.2020.3000705)
- Ortega, Putting energy back in control. Control Systems Magazine (2001)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Quispel, G. R. W. & Turner, G. S. Discrete gradient methods for solving ODEs numerically while preserving a first integral. Journal of Physics A: Mathematical and General vol. 29 L341–L349 (1996) -- [10.1088/0305-4470/29/13/006](https://doi.org/10.1088/0305-4470/29/13/006)
- Stramigioli, Sampled data systems passivity and discrete port-Hamiltonian systems. IEEE Transactions on (2005)
- [van der Schaft, A. L2-Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer International Publishing, 2017). doi:10.1007/978-3-319-49992-5](l2-gain-and-passivity-techniques-in-nonlinear-control) -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)

