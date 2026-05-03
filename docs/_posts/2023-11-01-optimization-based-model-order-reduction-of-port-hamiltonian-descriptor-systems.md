---
title: "Optimization-based model order reduction of port-Hamiltonian descriptor systems"
date: 2023-11-01 00:00:00 +0100
permalink: optimization-based-model-order-reduction-of-port-hamiltonian-descriptor-systems
year: 2023
authors: Paul Schwerdtner, Tim Moser, Volker Mehrmann, Matthias Voigt
category: articles
tags:
  - descriptor systems, model order reduction, port-hamiltonian systems, structure-preservation
---
 
## Authors
[Paul Schwerdtner](authors/paul-schwerdtner), [Tim Moser](authors/tim-moser), [Volker Mehrmann](authors/volker-mehrmann), [Matthias Voigt](authors/matthias-voigt)
 
## Abstract
We present a new optimization-based structure-preserving model order reduction (MOR) method for port-Hamiltonian differential–algebraic equations (pH-DAEs). Our method is based on a novel parameterization that allows us to represent any linear time-invariant pH-DAE of a prescribed model order. We propose two algorithms which directly optimize the parameters of a reduced model to approximate a given large-scale model with respect to either the H ∞ or the H 2 norm. This approach has several benefits. Our parameterization ensures that the reduced model is again a pH-DAE system and enables a compact representation of the algebraic part of the large-scale model, which in projection-based methods often requires a more involved treatment. The direct optimization is entirely based on transfer function evaluations of the large-scale model and is therefore independent of the structure of the system matrices. Numerical experiments are conducted to illustrate the high accuracy and small reduced model orders in comparison to other structure-preserving MOR methods.
 
## Keywords
descriptor systems, model order reduction, port-hamiltonian systems, structure-preservation
 
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
  journal={Systems \&amp; Control Letters},
  publisher={Elsevier BV},
  author={Schwerdtner, Paul and Moser, Tim and Mehrmann, Volker and Voigt, Matthias},
  year={2023},
  pages={105655}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/optimization-based-model-order-reduction-of-port-hamiltonian-descriptor-systems.bib)
 
