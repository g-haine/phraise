---
title: "Neural Port-Hamiltonian Models for Nonlinear Distributed Control: An Unconstrained Parameterization Approach"
date: 2026-04-13 00:00:00 +0100
permalink: neural-port-hamiltonian-models-for-nonlinear-distributed-control-an-unconstrained-parameterization-approach
year: 2026
authors: Muhammad Zakwan, Giancarlo Ferrari-Trecate
category: articles
---
 
## Authors
[Muhammad Zakwan](authors/muhammad-zakwan), [Giancarlo Ferrari-Trecate](authors/giancarlo-ferrari-trecate)
 
## Abstract
The control of large-scale cyber-physical systems requires optimal distributed policies relying solely on limited communication with neighboring agents. However, computing stabilizing controllers for nonlinear systems while optimizing complex costs remains a significant challenge. Neural networks (NNs), known for their expressivity, can be leveraged to parameterize control policies that yield good performance. However, NNs' sensitivity to small input changes poses a risk of destabilizing the closed-loop system. Many existing approaches enforce constraints on the controllers' parameter space to guarantee closed-loop stability, leading to computationally expensive optimization procedures. To address these problems, we leverage the framework of port-Hamiltonian systems to design continuous-time distributed control policies for nonlinear systems that guarantee closed-loop stability and finite \\( \mathcal {L}_{2} \\) or incremental \\( \mathcal {L}_{2} \\) gains, independent of the optimization parameters of the controllers. This eliminates the need to constrain parameters during optimization, allowing the use of standard techniques such as gradient-based methods. In addition, we discuss discretization schemes that preserve the dissipation properties of these controllers for implementation on embedded systems. The effectiveness of the proposed distributed controllers is demonstrated through consensus control of nonholonomic mobile robots subject to collision avoidance and averaged voltage regulation with weighted power sharing in islanded DC microgrids.
 
## Citation
- **Journal:** IEEE Transactions on Automatic Control
- **Year:** 2026
- **Volume:** 71
- **Issue:** 9
- **Pages:** 6100--6115
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tac.2026.3683628](https://doi.org/10.1109/tac.2026.3683628)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Zakwan_2026,
  title={{Neural Port-Hamiltonian Models for Nonlinear Distributed Control: An Unconstrained Parameterization Approach}},
  volume={71},
  ISSN={2334-3303},
  DOI={10.1109/tac.2026.3683628},
  number={9},
  journal={IEEE Transactions on Automatic Control},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Zakwan, Muhammad and Ferrari-Trecate, Giancarlo},
  year={2026},
  pages={6100--6115}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/neural-port-hamiltonian-models-for-nonlinear-distributed-control-an-unconstrained-parameterization-approach.bib)
 
