---
layout: post
title: "Improved a posteriori error bounds for reduced port-Hamiltonian systems"
date: 2024-09-11 00:00:00 +0100
permalink: improved-a-posteriori-error-bounds-for-reduced-port-hamiltonian-systems
year: 2024
authors: Johannes Rettberg, Dominik Wittwar, Patrick Buchfink, Robin Herkert, Jörg Fehr, Bernard Haasdonk
category: articles
tags:
  - Structure-preserving model order reduction
  - A posteriori error control
  - Port-Hamiltonian system
  - Fluid–structure interaction
  - 65L70
  - 34C20
---
 
## Authors
[Johannes Rettberg](authors/johannes-rettberg), [Dominik Wittwar](authors/dominik-wittwar), [Patrick Buchfink](authors/patrick-buchfink), [Robin Herkert](authors/robin-herkert), [Jörg Fehr](authors/jorg-fehr), [Bernard Haasdonk](authors/bernard-haasdonk)
 
## Abstract
Projection-based model order reduction of dynamical systems usually introduces an error between the high-fidelity model and its counterpart of lower dimension. This unknown error can be bounded by residual-based methods, which are typically known to be highly pessimistic in the sense of largely overestimating the true error. This work applies two improved error bounding techniques, namely (a)  a hierarchical error bound and (b)  an error bound based on an auxiliary linear problem , to the case of port-Hamiltonian systems. The approaches rely on a secondary approximation of (a) the dynamical system and (b) the error system. In this paper, these methods are adapted to port-Hamiltonian systems. The mathematical relationship between the two methods is discussed both theoretically and numerically. The effectiveness of the described methods is demonstrated using a challenging three-dimensional port-Hamiltonian model of a classical guitar with fluid–structure interaction.
 
## Keywords
Structure-preserving model order reduction; A posteriori error control; Port-Hamiltonian system; Fluid–structure interaction; 65L70; 34C20
 
## Citation
- **Journal:** Advances in Computational Mathematics
- **Year:** 2024
- **Volume:** 50
- **Issue:** 5
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10444-024-10195-8](https://doi.org/10.1007/s10444-024-10195-8)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Rettberg_2024,
  title={{Improved a posteriori error bounds for reduced port-Hamiltonian systems}},
  volume={50},
  ISSN={1572-9044},
  DOI={10.1007/s10444-024-10195-8},
  number={5},
  journal={Advances in Computational Mathematics},
  publisher={Springer Science and Business Media LLC},
  author={Rettberg, Johannes and Wittwar, Dominik and Buchfink, Patrick and Herkert, Robin and Fehr, Jörg and Haasdonk, Bernard},
  year={2024}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/improved-a-posteriori-error-bounds-for-reduced-port-hamiltonian-systems.bib)
 
