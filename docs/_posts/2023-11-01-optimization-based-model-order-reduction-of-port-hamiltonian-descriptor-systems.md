---
layout: post
title: "Optimization-based model order reduction of port-Hamiltonian descriptor systems"
date: 2023-11-01 00:00:00 +0100
permalink: optimization-based-model-order-reduction-of-port-hamiltonian-descriptor-systems
year: 2023
authors: Paul Schwerdtner, Tim Moser, Volker Mehrmann, Matthias Voigt
category: articles
tags:
  - Port-Hamiltonian systems
  - Model order reduction
  - Structure-preservation
  - Descriptor systems
---
 
## Authors
[Paul Schwerdtner](authors/paul-schwerdtner), [Tim Moser](authors/tim-moser), [Volker Mehrmann](authors/volker-mehrmann), [Matthias Voigt](authors/matthias-voigt)
 
## Abstract
We present a new optimization-based structure-preserving model order reduction (MOR) method for port-Hamiltonian differential–algebraic equations (pH-DAEs). Our method is based on a novel parameterization that allows us to represent any linear time-invariant pH-DAE of a prescribed model order. We propose two algorithms which directly optimize the parameters of a reduced model to approximate a given large-scale model with respect to either the H ∞ or the H 2 norm. This approach has several benefits. Our parameterization ensures that the reduced model is again a pH-DAE system and enables a compact representation of the algebraic part of the large-scale model, which in projection-based methods often requires a more involved treatment. The direct optimization is entirely based on transfer function evaluations of the large-scale model and is therefore independent of the structure of the system matrices. Numerical experiments are conducted to illustrate the high accuracy and small reduced model orders in comparison to other structure-preserving MOR methods.
 
## Keywords
Port-Hamiltonian systems; Model order reduction; Structure-preservation; Descriptor systems
 
## Citation
- **Journal:** Systems &amp; Control Letters
- **Year:** 2023
- **Volume:** 182
- **Issue:** 
- **Pages:** 105655
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.sysconle.2023.105655](https://doi.org/10.1016/j.sysconle.2023.105655)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Schwerdtner_2023,
  title={{Optimization-based model order reduction of port-Hamiltonian descriptor systems}},
  volume={182},
  ISSN={0167-6911},
  DOI={10.1016/j.sysconle.2023.105655},
  journal={Systems &amp; Control Letters},
  publisher={Elsevier BV},
  author={Schwerdtner, Paul and Moser, Tim and Mehrmann, Volker and Voigt, Matthias},
  year={2023},
  pages={105655}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/optimization-based-model-order-reduction-of-port-hamiltonian-descriptor-systems.bib)
 
