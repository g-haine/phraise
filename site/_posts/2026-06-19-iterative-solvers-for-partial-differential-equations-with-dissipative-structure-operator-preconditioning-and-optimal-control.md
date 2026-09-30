---
title: "Iterative solvers for partial differential equations with dissipative structure: operator preconditioning and optimal control"
date: 2026-06-19 00:00:00 +0100
permalink: iterative-solvers-for-partial-differential-equations-with-dissipative-structure-operator-preconditioning-and-optimal-control
year: 2026
authors: Volker Mehrmann, Manuel Schaller, Martin Stoll
category: articles
---
 
## Authors
[Volker Mehrmann](authors/volker-mehrmann), [Manuel Schaller](authors/manuel-schaller), [Martin Stoll](authors/martin-stoll)
 
## Abstract
This work considers the iterative solution of large-scale problems subject to non-symmetric matrices or operators arising in discretizations of (port-)Hamiltonian partial differential equations. We consider problems governed by an operator \\( \mathcal{A}=\mathcal{H}+\mathcal{S} \\) with a symmetric part \\( \mathcal{H} \\) that is positive (semi-)definite and a skew-symmetric part \\( \mathcal{S} \\). Prior work has shown that the structure and sparsity of the associated linear system enables Krylov subspace solvers such as the generalized minimal residual method (GMRES) or short recurrence variants such as Widlund\'s or Rapoport\'s method using the symmetric part \\( \mathcal{H} \\), or an approximation of it, as preconditioner. In this work, we analyze the resulting condition numbers, which are crucial for fast convergence of these methods, for various partial differential equations (PDEs) arising in diffusion phenomena, fluid dynamics, and elasticity. We show that preconditioning with the symmetric part leads to a condition number uniform in the mesh size in the case of elliptic and parabolic PDEs, where \\( \mathcal{H}^{-1}\mathcal{S} \\) is a bounded operator. Further, we employ the tailored Krylov subspace methods in optimal control by means of a condensing approach and a constraint preconditioner for the optimality system. We illustrate the results by various large-scale numerical examples and discuss efficient evaluations of the preconditioner such as the incomplete Cholesky factorization or the algebraic multigrid method.
 
## Citation
- **Journal:** ETNA - Electronic Transactions on Numerical Analysis
- **Year:** 2026
- **Volume:** 65
- **Issue:** 
- **Pages:** 226--253
- **Publisher:** Osterreichische Akademie der Wissenschaften, Verlag
- **DOI:** [10.1553/etna_vol65s226](https://doi.org/10.1553/etna_vol65s226)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Mehrmann_2026,
  title={{Iterative solvers for partial differential equations with dissipative structure: operator preconditioning and optimal control}},
  volume={65},
  ISSN={1068-9613},
  DOI={10.1553/etna_vol65s226},
  journal={ETNA - Electronic Transactions on Numerical Analysis},
  publisher={Osterreichische Akademie der Wissenschaften, Verlag},
  author={Mehrmann, Volker and Schaller, Manuel and Stoll, Martin},
  year={2026},
  pages={226--253}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/iterative-solvers-for-partial-differential-equations-with-dissipative-structure-operator-preconditioning-and-optimal-control.bib)
 
