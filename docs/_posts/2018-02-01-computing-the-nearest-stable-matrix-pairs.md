---
title: "Computing the nearest stable matrix pairs"
date: 2018-02-01 00:00:00 +0100
permalink: computing-the-nearest-stable-matrix-pairs
year: 2018
authors: Nicolas Gillis, Volker Mehrmann, Punit Sharma
category: articles
---
 
## Authors
[Nicolas Gillis](authors/nicolas-gillis), [Volker Mehrmann](authors/volker-mehrmann), [Punit Sharma](authors/punit-sharma)
 
## Abstract
In this paper, we study the nearest stable matrix pair problem: given a square matrix pair (E,A), minimize the Frobenius norm of (ΔE,ΔA) such that (E+ΔE,A+ΔA) is a stable matrix pair. We propose a reformulation of the problem with a simpler feasible set by introducing dissipative Hamiltonian matrix pairs: A matrix pair (E,A) is dissipative Hamiltonian if A=(J−R)Q with skew‐symmetric J, positive semidefinite R, and an invertible Q such that QTE is positive semidefinite. This reformulation has a convex feasible domain onto which it is easy to project. This allows us to employ a fast gradient method to obtain a nearby stable approximation of a given matrix pair.
 
## Citation
- **Journal:** Numerical Linear Algebra with Applications
- **Year:** 2018
- **Volume:** 25
- **Issue:** 5
- **Pages:** 
- **Publisher:** Wiley
- **DOI:** [10.1002/nla.2153](https://doi.org/10.1002/nla.2153)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gillis_2018,
  title={{Computing the nearest stable matrix pairs}},
  volume={25},
  ISSN={1099-1506},
  DOI={10.1002/nla.2153},
  number={5},
  journal={Numerical Linear Algebra with Applications},
  publisher={Wiley},
  author={Gillis, Nicolas and Mehrmann, Volker and Sharma, Punit},
  year={2018}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/computing-the-nearest-stable-matrix-pairs.bib)
 
