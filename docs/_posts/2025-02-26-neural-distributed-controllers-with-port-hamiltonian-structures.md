---
layout: post
title: "Neural Distributed Controllers with Port-Hamiltonian Structures"
date: 2025-02-26 00:00:00 +0100
permalink: neural-distributed-controllers-with-port-hamiltonian-structures
year: 2024
authors: Muhammad Zakwan, Giancarlo Ferrari-Trecate
category: proceedings
---
 
## Authors
[Muhammad Zakwan](authors/muhammad-zakwan), [Giancarlo Ferrari-Trecate](authors/giancarlo-ferrari-trecate)
 
## Abstract
Controlling large-scale cyber-physical systems necessitates optimal distributed policies, relying solely on local real-time data and limited communication with neighboring agents. However, finding optimal controllers remains challenging, even in seemingly simple scenarios. Parameterizing these policies using Neural Networks (NNs) can deliver good performance, but their sensitivity to small input changes can destabilize the closed-loop system. This paper addresses this issue for a network of nonlinear dissipative systems. Specifically, we leverage well-established port-Hamiltonian structures to characterize deep distributed control policies with closed-loop stability guarantees and a finite \\( {\mathcal{L}[[:space:]]}_{2} \\) gain, regardless of specific NN parameters. This eliminates the need to constrain the parameters during optimization and enables training with standard methods like stochastic gradient descent. A numerical study on the consensus control of Kuramoto oscillators demonstrates the effectiveness of the proposed controllers.
 
## Citation
- **Journal:** 2024 IEEE 63rd Conference on Decision and Control (CDC)
- **Year:** 2024
- **Volume:** 
- **Issue:** 
- **Pages:** 8633--8638
- **Publisher:** IEEE
- **DOI:** [10.1109/cdc56724.2024.10886616](https://doi.org/10.1109/cdc56724.2024.10886616)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Zakwan_2024,
  title={{Neural Distributed Controllers with Port-Hamiltonian Structures}},
  DOI={10.1109/cdc56724.2024.10886616},
  booktitle={{2024 IEEE 63rd Conference on Decision and Control (CDC)}},
  publisher={IEEE},
  author={Zakwan, Muhammad and Ferrari-Trecate, Giancarlo},
  year={2024},
  pages={8633--8638}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/neural-distributed-controllers-with-port-hamiltonian-structures.bib)
 
