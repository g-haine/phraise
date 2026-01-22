---
title: "Neural Port-Hamiltonian Differential Algebraic Equations for Compositional Learning of Electrical Networks"
date: 2026-01-12 00:00:00 +0100
permalink: neural-port-hamiltonian-differential-algebraic-equations-for-compositional-learning-of-electrical-networks
year: 2025
authors: Cyrus Neary, Nathan Tsao, Ufuk Topcu
category: proceedings
---
 
## Authors
[Cyrus Neary](authors/cyrus-neary), [Nathan Tsao](authors/nathan-tsao), [Ufuk Topcu](authors/ufuk-topcu)
 
## Abstract
We develop compositional learning algorithms for coupled dynamical systems, with a particular focus on electrical networks. While deep learning has proven effective at modeling complex relationships from data, compositional couplings between system components typically introduce algebraic constraints on state variables, posing challenges to many existing data-driven approaches to modeling dynamical systems. Towards developing deep learning models for constrained dynamical systems, we introduce neural port-Hamiltonian differential algebraic equations (N-PHDAEs), which use neural networks to parameterize unknown terms in both the differential and algebraic components of a port-Hamiltonian DAE. To train these models, we propose an algorithm that uses automatic differentiation to perform index reduction, automatically transforming the neural DAE into an equivalent system of neural ordinary differential equations (N-ODEs), for which established model inference and backpropagation methods exist. Experiments simulating the dynamics of nonlinear circuits exemplify the benefits of our approach: the proposed N-PHDAE model achieves an order of magnitude improvement in prediction accuracy and constraint satisfaction when compared to a baseline N-ODE over long prediction time horizons. We also validate the compositional capabilities of our approach through experiments on a simulated DC microgrid: we train individual N-PHDAE models for separate grid components, before coupling them to accurately predict the behavior of larger-scale networks.
 
## Citation
- **Journal:** 2025 IEEE 64th Conference on Decision and Control (CDC)
- **Year:** 2025
- **Volume:** 
- **Issue:** 
- **Pages:** 2097--2103
- **Publisher:** IEEE
- **DOI:** [10.1109/cdc57313.2025.11312148](https://doi.org/10.1109/cdc57313.2025.11312148)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Neary_2025,
  title={{Neural Port-Hamiltonian Differential Algebraic Equations for Compositional Learning of Electrical Networks}},
  DOI={10.1109/cdc57313.2025.11312148},
  booktitle={{2025 IEEE 64th Conference on Decision and Control (CDC)}},
  publisher={IEEE},
  author={Neary, Cyrus and Tsao, Nathan and Topcu, Ufuk},
  year={2025},
  pages={2097--2103}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/neural-port-hamiltonian-differential-algebraic-equations-for-compositional-learning-of-electrical-networks.bib)
 
