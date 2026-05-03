---
title: "Physics-Informed Multiagent Reinforcement Learning for Distributed Multirobot Problems"
date: 2025-06-24 00:00:00 +0100
permalink: physics-informed-multiagent-reinforcement-learning-for-distributed-multirobot-problems
year: 2025
authors: Eduardo Sebastián, Thai Duong, Nikolay Atanasov, Eduardo Montijano, Carlos Sagüés
category: articles
---
 
## Authors
[Eduardo Sebastián](authors/eduardo-sebastian), [Thai Duong](authors/thai-duong), [Nikolay Atanasov](authors/nikolay-atanasov), [Eduardo Montijano](authors/eduardo-montijano), [Carlos Sagüés](authors/carlos-sagues)
 
## Abstract
The networked nature of multirobot systems presents challenges in the context of multiagent reinforcement learning. Centralized control policies do not scale with increasing numbers of robots, whereas independent control policies do not exploit the information provided by other robots, exhibiting poor performance in cooperative-competitive tasks. In this work, we propose a physics-informed reinforcement learning approach able to learn distributed multirobot control policies that are both scalable and make use of all the available information to each robot. Our approach has three key characteristics. First, it imposes a port-Hamiltonian structure on the policy representation, respecting energy conservation properties of physical robot systems and the networked nature of robot team interactions. Second, it uses self-attention to ensure a sparse policy representation able to handle time-varying information at each robot from the interaction graph. Third, we present a soft actor–critic reinforcement learning algorithm parameterized by our self-attention port-Hamiltonian control policy, which accounts for the correlation among robots during training while overcoming the need of value function factorization. Extensive simulations in different multirobot scenarios demonstrate the success of the proposed approach, surpassing previous multirobot reinforcement learning solutions in scalability, while achieving similar or superior performance (with averaged cumulative reward up to \\( \times {\text{2}[[:space:]]} \\) greater than the state-of-the-art with robot teams \\( \times {\text{6}[[:space:]]} \\) larger than the number of robots at training time). We also validate our approach on multiple real robots in the Georgia Tech Robotarium under imperfect communication, demonstrating zero-shot sim-to-real transfer and scalability across number of robots.
 
## Citation
- **Journal:** IEEE Transactions on Robotics
- **Year:** 2025
- **Volume:** 41
- **Issue:** 
- **Pages:** 4499--4517
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tro.2025.3582836](https://doi.org/10.1109/tro.2025.3582836)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Sebasti_n_2025,
  title={{Physics-Informed Multiagent Reinforcement Learning for Distributed Multirobot Problems}},
  volume={41},
  ISSN={1941-0468},
  DOI={10.1109/tro.2025.3582836},
  journal={IEEE Transactions on Robotics},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Sebastián, Eduardo and Duong, Thai and Atanasov, Nikolay and Montijano, Eduardo and Sagüés, Carlos},
  year={2025},
  pages={4499--4517}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/physics-informed-multiagent-reinforcement-learning-for-distributed-multirobot-problems.bib)
 