## References
- Witsenhausen HS (1968) A Counterexample in Stochastic Optimum Control. SIAM Journal on Control 6(1):131–147. https://doi.org/10.1137/030601 -- [10.1137/0306011](https://doi.org/10.1137/0306011)
- Lessard L, Lall S (2011) Quadratic invariance is necessary and sufficient for convexity. Proceedings of the 2011 American Control Conference 5360–536 -- [10.1109/acc.2011.5990928](https://doi.org/10.1109/acc.2011.5990928)
- Furieri, Distributed neural network control with dependability guarantees: A compositional port-Hamiltonian approach. Proc. Learn. Dyn. Control Conf. (2022)
- Brunke L, Greeff M, Hall AW, Yuan Z, Zhou S, Panerati J, Schoellig AP (2022) Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning. Annu Rev Control Robot Auton Syst 5(1):411–444. https://doi.org/10.1146/annurev-control-042920-02021 -- [10.1146/annurev-control-042920-020211](https://doi.org/10.1146/annurev-control-042920-020211)
- Tsukamoto H, Chung S-J, Slotine J-JE (2021) Contraction theory for nonlinear stability analysis and learning-based control: A tutorial overview. Annual Reviews in Control 52:135–169. https://doi.org/10.1016/j.arcontrol.2021.10.00 -- [10.1016/j.arcontrol.2021.10.001](https://doi.org/10.1016/j.arcontrol.2021.10.001)
- Dawson C, Gao S, Fan C (2023) Safe Control With Learned Certificates: A Survey of Neural Lyapunov, Barrier, and Contraction Methods for Robotics and Control. IEEE Trans Robot 39(3):1749–1767. https://doi.org/10.1109/tro.2022.323254 -- [10.1109/tro.2022.3232542](https://doi.org/10.1109/tro.2022.3232542)
- Furieri L, Galimberti CL, Ferrari-Trecate G (2024) Learning to Boost the Performance of Stable Nonlinear Systems. IEEE Open J Control Syst 3:342–357. https://doi.org/10.1109/ojcsys.2024.344176 -- [10.1109/ojcsys.2024.3441768](https://doi.org/10.1109/ojcsys.2024.3441768)
- Zakwan M, Xu L, Ferrari-Trecate G (2024) Neural Exponential Stabilization of Control-affine Nonlinear Systems. 2024 IEEE 63rd Conference on Decision and Control (CDC) 8602–860 -- [10.1109/cdc56724.2024.10886677](https://doi.org/10.1109/cdc56724.2024.10886677)
- Nghiem TX, Drgoňa J, Jones C, Nagy Z, Schwan R, Dey B, Chakrabarty A, Di Cairano S, Paulson JA, Carron A, Zeilinger MN, Shaw Cortez W, Vrabie DL (2023) Physics-Informed Machine Learning for Modeling and Control of Dynamical Systems. 2023 American Control Conference (ACC) 3735–375 -- [10.23919/acc55779.2023.10155901](https://doi.org/10.23919/acc55779.2023.10155901)
- Beintema GI, Schoukens M, Tóth R (2023) Deep subspace encoders for nonlinear system identification. Automatica 156:111210. https://doi.org/10.1016/j.automatica.2023.11121 -- [10.1016/j.automatica.2023.111210](https://doi.org/10.1016/j.automatica.2023.111210)
- Revay M, Wang R, Manchester IR (2024) Recurrent Equilibrium Networks: Flexible Dynamic Models With Guaranteed Stability and Robustness. IEEE Trans Automat Contr 69(5):2855–2870. https://doi.org/10.1109/tac.2023.329410 -- [10.1109/tac.2023.3294101](https://doi.org/10.1109/tac.2023.3294101)
- [Zakwan M, Natale LD, Svetozarevic B, Heer P, Jones CN, Trecate GF (2023) Physically Consistent Neural ODEs for Learning Multi-Physics Systems*. IFAC-PapersOnLine 56(2):5855–5860. https://doi.org/10.1016/j.ifacol.2023.10.07](physically-consistent-neural-odes-for-learning-multi-physics-systems) -- [10.1016/j.ifacol.2023.10.079](https://doi.org/10.1016/j.ifacol.2023.10.079)
- Natale LD, Zakwan M, Heer P, Ferrari-Trecate G, Jones CN (2025) SIMBa: System Identification Methods Leveraging Backpropagation. IEEE Trans Contr Syst Technol 33(2):418–433. https://doi.org/10.1109/tcst.2024.347730 -- [10.1109/tcst.2024.3477301](https://doi.org/10.1109/tcst.2024.3477301)
- Di Natale L, Zakwan M, Svetozarevic B, Heer P, Ferrari-Trecate G, Jones CN (2024) Stable Linear Subspace Identification: A Machine Learning Approach. 2024 European Control Conference (ECC) 3539–354 -- [10.23919/ecc64448.2024.10590843](https://doi.org/10.23919/ecc64448.2024.10590843)
- Asikis T, Böttcher L, Antulov-Fantulin N (2022) Neural ordinary differential equation control of dynamics on graphs. Phys Rev Research 4(1). https://doi.org/10.1103/physrevresearch.4.01322 -- [10.1103/physrevresearch.4.013221](https://doi.org/10.1103/physrevresearch.4.013221)
- Böttcher L, Antulov-Fantulin N, Asikis T (2022) AI Pontryagin or how artificial neural networks learn to control dynamical systems. Nat Commun 13(1). https://doi.org/10.1038/s41467-021-27590- -- [10.1038/s41467-021-27590-0](https://doi.org/10.1038/s41467-021-27590-0)
- Hewing L, Kabzan J, Zeilinger MN (2020) Cautious Model Predictive Control Using Gaussian Process Regression. IEEE Trans Contr Syst Technol 28(6):2736–2743. https://doi.org/10.1109/tcst.2019.294975 -- [10.1109/tcst.2019.2949757](https://doi.org/10.1109/tcst.2019.2949757)
- Armenio LB, Terzi E, Farina M, Scattolini R (2019) Model Predictive Control Design for Dynamical Systems Learned by Echo State Networks. IEEE Control Syst Lett 3(4):1044–1049. https://doi.org/10.1109/lcsys.2019.292072 -- [10.1109/lcsys.2019.2920720](https://doi.org/10.1109/lcsys.2019.2920720)
- Bonassi F, Farina M, Xie J, Scattolini R (2022) On Recurrent Neural Networks for learning-based control: Recent results and ideas for future developments. Journal of Process Control 114:92–104. https://doi.org/10.1016/j.jprocont.2022.04.01 -- [10.1016/j.jprocont.2022.04.011](https://doi.org/10.1016/j.jprocont.2022.04.011)
- Terzi E, Bonassi F, Farina M, Scattolini R (2021) Learning model predictive control with long short‐term memory networks. Intl J Robust &amp; Nonlinear 31(18):8877–8896. https://doi.org/10.1002/rnc.551 -- [10.1002/rnc.5519](https://doi.org/10.1002/rnc.5519)
- Zakwan M, Xu L, Ferrari-Trecate G (2023) Robust Classification Using Contractive Hamiltonian Neural ODEs. IEEE Control Syst Lett 7:145–150. https://doi.org/10.1109/lcsys.2022.318695 -- [10.1109/lcsys.2022.3186959](https://doi.org/10.1109/lcsys.2022.3186959)
- [van der Schaft A (2017) L2-Gain and Passivity Techniques in Nonlinear Control. Springer International Publishin](l2-gain-and-passivity-techniques-in-nonlinear-control) -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- Yang F, Matni N (2021) Communication Topology Co-Design in Graph Recurrent Neural Network based Distributed Control. 2021 60th IEEE Conference on Decision and Control (CDC) 3619–362 -- [10.1109/cdc45484.2021.9683779](https://doi.org/10.1109/cdc45484.2021.9683779)
- Tolstaya, Learning decentralized controllers for robot swarms with graph neural networks. Proc. Conf. Robot Learn. (2020)
- Khan, Graph policy gradients for large scale robot control. Proc. Conf. Robot Learn. (2020)
- Gama, Graph neural networks for distributed linear-quadratic control. Proc. Learn. Dyn. Control (2021)
- Brunke L, Greeff M, Hall AW, Yuan Z, Zhou S, Panerati J, Schoellig AP (2022) Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning. Annu Rev Control Robot Auton Syst 5(1):411–444. https://doi.org/10.1146/annurev-control-042920-02021 -- [10.1146/annurev-control-042920-020211](https://doi.org/10.1146/annurev-control-042920-020211)
- Cheng R, Orosz G, Murray RM, Burdick JW (2019) End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks. AAAI 33(01):3387–3395. https://doi.org/10.1609/aaai.v33i01.3301338 -- [10.1609/aaai.v33i01.33013387](https://doi.org/10.1609/aaai.v33i01.33013387)
- Berkenkamp, Safe model-based reinforcement learning with stability guarantees. Proc. Int. Conf. Neural Inf. Process. Syst. (2018)
- Richards, The Lyapunov neural network: Adaptive stability certification for safe learning of dynamical systems. Proc. Conf. Robot Learn. (2018)
- Koller T, Berkenkamp F, Turchetta M, Krause A (2018) Learning-Based Model Predictive Control for Safe Exploration. 2018 IEEE Conference on Decision and Control (CDC) 6059–606 -- [10.1109/cdc.2018.8619572](https://doi.org/10.1109/cdc.2018.8619572)
- Pauli, Offset-free setpoint tracking using neural network controllers. Proc. Learn. Dyn. Control (2021)
- Khader SA, Yin H, Falco P, Kragic D (2021) Learning Deep Energy Shaping Policies for Stability-Guaranteed Manipulation. IEEE Robot Autom Lett 6(4):8583–8590. https://doi.org/10.1109/lra.2021.311196 -- [10.1109/lra.2021.3111962](https://doi.org/10.1109/lra.2021.3111962)
- Duong T, Atanasov N (2021) Hamiltonian-based Neural ODE Networks on the SE(3) Manifold For Dynamics Learning and Control. Robotics: Science and Systems XVI -- [10.15607/rss.2021.xvii.086](https://doi.org/10.15607/rss.2021.xvii.086)
- Martinelli D, Galimberti CL, Manchester IR, Furieri L, Ferrari-Trecate G (2023) Unconstrained Parametrization of Dissipative and Contracting Neural Ordinary Differential Equations. 2023 62nd IEEE Conference on Decision and Control (CDC) 3043–304 -- [10.1109/cdc49753.2023.10383704](https://doi.org/10.1109/cdc49753.2023.10383704)
- Massai L, Saccani D, Furieri L, Ferrari-Trecate G (2024) Unconstrained Learning of Networked Nonlinear Systems via Free Parametrization of Stable Interconnected Operators. 2024 European Control Conference (ECC) 651–65 -- [10.23919/ecc64448.2024.10591242](https://doi.org/10.23919/ecc64448.2024.10591242)
- Khong SZ, van der Schaft A (2018) On the converse of the passivity and small-gain theorems for input–output maps. Automatica 97:58–63. https://doi.org/10.1016/j.automatica.2018.07.02 -- [10.1016/j.automatica.2018.07.026](https://doi.org/10.1016/j.automatica.2018.07.026)
- Ehrhardt MJ, Riis ES, Ringholm T, Schönlieb C-B (2024) A geometric integration approach to smooth optimization: foundations of the discrete gradient method. IMA Journal of Numerical Analysis 45(3):1269–1299. https://doi.org/10.1093/imanum/drae03 -- [10.1093/imanum/drae037](https://doi.org/10.1093/imanum/drae037)
- [Zakwan M, Ferrari-Trecate G (2024) Neural Distributed Controllers with Port-Hamiltonian Structures. 2024 IEEE 63rd Conference on Decision and Control (CDC) 8633–863](neural-distributed-controllers-with-port-hamiltonian-structures) -- [10.1109/cdc56724.2024.10886616](https://doi.org/10.1109/cdc56724.2024.10886616)
- Angeli D (2002) A Lyapunov approach to incremental stability properties. IEEE Trans Automat Contr 47(3):410–421. https://doi.org/10.1109/9.98906 -- [10.1109/9.989067](https://doi.org/10.1109/9.989067)
- Stan G-B, Sepulchre R (2007) Analysis of Interconnected Oscillators by Dissipativity Theory. IEEE Trans Automat Contr 52(2):256–270. https://doi.org/10.1109/tac.2006.89047 -- [10.1109/tac.2006.890471](https://doi.org/10.1109/tac.2006.890471)
- Tran DN, Ruffer BS, Kellett CM (2016) Incremental stability properties for discrete-time systems. 2016 IEEE 55th Conference on Decision and Control (CDC) 477–48 -- [10.1109/cdc.2016.7798314](https://doi.org/10.1109/cdc.2016.7798314)
- Sepulchre R, Chaffey T, Forni F (2022) On the incremental form of dissipativity. IFAC-PapersOnLine 55(30):290–294. https://doi.org/10.1016/j.ifacol.2022.11.06 -- [10.1016/j.ifacol.2022.11.067](https://doi.org/10.1016/j.ifacol.2022.11.067)
- Arcak M, Meissen C, Packard A (2016) Networks of Dissipative Systems. Springer International Publishin -- [10.1007/978-3-319-29928-0](https://doi.org/10.1007/978-3-319-29928-0)
- Verhoek C, Koelewijn PJW, Haesaert S, Tóth R (2023) Convex incremental dissipativity analysis of nonlinear systems. Automatica 150:110859. https://doi.org/10.1016/j.automatica.2023.11085 -- [10.1016/j.automatica.2023.110859](https://doi.org/10.1016/j.automatica.2023.110859)
- [van der Schaft A (2020) Port-Hamiltonian Modeling for Control. Annu Rev Control Robot Auton Syst 3(1):393–416. https://doi.org/10.1146/annurev-control-081219-09225](port-hamiltonian-modeling-for-control) -- [10.1146/annurev-control-081219-092250](https://doi.org/10.1146/annurev-control-081219-092250)
- Galimberti CL, Furieri L, Xu L, Ferrari-Trecate G (2023) Hamiltonian Deep Neural Networks Guaranteeing Nonvanishing Gradients by Design. IEEE Trans Automat Contr 68(5):3155–3162. https://doi.org/10.1109/tac.2023.323943 -- [10.1109/tac.2023.3239430](https://doi.org/10.1109/tac.2023.3239430)
- Zakwan M, d’Angelo M, Ferrari-Trecate G (2023) Universal Approximation Property of Hamiltonian Deep Neural Networks. IEEE Control Syst Lett :1–1. https://doi.org/10.1109/lcsys.2023.328835 -- [10.1109/lcsys.2023.3288350](https://doi.org/10.1109/lcsys.2023.3288350)
- Amos, Input convex neural networks. Proc. Int. Conf. Mach. Learn. (2017)
- He K, Zhang X, Ren S, Sun J (2016) Deep Residual Learning for Image Recognition. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 770–77 -- [10.1109/cvpr.2016.90](https://doi.org/10.1109/cvpr.2016.90)
- Nocedal J, Wright SJ (eds) (1999) Numerical Optimization. Springer-Verla -- [10.1007/b98874](https://doi.org/10.1007/b98874)
- Wang Y, Yin W, Zeng J (2018) Global Convergence of ADMM in Nonconvex Nonsmooth Optimization. J Sci Comput 78(1):29–63. https://doi.org/10.1007/s10915-018-0757- -- [10.1007/s10915-018-0757-z](https://doi.org/10.1007/s10915-018-0757-z)
- Houska B, Frasch J, Diehl M (2016) An Augmented Lagrangian Based Algorithm for Distributed NonConvex Optimization. SIAM J Optim 26(2):1101–1127. https://doi.org/10.1137/14097599 -- [10.1137/140975991](https://doi.org/10.1137/140975991)
- Biegler LT, Zavala VM (2009) Large-scale nonlinear programming using IPOPT: An integrating framework for enterprise-wide dynamic optimization. Computers &amp; Chemical Engineering 33(3):575–582. https://doi.org/10.1016/j.compchemeng.2008.08.00 -- [10.1016/j.compchemeng.2008.08.006](https://doi.org/10.1016/j.compchemeng.2008.08.006)
- Werbos PJ (1990) Backpropagation through time: what it does and how to do it. Proc IEEE 78(10):1550–1560. https://doi.org/10.1109/5.5833 -- [10.1109/5.58337](https://doi.org/10.1109/5.58337)
- Chen, Neural ordinary differential equations. Proc. 32nd Int. Conf. Neural Inf. Process. Syst. (2018)
- Foucart S, Rauhut H (2013) A Mathematical Introduction to Compressive Sensing. Springer New Yor -- [10.1007/978-0-8176-4948-7](https://doi.org/10.1007/978-0-8176-4948-7)
- Bauschke HH, Combettes PL (2011) Convex Analysis and Monotone Operator Theory in Hilbert Spaces. Springer New Yor -- [10.1007/978-1-4419-9467-7](https://doi.org/10.1007/978-1-4419-9467-7)
- Paszke, PyTorch: An imperative style, high-performance deep learning library. Proc. 33rd Int. Conf. Neural Inf. Process. Syst. (2019)
- Xia M, Antsaklis PJ, Gupta V (2014) Passivity indices and passivation of systems with application to systems with input/output delay. 53rd IEEE Conference on Decision and Control 783–78 -- [10.1109/cdc.2014.7039477](https://doi.org/10.1109/cdc.2014.7039477)
- Joo Y, Harvey R, Qu Z (2020) Preserving and Achieving Passivity-Short Property Through Discretization. IEEE Trans Automat Contr 65(10):4265–4272. https://doi.org/10.1109/tac.2019.295436 -- [10.1109/tac.2019.2954361](https://doi.org/10.1109/tac.2019.2954361)
- Martinelli, Interconnection of discrete-time dissipative systems. (2023)
- Hairer E, Hochbruck M, Iserles A, Lubich C (2006) Geometric Numerical Integration. Oberwolfach Rep 3(1):805–882. https://doi.org/10.4171/owr/2006/1 -- [10.4171/owr/2006/14](https://doi.org/10.4171/owr/2006/14)
- [Gonzalez O (1996) Time integration and discrete Hamiltonian systems. J Nonlinear Sci 6(5):449–467. https://doi.org/10.1007/bf0244016](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- Harten A, Lax PD, Leer B van (1983) On Upstream Differencing and Godunov-Type Schemes for Hyperbolic Conservation Laws. SIAM Rev 25(1):35–61. https://doi.org/10.1137/102500 -- [10.1137/1025002](https://doi.org/10.1137/1025002)
- Itoh T, Abe K (1988) Hamiltonian-conserving discrete canonical equations based on variational difference quotients. Journal of Computational Physics 76(1):85–102. https://doi.org/10.1016/0021-9991(88)90132- -- [10.1016/0021-9991(88)90132-5](https://doi.org/10.1016/0021-9991(88)90132-5)
- [Macchelli A (2023) Control Design for a Class of Discrete-Time Port-Hamiltonian Systems. IEEE Trans Automat Contr 68(12):8224–8231. https://doi.org/10.1109/tac.2023.329218](control-design-for-a-class-of-discrete-time-port-hamiltonian-systems) -- [10.1109/tac.2023.3292180](https://doi.org/10.1109/tac.2023.3292180)
- Jafarpour, Robust implicit networks via non-Euclidean contractions. Proc. 35th Int. Conf. Neural Inf. Process. Syst. (2021)
- Smith KD, Seccamonte F, Swami A, Bullo F (2022) Physics-Informed Implicit Representations of Equilibrium Network Flows. Advances in Neural Information Processing Systems 35 7211–722 -- [10.52202/068431-0523](https://doi.org/10.52202/068431-0523)
- Jafarpour, Robustness certificates for implicit neural networks: A mixed monotone contractive approach. Proc. Learn. Dyn. Control Conf. (2022)
- Winston, Monotone operator equilibrium networks. Proc. 34th Int. Conf. Neural Inf. Process. Syst. (2020)
- [Moreschini A, Mattioni M, Monaco S, Normand-Cyrot D (2021) Stabilization of Discrete Port-Hamiltonian Dynamics via Interconnection and Damping Assignment. IEEE Control Syst Lett 5(1):103–108. https://doi.org/10.1109/lcsys.2020.300070](stabilization-of-discrete-port-hamiltonian-dynamics-via-interconnection-and-damping-assignment) -- [10.1109/lcsys.2020.3000705](https://doi.org/10.1109/lcsys.2020.3000705)
- [Tsolakis A, Keviczky T (2021) Distributed IDA-PBC for a Class of Nonholonomic Mechanical Systems. IFAC-PapersOnLine 54(14):275–280. https://doi.org/10.1016/j.ifacol.2021.10.36](distributed-ida-pbc-for-a-class-of-nonholonomic-mechanical-systems) -- [10.1016/j.ifacol.2021.10.365](https://doi.org/10.1016/j.ifacol.2021.10.365)
- [Gimenez J, Rosales C, Carelli R (2015) Port-hamiltonian modelling of a differential drive mobile robot with reference velocities as inputs. 2015 XVI Workshop on Information Processing and Control (RPIC) 1–](port-hamiltonian-modelling-of-a-differential-drive-mobile-robot-with-reference-velocities-as-inputs) -- [10.1109/rpic.2015.7497079](https://doi.org/10.1109/rpic.2015.7497079)
- Nahata P, Turan MS, Ferrari-Trecate G (2022) Consensus-Based Current Sharing and Voltage Balancing in DC Microgrids With Exponential Loads. IEEE Trans Contr Syst Technol 30(4):1668–1680. https://doi.org/10.1109/tcst.2021.312032 -- [10.1109/tcst.2021.3120321](https://doi.org/10.1109/tcst.2021.3120321)
- Otten, Power sharing in DC microgrids. (2020)
- [Strehle F, Pfeifer M, Malan AJ, Krebs S, Hohmann S (2020) A Scalable Port-Hamiltonian Approach to Plug-and-Play Voltage Stabilization in DC Microgrids. 2020 IEEE Conference on Control Technology and Applications (CCTA) 787–79](a-scalable-port-hamiltonian-approach-to-plug-and-play-voltage-stabilization-in-dc-microgrids) -- [10.1109/ccta41146.2020.9206323](https://doi.org/10.1109/ccta41146.2020.9206323)
- Sontag ED, Wang Y (1999) Notions of input to output stability. Systems &amp; Control Letters 38(4–5):235–248. https://doi.org/10.1016/s0167-6911(99)00070- -- [10.1016/s0167-6911(99)00070-5](https://doi.org/10.1016/s0167-6911(99)00070-5)
- Meng L, Shafiee Q, Ferrari Trecate G, Karimi H, Fulwani D, Lu X, Guerrero JM (2017) Review on Control of DC Microgrids. IEEE J Emerg Sel Topics Power Electron :1–1. https://doi.org/10.1109/jestpe.2017.269021 -- [10.1109/jestpe.2017.2690219](https://doi.org/10.1109/jestpe.2017.2690219)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Poli, TorchDyn: A neural differential equations library. (2020)
- Kingma, Adam: A method for stochastic gradient descent. Proc. Int. Conf. Learn. Represent. (2015)

