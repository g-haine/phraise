---
title: "Modeling and Control Design of Port-Hamiltonian Systems in Discrete-Time"
date: 2026-09-07 00:00:00 +0100
permalink: modeling-and-control-design-of-port-hamiltonian-systems-in-discrete-time
year: 2026
authors: Alessandro Macchelli
category: articles
---
 
## Authors
[Alessandro Macchelli](authors/alessandro-macchelli)
 
## Abstract
This paper aims to describe a synthesis procedure for discrete-time, energy-based regulators for continuous-time port-Hamiltonian systems. The methodology consists of three steps. The first deals with the definition of a discrete-time approximation of the plant, which is subsequently employed in the development of the control law. The discrete-time model is obtained from the continuous-time dynamics by replacing the gradient of the Hamiltonian function with a discrete gradient. In this way, passivity, with the energy as storage function, is preserved, although the resulting state equation is in implicit form. The second step concerns the control synthesis and extends the continuous-time energy-shaping plus damping injection design technique to the proposed class of discrete-time port-Hamiltonian systems. Finally, the last step addresses the interconnection between the digital controller and the continuous-time plant. The coupling is implemented via a zero-order hold and relies on the solution of an optimization problem that determines the “best” and “minimal” correction to be applied to the nominal control action in order to achieve the same performance as that obtained when the regulator is connected in closed loop with the discrete-time model of the plant. This is the reference scenario used to develop and tune the control law. The complete procedure (time discretisation, control design, and coupling implementation) is illustrated through an example.
 
## Citation
- **Journal:** Entropy
- **Year:** 2026
- **Volume:** 28
- **Issue:** 9
- **Pages:** 1002
- **Publisher:** MDPI AG
- **DOI:** [10.3390/e28091002](https://doi.org/10.3390/e28091002)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Macchelli_2026,
  title={{Modeling and Control Design of Port-Hamiltonian Systems in Discrete-Time}},
  volume={28},
  ISSN={1099-4300},
  DOI={10.3390/e28091002},
  number={9},
  journal={Entropy},
  publisher={MDPI AG},
  author={Macchelli, Alessandro},
  year={2026},
  pages={1002}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/modeling-and-control-design-of-port-hamiltonian-systems-in-discrete-time.bib)
 
