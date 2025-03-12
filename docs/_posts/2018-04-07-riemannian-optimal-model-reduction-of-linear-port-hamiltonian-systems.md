---
layout: post
title: "Riemannian optimal model reduction of linear port-Hamiltonian systems"
date: 2018-04-07 00:00:00 +0100
permalink: riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems
year: 2018
authors: Kazuhiro Sato
category: articles
tags:
  - \\( H^2 \\) optimal model reduction
  - Linear port-Hamiltonian system
  - Riemannian optimization
---
 
## Authors
[Kazuhiro Sato](authors/kazuhiro-sato)
 
## Abstract
In this paper, we describe the development of a Riemannian optimal model reduction method for linear stable port-Hamiltonian systems. This development is motivated by the fact that there remains room for improvement in existing methods. The model reduction problem is formulated as an optimization problem on the product manifold of the set of skew symmetric matrices, the manifold of the symmetric positive definite matrices, and Euclidean space. The reduced systems constructed using the optimal solutions to the problem preserve the original structure, i.e., stability, passivity, and the port-Hamiltonian form. The Riemannian gradient is derived to relate our problem to another problem in some studies, and the Hessian is also derived to solve our problem using a Riemannian trust region method. The initial point in the proposed method is chosen by using the output of the iterative rational Krylov algorithm for linear port-Hamiltonian systems (IRKA-PH). A numerical experiment illustrates that the proposed method considerably improves the results of IRKA-PH when the reduced-model dimension is small.
 
## Keywords
\\( H^2 \\) optimal model reduction; Linear port-Hamiltonian system; Riemannian optimization
 
## Citation
- **Journal:** Automatica
- **Year:** 2018
- **Volume:** 93
- **Issue:** 
- **Pages:** 428--434
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Sato_2018,
  title={{Riemannian optimal model reduction of linear port-Hamiltonian systems}},
  volume={93},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2018.03.051},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Sato, Kazuhiro},
  year={2018},
  pages={428--434}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems.bib)
 
## References
- Absil, P.-A., Baker, C. G. & Gallivan, K. A. Trust-Region Methods on Riemannian Manifolds. Foundations of Computational Mathematics vol. 7 303–330 (2006) -- [10.1007/s10208-005-0179-9](https://doi.org/10.1007/s10208-005-0179-9)
- Absil, (2008)
- Boumal, Manopt, a MATLAB toolbox for optimization on manifolds. Journal of Machine Learning Research (JMLR) (2014)
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- Flagg, G., Beattie, C. & Gugercin, S. Convergence of the Iterative Rational Krylov Algorithm. Systems &amp; Control Letters vol. 61 688–691 (2012) -- [10.1016/j.sysconle.2012.03.005](https://doi.org/10.1016/j.sysconle.2012.03.005)
- Gugercin, S., Antoulas, A. C. & Beattie, C. $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM Journal on Matrix Analysis and Applications vol. 30 609–638 (2008) -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Ionescu, T. C. & Astolfi, A. Families of moment matching based, structure preserving approximations for linear port Hamiltonian systems. Automatica vol. 49 2424–2434 (2013)](families-of-moment-matching-based-structure-preserving-approximations-for-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.05.006](https://doi.org/10.1016/j.automatica.2013.05.006)
- Jacob, (2012)
- Putting energy back in control. IEEE Control Systems vol. 21 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- [Polyuga, R. V. & van der Schaft, A. J. Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Systems &amp; Control Letters vol. 61 412–421 (2012)](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- [Sato, K. Riemannian Optimal Control and Model Matching of Linear Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 62 6575–6581 (2017)](riemannian-optimal-control-and-model-matching-of-linear-port-hamiltonian-systems) -- [10.1109/tac.2017.2712905](https://doi.org/10.1109/tac.2017.2712905)
- Sato, Riemannian optimal model reduction of linear second-order systems. IEEE Control Systems Letters (2017)
- Sato, K. & Sato, H. Structure-Preserving $H^2$ Optimal Model Reduction Based on the Riemannian Trust-Region Method. IEEE Transactions on Automatic Control vol. 63 505–512 (2018) -- [10.1109/tac.2017.2723259](https://doi.org/10.1109/tac.2017.2723259)
- van der Schaft, (2000)
- Van Dooren, P., Gallivan, K. A. & Absil, P.-A. <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si1.gif" display="inline" overflow="scroll"><mml:msub><mml:mrow><mml:mi mathvariant="script">H</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:math>-optimal model reduction of MIMO systems. Applied Mathematics Letters vol. 21 1267–1273 (2008) -- [10.1016/j.aml.2007.09.015](https://doi.org/10.1016/j.aml.2007.09.015)
- Villegas, (2007)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control vol. 16 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)
- Wei-Yong Yan & Lam, J. An approximate approach to H/sup 2/ optimal model reduction. IEEE Transactions on Automatic Control vol. 44 1341–1358 (1999) -- [10.1109/9.774107](https://doi.org/10.1109/9.774107)