## References
- Kunkel P, EMS textbooks in mathematics (2006)
- Gantmacher FR, The theory of matrices I (1959)
- Mehrmann V, Lecture notes in control and information sciences (1991)
- Varga, A. On stabilization methods of descriptor systems. Systems &amp; Control Letters vol. 24 133–138 (1995) -- [10.1016/0167-6911(94)00017-p](https://doi.org/10.1016/0167-6911(94)00017-p)
- Boyd, S., El Ghaoui, L., Feron, E. & Balakrishnan, V. Linear Matrix Inequalities in System and Control Theory. (1994) doi:10.1137/1.9781611970777 -- [10.1137/1.9781611970777](https://doi.org/10.1137/1.9781611970777)
- Byers, R. & Nichols, N. K. On the stability radius of a generalized state-space system. Linear Algebra and its Applications vols 188–189 113–134 (1993) -- [10.1016/0024-3795(93)90466-2](https://doi.org/10.1016/0024-3795(93)90466-2)
- Du, N. H., Linh, V. H. & Mehrmann, V. Robust Stability of Differential-Algebraic Equations. Surveys in Differential-Algebraic Equations I 63–95 (2013) doi:10.1007/978-3-642-34928-7_2 -- [10.1007/978-3-642-34928-7_2](https://doi.org/10.1007/978-3-642-34928-7_2)
- Benner, P. Partial Stabilization of Descriptor Systems Using Spectral Projectors. Lecture Notes in Electrical Engineering 55–76 (2011) doi:10.1007/978-94-007-0602-6_3 -- [10.1007/978-94-007-0602-6_3](https://doi.org/10.1007/978-94-007-0602-6_3)
- Singular Control Systems. Lecture Notes in Control and Information Sciences (Springer-Verlag, 1989). doi:10.1007/bfb0002475 -- [10.1007/bfb0002475](https://doi.org/10.1007/bfb0002475)
- Bunse-Gerstner, A., Mehrmann, V. & Nichols, N. K. Regularization of Descriptor Systems by Derivative and Proportional State Feedback. SIAM Journal on Matrix Analysis and Applications vol. 13 46–67 (1992) -- [10.1137/0613007](https://doi.org/10.1137/0613007)
- Bunse-Gerstner, A., Mehrmann, V. & Nichols, N. K. Regularization of descriptor systems by output feedback. IEEE Transactions on Automatic Control vol. 39 1742–1748 (1994) -- [10.1109/9.310065](https://doi.org/10.1109/9.310065)
- [Gillis, N. & Sharma, P. On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica vol. 85 113–121 (2017)](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- Orbandexivry, F.-X., Nesterov, Y. & Van Dooren, P. Nearest stable system using successive convex approximations. Automatica vol. 49 1195–1203 (2013) -- [10.1016/j.automatica.2013.01.053](https://doi.org/10.1016/j.automatica.2013.01.053)
- Byers, R., He, C. & Mehrmann, V. Where is the nearest non-regular pencil? Linear Algebra and its Applications vol. 285 81–105 (1998) -- [10.1016/s0024-3795(98)10122-2](https://doi.org/10.1016/s0024-3795(98)10122-2)
- Guglielmi, N., Lubich, C. & Mehrmann, V. On the Nearest Singular Matrix Pencil. SIAM Journal on Matrix Analysis and Applications vol. 38 776–806 (2017) -- [10.1137/16m1079026](https://doi.org/10.1137/16m1079026)
- Mehl, C., Mehrmann, V. & Wojtylak, M. On the distance to singularity via low rank perturbations. Operators and Matrices 733–772 (2015) doi:10.7153/oam-09-44 -- [10.7153/oam-09-44](https://doi.org/10.7153/oam-09-44)
- Beattie C, Port‐Hamiltonian realizations of linear time invariant systems (2015)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability Radii for Linear Hamiltonian Systems with Dissipation Under Structure-Preserving Perturbations. SIAM Journal on Matrix Analysis and Applications vol. 37 1625–1654 (2016)](stability-radii-for-linear-hamiltonian-systems-with-dissipation-under-structure-preserving-perturbations) -- [10.1137/16m1067330](https://doi.org/10.1137/16m1067330)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability radii for real linear Hamiltonian systems with perturbed dissipation. BIT Numerical Mathematics vol. 57 811–843 (2017)](stability-radii-for-real-linear-hamiltonian-systems-with-perturbed-dissipation) -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- Beattie C, Port‐Hamiltonian descriptor systems (2017)
- Gohberg I, Classics in applied mathematics (1982)
- Masubuchi, I., Kamitane, Y., Ohara, A. & Suda, N. H∞ control for descriptor systems: A matrix inequalities approach. Automatica vol. 33 669–673 (1997) -- [10.1016/s0005-1098(96)00193-8](https://doi.org/10.1016/s0005-1098(96)00193-8)
- Kautsky, J., Nichols, N. K. & Chu, E. K.-W. Robust pole assignment in singular control systems. Linear Algebra and its Applications vol. 121 9–37 (1989) -- [10.1016/0024-3795(89)90689-7](https://doi.org/10.1016/0024-3795(89)90689-7)
- Wright, S. J. Coordinate descent algorithms. Mathematical Programming vol. 151 3–34 (2015) -- [10.1007/s10107-015-0892-3](https://doi.org/10.1007/s10107-015-0892-3)
- Tisseur, F. Backward error and condition of polynomial eigenvalue problems. Linear Algebra and its Applications vol. 309 339–361 (2000) -- [10.1016/s0024-3795(99)00063-4](https://doi.org/10.1016/s0024-3795(99)00063-4)
- Nesterov, Y. Introductory Lectures on Convex Optimization. Applied Optimization (Springer US, 2004). doi:10.1007/978-1-4419-8853-9 -- [10.1007/978-1-4419-8853-9](https://doi.org/10.1007/978-1-4419-8853-9)
- Veselić, K. Damped Oscillations of Linear Systems. Lecture Notes in Mathematics (Springer Berlin Heidelberg, 2011). doi:10.1007/978-3-642-21335-9 -- [10.1007/978-3-642-21335-9](https://doi.org/10.1007/978-3-642-21335-9)
- Magnus J, Matrix differential calculus with applications in statistics and econometrics (1999)
- Olsen, P. A., Rennie, S. J. & Goel, V. Efficient Automatic Differentiation of Matrix Functions. Lecture Notes in Computational Science and Engineering 71–81 (2012) doi:10.1007/978-3-642-30023-3_7 -- [10.1007/978-3-642-30023-3_7](https://doi.org/10.1007/978-3-642-30023-3_7)

