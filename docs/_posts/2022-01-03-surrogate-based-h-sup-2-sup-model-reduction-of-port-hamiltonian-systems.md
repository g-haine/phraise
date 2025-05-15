---
layout: post
title: "Surrogate-Based ℋ<sup>2</sup> Model Reduction of Port-Hamiltonian Systems"
date: 2022-01-03 00:00:00 +0100
permalink: surrogate-based-h-sup-2-sup-model-reduction-of-port-hamiltonian-systems
year: 2021
authors: Tim Moser, Julius Durmann, Boris Lohmann
category: proceedings
---
 
## Authors
[Tim Moser](authors/tim-moser), [Julius Durmann](authors/julius-durmann), [Boris Lohmann](authors/boris-lohmann)
 
## Abstract
Interpolatory methods for structure-preserving model reduction of port-Hamiltonian systems are especially suitable for very large-scale models, owing to their low computational cost and memory requirements. \\( {[[:space:]]{\mathcal{H}[[:space:]]}_2} \\)-based techniques iteratively search for models which fulfill a subset of first-order \\( {[[:space:]]{\mathcal{H}[[:space:]]}_2} \\)-optimality conditions. In each iteration, a new reduced-order model is computed, which might weaken the computational advantages in cases of slow convergence. We propose a new structure-preserving framework for port-Hamiltonian systems based on surrogate modeling. By exploiting the local nature of the \\( {[[:space:]]{\mathcal{H}[[:space:]]}_2} \\)-optimization problem, the cost of optimization is decoupled from the cost of reduction. Consequently, \\( {[[:space:]]{\mathcal{H}[[:space:]]}_2} \\)-based interpolatory methods can be accelerated significantly and especially for very large-scale port-Hamiltonian systems, which is illustrated by a numerical example.
 
## Citation
- **Journal:** 2021 European Control Conference (ECC)
- **Year:** 2021
- **Volume:** 
- **Issue:** 
- **Pages:** 2058--2065
- **Publisher:** IEEE
- **DOI:** [10.23919/ecc54610.2021.9655109](https://doi.org/10.23919/ecc54610.2021.9655109)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Moser_2021,
  title={{Surrogate-Based ℋ2 Model Reduction of Port-Hamiltonian Systems}},
  DOI={10.23919/ecc54610.2021.9655109},
  booktitle={{2021 European Control Conference (ECC)}},
  publisher={IEEE},
  author={Moser, Tim and Durmann, Julius and Lohmann, Boris},
  year={2021},
  pages={2058--2065}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/surrogate-based-h-sup-2-sup-model-reduction-of-port-hamiltonian-systems.bib)
 
