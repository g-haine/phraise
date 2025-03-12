---
layout: post
title: "Goal-oriented time adaptivity for port-Hamiltonian systems"
date: 2024-12-19 00:00:00 +0100
permalink: goal-oriented-time-adaptivity-for-port-hamiltonian-systems
year: 2025
authors: Andreas Bartel, Manuel Schaller
category: articles
tags:
  - Goal-oriented grid adaptivity
  - Port-Hamiltonian systems
  - Energy balance
---
 
## Authors
[Andreas Bartel](authors/andreas-bartel), [Manuel Schaller](authors/manuel-schaller)
 
## Abstract
Port-Hamiltonian systems provide an energy-based modeling paradigm for dynamical input-state-output systems. At their core, they fulfill an energy balance relating stored, dissipated and supplied energy. To accurately resolve this energy balance in time discretizations, we propose an adaptive grid refinement technique based on a posteriori error estimation. The evaluation of the error estimator includes the computation of adjoint sensitivities. To interpret this adjoint equation as a backwards-in-time equation, we show piecewise weak differentiability of the dual variable. Then, leveraging dissipativity of the port-Hamiltonian dynamics, we present a parallelizable approximation of the underlying adjoint system in the spirit of a block-Jacobi method to efficiently compute error indicators. We illustrate the performance of the proposed scheme by means of numerical experiments showing that it yields a smaller violation of the energy balance when compared to uniform refinements and traditional step size controlled time stepping.
 
## Keywords
Goal-oriented grid adaptivity; Port-Hamiltonian systems; Energy balance
 
## Citation
- **Journal:** Journal of Computational and Applied Mathematics
- **Year:** 2025
- **Volume:** 461
- **Issue:** 
- **Pages:** 116450
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.cam.2024.116450](https://doi.org/10.1016/j.cam.2024.116450)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Bartel_2025,
  title={{Goal-oriented time adaptivity for port-Hamiltonian systems}},
  volume={461},
  ISSN={0377-0427},
  DOI={10.1016/j.cam.2024.116450},
  journal={Journal of Computational and Applied Mathematics},
  publisher={Elsevier BV},
  author={Bartel, Andreas and Schaller, Manuel},
  year={2025},
  pages={116450}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/goal-oriented-time-adaptivity-for-port-hamiltonian-systems.bib)
 
