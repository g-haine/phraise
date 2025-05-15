---
layout: post
title: "Model Reduction for Linear Systems with Low-Rank Switching"
date: 2018-12-11 00:00:00 +0100
permalink: model-reduction-for-linear-systems-with-low-rank-switching
year: 2018
authors: Philipp Schulze, Benjamin Unger
category: articles
---
 
## Authors
[Philipp Schulze](authors/philipp-schulze), [Benjamin Unger](authors/benjamin-unger)
 
## Abstract
We introduce a novel model order reduction (MOR) method for large-scale linear switched systems (LSS) where the coefficient matrices are affected by a low-rank switching. The key idea is to replace the LSS by a nonswitched system with extended input and output vectors---called the envelope system---which is able to reproduce the dynamical behavior of the original LSS by applying a certain feedback law. The envelope system can be reduced using standard MOR schemes and then transformed back into an LSS. Furthermore, we present an upper bound for the output error of the reduced-order LSS and show how to preserve quadratic Lyapunov stability. The approach is tested by means of a numerical example demonstrating the efficacy of the presented method.
 
## Citation
- **Journal:** SIAM Journal on Control and Optimization
- **Year:** 2018
- **Volume:** 56
- **Issue:** 6
- **Pages:** 4365--4384
- **Publisher:** Society for Industrial & Applied Mathematics (SIAM)
- **DOI:** [10.1137/18m1167887](https://doi.org/10.1137/18m1167887)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Schulze_2018,
  title={{Model Reduction for Linear Systems with Low-Rank Switching}},
  volume={56},
  ISSN={1095-7138},
  DOI={10.1137/18m1167887},
  number={6},
  journal={SIAM Journal on Control and Optimization},
  publisher={Society for Industrial & Applied Mathematics (SIAM)},
  author={Schulze, Philipp and Unger, Benjamin},
  year={2018},
  pages={4365--4384}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/model-reduction-for-linear-systems-with-low-rank-switching.bib)
 