## References
- [Mehrmann, V., Morandin, R., Olmi, S. & Schöll, E. Qualitative stability and synchronicity analysis of power network models in port-Hamiltonian form. Chaos: An Interdisciplinary Journal of Nonlinear Science vol. 28 (2018)](qualitative-stability-and-synchronicity-analysis-of-power-network-models-in-port-hamiltonian-form) -- [10.1063/1.5054850](https://doi.org/10.1063/1.5054850)
- Domschke, (2021)
- Hauschild, Port-Hamiltonian modeling of district heating networks. (2020)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- Jacob, (2012)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Est�vez Schwarz, D. & Tischendorf, C. Structural analysis of electric circuits and consequences for MNA. International Journal of Circuit Theory and Applications vol. 28 131–162 (2000) -- [10.1002/(sici)1097-007x(200003/04)28:2<131::aid-cta100>3.0.co;2-w](https://doi.org/10.1002/(sici)1097-007x(200003/04)28:2<131::aid-cta100>3.0.co;2-w)
- Günther, CAD-based electric-circuit modeling in industry. I. Mathematical structure and index of network equations. Surv. Math. Ind. (1999)
- Günther, CAD-based electric-circuit modeling in industry. II. Impact of circuit configurations and parameters. Surv. Math. Ind. (1999)
- Dänschel, H., Mehrmann, V., Roland, M. & Schmidt, M. Adaptive nonlinear optimization of district heating networks based on model and discretization catalogs. SeMA Journal vol. 81 81–112 (2023) -- [10.1007/s40324-023-00332-6](https://doi.org/10.1007/s40324-023-00332-6)
- Mehrmann, V., Schmidt, M. & Stolwijk, J. J. Model and Discretization Error Adaptivity Within Stationary Gas Transport Optimization. Vietnam Journal of Mathematics vol. 46 779–801 (2018) -- [10.1007/s10013-018-0303-1](https://doi.org/10.1007/s10013-018-0303-1)
- [Gugercin, S., Polyuga, R. V., Beattie, C. A. & van der Schaft, A. J. Interpolation-based &amp;#x210C;&lt;inf&gt;2&lt;/inf&gt; model reduction for port-Hamiltonian systems. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference 5362–5369 (2009) doi:10.1109/cdc.2009.5400626](interpolation-based-amp-x210c-lt-inf-gt-2-lt-inf-gt-model-reduction-for-port-hamiltonian-systems) -- [10.1109/cdc.2009.5400626](https://doi.org/10.1109/cdc.2009.5400626)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Polyuga, R. V. & van der Schaft, A. J. Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Systems &amp; Control Letters vol. 61 412–421 (2012)](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- [Borja, P., Scherpen, J. M. A. & Fujimoto, K. Extended Balancing of Continuous LTI Systems: A Structure-Preserving Approach. IEEE Transactions on Automatic Control vol. 68 257–271 (2023)](extended-balancing-of-continuous-lti-systems-a-structure-preserving-approach) -- [10.1109/tac.2021.3138645](https://doi.org/10.1109/tac.2021.3138645)
- Hauschild, Model reduction techniques for linear constant coefficient port-Hamiltonian differential-algebraic systems. Control Cybern. (2019)
- Beattie, Structure-preserving interpolatory model reduction for port-Hamiltonian differential-algebraic systems. (2022)
- Desai, U. & Pal, D. A transformation approach to stochastic model reduction. IEEE Transactions on Automatic Control vol. 29 1097–1100 (1984) -- [10.1109/tac.1984.1103438](https://doi.org/10.1109/tac.1984.1103438)
- Reis, T. & Stykel, T. Positive real and bounded real balancing for model reduction of descriptor systems. International Journal of Control vol. 83 74–88 (2009) -- [10.1080/00207170903100214](https://doi.org/10.1080/00207170903100214)
- Mehrmann, Balanced truncation model reduction for large-scale system in descriptor form. (2005)
- [Breiten, T. & Unger, B. Passivity preserving model reduction via spectral factorization. Automatica vol. 142 110368 (2022)](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- [Beattie, C., Mehrmann, V., Xu, H. & Zwart, H. Linear port-Hamiltonian descriptor systems. Mathematics of Control, Signals, and Systems vol. 30 (2018)](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- [Mehl, C., Mehrmann, V. & Wojtylak, M. Distance problems for dissipative Hamiltonian systems and related matrix polynomials. Linear Algebra and its Applications vol. 623 335–366 (2021)](distance-problems-for-dissipative-hamiltonian-systems-and-related-matrix-polynomials) -- [10.1016/j.laa.2020.05.026](https://doi.org/10.1016/j.laa.2020.05.026)
- Benner, Model order reduction for differential-algebraic equations: A survey. (2017)
- Gugercin, S., Stykel, T. & Wyatt, S. Model Reduction of Descriptor Systems by Interpolatory Projection Methods. SIAM Journal on Scientific Computing vol. 35 B1010–B1033 (2013) -- [10.1137/130906635](https://doi.org/10.1137/130906635)
- [Mehl, C., Mehrmann, V. & Wojtylak, M. Linear Algebra Properties of Dissipative Hamiltonian Descriptor Systems. SIAM Journal on Matrix Analysis and Applications vol. 39 1489–1519 (2018)](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18m1164275](https://doi.org/10.1137/18m1164275)
- Moser, T. & Lohmann, B. A New Riemannian Framework for Efficient ℋ2-Optimal Model Reduction of Port-Hamiltonian Systems. 2020 59th IEEE Conference on Decision and Control (CDC) 5043–5049 (2020) doi:10.1109/cdc42340.2020.9304134 -- [10.1109/cdc42340.2020.9304134](https://doi.org/10.1109/cdc42340.2020.9304134)
- [Schwerdtner, P. & Voigt, M. SOBMOR: Structured Optimization-Based Model Order Reduction. SIAM Journal on Scientific Computing vol. 45 A502–A529 (2023)](sobmor-structured-optimization-based-model-order-reduction) -- [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
- Stykel, T. Gramian-Based Model Reduction for Descriptor Systems. Mathematics of Control, Signals, and Systems (MCSS) vol. 16 297–319 (2004) -- [10.1007/s00498-004-0141-4](https://doi.org/10.1007/s00498-004-0141-4)
- Benner, P. & Werner, S. W. R. Model Reduction of Descriptor Systems with the MORLAB Toolbox. IFAC-PapersOnLine vol. 51 547–552 (2018) -- [10.1016/j.ifacol.2018.03.092](https://doi.org/10.1016/j.ifacol.2018.03.092)
- Banagaaya, N. & Schilders, W. H. A. Index-Aware Model Order Reduction for Higher Index DAEs. Differential-Algebraic Equations Forum 155–182 (2014) doi:10.1007/978-3-662-44926-4_8 -- [10.1007/978-3-662-44926-4_8](https://doi.org/10.1007/978-3-662-44926-4_8)
- Gugercin, S., Antoulas, A. C. & Beattie, C. $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM Journal on Matrix Analysis and Applications vol. 30 609–638 (2008) -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- Antoulas, (2020)
- Guiver, C. & Opmeer, M. R. Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra and its Applications vol. 439 3659–3698 (2013) -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- Cherifi, (2022)
- Achleitner, Hypocoercivity and controllability in linear semi-dissipative Hamiltonian ordinary differential equations and differential-algebraic equations. ZAMM J. Appl. Math. Mech. (2021)
- Güdücü, (2021)
- Anderson, (1973)
- Wohlers, (1969)
- Beattie, (2022)
- Antoulas, Data-driven model reduction for a class of semi-explicit DAEs using the loewner framework. (2020)
- Schwerdtner, P., Mengi, E. & Voigt, M. Certifying Global Optimality for the L∞-Norm Computation of Large-Scale Descriptor Systems. IFAC-PapersOnLine vol. 53 4279–4284 (2020) -- [10.1016/j.ifacol.2020.12.2482](https://doi.org/10.1016/j.ifacol.2020.12.2482)
- [Schwerdtner, P. & Voigt, M. Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine vol. 54 143–148 (2021)](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- Beattie, C. A. & Gugercin, S. A trust region method for optimal H&lt;inf&gt;2&lt;/inf&gt; model reduction. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference 5370–5375 (2009) doi:10.1109/cdc.2009.5400605 -- [10.1109/cdc.2009.5400605](https://doi.org/10.1109/cdc.2009.5400605)
- Van Dooren, P., Gallivan, K. A. & Absil, P.-A. $\mathcal{H}_2$-Optimal Model Reduction with Higher-Order Poles. SIAM Journal on Matrix Analysis and Applications vol. 31 2738–2753 (2010) -- [10.1137/080731591](https://doi.org/10.1137/080731591)
- [Sato, K. Riemannian optimal model reduction of linear port-Hamiltonian systems. Automatica vol. 93 428–434 (2018)](riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
- Jiang, Model order reduction of port-Hamiltonian systems by Riemannian modified Fletcher–Reeves scheme. IEEE Trans. Circuits Syst. II Express Briefs (2019)
- van der Schaft, (2022)
- Gillis, N. & Sharma, P. On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica vol. 85 113–121 (2017) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- [Hauschild, S.-A., Marheineke, N. & Mehrmann, V. Model reduction techniques for port‐Hamiltonian differential‐algebraic systems. PAMM vol. 19 (2019)](model-reduction-techniques-for-port-hamiltonian-differential-algebraic-systems) -- [10.1002/pamm.201900040](https://doi.org/10.1002/pamm.201900040)
- Freund, The SPRIM algorithm for structure-preserving order reduction of general RCL circuits. (2011)
- Trefethen, L. N. Rational Chebyshev approximation on the unit disk. Numerische Mathematik vol. 37 297–320 (1981) -- [10.1007/bf01398258](https://doi.org/10.1007/bf01398258)

