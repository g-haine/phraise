---
layout: post
title: "Learning the Optimal Energy-based Control Strategy for Port-Hamiltonian Systems"
date: 2024-09-25 00:00:00 +0100
permalink: learning-the-optimal-energy-based-control-strategy-for-port-hamiltonian-systems
year: 2024
authors: Riccardo Zanella, Alessandro Macchelli, Stefano Stramigioli
category: proceedings
tags:
  - port-Hamiltonian systems
  - passivity-based control
  - reinforcement learning
---
 
## Authors
[Riccardo Zanella](authors/riccardo-zanella), [Alessandro Macchelli](authors/alessandro-macchelli), [Stefano Stramigioli](authors/stefano-stramigioli)
 
## Abstract
This paper describes a synthesis and tuning procedure of discrete-time, energy-based regulators for port-Hamiltonian systems. Based on a discrete-time approximation of the plant, the control system is designed within the energy-shaping plus damping injection paradigm. This approach guarantees asymptotic stability, but it is not able “as is” to meet other requirements, such as task performance optimisation. The contribution is integrating the power of artificial neural networks as parametric function approximators and passivity-based control to enhance the performance of an asymptotically stable controlled system. The idea is to employ artificial neural networks that are optimally shaped to enhance the performances during task execution through the solution of an optimisation problem.
 
## Keywords
port-Hamiltonian systems; passivity-based control; reinforcement learning
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2024
- **Volume:** 58
- **Issue:** 6
- **Pages:** 208--213
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2024.08.282](https://doi.org/10.1016/j.ifacol.2024.08.282)
- **Note:** 8th IFAC Workshop on Lagrangian and Hamiltonian Methods for Nonlinear Control LHMNC 2024- Besançon, France, June 10 – 12, 2024
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Zanella_2024,
  title={{Learning the Optimal Energy-based Control Strategy for Port-Hamiltonian Systems}},
  volume={58},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2024.08.282},
  number={6},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Zanella, Riccardo and Macchelli, Alessandro and Stramigioli, Stefano},
  year={2024},
  pages={208--213}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/learning-the-optimal-energy-based-control-strategy-for-port-hamiltonian-systems.bib)
 
## References
- [Aoues, S., Di Loreto, M., Eberard, D. & Marquis-Favre, W. Hamiltonian systems discrete-time approximation: Losslessness, passivity and composability. Systems &amp; Control Letters vol. 110 9–14 (2017)](hamiltonian-systems-discrete-time-approximation-losslessness-passivity-and-composability) -- [10.1016/j.sysconle.2017.10.003](https://doi.org/10.1016/j.sysconle.2017.10.003)
- Baydin, Automatic differentiation n machine learning: A survey. Journal of Marchine Learning Research (2018)
- Fujimoto, K. & Sugie, T. Canonical transformation and stabilization of generalized Hamiltonian systems. Systems &amp; Control Letters vol. 42 217–227 (2001) -- [10.1016/s0167-6911(00)00091-8](https://doi.org/10.1016/s0167-6911(00)00091-8)
- [Gonzalez, O. Time integration and discrete Hamiltonian systems. Journal of Nonlinear Science vol. 6 449–467 (1996)](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- Gören-Sümer, (2008)
- Harten, A., Lax, P. D. & Leer, B. van. On Upstream Differencing and Godunov-Type Schemes for Hyperbolic Conservation Laws. SIAM Review vol. 25 35–61 (1983) -- [10.1137/1025002](https://doi.org/10.1137/1025002)
- [Kotyczka, P. & Thoma, T. Symplectic discrete-time energy-based control for nonlinear mechanical systems. Automatica vol. 133 109842 (2021)](symplectic-discrete-time-energy-based-control-for-nonlinear-mechanical-systems) -- [10.1016/j.automatica.2021.109842](https://doi.org/10.1016/j.automatica.2021.109842)
- [Macchelli, A. Trajectory Tracking for Discrete-Time Port-Hamiltonian Systems. IEEE Control Systems Letters vol. 6 3146–3151 (2022)](trajectory-tracking-for-discrete-time-port-hamiltonian-systems) -- [10.1109/lcsys.2022.3182845](https://doi.org/10.1109/lcsys.2022.3182845)
- [Macchelli, A. Control Design for a Class of Discrete-Time Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 68 8224–8231 (2023)](control-design-for-a-class-of-discrete-time-port-hamiltonian-systems) -- [10.1109/tac.2023.3292180](https://doi.org/10.1109/tac.2023.3292180)
- Macchelli, (2023)
- [Massaroli, S. et al. Optimal Energy Shaping via Neural Approximators. SIAM Journal on Applied Dynamical Systems vol. 21 2126–2147 (2022)](optimal-energy-shaping-via-neural-approximators) -- [10.1137/21m1414279](https://doi.org/10.1137/21m1414279)
- Monaco, S., Normand-Cyrot, D. & Tiefensee, F. Nonlinear port controlled Hamiltonian systems under sampling. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference 1782–1787 (2009) doi:10.1109/cdc.2009.5399866 -- [10.1109/cdc.2009.5399866](https://doi.org/10.1109/cdc.2009.5399866)
- [Moreschini, A., Mattioni, M., Monaco, S. & Normand-Cyrot, D. Stabilization of Discrete Port-Hamiltonian Dynamics via Interconnection and Damping Assignment. IEEE Control Systems Letters vol. 5 103–108 (2021)](stabilization-of-discrete-port-hamiltonian-dynamics-via-interconnection-and-damping-assignment) -- [10.1109/lcsys.2020.3000705](https://doi.org/10.1109/lcsys.2020.3000705)
- Nunna, K., Sassano, M. & Astolfi, A. Constructive Interconnection and Damping Assignment for Port-Controlled Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 60 2350–2361 (2015) -- [10.1109/tac.2015.2400663](https://doi.org/10.1109/tac.2015.2400663)
- Ortega, Putting energy back in control. Control Systems Magazine, IEEE (2001)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Paszke, Pytorch: An imperative style, high-performance deep learning library. Advances in Neural Information Processing Systems (2019)
- Quispel, G. R. W. & Turner, G. S. Discrete gradient methods for solving ODEs numerically while preserving a first integral. Journal of Physics A: Mathematical and General vol. 29 L341–L349 (1996) -- [10.1088/0305-4470/29/13/006](https://doi.org/10.1088/0305-4470/29/13/006)
- Robbins, H. & Monro, S. A Stochastic Approximation Method. The Annals of Mathematical Statistics vol. 22 400–407 (1951) -- [10.1214/aoms/1177729586](https://doi.org/10.1214/aoms/1177729586)
- Song, Y., Romero, A., Müller, M., Koltun, V. & Scaramuzza, D. Reaching the limit in autonomous racing: Optimal control versus reinforcement learning. Science Robotics vol. 8 (2023) -- [10.1126/scirobotics.adg1462](https://doi.org/10.1126/scirobotics.adg1462)
- van der Schaft, A. L2-Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer International Publishing, 2017). doi:10.1007/978-3-319-49992-5 -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- Zanella, (2024)