## References
- [Mehrmann V, Morandin R, Olmi S, Schöll E (2018) Qualitative stability and synchronicity analysis of power network models in port-Hamiltonian form. Chaos: An Interdisciplinary Journal of Nonlinear Science 28(10). https://doi.org/10.1063/1.505485](qualitative-stability-and-synchronicity-analysis-of-power-network-models-in-port-hamiltonian-form) -- [10.1063/1.5054850](https://doi.org/10.1063/1.5054850)
- Domschke, (2021)
- Hauschild, Port-Hamiltonian modeling of district heating networks. (2020)
- [Mehrmann V, Unger B (2023) Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica 32:395–515. https://doi.org/10.1017/s096249292200008](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- Jacob, (2012)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Est�vez Schwarz D, Tischendorf C (2000) Structural analysis of electric circuits and consequences for MNA. Int J Circ Theor Appl 28(2):131–162. https://doi.org/10.1002/(sici)1097-007x(200003/04)28:2<131::aid-cta100>3.0.co;2- -- [10.1002/(sici)1097-007x(200003/04)28:2<131::aid-cta100>3.0.co;2-w](https://doi.org/10.1002/(sici)1097-007x(200003/04)28:2<131::aid-cta100>3.0.co;2-w)
- Günther, CAD-based electric-circuit modeling in industry. I. Mathematical structure and index of network equations. Surv. Math. Ind. (1999)
- Günther, CAD-based electric-circuit modeling in industry. II. Impact of circuit configurations and parameters. Surv. Math. Ind. (1999)
- Dänschel, Adaptive nonlinear optimization of district heating networks based on model and discretization catalogs. SeMA J. (2023)
- Mehrmann V, Schmidt M, Stolwijk JJ (2018) Model and Discretization Error Adaptivity Within Stationary Gas Transport Optimization. Vietnam J Math 46(4):779–801. https://doi.org/10.1007/s10013-018-0303- -- [10.1007/s10013-018-0303-1](https://doi.org/10.1007/s10013-018-0303-1)
- [Gugercin S, Polyuga RV, Beattie CA, van der Schaft AJ (2009) Interpolation-based &amp;#x210C;&lt;inf&gt;2&lt;/inf&gt; model reduction for port-Hamiltonian systems. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference 5362–536](interpolation-based-amp-x210c-lt-inf-gt-2-lt-inf-gt-model-reduction-for-port-hamiltonian-systems) -- [10.1109/cdc.2009.5400626](https://doi.org/10.1109/cdc.2009.5400626)
- [Gugercin S, Polyuga RV, Beattie C, van der Schaft A (2012) Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9):1963–1974. https://doi.org/10.1016/j.automatica.2012.05.05](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Polyuga RV, van der Schaft AJ (2012) Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Systems &amp; Control Letters 61(3):412–421. https://doi.org/10.1016/j.sysconle.2011.12.00](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- [Borja P, Scherpen JMA, Fujimoto K (2023) Extended Balancing of Continuous LTI Systems: A Structure-Preserving Approach. IEEE Trans Automat Contr 68(1):257–271. https://doi.org/10.1109/tac.2021.313864](extended-balancing-of-continuous-lti-systems-a-structure-preserving-approach) -- [10.1109/tac.2021.3138645](https://doi.org/10.1109/tac.2021.3138645)
- Hauschild, Model reduction techniques for linear constant coefficient port-Hamiltonian differential-algebraic systems. Control Cybern. (2019)
- Beattie, Structure-preserving interpolatory model reduction for port-Hamiltonian differential-algebraic systems. (2022)
- Desai U, Pal D (1984) A transformation approach to stochastic model reduction. IEEE Trans Automat Contr 29(12):1097–1100. https://doi.org/10.1109/tac.1984.110343 -- [10.1109/tac.1984.1103438](https://doi.org/10.1109/tac.1984.1103438)
- Reis T, Stykel T (2009) Positive real and bounded real balancing for model reduction of descriptor systems. International Journal of Control 83(1):74–88. https://doi.org/10.1080/0020717090310021 -- [10.1080/00207170903100214](https://doi.org/10.1080/00207170903100214)
- Mehrmann, Balanced truncation model reduction for large-scale system in descriptor form. (2005)
- [Breiten T, Unger B (2022) Passivity preserving model reduction via spectral factorization. Automatica 142:110368. https://doi.org/10.1016/j.automatica.2022.11036](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- [Beattie C, Mehrmann V, Xu H, Zwart H (2018) Linear port-Hamiltonian descriptor systems. Math Control Signals Syst 30(4). https://doi.org/10.1007/s00498-018-0223-](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- [Mehl C, Mehrmann V, Wojtylak M (2021) Distance problems for dissipative Hamiltonian systems and related matrix polynomials. Linear Algebra and its Applications 623:335–366. https://doi.org/10.1016/j.laa.2020.05.02](distance-problems-for-dissipative-hamiltonian-systems-and-related-matrix-polynomials) -- [10.1016/j.laa.2020.05.026](https://doi.org/10.1016/j.laa.2020.05.026)
- Benner, Model order reduction for differential-algebraic equations: A survey. (2017)
- Gugercin S, Stykel T, Wyatt S (2013) Model Reduction of Descriptor Systems by Interpolatory Projection Methods. SIAM J Sci Comput 35(5):B1010–B1033. https://doi.org/10.1137/13090663 -- [10.1137/130906635](https://doi.org/10.1137/130906635)
- [Mehl C, Mehrmann V, Wojtylak M (2018) Linear Algebra Properties of Dissipative Hamiltonian Descriptor Systems. SIAM J Matrix Anal &amp; Appl 39(3):1489–1519. https://doi.org/10.1137/18m116427](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18m1164275](https://doi.org/10.1137/18m1164275)
- [Moser T, Lohmann B (2020) A New Riemannian Framework for Efficient ℋ2-Optimal Model Reduction of Port-Hamiltonian Systems. 2020 59th IEEE Conference on Decision and Control (CDC) 5043–504](a-new-riemannian-framework-for-efficient-h-sub-2-sub-optimal-model-reduction-of-port-hamiltonian-systems) -- [10.1109/cdc42340.2020.9304134](https://doi.org/10.1109/cdc42340.2020.9304134)
- [Schwerdtner P, Voigt M (2023) SOBMOR: Structured Optimization-Based Model Order Reduction. SIAM J Sci Comput 45(2):A502–A529. https://doi.org/10.1137/20m138023](sobmor-structured-optimization-based-model-order-reduction) -- [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
- Stykel T (2004) Gramian-Based Model Reduction for Descriptor Systems. Mathematics of Control, Signals, and Systems (MCSS) 16(4):297–319. https://doi.org/10.1007/s00498-004-0141- -- [10.1007/s00498-004-0141-4](https://doi.org/10.1007/s00498-004-0141-4)
- Benner P, Werner SWR (2018) Model Reduction of Descriptor Systems with the MORLAB Toolbox ⁎ ⁎This work was supported by the DFG priority program 1897: “Calm, Smooth and Smart – Novel Approaches for Influencing Vibrations by Means of Deliberately Introduced Dissipation” and the DFG - 314838170, GRK 2297 MathCoRe. IFAC-PapersOnLine 51(2):547–552. https://doi.org/10.1016/j.ifacol.2018.03.09 -- [10.1016/j.ifacol.2018.03.092](https://doi.org/10.1016/j.ifacol.2018.03.092)
- Banagaaya N, Schilders WHA (2014) Index-Aware Model Order Reduction for Higher Index DAEs. Differential-Algebraic Equations Forum 155–18 -- [10.1007/978-3-662-44926-4_8](https://doi.org/10.1007/978-3-662-44926-4_8)
- Gugercin S, Antoulas AC, Beattie C (2008) $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM J Matrix Anal &amp; Appl 30(2):609–638. https://doi.org/10.1137/06066612 -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- Antoulas, (2020)
- Guiver C, Opmeer MR (2013) Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra and its Applications 439(12):3659–3698. https://doi.org/10.1016/j.laa.2013.09.03 -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- Cherifi, (2022)
- Achleitner, Hypocoercivity and controllability in linear semi-dissipative Hamiltonian ordinary differential equations and differential-algebraic equations. ZAMM J. Appl. Math. Mech. (2021)
- Güdücü, (2021)
- Anderson, (1973)
- Wohlers, (1969)
- Beattie, (2022)
- Antoulas, Data-driven model reduction for a class of semi-explicit DAEs using the loewner framework. (2020)
- Schwerdtner P, Mengi E, Voigt M (2020) Certifying Global Optimality for the L∞-Norm Computation of Large-Scale Descriptor Systems. IFAC-PapersOnLine 53(2):4279–4284. https://doi.org/10.1016/j.ifacol.2020.12.248 -- [10.1016/j.ifacol.2020.12.2482](https://doi.org/10.1016/j.ifacol.2020.12.2482)
- [Schwerdtner P, Voigt M (2021) Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine 54(19):143–148. https://doi.org/10.1016/j.ifacol.2021.11.06](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- Beattie CA, Gugercin S (2009) A trust region method for optimal H&lt;inf&gt;2&lt;/inf&gt; model reduction. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference 5370–537 -- [10.1109/cdc.2009.5400605](https://doi.org/10.1109/cdc.2009.5400605)
- Van Dooren P, Gallivan KA, Absil P-A (2010) $\mathcal{H}_2$-Optimal Model Reduction with Higher-Order Poles. SIAM J Matrix Anal &amp; Appl 31(5):2738–2753. https://doi.org/10.1137/08073159 -- [10.1137/080731591](https://doi.org/10.1137/080731591)
- [Sato K (2018) Riemannian optimal model reduction of linear port-Hamiltonian systems. Automatica 93:428–434. https://doi.org/10.1016/j.automatica.2018.03.05](riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
- Jiang, Model order reduction of port-Hamiltonian systems by Riemannian modified Fletcher–Reeves scheme. IEEE Trans. Circuits Syst. II Express Briefs (2019)
- van der Schaft, (2022)
- [Gillis N, Sharma P (2017) On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica 85:113–121. https://doi.org/10.1016/j.automatica.2017.07.04](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- [Hauschild S-A, Marheineke N, Mehrmann V (2019) Model reduction techniques for port‐Hamiltonian differential‐algebraic systems. Proc Appl Math and Mech 19(1). https://doi.org/10.1002/pamm.20190004](model-reduction-techniques-for-port-hamiltonian-differential-algebraic-systems) -- [10.1002/pamm.201900040](https://doi.org/10.1002/pamm.201900040)
- Freund, The SPRIM algorithm for structure-preserving order reduction of general RCL circuits. (2011)
- Trefethen LN (1981) Rational Chebyshev approximation on the unit disk. Numer Math 37(2):297–320. https://doi.org/10.1007/bf0139825 -- [10.1007/bf01398258](https://doi.org/10.1007/bf01398258)