## References
- Antoulas A. C., New York (2010)
- Astolfi, A. Model Reduction by Moment Matching for Linear and Nonlinear Systems. IEEE Transactions on Automatic Control vol. 55 2321–2336 (2010) -- [10.1109/tac.2010.2046044](https://doi.org/10.1109/tac.2010.2046044)
- Baştuğ M., OR (2014)
- Bastug, M., Petreczky, M., Wisniewski, R. & Leth, J. Model Reduction by Nice Selections for Linear Switched Systems. IEEE Transactions on Automatic Control vol. 61 3422–3437 (2016) -- [10.1109/tac.2016.2518023](https://doi.org/10.1109/tac.2016.2518023)
- Balluchi, A., Benvenuti, L., di Benedetto, M. D., Pinello, C. & Sangiovanni-Vincentelli, A. L. Automotive engine control and hybrid systems: challenges and opportunities. Proceedings of the IEEE vol. 88 888–912 (2000) -- [10.1109/5.871300](https://doi.org/10.1109/5.871300)
- Baur, U., Beattie, C. & Benner, P. Mapping parameters across system boundaries: parameterized model reduction with low rank variability in dynamics. PAMM vol. 14 19–22 (2014) -- [10.1002/pamm.201410006](https://doi.org/10.1002/pamm.201410006)
- Baur, U., Benner, P. & Feng, L. Model Order Reduction for Linear and Nonlinear Systems: A System-Theoretic Perspective. Archives of Computational Methods in Engineering vol. 21 331–358 (2014) -- [10.1007/s11831-014-9111-2](https://doi.org/10.1007/s11831-014-9111-2)
- Beattie, C. & Gugercin, S. Interpolatory projection methods for structure-preserving model reduction. Systems &amp; Control Letters vol. 58 225–232 (2009) -- [10.1016/j.sysconle.2008.10.016](https://doi.org/10.1016/j.sysconle.2008.10.016)
- Beattie, C., Gugercin, S. & Mehrmann, V. Model reduction for systems with inhomogeneous initial conditions. Systems &amp; Control Letters vol. 99 99–106 (2017) -- [10.1016/j.sysconle.2016.11.007](https://doi.org/10.1016/j.sysconle.2016.11.007)
- Berry M. W., Int. J. High Performance Comput. Appl. (1992)
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- Freund R. W., Berlin (2008)
- [Gillis, N. & Sharma, P. On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica vol. 85 113–121 (2017)](on-computing-the-distance-to-stability-for-matrices-using-linear-dissipative-hamiltonian-systems) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- Gugercin, S., Antoulas, A. C. & Beattie, C. $\mathcal{H}_2$ Model Reduction for Large-Scale Linear Dynamical Systems. SIAM Journal on Matrix Analysis and Applications vol. 30 609–638 (2008) -- [10.1137/060666123](https://doi.org/10.1137/060666123)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Heinkenschloss, M., Reis, T. & Antoulas, A. C. Balanced truncation model reduction for systems with inhomogeneous initial conditions. Automatica vol. 47 559–564 (2011) -- [10.1016/j.automatica.2010.12.002](https://doi.org/10.1016/j.automatica.2010.12.002)
- Hinze M., Berlin (2005)
- Jarlebring, E., Damm, T. & Michiels, W. Model reduction of time-delay systems using position balancing and delay Lyapunov equations. Mathematics of Control, Signals, and Systems vol. 25 147–166 (2012) -- [10.1007/s00498-012-0096-9](https://doi.org/10.1007/s00498-012-0096-9)
- Lall, S., Krysl, P. & Marsden, J. E. Structure-preserving model reduction for mechanical systems. Physica D: Nonlinear Phenomena vol. 184 304–318 (2003) -- [10.1016/s0167-2789(03)00227-6](https://doi.org/10.1016/s0167-2789(03)00227-6)
- Lee J., China (2003)
- Mazzi E., Mexico (2008)
- Moore, B. Principal component analysis in linear systems: Controllability, observability, and model reduction. IEEE Transactions on Automatic Control vol. 26 17–32 (1981) -- [10.1109/tac.1981.1102568](https://doi.org/10.1109/tac.1981.1102568)
- Mullis, C. & Roberts, R. Synthesis of minimum roundoff noise fixed point digital filters. IEEE Transactions on Circuits and Systems vol. 23 551–562 (1976) -- [10.1109/tcs.1976.1084254](https://doi.org/10.1109/tcs.1976.1084254)
- Ohlberger M., Slovakia (2016)
- Papadopoulos A. V., Berlin (2014)
- Papadopoulos, A. V. & Prandini, M. Model reduction of switched affine systems. Automatica vol. 70 57–65 (2016) -- [10.1016/j.automatica.2016.03.019](https://doi.org/10.1016/j.automatica.2016.03.019)
- Pepyne, D. L. & Cassandras, C. G. Optimal control of hybrid systems in manufacturing. Proceedings of the IEEE vol. 88 1108–1123 (2000) -- [10.1109/5.871312](https://doi.org/10.1109/5.871312)
- Petreczky, M. Realization theory for linear and bilinear switched systems: A formal power series approach. ESAIM: Control, Optimisation and Calculus of Variations vol. 17 410–445 (2010) -- [10.1051/cocv/2010014](https://doi.org/10.1051/cocv/2010014)
- Petreczky, M., Wisniewski, R. & Leth, J. Balanced truncation for linear switched systems. Nonlinear Analysis: Hybrid Systems vol. 10 4–20 (2013) -- [10.1016/j.nahs.2013.03.007](https://doi.org/10.1016/j.nahs.2013.03.007)
- Scarciotti, G. & Astolfi, A. Model reduction for hybrid systems with state-dependent jumps. IFAC-PapersOnLine vol. 49 850–855 (2016) -- [10.1016/j.ifacol.2016.10.272](https://doi.org/10.1016/j.ifacol.2016.10.272)
- Schulze, P., Unger, B., Beattie, C. & Gugercin, S. Data-driven structured realization. Linear Algebra and its Applications vol. 537 250–286 (2018) -- [10.1016/j.laa.2017.09.030](https://doi.org/10.1016/j.laa.2017.09.030)
- Shaker H. R., Hungary (2009)
- Shaker H. R., Int. J. Innov. Comput. Inform. Control (2012)
- Sun, Z., Ge, S. S. & Lee, T. H. Controllability and reachability criteria for switched linear systems. Automatica vol. 38 775–786 (2002) -- [10.1016/s0005-1098(01)00267-9](https://doi.org/10.1016/s0005-1098(01)00267-9)
- van de Wouw, N., Michiels, W. & Besselink, B. Model reduction for delay differential equations with guaranteed stability and error bound. Automatica vol. 55 132–139 (2015) -- [10.1016/j.automatica.2015.02.031](https://doi.org/10.1016/j.automatica.2015.02.031)
- Volkwein, S. Optimal Control of a Phase-Field Model Using Proper Orthogonal Decomposition. ZAMM vol. 81 83–97 (2001) -- [10.1002/1521-4001(200102)81:2<83::aid-zamm83>3.0.co;2-r](https://doi.org/10.1002/1521-4001(200102)81:2<83::aid-zamm83>3.0.co;2-r)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control vol. 16 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)

