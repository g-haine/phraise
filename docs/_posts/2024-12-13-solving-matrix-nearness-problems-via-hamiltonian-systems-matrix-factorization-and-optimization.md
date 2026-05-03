---
title: "Solving Matrix Nearness Problems via Hamiltonian Systems, Matrix Factorization, and Optimization"
date: 2024-12-13 00:00:00 +0100
permalink: solving-matrix-nearness-problems-via-hamiltonian-systems-matrix-factorization-and-optimization
year: 2024
authors: Nicolas Gillis, Punit Sharma
category: chapters
---
 
## Authors
[Nicolas Gillis](authors/nicolas-gillis), [Punit Sharma](authors/punit-sharma)
 
## Abstract
The main goal of these lecture notes is to survey a series of recent works (Gillis and Sharma, Automatica 85:113–121, 2017; SIAM J. Numer. Anal. 56(2):1022–1047, 2018; Linear Algebra Appl. 623:258–281, 2021; Gillis et al., Numerical Linear Algebra Appl. 25(5):e2153, 2018; Linear Algebra Appl. 573:37–53, 2019; Appl. Numer. Math. 148:131–139, 2020; Choudhary et al., Numerical Linear Algebra Appl. 27(3):e2282, 2020) that aim at solving several nearness problems for a given system. As we will see, these problems can be written as distance problems of matrices or matrix pencils. To solve them, this series of recent works rely on a two-step approach. The first step parametrizes the system using a Port-Hamiltonian representation where stability is guaranteed via convex constraints on the parameters. The second step uses standard non-linear optimization algorithms to optimize these parameters, minimizing the distance between the given system and the sought parametrized stable system. In these lecture notes, we will illustrate this strategy in order to find the nearest stable continuous-time and discrete-time systems, the nearest stable matrix pair, and the nearest positive-real system, as well as generalizations when the eigenvalues need to belong to some set Omega (which is referred to as Omega stability).
 
## Citation
- **ISBN:** 9783031713255
- **Publisher:** Springer Nature Switzerland
- **DOI:** [10.1007/978-3-031-71326-2_1](https://doi.org/10.1007/978-3-031-71326-2_1)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inbook{Gillis_2024,
  title={{Solving Matrix Nearness Problems via Hamiltonian Systems, Matrix Factorization, and Optimization}},
  ISBN={9783031713262},
  ISSN={1617-9692},
  DOI={10.1007/978-3-031-71326-2_1},
  booktitle={{Recent Stability Issues for Linear Dynamical Systems}},
  publisher={Springer Nature Switzerland},
  author={Gillis, Nicolas and Sharma, Punit},
  year={2024},
  pages={1--83}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/solving-matrix-nearness-problems-via-hamiltonian-systems-matrix-factorization-and-optimization.bib)
 