## References
- [Beckers T (2023) Data-Driven Bayesian Control of Port-Hamiltonian Systems. 2023 62nd IEEE Conference on Decision and Control (CDC) 8708–871](data-driven-bayesian-control-of-port-hamiltonian-systems) -- [10.1109/cdc49753.2023.10384219](https://doi.org/10.1109/cdc49753.2023.10384219)
- Chen, Neural ordinary differential equations. Advances in neural information processing systems (2018)
- Cucuzzella M, Trip S, De Persis C, Cheng X, Ferrara A, van der Schaft A (2019) A Robust Consensus Algorithm for Current Sharing and Voltage Regulation in DC Microgrids. IEEE Trans Contr Syst Technol 27(4):1583–1595. https://doi.org/10.1109/tcst.2018.283487 -- [10.1109/tcst.2018.2834878](https://doi.org/10.1109/tcst.2018.2834878)
- [Desai SA, Mattheakis M, Sondak D, Protopapas P, Roberts SJ (2021) Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Phys Rev E 104(3). https://doi.org/10.1103/physreve.104.03431](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Djeumou, How to Learn and Generalize From Three Minutes of Data: Physics-Constrained and Uncertainty-Aware Neural Stochastic Differential Equations. Conference on Robot Learning
- Djeumou, Neural Networks with Physics-Informed Architectures and Constraints for Dynamical Systems Modeling. Learning for Dynamics and Control Conference
- [Duindam V, Macchelli A, Stramigioli S, Bruyninckx H (2009) Modeling and Control of Complex Physical Systems. Springer Berlin Heidelber](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [Duong T, Altawaitan A, Stanley J, Atanasov N (2024) Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control. IEEE Trans Robot 40:3695–3715. https://doi.org/10.1109/tro.2024.342843](port-hamiltonian-neural-ode-networks-on-lie-groups-for-robot-dynamics-learning-and-control) -- [10.1109/tro.2024.3428433](https://doi.org/10.1109/tro.2024.3428433)
- Furieri, Distributed neural network control with dependability guarantees: a compositional port-Hamiltonian approach. Learning for Dynamics and Control Conference
- Greydanus, Hamiltonian Neural Networks. Advances in Neural Information Processing Systems. (2019)
- [Günther M, Bartel A, Jacob B, Reis T (2020) Dynamic iteration schemes and port‐Hamiltonian formulation in coupled differential‐algebraic equation circuit simulation. Circuit Theory &amp; Apps 49(2):430–452. https://doi.org/10.1002/cta.287](dynamic-iteration-schemes-and-port-hamiltonian-formulation-in-coupled-differential-algebraic-equation-circuit-simulation) -- [10.1002/cta.2870](https://doi.org/10.1002/cta.2870)
- Han J, Jentzen A, E W (2018) Solving high-dimensional partial differential equations using deep learning. Proc Natl Acad Sci USA 115(34):8505–8510. https://doi.org/10.1073/pnas.171894211 -- [10.1073/pnas.1718942115](https://doi.org/10.1073/pnas.1718942115)
- Huang Y, Zou C, Li Y, Wik T (2024) MINN: Learning the Dynamics of Differential-Algebraic Equations and Application to Battery Modeling. IEEE Trans Pattern Anal Mach Intell 46(12):11331–11344. https://doi.org/10.1109/tpami.2024.345647 -- [10.1109/tpami.2024.3456475](https://doi.org/10.1109/tpami.2024.3456475)
- Izhikevich E, FitzHugh R (2006) FitzHugh-Nagumo model. Scholarpedia 1(9):1349. https://doi.org/10.4249/scholarpedia.134 -- [10.4249/scholarpedia.1349](https://doi.org/10.4249/scholarpedia.1349)
- Karniadakis GE, Kevrekidis IG, Lu L, Perdikaris P, Wang S, Yang L (2021) Physics-informed machine learning. Nat Rev Phys 3(6):422–440. https://doi.org/10.1038/s42254-021-00314- -- [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5)
- Kidger, On neural differential equations. PhD thesis. (2021)
- Koch, Neural Differential Algebraic Equations. arXiv preprint arXiv: (2024)
- Long Z, Lu Y, Dong B (2019) PDE-Net 2.0: Learning PDEs from data with a numeric-symbolic hybrid deep network. Journal of Computational Physics 399:108925. https://doi.org/10.1016/j.jcp.2019.10892 -- [10.1016/j.jcp.2019.108925](https://doi.org/10.1016/j.jcp.2019.108925)
- Lu L, Pestourie R, Yao W, Wang Z, Verdugo F, Johnson SG (2021) Physics-Informed Neural Networks with Hard Constraints for Inverse Design. SIAM J Sci Comput 43(6):B1105–B1132. https://doi.org/10.1137/21m139790 -- [10.1137/21m1397908](https://doi.org/10.1137/21m1397908)
- [Mehrmann V, Morandin R (2019) Structure-preserving discretization for port-Hamiltonian descriptor systems. 2019 IEEE 58th Conference on Decision and Control (CDC) 6863–686](structure-preserving-discretization-for-port-hamiltonian-descriptor-systems) -- [10.1109/cdc40024.2019.9030180](https://doi.org/10.1109/cdc40024.2019.9030180)
- Moya C, Lin G (2022) DAE-PINN: a physics-informed neural network model for simulating differential algebraic equations with application to power networks. Neural Comput &amp; Applic 35(5):3789–3804. https://doi.org/10.1007/s00521-022-07886- -- [10.1007/s00521-022-07886-y](https://doi.org/10.1007/s00521-022-07886-y)
- Neary, Engineering AI systems and AI for engineering: compositionality and physics in learning. PhD thesis. (2024)
- Neary, Compositional learning of dynamical system models using port-hamiltonian neural networks. Learning for Dynamics and Control Conference
- Neary, Neural Port-Hamiltonian Differential Algebraic Equations for Compositional Learning of Electrical Networks. arXiv preprint arXiv: (2024)
- Plaza, Total Energy Shaping with Neural Interconnection and Damping Assignment - Passivity Based Control. Learning for Dynamics and Control Conference
- Rackauckas, Universal differential equations for scientific machine learning. arXiv preprint arXiv: (2020)
- Raissi, Deep hidden physics models: Deep learning of nonlinear partial differential equations. The Journal of Machine Learning Research (2018)
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.04 -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Sirignano J, Spiliopoulos K (2018) DGM: A deep learning algorithm for solving partial differential equations. Journal of Computational Physics 375:1339–1364. https://doi.org/10.1016/j.jcp.2018.08.02 -- [10.1016/j.jcp.2018.08.029](https://doi.org/10.1016/j.jcp.2018.08.029)
- Tan, Physics-constrained learning of PDE systems with uncertainty quantified port-Hamiltonian models. Learning for Dynamics and Control Conference
- [Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [van der Schaft AJ, Maschke BM (2013) Port-Hamiltonian Systems on Graphs. SIAM J Control Optim 51(2):906–937. https://doi.org/10.1137/11084009](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Wanner, Solving ordinary differential equations II. (1996)
- Xiao T, Chen Y, Huang S, He T, Guan H (2023) Feasibility Study of Neural ODE and DAE Modules for Power System Dynamic Component Modeling. IEEE Trans Power Syst 38(3):2666–2678. https://doi.org/10.1109/tpwrs.2022.319457 -- [10.1109/tpwrs.2022.3194570](https://doi.org/10.1109/tpwrs.2022.3194570)
- [Xu L, Zakwan M, Ferrari-Trecate G (2022) Neural Energy Casimir Control for Port-Hamiltonian Systems. 2022 IEEE 61st Conference on Decision and Control (CDC) 4053–405](neural-energy-casimir-control-for-port-hamiltonian-systems) -- [10.1109/cdc51059.2022.9992784](https://doi.org/10.1109/cdc51059.2022.9992784)
- Zhong, Benchmarking Energy-Conserving Neural Networks for Learning Dynamics from Data. Learning for Dynamics and Control Conference

