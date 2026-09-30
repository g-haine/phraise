---
title: "Port-Hamiltonian Dynamic Mode Decomposition"
date: 2023-07-12 00:00:00 +0100
permalink: port-hamiltonian-dynamic-mode-decomposition
year: 2023
authors: Riccardo Morandin, Jonas Nicodemus, Benjamin Unger
category: articles
---
 
## Authors
[Riccardo Morandin](authors/riccardo-morandin), [Jonas Nicodemus](authors/jonas-nicodemus), [Benjamin Unger](authors/benjamin-unger)
 
## Abstract
We present a novel physics-informed system identification method to construct a passive linear time-invariant system. In more detail, for a given quadratic energy functional, measurements of the input, state, and output of a system in the time domain, we find a realization that approximates the data well while guaranteeing that the energy functional satisfies a dissipation inequality. To this end, we use the framework of port-Hamiltonian (pH) systems and modify the dynamic mode decomposition, respectively, operator inference, to be feasible for continuous-time pH systems. We propose an iterative numerical method to solve the corresponding least-squares minimization problem. We construct an effective initialization of the algorithm by studying the least-squares problem in a weighted norm, for which we present the analytical minimum-norm solution. The efficiency of the proposed method is demonstrated with several numerical examples.
 
## Citation
- **Journal:** SIAM Journal on Scientific Computing
- **Year:** 2023
- **Volume:** 45
- **Issue:** 4
- **Pages:** A1690--A1710
- **Publisher:** Society for Industrial & Applied Mathematics (SIAM)
- **DOI:** [10.1137/22m149329x](https://doi.org/10.1137/22m149329x)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Morandin_2023,
  title={{Port-Hamiltonian Dynamic Mode Decomposition}},
  volume={45},
  ISSN={1095-7197},
  DOI={10.1137/22m149329x},
  number={4},
  journal={SIAM Journal on Scientific Computing},
  publisher={Society for Industrial & Applied Mathematics (SIAM)},
  author={Morandin, Riccardo and Nicodemus, Jonas and Unger, Benjamin},
  year={2023},
  pages={A1690--A1710}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-dynamic-mode-decomposition.bib)
 
