---
title: "A flexible short recurrence Krylov subspace method for matrices arising in the time integration of port-Hamiltonian systems and ODEs/DAEs with a dissipative Hamiltonian"
date: 2023-11-10 00:00:00 +0100
permalink: a-flexible-short-recurrence-krylov-subspace-method-for-matrices-arising-in-the-time-integration-of-port-hamiltonian-systems-and-odes-daes-with-a-dissipative-hamiltonian
year: 2023
authors: Malak Diab, Andreas Frommer, Karsten Kahl
category: articles
tags:
  - Krylov subspace
  - Short recurrence
  - Right preconditioning
  - Optimal methods
  - Flexible preconditioning
  - Dissipative Hamiltonian
  - Port-Hamiltonian systems
  - Implicit time integration
  - 65F08
  - 65F10
  - 65L04
  - 65L80
---
 
## Authors
[Malak Diab](authors/malak-diab), [Andreas Frommer](authors/andreas-frommer), [Karsten Kahl](authors/karsten-kahl)
 
## Abstract
For several classes of mathematical models that yield linear systems, the splitting of the matrix into its Hermitian and skew Hermitian parts is naturally related to properties of the underlying model. This is particularly so for discretizations of dissipative Hamiltonian ODEs, DAEs and port-Hamiltonian systems where, in addition, the Hermitian part is positive definite or semi-definite. It is then possible to develop short recurrence optimal Krylov subspace methods in which the Hermitian part is used as a preconditioner. In this paper, we develop new, right preconditioned variants of this approach which, as their crucial new feature, allow the systems with the Hermitian part to be solved only approximately in each iteration while keeping the short recurrences. This new class of methods is particularly efficient as it allows, for example, to use few steps of a multigrid solver or a (preconditioned) CG method for the Hermitian part in each iteration. We illustrate this with several numerical experiments for large scale systems.
 
## Keywords
Krylov subspace; Short recurrence; Right preconditioning; Optimal methods; Flexible preconditioning; Dissipative Hamiltonian; Port-Hamiltonian systems; Implicit time integration; 65F08; 65F10; 65L04; 65L80
 
## Citation
- **Journal:** BIT Numerical Mathematics
- **Year:** 2023
- **Volume:** 63
- **Issue:** 4
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10543-023-00999-3](https://doi.org/10.1007/s10543-023-00999-3)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Diab_2023,
  title={{A flexible short recurrence Krylov subspace method for matrices arising in the time integration of port-Hamiltonian systems and ODEs/DAEs with a dissipative Hamiltonian}},
  volume={63},
  ISSN={1572-9125},
  DOI={10.1007/s10543-023-00999-3},
  number={4},
  journal={BIT Numerical Mathematics},
  publisher={Springer Science and Business Media LLC},
  author={Diab, Malak and Frommer, Andreas and Kahl, Karsten},
  year={2023}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-flexible-short-recurrence-krylov-subspace-method-for-matrices-arising-in-the-time-integration-of-port-hamiltonian-systems-and-odes-daes-with-a-dissipative-hamiltonian.bib)
 
