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
 
## References
- [Mehrmann, V., Unger, B.: Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numer 32, 395–515 (2023). https://doi.org/10.1017/S0962492922000083](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/S0962492922000083](https://doi.org/10.1017/S0962492922000083)
- [Duindam, V., Macchelli, A., Stramigioli, S., Bruyninckx, H.: Modeling and control of complex physical systems - the port-Hamiltonian approach., 1st edn. Springer, Berlin Heidelberg (2009). https://doi.org/10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [Rettberg, J., Wittwar, D., Buchfink, P., Brauchler, A., Ziegler, P., Fehr, J., Haasdonk, B.: Port-Hamiltonian fluid-structure interaction modeling and structure-preserving model order reduction of a classical guitar. Math. Comput. Model. Dyn. Syst. (2023). https://doi.org/10.1080/13873954.2023.2173238](port-hamiltonian-fluid-structure-interaction-modelling-and-structure-preserving-model-order-reduction-of-a-classical-guitar) -- [10.1080/13873954.2023.2173238](https://doi.org/10.1080/13873954.2023.2173238)
- Haasdonk, B., Ohlberger, M.: Space-adaptive reduced basis simulation for time-dependent problems. In: MATHMOD, 6th Vienna International Conference on Mathematical Modelling, Vienna, Austria, pp. 718–723 (2009). https://www.argesim.org/fileadmin/user_upload_argesim/ARGESIM_Publications_OA/MATHMOD_Publications_OA/MATHMOD_2009_AR34_35/full_papers/184.pdf
- Haasdonk, B., Kleikamp, H., Ohlberger, M., Schindler, F., Wenzel, T.: A new certified hierarchical and adaptive RB-ML-ROM surrogate model for parametrized PDEs. SIAM J. Sci. Comput. 45(3), 1039–1065 (2023). https://doi.org/10.1137/22M1493318 -- [10.1137/22M1493318](https://doi.org/10.1137/22M1493318)
- Haasdonk, B., Ohlberger, M.: Efficient reduced models and a posteriori error estimation for parametrized dynamical systems by offline/online decomposition. MCMDS 17(2), 145–161 (2011). https://doi.org/10.1080/13873954.2010.514703 -- [10.1080/13873954.2010.514703](https://doi.org/10.1080/13873954.2010.514703)
- Hain, S., Ohlberger, M., Radic, M., Urban, K.: A hierarchical a posteriori error estimator for the reduced basis method. Adv. Comput. Math. 45(5), 2191–2214 (2019). https://doi.org/10.1007/s10444-019-09675-z -- [10.1007/s10444-019-09675-z](https://doi.org/10.1007/s10444-019-09675-z)
- Schmidt, A., Wittwar, D., Haasdonk, B.: Rigorous and effective a-posteriori error bounds for nonlinear problems-application to RB methods. Adv. Comput. Math. 46(2), 32 (2020). https://doi.org/10.1007/s10444-020-09741-x -- [10.1007/s10444-020-09741-x](https://doi.org/10.1007/s10444-020-09741-x)
- [Mehl, C., Mehrmann, V., Wojtylak, M.: Linear algebra properties of dissipative Hamiltonian descriptor systems. SIAM J. Matrix Anal. Appl. 39(3), 1489–1519 (2018). https://doi.org/10.1137/18M1164275](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18M1164275](https://doi.org/10.1137/18M1164275)
- Willems, J.C.: Dissipative dynamical systems part i: General theory. Arch. Ration. Mech. Anal. 45(5), 321–351 (1972). https://doi.org/10.1007/BF00276493 -- [10.1007/BF00276493](https://doi.org/10.1007/BF00276493)
- [Cherifi, K., Gernandt, H., Hinsen, D.: The difference between port-Hamiltonian, passive and positive real descriptor systems. Mathematics of Control, Signals, and Systems (2023). https://doi.org/10.1007/s00498-023-00373-2](the-difference-between-port-hamiltonian-passive-and-positive-real-descriptor-systems) -- [10.1007/s00498-023-00373-2](https://doi.org/10.1007/s00498-023-00373-2)
- [Beattie, C.A., Mehrmann, V., Van Dooren, P.: Robust port-Hamiltonian representations of passive systems. Automatica 100, 182–186 (2019). https://doi.org/10.1016/j.automatica.2018.11.013](robust-port-hamiltonian-representations-of-passive-systems) -- [10.1016/j.automatica.2018.11.013](https://doi.org/10.1016/j.automatica.2018.11.013)
- Hinrichsen, D., Pritchard, A.J.: Mathematical Systems Theory I. Springer, Berlin Heidelberg (2005). https://doi.org/10.1007/b137541 -- [10.1007/b137541](https://doi.org/10.1007/b137541)
- [van der Schaft, A., Jeltsema, D.: Port-Hamiltonian systems theory: an introductory overview. Fndn Trends in Syst Contr 1(2–3), 173–378 (2014). https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Gillis, N., Sharma, P.: Finding the nearest positive-real system. SIAM J. Numer. Anal. 56(2), 1022–1047 (2018). https://doi.org/10.1137/17M1137176](finding-the-nearest-positive-real-system) -- [10.1137/17M1137176](https://doi.org/10.1137/17M1137176)
- [Rashad, R., Califano, F., van der Schaft, A., Stramigioli, S.: Twenty years of distributed port-Hamiltonian systems: a literature review. IMA J. Math. Control. Inf. 37(4), 1400–1422 (2020). https://doi.org/10.1093/imamci/dnaa018](twenty-years-of-distributed-port-hamiltonian-systems-a-literature-review) -- [10.1093/imamci/dnaa018](https://doi.org/10.1093/imamci/dnaa018)
- Goyal, P., Pontes Duff, I., Benner, P.: Guaranteed stable quadratic models and their applications in SINDy and operator inference. arXiv Preprint (2023). https://doi.org/10.48550/arXiv.2308.13819 -- [10.48550/arXiv.2308.13819](https://doi.org/10.48550/arXiv.2308.13819)
- Gillis, N., Sharma, P.: On computing the distance to stability for matrices using linear dissipative Hamiltonian systems. Automatica 85, 113–121 (2017). https://doi.org/10.1016/j.automatica.2017.07.047 -- [10.1016/j.automatica.2017.07.047](https://doi.org/10.1016/j.automatica.2017.07.047)
- Gillis, N., Mehrmann, V., Sharma, P.: Computing the nearest stable matrix pairs. Numerical Linear Algebra with Applications 25(5), 2153 (2018). https://doi.org/10.1002/nla.2153.e2153nla.2153 -- [10.1002/nla.2153.e2153nla.2153](https://doi.org/10.1002/nla.2153.e2153nla.2153)
- Mehl, C., Mehrmann, V., Sharma, P.: Stability radii for linear Hamiltonian systems with dissipation under structure-preserving perturbations. SIAM J. Matrix Anal. Appl. 37(4), 1625–1654 (2016). https://doi.org/10.1137/16M1067330 -- [10.1137/16M1067330](https://doi.org/10.1137/16M1067330)
- Mehl, C., Mehrmann, V., Sharma, P.: Stability radii for real linear Hamiltonian systems with perturbed dissipation. BIT Numer. Math. 57(3), 811–843 (2017). https://doi.org/10.1007/s10543-017-0654-0 -- [10.1007/s10543-017-0654-0](https://doi.org/10.1007/s10543-017-0654-0)
- Liljegren-Sailer, B.: On port-Hamiltonian modeling and structure-preserving model reduction. Doctoral thesis, Universität Trier (2020). https://nbn-resolving.org/urn:nbn:de:hbz:385-1-14498
- Beattie, C., Gugercin, S., Mehrmann, V.: Structured Dynamical Systems. In: Beattie, C., Benner, P., Embree, M., Gugercin, S., Lefteriu, S. (eds.) Structure-preserving interpolatory model reduction for port-Hamiltonian differential-algebraic systems, pp. 235–254. Springer, Cham (2022). https://doi.org/10.1007/978-3-030-95157-3_13 -- [10.1007/978-3-030-95157-3_13](https://doi.org/10.1007/978-3-030-95157-3_13)
- [Gugercin, S., Polyuga, R.V., Beattie, C., van der Schaft, A.: Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9), 1963–1974 (2012). https://doi.org/10.1016/j.automatica.2012.05.052](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- [Breiten, T., Unger, B.: Passivity preserving model reduction via spectral factorization. Automatica 142, 110368 (2022). https://doi.org/10.1016/j.automatica.2022.110368](passivity-preserving-model-reduction-via-spectral-factorization) -- [10.1016/j.automatica.2022.110368](https://doi.org/10.1016/j.automatica.2022.110368)
- [Polyuga, R.V., van der Schaft, A.: Structure preserving model reduction of port-Hamiltonian systems by moment matching at infinity. Automatica 46(4), 665–672 (2010). https://doi.org/10.1016/j.automatica.2010.01.018](structure-preserving-model-reduction-of-port-hamiltonian-systems-by-moment-matching-at-infinity) -- [10.1016/j.automatica.2010.01.018](https://doi.org/10.1016/j.automatica.2010.01.018)
- [Ionescu, T.C., Astolfi, A.: Families of moment matching based, structure preserving approximations for linear port Hamiltonian systems. Automatica 49(8), 2424–2434 (2013). https://doi.org/10.1016/j.automatica.2013.05.006](families-of-moment-matching-based-structure-preserving-approximations-for-linear-port-hamiltonian-systems) -- [10.1016/j.automatica.2013.05.006](https://doi.org/10.1016/j.automatica.2013.05.006)
- [Egger, H., Kugler, T., Liljegren-Sailer, B., Marheineke, N., Mehrmann, V.: On structure-preserving model reduction for damped wave propagation in transport networks. SIAM J. Sci. Comput. 40(1), 331–365 (2018). https://doi.org/10.1137/17M1125303](on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks) -- [10.1137/17M1125303](https://doi.org/10.1137/17M1125303)
- Moser, T., Lohmann, B.: A new Riemannian framework for efficient H2-optimal model reduction of port-Hamiltonian systems. In: 2020 59th IEEE Conference on Decision and Control (CDC), pp. 5043–5049 (2020). https://doi.org/10.1109/CDC42340.2020.9304134 -- [10.1109/CDC42340.2020.9304134](https://doi.org/10.1109/CDC42340.2020.9304134)
- [Schwerdtner, P., Voigt, M.: SOBMOR: structured optimization-based model order reduction. SIAM J. Sci. Comput. 45(2), 502–529 (2023). https://doi.org/10.1137/20M1380235](sobmor-structured-optimization-based-model-order-reduction) -- [10.1137/20M1380235](https://doi.org/10.1137/20M1380235)
- [Polyuga, R.V., van der Schaft, A.J.: Effort- and flow-constraint reduction methods for structure preserving model reduction of port-Hamiltonian systems. Syst. Contr. Lett. 61(3), 412–421 (2012). https://doi.org/10.1016/j.sysconle.2011.12.008](effort-and-flow-constraint-reduction-methods-for-structure-preserving-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.sysconle.2011.12.008](https://doi.org/10.1016/j.sysconle.2011.12.008)
- Hauschild, S.-A., Marheineke, N., Mehrmann, V.: Model reduction techniques for linear constant coefficient port-Hamiltonian differential-algebraic systems. Control and Cybernetics 48, 125–152 (2019). https://doi.org/10.48550/arXiv.1901.10242 -- [10.48550/arXiv.1901.10242](https://doi.org/10.48550/arXiv.1901.10242)
- Guiver, C., Opmeer, M.R.: Error bounds in the gap metric for dissipative balanced approximations. Linear Algebra Appl. 439(12), 3659–3698 (2013). https://doi.org/10.1016/j.laa.2013.09.032 -- [10.1016/j.laa.2013.09.032](https://doi.org/10.1016/j.laa.2013.09.032)
- [Breiten, T., Morandin, R., Schulze, P.: Error bounds for port-Hamiltonian model and controller reduction based on system balancing. Comp. Math. Appl. 116, 100–115 (2022). https://doi.org/10.1016/j.camwa.2021.07.022](error-bounds-for-port-hamiltonian-model-and-controller-reduction-based-on-system-balancing) -- [10.1016/j.camwa.2021.07.022](https://doi.org/10.1016/j.camwa.2021.07.022)
- [Borja, P., Scherpen, J.M.A., Fujimoto, K.: Extended balancing of continuous LTI systems: a structure-preserving approach. IEEE Trans. Autom. Control 68(1), 257–271 (2023). https://doi.org/10.1109/TAC.2021.3138645](extended-balancing-of-continuous-lti-systems-a-structure-preserving-approach) -- [10.1109/TAC.2021.3138645](https://doi.org/10.1109/TAC.2021.3138645)
- [Schulze, P., Unger, B.: Model reduction for linear systems with low-rank switching. SIAM J. Control. Optim. 56(6), 4365–4384 (2018). https://doi.org/10.1137/18M1167887](model-reduction-for-linear-systems-with-low-rank-switching) -- [10.1137/18M1167887](https://doi.org/10.1137/18M1167887)
- Schulze, P.: Energy-based model reduction of transport-dominated phenomena. Doctoral thesis, Technische Universität Berlin (2023). https://doi.org/10.14279/depositonce-17843 -- [10.14279/depositonce-17843](https://doi.org/10.14279/depositonce-17843)
- Beattie, C., Gugercin, S.: Structure-preserving model reduction for nonlinear port-Hamiltonian systems. Proceed. IEEE Conf. Decision. Contr. 6564–6569 (2011). https://doi.org/10.1109/CDC.2011.6161504 -- [10.1109/CDC.2011.6161504](https://doi.org/10.1109/CDC.2011.6161504)
- [Chaturantabut, S., Beattie, C., Gugercin, S.: Structure-preserving model reduction for nonlinear port-Hamiltonian systems. SIAM J. Sci. Comput. 38(5), 837–865 (2016). https://doi.org/10.1137/15M1055085](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15M1055085](https://doi.org/10.1137/15M1055085)
- Wolf, T., Lohmann, B., Eid, R., Kotyczka, P.: Passivity and structure preserving order reduction of linear port-Hamiltonian systems using Krylov subspaces. Eur. J. Control. 16(4), 401–406 (2010). https://doi.org/10.3166/EJC.16.401-406 -- [10.3166/EJC.16.401-406](https://doi.org/10.3166/EJC.16.401-406)
- Nguyen, N.-C., Veroy, K., Patera, A.T.: Certified real-time solution of parametrized partial differential equations. In: Yip, S. (ed.) Handbook of Materials Modeling, pp. 1529–1564. Springer, Dordrecht (2005). https://doi.org/10.1007/978-1-4020-3286-8_76 -- [10.1007/978-1-4020-3286-8_76](https://doi.org/10.1007/978-1-4020-3286-8_76)
- Veroy, K., Patera, A.T.: Certified real-time solution of the parametrized steady incompressible Navier-Stokes equations: rigorous reduced-basis a posteriori error bounds. Int. J. Numer. Methods Fluids 47(8–9), 773–788 (2005). https://doi.org/10.1002/fld.867 -- [10.1002/fld.867](https://doi.org/10.1002/fld.867)
- Grepl, M.A., Patera, A.T.: A posteriori error bounds for reduced-basis approximations of parametrized parabolic partial differential equations. ESAIM: M2AN 39(1), 157–181 (2005). https://doi.org/10.1051/m2an:2005006 -- [10.1051/m2an:2005006](https://doi.org/10.1051/m2an:2005006)
- Knezevic, D.J., Nguyen, N.-C., Patera, A.T.: Reduced basis approximation and a posteriori error estimation for the parametrized unsteady Boussinesq equations. Math. Models Methods Appl. Sci. 21(07), 1415–1442 (2011). https://doi.org/10.1142/S0218202511005441 -- [10.1142/S0218202511005441](https://doi.org/10.1142/S0218202511005441)
- Grepl, M.A., Maday, Y., Nguyen, N.-C., Patera, A.T.: Efficient reduced-basis treatment of nonaffine and nonlinear partial differential equations. ESAIM: M2AN 41(3), 575–605 (2007). https://doi.org/10.1051/m2an:2007031 -- [10.1051/m2an:2007031](https://doi.org/10.1051/m2an:2007031)
- Grunert, D., Fehr, J., Haasdonk, B.: Well-scaled, a-posteriori error estimation for model order reduction of large second-order mechanical systems. ZAMM - J. Appl. Math. Mech. 100(8), 201900186 (2020). https://doi.org/10.1002/zamm.201900186 -- [10.1002/zamm.201900186](https://doi.org/10.1002/zamm.201900186)
- Glas, S., Patera, A.T., Urban, K.: A reduced basis method for the wave equation. Int. J. Comput. Fluid Dyn. 34(2), 139–146 (2020). https://doi.org/10.1080/10618562.2019.1686486 -- [10.1080/10618562.2019.1686486](https://doi.org/10.1080/10618562.2019.1686486)
- Stahl, N., Liljegren-Sailer, B., Marheineke, N.: Certified reduced basis method for the damped wave equations on networks. IFAC-PapersOnLine 55(20), 289–294 (2022). https://doi.org/10.1016/j.ifacol.2022.09.110 -- [10.1016/j.ifacol.2022.09.110](https://doi.org/10.1016/j.ifacol.2022.09.110)
- Antoulas, A.C., Benner, P., Feng, L.: Model reduction by iterative error system approximation. MCMDS 24(2), 103–118 (2018). https://doi.org/10.1080/13873954.2018.1427116 -- [10.1080/13873954.2018.1427116](https://doi.org/10.1080/13873954.2018.1427116)
- Feng, L., Lombardi, L., Antonini, G., Benner, P.: Multi-fidelity error estimation accelerates greedy model reduction of complex dynamical systems. Int. J. Numer. Meth. Eng. 124(23), 5312–5333 (2023). https://doi.org/10.1002/nme.7348 -- [10.1002/nme.7348](https://doi.org/10.1002/nme.7348)
- Güttel, S., Nakatsukasa, Y.: Scaled and squared subdiagonal Padé approximation for the matrix exponential. SIAM J. Matrix Anal. Appl. 37(1), 145–170 (2016). https://doi.org/10.1137/15M1027553 -- [10.1137/15M1027553](https://doi.org/10.1137/15M1027553)
- Söderlind, G.: The logarithmic norm. history and modern theory. BIT Numerical Mathematics 46(3), 631–652 (2006). https://doi.org/10.1007/s10543-006-0069-9 -- [10.1007/s10543-006-0069-9](https://doi.org/10.1007/s10543-006-0069-9)
- Desoer, C.A., Vidyasagar, M.: Feedback Systems. Society for Industrial and Applied Mathematics, Philadelphia (2009). https://doi.org/10.1137/1.9780898719055 -- [10.1137/1.9780898719055](https://doi.org/10.1137/1.9780898719055)
- Wittwar, D.: Approximation with matrix-valued kernels and highly effective error estimators for reduced basis approximations. Dissertation. University library Stuttgart, Stuttgart (2022). https://doi.org/10.18419/opus-12526 -- [10.18419/opus-12526](https://doi.org/10.18419/opus-12526)
- Hackbusch, W.: Hierarchical matrices: algorithms and analysis. Springer, Berlin Heidelberg (2015). https://doi.org/10.1007/978-3-662-47324-5 -- [10.1007/978-3-662-47324-5](https://doi.org/10.1007/978-3-662-47324-5)
- Gugercin, S., Antoulas, A.C.: A survey of model reduction by balanced truncation and some new results. Int. J. Control 77(8), 748–766 (2004). https://doi.org/10.1080/00207170410001713448 -- [10.1080/00207170410001713448](https://doi.org/10.1080/00207170410001713448)
- Rettberg, J., Wittwar, D., Buchfink, P., Brauchler, A., Ziegler, P., Fehr, J., Haasdonk, B.: Replication data for: port-Hamiltonian fluid-structure interaction modeling and structure-preserving model order reduction of a classical guitar. DaRUS (2023). https://doi.org/10.18419/darus-3248 -- [10.18419/darus-3248](https://doi.org/10.18419/darus-3248)
- Rettberg, J., Wittwar, D., Herkert, R.: Softwarepackage CCMOR2. DaRUS (2023). https://doi.org/10.18419/darus-3839 -- [10.18419/darus-3839](https://doi.org/10.18419/darus-3839)
- Peng, L., Mohseni, K.: Symplectic model reduction of Hamiltonian systems. SIAM J. Sci. Comput. 38(1), 1–27 (2016). https://doi.org/10.1137/140978922 -- [10.1137/140978922](https://doi.org/10.1137/140978922)
- Buchfink, P., Bhatt, A., Haasdonk, B.: Symplectic model order reduction with non-orthonormal bases. Math. Comput. Appl. 24(2) (2019). https://doi.org/10.3390/mca24020043 -- [10.3390/mca24020043](https://doi.org/10.3390/mca24020043)
- Chellappa, S., Feng, L., de la Rubia, V., Benner, P.: Inf-sup-constant-free state error estimator for model order reduction of parametric systems in electromagnetics. IEEE Trans. Microw. Theory Tech. 71(11), 4762–4777 (2023). https://doi.org/10.1109/TMTT.2023.3288642 -- [10.1109/TMTT.2023.3288642](https://doi.org/10.1109/TMTT.2023.3288642)
- Buchfink, P., Haasdonk, B., Rave, S.: PSD-Greedy basis generation for structure-preserving model order reduction of Hamiltonian systems. In: Frolkovič, P., Mikula, K., Ševčovič, D. (eds.) Proceedings of the Conference Algoritmy 2020, pp. 151–160. Vydavateľstvo SPEKTRUM, Vysoke Tatry, Podbanske (2020). http://www.iam.fmph.uniba.sk/amuc/ojs/index.php/algoritmy/article/view/1577/829

