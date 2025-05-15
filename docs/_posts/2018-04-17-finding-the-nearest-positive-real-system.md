---
layout: post
title: "Finding the Nearest Positive-Real System"
date: 2018-04-17 00:00:00 +0100
permalink: finding-the-nearest-positive-real-system
year: 2018
authors: Nicolas Gillis, Punit Sharma
category: articles
---
 
## Authors
[Nicolas Gillis](authors/nicolas-gillis), [Punit Sharma](authors/punit-sharma)
 
## Abstract
The notion of positive realness for linear time-invariant (LTI) dynamical systems, equivalent to passivity, is one of the oldest in system and control theory. In this paper, we consider the problem of finding the nearest positive real (PR) system to a non-PR system: given an LTI control system defined by \\( E \dot{x}=Ax+Bu \\) and \\( y=Cx+Du \\), minimize the Frobenius norm of \\( (\Delta_E,\Delta_A,\Delta_B,\Delta_C,\Delta_D) \\) such that \\( (E+\Delta_E,A+\Delta_A,B+\Delta_B,C+\Delta_C,D+\Delta_D) \\) is a PR system. We first show that a system is extended strictly PR if and only if it can be written as a strict port-Hamiltonian system. This allows us to reformulate the nearest PR system problem into an optimization problem with a simple convex feasible set. We then use a fast gradient method to obtain a nearby PR system to a given non-PR system and illustrate the behavior of our algorithm with several examples. This is, to the best of our knowledge, the first algorithm that computes a nearby PR system to a given non-PR sys...
 
## Citation
- **Journal:** SIAM Journal on Numerical Analysis
- **Year:** 2018
- **Volume:** 56
- **Issue:** 2
- **Pages:** 1022--1047
- **Publisher:** Society for Industrial & Applied Mathematics (SIAM)
- **DOI:** [10.1137/17m1137176](https://doi.org/10.1137/17m1137176)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gillis_2018,
  title={{Finding the Nearest Positive-Real System}},
  volume={56},
  ISSN={1095-7170},
  DOI={10.1137/17m1137176},
  number={2},
  journal={SIAM Journal on Numerical Analysis},
  publisher={Society for Industrial & Applied Mathematics (SIAM)},
  author={Gillis, Nicolas and Sharma, Punit},
  year={2018},
  pages={1022--1047}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/finding-the-nearest-positive-real-system.bib)
 
