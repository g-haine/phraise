---
layout: post
title: "MORpH: Model reduction of linear port-Hamiltonian systems in MATLAB"
date: 2023-06-06 00:00:00 +0100
permalink: morph-model-reduction-of-linear-port-hamiltonian-systems-in-matlab
year: 2023
authors: Tim Moser, Julius Durmann, Maximilian Bonauer, Boris Lohmann
category: articles
---
 
## Authors
[Tim Moser](authors/tim-moser), [Julius Durmann](authors/julius-durmann), [Maximilian Bonauer](authors/maximilian-bonauer), [Boris Lohmann](authors/boris-lohmann)
 
## Abstract
We present a novel software toolbox MORpH for the efficient storage, analysis, interconnection and structure-preserving model order reduction (MOR) of linear port-Hamiltonian differential-algebraic equation systems (pH-DAEs). The model class of pH-DAEs enables energy-based modeling and a flexible coupling of models across different physical domains. This makes them particularly suited for the simulation and control of complex technical systems. To promote the use of recent theoretical findings in engineering practice, efficient software solutions are required. In this work, we illustrate how possibly large-scale pH-DAEs can be efficiently stored and interconnected in MATLAB in an object-oriented way. We discuss three structure-preserving MOR strategies that are supported by MORpH and demonstrate the application and performance of selected MOR algorithms by means of two benchmark examples.
 
## Citation
- **Journal:** at - Automatisierungstechnik
- **Year:** 2023
- **Volume:** 71
- **Issue:** 6
- **Pages:** 476--489
- **Publisher:** Walter de Gruyter GmbH
- **DOI:** [10.1515/auto-2022-0119](https://doi.org/10.1515/auto-2022-0119)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Moser_2023,
  title={{MORpH: Model reduction of linear port-Hamiltonian systems in MATLAB}},
  volume={71},
  ISSN={2196-677X},
  DOI={10.1515/auto-2022-0119},
  number={6},
  journal={at - Automatisierungstechnik},
  publisher={Walter de Gruyter GmbH},
  author={Moser, Tim and Durmann, Julius and Bonauer, Maximilian and Lohmann, Boris},
  year={2023},
  pages={476--489}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/morph-model-reduction-of-linear-port-hamiltonian-systems-in-matlab.bib)
 
