---
title: "SOBMOR: Structured Optimization-Based Model Order Reduction"
date: 2023-04-26 00:00:00 +0100
permalink: sobmor-structured-optimization-based-model-order-reduction
year: 2023
authors: Paul Schwerdtner, Matthias Voigt
category: articles
---
 
## Authors
[Paul Schwerdtner](authors/paul-schwerdtner), [Matthias Voigt](authors/matthias-voigt)
 
## Abstract
Model order reduction (MOR) methods that are designed to preserve structural features of a given full order model (FOM) often suffer from a lower accuracy when compared to their non-structure-preserving counterparts. In this paper, we present a framework for structure-preserving MOR, which allows to compute structured reduced order models (ROMs) with a much higher accuracy. The framework is based on parameter optimization, i.e., the elements of the system matrices of the ROM are iteratively varied to minimize an objective functional that measures the difference between the FOM and the ROM. The structural constraints can be encoded in the parametrization of the ROM. The method only depends on frequency response data and can thus be applied to a wide range of dynamical systems. We illustrate the effectiveness of our method on a port-Hamiltonian and on a symmetric second-order system in a comparison with other structure-preserving MOR algorithms.
 
## Citation
- **Journal:** SIAM Journal on Scientific Computing
- **Year:** 2023
- **Volume:** 45
- **Issue:** 2
- **Pages:** A502--A529
- **Publisher:** Society for Industrial & Applied Mathematics (SIAM)
- **DOI:** [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Schwerdtner_2023,
  title={{SOBMOR: Structured Optimization-Based Model Order Reduction}},
  volume={45},
  ISSN={1095-7197},
  DOI={10.1137/20m1380235},
  number={2},
  journal={SIAM Journal on Scientific Computing},
  publisher={Society for Industrial & Applied Mathematics (SIAM)},
  author={Schwerdtner, Paul and Voigt, Matthias},
  year={2023},
  pages={A502--A529}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/sobmor-structured-optimization-based-model-order-reduction.bib)
 