## References
- Alam R, Bora S, Karow M, Mehrmann V, Moro J (2011) Perturbation Theory for Hamiltonian Matrices and the Distance to Bounded-Realness. SIAM J Matrix Anal &amp; Appl 32(2):484–514. https://doi.org/10.1137/10079464 -- [10.1137/10079464x](https://doi.org/10.1137/10079464x)
- B Anderson, Network Analysis and Synthesis (1973)
- Antoulas AC (2005) Approximation of Large-Scale Dynamical System -- [10.1137/1.9780898718713](https://doi.org/10.1137/1.9780898718713)
- PJ Antsaklis, Linear Systems (1997)
- Astolfi A, Ortega R, Venkatraman A (2010) A globally exponentially convergent immersion and invariance speed observer for mechanical systems with non-holonomic constraints. Automatica 46(1):182–189. https://doi.org/10.1016/j.automatica.2009.10.02 -- [10.1016/j.automatica.2009.10.027](https://doi.org/10.1016/j.automatica.2009.10.027)
- [Beattie C, Mehrmann V, Xu H, Zwart H (2018) Linear port-Hamiltonian descriptor systems. Math Control Signals Syst 30(4). https://doi.org/10.1007/s00498-018-0223-](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- Blondel VD, Tsitsiklis JN (2000) A survey of computational complexity results in systems and control. Automatica 36(9):1249–1274. https://doi.org/10.1016/s0005-1098(00)00050- -- [10.1016/s0005-1098(00)00050-9](https://doi.org/10.1016/s0005-1098(00)00050-9)
- Bolte J, Sabach S, Teboulle M (2013) Proximal alternating linearized minimization for nonconvex and nonsmooth problems. Math Program 146(1–2):459–494. https://doi.org/10.1007/s10107-013-0701- -- [10.1007/s10107-013-0701-9](https://doi.org/10.1007/s10107-013-0701-9)
- N Boumal, J. Mach. Learn. Res. (2014)
- N Boumal, Adv. Neural Inf. Process. Syst. (2016)
- Boyd S, El Ghaoui L, Feron E, Balakrishnan V (1994) Linear Matrix Inequalities in System and Control Theor -- [10.1137/1.9781611970777](https://doi.org/10.1137/1.9781611970777)
- BROCK JE (1968) Optimal matrices describing linear systems. AIAA Journal 6(7):1292–1296. https://doi.org/10.2514/3.473 -- [10.2514/3.4736](https://doi.org/10.2514/3.4736)
- Brockett RW (2015) Finite Dimensional Linear System -- [10.1137/1.9781611973884](https://doi.org/10.1137/1.9781611973884)
- Brull T, Schroder C (2013) Dissipativity Enforcement via Perturbation of Para-Hermitian Pencils. IEEE Trans Circuits Syst I 60(1):164–177. https://doi.org/10.1109/tcsi.2012.221573 -- [10.1109/tcsi.2012.2215731](https://doi.org/10.1109/tcsi.2012.2215731)
- Burer S, Monteiro RDC (2003) A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization. Mathematical Programming 95(2):329–357. https://doi.org/10.1007/s10107-002-0352- -- [10.1007/s10107-002-0352-8](https://doi.org/10.1007/s10107-002-0352-8)
- Byers R (1988) A Bisection Method for Measuring the Distance of a Stable Matrix to the Unstable Matrices. SIAM J Sci and Stat Comput 9(5):875–881. https://doi.org/10.1137/090905 -- [10.1137/0909059](https://doi.org/10.1137/0909059)
- Byers R, Nichols NK (1993) On the stability radius of a generalized state-space system. Linear Algebra and its Applications 188–189:113–134. https://doi.org/10.1016/0024-3795(93)90466- -- [10.1016/0024-3795(93)90466-2](https://doi.org/10.1016/0024-3795(93)90466-2)
- Byers R, He C, Mehrmann V (1998) Where is the nearest non-regular pencil? Linear Algebra and its Applications 285(1–3):81–105. https://doi.org/10.1016/s0024-3795(98)10122- -- [10.1016/s0024-3795(98)10122-2](https://doi.org/10.1016/s0024-3795(98)10122-2)
- SL Campbell, Singular Systems of Differential Equations (1980)
- Chilali M, Gahinet P (1996) H/sub ∞/ design with pole placement constraints: an LMI approach. IEEE Trans Automat Contr 41(3):358–367. https://doi.org/10.1109/9.48663 -- [10.1109/9.486637](https://doi.org/10.1109/9.486637)
- Choudhary N, Gillis N, Sharma P (2020) On approximating the nearest Ω‐stable matrix. Numerical Linear Algebra App 27(3). https://doi.org/10.1002/nla.228 -- [10.1002/nla.2282](https://doi.org/10.1002/nla.2282)
- Choudhary N, Gillis N, Sharma P (2024) Characterizing matrices with eigenvalues in an LMI region: a dissipative-Hamiltonian approach. Linear and Multilinear Algebra 72(17):2984–2999. https://doi.org/10.1080/03081087.2024.230414 -- [10.1080/03081087.2024.2304144](https://doi.org/10.1080/03081087.2024.2304144)
- Coelho CP, Phillips JR, Silveira LM Robust rational function approximation algorithm for model generation. Proceedings 1999 Design Automation Conference (Cat. No. 99CH36361) 207–21 -- [10.1109/dac.1999.781313](https://doi.org/10.1109/dac.1999.781313)
- Conn AR, Gould NIM, Toint PL (2000) Trust Region Method -- [10.1137/1.9780898719857](https://doi.org/10.1137/1.9780898719857)
- DESOER CA, VIDYASAGAR M (1975) NORMS. Feedback Systems: Input–Output Properties 10–3 -- [10.1016/b978-0-12-212050-3.50009-8](https://doi.org/10.1016/b978-0-12-212050-3.50009-8)
- N Du, Robust stability of differential-algebraic equations, in Surveys in Differential-Algebraic Equations I (2013)
- Duan G-R (2010) Analysis and Design of Descriptor Linear Systems. Springer New Yor -- [10.1007/978-1-4419-6397-0](https://doi.org/10.1007/978-1-4419-6397-0)
- Eising R The distance between a system and the set of uncontrollable systems. Lecture Notes in Control and Information Sciences 303–31 -- [10.1007/bfb0031061](https://doi.org/10.1007/bfb0031061)
- Emmrich E, Mehrmann V (2013) Operator Differential-Algebraic Equations Arising in Fluid Dynamics. Computational Methods in Applied Mathematics 13(4):443–470. https://doi.org/10.1515/cmam-2013-001 -- [10.1515/cmam-2013-0018](https://doi.org/10.1515/cmam-2013-0018)
- R Freund, The SPRIM algorithm for structure-preserving order reduction of general RLC circuits, in Model Reduction for Circuit Simulation (2011)
- Freund RW, Jarre F (2004) An extension of the positive real lemma to descriptor systems. Optimization Methods and Software 19(1):69–87. https://doi.org/10.1080/1055678041000165423 -- [10.1080/10556780410001654232](https://doi.org/10.1080/10556780410001654232)
- Freund RW, Jarre F, Vogelbusch CH (2006) Nonlinear semidefinite programming: sensitivity, convergence, and an application in passive reduced-order modeling. Math Program 109(2–3):581–611. https://doi.org/10.1007/s10107-006-0028- -- [10.1007/s10107-006-0028-x](https://doi.org/10.1007/s10107-006-0028-x)
- [Fujimoto K, Sakai S, Sugie T (2012) Passivity based control of a class of Hamiltonian systems with nonholonomic constraints. Automatica 48(12):3054–3063. https://doi.org/10.1016/j.automatica.2012.08.03](passivity-based-control-of-a-class-of-hamiltonian-systems-with-nonholonomic-constraints) -- [10.1016/j.automatica.2012.08.032](https://doi.org/10.1016/j.automatica.2012.08.032)
- Gangsaas D, Bruce K, Blight J, Uy-Loi Ly (1986) Application of modem synthesis to aircraft control: Three case studies. IEEE Trans Automat Contr 31(11):995–1014. https://doi.org/10.1109/tac.1986.110416 -- [10.1109/tac.1986.1104161](https://doi.org/10.1109/tac.1986.1104161)
- F Gantmacher, The Theory of Matrices I (1959)
- Gillis N (2020) Nonnegative Matrix Factorizatio -- [10.1137/1.9781611976410](https://doi.org/10.1137/1.9781611976410)
- [Gillis N, Sharma P (2017) On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica 85:113–121. https://doi.org/10.1016/j.automatica.2017.07.04](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- [Gillis N, Sharma P (2018) Finding the Nearest Positive-Real System. SIAM J Numer Anal 56(2):1022–1047. https://doi.org/10.1137/17m113717](finding-the-nearest-positive-real-system) -- [10.1137/17m1137176](https://doi.org/10.1137/17m1137176)
- Gillis N, Sharma P (2018) A semi-analytical approach for the positive semidefinite Procrustes problem. Linear Algebra and its Applications 540:112–137. https://doi.org/10.1016/j.laa.2017.11.02 -- [10.1016/j.laa.2017.11.023](https://doi.org/10.1016/j.laa.2017.11.023)
- Gillis N, Sharma P (2021) Minimal-norm static feedbacks using dissipative Hamiltonian matrices. Linear Algebra and its Applications 623:258–281. https://doi.org/10.1016/j.laa.2020.02.00 -- [10.1016/j.laa.2020.02.008](https://doi.org/10.1016/j.laa.2020.02.008)
- [Gillis N, Mehrmann V, Sharma P (2018) Computing the nearest stable matrix pairs. Numerical Linear Algebra App 25(5). https://doi.org/10.1002/nla.215](computing-the-nearest-stable-matrix-pairs) -- [10.1002/nla.2153](https://doi.org/10.1002/nla.2153)
- Gillis N, Karow M, Sharma P (2019) Approximating the nearest stable discrete-time system. Linear Algebra and its Applications 573:37–53. https://doi.org/10.1016/j.laa.2019.03.01 -- [10.1016/j.laa.2019.03.014](https://doi.org/10.1016/j.laa.2019.03.014)
- Gillis N, Karow M, Sharma P (2020) A note on approximating the nearest stable discrete-time descriptor systems with fixed rank. Applied Numerical Mathematics 148:131–139. https://doi.org/10.1016/j.apnum.2019.09.00 -- [10.1016/j.apnum.2019.09.004](https://doi.org/10.1016/j.apnum.2019.09.004)
- G Golo, Nonlinear and Hybrid Systems in Automotive Control (2003)
- Grivet-Talocia S (2004) Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Trans Circuits Syst I 51(9):1755–1769. https://doi.org/10.1109/tcsi.2004.83452 -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- [Gugercin S, Polyuga RV, Beattie C, van der Schaft A (2012) Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9):1963–1974. https://doi.org/10.1016/j.automatica.2012.05.05](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Guglielmi N, Lubich C (2017) Matrix Stabilization Using Differential Equations. SIAM J Numer Anal 55(6):3097–3119. https://doi.org/10.1137/16m110584 -- [10.1137/16m1105840](https://doi.org/10.1137/16m1105840)
- Guglielmi N, Protasov VYu (2018) On the Closest Stable/Unstable Nonnegative Matrix and Related Stability Radii. SIAM J Matrix Anal Appl 39(4):1642–1669. https://doi.org/10.1137/18m117245 -- [10.1137/18m1172454](https://doi.org/10.1137/18m1172454)
- Guglielmi N, Kressner D, Lubich C (2014) Low rank differential equations for Hamiltonian matrix nearness problems. Numer Math 129(2):279–319. https://doi.org/10.1007/s00211-014-0637- -- [10.1007/s00211-014-0637-x](https://doi.org/10.1007/s00211-014-0637-x)
- Guglielmi N, Lubich C, Mehrmann V (2017) On the Nearest Singular Matrix Pencil. SIAM J Matrix Anal &amp; Appl 38(3):776–806. https://doi.org/10.1137/16m107902 -- [10.1137/16m1079026](https://doi.org/10.1137/16m1079026)
- Gustavsen B, Semlyen A (2001) Enforcing passivity for admittance matrices approximated by rational functions. IEEE Trans Power Syst 16(1):97–104. https://doi.org/10.1109/59.91078 -- [10.1109/59.910786](https://doi.org/10.1109/59.910786)
- Haddad MM, Bernstein DS Explicit construction of quadratic Lyapunov functions for the small gain, positivity, circle and Popov theorems and their application to robust stability. [1991] Proceedings of the 30th IEEE Conference on Decision and Control 2618–262 -- [10.1109/cdc.1991.261825](https://doi.org/10.1109/cdc.1991.261825)
- Higham NJ (1988) Computing a nearest symmetric positive semidefinite matrix. Linear Algebra and its Applications 103:103–118. https://doi.org/10.1016/0024-3795(88)90223- -- [10.1016/0024-3795(88)90223-6](https://doi.org/10.1016/0024-3795(88)90223-6)
- N Higham, Applications of Matrix Theory (1989)
- Hinrichsen D, Pritchard AJ (1986) Stability radii of linear systems. Systems &amp; Control Letters 7(1):1–10. https://doi.org/10.1016/0167-6911(86)90094- -- [10.1016/0167-6911(86)90094-0](https://doi.org/10.1016/0167-6911(86)90094-0)
- Horn RA, Johnson CR (1985) Matrix Analysi -- [10.1017/cbo9780511810817](https://doi.org/10.1017/cbo9780511810817)
- Huang C-H, Ioannou PA, Maroulas J, Safonov MG (1999) Design of strictly positive real systems using constant output feedback. IEEE Trans Automat Contr 44(3):569–573. https://doi.org/10.1109/9.75135 -- [10.1109/9.751352](https://doi.org/10.1109/9.751352)
- Ida N, Bastos JPA (1997) Electromagnetics and Calculation of Fields. Springer New Yor -- [10.1007/978-1-4612-0661-3](https://doi.org/10.1007/978-1-4612-0661-3)
- Ioannou P, Gang Tao (1987) Frequency domain conditions for strictly positive real functions. IEEE Trans Automat Contr 32(1):53–54. https://doi.org/10.1109/tac.1987.110444 -- [10.1109/tac.1987.1104447](https://doi.org/10.1109/tac.1987.1104447)
- [Jacob B, Zwart HJ (2012) Linear Port-Hamiltonian Systems on Infinite-dimensional Spaces. Springer Base](linear-port-hamiltonian-systems-on-infinite-dimensional-spaces) -- [10.1007/978-3-0348-0399-1](https://doi.org/10.1007/978-3-0348-0399-1)
- Joshi SM (ed) (1989) Control of Large Flexible Space Structures. Springer-Verla -- [10.1007/bfb0042076](https://doi.org/10.1007/bfb0042076)
- T Kailath, Linear Systems (1980)
- Kautsky J, Nichols NK, Chu EK-W (1989) Robust pole assignment in singular control systems. Linear Algebra and its Applications 121:9–37. https://doi.org/10.1016/0024-3795(89)90689- -- [10.1016/0024-3795(89)90689-7](https://doi.org/10.1016/0024-3795(89)90689-7)
- HK Khalil, Nonlinear Systems (1992)
- Kunkel P, Mehrmann V (2006) Differential-Algebraic Equations. EMS Textbooks in Mathematic -- [10.4171/017](https://doi.org/10.4171/017)
- P Lancaster, The Theory of Matrices (1985)
- F Leibfritz, Compleib, constraint matrix-optimization problem library-a collection of test examples for nonlinear semidefinite programs, control system design and related problems (2004)
- R Lozano, Dissipative Systems Analysis and Control: Theory and Applications (2013)
- Lozano-Leal R, Joshi SM (1990) Strictly positive real transfer functions revisited. IEEE Trans Automat Contr 35(11):1243–1245. https://doi.org/10.1109/9.5981 -- [10.1109/9.59811](https://doi.org/10.1109/9.59811)
- Markovsky I (2019) Low-Rank Approximation. Springer International Publishin -- [10.1007/978-3-319-89620-5](https://doi.org/10.1007/978-3-319-89620-5)
- [Maschke BM, Van Der Schaft AJ, Breedveld PC (1992) An intrinsic hamiltonian formulation of network dynamics: non-standard poisson structures and gyrators. Journal of the Franklin Institute 329(5):923–966. https://doi.org/10.1016/s0016-0032(92)90049-](an-intrinsic-hamiltonian-formulation-of-network-dynamics-non-standard-poisson-structures-and-gyrators) -- [10.1016/s0016-0032(92)90049-m](https://doi.org/10.1016/s0016-0032(92)90049-m)
- Masubuchi I, Kamitane Y, Ohara A, Suda N (1997) H∞ control for descriptor systems: A matrix inequalities approach. Automatica 33(4):669–673. https://doi.org/10.1016/s0005-1098(96)00193- -- [10.1016/s0005-1098(96)00193-8](https://doi.org/10.1016/s0005-1098(96)00193-8)
- Mehl C, Mehrmann V, Wojtylak M (2015) On the distance to singularity via low rank perturbations. Operators and Matrices (4):733–772. https://doi.org/10.7153/oam-09-4 -- [10.7153/oam-09-44](https://doi.org/10.7153/oam-09-44)
- [Mehl C, Mehrmann V, Sharma P (2016) Stability Radii for Linear Hamiltonian Systems with Dissipation Under Structure-Preserving Perturbations. SIAM J Matrix Anal &amp; Appl 37(4):1625–1654. https://doi.org/10.1137/16m106733](stability-radii-for-linear-hamiltonian-systems-with-dissipation-under-structure-preserving-perturbations) -- [10.1137/16m1067330](https://doi.org/10.1137/16m1067330)
- [Mehl C, Mehrmann V, Sharma P (2017) Stability radii for real linear Hamiltonian systems with perturbed dissipation. Bit Numer Math 57(3):811–843. https://doi.org/10.1007/s10543-017-0654-](stability-radii-for-real-linear-hamiltonian-systems-with-perturbed-dissipation) -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- [Mehl C, Mehrmann V, Wojtylak M (2018) Linear Algebra Properties of Dissipative Hamiltonian Descriptor Systems. SIAM J Matrix Anal &amp; Appl 39(3):1489–1519. https://doi.org/10.1137/18m116427](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18m1164275](https://doi.org/10.1137/18m1164275)
- [Mehl C, Mehrmann V, Wojtylak M (2021) Distance problems for dissipative Hamiltonian systems and related matrix polynomials. Linear Algebra and its Applications 623:335–366. https://doi.org/10.1016/j.laa.2020.05.02](distance-problems-for-dissipative-hamiltonian-systems-and-related-matrix-polynomials) -- [10.1016/j.laa.2020.05.026](https://doi.org/10.1016/j.laa.2020.05.026)
- Mehrmann VL (ed) (1991) The Autonomous Linear Quadratic Control Problem. Springer-Verla -- [10.1007/bfb0039443](https://doi.org/10.1007/bfb0039443)
- Mehrmann V, Schröder C (2011) Nonlinear eigenvalue and frequency response problems in industrial practice. Mathematics in Industry 1(1):7. https://doi.org/10.1186/2190-5983-1- -- [10.1186/2190-5983-1-7](https://doi.org/10.1186/2190-5983-1-7)
- [Mehrmann V, Van Dooren PM (2020) Optimal Robustness of Port-Hamiltonian Systems. SIAM J Matrix Anal Appl 41(1):134–151. https://doi.org/10.1137/19m125909](optimal-robustness-of-port-hamiltonian-systems) -- [10.1137/19m1259092](https://doi.org/10.1137/19m1259092)
- Moses RL, Liu D (1991) Determining the closest stable polynomial to an unstable one. IEEE Trans Signal Process 39(4):901–906. https://doi.org/10.1109/78.8091 -- [10.1109/78.80912](https://doi.org/10.1109/78.80912)
- Y Nesterov, Soviet Math. Doklady (1983)
- Nesterov Y (2004) Introductory Lectures on Convex Optimization. Springer U -- [10.1007/978-1-4419-8853-9](https://doi.org/10.1007/978-1-4419-8853-9)
- Nesterov Y, Nemirovskii A (1994) Interior-Point Polynomial Algorithms in Convex Programmin -- [10.1137/1.9781611970791](https://doi.org/10.1137/1.9781611970791)
- Nesterov Yu, Protasov VYu (2020) Computing Closest Stable Nonnegative Matrix. SIAM J Matrix Anal Appl 41(1):1–28. https://doi.org/10.1137/17m114456 -- [10.1137/17m1144568](https://doi.org/10.1137/17m1144568)
- Noferini V, Poloni F (2021) Nearest $$arOmega $$-stable matrix via Riemannian optimization. Numer Math 148(4):817–851. https://doi.org/10.1007/s00211-021-01217- -- [10.1007/s00211-021-01217-4](https://doi.org/10.1007/s00211-021-01217-4)
- O’Donoghue B, Candès E (2013) Adaptive Restart for Accelerated Gradient Schemes. Found Comput Math 15(3):715–732. https://doi.org/10.1007/s10208-013-9150- -- [10.1007/s10208-013-9150-3](https://doi.org/10.1007/s10208-013-9150-3)
- Orbandexivry F-X, Nesterov Y, Van Dooren P (2013) Nearest stable system using successive convex approximations. Automatica 49(5):1195–1203. https://doi.org/10.1016/j.automatica.2013.01.05 -- [10.1016/j.automatica.2013.01.053](https://doi.org/10.1016/j.automatica.2013.01.053)
- Overton ML, Van Dooren P On computing the complex passivity radius. Proceedings of the 44th IEEE Conference on Decision and Control 7960–796 -- [10.1109/cdc.2005.1583449](https://doi.org/10.1109/cdc.2005.1583449)
- Packard A, Doyle J (1993) The complex structured singular value. Automatica 29(1):71–109. https://doi.org/10.1016/0005-1098(93)90175- -- [10.1016/0005-1098(93)90175-s](https://doi.org/10.1016/0005-1098(93)90175-s)
- [Polyuga RV, van der Schaft A (2010) Structure preserving model reduction of port-Hamiltonian systems by moment matching at infinity. Automatica 46(4):665–672. https://doi.org/10.1016/j.automatica.2010.01.01](structure-preserving-model-reduction-of-port-hamiltonian-systems-by-moment-matching-at-infinity) -- [10.1016/j.automatica.2010.01.018](https://doi.org/10.1016/j.automatica.2010.01.018)
- Popov V-M (1973) Hyperstability of Control Systems. Springer Berlin Heidelber -- [10.1007/978-3-642-65654-5](https://doi.org/10.1007/978-3-642-65654-5)
- Prajapati A, Sharma P (2022) Estimation of Structured Distances to Singularity for Matrix Pencils with Symmetry Structures: A Linear Algebra--Based Approach. SIAM J Matrix Anal Appl 43(2):740–763. https://doi.org/10.1137/21m142326 -- [10.1137/21m1423269](https://doi.org/10.1137/21m1423269)
- Razaviyayn M, Hong M, Luo Z-Q (2013) A Unified Convergence Analysis of Block Successive Minimization Methods for Nonsmooth Optimization. SIAM J Optim 23(2):1126–1153. https://doi.org/10.1137/12089100 -- [10.1137/120891009](https://doi.org/10.1137/120891009)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- AP Singh, A unified view of matrix factorization models, in Joint European Conference on Machine Learning and Knowledge Discovery in Databases (2008)
- Suffridge TJ, Hayden TL (1993) Approximation by a Hermitian Positive Semidefinite Toeplitz Matrix. SIAM J Matrix Anal &amp; Appl 14(3):721–734. https://doi.org/10.1137/061405 -- [10.1137/0614052](https://doi.org/10.1137/0614052)
- Weiqian Sun, Khargonekar PP, Duksun Shim (1994) Solution to the positive real control problem for linear time-invariant systems. IEEE Trans Automat Contr 39(10):2034–2046. https://doi.org/10.1109/9.32882 -- [10.1109/9.328822](https://doi.org/10.1109/9.328822)
- Syrmos VL, Abdallah CT, Dorato P, Grigoriadis K (1997) Static output feedback—A survey. Automatica 33(2):125–137. https://doi.org/10.1016/s0005-1098(96)00141- -- [10.1016/s0005-1098(96)00141-0](https://doi.org/10.1016/s0005-1098(96)00141-0)
- Toh KC, Todd MJ, Tütüncü RH (1999) SDPT3 — A Matlab software package for semidefinite programming, Version 1.3. Optimization Methods and Software 11(1–4):545–581. https://doi.org/10.1080/1055678990880576 -- [10.1080/10556789908805762](https://doi.org/10.1080/10556789908805762)
- T�t�nc� RH, Toh KC, Todd MJ (2003) Solving semidefinite-quadratic-linear programs using SDPT3. Mathematical Programming 95(2):189–217. https://doi.org/10.1007/s10107-002-0347- -- [10.1007/s10107-002-0347-5](https://doi.org/10.1007/s10107-002-0347-5)
- Udell M, Horn C, Zadeh R, Boyd S (2016) Generalized Low Rank Models. Foundations and Trends® in Machine Learning 9(1):1–118. https://doi.org/10.1561/220000005 -- [10.1561/2200000055](https://doi.org/10.1561/2200000055)
- A van der Schaft, Port-Hamiltonian differential-algebraic systems, in Surveys in Differential-Algebraic Equations (2013)
- A van der Schaft, Arch. Elektron. Übertragungstech. (1995)
- [van der Schaft AJ, Maschke BM (2002) Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics 42(1–2):166–194. https://doi.org/10.1016/s0393-0440(01)00083-](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/s0393-0440(01)00083-3](https://doi.org/10.1016/s0393-0440(01)00083-3)
- [van der Schaft AJ, Maschke BM (2013) Port-Hamiltonian Systems on Graphs. SIAM J Control Optim 51(2):906–937. https://doi.org/10.1137/11084009](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Vandenberghe L, Boyd S (1996) Semidefinite Programming. SIAM Rev 38(1):49–95. https://doi.org/10.1137/103800 -- [10.1137/1038003](https://doi.org/10.1137/1038003)
- Varga A (1995) On stabilization methods of descriptor systems. Systems &amp; Control Letters 24(2):133–138. https://doi.org/10.1016/0167-6911(94)00017- -- [10.1016/0167-6911(94)00017-p](https://doi.org/10.1016/0167-6911(94)00017-p)
- Waldspurger I, Waters A (2020) Rank Optimality for the Burer--Monteiro Factorization. SIAM J Optim 30(3):2577–2602. https://doi.org/10.1137/19m125531 -- [10.1137/19m1255318](https://doi.org/10.1137/19m1255318)
- He-Sheng Wang, Fan-Ren Chang The generalized state-space description of positive realness and bounded realness. Proceedings of the 39th Midwest Symposium on Circuits and Systems 2:893–89 -- [10.1109/mwscas.1996.588069](https://doi.org/10.1109/mwscas.1996.588069)
- Wang Y, Zhang Z, Koh C-K, Pang GKH, Wong N (2010) PEDS: Passivity enforcement for descriptor systems via Hamiltonian-symplectic matrix pencil perturbation. 2010 IEEE/ACM International Conference on Computer-Aided Design (ICCAD) 800–80 -- [10.1109/iccad.2010.5653885](https://doi.org/10.1109/iccad.2010.5653885)
- Wen JT (1988) Time domain and frequency domain conditions for strict positive realness. IEEE Trans Automat Contr 33(10):988–992. https://doi.org/10.1109/9.726 -- [10.1109/9.7263](https://doi.org/10.1109/9.7263)
- J Wilkinson, Utilitas Math. (1984)
- H Wolkowicz, Handbook of Semidefinite Programming: Theory, Algorithms, and Applications (2012)
- Wright SJ (2015) Coordinate descent algorithms. Math Program 151(1):3–34. https://doi.org/10.1007/s10107-015-0892- -- [10.1007/s10107-015-0892-3](https://doi.org/10.1007/s10107-015-0892-3)
- S Wright, Numerical Optimization (1999)
- Xu Y, Yin W (2013) A Block Coordinate Descent Method for Regularized Multiconvex Optimization with Applications to Nonnegative Tensor Factorization and Completion. SIAM J Imaging Sci 6(3):1758–1789. https://doi.org/10.1137/12088779 -- [10.1137/120887795](https://doi.org/10.1137/120887795)
- Xu Y, Yin W (2017) A Globally Convergent Algorithm for Nonconvex Optimization Based on Block Coordinate Update. J Sci Comput 72(2):700–734. https://doi.org/10.1007/s10915-017-0376- -- [10.1007/s10915-017-0376-0](https://doi.org/10.1007/s10915-017-0376-0)
- Yip E, Sincovec R (1981) Solvability, controllability, and observability of continuous descriptor systems. IEEE Trans Automat Contr 26(3):702–707. https://doi.org/10.1109/tac.1981.110269 -- [10.1109/tac.1981.1102699](https://doi.org/10.1109/tac.1981.1102699)
- Yurtsever A, Tropp JA, Fercoq O, Udell M, Cevher V (2021) Scalable Semidefinite Programming. SIAM Journal on Mathematics of Data Science 3(1):171–200. https://doi.org/10.1137/19m130504 -- [10.1137/19m1305045](https://doi.org/10.1137/19m1305045)
- Liqian Zhang, Lam J, Shengyuan Xu (2002) On positive realness of descriptor systems. IEEE Trans Circuits Syst I 49(3):401–407. https://doi.org/10.1109/81.98918 -- [10.1109/81.989180](https://doi.org/10.1109/81.989180)
- Zhou T (2011) On Nonsingularity Verification of Uncertain Matrices Over a Quadratically Constrained Set. IEEE Trans Automat Contr 56(9):2206–2212. https://doi.org/10.1109/tac.2011.215445 -- [10.1109/tac.2011.2154450](https://doi.org/10.1109/tac.2011.2154450)