## References
- T. Breiten, R. Morandin, and P. Schulze, “Error bounds for port-Hamiltonian model and controller reduction based on system balancing,” arXiv Preprint arXiv:2012.15266, 2020.
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Liljegren-Sailer, B. & Marheineke, N. On Port-Hamiltonian Approximation of a Nonlinear Flow Problem on Networks. SIAM Journal on Scientific Computing vol. 44 B834–B859 (2022)](on-port-hamiltonian-approximation-of-a-nonlinear-flow-problem-on-networks) -- [10.1137/21m1443480](https://doi.org/10.1137/21m1443480)
- T. Moser, P. Schwerdtner, V. Mehrmann, and M. Voigt, “Structure-preserving model order reduction for index two port-Hamiltonian descriptor systems,” arXiv Preprint arXiv:2206.03942, 2022.
- K. Cherifi, H. Gernandt, and D. Hinsen, “The difference between port-Hamiltonian, passive and positive real descriptor systems,” arXiv Preprint arXiv:2204.04990, 2022.
- [Breiten, T. & Unger, B. Passivity preserving model reduction via spectral factorization. Automatica vol. 142 110368 (2022)](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- Ionutiu, R., Rommes, J. & Antoulas, A. C. Passivity-Preserving Model Reduction Using Dominant Spectral-Zero Interpolation. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems vol. 27 2250–2263 (2008) -- [10.1109/tcad.2008.2006160](https://doi.org/10.1109/tcad.2008.2006160)
- Unneland, K., Van Dooren, P. & Egeland, O. A Novel Scheme for Positive Real Balanced Truncation. 2007 American Control Conference 947–952 (2007) doi:10.1109/acc.2007.4282863 -- [10.1109/acc.2007.4282863](https://doi.org/10.1109/acc.2007.4282863)
- Grivet‐Talocia, S. & Gustavsen, B. Passive Macromodeling. (2015) doi:10.1002/9781119140931 -- [10.1002/9781119140931](https://doi.org/10.1002/9781119140931)
- Milk, R., Rave, S. & Schindler, F. pyMOR -- Generic Algorithms and Interfaces for Model Order Reduction. SIAM Journal on Scientific Computing vol. 38 S194–S216 (2016) -- [10.1137/15m1026614](https://doi.org/10.1137/15m1026614)
- Castagnotto, A., Varona, M. C., Jeschek, L. & Lohmann, B. sss &amp; sssMOR: Analysis and reduction of large-scale dynamic systems in MATLAB. at - Automatisierungstechnik vol. 65 134–150 (2017) -- [10.1515/auto-2016-0137](https://doi.org/10.1515/auto-2016-0137)
- Benner, P. & Werner, S. W. R. MORLAB—The Model Order Reduction LABoratory. International Series of Numerical Mathematics 393–415 (2021) doi:10.1007/978-3-030-72983-7_19 -- [10.1007/978-3-030-72983-7_19](https://doi.org/10.1007/978-3-030-72983-7_19)
- [Gillis, N. & Sharma, P. Finding the Nearest Positive-Real System. SIAM Journal on Numerical Analysis vol. 56 1022–1047 (2018)](finding-the-nearest-positive-real-system) -- [10.1137/17m1137176](https://doi.org/10.1137/17m1137176)
- [Beattie, C., Mehrmann, V., Xu, H. & Zwart, H. Linear port-Hamiltonian descriptor systems. Mathematics of Control, Signals, and Systems vol. 30 (2018)](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- [Hauschild, S.-A., Marheineke, N. & Mehrmann, V. Model reduction techniques for port‐Hamiltonian differential‐algebraic systems. PAMM vol. 19 (2019)](model-reduction-techniques-for-port-hamiltonian-differential-algebraic-systems) -- [10.1002/pamm.201900040](https://doi.org/10.1002/pamm.201900040)
- [Güdücü, C., Liesen, J., Mehrmann, V. & Szyld, D. B. On Non-Hermitian Positive (Semi)Definite Linear Algebraic Systems Arising from Dissipative Hamiltonian DAEs. SIAM Journal on Scientific Computing vol. 44 A2871–A2894 (2022)](on-non-hermitian-positive-semi-definite-linear-algebraic-systems-arising-from-dissipative-hamiltonian-daes) -- [10.1137/21m1458594](https://doi.org/10.1137/21m1458594)
- Achleitner, F., Arnold, A. & Mehrmann, V. Hypocoercivity and controllability in linear semi‐dissipative Hamiltonian ordinary differential equations and differential‐algebraic equations. ZAMM - Journal of Applied Mathematics and Mechanics / Zeitschrift für Angewandte Mathematik und Mechanik vol. 103 (2021) -- [10.1002/zamm.202100171](https://doi.org/10.1002/zamm.202100171)
- Realization and Model Reduction of Dynamical Systems. (Springer International Publishing, 2022). doi:10.1007/978-3-030-95157-3 -- [10.1007/978-3-030-95157-3](https://doi.org/10.1007/978-3-030-95157-3)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Willems, J. C. Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Archive for Rational Mechanics and Analysis vol. 45 352–393 (1972) -- [10.1007/bf00276494](https://doi.org/10.1007/bf00276494)
- B. D. O. Anderson and S. Vongpanitlerd, Network Analysis and Synthesis – A Modern Systems Theory Approach, Englewood Cliffs, NJ, Prentice-Hall, 1973.
- [Polyuga, R. V. & van der Schaft, A. J. Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Systems &amp; Control Letters vol. 61 412–421 (2012)](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- [Polyuga, R. V. & van der Schaft, A. Structure Preserving Moment Matching for Port-Hamiltonian Systems: Arnoldi and Lanczos. IEEE Transactions on Automatic Control vol. 56 1458–1462 (2011)](structure-preserving-moment-matching-for-port-hamiltonian-systems-arnoldi-and-lanczos) -- [10.1109/tac.2011.2128650](https://doi.org/10.1109/tac.2011.2128650)
- Moser, T., Durmann, J. & Lohmann, B. Surrogate-Based ℋ2 Model Reduction of Port-Hamiltonian Systems. 2021 European Control Conference (ECC) 2058–2065 (2021) doi:10.23919/ecc54610.2021.9655109 -- [10.23919/ecc54610.2021.9655109](https://doi.org/10.23919/ecc54610.2021.9655109)
- Druskin, V. & Simoncini, V. Adaptive rational Krylov subspaces for large-scale dynamical systems. Systems &amp; Control Letters vol. 60 546–560 (2011) -- [10.1016/j.sysconle.2011.04.013](https://doi.org/10.1016/j.sysconle.2011.04.013)
- Druskin, V., Simoncini, V. & Zaslavsky, M. Adaptive Tangential Interpolation in Rational Krylov Subspaces for MIMO Dynamical Systems. SIAM Journal on Matrix Analysis and Applications vol. 35 476–498 (2014) -- [10.1137/120898784](https://doi.org/10.1137/120898784)
- [Sato, K. Riemannian optimal model reduction of linear port-Hamiltonian systems. Automatica vol. 93 428–434 (2018)](riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
- Moser, T. & Lohmann, B. A New Riemannian Framework for Efficient ℋ2-Optimal Model Reduction of Port-Hamiltonian Systems. 2020 59th IEEE Conference on Decision and Control (CDC) 5043–5049 (2020) doi:10.1109/cdc42340.2020.9304134 -- [10.1109/cdc42340.2020.9304134](https://doi.org/10.1109/cdc42340.2020.9304134)
- P. Schwerdtner and M. Voigt, “Structure preserving model order reduction by parameter optimization,” arXiv Preprint arXiv:2011.07567, 2020.
- Desai, U. & Pal, D. A transformation approach to stochastic model reduction. IEEE Transactions on Automatic Control vol. 29 1097–1100 (1984) -- [10.1109/tac.1984.1103438](https://doi.org/10.1109/tac.1984.1103438)
- Phillips, J., Daniel, L. & Miguel Silveira, L. Guaranteed passive balancing transformations for model order reduction. Proceedings 2002 Design Automation Conference (IEEE Cat. No.02CH37324) 52–57 (2002) doi:10.1109/dac.2002.1012593 -- [10.1109/dac.2002.1012593](https://doi.org/10.1109/dac.2002.1012593)
- T. Moser and B. Lohmann, “A Rosenbrock framework for tangential interpolation of port-Hamiltonian descriptor systems,” arXiv Preprint arXiv:2210.16071, 2022.
- P. Schwerdtner, T. Moser, V. Mehrmann, and M. Voigt, “Structure-preserving model order reduction for index one port-Hamiltonian descriptor systems,” arXiv Preprint arXiv:2206.01608, 2022.
- Flagg, G., Beattie, C. A. & Gugercin, S. Interpolatory model reduction. Systems &amp; Control Letters vol. 62 567–574 (2013) -- [10.1016/j.sysconle.2013.03.006](https://doi.org/10.1016/j.sysconle.2013.03.006)
- Castagnotto, A., Beattie, C. & Gugercin, S. Interpolatory Methods for $\mathcal{H}_{\infty }$ Model Reduction of Multi-Input/Multi-Output Systems. MS&amp;A 349–365 (2017) doi:10.1007/978-3-319-58786-8_22 -- [10.1007/978-3-319-58786-8_22](https://doi.org/10.1007/978-3-319-58786-8_22)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Transactions on Circuits and Systems I: Regular Papers vol. 51 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- T. Moser, “Benchmark systems and code for article: MORpH: model reduction of linear port-Hamiltonian systems in MATLAB,” 2022. https://doi.org/10.5281/zenodo.7081776.
- Benner, P., Bujanović, Z., Kürschner, P. & Saak, J. RADI: a low-rank ADI-type algorithm for large scale algebraic Riccati equations. Numerische Mathematik vol. 138 301–330 (2017) -- [10.1007/s00211-017-0907-5](https://doi.org/10.1007/s00211-017-0907-5)
- J. Saak, M. Köhler, and P. Benner, M-M.E.S.S.-2.1 – The Matrix Equations Sparse Solvers Library, 2022. Available at: https://www.mpi-magdeburg.mpg.de/projects/mess.
- N. Boumal, B. Mishra, P. A. Absil, and R. Sepulchre, “Manopt, a matlab toolbox for optimization on manifolds,” J. Mach. Learn. Res., vol. 15, no. 42, pp. 1455–1459, 2014.
- Curtis, F. E., Mitchell, T. & Overton, M. L. A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles. Optimization Methods and Software vol. 32 148–181 (2016) -- [10.1080/10556788.2016.1208749](https://doi.org/10.1080/10556788.2016.1208749)
- Rommes, J. & Martins, N. Efficient Computation of Transfer Function Dominant Poles Using Subspace Acceleration. IEEE Transactions on Power Systems vol. 21 1218–1226 (2006) -- [10.1109/tpwrs.2006.876671](https://doi.org/10.1109/tpwrs.2006.876671)
- Rommes, J. & Martins, N. Efficient Computation of Multivariable Transfer Function Dominant Poles Using Subspace Acceleration. IEEE Transactions on Power Systems vol. 21 1471–1483 (2006) -- [10.1109/tpwrs.2006.881154](https://doi.org/10.1109/tpwrs.2006.881154)
- M. Grant and S. Boyd, “CVX: matlab software for disciplined convex programming, version 2.1,” 2014. Available at: http://cvxr.com/cvx.
- Grant, M. C. & Boyd, S. P. Graph Implementations for Nonsmooth Convex Programs. Lecture Notes in Control and Information Sciences 95–110 doi:10.1007/978-1-84800-155-8_7 -- [10.1007/978-1-84800-155-8_7](https://doi.org/10.1007/978-1-84800-155-8_7)
- J. Löfberg, “YALMIP: a toolbox for modeling and optimization in MATLAB,” in Proceedings of the CACSD Conference, Taipei, Taiwan, 2004.
- Aliyev, N., Benner, P., Mengi, E., Schwerdtner, P. & Voigt, M. Large-Scale Computation of $\mathcal{L}_\infty$-Norms by a Greedy Subspace Method. SIAM Journal on Matrix Analysis and Applications vol. 38 1496–1516 (2017) -- [10.1137/16m1086200](https://doi.org/10.1137/16m1086200)
- Schwerdtner, P. & Voigt, M. Computation of the $L^\infty$-Norm Using Rational Interpolation. IFAC-PapersOnLine vol. 51 84–89 (2018) -- [10.1016/j.ifacol.2018.11.086](https://doi.org/10.1016/j.ifacol.2018.11.086)
- Benner, P. & Voigt, M. A structured pseudospectral method for $\mathcal {H}_\infty$-norm computation of large-scale descriptor systems. Mathematics of Control, Signals, and Systems vol. 26 303–338 (2013) -- [10.1007/s00498-013-0121-7](https://doi.org/10.1007/s00498-013-0121-7)

