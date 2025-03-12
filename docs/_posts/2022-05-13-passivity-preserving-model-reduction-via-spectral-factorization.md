---
layout: post
title: "Passivity preserving model reduction via spectral factorization"
date: 2022-05-13 00:00:00 +0100
permalink: passivity-preserving-model-reduction-via-spectral-factorization
year: 2022
authors: Tobias Breiten, Benjamin Unger
category: articles
tags:
  - Port-Hamiltonian systems
  - Structure-preserving model-order reduction
  - Passivity
  - Spectral factorization
  - \\( H^2 \\)-optimal
---
 
## Authors
[Tobias Breiten](authors/tobias-breiten), [Benjamin Unger](authors/benjamin-unger)
 
## Abstract
We present a novel model-order reduction (MOR) method for linear time-invariant systems that preserves passivity and is thus suited for structure-preserving MOR for port-Hamiltonian (pH) systems. Our algorithm exploits the well-known spectral factorization of the Popov function by a solution of the Kalman–Yakubovich–Popov (KYP) inequality. It performs MOR directly on the spectral factor inheriting the original system’s sparsity enabling MOR in a large-scale context. Our analysis reveals that the spectral factorization corresponding to the minimal solution of an associated algebraic Riccati equation is preferable from a model reduction perspective and benefits pH-preserving MOR methods such as a modified version of the iterative rational Krylov algorithm (IRKA). Numerical examples demonstrate that our approach can produce high-fidelity reduced-order models close to (unstructured) H 2 -optimal reduced-order models.
 
## Keywords
Port-Hamiltonian systems; Structure-preserving model-order reduction; Passivity; Spectral factorization; \\( H^2 \\)-optimal
 
## Citation
- **Journal:** Automatica
- **Year:** 2022
- **Volume:** 142
- **Issue:** 
- **Pages:** 110368
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Breiten_2022,
  title={{Passivity preserving model reduction via spectral factorization}},
  volume={142},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2022.110368},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Breiten, Tobias and Unger, Benjamin},
  year={2022},
  pages={110368}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/passivity-preserving-model-reduction-via-spectral-factorization.bib)
 
