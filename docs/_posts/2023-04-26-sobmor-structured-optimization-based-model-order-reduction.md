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
- Aliyev, N., Benner, P., Mengi, E., Schwerdtner, P. & Voigt, M. Large-Scale Computation of $\mathcal{L}_\infty$-Norms by a Greedy Subspace Method. SIAM Journal on Matrix Analysis and Applications vol. 38 1496–1516 (2017) -- [10.1137/16m1086200](https://doi.org/10.1137/16m1086200)
- Antoulas, A. C. Approximation of Large-Scale Dynamical Systems. (2005) doi:10.1137/1.9780898718713 -- [10.1137/1.9780898718713](https://doi.org/10.1137/1.9780898718713)
- Antoulas, A. C., Beattie, C. A. & Güğercin, S. Interpolatory Methods for Model Reduction. (Society for Industrial and Applied Mathematics, 2020). doi:10.1137/1.9781611976083 -- [10.1137/1.9781611976083](https://doi.org/10.1137/1.9781611976083)
- Bai, Z. & Su, Y. Dimension Reduction of Large-Scale Second-Order Dynamical Systems via a Second-Order Arnoldi Method. SIAM Journal on Scientific Computing vol. 26 1692–1709 (2005) -- [10.1137/040605552](https://doi.org/10.1137/040605552)
- Beddig, R. S. et al. Model Reduction for Second‐Order Dynamical Systems Revisited. PAMM vol. 19 (2019) -- [10.1002/pamm.201900224](https://doi.org/10.1002/pamm.201900224)
- Benner, P., Kürschner, P. & Saak, J. An improved numerical method for balanced truncation for symmetric second-order systems. Mathematical and Computer Modelling of Dynamical Systems vol. 19 593–615 (2013) -- [10.1080/13873954.2013.794363](https://doi.org/10.1080/13873954.2013.794363)
- Benner, P., Sima, V. & Voigt, M. &lt;formula formulatype="inline"&gt;&lt;tex Notation="TeX"&gt;${\cal L}_{\infty}$&lt;/tex&gt;&lt;/formula&gt;-Norm Computation for Continuous-Time Descriptor Systems Using Structured Matrix Pencils. IEEE Transactions on Automatic Control vol. 57 233–238 (2012) -- [10.1109/tac.2011.2161833](https://doi.org/10.1109/tac.2011.2161833)
- Boyd, S. & Balakrishnan, V. A regularity result for the singular values of a transfer matrix and a quadratically convergent algorithm for computing its L∞-norm. Systems &amp; Control Letters vol. 15 1–7 (1990) -- [10.1016/0167-6911(90)90037-u](https://doi.org/10.1016/0167-6911(90)90037-u)
- Bruinsma, N. A. & Steinbuch, M. A fast algorithm to compute the of a transfer function matrix. Systems &amp; Control Letters vol. 14 287–293 (1990) -- [10.1016/0167-6911(90)90049-z](https://doi.org/10.1016/0167-6911(90)90049-z)
- Bunse-Gerstner, A., Kubalińska, D., Vossen, G. & Wilczek, D. <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si12.gif" display="inline" overflow="scroll"><mml:msub><mml:mrow><mml:mi>h</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:math>-norm optimal model reduction for large scale discrete dynamical MIMO systems. Journal of Computational and Applied Mathematics vol. 233 1202–1216 (2010) -- [10.1016/j.cam.2008.12.029](https://doi.org/10.1016/j.cam.2008.12.029)
- Burke, J. V., Lewis, A. S. & Overton, M. L. A Robust Gradient Sampling Algorithm for Nonsmooth, Nonconvex Optimization. SIAM Journal on Optimization vol. 15 751–779 (2005) -- [10.1137/030601296](https://doi.org/10.1137/030601296)
- Chahlaoui, Y., Lemonnier, D., Vandendorpe, A. & Van Dooren, P. Second-order balanced truncation. Linear Algebra and its Applications vol. 415 373–384 (2006) -- [10.1016/j.laa.2004.03.032](https://doi.org/10.1016/j.laa.2004.03.032)
- Curtis, F. E., Mitchell, T. & Overton, M. L. A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles. Optimization Methods and Software vol. 32 148–181 (2016) -- [10.1080/10556788.2016.1208749](https://doi.org/10.1080/10556788.2016.1208749)
- Curtis, F. E. & Overton, M. L. A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization. SIAM Journal on Optimization vol. 22 474–500 (2012) -- [10.1137/090780201](https://doi.org/10.1137/090780201)
- Delfour, M. C. Introduction to Optimization and Hadamard Semidifferential Calculus, Second Edition. (Society for Industrial and Applied Mathematics, 2019). doi:10.1137/1.9781611975963 -- [10.1137/1.9781611975963](https://doi.org/10.1137/1.9781611975963)
- Dopico, F. M., Lawrence, P. W., Pérez, J. & Dooren, P. V. Block Kronecker linearizations of matrix polynomials and their backward errors. Numerische Mathematik vol. 140 373–426 (2018) -- [10.1007/s00211-018-0969-z](https://doi.org/10.1007/s00211-018-0969-z)
- Dorschky, I., Reis, T. & Voigt, M. Balanced Truncation Model Reduction for Symmetric Second Order Systems---A Passivity-Based Approach. SIAM Journal on Matrix Analysis and Applications vol. 42 1602–1635 (2021) -- [10.1137/20m1346109](https://doi.org/10.1137/20m1346109)
- Freitag, M. A., Spence, A. & Dooren, P. V. Calculating the $H_{\infty}$-norm Using the Implicit Determinant Method. SIAM Journal on Matrix Analysis and Applications vol. 35 619–635 (2014) -- [10.1137/130933228](https://doi.org/10.1137/130933228)
- Gugercin, S., Antoulas, A. C. & Beattie, C. $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM Journal on Matrix Analysis and Applications vol. 30 609–638 (2008) -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Guglielmi, N., Gürbüzbalaban, M. & Overton, M. L. Fast Approximation of the $H_\infty$ Norm via Optimization over Spectral Value Sets. SIAM Journal on Matrix Analysis and Applications vol. 34 709–737 (2013) -- [10.1137/120875752](https://doi.org/10.1137/120875752)
- Guiver, C. & Opmeer, M. R. Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra and its Applications vol. 439 3659–3698 (2013) -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- Hager, W. W. & Zhang, H. Algorithm 851. ACM Transactions on Mathematical Software vol. 32 113–137 (2006) -- [10.1145/1132973.1132979](https://doi.org/10.1145/1132973.1132979)
- Hartmann, C., Vulcanov, V.-M. & Schütte, C. Balanced Truncation of Linear Second-Order Systems: A Hamiltonian Approach. Multiscale Modeling &amp; Simulation vol. 8 1348–1367 (2010) -- [10.1137/080732717](https://doi.org/10.1137/080732717)
- Hauschild S.-A., Control Cybernet. (2019)
- Ionutiu, R., Rommes, J. & Antoulas, A. C. Passivity-Preserving Model Reduction Using Dominant Spectral-Zero Interpolation. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems vol. 27 2250–2263 (2008) -- [10.1109/tcad.2008.2006160](https://doi.org/10.1109/tcad.2008.2006160)
- Lancaster, P. On eigenvalues of matrices dependent on a parameter. Numerische Mathematik vol. 6 377–387 (1964) -- [10.1007/bf01386087](https://doi.org/10.1007/bf01386087)
- [Mehrmann, V. & Dooren, P. V. Structured Backward Errors for Eigenvalues of Linear Port-Hamiltonian Descriptor Systems. SIAM Journal on Matrix Analysis and Applications vol. 42 1–16 (2021)](structured-backward-errors-for-eigenvalues-of-linear-port-hamiltonian-descriptor-systems) -- [10.1137/20m1344184](https://doi.org/10.1137/20m1344184)
- Mehrmann, V. & Stykel, T. Balanced Truncation Model Reduction for Large-Scale Systems in Descriptor Form. Lecture Notes in Computational Science and Engineering 83–115 doi:10.1007/3-540-27909-1_3 -- [10.1007/3-540-27909-1_3](https://doi.org/10.1007/3-540-27909-1_3)
- Meyer, D. G. & Srinivasan, S. Balancing and model reduction for second-order form linear systems. IEEE Transactions on Automatic Control vol. 41 1632–1644 (1996) -- [10.1109/9.544000](https://doi.org/10.1109/9.544000)
- Mitchell, T. & Overton, M. L. Hybrid expansion–contraction: a robust scaleable method for approximating theH∞norm. IMA Journal of Numerical Analysis vol. 36 985–1014 (2015) -- [10.1093/imanum/drv046](https://doi.org/10.1093/imanum/drv046)
- K Mogensen, P. & N Riseth, A. Optim: A mathematical optimization package for Julia. Journal of Open Source Software vol. 3 615 (2018) -- [10.21105/joss.00615](https://doi.org/10.21105/joss.00615)
- Ober, R. Balanced Parametrization of Classes of Linear Systems. SIAM Journal on Control and Optimization vol. 29 1251–1287 (1991) -- [10.1137/0329065](https://doi.org/10.1137/0329065)
- Feedback Control of Negative-Imaginary Systems. IEEE Control Systems vol. 30 54–72 (2010) -- [10.1109/mcs.2010.937676](https://doi.org/10.1109/mcs.2010.937676)
- Polyuga R. V., Model Reduction of Port-Hamiltonian Systems (2010)
- Reis, T. & Stykel, T. Balanced truncation model reduction of second-order systems. Mathematical and Computer Modelling of Dynamical Systems vol. 14 391–406 (2008) -- [10.1080/13873950701844170](https://doi.org/10.1080/13873950701844170)
- Rommes, J. & Martins, N. Efficient Computation of Multivariable Transfer Function Dominant Poles Using Subspace Acceleration. IEEE Transactions on Power Systems vol. 21 1471–1483 (2006) -- [10.1109/tpwrs.2006.881154](https://doi.org/10.1109/tpwrs.2006.881154)
- Ruszczynski, A. Nonlinear Optimization. (2006) doi:10.1515/9781400841059 -- [10.1515/9781400841059](https://doi.org/10.1515/9781400841059)
- Saak, J., Siebelts, D. & Werner, S. W. R. A comparison of second-order model order reduction methods for an artificial fishtail. at - Automatisierungstechnik vol. 67 648–667 (2019) -- [10.1515/auto-2019-0027](https://doi.org/10.1515/auto-2019-0027)
- Salimbahrami, B. & Lohmann, B. Order reduction of large scale second-order systems using Krylov subspace methods. Linear Algebra and its Applications vol. 415 385–405 (2006) -- [10.1016/j.laa.2004.12.013](https://doi.org/10.1016/j.laa.2004.12.013)
- Schwerdtner, P., Mengi, E. & Voigt, M. Certifying Global Optimality for the L∞-Norm Computation of Large-Scale Descriptor Systems. IFAC-PapersOnLine vol. 53 4279–4284 (2020) -- [10.1016/j.ifacol.2020.12.2482](https://doi.org/10.1016/j.ifacol.2020.12.2482)
- Schwerdtner, P. & Voigt, M. Computation of the L∞-Norm Using Rational Interpolation. IFAC-PapersOnLine vol. 51 84–89 (2018) -- [10.1016/j.ifacol.2018.11.086](https://doi.org/10.1016/j.ifacol.2018.11.086)
- [Schwerdtner, P. & Voigt, M. Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine vol. 54 143–148 (2021)](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- Sorensen, D. C. Passivity preserving model reduction via interpolation of spectral zeros. Systems &amp; Control Letters vol. 54 347–360 (2005) -- [10.1016/j.sysconle.2004.07.006](https://doi.org/10.1016/j.sysconle.2004.07.006)
- Truhar, N. & Veselić, K. An Efficient Method for Estimating the Optimal Dampers’ Viscosity for Linear Vibrating Systems Using Lyapunov Equation. SIAM Journal on Matrix Analysis and Applications vol. 31 18–39 (2009) -- [10.1137/070683052](https://doi.org/10.1137/070683052)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Van Dooren, P., Gallivan, K. A. & Absil, P.-A. <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si1.gif" display="inline" overflow="scroll"><mml:msub><mml:mrow><mml:mi mathvariant="script">H</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:math>-optimal model reduction of MIMO systems. Applied Mathematics Letters vol. 21 1267–1273 (2008) -- [10.1016/j.aml.2007.09.015](https://doi.org/10.1016/j.aml.2007.09.015)
- Voigt M., On Linear-Quadratic Optimal Control and Robustness of Differential-Algebraic Systems (2015)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control vol. 16 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)