## References
- Pickem D, Glotfelter P, Wang L, Mote M, Ames A, Feron E, Egerstedt M (2017) The Robotarium: A remotely accessible swarm robotics research testbed. 2017 IEEE International Conference on Robotics and Automation (ICRA) 1699–170 -- [10.1109/icra.2017.7989200](https://doi.org/10.1109/icra.2017.7989200)
- Peng, FACMAC: Factored multi-agent centralised policy gradients. Adv. Neural Inf. Process. Syst. (2021)
- Atanasov N, Le Ny J, Daniilidis K, Pappas GJ (2015) Decentralized active information acquisition: Theory and application to multi-robot SLAM. 2015 IEEE International Conference on Robotics and Automation (ICRA) 4775–478 -- [10.1109/icra.2015.7139863](https://doi.org/10.1109/icra.2015.7139863)
- Tian Y, Chang Y, Herrera Arias F, Nieto-Granda C, How JP, Carlone L (2022) Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems. IEEE Trans Robot 38(4):2022–2038. https://doi.org/10.1109/tro.2021.313775 -- [10.1109/tro.2021.3137751](https://doi.org/10.1109/tro.2021.3137751)
- Kan X, Thayer TC, Carpin S, Karydis K (2021) Task Planning on Stochastic Aisle Graphs for Precision Agriculture. IEEE Robot Autom Lett 6(2):3287–3294. https://doi.org/10.1109/lra.2021.306233 -- [10.1109/lra.2021.3062337](https://doi.org/10.1109/lra.2021.3062337)
- Pierson A, Schwager M (2015) Bio-inspired non-cooperative multi-robot herding. 2015 IEEE International Conference on Robotics and Automation (ICRA) 1843–184 -- [10.1109/icra.2015.7139438](https://doi.org/10.1109/icra.2015.7139438)
- Sebastian E, Montijano E (2021) Multi-robot Implicit Control of Herds. 2021 IEEE International Conference on Robotics and Automation (ICRA) 1601–160 -- [10.1109/icra48506.2021.9561231](https://doi.org/10.1109/icra48506.2021.9561231)
- Sebastian E, Montijano E, Sagues C (2022) Adaptive Multirobot Implicit Control of Heterogeneous Herds. IEEE Trans Robot 38(6):3622–3635. https://doi.org/10.1109/tro.2022.318353 -- [10.1109/tro.2022.3183537](https://doi.org/10.1109/tro.2022.3183537)
- Heintzman L, Hashimoto A, Abaid N, Williams RK (2021) Anticipatory Planning and Dynamic Lost Person Models for Human-Robot Search and Rescue. 2021 IEEE International Conference on Robotics and Automation (ICRA) 8252–825 -- [10.1109/icra48506.2021.9562070](https://doi.org/10.1109/icra48506.2021.9562070)
- Matarić MJ (1997) Reinforcement Learning in the Multi-Robot Domain. Robot Colonies 73–8 -- [10.1007/978-1-4757-6451-2_4](https://doi.org/10.1007/978-1-4757-6451-2_4)
- Matignon L, Laurent GJ, Le Fort-Piat N (2007) Hysteretic Q-learning : an algorithm for Decentralized Reinforcement Learning in Cooperative Multi-Agent Teams. 2007 IEEE/RSJ International Conference on Intelligent Robots and Systems 64–6 -- [10.1109/iros.2007.4399095](https://doi.org/10.1109/iros.2007.4399095)
- Matignon L, Jeanpierre L, Mouaddib A-I (2021) Coordinated Multi-Robot Exploration Under Communication Constraints Using Decentralized Markov Decision Processes. AAAI 26(1):2017–2023. https://doi.org/10.1609/aaai.v26i1.838 -- [10.1609/aaai.v26i1.8380](https://doi.org/10.1609/aaai.v26i1.8380)
- Munikoti S, Agarwal D, Das L, Halappanavar M, Natarajan B (2024) Challenges and Opportunities in Deep Reinforcement Learning With Graph Neural Networks: A Comprehensive Review of Algorithms and Applications. IEEE Trans Neural Netw Learning Syst 35(11):15051–15071. https://doi.org/10.1109/tnnls.2023.328352 -- [10.1109/tnnls.2023.3283523](https://doi.org/10.1109/tnnls.2023.3283523)
- Serra-Gómez Á, Zhu H, Brito B, Böhmer W, Alonso-Mora J (2023) Learning scalable and efficient communication policies for multi-robot collision avoidance. Auton Robot 47(8):1275–1297. https://doi.org/10.1007/s10514-023-10127- -- [10.1007/s10514-023-10127-3](https://doi.org/10.1007/s10514-023-10127-3)
- Lo, Cheap talk discovery and utilization in multi-agent reinforcement learning. Proc. Int. Conf. Learn. Representations (2023)
- Qu G, Wierman A, Li N (2022) Scalable Reinforcement Learning for Multiagent Networked Systems. Operations Research 70(6):3601–3628. https://doi.org/10.1287/opre.2021.222 -- [10.1287/opre.2021.2226](https://doi.org/10.1287/opre.2021.2226)
- [Beckers T, Jiahao TZ, Pappas GJ (2023) Learning Switching Port-Hamiltonian Systems with Uncertainty Quantification. IFAC-PapersOnLine 56(2):525–532. https://doi.org/10.1016/j.ifacol.2023.10.162](learning-switching-port-hamiltonian-systems-with-uncertainty-quantification) -- [10.1016/j.ifacol.2023.10.1621](https://doi.org/10.1016/j.ifacol.2023.10.1621)
- Neary, Compositional learning of dynamical system models using port-Hamiltonian neural networks. Proc. Learn. Dyn. Control Conf. (2023)
- [Sebastián E, Duong T, Atanasov N, Montijano E, Sagüés C (2023) LEMURS: Learning Distributed Multi-Robot Interactions. 2023 IEEE International Conference on Robotics and Automation (ICRA) 7713–771](lemurs-learning-distributed-multi-robot-interactions) -- [10.1109/icra48891.2023.10161328](https://doi.org/10.1109/icra48891.2023.10161328)
- Nghiem TX, Drgoňa J, Jones C, Nagy Z, Schwan R, Dey B, Chakrabarty A, Di Cairano S, Paulson JA, Carron A, Zeilinger MN, Shaw Cortez W, Vrabie DL (2023) Physics-Informed Machine Learning for Modeling and Control of Dynamical Systems. 2023 American Control Conference (ACC) 3735–375 -- [10.23919/acc55779.2023.10155901](https://doi.org/10.23919/acc55779.2023.10155901)
- Sanyal S, Roy K (2023) RAMP-Net: A Robust Adaptive MPC for Quadrotors via Physics-informed Neural Network. 2023 IEEE International Conference on Robotics and Automation (ICRA) 1019–102 -- [10.1109/icra48891.2023.10161410](https://doi.org/10.1109/icra48891.2023.10161410)
- Rodwell C, Tallapragada P (2023) Physics-informed reinforcement learning for motion control of a fish-like swimming robot. Sci Rep 13(1). https://doi.org/10.1038/s41598-023-36399- -- [10.1038/s41598-023-36399-4](https://doi.org/10.1038/s41598-023-36399-4)
- Cuomo S, Di Cola VS, Giampaolo F, Rozza G, Raissi M, Piccialli F (2022) Scientific Machine Learning Through Physics–Informed Neural Networks: Where we are and What’s Next. J Sci Comput 92(3). https://doi.org/10.1007/s10915-022-01939- -- [10.1007/s10915-022-01939-z](https://doi.org/10.1007/s10915-022-01939-z)
- Xu Y, Kohtz S, Boakye J, Gardoni P, Wang P (2023) Physics-informed machine learning for reliability and systems safety applications: State of the art and challenges. Reliability Engineering &amp; System Safety 230:108900. https://doi.org/10.1016/j.ress.2022.10890 -- [10.1016/j.ress.2022.108900](https://doi.org/10.1016/j.ress.2022.108900)
- Bloembergen D, Tuyls K, Hennes D, Kaisers M (2015) Evolutionary Dynamics of Multi-Agent Learning: A Survey. jair 53:659–697. https://doi.org/10.1613/jair.481 -- [10.1613/jair.4818](https://doi.org/10.1613/jair.4818)
- Long P, Fanl T, Liao X, Liu W, Zhang H, Pan J (2018) Towards Optimally Decentralized Multi-Robot Collision Avoidance via Deep Reinforcement Learning. 2018 IEEE International Conference on Robotics and Automation (ICRA) 6252–625 -- [10.1109/icra.2018.8461113](https://doi.org/10.1109/icra.2018.8461113)
- Semnani SH, Liu H, Everett M, de Ruiter A, How JP (2020) Multi-Agent Motion Planning for Dense and Dynamic Environments via Deep Reinforcement Learning. IEEE Robot Autom Lett 5(2):3221–3226. https://doi.org/10.1109/lra.2020.297469 -- [10.1109/lra.2020.2974695](https://doi.org/10.1109/lra.2020.2974695)
- Ng, Algorithms for inverse reinforcement learning. Proc. Int. Conf. Mach. Learn. (2000)
- Dasari, RoboNet: Large-scale multi-robot learning. Proc. Conf. Robot Learn. (2020)
- Bogert K, Doshi P (2018) Multi-robot inverse reinforcement learning under occlusion with estimation of state transitions. Artificial Intelligence 263:46–73. https://doi.org/10.1016/j.artint.2018.07.00 -- [10.1016/j.artint.2018.07.002](https://doi.org/10.1016/j.artint.2018.07.002)
- Han R, Chen S, Hao Q (2020) Cooperative Multi-Robot Navigation in Dynamic Environment with Deep Reinforcement Learning. 2020 IEEE International Conference on Robotics and Automation (ICRA) 448–45 -- [10.1109/icra40945.2020.9197209](https://doi.org/10.1109/icra40945.2020.9197209)
- Gharbi I, Kuckling J, Ramos DG, Birattari M (2023) Show me What you want: Inverse Reinforcement Learning to Automatically Design Robot Swarms by Demonstration. 2023 IEEE International Conference on Robotics and Automation (ICRA) 5063–507 -- [10.1109/icra48891.2023.10160947](https://doi.org/10.1109/icra48891.2023.10160947)
- Zhu H, Claramunt FM, Brito B, Alonso-Mora J (2021) Learning Interaction-Aware Trajectory Predictions for Decentralized Multi-Robot Motion Planning in Dynamic Environments. IEEE Robot Autom Lett 6(2):2256–2263. https://doi.org/10.1109/lra.2021.306107 -- [10.1109/lra.2021.3061073](https://doi.org/10.1109/lra.2021.3061073)
- Zhou S, Phielipp MJ, Sefair JA, Walker SI, Amor HB (2019) Clone Swarms: Learning to Predict and Control Multi-Robot Systems by Imitation. 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 4092–409 -- [10.1109/iros40897.2019.8967824](https://doi.org/10.1109/iros40897.2019.8967824)
- Qu, Scalable reinforcement learning of localized policies for multi-agent networked systems. Proc. Learn. Dyn. Control (2020)
- Zambaldi, Deep reinforcement learning with relational inductive biases. Proc. Int. Conf. Learn. Representations (2018)
- Iqbal, Actor-attention-critic for multi-agent reinforcement learning. Proc. Int. Conf. Mach. Learn. (2019)
- Li G, Jiang B, Zhu H, Che Z, Liu Y (2020) Generative Attention Networks for Multi-Agent Behavioral Modeling. AAAI 34(05):7195–7202. https://doi.org/10.1609/aaai.v34i05.620 -- [10.1609/aaai.v34i05.6209](https://doi.org/10.1609/aaai.v34i05.6209)
- Parnika, Attention actor-critic algorithm for multi-agent constrained co-operative reinforcement learning. Proc. Int. Conf. Auton. Agents Multiagent Syst. (2021)
- Marino A, Pacchierotti C, Giordano PR (2024) Input State Stability of Gated Graph Neural Networks. IEEE Trans Control Netw Syst 11(4):2052–2063. https://doi.org/10.1109/tcns.2024.337271 -- [10.1109/tcns.2024.3372710](https://doi.org/10.1109/tcns.2024.3372710)
- Li Q, Lin W, Liu Z, Prorok A (2021) Message-Aware Graph Attention Networks for Large-Scale Multi-Robot Path Planning. IEEE Robot Autom Lett 6(3):5533–5540. https://doi.org/10.1109/lra.2021.307786 -- [10.1109/lra.2021.3077863](https://doi.org/10.1109/lra.2021.3077863)
- Khan, Graph policy gradients for large scale robot control. Proc. Conf. Robot Learn. (2020)
- Tolstaya, Learning decentralized controllers for robot Swarms with graph neural networks. Proc. Conf. Robot Learn. (2020)
- Tolstaya E, Paulos J, Kumar V, Ribeiro A (2021) Multi-Robot Coverage and Exploration using Spatial Graph Neural Networks. 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 8944–895 -- [10.1109/iros51168.2021.9636675](https://doi.org/10.1109/iros51168.2021.9636675)
- Yang F, Matni N (2021) Communication Topology Co-Design in Graph Recurrent Neural Network based Distributed Control. 2021 60th IEEE Conference on Decision and Control (CDC) 3619–362 -- [10.1109/cdc45484.2021.9683779](https://doi.org/10.1109/cdc45484.2021.9683779)
- Gama F, Li Q, Tolstaya E, Prorok A, Ribeiro A (2022) Synthesizing Decentralized Controllers With Graph Neural Networks and Imitation Learning. IEEE Trans Signal Process 70:1932–1946. https://doi.org/10.1109/tsp.2022.316640 -- [10.1109/tsp.2022.3166401](https://doi.org/10.1109/tsp.2022.3166401)
- Kuyer L, Whiteson S, Bakker B, Vlassis N Multiagent Reinforcement Learning for Urban Traffic Control Using Coordination Graphs. Lecture Notes in Computer Science 656–67 -- [10.1007/978-3-540-87479-9_61](https://doi.org/10.1007/978-3-540-87479-9_61)
- Buşoniu L, Babuška R, De Schutter B (2010) Multi-agent Reinforcement Learning: An Overview. Studies in Computational Intelligence 183–22 -- [10.1007/978-3-642-14435-6_7](https://doi.org/10.1007/978-3-642-14435-6_7)
- Vinyals, Starcraft II: A new challenge for reinforcement learning. (2017)
- Ellis, SMACv2: An improved benchmark for cooperative multi-agent reinforcement learning. Adv. Neural Inf. Process. Syst. (2024)
- Gronauer S, Diepold K (2021) Multi-agent deep reinforcement learning: a survey. Artif Intell Rev 55(2):895–943. https://doi.org/10.1007/s10462-021-09996- -- [10.1007/s10462-021-09996-w](https://doi.org/10.1007/s10462-021-09996-w)
- Oroojlooy A, Hajinezhad D (2022) A review of cooperative multi-agent deep reinforcement learning. Appl Intell 53(11):13677–13722. https://doi.org/10.1007/s10489-022-04105- -- [10.1007/s10489-022-04105-y](https://doi.org/10.1007/s10489-022-04105-y)
- Matignon L, Laurent GJ, Le Fort-Piat N (2012) Independent reinforcement learners in cooperative Markov games: a survey regarding coordination problems. The Knowledge Engineering Review 27(1):1–31. https://doi.org/10.1017/s026988891200005 -- [10.1017/s0269888912000057](https://doi.org/10.1017/s0269888912000057)
- Papoudakis, Dealing with non-stationarity in multi-agent deep reinforcement learning. (2019)
- Bhmer, Deep coordination graphs. Proc. Int. Conf. Mach. Learn. (2020)
- Haarnoja, Soft actor-critic algorithms and applications. (2018)
- Zhang S Continuous control for robot based on deep reinforcement learnin -- [10.32657/10356/90191](https://doi.org/10.32657/10356/90191)
- Liu Y Proximal Policy Optimization in StarCraf -- [10.12794/metadc1505267](https://doi.org/10.12794/metadc1505267)
- Lowe, Multi-agent actor-critic for mixed cooperative-competitive environments. Adv. Neural Inf. Process. Syst. (2017)
- Yu, The surprising effectiveness of PPO in cooperative multi-agent games. Adv. Neural Inf. Process. Syst. (2022)
- Bettini, BenchMARL: Benchmarking multi-agent reinforcement learning. J. Mach. Learn. Res. (2024)
- Kuba, Trust region policy optimisation in multi-agent reinforcement learning. Proc. Int. Conf. Learn. Representations (2021)
- Bloom J, Paliwal P, Mukherjee A, Pinciroli C (2023) Decentralized Multi-Agent Reinforcement Learning with Global State Prediction. 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 8854–886 -- [10.1109/iros55552.2023.10341563](https://doi.org/10.1109/iros55552.2023.10341563)
- Yang, Mean field multi-agent reinforcement learning. Proc. Int. Conf. Mach. Learn. (2018)
- Wang B, Xie J, Atanasov N (2022) DARL1N: Distributed multi-Agent Reinforcement Learning with One-hop Neighbors. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 9003–901 -- [10.1109/iros47612.2022.9981441](https://doi.org/10.1109/iros47612.2022.9981441)
- Witt, Is independent learning all you need in the starcraft multi-agent challenge. (2020)
- Motokawa Y, Sugawara T (2023) Interpretability for Conditional Coordinated Behavior in Multi-Agent Reinforcement Learning. 2023 International Joint Conference on Neural Networks (IJCNN) 1– -- [10.1109/ijcnn54540.2023.10191825](https://doi.org/10.1109/ijcnn54540.2023.10191825)
- Kortvelesy, QGNN: Value function factorisation with graph neural networks. (2022)
- Hu Y, Fu J, Wen G (2025) Graph Soft Actor–Critic Reinforcement Learning for Large-Scale Distributed Multirobot Coordination. IEEE Trans Neural Netw Learning Syst 36(1):665–676. https://doi.org/10.1109/tnnls.2023.332953 -- [10.1109/tnnls.2023.3329530](https://doi.org/10.1109/tnnls.2023.3329530)
- Huang Z, Yang Z, Krupani R, Şenbaşlar B, Batra S, Sukhatme GS (2024) Collision Avoidance and Navigation for a Quadrotor Swarm Using End-to-end Deep Reinforcement Learning. 2024 IEEE International Conference on Robotics and Automation (ICRA) 300–30 -- [10.1109/icra57147.2024.10611499](https://doi.org/10.1109/icra57147.2024.10611499)
- Zhao P, Liu Y (2022) Physics Informed Deep Reinforcement Learning for Aircraft Conflict Resolution. IEEE Trans Intell Transport Syst 23(7):8288–8301. https://doi.org/10.1109/tits.2021.307757 -- [10.1109/tits.2021.3077572](https://doi.org/10.1109/tits.2021.3077572)
- Sartoretti G, Wu Y, Paivine W, Kumar TKS, Koenig S, Choset H (2019) Distributed Reinforcement Learning for Multi-robot Decentralized Collective Construction. Springer Proceedings in Advanced Robotics 35–4 -- [10.1007/978-3-030-05816-6_3](https://doi.org/10.1007/978-3-030-05816-6_3)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Furieri, Distributed neural network control with dependability guarantees: A compositional port-Hamiltonian approach. Proc. Learn. Dyn. Control Conf. (2022)
- Galimberti CL, Furieri L, Xu L, Ferrari-Trecate G (2023) Hamiltonian Deep Neural Networks Guaranteeing Nonvanishing Gradients by Design. IEEE Trans Automat Contr 68(5):3155–3162. https://doi.org/10.1109/tac.2023.323943 -- [10.1109/tac.2023.3239430](https://doi.org/10.1109/tac.2023.3239430)
- Shi G, Honig W, Yue Y, Chung S-J (2020) Neural-Swarm: Decentralized Close-Proximity Multirotor Control Using Learned Interactions. 2020 IEEE International Conference on Robotics and Automation (ICRA) 3241–324 -- [10.1109/icra40945.2020.9196800](https://doi.org/10.1109/icra40945.2020.9196800)
- Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser L, Polosukhin I (2017) Attention Is All You Nee -- [10.48550/arxiv.1706.03762](https://doi.org/10.48550/arxiv.1706.03762)
- [Schaft AJ (2004) Port-Hamiltonian Systems: Network Modeling and Control of Nonlinear Physical Systems. Advanced Dynamics and Control of Structures and Machines 127–16](port-hamiltonian-systems-network-modeling-and-control-of-nonlinear-physical-systems) -- [10.1007/978-3-7091-2774-2_9](https://doi.org/10.1007/978-3-7091-2774-2_9)
- Blankenstein G, Ortega R, Van Der Schaft AJ (2002) The matching conditions of controlled Lagrangians and IDA-passivity based control. International Journal of Control 75(9):645–665. https://doi.org/10.1080/0020717021013593 -- [10.1080/00207170210135939](https://doi.org/10.1080/00207170210135939)
- Haarnoja, Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. Proc. Int. Conf. Mach. Learn. (2018)
- Bettini M, Kortvelesy R, Blumenkamp J, Prorok A (2024) VMAS: A Vectorized Multi-agent Simulator for Collective Robot Learning. Springer Proceedings in Advanced Robotics 42–5 -- [10.1007/978-3-031-51497-5_4](https://doi.org/10.1007/978-3-031-51497-5_4)
- Haarnoja T, Ha S, Zhou A, Tan J, Tucker G, Levine S (2019) Learning to Walk Via Deep Reinforcement Learning. Robotics: Science and Systems X -- [10.15607/rss.2019.xv.011](https://doi.org/10.15607/rss.2019.xv.011)
- Mordatch I, Abbeel P (2018) Emergence of Grounded Compositional Language in Multi-Agent Populations. AAAI 32(1). https://doi.org/10.1609/aaai.v32i1.1149 -- [10.1609/aaai.v32i1.11492](https://doi.org/10.1609/aaai.v32i1.11492)
- Long, Evolutionary population curriculum for scaling multi-agent reinforcement learning. Proc. Int. Conf. Learn. Representations (2019)
- Baydin, Automatic differentiation in machine learning: A survey. J. Mach. Learn. Res. (2018)
- Todorov E, Erez T, Tassa Y (2012) MuJoCo: A physics engine for model-based control. 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems 5026–503 -- [10.1109/iros.2012.6386109](https://doi.org/10.1109/iros.2012.6386109)
- Schulman, Trust region policy optimization. Proc. Int. Conf. Mach. Learn. (2015)
- Ramachandran, Searching for activation functions. (2017)
- Kingma, Adam: A method for stochastic optimization. Proc. Int. Conf. Learn. Representations (2015)

