---
title: "Physics-informed multi-agent reinforcement learning with multi-scale graph perception for multi-robot coordination"
date: 2026-08-06 00:00:00 +0100
permalink: physics-informed-multi-agent-reinforcement-learning-with-multi-scale-graph-perception-for-multi-robot-coordination
year: 2027
authors: Han Jing, Yuguang Zhong, Zhengyu Zhang, Dening Song
category: articles
tags:
  - graph neural networks, long-range coordination, multi-agent reinforcement learning, multi-robot systems, physics-informed control, port-hamiltonian systems
---
 
## Authors
[Han Jing](authors/han-jing), [Yuguang Zhong](authors/yuguang-zhong), [Zhengyu Zhang](authors/zhengyu-zhang), [Dening Song](authors/dening-song)
 
## Abstract
Distributed control for large-scale multi-robot systems remains challenging under sparse and time-varying communication graphs, where one-hop interaction models may miss long-range task context and homogeneous policies may produce overly similar behaviors. This paper proposes PIMARL–V–Cycle, a physics-informed multi-agent reinforcement learning framework that embeds a fixed-graph V-shaped multi-hop attention backbone into a port-Hamiltonian policy actor. The V-shaped backbone repeatedly applies sparse graph attention on the communication graph to enlarge the receptive field, while skip connections preserve local geometric information and agent-specific cues. The decoder then synthesizes actions through a structured port-Hamiltonian parameterization, and the overall policy is trained with Soft Actor-Critic under centralized training and decentralized execution using a graph-structured replay buffer. We evaluate the method on cooperative navigation and spatial sampling tasks in VMAS and assess communication robustness in a Robotarium simulator with communication delays, packet losses, and noise. In the tested settings, PIMARL–V–Cycle improves mean coordination performance over MLP, graph self-attention, and the original physics-informed baseline, and it transfers to larger test teams within the reported range without additional training. Qualitative observations further suggest that skip-connected multi-hop aggregation reduces the herding behavior observed in the baseline during large-scale exploration. The results demonstrate the value of combining V-shaped long-range graph perception with port-Hamiltonian action decoding for scalable and robust multi-robot coordination.
 
## Keywords
graph neural networks, long-range coordination, multi-agent reinforcement learning, multi-robot systems, physics-informed control, port-hamiltonian systems
 
## Citation
- **Journal:** Expert Systems with Applications
- **Year:** 2027
- **Volume:** 333
- **Issue:** 
- **Pages:** 133930
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.eswa.2026.133930](https://doi.org/10.1016/j.eswa.2026.133930)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Jing_2027,
  title={{Physics-informed multi-agent reinforcement learning with multi-scale graph perception for multi-robot coordination}},
  volume={333},
  ISSN={0957-4174},
  DOI={10.1016/j.eswa.2026.133930},
  journal={Expert Systems with Applications},
  publisher={Elsevier BV},
  author={Jing, Han and Zhong, Yuguang and Zhang, Zhengyu and Song, Dening},
  year={2027},
  pages={133930}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/physics-informed-multi-agent-reinforcement-learning-with-multi-scale-graph-perception-for-multi-robot-coordination.bib)
 