## References
- Jacob, (2012)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- [Venkatraman, A. & van der Schaft, A. J. Full-order observer design for a class of port-Hamiltonian systems. Automatica vol. 46 555–561 (2010)](full-order-observer-design-for-a-class-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2010.01.019](https://doi.org/10.1016/j.automatica.2010.01.019)
- [Mehl, C., Mehrmann, V. & Wojtylak, M. Linear Algebra Properties of Dissipative Hamiltonian Descriptor Systems. SIAM Journal on Matrix Analysis and Applications vol. 39 1489–1519 (2018)](linear-algebra-properties-of-dissipative-hamiltonian-descriptor-systems) -- [10.1137/18m1164275](https://doi.org/10.1137/18m1164275)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- [Schaller, M., Philipp, F., Faulwasser, T., Worthmann, K. & Maschke, B. Control of port-Hamiltonian systems with minimal energy supply. European Journal of Control vol. 62 33–40 (2021)](control-of-port-hamiltonian-systems-with-minimal-energy-supply) -- [10.1016/j.ejcon.2021.06.017](https://doi.org/10.1016/j.ejcon.2021.06.017)
- [Faulwasser, T., Maschke, B., Philipp, F., Schaller, M. & Worthmann, K. Optimal Control of Port-Hamiltonian Descriptor Systems with Minimal Energy Supply. SIAM Journal on Control and Optimization vol. 60 2132–2158 (2022)](optimal-control-of-port-hamiltonian-descriptor-systems-with-minimal-energy-supply) -- [10.1137/21m1427723](https://doi.org/10.1137/21m1427723)
- [Schaller, M. et al. Energy-optimal control of adaptive structures. at - Automatisierungstechnik vol. 72 107–119 (2024)](energy-optimal-control-of-adaptive-structures) -- [10.1515/auto-2023-0090](https://doi.org/10.1515/auto-2023-0090)
- Hairer, E., Hochbruck, M., Iserles, A. & Lubich, C. Geometric Numerical Integration. Oberwolfach Reports vol. 3 805–882 (2006) -- [10.4171/owr/2006/14](https://doi.org/10.4171/owr/2006/14)
- Leimkuhler, (2004)
- Mehrmann, V. & Morandin, R. Structure-preserving discretization for port-Hamiltonian descriptor systems. 2019 IEEE 58th Conference on Decision and Control (CDC) 6863–6868 (2019) doi:10.1109/cdc40024.2019.9030180 -- [10.1109/cdc40024.2019.9030180](https://doi.org/10.1109/cdc40024.2019.9030180)
- [Kotyczka, P. & Lefèvre, L. Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters vol. 133 104530 (2019)](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- Gören-Sümer, L. & Yalçιn, Y. Gradient Based Discrete-Time Modeling and Control of Hamiltonian Systems. IFAC Proceedings Volumes vol. 41 212–217 (2008) -- [10.3182/20080706-5-kr-1001.00036](https://doi.org/10.3182/20080706-5-kr-1001.00036)
- [Kinon, P. L., Thoma, T., Betsch, P. & Kotyczka, P. Discrete nonlinear elastodynamics in a port‐Hamiltonian framework. PAMM vol. 23 (2023)](discrete-nonlinear-elastodynamics-in-a-port-hamiltonian-framework) -- [10.1002/pamm.202300144](https://doi.org/10.1002/pamm.202300144)
- [Gonzalez, O. Time integration and discrete Hamiltonian systems. Journal of Nonlinear Science vol. 6 449–467 (1996)](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- Schops, S., De Gersem, H. & Bartel, A. A Cosimulation Framework for Multirate Time Integration of Field/Circuit Coupled Problems. IEEE Transactions on Magnetics vol. 46 3233–3236 (2010) -- [10.1109/tmag.2010.2045156](https://doi.org/10.1109/tmag.2010.2045156)
- Gear, C. W. & Wells, D. R. Multirate linear multistep methods. BIT vol. 24 484–502 (1984) -- [10.1007/bf01934907](https://doi.org/10.1007/bf01934907)
- Bartel, Multirate schemes — an answer of numerical analysis. (2022)
- Schäfers, (2023)
- Günther, M. & Sandu, A. Multirate generalized additive Runge Kutta methods. Numerische Mathematik vol. 133 497–524 (2015) -- [10.1007/s00211-015-0756-z](https://doi.org/10.1007/s00211-015-0756-z)
- Estep, D. A Posteriori Error Bounds and Global Error Control for Approximation of Ordinary Differential Equations. SIAM Journal on Numerical Analysis vol. 32 1–48 (1995) -- [10.1137/0732001](https://doi.org/10.1137/0732001)
- Becker, R., Kapp, H. & Rannacher, R. Adaptive Finite Element Methods for Optimal Control of Partial Differential Equations: Basic Concept. SIAM Journal on Control and Optimization vol. 39 113–132 (2000) -- [10.1137/s0363012999351097](https://doi.org/10.1137/s0363012999351097)
- Becker, R. & Rannacher, R. An optimal control approach to a posteriori error estimation in finite element methods. Acta Numerica vol. 10 1–102 (2001) -- [10.1017/s0962492901000010](https://doi.org/10.1017/s0962492901000010)
- Hartmann, (2002)
- Meidner, D. & Vexler, B. Adaptive Space‐Time Finite Element Methods for Parabolic Optimization Problems. SIAM Journal on Control and Optimization vol. 46 116–142 (2007) -- [10.1137/060648994](https://doi.org/10.1137/060648994)
- Vexler, (2004)
- Kröner, A. Adaptive Finite Element Methods For Optimal Control Of Second Order Hyperbolic Equations. Computational Methods in Applied Mathematics vol. 11 214–240 (2011) -- [10.2478/cmam-2011-0012](https://doi.org/10.2478/cmam-2011-0012)
- Estep, D., Ginting, V. & Tavener, S. A Posteriori analysis of a multirate numerical method for ordinary differential equations. Computer Methods in Applied Mechanics and Engineering vols 223–224 10–27 (2012) -- [10.1016/j.cma.2012.02.021](https://doi.org/10.1016/j.cma.2012.02.021)
- Bangerth, (2003)
- Becker, A feed-back approach to error control in finite element methods: basic analysis and examples. East-West J. Numer. Math. (1996)
- Schiela, A. A concise proof for existence and uniqueness of solutions of linear parabolic PDEs in the context of optimal control. Systems &amp; Control Letters vol. 62 895–901 (2013) -- [10.1016/j.sysconle.2013.06.013](https://doi.org/10.1016/j.sysconle.2013.06.013)
- Dörfler, W. A Convergent Adaptive Algorithm for Poisson’s Equation. SIAM Journal on Numerical Analysis vol. 33 1106–1124 (1996) -- [10.1137/0733054](https://doi.org/10.1137/0733054)
- Deuflhard, P., Leinen, P. & Yserentant, H. Concepts of an adaptive hierarchical finite element code. IMPACT of Computing in Science and Engineering vol. 1 3–35 (1989) -- [10.1016/0899-8248(89)90018-9](https://doi.org/10.1016/0899-8248(89)90018-9)
- Petzold, L. Automatic Selection of Methods for Solving Stiff and Nonstiff Systems of Ordinary Differential Equations. SIAM Journal on Scientific and Statistical Computing vol. 4 136–148 (1983) -- [10.1137/0904010](https://doi.org/10.1137/0904010)
- Estep, D., Holst, M. & Larson, M. Generalized Green’s Functions and the Effective Domain of Influence. SIAM Journal on Scientific Computing vol. 26 1314–1339 (2005) -- [10.1137/s1064827502416319](https://doi.org/10.1137/s1064827502416319)