## References
- Arioli, M., Liesen, J., Miçdlar, A. & Strakoš, Z. Interplay between discretization and algebraic computation in adaptive numerical solutionof elliptic PDE problems. GAMM-Mitteilungen 36, 102–129 (2013) -- [10.1002/gamm.201310006](https://doi.org/10.1002/gamm.201310006)
- Banagaaya, N. et al. Model Order Reduction for Nanoelectronics Coupled Problems with Many Inputs. Proceedings of the 2016 Design, Automation &amp; Test in Europe Conference &amp; Exhibition (DATE) 313–318 (2016) doi:10.3850/9783981537079_0996 -- [10.3850/9783981537079_0996](https://doi.org/10.3850/9783981537079_0996)
- Concus, P. & Golub, G. H. A Generalized Conjugate Gradient Method for Nonsymmetric Systems of Linear Equations. Lecture Notes in Economics and Mathematical Systems 56–65 (1976) doi:10.1007/978-3-642-85972-4_4 -- [10.1007/978-3-642-85972-4_4](https://doi.org/10.1007/978-3-642-85972-4_4)
- Eisenstat, S. C. A Note on the Generalized Conjugate Gradient Method. SIAM J. Numer. Anal. 20, 358–361 (1983) -- [10.1137/0720024](https://doi.org/10.1137/0720024)
- Faber, V. & Manteuffel, T. Necessary and Sufficient Conditions for the Existence of a Conjugate Gradient Method. SIAM J. Numer. Anal. 21, 352–362 (1984) -- [10.1137/0721026](https://doi.org/10.1137/0721026)
- Freund, R. On conjugate gradient type methods and polynomial preconditioners for a class of complex non-hermitian matrices. Numer. Math. 57, 285–312 (1990) -- [10.1007/bf01386412](https://doi.org/10.1007/bf01386412)
- Freund, R. W. & Nachtigal, N. M. QMR: a quasi-minimal residual method for non-Hermitian linear systems. Numer. Math. 60, 315–339 (1991) -- [10.1007/bf01385726](https://doi.org/10.1007/bf01385726)
- VM Fridman, Ž Vyčisl Mat i Mat Fiz (1962)
- Golub, G. H. & Ye, Q. Inexact Preconditioned Conjugate Gradient Method with Inner-Outer Iteration. SIAM J. Sci. Comput. 21, 1305–1320 (1999) -- [10.1137/s1064827597323415](https://doi.org/10.1137/s1064827597323415)
- [Güdücü, C., Liesen, J., Mehrmann, V. & Szyld, D. B. On Non-Hermitian Positive (Semi)Definite Linear Algebraic Systems Arising from Dissipative Hamiltonian DAEs. SIAM J. Sci. Comput. 44, A2871–A2894 (2022)](on-non-hermitian-positive-semi-definite-linear-algebraic-systems-arising-from-dissipative-hamiltonian-daes) -- [10.1137/21m1458594](https://doi.org/10.1137/21m1458594)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48, 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Hageman, L. A., Luk, F. T. & Young, D. M. On the Equivalence of Certain Iterative Acceleration Methods. SIAM J. Numer. Anal. 17, 852–873 (1980) -- [10.1137/0717071](https://doi.org/10.1137/0717071)
- Liesen, J. When is the Adjoint of a Matrix a Low Degree Rational Function in the Matrix? SIAM J. Matrix Anal. &amp; Appl. 29, 1171–1180 (2008) -- [10.1137/060675538](https://doi.org/10.1137/060675538)
- J Liesen, Krylov Subspace Methods. Numerical Mathematics and Scientific Computation—Principles and Analysis (2013)
- Málek, J. & Strakoš, Z. Preconditioning and the Conjugate Gradient Method in the Context of Solving PDEs. (2014) doi:10.1137/1.9781611973846 -- [10.1137/1.9781611973846](https://doi.org/10.1137/1.9781611973846)
- DOI not foun -- [10.48550/arxiv.1903.10451,](https://doi.org/10.48550/arxiv.1903.10451,)
- Mehrmann, V. & Stykel, T. Balanced Truncation Model Reduction for Large-Scale Systems in Descriptor Form. Lecture Notes in Computational Science and Engineering 83–115 doi:10.1007/3-540-27909-1_3 -- [10.1007/3-540-27909-1_3](https://doi.org/10.1007/3-540-27909-1_3)
- Meurant, G., Papež, J. & Tichý, P. Accurate error estimation in CG. Numer Algor 88, 1337–1359 (2021) -- [10.1007/s11075-021-01078-w](https://doi.org/10.1007/s11075-021-01078-w)
- Notay, Y. Flexible Conjugate Gradients. SIAM J. Sci. Comput. 22, 1444–1460 (2000) -- [10.1137/s1064827599362314](https://doi.org/10.1137/s1064827599362314)
- Paige, C. C. & Saunders, M. A. Solution of Sparse Indefinite Systems of Linear Equations. SIAM J. Numer. Anal. 12, 617–629 (1975) -- [10.1137/0712047](https://doi.org/10.1137/0712047)
- Saad, Y. A Flexible Inner-Outer Preconditioned GMRES Algorithm. SIAM J. Sci. Comput. 14, 461–469 (1993) -- [10.1137/0914028](https://doi.org/10.1137/0914028)
- Saad, Y. Iterative Methods for Sparse Linear Systems. (2003) doi:10.1137/1.9780898718003 -- [10.1137/1.9780898718003](https://doi.org/10.1137/1.9780898718003)
- Sarkis, M. & Szyld, D. B. Optimal left and right additive Schwarz preconditioning for minimal residual methods with Euclidean and energy norms. Computer Methods in Applied Mechanics and Engineering 196, 1612–1621 (2007) -- [10.1016/j.cma.2006.03.027](https://doi.org/10.1016/j.cma.2006.03.027)
- Simoncini, V. & Szyld, D. B. Recent computational developments in Krylov subspace methods for linear systems. Numerical Linear Algebra App 14, 1–59 (2006) -- [10.1002/nla.499](https://doi.org/10.1002/nla.499)
- Szyld, D. B. & Vogel, J. A. FQMR: A Flexible Quasi-Minimal Residual Method with Inexact Preconditioning. SIAM J. Sci. Comput. 23, 363–380 (2001) -- [10.1137/s106482750037336x](https://doi.org/10.1137/s106482750037336x)
- DB Szyld, East-West J. Numer. Math. (1993)
- U Trottenberg, Multigrid (2001)
- Van der Vorst, H. A. & Vuik, C. GMRESR: a family of nested GMRES methods. Numerical Linear Algebra App 1, 369–386 (1994) -- [10.1002/nla.1680010404](https://doi.org/10.1002/nla.1680010404)
- Widlund, O. A Lanczos Method for a Class of Nonsymmetric Systems of Linear Equations. SIAM J. Numer. Anal. 15, 801–812 (1978) -- [10.1137/0715053](https://doi.org/10.1137/0715053)

