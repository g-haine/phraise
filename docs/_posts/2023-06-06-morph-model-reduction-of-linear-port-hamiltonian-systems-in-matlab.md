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
 
## References
- T. Breiten, R. Morandin, and P. Schulze, “Error bounds for port-Hamiltonian model and controller reduction based on system balancing,” arXiv Preprint arXiv:2012.15266, 2020.
- [S. Chaturantabut, C. Beattie, and S. Gugercin, “Structure-preserving model reduction for nonlinear port-Hamiltonian systems,” SIAM J. Sci. Comput., vol. 38, no. 5, pp. B837–B865, 2016. https://doi.org/10.1137/15m1055085.](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15M1055085](https://doi.org/10.1137/15M1055085)
- [S. Gugercin, R. V. Polyuga, C. Beattie, and A. van der Schaft, “Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems,” Automatica, vol. 48, no. 9, pp. 1963–1974, 2012. https://doi.org/10.1016/j.automatica.2012.05.052.](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [B. Liljegren-Sailer and N. Marheineke, “On port-Hamiltonian approximation of a nonlinear flow problem on networks,” SIAM J. Sci. Comput., vol. 44, no. 3, pp. B834–B859, 2022. https://doi.org/10.1137/21m1443480.](on-port-hamiltonian-approximation-of-a-nonlinear-flow-problem-on-networks) -- [10.1137/21M1443480](https://doi.org/10.1137/21M1443480)
- T. Moser, P. Schwerdtner, V. Mehrmann, and M. Voigt, “Structure-preserving model order reduction for index two port-Hamiltonian descriptor systems,” arXiv Preprint arXiv:2206.03942, 2022.
- K. Cherifi, H. Gernandt, and D. Hinsen, “The difference between port-Hamiltonian, passive and positive real descriptor systems,” arXiv Preprint arXiv:2204.04990, 2022.
- [T. Breiten and B. Unger, “Passivity preserving model reduction via spectral factorization,” Automatica, vol. 142, p. 110368, 2022. https://doi.org/10.1016/j.automatica.2022.110368.](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- R. Ionutiu, J. Rommes, and A. C. Antoulas, “Passivity-preserving model reduction using dominant spectral-zero interpolation,” IEEE Trans. Comput. Aided Des. Integrated Circ. Syst., vol. 27, no. 12, pp. 2250–2263, 2008. https://doi.org/10.1109/tcad.2008.2006160. -- [10.1109/TCAD.2008.2006160](https://doi.org/10.1109/TCAD.2008.2006160)
- K. Unneland, P. Van Dooren, and O. Egeland, “A novel scheme for positive real balanced truncation,” in 2007 American Control Conference, 2007, pp. 947–952. -- [10.1109/ACC.2007.4282863](https://doi.org/10.1109/ACC.2007.4282863)
- S. Grivet-Talocia and B. Gustavsen, Passive Macromodeling: Theory and Applications, Hoboken, NJ, John Wiley & Sons, Inc., 2016. -- [10.1002/9781119140931](https://doi.org/10.1002/9781119140931)
- R. Milk, S. Rave, and F. Schindler, “pyMOR – generic algorithms and interfaces for model order reduction,” SIAM J. Sci. Comput., vol. 38, no. 5, pp. S194–S216, 2016. https://doi.org/10.1137/15m1026614. -- [10.1137/15M1026614](https://doi.org/10.1137/15M1026614)
- A. Castagnotto, M. Cruz Varona, L. Jeschek, and B. Lohmann, “sss & sssMOR: analysis and reduction of large-scale dynamic systems in MATLAB,” Automatisierungstechnik, vol. 65, no. 2, pp. 134–150, 2017. https://doi.org/10.1515/auto-2016-0137. -- [10.1515/auto-2016-0137](https://doi.org/10.1515/auto-2016-0137)
- P. Benner and S. W. R. Werner, “MORLAB—the model order reduction LABoratory,” in Model Reduction of Complex Dynamical Systems, P. Benner, T. Breiten, H. Faßbender, M. Hinze, T. Stykel, and R. Zimmermann, Eds., Cham, Springer International Publishing, 2021, pp. 393–415. -- [10.1007/978-3-030-72983-7_19](https://doi.org/10.1007/978-3-030-72983-7_19)
- [N. Gillis and P. Sharma, “Finding the nearest positive-real system,” SIAM J. Numer. Anal., vol. 56, no. 2, pp. 1022–1047, 2018. https://doi.org/10.1137/17m1137176.](finding-the-nearest-positive-real-system) -- [10.1137/17M1137176](https://doi.org/10.1137/17M1137176)
- [C. Beattie, V. Mehrmann, H. Xu, and H. Zwart, “Linear port-Hamiltonian descriptor systems,” Math. Control Signals Syst., vol. 30, no. 17, pp. 1–27, 2018. https://doi.org/10.1007/s00498-018-0223-3.](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- [S. A. Hauschild, N. Marheineke, and V. Mehrmann, “Model reduction techniques for linear constant coefficient port-Hamiltonian differential-algebraic systems,” Control Cybern., vol. 48, no. 1, pp. 125–152, 2019.](model-reduction-techniques-for-port-hamiltonian-differential-algebraic-systems) -- [10.1002/pamm.201900040](https://doi.org/10.1002/pamm.201900040)
- C. Güdücü, J. Liesen, V. Mehrmann, and D. B. Szyld, “On non-Hermitian positive (semi)definite linear algebraic systems arising from dissipative Hamiltonian DAEs,” arXiv Preprint arXiv:2111.05616, 2021. -- [10.1137/21M1458594](https://doi.org/10.1137/21M1458594)
- F. Achleitner, A. Arnold, and V. Mehrmann, “Hypocoercivity and controllability in linear semi-dissipative Hamiltonian ordinary differential equations and differential-algebraic equations,” ZAMM Z. fur Angew. Math. Mech., 2021. https://doi.org/10.1002/zamm.202100171. -- [10.1002/zamm.202100171](https://doi.org/10.1002/zamm.202100171)
- C. A. Beattie, S. Gugercin, and V. Mehrmann, “Structure-preserving interpolatory model reduction for port-Hamiltonian differential-algebraic systems,” in Realization and Model Reduction of Dynamical Systems: A Festschrift in Honor of the 70th Birthday of Thanos Antoulas, C. Beattie, P. Benner, M. Embree, S. Gugercin, and S. Lefteriu, Eds., Cham, Springer, 2022. -- [10.1007/978-3-030-95157-3](https://doi.org/10.1007/978-3-030-95157-3)
- [V. Duindam, A. Macchelli, S. Stramigioli, and H. Bruyninckx, Modeling and Control of Complex Physical Systems, Berlin, Heidelberg, Springer-Verlag, 2009.](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- J. C. Willems, “Dissipative dynamical systems Part II: linear systems with quadratic supply rates,” Arch. Ration. Mech. Anal., vol. 45, no. 5, pp. 352–393, 1972. https://doi.org/10.1007/bf00276494. -- [10.1007/BF00276494](https://doi.org/10.1007/BF00276494)
- B. D. O. Anderson and S. Vongpanitlerd, Network Analysis and Synthesis – A Modern Systems Theory Approach, Englewood Cliffs, NJ, Prentice-Hall, 1973.
- [R. V. Polyuga and A. van der Schaft, “Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems,” Syst. Control Lett., vol. 61, no. 3, pp. 412–421, 2012. https://doi.org/10.1016/j.sysconle.2011.12.008.](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- [R. V. Polyuga and A. van der Schaft, “Structure preserving moment matching for port-Hamiltonian systems: Arnoldi and Lanczos,” IEEE Trans. Automat. Control, vol. 56, no. 6, pp. 1458–1462, 2011. https://doi.org/10.1109/tac.2011.2128650.](structure-preserving-moment-matching-for-port-hamiltonian-systems-arnoldi-and-lanczos) -- [10.1109/TAC.2011.2128650](https://doi.org/10.1109/TAC.2011.2128650)
- T. Moser, J. Durmann, and B. Lohmann, “Surrogate-based H2${\mathcal{H}}_{2}$ model reduction of port-Hamiltonian systems,” in 2021 Eur. Control Conf. (ECC), 2021, pp. 2058–2065. -- [10.23919/ECC54610.2021.9655109](https://doi.org/10.23919/ECC54610.2021.9655109)
- V. Druskin and V. Simoncini, “Adaptive rational Krylov subspaces for large-scale dynamical systems,” Syst. Control Lett., vol. 60, no. 8, pp. 546–560, 2011. https://doi.org/10.1016/j.sysconle.2011.04.013. -- [10.1016/j.sysconle.2011.04.013](https://doi.org/10.1016/j.sysconle.2011.04.013)
- V. Druskin, V. Simoncini, and M. Zaslavsky, “Adaptive tangential interpolation in rational Krylov subspaces for MIMO dynamical systems,” SIAM J. Matrix Anal. Appl., vol. 35, no. 2, pp. 476–498, 2014. https://doi.org/10.1137/120898784. -- [10.1137/120898784](https://doi.org/10.1137/120898784)
- [K. Sato, “Riemannian optimal model reduction of linear port-Hamiltonian systems,” Automatica J. IFAC, vol. 93, pp. 428–434, 2018. https://doi.org/10.1016/j.automatica.2018.03.051.](riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
- T. Moser and B. Lohmann, “A new Riemannian framework for efficient H2${\mathcal{H}}_{2}$-optimal model reduction of port-Hamiltonian systems,” in Proceedings of 59th IEEE Conference on Decisison and Control (CDC), Jeju Island, Republic of Korea, 2020, pp. 5043–5049. -- [10.1109/CDC42340.2020.9304134](https://doi.org/10.1109/CDC42340.2020.9304134)
- P. Schwerdtner and M. Voigt, “Structure preserving model order reduction by parameter optimization,” arXiv Preprint arXiv:2011.07567, 2020.
- U. Desai and D. Pal, “A transformation approach to stochastic model reduction,” IEEE Trans. Automat. Control, vol. 29, no. 12, pp. 1097–1100, 1984. https://doi.org/10.1109/tac.1984.1103438. -- [10.1109/TAC.1984.1103438](https://doi.org/10.1109/TAC.1984.1103438)
- J. Phillips, L. Daniel, and L. M. Silveira, “Guaranteed passive balancing transformations for model order reduction,” in Proceedings 2002 Design Automation Conference (IEEE Cat. No.02CH37324), 2002, pp. 52–57. -- [10.1109/DAC.2002.1012593](https://doi.org/10.1109/DAC.2002.1012593)
- T. Moser and B. Lohmann, “A Rosenbrock framework for tangential interpolation of port-Hamiltonian descriptor systems,” arXiv Preprint arXiv:2210.16071, 2022.
- P. Schwerdtner, T. Moser, V. Mehrmann, and M. Voigt, “Structure-preserving model order reduction for index one port-Hamiltonian descriptor systems,” arXiv Preprint arXiv:2206.01608, 2022.
- G. Flagg, C. A. Beattie, and S. Gugercin, “Interpolatory H∞${\mathcal{H}}_{\infty }$ model reduction,” Syst. Control Lett., vol. 627, pp. 567–574, 2013. https://doi.org/10.1016/j.sysconle.2013.03.006. -- [10.1016/j.sysconle.2013.03.006](https://doi.org/10.1016/j.sysconle.2013.03.006)
- A. Castagnotto, C. Beattie, and S. Gugercin, “Interpolatory methods for H∞${\mathcal{H}}_{\infty }$ model reduction of multi-input/multi-output systems,” in Modeling, Simulation and Applications, Cham, Springer International Publishing, 2017, pp. 349–365. -- [10.1007/978-3-319-58786-8_22](https://doi.org/10.1007/978-3-319-58786-8_22)
- S. Grivet-Talocia, “Passivity enforcement via perturbation of Hamiltonian matrices,” IEEE Trans. Circuits Syst. I: Regul. Pap, vol. 51, no. 9, pp. 1755–1769, 2004. https://doi.org/10.1109/tcsi.2004.834527. -- [10.1109/TCSI.2004.834527](https://doi.org/10.1109/TCSI.2004.834527)
- [V. Mehrmann and B. Unger, “Control of port-Hamiltonian differential-algebraic systems and applications,” arXiv Preprint arXiv:2201.06590, 2022.](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/S0962492922000083](https://doi.org/10.1017/S0962492922000083)
- T. Moser, “Benchmark systems and code for article: MORpH: model reduction of linear port-Hamiltonian systems in MATLAB,” 2022. https://doi.org/10.5281/zenodo.7081776.
- P. Benner, Z. Bujanovic, P. Kürschner, and J. Saak, “RADI: a low-rank ADI-type algorithm for large scale algebraic Riccati equations,” Numer. Math., vol. 138, no. 2, pp. 301–330, 2017. https://doi.org/10.1007/s00211-017-0907-5. -- [10.1007/s00211-017-0907-5](https://doi.org/10.1007/s00211-017-0907-5)
- J. Saak, M. Köhler, and P. Benner, M-M.E.S.S.-2.1 – The Matrix Equations Sparse Solvers Library, 2022. Available at: https://www.mpi-magdeburg.mpg.de/projects/mess.
- N. Boumal, B. Mishra, P. A. Absil, and R. Sepulchre, “Manopt, a matlab toolbox for optimization on manifolds,” J. Mach. Learn. Res., vol. 15, no. 42, pp. 1455–1459, 2014.
- F. E. Curtis, T. Mitchell, and M. L. Overton, “A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles,” Optim. Methods Software, vol. 32, no. 1, pp. 148–181, 2017. https://doi.org/10.1080/10556788.2016.1208749. -- [10.1080/10556788.2016.1208749](https://doi.org/10.1080/10556788.2016.1208749)
- J. Rommes and N. Martins, “Efficient computation of transfer function dominant poles using subspace acceleration,” IEEE Trans. Power Syst., vol. 21, no. 3, pp. 1218–1226, 2006. https://doi.org/10.1109/tpwrs.2006.876671. -- [10.1109/TPWRS.2006.876671](https://doi.org/10.1109/TPWRS.2006.876671)
- J. Rommes and N. Martins, “Efficient computation of multivariable transfer function dominant poles using subspace acceleration,” IEEE Trans. Power Syst., vol. 21, no. 4, pp. 1471–1483, 2006. https://doi.org/10.1109/tpwrs.2006.881154. -- [10.1109/TPWRS.2006.881154](https://doi.org/10.1109/TPWRS.2006.881154)
- M. Grant and S. Boyd, “CVX: matlab software for disciplined convex programming, version 2.1,” 2014. Available at: http://cvxr.com/cvx.
- M. Grant and S. Boyd, “Graph implementations for nonsmooth convex programs,” in Recent Advances in Learning and Control. Lecture Notes in Control and Information Sciences, V. Blondel, S. Boyd, and H. Kimura, Eds., London, Springer, 2008, pp. 95–110. -- [10.1007/978-1-84800-155-8_7](https://doi.org/10.1007/978-1-84800-155-8_7)
- J. Löfberg, “YALMIP: a toolbox for modeling and optimization in MATLAB,” in Proceedings of the CACSD Conference, Taipei, Taiwan, 2004.
- N. Aliyev, P. Benner, E. Mengi, P. Schwerdtner, and M. Voigt, et al.., “Large-scale computation of L∞${\mathcal{L}}_{\infty }$-norms by a greedy subspace method,” SIAM J. Matrix Anal. Appl., vol. 38.4, pp. 1496–1516, 2017. https://doi.org/10.1137/16m1086200. -- [10.1137/16M1086200](https://doi.org/10.1137/16M1086200)
- P. Schwerdtner and M. Voigt, “Computation of the L∞${\mathcal{L}}_{\infty }$-norm using rational interpolation,” in IFACPapersOnLine 51.25 (2018). 9th IFAC Symposium on Robust Control Design ROCOND, 2018, pp. 84–89. -- [10.1016/j.ifacol.2018.11.086](https://doi.org/10.1016/j.ifacol.2018.11.086)
- P. Benner and M. Voigt, “A structured pseudospectral method for L∞${\mathcal{L}}_{\infty }$-norm computation of large-scale descriptor systems,” Math. Control. Signals, Syst., vol. 26, no. 2, pp. 303–338, 2013. https://doi.org/10.1007/s00498-013-0121-7. -- [10.1007/s00498-013-0121-7](https://doi.org/10.1007/s00498-013-0121-7)