## References
- Castagnotto, A., Panzer, H. K. F. & Lohmann, B. Fast H&lt;inf&gt;2&lt;/inf&gt;-optimal model order reduction exploiting the local nature of Krylov-subspace methods. 2016 European Control Conference (ECC) 1958–1969 (2016) doi:10.1109/ecc.2016.7810578 -- [10.1109/ecc.2016.7810578](https://doi.org/10.1109/ecc.2016.7810578)
- Castagnotto, A. & Lohmann, B. A new framework for H2-optimal model reduction. Mathematical and Computer Modelling of Dynamical Systems 24, 236–257 (2018) -- [10.1080/13873954.2018.1464030](https://doi.org/10.1080/13873954.2018.1464030)
- Antoulas, A. C., Beattie, C. A. & Güğercin, S. Interpolatory Methods for Model Reduction. (Society for Industrial and Applied Mathematics, 2020). doi:10.1137/1.9781611976083 -- [10.1137/1.9781611976083](https://doi.org/10.1137/1.9781611976083)
- Chu, K. E. The solution of the matrix equations AXB−CXD=E AND (YA−DZ,YC−BZ)=(E,F). Linear Algebra and its Applications 93, 93–105 (1987) -- [10.1016/s0024-3795(87)90314-4](https://doi.org/10.1016/s0024-3795(87)90314-4)
- Gallivan, K., Vandendorpe, A. & Van Dooren, P. Sylvester equations and projection-based model reduction. Journal of Computational and Applied Mathematics 162, 213–229 (2004) -- [10.1016/j.cam.2003.08.026](https://doi.org/10.1016/j.cam.2003.08.026)
- Beattie, C. & Gugercin, S. Chapter 7: Model Reduction by Rational Interpolation. Model Reduction and Approximation 297–334 (2017) doi:10.1137/1.9781611974829.ch7 -- [10.1137/1.9781611974829.ch7](https://doi.org/10.1137/1.9781611974829.ch7)
- Wilson, D. A. Optimum solution of model-reduction problem. Proc. Inst. Electr. Eng. UK 117, 1161 (1970) -- [10.1049/piee.1970.0227](https://doi.org/10.1049/piee.1970.0227)
- Wei-Yong Yan & Lam, J. An approximate approach to H/sup 2/ optimal model reduction. IEEE Trans. Automat. Contr. 44, 1341–1358 (1999) -- [10.1109/9.774107](https://doi.org/10.1109/9.774107)
- Meier, L. & Luenberger, D. Approximation of linear constant systems. IEEE Trans. Automat. Contr. 12, 585–588 (1967) -- [10.1109/tac.1967.1098680](https://doi.org/10.1109/tac.1967.1098680)
- Beattie, C. A. & Gugercin, S. Krylov-based minimization for optimal H&lt;inf&gt;2&lt;/inf&gt; model reduction. 2007 46th IEEE Conference on Decision and Control 4385–4390 (2007) doi:10.1109/cdc.2007.4434939 -- [10.1109/cdc.2007.4434939](https://doi.org/10.1109/cdc.2007.4434939)
- kotyczka, Numerical Methods for Distributed Parameter Port-Hamiltonian Systems (2019)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. FnT in Systems and Control 1, 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48, 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- gugercin, Interpolation-based H2 model reduction for port-Hamiltonian systems. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) Held Jointly with 2009 28th Chinese Control Conference (2009)
- [Moser, T. & Lohmann, B. A New Riemannian Framework for Efficient ℋ2-Optimal Model Reduction of Port-Hamiltonian Systems. 2020 59th IEEE Conference on Decision and Control (CDC) 5043–5049 (2020) doi:10.1109/cdc42340.2020.9304134](a-new-riemannian-framework-for-efficient-h-sub-2-sub-optimal-model-reduction-of-port-hamiltonian-systems) -- [10.1109/cdc42340.2020.9304134](https://doi.org/10.1109/cdc42340.2020.9304134)
- [Sato, K. Riemannian optimal model reduction of linear port-Hamiltonian systems. Automatica 93, 428–434 (2018)](riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
- Putting energy back in control. IEEE Control Syst. 21, 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- panzer, Model order reduction by Krylov subspace methods with global error bounds and automatic choice of parameters. Dissertation (2014)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control 16, 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)
- [Polyuga, R. V. & van der Schaft, A. Structure Preserving Moment Matching for Port-Hamiltonian Systems: Arnoldi and Lanczos. IEEE Trans. Automat. Contr. 56, 1458–1462 (2011)](structure-preserving-moment-matching-for-port-hamiltonian-systems-arnoldi-and-lanczos) -- [10.1109/tac.2011.2128650](https://doi.org/10.1109/tac.2011.2128650)
- Van Dooren, P., Gallivan, K. A. & Absil, P.-A. <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si1.gif" display="inline" overflow="scroll"><mml:msub><mml:mrow><mml:mi mathvariant="script">H</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:math>-optimal model reduction of MIMO systems. Applied Mathematics Letters 21, 1267–1273 (2008) -- [10.1016/j.aml.2007.09.015](https://doi.org/10.1016/j.aml.2007.09.015)
- [Mehl, C., Mehrmann, V. & Wojtylak, M. Linear Algebra Properties of Dissipative Hamiltonian Descriptor Systems. SIAM J. Matrix Anal. &amp; Appl. 39, 1489–1519 (2018)](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18m1164275](https://doi.org/10.1137/18m1164275)