## References
- Alam, R., Bora, S., Karow, M., Mehrmann, V. & Moro, J. Perturbation Theory for Hamiltonian Matrices and the Distance to Bounded-Realness. SIAM Journal on Matrix Analysis and Applications vol. 32 484–514 (2011) -- [10.1137/10079464x](https://doi.org/10.1137/10079464x)
- Boyd, S., Balakrishnan, V. & Kabamba, P. A bisection method for computing the H∞ norm of a transfer matrix and related problems. Mathematics of Control, Signals, and Systems vol. 2 207–219 (1989) -- [10.1007/bf02551385](https://doi.org/10.1007/bf02551385)
- Brull, T. & Schroder, C. Dissipativity Enforcement via Perturbation of Para-Hermitian Pencils. IEEE Transactions on Circuits and Systems I: Regular Papers vol. 60 164–177 (2013) -- [10.1109/tcsi.2012.2215731](https://doi.org/10.1109/tcsi.2012.2215731)
- Byers, R. & Nichols, N. K. On the stability radius of a generalized state-space system. Linear Algebra and its Applications vols 188–189 113–134 (1993) -- [10.1016/0024-3795(93)90466-2](https://doi.org/10.1016/0024-3795(93)90466-2)
- Freund, R. W. & Jarre, F. An extension of the positive real lemma to descriptor systems. Optimization Methods and Software vol. 19 69–87 (2004) -- [10.1080/10556780410001654232](https://doi.org/10.1080/10556780410001654232)
- Ghadimi, S. & Lan, G. Accelerated gradient methods for nonconvex nonlinear and stochastic programming. Mathematical Programming vol. 156 59–99 (2015) -- [10.1007/s10107-015-0871-8](https://doi.org/10.1007/s10107-015-0871-8)
- [Gillis, N. & Sharma, P. On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica vol. 85 113–121 (2017)](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- Grant M., Berlin (2008)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Transactions on Circuits and Systems I: Regular Papers vol. 51 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Guglielmi, N., Kressner, D. & Lubich, C. Low rank differential equations for Hamiltonian matrix nearness problems. Numerische Mathematik vol. 129 279–319 (2014) -- [10.1007/s00211-014-0637-x](https://doi.org/10.1007/s00211-014-0637-x)
- Higham, N. J. Computing a nearest symmetric positive semidefinite matrix. Linear Algebra and its Applications vol. 103 103–118 (1988) -- [10.1016/0024-3795(88)90223-6](https://doi.org/10.1016/0024-3795(88)90223-6)
- Huang, C.-H., Ioannou, P. A., Maroulas, J. & Safonov, M. G. Design of strictly positive real systems using constant output feedback. IEEE Transactions on Automatic Control vol. 44 569–573 (1999) -- [10.1109/9.751352](https://doi.org/10.1109/9.751352)
- Hughes, T. H. A theory of passive linear systems with no assumptions. Automatica vol. 86 87–97 (2017) -- [10.1016/j.automatica.2017.08.017](https://doi.org/10.1016/j.automatica.2017.08.017)
- Ioannou, P. & Gang Tao. Frequency domain conditions for strictly positive real functions. IEEE Transactions on Automatic Control vol. 32 53–54 (1987) -- [10.1109/tac.1987.1104447](https://doi.org/10.1109/tac.1987.1104447)
- Lozano-Leal, R. & Joshi, S. M. Strictly positive real transfer functions revisited. IEEE Transactions on Automatic Control vol. 35 1243–1245 (1990) -- [10.1109/9.59811](https://doi.org/10.1109/9.59811)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability Radii for Linear Hamiltonian Systems with Dissipation Under Structure-Preserving Perturbations. SIAM Journal on Matrix Analysis and Applications vol. 37 1625–1654 (2016)](stability-radii-for-linear-hamiltonian-systems-with-dissipation-under-structure-preserving-perturbations) -- [10.1137/16m1067330](https://doi.org/10.1137/16m1067330)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability radii for real linear Hamiltonian systems with perturbed dissipation. BIT Numerical Mathematics vol. 57 811–843 (2017)](stability-radii-for-real-linear-hamiltonian-systems-with-perturbed-dissipation) -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- Nesterov Y., Soviet Math. Dokl. (1983)
- Weiqian Sun, Khargonekar, P. P. & Duksun Shim. Solution to the positive real control problem for linear time-invariant systems. IEEE Transactions on Automatic Control vol. 39 2034–2046 (1994) -- [10.1109/9.328822](https://doi.org/10.1109/9.328822)
- Toh, K. C., Todd, M. J. & Tütüncü, R. H. SDPT3 — A Matlab software package for semidefinite programming, Version 1.3. Optimization Methods and Software vol. 11 545–581 (1999) -- [10.1080/10556789908805762](https://doi.org/10.1080/10556789908805762)
- T�t�nc�, R. H., Toh, K. C. & Todd, M. J. Solving semidefinite-quadratic-linear programs using SDPT3. Mathematical Programming vol. 95 189–217 (2003) -- [10.1007/s10107-002-0347-5](https://doi.org/10.1007/s10107-002-0347-5)
- van der Schaft A., Spain (2006)
- van der Schaft A., New York (2013)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- van der Schaft A., Arch. Elektron. Übertragungstech. (1995)
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM Journal on Control and Optimization vol. 51 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Varga, A. On stabilization methods of descriptor systems. Systems &amp; Control Letters vol. 24 133–138 (1995) -- [10.1016/0167-6911(94)00017-p](https://doi.org/10.1016/0167-6911(94)00017-p)
- Wen, J. T. Time domain and frequency domain conditions for strict positive realness. IEEE Transactions on Automatic Control vol. 33 988–992 (1988) -- [10.1109/9.7263](https://doi.org/10.1109/9.7263)
- Willems, J. C. Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Archive for Rational Mechanics and Analysis vol. 45 352–393 (1972) -- [10.1007/bf00276494](https://doi.org/10.1007/bf00276494)
- Liqian Zhang, Lam, J. & Shengyuan Xu. On positive realness of descriptor systems. IEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications vol. 49 401–407 (2002) -- [10.1109/81.989180](https://doi.org/10.1109/81.989180)

