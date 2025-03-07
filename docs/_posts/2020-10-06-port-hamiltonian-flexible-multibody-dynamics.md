---
layout: post
title: "Port-Hamiltonian flexible multibody dynamics"
date: 2020-10-06 00:00:00 +0100
permalink: port-hamiltonian-flexible-multibody-dynamics
year: 2021
authors: Andrea Brugnoli, Daniel Alazard, Valérie Pommier-Budinger, Denis Matignon
category: articles
tags:
  - Port-Hamiltonian systems
  - Floating frame formulation
  - Flexible multibody systems
  - Structure-preserving discretization
  - Substructuring
---
 
## Authors
[Andrea Brugnoli](authors/andrea-brugnoli), [Daniel Alazard](authors/daniel-alazard), [Valérie Pommier-Budinger](authors/valerie-pommier-budinger), [Denis Matignon](authors/denis-matignon)
 
## Abstract
A new formulation for the modular construction of flexible multibody systems is presented. By rearranging the equations for a flexible floating body and introducing the appropriate canonical momenta, the model is recast into a coupled system of ordinary and partial differential equations in port-Hamiltonian (pH) form. This approach relies on a floating frame description and is valid under the assumption of small deformations. This allows including mechanical models that cannot be easily formulated in terms of differential forms. Once a pH model is established, a finite element based method is then introduced to discretize the dynamics in a structure-preserving manner. Thanks to the features of the pH framework, complex multibody systems could be constructed in a modular way. Constraints are imposed at the velocity level, leading to an index 2 quasilinear differential-algebraic system. Numerical tests are carried out to assess the validity of the proposed approach.
 
## Keywords
Port-Hamiltonian systems; Floating frame formulation; Flexible multibody systems; Structure-preserving discretization; Substructuring
 
## Citation
- **Journal:** Multibody System Dynamics
- **Year:** 2021
- **Volume:** 51
- **Issue:** 3
- **Pages:** 343--375
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s11044-020-09758-6](https://doi.org/10.1007/s11044-020-09758-6)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Brugnoli_2020,
  title={{Port-Hamiltonian flexible multibody dynamics}},
  volume={51},
  ISSN={1573-272X},
  DOI={10.1007/s11044-020-09758-6},
  number={3},
  journal={Multibody System Dynamics},
  publisher={Springer Science and Business Media LLC},
  author={Brugnoli, Andrea and Alazard, Daniel and Pommier-Budinger, Valérie and Matignon, Denis},
  year={2020},
  pages={343--375}
}
{% endraw %}
{% endhighlight %}
 
