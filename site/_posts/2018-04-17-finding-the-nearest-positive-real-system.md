---
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
- Alam R, Bora S, Karow M, Mehrmann V, Moro J (2011) Perturbation Theory for Hamiltonian Matrices and the Distance to Bounded-Realness. SIAM J Matrix Anal Appl 32(2):484–514. https://doi.org/10.1137/10079464x -- [10.1137/10079464x](https://doi.org/10.1137/10079464x)
- Anderson B., Network Analysis and Synthesis (1973)
- Antoulas AC (2005) Approximation of Large-Scale Dynamical Systems. Society for Industrial and Applied Mathematics -- [10.1137/1.9780898718713](https://doi.org/10.1137/1.9780898718713)
- Beattie C., Preprint 23-2015 (2015)
- Beattie C., Port-Hamiltonian Descriptor Systems, arXiv:1705.09081 (2017)
- Bonnans J., Perturbation Analysis of Optimization Problems (2013)
- Boyd S, Balakrishnan V, Kabamba P (1989) A bisection method for computing the H∞ norm of a transfer matrix and related problems. Math Control Signal Systems 2(3):207–219. https://doi.org/10.1007/bf02551385 -- [10.1007/bf02551385](https://doi.org/10.1007/bf02551385)
- Boyd S, El Ghaoui L, Feron E, Balakrishnan V (1994) Linear Matrix Inequalities in System and Control Theory. Society for Industrial and Applied Mathematics -- [10.1137/1.9781611970777](https://doi.org/10.1137/1.9781611970777)
- Brull T, Schroder C (2013) Dissipativity Enforcement via Perturbation of Para-Hermitian Pencils. IEEE Trans Circuits Syst I 60(1):164–177. https://doi.org/10.1109/tcsi.2012.2215731 -- [10.1109/tcsi.2012.2215731](https://doi.org/10.1109/tcsi.2012.2215731)
- Byers R, Nichols NK (1993) On the stability radius of a generalized state-space system. Linear Algebra and its Applications 188-189:113–134. https://doi.org/10.1016/0024-3795(93)90466-2 -- [10.1016/0024-3795(93)90466-2](https://doi.org/10.1016/0024-3795(93)90466-2)
- CVX: MATLAB Software for Disciplined Convex Programming, Version
                      2.0,http://cvxr.com/cvx(2012).
- Desoer C., Feedback Systems: Input-Output Properties (1975)
- Freund RW, Jarre F (2004) An extension of the positive real lemma to descriptor systems. Optimization Methods and Software 19(1):69–87. https://doi.org/10.1080/10556780410001654232 -- [10.1080/10556780410001654232](https://doi.org/10.1080/10556780410001654232)
- Gantmacher F., The Theory of Matrices I (1959)
- Ghadimi S, Lan G (2015) Accelerated gradient methods for nonconvex nonlinear and stochastic programming. Math Program 156(1-2):59–99. https://doi.org/10.1007/s10107-015-0871-8 -- [10.1007/s10107-015-0871-8](https://doi.org/10.1007/s10107-015-0871-8)
- [Gillis N, Mehrmann V, Sharma P (2018) Computing the nearest stable matrix pairs. Numerical Linear Algebra App 25(5):e2153. https://doi.org/10.1002/nla.2153](computing-the-nearest-stable-matrix-pairs) -- [10.1002/nla.2153](https://doi.org/10.1002/nla.2153)
- [Gillis N, Sharma P (2017) On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica 85:113–121. https://doi.org/10.1016/j.automatica.2017.07.047](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- Grant MC, Boyd SP (2007) Graph Implementations for Nonsmooth Convex Programs. In: Lecture Notes in Control and Information Sciences. Springer London, London, pp 95–110 -- [10.1007/978-1-84800-155-8_7](https://doi.org/10.1007/978-1-84800-155-8_7)
- Grivet-Talocia S (2004) Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Trans Circuits Syst I 51(9):1755–1769. https://doi.org/10.1109/tcsi.2004.834527 -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Guglielmi N, Kressner D, Lubich C (2014) Low rank differential equations for Hamiltonian matrix nearness problems. Numer Math 129(2):279–319. https://doi.org/10.1007/s00211-014-0637-x -- [10.1007/s00211-014-0637-x](https://doi.org/10.1007/s00211-014-0637-x)
- Haddad MM, Bernstein DS (2002) Explicit construction of quadratic Lyapunov functions for the small gain, positivity, circle and Popov theorems and their application to robust stability. In: [1991] Proceedings of the 30th IEEE Conference on Decision and Control. IEEE, pp 2618–2623 -- [10.1109/cdc.1991.261825](https://doi.org/10.1109/cdc.1991.261825)
- Higham NJ (1988) Computing a nearest symmetric positive semidefinite matrix. Linear Algebra and its Applications 103:103–118. https://doi.org/10.1016/0024-3795(88)90223-6 -- [10.1016/0024-3795(88)90223-6](https://doi.org/10.1016/0024-3795(88)90223-6)
- Huang C-H, Ioannou PA, Maroulas J, Safonov MG (1999) Design of strictly positive real systems using constant output feedback. IEEE Trans Automat Contr 44(3):569–573. https://doi.org/10.1109/9.751352 -- [10.1109/9.751352](https://doi.org/10.1109/9.751352)
- Hughes TH (2017) A theory of passive linear systems with no assumptions. Automatica 86:87–97. https://doi.org/10.1016/j.automatica.2017.08.017 -- [10.1016/j.automatica.2017.08.017](https://doi.org/10.1016/j.automatica.2017.08.017)
- Ioannou P, Gang Tao (1987) Frequency domain conditions for strictly positive real functions. IEEE Trans Automat Contr 32(1):53–54. https://doi.org/10.1109/tac.1987.1104447 -- [10.1109/tac.1987.1104447](https://doi.org/10.1109/tac.1987.1104447)
- Joshi SM (ed) (1989) Control of Large Flexible Space Structures. Springer-Verlag, Berlin/Heidelberg -- [10.1007/bfb0042076](https://doi.org/10.1007/bfb0042076)
- Kunkel P, Mehrmann V (2006) Differential-Algebraic Equations. EMS Press -- [10.4171/017](https://doi.org/10.4171/017)
- Lozano R., Dissipative Systems Analysis and Control: Theory and Applications (2013)
- Lozano-Leal R, Joshi SM (1990) Strictly positive real transfer functions revisited. IEEE Trans Automat Contr 35(11):1243–1245. https://doi.org/10.1109/9.59811 -- [10.1109/9.59811](https://doi.org/10.1109/9.59811)
- [Mehl C, Mehrmann V, Sharma P (2016) Stability Radii for Linear Hamiltonian Systems with Dissipation Under Structure-Preserving Perturbations. SIAM J Matrix Anal Appl 37(4):1625–1654. https://doi.org/10.1137/16m1067330](stability-radii-for-linear-hamiltonian-systems-with-dissipation-under-structure-preserving-perturbations) -- [10.1137/16m1067330](https://doi.org/10.1137/16m1067330)
- [Mehl C, Mehrmann V, Sharma P (2017) Stability radii for real linear Hamiltonian systems with perturbed dissipation. Bit Numer Math 57(3):811–843. https://doi.org/10.1007/s10543-017-0654-0](stability-radii-for-real-linear-hamiltonian-systems-with-perturbed-dissipation) -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- Mehrmann VL (ed) (1991) The Autonomous Linear Quadratic Control Problem. Springer-Verlag, Berlin/Heidelberg -- [10.1007/bfb0039443](https://doi.org/10.1007/bfb0039443)
- Nesterov Y., Soviet Math. Dokl. (1983)
- Nesterov Y., Appl. Optim. 87 (2004)
- O'Neill M., Behavior of Accelerated Gradient Methods Near Critical Points of Nonconvex Problems, arXiv:1706.07993 (2017)
- Overton ML, Van Dooren P (2006) On computing the complex passivity radius. In: Proceedings of the 44th IEEE Conference on Decision and Control. IEEE, pp 7960–7964 -- [10.1109/cdc.2005.1583449](https://doi.org/10.1109/cdc.2005.1583449)
- Popov V-M (1973) Hyperstability of Control Systems. Springer Berlin Heidelberg, Berlin, Heidelberg -- [10.1007/978-3-642-65654-5](https://doi.org/10.1007/978-3-642-65654-5)
- Schröder C., MATHEON (2007)
- Weiqian Sun, Khargonekar PP, Duksun Shim (1994) Solution to the positive real control problem for linear time-invariant systems. IEEE Trans Automat Contr 39(10):2034–2046. https://doi.org/10.1109/9.328822 -- [10.1109/9.328822](https://doi.org/10.1109/9.328822)
- Toh KC, Todd MJ, Tütüncü RH (1999) SDPT3 — A Matlab software package for semidefinite programming, Version 1.3. Optimization Methods and Software 11(1-4):545–581. https://doi.org/10.1080/10556789908805762 -- [10.1080/10556789908805762](https://doi.org/10.1080/10556789908805762)
- Tütüncü RH, Toh KC, Todd MJ (2003) Solving semidefinite-quadratic-linear programs using SDPT3. Mathematical Programming 95(2):189–217. https://doi.org/10.1007/s10107-002-0347-5 -- [10.1007/s10107-002-0347-5](https://doi.org/10.1007/s10107-002-0347-5)
- van der Schaft A., Proceedings of the International Congress of Mathematicians (2006)
- [van der Schaft AJ (2013) Port-Hamiltonian Differential-Algebraic Systems. In: Surveys in Differential-Algebraic Equations I. Springer Berlin Heidelberg, Berlin, Heidelberg, pp 173–226](port-hamiltonian-differential-algebraic-systems) -- [10.1007/978-3-642-34928-7_5](https://doi.org/10.1007/978-3-642-34928-7_5)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2-3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- van der Schaft A., Arch. Elektron. Übertragungstech. (1995)
- [van der Schaft AJ, Maschke BM (2002) Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42(1-2):166–194. https://doi.org/10.1016/s0393-0440(01)00083-3](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- [van der Schaft AJ, Maschke BM (2013) Port-Hamiltonian Systems on Graphs. SIAM J Control Optim 51(2):906–937. https://doi.org/10.1137/110840091](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Varga A (1995) On stabilization methods of descriptor systems. Systems & Control Letters 24(2):133–138. https://doi.org/10.1016/0167-6911(94)00017-p -- [10.1016/0167-6911(94)00017-p](https://doi.org/10.1016/0167-6911(94)00017-p)
- Voigt M., Linz (2011)
- He-Sheng Wang, Fan-Ren Chang (2002) The generalized state-space description of positive realness and bounded realness. In: Proceedings of the 39th Midwest Symposium on Circuits and Systems. IEEE, pp 893–896 -- [10.1109/mwscas.1996.588069](https://doi.org/10.1109/mwscas.1996.588069)
- Wang Y, Zhang Z, Koh C-K, Pang GKH, Wong N (2010) PEDS: Passivity enforcement for descriptor systems via Hamiltonian-symplectic matrix pencil perturbation. In: 2010 IEEE/ACM International Conference on Computer-Aided Design (ICCAD). IEEE, pp 800–807 -- [10.1109/iccad.2010.5653885](https://doi.org/10.1109/iccad.2010.5653885)
- Wen JT (1988) Time domain and frequency domain conditions for strict positive realness. IEEE Trans Automat Contr 33(10):988–992. https://doi.org/10.1109/9.7263 -- [10.1109/9.7263](https://doi.org/10.1109/9.7263)
- Willems JC (1972) Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Arch Rational Mech Anal 45(5):352–393. https://doi.org/10.1007/bf00276494 -- [10.1007/bf00276494](https://doi.org/10.1007/bf00276494)
- Liqian Zhang, Lam J, Shengyuan Xu (2002) On positive realness of descriptor systems. IEEE Trans Circuits Syst I 49(3):401–407. https://doi.org/10.1109/81.989180 -- [10.1109/81.989180](https://doi.org/10.1109/81.989180)