## References
- [Altmann, R., Mehrmann, V. & Unger, B. Port-Hamiltonian formulations of poroelastic network models. Mathematical and Computer Modelling of Dynamical Systems vol. 27 429–452 (2021)](port-hamiltonian-formulations-of-poroelastic-network-models) -- [10.1080/13873954.2021.1975137](https://doi.org/10.1080/13873954.2021.1975137)
- Anderson, (1973)
- Antoulas, (2005)
- Antoulas, A. C. A new result on passivity preserving model reduction. Systems &amp; Control Letters vol. 54 361–374 (2005) -- [10.1016/j.sysconle.2004.07.007](https://doi.org/10.1016/j.sysconle.2004.07.007)
- Antoulas, (2020)
- Antoulas, Chapter 8: A tutorial introduction to the loewner framework for model reduction. (2017)
- Beattie, Chapter 7: Model reduction by rational interpolation. (2017)
- [Beattie, C. A., Mehrmann, V. & Van Dooren, P. Robust port-Hamiltonian representations of passive systems. Automatica vol. 100 182–186 (2019)](robust-port-hamiltonian-representations-of-passive-systems) -- [10.1016/j.automatica.2018.11.013](https://doi.org/10.1016/j.automatica.2018.11.013)
- Beattie, Port-Hamiltonian descriptor systems. Mathematics of Control, Signals and Systems (2018)
- [Benner, P., Goyal, P. & Van Dooren, P. Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters vol. 143 104741 (2020)](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- Benner, P. & Saak, J. Numerical solution of large and sparse continuous time algebraic matrix Riccati and Lyapunov equations: a state of the art survey. GAMM-Mitteilungen vol. 36 32–52 (2013) -- [10.1002/gamm.201310003](https://doi.org/10.1002/gamm.201310003)
- Biot, M. A. General Theory of Three-Dimensional Consolidation. Journal of Applied Physics vol. 12 155–164 (1941) -- [10.1063/1.1712886](https://doi.org/10.1063/1.1712886)
- Black, F., Schulze, P. & Unger, B. Projection-based model reduction with dynamically transformed modes. ESAIM: Mathematical Modelling and Numerical Analysis vol. 54 2011–2043 (2020) -- [10.1051/m2an/2020046](https://doi.org/10.1051/m2an/2020046)
- Breiten, Error bounds for port-Hamiltonian model and controller reduction based on system balancing. Computers & Mathematics with Applications (2021)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A partitioned finite element method for power-preserving discretization of open systems of conservation laws. IMA Journal of Mathematical Control and Information vol. 38 493–533 (2020)](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Cherifi, (2019)
- Curtain, (1995)
- Desai, U. & Pal, D. A transformation approach to stochastic model reduction. IEEE Transactions on Automatic Control vol. 29 1097–1100 (1984) -- [10.1109/tac.1984.1103438](https://doi.org/10.1109/tac.1984.1103438)
- (2009)
- [Egger, H. Structure preserving approximation of dissipative evolution problems. Numerische Mathematik vol. 143 85–106 (2019)](structure-preserving-approximation-of-dissipative-evolution-problems) -- [10.1007/s00211-019-01050-w](https://doi.org/10.1007/s00211-019-01050-w)
- [Egger, H., Kugler, T., Liljegren-Sailer, B., Marheineke, N. & Mehrmann, V. On Structure-Preserving Model Reduction for Damped Wave Propagation in Transport Networks. SIAM Journal on Scientific Computing vol. 40 A331–A365 (2018)](on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks) -- [10.1137/17m1125303](https://doi.org/10.1137/17m1125303)
- Golub, (1996)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Transactions on Circuits and Systems I: Regular Papers vol. 51 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Gugercin, S. & Antoulas, A. C. A Survey of Model Reduction by Balanced Truncation and Some New Results. International Journal of Control vol. 77 748–766 (2004) -- [10.1080/00207170410001713448](https://doi.org/10.1080/00207170410001713448)
- Gugercin, S., Antoulas, A. C. & Beattie, C. $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM Journal on Matrix Analysis and Applications vol. 30 609–638 (2008) -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Guiver, C. & Opmeer, M. R. Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra and its Applications vol. 439 3659–3698 (2013) -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- Harshavardhana, P., Jonckheere, E. & Silverman, L. Stochastic balancing and approximation-stability and minimality. IEEE Transactions on Automatic Control vol. 29 744–746 (1984) -- [10.1109/tac.1984.1103631](https://doi.org/10.1109/tac.1984.1103631)
- [Ionescu, T. C. & Astolfi, A. Families of moment matching based, structure preserving approximations for linear port Hamiltonian systems. Automatica vol. 49 2424–2434 (2013)](families-of-moment-matching-based-structure-preserving-approximations-for-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.05.006](https://doi.org/10.1016/j.automatica.2013.05.006)
- Jacob, (2012)
- Massoudi, A., Opmeer, M. R. & Reis, T. The ADI method for bounded real and positive real Lur’e equations. Numerische Mathematik vol. 135 431–458 (2016) -- [10.1007/s00211-016-0805-2](https://doi.org/10.1007/s00211-016-0805-2)
- Mayo, A. J. & Antoulas, A. C. A framework for the solution of the generalized realization problem. Linear Algebra and its Applications vol. 425 634–662 (2007) -- [10.1016/j.laa.2007.03.008](https://doi.org/10.1016/j.laa.2007.03.008)
- Mehrmann, (2022)
- Meier, L. & Luenberger, D. Approximation of linear constant systems. IEEE Transactions on Automatic Control vol. 12 585–588 (1967) -- [10.1109/tac.1967.1098680](https://doi.org/10.1109/tac.1967.1098680)
- Moser, A new Riemannian framework for efficient H2-optimal model reduction of port-Hamiltonian systems. (2020)
- Poloni, F. & Reis, T. A Deflation Approach for Large-Scale Lur’e Equations. SIAM Journal on Matrix Analysis and Applications vol. 33 1339–1368 (2012) -- [10.1137/120861679](https://doi.org/10.1137/120861679)
- Polyuga, (2010)
- [Polyuga, R. V. & van der Schaft, A. Structure preserving model reduction of port-Hamiltonian systems by moment matching at infinity. Automatica vol. 46 665–672 (2010)](structure-preserving-model-reduction-of-port-hamiltonian-systems-by-moment-matching-at-infinity) -- [10.1016/j.automatica.2010.01.018](https://doi.org/10.1016/j.automatica.2010.01.018)
- [Polyuga, R. V. & van der Schaft, A. Structure Preserving Moment Matching for Port-Hamiltonian Systems: Arnoldi and Lanczos. IEEE Transactions on Automatic Control vol. 56 1458–1462 (2011)](structure-preserving-moment-matching-for-port-hamiltonian-systems-arnoldi-and-lanczos) -- [10.1109/tac.2011.2128650](https://doi.org/10.1109/tac.2011.2128650)
- Reis, T. Lur’e equations and even matrix pencils. Linear Algebra and its Applications vol. 434 152–173 (2011) -- [10.1016/j.laa.2010.09.005](https://doi.org/10.1016/j.laa.2010.09.005)
- Reis, T. & Stykel, T. Positive real and bounded real balancing for model reduction of descriptor systems. International Journal of Control vol. 83 74–88 (2009) -- [10.1080/00207170903100214](https://doi.org/10.1080/00207170903100214)
- [Sato, K. Riemannian optimal model reduction of linear port-Hamiltonian systems. Automatica vol. 93 428–434 (2018)](riemannian-optimal-model-reduction-of-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.03.051](https://doi.org/10.1016/j.automatica.2018.03.051)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Schwerdtner, (2020)
- Simoncini, V. Computational Methods for Linear Matrix Equations. SIAM Review vol. 58 377–441 (2016) -- [10.1137/130912839](https://doi.org/10.1137/130912839)
- Sorensen, D. C. Passivity preserving model reduction via interpolation of spectral zeros. Systems &amp; Control Letters vol. 54 347–360 (2005) -- [10.1016/j.sysconle.2004.07.006](https://doi.org/10.1016/j.sysconle.2004.07.006)
- Unger, B. & Gugercin, S. Kolmogorov n-widths for linear dynamical systems. Advances in Computational Mathematics vol. 45 2273–2286 (2019) -- [10.1007/s10444-019-09701-0](https://doi.org/10.1007/s10444-019-09701-0)
- Willems, J. Least squares stationary optimal control and the algebraic Riccati equation. IEEE Transactions on Automatic Control vol. 16 621–634 (1971) -- [10.1109/tac.1971.1099831](https://doi.org/10.1109/tac.1971.1099831)
- Willems, J. C. Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Archive for Rational Mechanics and Analysis vol. 45 352–393 (1972) -- [10.1007/bf00276494](https://doi.org/10.1007/bf00276494)
- Wilson, D. A. Optimum solution of model-reduction problem. Proceedings of the Institution of Electrical Engineers vol. 117 1161 (1970) -- [10.1049/piee.1970.0227](https://doi.org/10.1049/piee.1970.0227)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control vol. 16 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)
- [Wu, Y., Hamroun, B., Le Gorrec, Y. & Maschke, B. Reduced order LQG control design for port Hamiltonian systems. Automatica vol. 95 86–92 (2018)](reduced-order-lqg-control-design-for-port-hamiltonian-systems) -- [10.1016/j.automatica.2018.05.003](https://doi.org/10.1016/j.automatica.2018.05.003)
- Zhou, (1996)