## References
- [Altmann R, Mehrmann V, Unger B (2021) Port-Hamiltonian formulations of poroelastic network models. Mathematical and Computer Modelling of Dynamical Systems 27(1):429–452. https://doi.org/10.1080/13873954.2021.1975137](port-hamiltonian-formulations-of-poroelastic-network-models) -- [10.1080/13873954.2021.1975137](https://doi.org/10.1080/13873954.2021.1975137)
- Annoni J, Gebraad P, Seiler P (2016) Wind farm flow modeling using an input-output reduced-order model. In: 2016 American Control Conference (ACC). IEEE, pp 506–512 -- [10.1109/acc.2016.7524964](https://doi.org/10.1109/acc.2016.7524964)
- Antoulas AC, Lefteriu S, Ionita AC (2017) Chapter 8: A Tutorial Introduction to the Loewner Framework for Model Reduction. In: Model Reduction and Approximation. Society for Industrial and Applied Mathematics, Philadelphia, PA, pp 335–376 -- [10.1137/1.9781611974829.ch8](https://doi.org/10.1137/1.9781611974829.ch8)
- P. J. Baddoo , 
B. Herrmann , 
B. J. McKeon , 
J. N. Kutz , and 
S. L. Brunton , Physics-Informed Dynamic Mode Decomposition (piDMD), 2021, https://royalsocietypublishing.org/doi/10.1098/rspa.2022.0576.
- [Beattie CA, Mehrmann V, Van Dooren P (2019) Robust port-Hamiltonian representations of passive systems. Automatica 100:182–186. https://doi.org/10.1016/j.automatica.2018.11.013](robust-port-hamiltonian-representations-of-passive-systems) -- [10.1016/j.automatica.2018.11.013](https://doi.org/10.1016/j.automatica.2018.11.013)
- [Beattie C, Mehrmann V, Xu H, Zwart H (2018) Linear port-Hamiltonian descriptor systems. Math Control Signals Syst 30(4):17. https://doi.org/10.1007/s00498-018-0223-3](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- Benner P, Goyal P, Heiland J, Duff IP (2021) Operator inference and physics-informed learning of low-dimensional models for incompressible flows. etna 56:28–51. https://doi.org/10.1553/etna_vol56s28 -- [10.1553/etna_vol56s28](https://doi.org/10.1553/etna_vol56s28)
- [Benner P, Goyal P, Van Dooren P (2020) Identification of port-Hamiltonian systems from frequency response data. Systems & Control Letters 143:104741. https://doi.org/10.1016/j.sysconle.2020.104741](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- Benner P, Himpe C, Mitchell T (2018) On reduced input-output dynamic mode decomposition. Adv Comput Math 44(6):1751–1768. https://doi.org/10.1007/s10444-018-9592-x -- [10.1007/s10444-018-9592-x](https://doi.org/10.1007/s10444-018-9592-x)
- Borja P., IEEE Trans. Automat. Control (2021)
- [Breiten T, Morandin R, Schulze P (2022) Error bounds for port-Hamiltonian model and controller reduction based on system balancing. Computers & Mathematics with Applications 116:100–115. https://doi.org/10.1016/j.camwa.2021.07.022](error-bounds-for-port-hamiltonian-model-and-controller-reduction-based-on-system-balancing) -- [10.1016/j.camwa.2021.07.022](https://doi.org/10.1016/j.camwa.2021.07.022)
- [Breiten T, Unger B (2022) Passivity preserving model reduction via spectral factorization. Automatica 142:110368. https://doi.org/10.1016/j.automatica.2022.110368](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- R. T. Q. Chen , 
Y. Rubanova , 
J. Bettencourt , and 
D. Duvenaud , Neural ordinary differential equations, in Proceedings of the 32nd Conference on Neural Information Processing Systems, NeurIPS, 2018; also available online from https://proceedings.neurips.cc/paper/2018/file/69386f6bb1dfed68692a24c8686939b9-Paper.pdf.
- K. Cherifi , 
V. Mehrmann , and 
K. Hariche , Numerical Methods to Compute a Minimal Realization of a Port-Hamiltonian System, http://arxiv.org/abs/1903.07042, 2019.
- Deng Y-B, Hu X-Y, Zhang L (2003) Least Squares Solution of \\(BXA^{T}=T\\) over Symmetric, Skew-Symmetric, and Positive Semidefinite \\(X\\). SIAM J Matrix Anal Appl 25(2):486–494. https://doi.org/10.1137/s0895479802402491 -- [10.1137/s0895479802402491](https://doi.org/10.1137/s0895479802402491)
- [Gillis N, Sharma P (2017) On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica 85:113–121. https://doi.org/10.1016/j.automatica.2017.07.047](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- Gillis N, Sharma P (2018) A semi-analytical approach for the positive semidefinite Procrustes problem. Linear Algebra and its Applications 540:112–137. https://doi.org/10.1016/j.laa.2017.11.023 -- [10.1016/j.laa.2017.11.023](https://doi.org/10.1016/j.laa.2017.11.023)
- [Gugercin S, Polyuga RV, Beattie C, van der Schaft A (2012) Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9):1963–1974. https://doi.org/10.1016/j.automatica.2012.05.052](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Gustavsen B, Semlyen A (1999) Rational approximation of frequency domain responses by vector fitting. IEEE Trans Power Delivery 14(3):1052–1061. https://doi.org/10.1109/61.772353 -- [10.1109/61.772353](https://doi.org/10.1109/61.772353)
- Heiland J, Unger B (2022) Identification of Linear Time-Invariant Systems with Dynamic Mode Decomposition. Mathematics 10(3):418. https://doi.org/10.3390/math10030418 -- [10.3390/math10030418](https://doi.org/10.3390/math10030418)
- Higham N. J., Matrix Nearness Problems and Applications (1988)
- Hillebrecht B, Unger B (2022) Certified machine learning: A posteriori error estimation for physics-informed neural networks. In: 2022 International Joint Conference on Neural Networks (IJCNN). IEEE, pp 1–8 -- [10.1109/ijcnn55064.2022.9892569](https://doi.org/10.1109/ijcnn55064.2022.9892569)
- B. Hillebrecht  and 
B. Unger , Certified Machine Learning: Rigorous A Posteriori Error Bounds for PDE Defined PINNs, http://arxiv.org/abs/2210.03426, 2022.
- [Jacob B, Zwart HJ (2012) Linear Port-Hamiltonian Systems on Infinite-dimensional Spaces. Springer Basel, Basel](linear-port-hamiltonian-systems-on-infinite-dimensional-spaces) -- [10.1007/978-3-0348-0399-1](https://doi.org/10.1007/978-3-0348-0399-1)
- Juang J-N, Pappa RS (1985) An eigensystem realization algorithm for modal parameter identification and model reduction. Journal of Guidance, Control, and Dynamics 8(5):620–627. https://doi.org/10.2514/3.20031 -- [10.2514/3.20031](https://doi.org/10.2514/3.20031)
- Karniadakis GE, Kevrekidis IG, Lu L, Perdikaris P, Wang S, Yang L (2021) Physics-informed machine learning. Nat Rev Phys 3(6):422–440. https://doi.org/10.1038/s42254-021-00314-5 -- [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5)
- [Kotyczka P, Lefèvre L (2018) Discrete-time port-Hamiltonian systems based on Gauss-Legendre collocation ⁎ ⁎P. Kotyczka received financial support as a part-time post-doctoral researcher (03/17–08/17) from the DFG-ANR funded project INFI-DHEM (no ANR-16-CE92-0028) and by a part-time visiting fellowship of Grenoble INP in summer term 2017. The work makes also part of the project KO 4750/1-1, funded by the German Research Foundation (DFG). IFAC-PapersOnLine 51(3):125–130. https://doi.org/10.1016/j.ifacol.2018.06.035](discrete-time-port-hamiltonian-systems-based-on-gauss-legendre-collocation) -- [10.1016/j.ifacol.2018.06.035](https://doi.org/10.1016/j.ifacol.2018.06.035)
- Kutz JN, Brunton SL, Brunton BW, Proctor JL (2016) Dynamic Mode Decomposition. Society for Industrial and Applied Mathematics, Philadelphia, PA -- [10.1137/1.9781611974508](https://doi.org/10.1137/1.9781611974508)
- Mayo AJ, Antoulas AC (2007) A framework for the solution of the generalized realization problem. Linear Algebra and its Applications 425(2-3):634–662. https://doi.org/10.1016/j.laa.2007.03.008 -- [10.1016/j.laa.2007.03.008](https://doi.org/10.1016/j.laa.2007.03.008)
- [Mehrmann V, Morandin R (2019) Structure-preserving discretization for port-Hamiltonian descriptor systems. In: 2019 IEEE 58th Conference on Decision and Control (CDC). IEEE, pp 6863–6868](structure-preserving-discretization-for-port-hamiltonian-descriptor-systems) -- [10.1109/cdc40024.2019.9030180](https://doi.org/10.1109/cdc40024.2019.9030180)
- V. Mehrmann  and 
B. Unger , Control of Port-Hamiltonian Differential-Algebraic Systems and Applications, http://arxiv.org/abs/2201.06590, 2022.
- [Moser T, Lohmann B (2020) A New Riemannian Framework for Efficient \\(\mathcal{H}_{2}\\)-Optimal Model Reduction of Port-Hamiltonian Systems. In: 2020 59th IEEE Conference on Decision and Control (CDC). IEEE, pp 5043–5049](a-new-riemannian-framework-for-efficient-h-sub-2-sub-optimal-model-reduction-of-port-hamiltonian-systems) -- [10.1109/cdc42340.2020.9304134](https://doi.org/10.1109/cdc42340.2020.9304134)
- Nesterov Y., Introductory Lectures on Convex Optimization: A Basic Course (2003)
- Peherstorfer B, Gugercin S, Willcox K (2017) Data-Driven Reduced Model Construction with Time-Domain Loewner Models. SIAM J Sci Comput 39(5):A2152–A2178. https://doi.org/10.1137/16m1094750 -- [10.1137/16m1094750](https://doi.org/10.1137/16m1094750)
- Peherstorfer B, Willcox K (2016) Data-driven operator inference for nonintrusive projection-based model reduction. Computer Methods in Applied Mechanics and Engineering 306:196–215. https://doi.org/10.1016/j.cma.2016.03.025 -- [10.1016/j.cma.2016.03.025](https://doi.org/10.1016/j.cma.2016.03.025)
- [Polyuga RV, van der Schaft A (2011) Structure Preserving Moment Matching for Port-Hamiltonian Systems: Arnoldi and Lanczos. IEEE Trans Automat Contr 56(6):1458–1462. https://doi.org/10.1109/tac.2011.2128650](structure-preserving-moment-matching-for-port-hamiltonian-systems-arnoldi-and-lanczos) -- [10.1109/tac.2011.2128650](https://doi.org/10.1109/tac.2011.2128650)
- [Polyuga RV, van der Schaft AJ (2012) Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Systems & Control Letters 61(3):412–421. https://doi.org/10.1016/j.sysconle.2011.12.008](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- Proctor JL, Brunton SL, Kutz JN (2016) Dynamic Mode Decomposition with Control. SIAM J Appl Dyn Syst 15(1):142–161. https://doi.org/10.1137/15m1013857 -- [10.1137/15m1013857](https://doi.org/10.1137/15m1013857)
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.045 -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Sato K, Sato H (2018) Structure-Preserving $H^2$ Optimal Model Reduction Based on the Riemannian Trust-Region Method. IEEE Trans Automat Contr 63(2):505–512. https://doi.org/10.1109/tac.2017.2723259 -- [10.1109/tac.2017.2723259](https://doi.org/10.1109/tac.2017.2723259)
- SCHMID PJ (2010) Dynamic mode decomposition of numerical and experimental data. J Fluid Mech 656:5–28. https://doi.org/10.1017/s0022112010001217 -- [10.1017/s0022112010001217](https://doi.org/10.1017/s0022112010001217)
- Schulze P, Unger B (2016) Data-driven interpolation of dynamical systems with delay. Systems & Control Letters 97:125–131. https://doi.org/10.1016/j.sysconle.2016.09.007 -- [10.1016/j.sysconle.2016.09.007](https://doi.org/10.1016/j.sysconle.2016.09.007)
- Schulze P, Unger B, Beattie C, Gugercin S (2018) Data-driven structured realization. Linear Algebra and its Applications 537:250–286. https://doi.org/10.1016/j.laa.2017.09.030 -- [10.1016/j.laa.2017.09.030](https://doi.org/10.1016/j.laa.2017.09.030)
- P. Schwerdtner , Port-Hamiltonian System Identification from Noisy Frequency Response Data, https://arxiv.org/abs/2106.11355, 2021.
- P. Schwerdtner  and 
M. Voigt , SOBMOR: Structured Optimization-Based Model Order Reduction, https://arxiv.org/abs/2011.07567, 2020.
- [Schwerdtner P, Voigt M (2021) Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine 54(19):143–148. https://doi.org/10.1016/j.ifacol.2021.11.069](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- H. Sharma  and 
B. Kramer , Preserving Lagrangian Structure in Data-Driven Reduced-Order Modeling of Large-Scale Mechanical Systems, http://arxiv.org/abs/2203.06361, 2022.
- Sharma H, Wang Z, Kramer B (2022) Hamiltonian operator inference: Physics-preserving learning of reduced-order models for canonical Hamiltonian systems. Physica D: Nonlinear Phenomena 431:133122. https://doi.org/10.1016/j.physd.2021.133122 -- [10.1016/j.physd.2021.133122](https://doi.org/10.1016/j.physd.2021.133122)
- Tu JH, Rowley CW, Luchtenburg DM, Brunton SL, Kutz JN (2014) On dynamic mode decomposition:  Theory and applications. JCD 1(2):391–421. https://doi.org/10.3934/jcd.2014.1.391 -- [10.3934/jcd.2014.1.391](https://doi.org/10.3934/jcd.2014.1.391)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2-3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Werner SWR, Gosea IV, Gugercin S (2022) Structured vector fitting framework for mechanical systems. IFAC-PapersOnLine 55(20):163–168. https://doi.org/10.1016/j.ifacol.2022.09.089 -- [10.1016/j.ifacol.2022.09.089](https://doi.org/10.1016/j.ifacol.2022.09.089)
- [Wolf T, Lohmann B, Eid R, Kotyczka P (2010) Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control 16(4):401–406. https://doi.org/10.3166/ejc.16.401-406](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)