## References
- Witsenhausen, H. S. A Counterexample in Stochastic Optimum Control. SIAM Journal on Control 6, 131–147 (1968) -- [10.1137/0306011](https://doi.org/10.1137/0306011)
- Lessard, L. & Lall, S. Quadratic invariance is necessary and sufficient for convexity. Proceedings of the 2011 American Control Conference 5360–5362 (2011) doi:10.1109/acc.2011.5990928 -- [10.1109/acc.2011.5990928](https://doi.org/10.1109/acc.2011.5990928)
- Furieri, Distributed neural network control with dependability guarantees: a compositional port-hamiltonian approach. Learning for Dynamics and Control Conference
- Brunke, L. et al. Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning. Annu. Rev. Control Robot. Auton. Syst. 5, 411–444 (2022) -- [10.1146/annurev-control-042920-020211](https://doi.org/10.1146/annurev-control-042920-020211)
- Tsukamoto, H., Chung, S.-J. & Slotine, J.-J. E. Contraction theory for nonlinear stability analysis and learning-based control: A tutorial overview. Annual Reviews in Control 52, 135–169 (2021) -- [10.1016/j.arcontrol.2021.10.001](https://doi.org/10.1016/j.arcontrol.2021.10.001)
- Dawson, Safe control with learned certificates: A survey of neural Lyapunov, barrier, and contraction methods. arXiv preprint arXiv:2202.11762 (2022)
- Furieri, L., Galimberti, C. L. & Ferrari-Trecate, G. Learning to Boost the Performance of Stable Nonlinear Systems. IEEE Open J. Control. Syst. 3, 342–357 (2024) -- [10.1109/ojcsys.2024.3441768](https://doi.org/10.1109/ojcsys.2024.3441768)
- Nghiem, T. X. et al. Physics-Informed Machine Learning for Modeling and Control of Dynamical Systems. 2023 American Control Conference (ACC) 3735–3750 (2023) doi:10.23919/acc55779.2023.10155901 -- [10.23919/acc55779.2023.10155901](https://doi.org/10.23919/acc55779.2023.10155901)
- Verhoek, C., Beintema, G. I., Haesaert, S., Schoukens, M. & Toth, R. Deep-Learning-Based Identification of LPV Models for Nonlinear Systems. 2022 IEEE 61st Conference on Decision and Control (CDC) 3274–3280 (2022) doi:10.1109/cdc51059.2022.9992609 -- [10.1109/cdc51059.2022.9992609](https://doi.org/10.1109/cdc51059.2022.9992609)
- Revay, M., Wang, R. & Manchester, I. R. Recurrent Equilibrium Networks: Flexible Dynamic Models With Guaranteed Stability and Robustness. IEEE Trans. Automat. Contr. 69, 2855–2870 (2024) -- [10.1109/tac.2023.3294101](https://doi.org/10.1109/tac.2023.3294101)
- Wang, R., Barbara, N. H., Revay, M. & Manchester, I. R. Learning Over All Stabilizing Nonlinear Controllers for a Partially-Observed Linear System. IEEE Control Syst. Lett. 7, 91–96 (2023) -- [10.1109/lcsys.2022.3184847](https://doi.org/10.1109/lcsys.2022.3184847)
- Scandella, M., Bin, M. & Parisini, T. Kernel-Based Identification of Incrementally Input-to-State Stable Nonlinear Systems. IFAC-PapersOnLine 56, 5127–5132 (2023) -- [10.1016/j.ifacol.2023.10.1297](https://doi.org/10.1016/j.ifacol.2023.10.1297)
- [Zakwan, M. et al. Physically Consistent Neural ODEs for Learning Multi-Physics Systems*. IFAC-PapersOnLine 56, 5855–5860 (2023)](physically-consistent-neural-odes-for-learning-multi-physics-systems) -- [10.1016/j.ifacol.2023.10.079](https://doi.org/10.1016/j.ifacol.2023.10.079)
- Natale, L. D., Zakwan, M., Heer, P., Ferrari-Trecate, G. & Jones, C. N. SIMBa: System Identification Methods Leveraging Backpropagation. IEEE Trans. Contr. Syst. Technol. 33, 418–433 (2025) -- [10.1109/tcst.2024.3477301](https://doi.org/10.1109/tcst.2024.3477301)
- Di Natale, L. et al. Stable Linear Subspace Identification: A Machine Learning Approach. 2024 European Control Conference (ECC) 3539–3544 (2024) doi:10.23919/ecc64448.2024.10590843 -- [10.23919/ecc64448.2024.10590843](https://doi.org/10.23919/ecc64448.2024.10590843)
- Asikis, T., Böttcher, L. & Antulov-Fantulin, N. Neural ordinary differential equation control of dynamics on graphs. Phys. Rev. Research 4, (2022) -- [10.1103/physrevresearch.4.013221](https://doi.org/10.1103/physrevresearch.4.013221)
- Böttcher, L., Antulov-Fantulin, N. & Asikis, T. AI Pontryagin or how artificial neural networks learn to control dynamical systems. Nat Commun 13, (2022) -- [10.1038/s41467-021-27590-0](https://doi.org/10.1038/s41467-021-27590-0)
- Hewing, L., Kabzan, J. & Zeilinger, M. N. Cautious Model Predictive Control Using Gaussian Process Regression. IEEE Trans. Contr. Syst. Technol. 28, 2736–2743 (2020) -- [10.1109/tcst.2019.2949757](https://doi.org/10.1109/tcst.2019.2949757)
- Armenio, L. B., Terzi, E., Farina, M. & Scattolini, R. Model Predictive Control Design for Dynamical Systems Learned by Echo State Networks. IEEE Control Syst. Lett. 3, 1044–1049 (2019) -- [10.1109/lcsys.2019.2920720](https://doi.org/10.1109/lcsys.2019.2920720)
- Bonassi, F., Farina, M., Xie, J. & Scattolini, R. On Recurrent Neural Networks for learning-based control: Recent results and ideas for future developments. Journal of Process Control 114, 92–104 (2022) -- [10.1016/j.jprocont.2022.04.011](https://doi.org/10.1016/j.jprocont.2022.04.011)
- Terzi, E., Bonassi, F., Farina, M. & Scattolini, R. Learning model predictive control with long short‐term memory networks. Intl J Robust &amp; Nonlinear 31, 8877–8896 (2021) -- [10.1002/rnc.5519](https://doi.org/10.1002/rnc.5519)
- Zakwan, M., Xu, L. & Ferrari-Trecate, G. Robust Classification Using Contractive Hamiltonian Neural ODEs. IEEE Control Syst. Lett. 7, 145–150 (2023) -- [10.1109/lcsys.2022.3186959](https://doi.org/10.1109/lcsys.2022.3186959)
- van der Schaft, A. L2-Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer International Publishing, 2017). doi:10.1007/978-3-319-49992-5 -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- Yang, F. & Matni, N. Communication Topology Co-Design in Graph Recurrent Neural Network based Distributed Control. 2021 60th IEEE Conference on Decision and Control (CDC) 3619–3626 (2021) doi:10.1109/cdc45484.2021.9683779 -- [10.1109/cdc45484.2021.9683779](https://doi.org/10.1109/cdc45484.2021.9683779)
- Tolstaya, Learning decentralized controllers for robot swarms with graph neural networks. Conference on robot learning
- Khan, Graph policy gradients for large scale robot control. Conference on robot learning
- Gama, Graph neural networks for distributed linearquadratic control. Learning for Dynamics and Control (2021)
- Brunke, L. et al. Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning. Annu. Rev. Control Robot. Auton. Syst. 5, 411–444 (2022) -- [10.1146/annurev-control-042920-020211](https://doi.org/10.1146/annurev-control-042920-020211)
- Cheng, R., Orosz, G., Murray, R. M. & Burdick, J. W. End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks. AAAI 33, 3387–3395 (2019) -- [10.1609/aaai.v33i01.33013387](https://doi.org/10.1609/aaai.v33i01.33013387)
- Berkenkamp, Safe model-based reinforcement learning with stability guarantees. Ad-vances in Neural Information Processing Systems 30 (2018)
- Richards, The Lyapunov neural network: Adaptive stability certification for safe learning of dynamical systems. Conference on Robot Learning
- Koller, Learningbased model predictive control for safe exploration. 2018 IEEE conference on decision and control (CDC)
- Pauli, Offsetfree setpoint tracking using neural network controllers. Learning for Dynamics and Control (2021)
- Khader, S. A., Yin, H., Falco, P. & Kragic, D. Learning Deep Energy Shaping Policies for Stability-Guaranteed Manipulation. IEEE Robot. Autom. Lett. 6, 8583–8590 (2021) -- [10.1109/lra.2021.3111962](https://doi.org/10.1109/lra.2021.3111962)
- Duong, T. & Atanasov, N. Hamiltonian-based Neural ODE Networks on the SE(3) Manifold For Dynamics Learning and Control. Robotics: Science and Systems XVII (2021) doi:10.15607/rss.2021.xvii.086 -- [10.15607/rss.2021.xvii.086](https://doi.org/10.15607/rss.2021.xvii.086)
- Martinelli, D., Galimberti, C. L., Manchester, I. R., Furieri, L. & Ferrari-Trecate, G. Unconstrained Parametrization of Dissipative and Contracting Neural Ordinary Differential Equations. 2023 62nd IEEE Conference on Decision and Control (CDC) 3043–3048 (2023) doi:10.1109/cdc49753.2023.10383704 -- [10.1109/cdc49753.2023.10383704](https://doi.org/10.1109/cdc49753.2023.10383704)
- Massai, Unconstrained learning of networked nonlinear systems via free parametrization of stable interconnected operators. arXiv preprint arXiv:2311.13967 (2023)
- Khong, S. Z. & van der Schaft, A. On the converse of the passivity and small-gain theorems for input–output maps. Automatica 97, 58–63 (2018) -- [10.1016/j.automatica.2018.07.026](https://doi.org/10.1016/j.automatica.2018.07.026)
- Zakwan, Neural distributed controllers with port-hamiltonian structures. arXiv preprint arXiv:2403.17785 (2024)
- Arcak, M., Meissen, C. & Packard, A. Networks of Dissipative Systems. SpringerBriefs in Electrical and Computer Engineering (Springer International Publishing, 2016). doi:10.1007/978-3-319-29928-0 -- [10.1007/978-3-319-29928-0](https://doi.org/10.1007/978-3-319-29928-0)
- Galimberti, C. L., Furieri, L., Xu, L. & Ferrari-Trecate, G. Hamiltonian Deep Neural Networks Guaranteeing Nonvanishing Gradients by Design. IEEE Trans. Automat. Contr. 68, 3155–3162 (2023) -- [10.1109/tac.2023.3239430](https://doi.org/10.1109/tac.2023.3239430)
- Zakwan, M., d’Angelo, M. & Ferrari-Trecate, G. Universal Approximation Property of Hamiltonian Deep Neural Networks. IEEE Control Syst. Lett. 1–1 (2023) doi:10.1109/lcsys.2023.3288350 -- [10.1109/lcsys.2023.3288350](https://doi.org/10.1109/lcsys.2023.3288350)
- Dörfler, F. & Bullo, F. Synchronization in complex networks of phase oscillators: A survey. Automatica 50, 1539–1564 (2014) -- [10.1016/j.automatica.2014.04.012](https://doi.org/10.1016/j.automatica.2014.04.012)
- Wu, J. & Li, X. Collective Synchronization of Kuramoto-Oscillator Networks. IEEE Circuits Syst. Mag. 20, 46–67 (2020) -- [10.1109/mcas.2020.3005485](https://doi.org/10.1109/mcas.2020.3005485)
- Chopra, N. & Spong, M. W. Passivity-Based Control of Multi-Agent Systems. Advances in Robot Control 107–134 doi:10.1007/978-3-540-37347-6_6 -- [10.1007/978-3-540-37347-6_6](https://doi.org/10.1007/978-3-540-37347-6_6)
- Haber, E. & Ruthotto, L. Stable architectures for deep neural networks. Inverse Problems 34, 014004 (2017) -- [10.1088/1361-6420/aa9a90](https://doi.org/10.1088/1361-6420/aa9a90)
- Kingma, Adam: A method for stochastic gradient descent. ICLR: International Conference on Learning Representations