## References
- Alon, On the bottleneck of graph neural networks and its practical implications. (2021)
- Arai T, Pagello E, Parker LE (2002) Guest editorial advances in multirobot systems. IEEE Trans Robot Automat 18(5):655–661. https://doi.org/10.1109/tra.2002.80602 -- [10.1109/tra.2002.806024](https://doi.org/10.1109/tra.2002.806024)
- Banerjee C, Nguyen K, Fookes C, Raissi M (2025) A survey on physics informed reinforcement learning: Review and open problems. Expert Systems with Applications 287:128166. https://doi.org/10.1016/j.eswa.2025.12816 -- [10.1016/j.eswa.2025.128166](https://doi.org/10.1016/j.eswa.2025.128166)
- [Beckers T, Jiahao TZ, Pappas GJ (2023) Learning Switching Port-Hamiltonian Systems with Uncertainty Quantification. IFAC-PapersOnLine 56(2):525–532. https://doi.org/10.1016/j.ifacol.2023.10.162](learning-switching-port-hamiltonian-systems-with-uncertainty-quantification) -- [10.1016/j.ifacol.2023.10.1621](https://doi.org/10.1016/j.ifacol.2023.10.1621)
- Bettini, VMAS: A vectorized multi-agent simulator for collective robot learning. (2024)
- Bettini, BenchMARL: Benchmarking multi-agent reinforcement learning. Journal of Machine Learning Research (2024)
- Blankenstein G, Ortega R, Van Der Schaft AJ (2002) The matching conditions of controlled Lagrangians and IDA-passivity based control. International Journal of Control 75(9):645–665. https://doi.org/10.1080/0020717021013593 -- [10.1080/00207170210135939](https://doi.org/10.1080/00207170210135939)
- Bohmer, Deep coordination graphs. (2020)
- Cort&eacute;s J, Egerstedt M (2017) Coordinated Control of Multi-Robot Systems: A Survey. SICE Journal of Control, Measurement, and System Integration 10(6):495–503. https://doi.org/10.9746/jcmsi.10.49 -- [10.9746/jcmsi.10.495](https://doi.org/10.9746/jcmsi.10.495)
- Cuomo S, Di Cola VS, Giampaolo F, Rozza G, Raissi M, Piccialli F (2022) Scientific Machine Learning Through Physics–Informed Neural Networks: Where we are and What’s Next. J Sci Comput 92(3). https://doi.org/10.1007/s10915-022-01939- -- [10.1007/s10915-022-01939-z](https://doi.org/10.1007/s10915-022-01939-z)
- Ellis, SMACv2: An improved benchmark for cooperative multi-agent reinforcement learning. Advances in Neural Information Processing Systems (2024)
- Foerster, Counterfactual multi-agent policy gradients. (2018)
- Furieri, Distributed neural network control with dependability guarantees: A compositional port-Hamiltonian approach. (2022)
- Galimberti CL, Furieri L, Xu L, Ferrari-Trecate G (2023) Hamiltonian Deep Neural Networks Guaranteeing Nonvanishing Gradients by Design. IEEE Trans Automat Contr 68(5):3155–3162. https://doi.org/10.1109/tac.2023.323943 -- [10.1109/tac.2023.3239430](https://doi.org/10.1109/tac.2023.3239430)
- Gama F, Li Q, Tolstaya E, Prorok A, Ribeiro A (2022) Synthesizing Decentralized Controllers With Graph Neural Networks and Imitation Learning. IEEE Trans Signal Process 70:1932–1946. https://doi.org/10.1109/tsp.2022.316640 -- [10.1109/tsp.2022.3166401](https://doi.org/10.1109/tsp.2022.3166401)
- Gilmer, Neural message passing for quantum chemistry. (2017)
- {"status":"error" -- [10.1007/s10462-021-09996-w](https://doi.org/10.1007/s10462-021-09996-w)
- Gu H, Hong F, Hu F, Hu F, Abbas G, Touti E (2026) Safe multi-agent reinforcement learning framework for coordinated control in multi-robot systems. Expert Systems with Applications 305:130895. https://doi.org/10.1016/j.eswa.2025.13089 -- [10.1016/j.eswa.2025.130895](https://doi.org/10.1016/j.eswa.2025.130895)
- He, Deep residual learning for image recognition. (2016)
- [Hernández Q, Badías A, Chinesta F, Cueto E (2023) Port-metriplectic neural networks: thermodynamics-informed machine learning of complex physical systems. Comput Mech 72(3):553–561. https://doi.org/10.1007/s00466-023-02296-](port-metriplectic-neural-networks-thermodynamics-informed-machine-learning-of-complex-physical-systems) -- [10.1007/s00466-023-02296-w](https://doi.org/10.1007/s00466-023-02296-w)
- Hu Y, Fu J, Wen G (2025) Graph Soft Actor–Critic Reinforcement Learning for Large-Scale Distributed Multirobot Coordination. IEEE Trans Neural Netw Learning Syst 36(1):665–676. https://doi.org/10.1109/tnnls.2023.332953 -- [10.1109/tnnls.2023.3329530](https://doi.org/10.1109/tnnls.2023.3329530)
- Huang, Collision avoidance and navigation for a quadrotor swarm using end-to-end deep reinforcement learning. (2024)
- Kim S, Santos M, Guerrero-Bonilla L, Yezzi A, Egerstedt M (2022) Coverage Control of Mobile Robots With Different Maximum Speeds for Time-Sensitive Applications. IEEE Robot Autom Lett 7(2):3001–3007. https://doi.org/10.1109/lra.2022.314659 -- [10.1109/lra.2022.3146593](https://doi.org/10.1109/lra.2022.3146593)
- Kipf, Semi-supervised classification with graph convolutional networks. (2017)
- Li, Multipole graph neural operator for parametric partial differential equations. (2020)
- Lo, Cheap talk discovery and utilization in multi-agent reinforcement learning. (2023)
- Long, Towards optimally decentralized multi-robot collision avoidance via deep reinforcement learning. (2018)
- Lowe, Multi-agent actor-critic for mixed cooperative-competitive environments. (2017)
- Luvisutto A, Celani A, Renda F, Stefanini C, De Masi G (2025) Enhancing collaboration in uncertain environment: Multi-Agent Reinforcement Learning for underwater monitoring. Expert Systems with Applications 277:127256. https://doi.org/10.1016/j.eswa.2025.12725 -- [10.1016/j.eswa.2025.127256](https://doi.org/10.1016/j.eswa.2025.127256)
- Malencia, Adaptive sampling of latent phenomena using heterogeneous robot teams (ASLap-HR). (2022)
- Nayak, Scalable multi-agent reinforcement learning through intelligent information aggregation. (2023)
- Neary, Compositional learning of dynamical system models using port-Hamiltonian neural networks. (2023)
- Nghiem, Physics-informed machine learning for modeling and control of dynamical systems. (2023)
- Oroojlooy A, Hajinezhad D (2022) A review of cooperative multi-agent deep reinforcement learning. Appl Intell 53(11):13677–13722. https://doi.org/10.1007/s10489-022-04105- -- [10.1007/s10489-022-04105-y](https://doi.org/10.1007/s10489-022-04105-y)
- Peng, FACMAC: Factored multi-agent centralised policy gradients. (2021)
- Peng J, Viswanath H, Bera A (2024) Graph-Based Decentralized Task Allocation for Multi-Robot Target Localization. IEEE Robot Autom Lett 9(11):10676–10683. https://doi.org/10.1109/lra.2024.347501 -- [10.1109/lra.2024.3475013](https://doi.org/10.1109/lra.2024.3475013)
- Pickem, The Robotarium: A remotely accessible swarm robotics research testbed. (2017)
- Qu G, Wierman A, Li N (2022) Scalable Reinforcement Learning for Multiagent Networked Systems. Operations Research 70(6):3601–3628. https://doi.org/10.1287/opre.2021.222 -- [10.1287/opre.2021.2226](https://doi.org/10.1287/opre.2021.2226)
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.04 -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Rampasek, Recipe for a general, powerful, scalable graph transformer. (2022)
- Rashid, Qmix: Monotonic value function factorisation for deep multi-agent deep reinforcement learning. (2018)
- Rodwell C, Tallapragada P (2023) Physics-informed reinforcement learning for motion control of a fish-like swimming robot. Sci Rep 13(1). https://doi.org/10.1038/s41598-023-36399- -- [10.1038/s41598-023-36399-4](https://doi.org/10.1038/s41598-023-36399-4)
- [Roth FJ, Klein DK, Kannapinn M, Peters J, Weeger O (2025) Stable Port-Hamiltonian Neural Networks. Advances in Neural Information Processing Systems 38 56483–5650](stable-port-hamiltonian-neural-networks) -- [10.52202/085713-1693](https://doi.org/10.52202/085713-1693)
- Sanyal, Ramp-Net: A robust adaptive mpc for quadrotors via physics-informed neural network. (2023)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Schaft AJ (2004) Port-Hamiltonian Systems: Network Modeling and Control of Nonlinear Physical Systems. Advanced Dynamics and Control of Structures and Machines 127–16](port-hamiltonian-systems-network-modeling-and-control-of-nonlinear-physical-systems) -- [10.1007/978-3-7091-2774-2_9](https://doi.org/10.1007/978-3-7091-2774-2_9)
- [Sebastián E, Duong T, Atanasov N, Montijano E, Sagüés C (2025) Physics-Informed Multiagent Reinforcement Learning for Distributed Multirobot Problems. IEEE Trans Robot 41:4499–4517. https://doi.org/10.1109/tro.2025.358283](physics-informed-multiagent-reinforcement-learning-for-distributed-multirobot-problems) -- [10.1109/tro.2025.3582836](https://doi.org/10.1109/tro.2025.3582836)
- Seraj E, Wang Z, Paleja R, Martin D, Sklar M, Patel A, Gombolay M (2022) Learning Efficient Diverse Communication for Cooperative Heterogeneous Teaming. International Joint Conference on Autonomous Agents and Multiagent Systems 1173–118 -- [10.65109/vjxc6483](https://doi.org/10.65109/vjxc6483)
- Serra-Gómez Á, Zhu H, Brito B, Böhmer W, Alonso-Mora J (2023) Learning scalable and efficient communication policies for multi-robot collision avoidance. Auton Robot 47(8):1275–1297. https://doi.org/10.1007/s10514-023-10127- -- [10.1007/s10514-023-10127-3](https://doi.org/10.1007/s10514-023-10127-3)
- Sunehag P, Lever G, Gruslys A, Czarnecki WM, Zambaldi V, Jaderberg M, Lanctot M, Sonnerat N, Leibo JZ, Tuyls K, Graepel T (2018) Value-Decomposition Networks For Cooperative Multi-Agent Learning Based On Team Reward. International Joint Conference on Autonomous Agents and Multiagent Systems 2085–208 -- [10.65109/jsrc7365](https://doi.org/10.65109/jsrc7365)
- Tian Y, Chang Y, Herrera Arias F, Nieto-Granda C, How JP, Carlone L (2022) Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems. IEEE Trans Robot 38(4):2022–2038. https://doi.org/10.1109/tro.2021.313775 -- [10.1109/tro.2021.3137751](https://doi.org/10.1109/tro.2021.3137751)
- Topping, Understanding over-squashing and bottlenecks on graphs via curvature. (2022)
- Vaswani, Attention is all you need. (2017)
- Velickovic, Graph attention networks. (2018)
- Wang, DARL1N: Distributed multi-agent reinforcement learning with one-hop neighbors. (2022)
- Xie Z, Shen S, Wang Y, Qiao C, Tang B, Song W (2026) ROCO: Role-oriented communication for efficient multi-agent reinforcement learning. Expert Systems with Applications 297:129421. https://doi.org/10.1016/j.eswa.2025.12942 -- [10.1016/j.eswa.2025.129421](https://doi.org/10.1016/j.eswa.2025.129421)
- Xu Y, Kohtz S, Boakye J, Gardoni P, Wang P (2023) Physics-informed machine learning for reliability and systems safety applications: State of the art and challenges. Reliability Engineering &amp; System Safety 230:108900. https://doi.org/10.1016/j.ress.2022.10890 -- [10.1016/j.ress.2022.108900](https://doi.org/10.1016/j.ress.2022.108900)
- Yu, The surprising effectiveness of PPO in cooperative multi-agent games. (2022)
- Yu H, Lei X, Song Z, Liu C, Wang J (2020) Supervised Network-Based Fuzzy Learning of EEG Signals for Alzheimer’s Disease Identification. IEEE Trans Fuzzy Syst 28(1):60–71. https://doi.org/10.1109/tfuzz.2019.290375 -- [10.1109/tfuzz.2019.2903753](https://doi.org/10.1109/tfuzz.2019.2903753)
- Yu H, Lin Z, Li F, Liu J, Liu C, Wang J (2026) Spatiospectral Representation and Neural Decoding of Somatic Perception of Acupuncture Stimulations. IEEE J Biomed Health Inform 30(3):2694–2707. https://doi.org/10.1109/jbhi.2025.360117 -- [10.1109/jbhi.2025.3601173](https://doi.org/10.1109/jbhi.2025.3601173)
- Yu H, Zeng F, Liu D, Wang J, Liu J (2025) Neural Manifold Decoder for Acupuncture Stimulations With Representation Learning: An Acupuncture-Brain Interface. IEEE J Biomed Health Inform 29(6):4147–4160. https://doi.org/10.1109/jbhi.2025.353092 -- [10.1109/jbhi.2025.3530922](https://doi.org/10.1109/jbhi.2025.3530922)