## References
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [Rettberg, J. et al. Port-Hamiltonian fluid–structure interaction modelling and structure-preserving model order reduction of a classical guitar. Mathematical and Computer Modelling of Dynamical Systems vol. 29 116–148 (2023)](port-hamiltonian-fluid-structure-interaction-modelling-and-structure-preserving-model-order-reduction-of-a-classical-guitar) -- [10.1080/13873954.2023.2173238](https://doi.org/10.1080/13873954.2023.2173238)
- Haasdonk, B., Ohlberger, M.: Space-adaptive reduced basis simulation for time-dependent problems. In: MATHMOD, 6th Vienna International Conference on Mathematical Modelling, Vienna, Austria, pp. 718–723 (2009). https://www.argesim.org/fileadmin/user_upload_argesim/ARGESIM_Publications_OA/MATHMOD_Publications_OA/MATHMOD_2009_AR34_35/full_papers/184.pdf
- Haasdonk, B., Kleikamp, H., Ohlberger, M., Schindler, F. & Wenzel, T. A New Certified Hierarchical and Adaptive RB-ML-ROM Surrogate Model for Parametrized PDEs. SIAM Journal on Scientific Computing vol. 45 A1039–A1065 (2023) -- [10.1137/22m1493318](https://doi.org/10.1137/22m1493318)
- Haasdonk, B. & Ohlberger, M. Efficient reduced models anda posteriorierror estimation for parametrized dynamical systems by offline/online decomposition. Mathematical and Computer Modelling of Dynamical Systems vol. 17 145–161 (2011) -- [10.1080/13873954.2010.514703](https://doi.org/10.1080/13873954.2010.514703)
- Hain, S., Ohlberger, M., Radic, M. & Urban, K. A hierarchical a posteriori error estimator for the Reduced Basis Method. Advances in Computational Mathematics vol. 45 2191–2214 (2019) -- [10.1007/s10444-019-09675-z](https://doi.org/10.1007/s10444-019-09675-z)
- Schmidt, A., Wittwar, D. & Haasdonk, B. Rigorous and effective a-posteriori error bounds for nonlinear problems—application to RB methods. Advances in Computational Mathematics vol. 46 (2020) -- [10.1007/s10444-020-09741-x](https://doi.org/10.1007/s10444-020-09741-x)
- [Mehl, C., Mehrmann, V. & Wojtylak, M. Linear Algebra Properties of Dissipative Hamiltonian Descriptor Systems. SIAM Journal on Matrix Analysis and Applications vol. 39 1489–1519 (2018)](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18m1164275](https://doi.org/10.1137/18m1164275)
- Willems, J. C. Dissipative dynamical systems part I: General theory. Archive for Rational Mechanics and Analysis vol. 45 321–351 (1972) -- [10.1007/bf00276493](https://doi.org/10.1007/bf00276493)
- [Cherifi, K., Gernandt, H. & Hinsen, D. The difference between port-Hamiltonian, passive and positive real descriptor systems. Mathematics of Control, Signals, and Systems vol. 36 451–482 (2023)](the-difference-between-port-hamiltonian-passive-and-positive-real-descriptor-systems) -- [10.1007/s00498-023-00373-2](https://doi.org/10.1007/s00498-023-00373-2)
- [Beattie, C. A., Mehrmann, V. & Van Dooren, P. Robust port-Hamiltonian representations of passive systems. Automatica vol. 100 182–186 (2019)](robust-port-hamiltonian-representations-of-passive-systems) -- [10.1016/j.automatica.2018.11.013](https://doi.org/10.1016/j.automatica.2018.11.013)
- Hinrichsen, D. & Pritchard, A. J. Mathematical Systems Theory I. Texts in Applied Mathematics (Springer Berlin Heidelberg, 2005). doi:10.1007/b137541 -- [10.1007/b137541](https://doi.org/10.1007/b137541)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Gillis, N. & Sharma, P. Finding the Nearest Positive-Real System. SIAM Journal on Numerical Analysis vol. 56 1022–1047 (2018)](finding-the-nearest-positive-real-system) -- [10.1137/17m1137176](https://doi.org/10.1137/17m1137176)
- [Rashad, R., Califano, F., van der Schaft, A. J. & Stramigioli, S. Twenty years of distributed port-Hamiltonian systems: a literature review. IMA Journal of Mathematical Control and Information vol. 37 1400–1422 (2020)](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Goyal, P., Duff, I. P. & Benner, P. Guaranteed Stable Quadratic Models and their applications in SINDy and Operator Inference. Preprint at https://doi.org/10.48550/ARXIV.2308.13819 (2023) -- [10.48550/arxiv.2308.13819](https://doi.org/10.48550/arxiv.2308.13819)
- Gillis, N. & Sharma, P. On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica vol. 85 113–121 (2017) -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- DOI not foun -- [10.1002/nla.2153.e2153nla.2153](https://doi.org/10.1002/nla.2153.e2153nla.2153)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability Radii for Linear Hamiltonian Systems with Dissipation Under Structure-Preserving Perturbations. SIAM Journal on Matrix Analysis and Applications vol. 37 1625–1654 (2016)](stability-radii-for-linear-hamiltonian-systems-with-dissipation-under-structure-preserving-perturbations) -- [10.1137/16m1067330](https://doi.org/10.1137/16m1067330)
- [Mehl, C., Mehrmann, V. & Sharma, P. Stability radii for real linear Hamiltonian systems with perturbed dissipation. BIT Numerical Mathematics vol. 57 811–843 (2017)](stability-radii-for-real-linear-hamiltonian-systems-with-perturbed-dissipation) -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- Liljegren-Sailer, B.: On port-Hamiltonian modeling and structure-preserving model reduction. Doctoral thesis, Universität Trier (2020). https://nbn-resolving.org/urn:nbn:de:hbz:385-1-14498
- Beattie, C., Gugercin, S. & Mehrmann, V. Structure-Preserving Interpolatory Model Reduction for Port-Hamiltonian Differential-Algebraic Systems. Realization and Model Reduction of Dynamical Systems 235–254 (2022) doi:10.1007/978-3-030-95157-3_13 -- [10.1007/978-3-030-95157-3_13](https://doi.org/10.1007/978-3-030-95157-3_13)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Breiten, T. & Unger, B. Passivity preserving model reduction via spectral factorization. Automatica vol. 142 110368 (2022)](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- [Polyuga, R. V. & van der Schaft, A. Structure preserving model reduction of port-Hamiltonian systems by moment matching at infinity. Automatica vol. 46 665–672 (2010)](structure-preserving-model-reduction-of-port-hamiltonian-systems-by-moment-matching-at-infinity) -- [10.1016/j.automatica.2010.01.018](https://doi.org/10.1016/j.automatica.2010.01.018)
- [Ionescu, T. C. & Astolfi, A. Families of moment matching based, structure preserving approximations for linear port Hamiltonian systems. Automatica vol. 49 2424–2434 (2013)](families-of-moment-matching-based-structure-preserving-approximations-for-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.05.006](https://doi.org/10.1016/j.automatica.2013.05.006)
- [Egger, H., Kugler, T., Liljegren-Sailer, B., Marheineke, N. & Mehrmann, V. On Structure-Preserving Model Reduction for Damped Wave Propagation in Transport Networks. SIAM Journal on Scientific Computing vol. 40 A331–A365 (2018)](on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks) -- [10.1137/17m1125303](https://doi.org/10.1137/17m1125303)
- Moser, T. & Lohmann, B. A New Riemannian Framework for Efficient ℋ2-Optimal Model Reduction of Port-Hamiltonian Systems. 2020 59th IEEE Conference on Decision and Control (CDC) 5043–5049 (2020) doi:10.1109/cdc42340.2020.9304134 -- [10.1109/cdc42340.2020.9304134](https://doi.org/10.1109/cdc42340.2020.9304134)
- [Schwerdtner, P. & Voigt, M. SOBMOR: Structured Optimization-Based Model Order Reduction. SIAM Journal on Scientific Computing vol. 45 A502–A529 (2023)](sobmor-structured-optimization-based-model-order-reduction) -- [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
- [Polyuga, R. V. & van der Schaft, A. J. Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Systems &amp; Control Letters vol. 61 412–421 (2012)](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- Hauschild, S.-A., Marheineke, N. & Mehrmann, V. Model reduction techniques for linear constant coefficient port-Hamiltonian differential-algebraic systems. Preprint at https://doi.org/10.48550/ARXIV.1901.10242 (2019) -- [10.48550/arxiv.1901.10242](https://doi.org/10.48550/arxiv.1901.10242)
- Guiver, C. & Opmeer, M. R. Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra and its Applications vol. 439 3659–3698 (2013) -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- [Breiten, T., Morandin, R. & Schulze, P. Error bounds for port-Hamiltonian model and controller reduction based on system balancing. Computers &amp; Mathematics with Applications vol. 116 100–115 (2022)](error-bounds-for-port-hamiltonian-model-and-controller-reduction-based-on-system-balancing) -- [10.1016/j.camwa.2021.07.022](https://doi.org/10.1016/j.camwa.2021.07.022)
- [Borja, P., Scherpen, J. M. A. & Fujimoto, K. Extended Balancing of Continuous LTI Systems: A Structure-Preserving Approach. IEEE Transactions on Automatic Control vol. 68 257–271 (2023)](extended-balancing-of-continuous-lti-systems-a-structure-preserving-approach) -- [10.1109/tac.2021.3138645](https://doi.org/10.1109/tac.2021.3138645)
- [Schulze, P. & Unger, B. Model Reduction for Linear Systems with Low-Rank Switching. SIAM Journal on Control and Optimization vol. 56 4365–4384 (2018)](model-reduction-for-linear-systems-with-low-rank-switching) -- [10.1137/18m1167887](https://doi.org/10.1137/18m1167887)
- Schulze, P. Energy-based model reduction of transport-dominated phenomena. Technische Universität Berlin (2023) doi:10.14279/DEPOSITONCE-17843 -- [10.14279/depositonce-17843](https://doi.org/10.14279/depositonce-17843)
- Beattie, C. & Gugercin, S. Structure-preserving model reduction for nonlinear port-Hamiltonian systems. IEEE Conference on Decision and Control and European Control Conference 6564–6569 (2011) doi:10.1109/cdc.2011.6161504 -- [10.1109/cdc.2011.6161504](https://doi.org/10.1109/cdc.2011.6161504)
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- [Wolf, T., Lohmann, B., Eid, R. & Kotyczka, P. Passivity and Structure Preserving Order Reduction of Linear Port-Hamiltonian Systems Using Krylov Subspaces. European Journal of Control vol. 16 401–406 (2010)](passivity-and-structure-preserving-order-reduction-of-linear-port-hamiltonian-systems-using-krylov-subspaces) -- [10.3166/ejc.16.401-406](https://doi.org/10.3166/ejc.16.401-406)
- Ngoc Cuong, N., Veroy, K. & Patera, A. T. Certified Real-Time Solution of Parametrized Partial Differential Equations. Handbook of Materials Modeling 1529–1564 (2005) doi:10.1007/978-1-4020-3286-8_76 -- [10.1007/978-1-4020-3286-8_76](https://doi.org/10.1007/978-1-4020-3286-8_76)
- Veroy, K. & Patera, A. T. Certified real‐time solution of the parametrized steady incompressible Navier–Stokes equations: rigorous reduced‐basis a posteriori error bounds. International Journal for Numerical Methods in Fluids vol. 47 773–788 (2005) -- [10.1002/fld.867](https://doi.org/10.1002/fld.867)
- Grepl, M. A. & Patera, A. T. A posteriorierror bounds for reduced-basis approximations of parametrized parabolic partial differential equations. ESAIM: Mathematical Modelling and Numerical Analysis vol. 39 157–181 (2005) -- [10.1051/m2an:2005006](https://doi.org/10.1051/m2an:2005006)
- KNEZEVIC, D. J., NGUYEN, N.-C. & PATERA, A. T. REDUCED BASIS APPROXIMATION AND A POSTERIORI ERROR ESTIMATION FOR THE PARAMETRIZED UNSTEADY BOUSSINESQ EQUATIONS. Mathematical Models and Methods in Applied Sciences vol. 21 1415–1442 (2011) -- [10.1142/s0218202511005441](https://doi.org/10.1142/s0218202511005441)
- Grepl, M. A., Maday, Y., Nguyen, N. C. & Patera, A. T. Efficient reduced-basis treatment of nonaffine and nonlinear partial differential equations. ESAIM: Mathematical Modelling and Numerical Analysis vol. 41 575–605 (2007) -- [10.1051/m2an:2007031](https://doi.org/10.1051/m2an:2007031)
- Grunert, D., Fehr, J. & Haasdonk, B. Well‐scaled, a‐posteriori error estimation for model order reduction of large second‐order mechanical systems. ZAMM - Journal of Applied Mathematics and Mechanics / Zeitschrift für Angewandte Mathematik und Mechanik vol. 100 (2020) -- [10.1002/zamm.201900186](https://doi.org/10.1002/zamm.201900186)
- Glas, S., Patera, A. T. & Urban, K. A reduced basis method for the wave equation. International Journal of Computational Fluid Dynamics vol. 34 139–146 (2019) -- [10.1080/10618562.2019.1686486](https://doi.org/10.1080/10618562.2019.1686486)
- Stahl, N., Liljegren-Sailer, B. & Marheineke, N. Certified Reduced Basis Method for the Damped Wave Equations on Networks. IFAC-PapersOnLine vol. 55 289–294 (2022) -- [10.1016/j.ifacol.2022.09.110](https://doi.org/10.1016/j.ifacol.2022.09.110)
- Antoulas, A. C., Benner, P. & Feng, L. Model reduction by iterative error system approximation. Mathematical and Computer Modelling of Dynamical Systems vol. 24 103–118 (2018) -- [10.1080/13873954.2018.1427116](https://doi.org/10.1080/13873954.2018.1427116)
- Feng, L., Lombardi, L., Antonini, G. & Benner, P. Multi‐fidelity error estimation accelerates greedy model reduction of complex dynamical systems. International Journal for Numerical Methods in Engineering vol. 124 5312–5333 (2023) -- [10.1002/nme.7348](https://doi.org/10.1002/nme.7348)
- Güttel, S. & Nakatsukasa, Y. Scaled and Squared Subdiagonal Padé Approximation for the Matrix Exponential. SIAM Journal on Matrix Analysis and Applications vol. 37 145–170 (2016) -- [10.1137/15m1027553](https://doi.org/10.1137/15m1027553)
- Söderlind, G. The logarithmic norm. History and modern theory. BIT Numerical Mathematics vol. 46 631–652 (2006) -- [10.1007/s10543-006-0069-9](https://doi.org/10.1007/s10543-006-0069-9)
- Desoer, C. A. & Vidyasagar, M. Feedback Systems. (2009) doi:10.1137/1.9780898719055 -- [10.1137/1.9780898719055](https://doi.org/10.1137/1.9780898719055)
- Wittwar, D. Approximation with matrix-valued kernels and highly effective error estimators for reduced basis approximations. Preprint at https://doi.org/10.18419/OPUS-12526 (2022) -- [10.18419/opus-12526](https://doi.org/10.18419/opus-12526)
- Hackbusch, W. Hierarchical Matrices: Algorithms and Analysis. Springer Series in Computational Mathematics (Springer Berlin Heidelberg, 2015). doi:10.1007/978-3-662-47324-5 -- [10.1007/978-3-662-47324-5](https://doi.org/10.1007/978-3-662-47324-5)
- Gugercin, S. & Antoulas, A. C. A Survey of Model Reduction by Balanced Truncation and Some New Results. International Journal of Control vol. 77 748–766 (2004) -- [10.1080/00207170410001713448](https://doi.org/10.1080/00207170410001713448)
- Rettberg, J. et al. Replication Data for: Port-Hamiltonian Fluid-Structure Interaction Modeling and Structure-Preserving Model Order Reduction of a Classical Guitar. DaRUS https://doi.org/10.18419/DARUS-3248 (2023) -- [10.18419/darus-3248](https://doi.org/10.18419/darus-3248)
- Rettberg, J., Wittwar, D. & Herkert, R. Softwarepackage CCMOR2. DaRUS https://doi.org/10.18419/DARUS-3839 (2023) -- [10.18419/darus-3839](https://doi.org/10.18419/darus-3839)
- Peng, L. & Mohseni, K. Symplectic Model Reduction of Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 A1–A27 (2016) -- [10.1137/140978922](https://doi.org/10.1137/140978922)
- Buchfink, P., Bhatt, A. & Haasdonk, B. Symplectic Model Order Reduction with Non-Orthonormal Bases. Mathematical and Computational Applications vol. 24 43 (2019) -- [10.3390/mca24020043](https://doi.org/10.3390/mca24020043)
- Chellappa, S., Feng, L., de la Rubia, V. & Benner, P. Inf-Sup-Constant-Free State Error Estimator for Model Order Reduction of Parametric Systems in Electromagnetics. IEEE Transactions on Microwave Theory and Techniques vol. 71 4762–4777 (2023) -- [10.1109/tmtt.2023.3288642](https://doi.org/10.1109/tmtt.2023.3288642)
- Buchfink, P., Haasdonk, B., Rave, S.: PSD-Greedy basis generation for structure-preserving model order reduction of Hamiltonian systems. In: Frolkovič, P., Mikula, K., Ševčovič, D. (eds.) Proceedings of the Conference Algoritmy 2020, pp. 151–160. Vydavateľstvo SPEKTRUM, Vysoke Tatry, Podbanske (2020). http://www.iam.fmph.uniba.sk/amuc/ojs/index.php/algoritmy/article/view/1577/829

