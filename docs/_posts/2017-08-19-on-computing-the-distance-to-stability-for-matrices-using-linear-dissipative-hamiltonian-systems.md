---
title: "On computing the distance to stability for matrices using linear dissipative Hamiltonian systems"
date: 2017-08-19 00:00:00 +0100
permalink: on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems
year: 2017
authors: Nicolas Gillis, Punit Sharma
category: articles
tags:
  - Dissipative Hamiltonian systems
  - Distance to stability
  - Convex optimization
---
 
## Authors
[Nicolas Gillis](authors/nicolas-gillis), [Punit Sharma](authors/punit-sharma)
 
## Abstract
In this paper, we consider the problem of computing the nearest stable matrix to an unstable one. We propose new algorithms to solve this problem based on a reformulation using linear dissipative Hamiltonian systems: we show that a matrix A is stable if and only if it can be written as A = ( J − R ) Q , where J = − J T , R ⪰ 0 and Q ≻ 0 (that is, R is positive semidefinite and Q is positive definite). This reformulation results in an equivalent optimization problem with a simple convex feasible set. We propose three strategies to solve the problem in variables ( J , R , Q ) : (i) a block coordinate descent method, (ii) a projected gradient descent method, and (iii) a fast gradient method inspired from smooth convex optimization. These methods require O ( n 3 ) operations per iteration, where n is the size of A . We show the effectiveness of the fast gradient method compared to the other approaches and to several state-of-the-art algorithms.
 
## Keywords
Dissipative Hamiltonian systems; Distance to stability; Convex optimization
 
## Citation
- **Journal:** Automatica
- **Year:** 2017
- **Volume:** 85
- **Issue:** 
- **Pages:** 113--121
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gillis_2017,
  title={{On computing the distance to stability for matrices using linear dissipative Hamiltonian systems}},
  volume={85},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2017.07.047},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Gillis, Nicolas and Sharma, Punit},
  year={2017},
  pages={113--121}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems.bib)
 
## References
- Alam, R., Bora, S., Karow, M., Mehrmann, V. & Moro, J. Perturbation Theory for Hamiltonian Matrices and the Distance to Bounded-Realness. SIAM J. Matrix Anal. &amp; Appl. 32, 484–514 (2011) -- [10.1137/10079464x](https://doi.org/10.1137/10079464x)
- Boyd, (1994)
- Burke, J. V., Henrion, D., Lewis, A. S. & Overton, M. L. HIFOO - A MATLAB PACKAGE FOR FIXED-ORDER CONTROLLER DESIGN AND H OPTIMIZATION. IFAC Proceedings Volumes 39, 339–344 (2006) -- [10.3182/20060705-3-fr-2907.00059](https://doi.org/10.3182/20060705-3-fr-2907.00059)
- Burke, J. V., Henrion, D., Lewis, A. S. & Overton, M. L. Stabilization via Nonsmooth, Nonconvex Optimization. IEEE Trans. Automat. Contr. 51, 1760–1769 (2006) -- [10.1109/tac.2006.884944](https://doi.org/10.1109/tac.2006.884944)
- Byers, R. A Bisection Method for Measuring the Distance of a Stable Matrix to the Unstable Matrices. SIAM J. Sci. and Stat. Comput. 9, 875–881 (1988) -- [10.1137/0909059](https://doi.org/10.1137/0909059)
- D’haene, T., Pintelon, R. & Vandersteen, G. An Iterative Method to Stabilize a Transfer Function in the&lt;tex&gt;$s$&lt;/tex&gt;- and&lt;tex&gt;$z$&lt;/tex&gt;-Domains. IEEE Trans. Instrum. Meas. 55, 1192–1196 (2006) -- [10.1109/tim.2006.876567](https://doi.org/10.1109/tim.2006.876567)
- Ghadimi, S. & Lan, G. Accelerated gradient methods for nonconvex nonlinear and stochastic programming. Math. Program. 156, 59–99 (2015) -- [10.1007/s10107-015-0871-8](https://doi.org/10.1007/s10107-015-0871-8)
- Golo, Hamiltonian formulation of bond graphs. (2003)
- Grippo, L. & Sciandrone, M. On the convergence of the block nonlinear Gauss–Seidel method under convex constraints. Operations Research Letters 26, 127–136 (2000) -- [10.1016/s0167-6377(99)00074-7](https://doi.org/10.1016/s0167-6377(99)00074-7)
- Higham, N. J. Computing a nearest symmetric positive semidefinite matrix. Linear Algebra and its Applications 103, 103–118 (1988) -- [10.1016/0024-3795(88)90223-6](https://doi.org/10.1016/0024-3795(88)90223-6)
- Higham, (1988)
- Hinrichsen, D. & Pritchard, A. J. Stability radii of linear systems. Systems &amp; Control Letters 7, 1–10 (1986) -- [10.1016/0167-6911(86)90094-0](https://doi.org/10.1016/0167-6911(86)90094-0)
- Horn, (1985)
- Lancaster, (1985)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability Radii for Linear Hamiltonian Systems with Dissipation Under Structure-Preserving Perturbations. SIAM J. Matrix Anal. &amp; Appl. 37, 1625–1654 (2016)](stability-radii-for-linear-hamiltonian-systems-with-dissipation-under-structure-preserving-perturbations) -- [10.1137/16m1067330](https://doi.org/10.1137/16m1067330)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability radii for real linear Hamiltonian systems with perturbed dissipation. Bit Numer Math 57, 811–843 (2017)](stability-radii-for-real-linear-hamiltonian-systems-with-perturbed-dissipation) -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- Moses, R. L. & Liu, D. Determining the closest stable polynomial to an unstable one. IEEE Trans. Signal Process. 39, 901–906 (1991) -- [10.1109/78.80912](https://doi.org/10.1109/78.80912)
- Nesterov, (2004)
- Orbandexivry, F.-X., Nesterov, Y. & Van Dooren, P. Nearest stable system using successive convex approximations. Automatica 49, 1195–1203 (2013) -- [10.1016/j.automatica.2013.01.053](https://doi.org/10.1016/j.automatica.2013.01.053)
- Ostrowski, (1960)
- Packard, A. & Doyle, J. The complex structured singular value. Automatica 29, 71–109 (1993) -- [10.1016/0005-1098(93)90175-s](https://doi.org/10.1016/0005-1098(93)90175-s)
- Sturm, J. F. Using SeDuMi 1.02, A Matlab toolbox for optimization over symmetric cones. Optimization Methods and Software 11, 625–653 (1999) -- [10.1080/10556789908805766](https://doi.org/10.1080/10556789908805766)
- Toh, K. C., Todd, M. J. & Tütüncü, R. H. SDPT3 — A Matlab software package for semidefinite programming, Version 1.3. Optimization Methods and Software 11, 545–581 (1999) -- [10.1080/10556789908805762](https://doi.org/10.1080/10556789908805762)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM J. Control Optim. 51, 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- Wilkinson, Sensitivity of eigenvalues. Utilitas Mathematica (1984)
- Wright, S. J. Coordinate descent algorithms. Math. Program. 151, 3–34 (2015) -- [10.1007/s10107-015-0892-3](https://doi.org/10.1007/s10107-015-0892-3)
- Zhou, T. On Nonsingularity Verification of Uncertain Matrices Over a Quadratically Constrained Set. IEEE Trans. Automat. Contr. 56, 2206–2212 (2011) -- [10.1109/tac.2011.2154450](https://doi.org/10.1109/tac.2011.2154450)