## References
- Aliyev N, Benner P, Mengi E, Schwerdtner P, Voigt M (2017) Large-Scale Computation of $\mathcal{L}_\infty$-Norms by a Greedy Subspace Method. SIAM J Matrix Anal Appl 38(4):1496–1516. https://doi.org/10.1137/16m1086200 -- [10.1137/16m1086200](https://doi.org/10.1137/16m1086200)
- Antoulas AC (2005) Approximation of Large-Scale Dynamical Systems. Society for Industrial and Applied Mathematics -- [10.1137/1.9780898718713](https://doi.org/10.1137/1.9780898718713)
- Antoulas AC, Beattie CA, Güğercin S (2020) Interpolatory Methods for Model Reduction. Society for Industrial and Applied Mathematics, Philadelphia, PA -- [10.1137/1.9781611976083](https://doi.org/10.1137/1.9781611976083)
- Bai Z, Su Y (2005) Dimension Reduction of Large-Scale Second-Order Dynamical Systems via a Second-Order Arnoldi Method. SIAM J Sci Comput 26(5):1692–1709. https://doi.org/10.1137/040605552 -- [10.1137/040605552](https://doi.org/10.1137/040605552)
- C. Beattie  and 
P. Benner ,   \\(\mathcal{H}_2\\)  -Optimality Conditions for Structured Dynamical Systems, Preprint MPIMD14-18, Max Planck Institute Magdeburg, 2014.
- C. Beattie , 
V. Mehrmann , and 
H. Xu , Port-Hamiltonian Realizations of Linear Time Invariant Systems, Preprint 23-2015, Institute of Mathematics, Technische Universität Berlin, 2015.
- Beddig RS, Benner P, Dorschky I, Reis T, Schwerdtner P, Voigt M, Werner SWR (2019) Model Reduction for Second‐Order Dynamical Systems Revisited. Proc Appl Math and Mech 19(1):e201900224. https://doi.org/10.1002/pamm.201900224 -- [10.1002/pamm.201900224](https://doi.org/10.1002/pamm.201900224)
- Benner P, Kürschner P, Saak J (2013) An improved numerical method for balanced truncation for symmetric second-order systems. Mathematical and Computer Modelling of Dynamical Systems 19(6):593–615. https://doi.org/10.1080/13873954.2013.794363 -- [10.1080/13873954.2013.794363](https://doi.org/10.1080/13873954.2013.794363)
- Benner P, Sima V, Voigt M (2012) \\({\cal L}_{\infty}\\)-Norm Computation for Continuous-Time Descriptor Systems Using Structured Matrix Pencils. IEEE Trans Automat Contr 57(1):233–238. https://doi.org/10.1109/tac.2011.2161833 -- [10.1109/tac.2011.2161833](https://doi.org/10.1109/tac.2011.2161833)
- Boyd S, Balakrishnan V (1990) A regularity result for the singular values of a transfer matrix and a quadratically convergent algorithm for computing its L∞-norm. Systems & Control Letters 15(1):1–7. https://doi.org/10.1016/0167-6911(90)90037-u -- [10.1016/0167-6911(90)90037-u](https://doi.org/10.1016/0167-6911(90)90037-u)
- Bruinsma NA, Steinbuch M (1990) A fast algorithm to compute the of a transfer function matrix. Systems & Control Letters 14(4):287–293. https://doi.org/10.1016/0167-6911(90)90049-z -- [10.1016/0167-6911(90)90049-z](https://doi.org/10.1016/0167-6911(90)90049-z)
- Bunse-Gerstner A, Kubalińska D, Vossen G, Wilczek D (2010) \\(h_{2}\\)-norm optimal model reduction for large scale discrete dynamical MIMO systems. Journal of Computational and Applied Mathematics 233(5):1202–1216. https://doi.org/10.1016/j.cam.2008.12.029 -- [10.1016/j.cam.2008.12.029](https://doi.org/10.1016/j.cam.2008.12.029)
- Burke JV, Lewis AS, Overton ML (2005) A Robust Gradient Sampling Algorithm for Nonsmooth, Nonconvex Optimization. SIAM J Optim 15(3):751–779. https://doi.org/10.1137/030601296 -- [10.1137/030601296](https://doi.org/10.1137/030601296)
- Chahlaoui Y, Lemonnier D, Vandendorpe A, Van Dooren P (2006) Second-order balanced truncation. Linear Algebra and its Applications 415(2-3):373–384. https://doi.org/10.1016/j.laa.2004.03.032 -- [10.1016/j.laa.2004.03.032](https://doi.org/10.1016/j.laa.2004.03.032)
- Curtis FE, Mitchell T, Overton ML (2016) A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles. Optimization Methods and Software 32(1):148–181. https://doi.org/10.1080/10556788.2016.1208749 -- [10.1080/10556788.2016.1208749](https://doi.org/10.1080/10556788.2016.1208749)
- Curtis FE, Overton ML (2012) A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization. SIAM J Optim 22(2):474–500. https://doi.org/10.1137/090780201 -- [10.1137/090780201](https://doi.org/10.1137/090780201)
- Delfour MC (2019) Introduction to Optimization and Hadamard Semidifferential Calculus, Second Edition. Society for Industrial and Applied Mathematics, Philadelphia, PA -- [10.1137/1.9781611975963](https://doi.org/10.1137/1.9781611975963)
- Dopico FM, Lawrence PW, Pérez J, Dooren PV (2018) Block Kronecker linearizations of matrix polynomials and their backward errors. Numer Math 140(2):373–426. https://doi.org/10.1007/s00211-018-0969-z -- [10.1007/s00211-018-0969-z](https://doi.org/10.1007/s00211-018-0969-z)
- Dorschky I, Reis T, Voigt M (2021) Balanced Truncation Model Reduction for Symmetric Second Order Systems---A Passivity-Based Approach. SIAM J Matrix Anal Appl 42(4):1602–1635. https://doi.org/10.1137/20m1346109 -- [10.1137/20m1346109](https://doi.org/10.1137/20m1346109)
- Freitag MA, Spence A, Dooren PV (2014) Calculating the $H_{\infty}$-norm Using the Implicit Determinant Method. SIAM J Matrix Anal Appl 35(2):619–635. https://doi.org/10.1137/130933228 -- [10.1137/130933228](https://doi.org/10.1137/130933228)
- Gugercin S, Antoulas AC, Beattie C (2008) $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM J Matrix Anal Appl 30(2):609–638. https://doi.org/10.1137/060666123 -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- [Gugercin S, Polyuga RV, Beattie C, van der Schaft A (2012) Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9):1963–1974. https://doi.org/10.1016/j.automatica.2012.05.052](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Guglielmi N, Gürbüzbalaban M, Overton ML (2013) Fast Approximation of the $H_\infty$ Norm via Optimization over Spectral Value Sets. SIAM J Matrix Anal Appl 34(2):709–737. https://doi.org/10.1137/120875752 -- [10.1137/120875752](https://doi.org/10.1137/120875752)
- Guiver C, Opmeer MR (2013) Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra and its Applications 439(12):3659–3698. https://doi.org/10.1016/j.laa.2013.09.032 -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- Hager WW, Zhang H (2006) Algorithm 851. ACM Trans Math Softw 32(1):113–137. https://doi.org/10.1145/1132973.1132979 -- [10.1145/1132973.1132979](https://doi.org/10.1145/1132973.1132979)
- Hartmann C, Vulcanov V-M, Schütte C (2010) Balanced Truncation of Linear Second-Order Systems: A Hamiltonian Approach. Multiscale Model Simul 8(4):1348–1367. https://doi.org/10.1137/080732717 -- [10.1137/080732717](https://doi.org/10.1137/080732717)
- Hauschild S.-A., Control Cybernet. (2019)
- Ionutiu R, Rommes J, Antoulas AC (2008) Passivity-Preserving Model Reduction Using Dominant Spectral-Zero Interpolation. IEEE Trans Comput-Aided Des Integr Circuits Syst 27(12):2250–2263. https://doi.org/10.1109/tcad.2008.2006160 -- [10.1109/tcad.2008.2006160](https://doi.org/10.1109/tcad.2008.2006160)
- Lancaster P (1964) On eigenvalues of matrices dependent on a parameter. Numer Math 6(1):377–387. https://doi.org/10.1007/bf01386087 -- [10.1007/bf01386087](https://doi.org/10.1007/bf01386087)
- [Mehrmann V, Dooren PV (2021) Structured Backward Errors for Eigenvalues of Linear Port-Hamiltonian Descriptor Systems. SIAM J Matrix Anal Appl 42(1):1–16. https://doi.org/10.1137/20m1344184](structured-backward-errors-for-eigenvalues-of-linear-port-hamiltonian-descriptor-systems) -- [10.1137/20m1344184](https://doi.org/10.1137/20m1344184)
- Mehrmann V, Stykel T (2005) Balanced Truncation Model Reduction for Large-Scale Systems in Descriptor Form. In: Lecture Notes in Computational Science and Engineering. Springer-Verlag, Berlin/Heidelberg, pp 83–115 -- [10.1007/3-540-27909-1_3](https://doi.org/10.1007/3-540-27909-1_3)
- Meyer DG, Srinivasan S (1996) Balancing and model reduction for second-order form linear systems. IEEE Trans Automat Contr 41(11):1632–1644. https://doi.org/10.1109/9.544000 -- [10.1109/9.544000](https://doi.org/10.1109/9.544000)
- Mitchell T, Overton ML (2015) Hybrid expansion–contraction: a robust scaleable method for approximating the \\(H_{\infty}\\) norm. IMA J Numer Anal 36(3):985–1014. https://doi.org/10.1093/imanum/drv046 -- [10.1093/imanum/drv046](https://doi.org/10.1093/imanum/drv046)
- K Mogensen P, N Riseth A (2018) Optim: A mathematical optimization package for Julia. JOSS 3(24):615. https://doi.org/10.21105/joss.00615 -- [10.21105/joss.00615](https://doi.org/10.21105/joss.00615)
- Ober R (1991) Balanced Parametrization of Classes of Linear Systems. SIAM J Control Optim 29(6):1251–1287. https://doi.org/10.1137/0329065 -- [10.1137/0329065](https://doi.org/10.1137/0329065)
- Panzer HKF, Wolf T, Lohmann B (2013) \\(H_{2}\\) and \\(H_{\infty}\\) error bounds for model order reduction of second order systems by Krylov subspace methods. In: 2013 European Control Conference (ECC). IEEE, pp 4484–4489 -- [10.23919/ecc.2013.6669657](https://doi.org/10.23919/ecc.2013.6669657)
- (2010) Feedback Control of Negative-Imaginary Systems. IEEE Control Syst 30(5):54–72. https://doi.org/10.1109/mcs.2010.937676 -- [10.1109/mcs.2010.937676](https://doi.org/10.1109/mcs.2010.937676)
- Polyuga R. V., Model Reduction of Port-Hamiltonian Systems (2010)
- R. V. Polyuga  and 
A. J. van der Schaft , Structure preserving model reduction of port-Hamiltonian systems, in Proceedings of the 18th International Symposium on Mathematical Theory of Networks and Systems, 2008.
- Reis T, Stykel T (2008) Balanced truncation model reduction of second-order systems. Mathematical and Computer Modelling of Dynamical Systems 14(5):391–406. https://doi.org/10.1080/13873950701844170 -- [10.1080/13873950701844170](https://doi.org/10.1080/13873950701844170)
- Rommes J, Martins N (2006) Efficient Computation of Multivariable Transfer Function Dominant Poles Using Subspace Acceleration. IEEE Trans Power Syst 21(4):1471–1483. https://doi.org/10.1109/tpwrs.2006.881154 -- [10.1109/tpwrs.2006.881154](https://doi.org/10.1109/tpwrs.2006.881154)
- Ruszczynski A (2006) Nonlinear Optimization. Princeton University Press -- [10.1515/9781400841059](https://doi.org/10.1515/9781400841059)
- Saak J, Siebelts D, Werner SWR (2019) A comparison of second-order model order reduction methods for an artificial fishtail. at - Automatisierungstechnik 67(8):648–667. https://doi.org/10.1515/auto-2019-0027 -- [10.1515/auto-2019-0027](https://doi.org/10.1515/auto-2019-0027)
- B. Salimbahrami , Structure Preserving Order Reduction of Large Scale Second Order Models, Dissertation, Fakultät für Maschinenwesen, Technische Universität München, 2005, https://mediatum.ub.tum.de/doc/601950/00000941.pdf.
- Salimbahrami B, Lohmann B (2006) Order reduction of large scale second-order systems using Krylov subspace methods. Linear Algebra and its Applications 415(2-3):385–405. https://doi.org/10.1016/j.laa.2004.12.013 -- [10.1016/j.laa.2004.12.013](https://doi.org/10.1016/j.laa.2004.12.013)
- P. Schwerdtner , Port-Hamiltonian System Identification from Noisy Frequency Response Data, preprint, arXiv:2106.11355, 2021.
- Schwerdtner P, Mengi E, Voigt M (2020) Certifying Global Optimality for the L∞-Norm Computation of Large-Scale Descriptor Systems. IFAC-PapersOnLine 53(2):4279–4284. https://doi.org/10.1016/j.ifacol.2020.12.2482 -- [10.1016/j.ifacol.2020.12.2482](https://doi.org/10.1016/j.ifacol.2020.12.2482)
- Schwerdtner P, Voigt M (2018) Computation of the L∞-Norm Using Rational Interpolation. IFAC-PapersOnLine 51(25):84–89. https://doi.org/10.1016/j.ifacol.2018.11.086 -- [10.1016/j.ifacol.2018.11.086](https://doi.org/10.1016/j.ifacol.2018.11.086)
- [Schwerdtner P, Voigt M (2021) Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine 54(19):143–148. https://doi.org/10.1016/j.ifacol.2021.11.069](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- Sorensen DC (2005) Passivity preserving model reduction via interpolation of spectral zeros. Systems & Control Letters 54(4):347–360. https://doi.org/10.1016/j.sysconle.2004.07.006 -- [10.1016/j.sysconle.2004.07.006](https://doi.org/10.1016/j.sysconle.2004.07.006)
- Truhar N, Veselić K (2009) An Efficient Method for Estimating the Optimal Dampers' Viscosity for Linear Vibrating Systems Using Lyapunov Equation. SIAM J Matrix Anal Appl 31(1):18–39. https://doi.org/10.1137/070683052 -- [10.1137/070683052](https://doi.org/10.1137/070683052)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2-3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Van Dooren P, Gallivan KA, Absil P-A (2008) \\(\mathcal{H}_{2}\\) -optimal model reduction of MIMO systems. Applied Mathematics Letters 21(12):1267–1273. https://doi.org/10.1016/j.aml.2007.09.015 -- [10.1016/j.aml.2007.09.015](https://doi.org/10.1016/j.aml.2007.09.015)
- Voigt M., On Linear-Quadratic Optimal Control and Robustness of Differential-Algebraic Systems (2015)
- [Wolf T, Lohmann B, Eid R, Kotyczka P (2010) Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control 16(4):401–406. https://doi.org/10.3166/ejc.16.401-406](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)