## References
- Alazard, D., Perez, J.A., Cumer, C., Loquen, T.: Two-input two-output port model for mechanical systems. In: AIAA 2015-1778 (2015). https://doi.org/10.2514/6.2015-1778 -- [10.2514/6.2015-1778](https://doi.org/10.2514/6.2015-1778)
- Andersson, C., Führer, C., Åkesson, J.: Assimulo: a unified framework for {ODE} solvers. Math. Comput. Simul. 116(0), 26–43 (2015). https://doi.org/10.1016/j.matcom.2015.04.007 -- [10.1016/j.matcom.2015.04.007](https://doi.org/10.1016/j.matcom.2015.04.007)
- Arnold, D., Lee, J.: Mixed methods for elastodynamics with weak symmetry. SIAM J. Numer. Anal. 52(6), 2743–2769 (2014). https://doi.org/10.1137/13095032X -- [10.1137/13095032X](https://doi.org/10.1137/13095032X)
- Bauchau, O.A., Laulusa, A.: Review of contemporary approaches for constraint enforcement in multibody systems. J. Comput. Nonlinear Dyn. 3(1), 011005 (2008) -- [10.1115/1.2803258](https://doi.org/10.1115/1.2803258)
- [Beattie, C., Mehrmann, V., Xu, H., Zwart, H.: Linear port-Hamiltonian descriptor systems. Math. Control Signals Syst. 30(4), 17 (2018)](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- Bremer, H.: Elastic Multibody Dynamics. Springer, Berlin (2008) -- [10.1007/978-1-4020-8680-9](https://doi.org/10.1007/978-1-4020-8680-9)
- Brenan, K.E., Campbell, S.L., Petzold, L.R.: Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations. SIAM, Philadelphia (1995). https://doi.org/10.1137/1.9781611971224 -- [10.1137/1.9781611971224](https://doi.org/10.1137/1.9781611971224)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V., Matignon, D.: Port-Hamiltonian formulation and symplectic discretization of plate models. Part I: Mindlin model for thick plates. Appl. Math. Model. 75, 940–960 (2019). https://doi.org/10.1016/j.apm.2019.04.035](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-i-mindlin-model-for-thick-plates) -- [10.1016/j.apm.2019.04.035](https://doi.org/10.1016/j.apm.2019.04.035)
- [Brugnoli, A., Alazard, D., Pommier-Budinger, V., Matignon, D.: Port-Hamiltonian formulation and symplectic discretization of plate models. Part II: Kirchhoff model for thin plates. Appl. Math. Model. 75, 961–981 (2019). https://doi.org/10.1016/j.apm.2019.04.036](port-hamiltonian-formulation-and-symplectic-discretization-of-plate-models-part-ii-kirchhoff-model-for-thin-plates) -- [10.1016/j.apm.2019.04.036](https://doi.org/10.1016/j.apm.2019.04.036)
- Cardona, A.: Superelements modelling in flexible multibody dynamics. Multibody Syst. Dyn. 4(2), 245–266 (2000). https://doi.org/10.1023/A:1009875930232 -- [10.1023/A:1009875930232](https://doi.org/10.1023/A:1009875930232)
- [Cardoso-Ribeiro, F.L., Matignon, D., Lefèvre, L.: A partitioned finite element method for power-preserving discretization of open systems of conservation laws (2019). arXiv preprint arXiv:1906.05965. Under review](a-partitioned-finite-element-method-for-power-preserving-discretization-of-open-systems-of-conservation-laws) -- [10.1093/imamci/dnaa038](https://doi.org/10.1093/imamci/dnaa038)
- Celledoni, E., Høiseth, E.H., Ramzina, N.: Passivity-preserving splitting methods for rigid body systems. Multibody Syst. Dyn. 44(3), 251–275 (2018) -- [10.1007/s11044-018-9628-5](https://doi.org/10.1007/s11044-018-9628-5)
- [Cervera, J., van der Schaft, A.J., Baños, A.: Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica 43(2), 212–225 (2007). https://doi.org/10.1016/j.automatica.2006.08.014](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- [Chaturantabut, S., Beattie, C., Gugercin, S.: Structure-preserving model reduction for nonlinear port-Hamiltonian systems. SIAM J. Sci. Comput. 38(5), B837–B865 (2016). https://doi.org/10.1137/15M1055085](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15M1055085](https://doi.org/10.1137/15M1055085)
- Chebbi, J., Dubanchet, V., Perez Gonzalez, J.A., Alazard, D.: Linear dynamics of flexible multibody systems. Multibody Syst. Dyn. 41(1), 75–100 (2017). https://doi.org/10.1007/s11044-016-9559-y -- [10.1007/s11044-016-9559-y](https://doi.org/10.1007/s11044-016-9559-y)
- Cohen, G., Fauqueux, S.: Mixed spectral finite elements for the linear elasticity system in unbounded domains. SIAM J. Sci. Comput. 26(3), 864–884 (2005). https://doi.org/10.1137/S1064827502407457 -- [10.1137/S1064827502407457](https://doi.org/10.1137/S1064827502407457)
- [Duindam, V., Macchelli, A., Stramigioli, S., Bruyninckx, H.: Modeling and Control of Complex Physical Systems. Springer, Berlin (2009). https://www.springer.com/us/book/9783642031953](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [Egger, H., Kugler, T., Liljegren-Sailer, B., Marheineke, N., Mehrmann, V.: On structure-preserving model reduction for damped wave propagation in transport networks. SIAM J. Sci. Comput. 40(1), A331–A365 (2018). https://doi.org/10.1137/17M1125303](on-structure-preserving-model-reduction-for-damped-wave-propagation-in-transport-networks) -- [10.1137/17M1125303](https://doi.org/10.1137/17M1125303)
- Ellenbroek, M., Schilder, J.: On the use of absolute interface coordinates in the floating frame of reference formulation for flexible multibody dynamics. Multibody Syst. Dyn. 43(3), 193–208 (2018). https://doi.org/10.1007/s11044-017-9606-3 -- [10.1007/s11044-017-9606-3](https://doi.org/10.1007/s11044-017-9606-3)
- [Forni, P., Jeltsema, D., Lopes, G.A.: Port-Hamiltonian formulation of rigid-body attitude control. IFAC-PapersOnLine 48(13), 164–169 (2015). https://doi.org/10.1016/j.ifacol.2015.10.233. 5th IFAC Workshop on Lagrangian and Hamiltonian Methods for Nonlinear Control LHMNC 2015](port-hamiltonian-formulation-of-rigid-body-attitude-control) -- [10.1016/j.ifacol.2015.10.233](https://doi.org/10.1016/j.ifacol.2015.10.233)
- [Golo, G., Talasila, V., van der Schaft, A.J., Maschke, B.: Hamiltonian discretization of boundary control systems. Automatica 40(5), 757–771 (2004). https://doi.org/10.1016/j.automatica.2003.12.017](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Holm, D.D.: Geometric Mechanics: Part II: Rotating, Translating and Rolling. World Scientific, Singapore (2008) -- [10.1142/p549](https://doi.org/10.1142/p549)
- Horn, R.A., Johnson, C.R.: Matrix Analysis. Cambridge University Press, Cambridge (2012) -- [10.1017/CBO9781139020411](https://doi.org/10.1017/CBO9781139020411)
- Hurty, W.C.: Dynamic analysis of structural systems using component modes. AIAA J. 3(4), 678–685 (1965). https://doi.org/10.2514/3.2947 -- [10.2514/3.2947](https://doi.org/10.2514/3.2947)
- Kitis, L., Lindenberg, R.: Natural frequencies and mode shapes of flexible mechanisms by a transfer matrix method. Finite Elem. Anal. Des. 6(4), 267–285 (1990). https://doi.org/10.1016/0168-874X(90)90020-F -- [10.1016/0168-874X(90)90020-F](https://doi.org/10.1016/0168-874X(90)90020-F)
- Klerk, D.D., Rixen, D.J., Voormeeren, S.N.: General framework for dynamic substructuring: history, review and classification of techniques. AIAA J. 46(5), 1169–1181 (2008). https://doi.org/10.2514/1.33274 -- [10.2514/1.33274](https://doi.org/10.2514/1.33274)
- [Kotyczka, P., Lefèvre, L.: Discrete-time port-Hamiltonian systems: a definition based on symplectic integration. Syst. Control Lett. 133, 104530 (2019). https://doi.org/10.1016/j.sysconle.2019.104530](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- Laulusa, A., Bauchau, O.A.: Review of classical approaches for constraint enforcement in multibody systems. J. Comput. Nonlinear Dyn. 3(1), 011004 (2008) -- [10.1115/1.2803257](https://doi.org/10.1115/1.2803257)
- Leyendecker, S., Betsch, P., Steinmann, P.: The discrete null space method for the energy-consistent integration of constrained mechanical systems. Part III: Flexible multibody dynamics. Multibody Syst. Dyn. 19(1), 45–72 (2008). https://doi.org/10.1007/s11044-007-9056-4 -- [10.1007/s11044-007-9056-4](https://doi.org/10.1007/s11044-007-9056-4)
- [Macchelli, A., Melchiorri, C., Stramigioli, S.: Port-based modeling of a flexible link. IEEE Trans. Robot. 23, 650–660 (2007). https://doi.org/10.1109/TRO.2007.898990](port-based-modeling-of-a-flexible-link) -- [10.1109/TRO.2007.898990](https://doi.org/10.1109/TRO.2007.898990)
- [Macchelli, A., Melchiorri, C., Stramigioli, S.: Port-based modeling and simulation of mechanical systems with rigid and flexible links. IEEE Trans. Robot. 25(5), 1016–1029 (2009). https://doi.org/10.1109/TRO.2009.2026504](port-based-modeling-and-simulation-of-mechanical-systems-with-rigid-and-flexible-links) -- [10.1109/TRO.2009.2026504](https://doi.org/10.1109/TRO.2009.2026504)
- Marsden, J.E.: Lectures on Geometric Methods in Mathematical Physics. CBMS-NSF Regional Conference Series in Applied Mathematics. SIAM, Philadelphia (1981) -- [10.1137/1.9781611970326](https://doi.org/10.1137/1.9781611970326)
- Mehrmann, V., Morandin, R.: Structure-preserving discretization for port-Hamiltonian descriptor systems. In: Proceedings of the 59th IEEE Conference on Decision and Control, pp. 6663–6868 (2019)
- [Nageshrao, S.P., Lopes, G.A.D., Jeltsema, D., Babuška, R.: Port-Hamiltonian systems in adaptive and learning control: a survey. IEEE Trans. Autom. Control 61(5), 1223–1238 (2016). https://doi.org/10.1109/TAC.2015.2458491](port-hamiltonian-systems-in-adaptive-and-learning-control-a-survey) -- [10.1109/TAC.2015.2458491](https://doi.org/10.1109/TAC.2015.2458491)
- Nowakowski, C., Fehr, J., Fischer, M., Eberhard, P.: Model order reduction in elastic multibody systems using the floating frame of reference formulation. IFAC Proc. Vol. 45(2), 40–48 (2012). https://doi.org/10.3182/20120215-3-AT-3016.00007. 7th Vienna International Conference on Mathematical Modelling -- [10.3182/20120215-3-AT-3016.00007](https://doi.org/10.3182/20120215-3-AT-3016.00007)
- Ortega, R., García-Canseco, E.: Interconnection and damping assignment passivity-based control: a survey. Eur. J. Control 10(5), 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Perez, J.A., Alazard, D., Loquen, T., Pittet, C., Cumer, C.: Flexible multibody system linear modeling for control using component modes synthesis and double-port approach. J. Dyn. Syst. Meas. Control 138(12), 121004 (2016). https://doi.org/10.1115/1.4034149 -- [10.1115/1.4034149](https://doi.org/10.1115/1.4034149)
- Rathgeber, F., Ham, D., Mitchell, L., Lange, M., Luporini, F., McRae, A.T., Bercea, G., Markall, G.R., Kelly, P.: Firedrake: automating the finite element method by composing abstractions. ACM Trans. Math. Softw. 43(3), 24 (2017) -- [10.1145/2998441](https://doi.org/10.1145/2998441)
- Rong, B., Rui, X., Tao, L., Wang, G.: Theoretical modeling and numerical solution methods for flexible multibody system dynamics. Nonlinear Dyn. 98(2), 1519–1553 (2019). https://doi.org/10.1007/s11071-019-05191-3 -- [10.1007/s11071-019-05191-3](https://doi.org/10.1007/s11071-019-05191-3)
- Rui, X., He, B., Lu, Y., Lu, W., Wang, G.: Discrete time transfer matrix method for multibody system dynamics. Multibody Syst. Dyn. 14(3), 317–344 (2005). https://doi.org/10.1007/s11044-005-5006-1 -- [10.1007/s11044-005-5006-1](https://doi.org/10.1007/s11044-005-5006-1)
- Sanfedino, F., Alazard, D., Pommier-Budinger, V., Falcoz, A., Boquet, F.: Finite element based N-port model for preliminary design of multibody systems. J. Sound Vib. 415, 128–146 (2018). https://doi.org/10.1016/j.jsv.2017.11.021 -- [10.1016/j.jsv.2017.11.021](https://doi.org/10.1016/j.jsv.2017.11.021)
- van der Schaft, A.: L2-Gain and Passivity Techniques in Nonlinear Control, vol. 2. Springer, Berlin (2000) -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- [Scholz, L.: Condensed forms for linear port-Hamiltonian descriptor systems. Electron. J. Linear Algebra 35, 65–89 (2019). https://doi.org/10.13001/1081-3810.3638](condensed-forms-for-linear-port-hamiltonian-descriptor-systems) -- [10.13001/1081-3810.3638](https://doi.org/10.13001/1081-3810.3638)
- Simeon, B.: DAEs and PDEs in elastic multibody systems. Numer. Algorithms 19(1), 235–246 (1998). https://doi.org/10.1023/A:1019118809892 -- [10.1023/A:1019118809892](https://doi.org/10.1023/A:1019118809892)
- Simeon, B.: Computational Flexible Multibody Dynamics. Springer, Berlin (2013) -- [10.1007/978-3-642-35158-7](https://doi.org/10.1007/978-3-642-35158-7)
- Steinbrecher, A.: Numerical solution of quasi-linear differential-algebraic equations and industrial simulation of multibody systems. PhD thesis, TU Berlin (2006). https://doi.org/10.14279/depositonce-1360 -- [10.14279/depositonce-1360](https://doi.org/10.14279/depositonce-1360)
- Tan, T., Yousuff, A., Bahar, L., Konstantinidis, M.: A modified finite element-transfer matrix for control design of space structures. Comput. Struct. 36(1), 47–55 (1990). https://doi.org/10.1016/0045-7949(90)90173-Y -- [10.1016/0045-7949(90)90173-Y](https://doi.org/10.1016/0045-7949(90)90173-Y)
- Wasfy, T.M., Noor, A.K.: Computational strategies for flexible multibody systems. Appl. Mech. Rev. 56(6), 553–613 (2003). https://doi.org/10.1115/1.1590354 -- [10.1115/1.1590354](https://doi.org/10.1115/1.1590354)
- Young, K.D.: Distributed finite-element modeling and control approach for large flexible structures. J. Guid. Control Dyn. 13(4), 703–713 (1990). https://doi.org/10.2514/3.25389 -- [10.2514/3.25389](https://doi.org/10.2514/3.25389)