## References
- [van der Schaft A (2017) L2-Gain and Passivity Techniques in Nonlinear Control. Springer International Publishin](l2-gain-and-passivity-techniques-in-nonlinear-control) -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- (2001) Putting energy back in control. IEEE Control Syst 21(2):18–33. https://doi.org/10.1109/37.91539 -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Fujimoto K, Sugie T (2001) Canonical transformation and stabilization of generalized Hamiltonian systems. Systems &amp; Control Letters 42(3):217–227. https://doi.org/10.1016/s0167-6911(00)00091- -- [10.1016/s0167-6911(00)00091-8](https://doi.org/10.1016/s0167-6911(00)00091-8)
- Ruth RD (1983) A Can0nical Integrati0n Technique. IEEE Trans Nucl Sci 30(4):2669–2671. https://doi.org/10.1109/tns.1983.433291 -- [10.1109/tns.1983.4332919](https://doi.org/10.1109/tns.1983.4332919)
- Gonzalez O, Simo JC (1996) On the stability of symplectic and energy-momentum algorithms for non-linear Hamiltonian systems with symmetry. Computer Methods in Applied Mechanics and Engineering 134(3–4):197–222. https://doi.org/10.1016/0045-7825(96)01009- -- [10.1016/0045-7825(96)01009-2](https://doi.org/10.1016/0045-7825(96)01009-2)
- Marsden JE, West M (2001) Discrete mechanics and variational integrators. Acta Numerica 10:357–514. https://doi.org/10.1017/s096249290100006 -- [10.1017/s096249290100006x](https://doi.org/10.1017/s096249290100006x)
- [Kotyczka P, Lefèvre L (2019) Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters 133:104530. https://doi.org/10.1016/j.sysconle.2019.10453](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- [Kotyczka P, Thoma T (2021) Symplectic discrete-time energy-based control for nonlinear mechanical systems. Automatica 133:109842. https://doi.org/10.1016/j.automatica.2021.10984](symplectic-discrete-time-energy-based-control-for-nonlinear-mechanical-systems) -- [10.1016/j.automatica.2021.109842](https://doi.org/10.1016/j.automatica.2021.109842)
- [Gonzalez O (1996) Time integration and discrete Hamiltonian systems. J Nonlinear Sci 6(5):449–467. https://doi.org/10.1007/bf0244016](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- Quispel GRW, Turner GS (1996) Discrete gradient methods for solving ODEs numerically while preserving a first integral. J Phys A: Math Gen 29(13):L341–L349. https://doi.org/10.1088/0305-4470/29/13/00 -- [10.1088/0305-4470/29/13/006](https://doi.org/10.1088/0305-4470/29/13/006)
- [Aoues S, Di Loreto M, Eberard D, Marquis-Favre W (2017) Hamiltonian systems discrete-time approximation: Losslessness, passivity and composability. Systems &amp; Control Letters 110:9–14. https://doi.org/10.1016/j.sysconle.2017.10.00](hamiltonian-systems-discrete-time-approximation-losslessness-passivity-and-composability) -- [10.1016/j.sysconle.2017.10.003](https://doi.org/10.1016/j.sysconle.2017.10.003)
- [Moreschini A, Mattioni M, Monaco S, Normand-Cyrot D (2019) Discrete port-controlled Hamiltonian dynamics and average passivation. 2019 IEEE 58th Conference on Decision and Control (CDC) 1430–143](discrete-port-controlled-hamiltonian-dynamics-and-average-passivation) -- [10.1109/cdc40024.2019.9029809](https://doi.org/10.1109/cdc40024.2019.9029809)
- [Moreschini A, Mattioni M, Monaco S, Normand-Cyrot D (2021) Stabilization of Discrete Port-Hamiltonian Dynamics via Interconnection and Damping Assignment. IEEE Control Syst Lett 5(1):103–108. https://doi.org/10.1109/lcsys.2020.300070](stabilization-of-discrete-port-hamiltonian-dynamics-via-interconnection-and-damping-assignment) -- [10.1109/lcsys.2020.3000705](https://doi.org/10.1109/lcsys.2020.3000705)
- [Macchelli A (2022) Trajectory Tracking for Discrete-Time Port-Hamiltonian Systems. IEEE Control Syst Lett 6:3146–3151. https://doi.org/10.1109/lcsys.2022.318284](trajectory-tracking-for-discrete-time-port-hamiltonian-systems) -- [10.1109/lcsys.2022.3182845](https://doi.org/10.1109/lcsys.2022.3182845)
- [Macchelli A (2023) Control Design for a Class of Discrete-Time Port-Hamiltonian Systems. IEEE Trans Automat Contr 68(12):8224–8231. https://doi.org/10.1109/tac.2023.329218](control-design-for-a-class-of-discrete-time-port-hamiltonian-systems) -- [10.1109/tac.2023.3292180](https://doi.org/10.1109/tac.2023.3292180)
- [Macchelli A (2024) A Discrete-Time Formulation of Nonlinear Distributed-Parameter Port-Hamiltonian Systems. IEEE Control Syst Lett 8:802–807. https://doi.org/10.1109/lcsys.2024.340476](a-discrete-time-formulation-of-nonlinear-distributed-parameter-port-hamiltonian-systems) -- [10.1109/lcsys.2024.3404769](https://doi.org/10.1109/lcsys.2024.3404769)
- [Macchelli A (2026) Port-Hamiltonian Boundary Control Systems in Discrete-Time Modeling and Control Design. IEEE Trans Automat Contr 71(2):722–736. https://doi.org/10.1109/tac.2025.359306](port-hamiltonian-boundary-control-systems-in-discrete-time-modeling-and-control-design) -- [10.1109/tac.2025.3593062](https://doi.org/10.1109/tac.2025.3593062)
- [Aoues S, Eberard D, Marquis-Favre W (2015) Discrete IDA-PBC control law for Newtonian mechanical port-Hamiltonian systems. 2015 54th IEEE Conference on Decision and Control (CDC) 4388–439](discrete-ida-pbc-control-law-for-newtonian-mechanical-port-hamiltonian-systems) -- [10.1109/cdc.2015.7402904](https://doi.org/10.1109/cdc.2015.7402904)
- [Stramigioli S, Secchi C, van der Schaft AJ, Fantuzzi C (2005) Sampled data systems passivity and discrete port-Hamiltonian systems. IEEE Trans Robot 21(4):574–587. https://doi.org/10.1109/tro.2004.84233](sampled-data-systems-passivity-and-discrete-port-hamiltonian-systems) -- [10.1109/tro.2004.842330](https://doi.org/10.1109/tro.2004.842330)
- Costa-Castelló R, Fossas E (2007) On Preserving Passivity in Sampled-data Linear Systems. European Journal of Control 13(6):583–590. https://doi.org/10.3166/ejc.13.583-59 -- [10.3166/ejc.13.583-590](https://doi.org/10.3166/ejc.13.583-590)
- Harten A, Lax PD, Leer B van (1983) On Upstream Differencing and Godunov-Type Schemes for Hyperbolic Conservation Laws. SIAM Rev 25(1):35–61. https://doi.org/10.1137/102500 -- [10.1137/1025002](https://doi.org/10.1137/1025002)
- [Nunna K, Sassano M, Astolfi A (2015) Constructive Interconnection and Damping Assignment for Port-Controlled Hamiltonian Systems. IEEE Trans Automat Contr 60(9):2350–2361. https://doi.org/10.1109/tac.2015.240066](constructive-interconnection-and-damping-assignment-for-port-controlled-hamiltonian-systems) -- [10.1109/tac.2015.2400663](https://doi.org/10.1109/tac.2015.2400663)
- Krupa P, Jaouani R, Limon D, Alamo T (2024) A Sparse ADMM-Based Solver for Linear MPC Subject to Terminal Quadratic Constraint. IEEE Trans Contr Syst Technol 32(6):2376–2384. https://doi.org/10.1109/tcst.2024.338606 -- [10.1109/tcst.2024.3386062](https://doi.org/10.1109/tcst.2024.3386062)

