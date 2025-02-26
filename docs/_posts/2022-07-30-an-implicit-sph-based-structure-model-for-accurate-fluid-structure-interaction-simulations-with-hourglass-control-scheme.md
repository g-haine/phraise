---
layout: post
title: "An implicit SPH-based structure model for accurate Fluid–Structure Interaction simulations with hourglass control scheme"
date: 2022-07-30 00:00:00 +0100
permalink: an-implicit-sph-based-structure-model-for-accurate-fluid-structure-interaction-simulations-with-hourglass-control-scheme
year: 2022
authors: Yuma Shimizu, Abbas Khayyer, Hitoshi Gotoh
category: journal-article
tag: Smoothed Particle Hydrodynamics; Implicit structure model; Hourglass control; Fluid–Structure Interaction
---
 
## Authors
**Yuma Shimizu, Abbas Khayyer, Hitoshi Gotoh**
 
## Abstract
This work is dedicated to development of an implicit SPH (Smoothed Particle Hydrodynamics)-based structure model as well as its integrated purely Lagrangian meshfree hydroelastic FSI (Fluid–Structure Interaction) solver for consistent, accurate and stable modeling of FSI problems. The implicit structure model is established in the context of Hamiltonian mechanics under the assumption of linear elastic solid. Four refined schemes are introduced for improved accuracy, consistency, efficiency and stability: two formerly developed schemes, [i] HT (High-order implicit Time integration) scheme, [ii] HD (High-order Discretization) operator scheme; as well as the novel two schemes newly proposed in this work, namely [iii] IPC (Iterative Predictor–Corrector) calculation procedures to minimize errors related to an imprecise assumption on rotation matrix and [iv] IHC (Implicit Hourglass Control) scheme for stabilizing simulation by suppressing spurious zero-energy modes. An enhanced particle-based FSI solver is formulated within a unified SPH framework by integrating a refined ISPH (Incompressible SPH) fluid model and the proposed implicit structure model, which allows consistent fluid–structure time coupling adopting the equivalent time step sizes in both phases. The proposed implicit structure model and FSI solver are configured in two-dimensions and validated with several 2D structure and FSI benchmark tests showing that our proposed implicit framework could provide almost consistent robustness, accuracy and efficiency with respect to the explicit one.
 
## Keywords
Smoothed Particle Hydrodynamics; Implicit structure model; Hourglass control; Fluid–Structure Interaction
 
## Citation
- **Journal:** European Journal of Mechanics - B/Fluids
- **Year:** 2022
- **Volume:** 96
- **Issue:** 
- **Pages:** 122--145
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.euromechflu.2022.07.007](https://doi.org/10.1016/j.euromechflu.2022.07.007)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Shimizu_2022,
  title={{An implicit SPH-based structure model for accurate Fluid–Structure Interaction simulations with hourglass control scheme}},
  volume={96},
  ISSN={0997-7546},
  DOI={10.1016/j.euromechflu.2022.07.007},
  journal={European Journal of Mechanics - B/Fluids},
  publisher={Elsevier BV},
  author={Shimizu, Yuma and Khayyer, Abbas and Gotoh, Hitoshi},
  year={2022},
  pages={122--145}
}
{% endraw %}
{% endhighlight %}
 
## References
- [10.1016/j.apor.2021.102734](https://doi.org/10.1016/j.apor.2021.102734)
- [10.1080/21664250.2018.1436243](https://doi.org/10.1080/21664250.2018.1436243)
- [10.1016/j.camwa.2018.06.002](https://doi.org/10.1016/j.camwa.2018.06.002)
- [10.1016/j.euromechflu.2020.11.004](https://doi.org/10.1016/j.euromechflu.2020.11.004)
- [10.1080/21664250.2018.1560683](https://doi.org/10.1080/21664250.2018.1560683)
- [10.1016/j.compfluid.2019.01.007](https://doi.org/10.1016/j.compfluid.2019.01.007)
- [10.1080/21664250.2018.1554203](https://doi.org/10.1080/21664250.2018.1554203)
- [10.1016/j.euromechflu.2019.10.006](https://doi.org/10.1016/j.euromechflu.2019.10.006)
- [10.1016/j.coastaleng.2020.103765](https://doi.org/10.1016/j.coastaleng.2020.103765)
- [10.1093/mnras/181.3.375](https://doi.org/10.1093/mnras/181.3.375)
- [10.13182/NSE96-A24205](https://doi.org/10.13182/NSE96-A24205)
- [10.1016/j.cma.2019.06.033](https://doi.org/10.1016/j.cma.2019.06.033)
- [10.1016/j.oceaneng.2021.108772](https://doi.org/10.1016/j.oceaneng.2021.108772)
- [10.1016/j.jfluidstructs.2020.103210](https://doi.org/10.1016/j.jfluidstructs.2020.103210)
- [10.1016/j.enganabound.2020.10.002](https://doi.org/10.1016/j.enganabound.2020.10.002)
- [10.1016/j.apor.2021.102775](https://doi.org/10.1016/j.apor.2021.102775)
- [10.1007/s42241-018-0005-x](https://doi.org/10.1007/s42241-018-0005-x)
- [10.1016/j.apor.2021.102822](https://doi.org/10.1016/j.apor.2021.102822)
- [10.1016/j.euromechflu.2010.09.010](https://doi.org/10.1016/j.euromechflu.2010.09.010)
- [10.1016/j.apor.2018.10.020](https://doi.org/10.1016/j.apor.2018.10.020)
- [10.1016/j.oceaneng.2021.108652](https://doi.org/10.1016/j.oceaneng.2021.108652)
- [10.1016/j.oceaneng.2020.108552](https://doi.org/10.1016/j.oceaneng.2020.108552)
- [10.1016/j.cpc.2021.108066](https://doi.org/10.1016/j.cpc.2021.108066)
- [10.1016/j.jfluidstructs.2019.02.002](https://doi.org/10.1016/j.jfluidstructs.2019.02.002)
- [10.1016/j.jfluidstructs.2021.103312](https://doi.org/10.1016/j.jfluidstructs.2021.103312)
- [10.1111/cgf.13317](https://doi.org/10.1111/cgf.13317)
- [10.1016/j.cma.2014.12.005](https://doi.org/10.1016/j.cma.2014.12.005)
- [A coupled incompressible SPH-Hamiltonian SPH solver for hydroelastic FSI corresponding to composite structures](a-coupled-incompressible-sph-hamiltonian-sph-solver-for-hydroelastic-fsi-corresponding-to-composite-structures) -- [10.1016/j.apm.2021.01.011](https://doi.org/10.1016/j.apm.2021.01.011)
- [10.1016/S0309-1708(03)00030-7](https://doi.org/10.1016/S0309-1708(03)00030-7)
- Y. Shimizu, H. Gotoh, A. Khayyer, An implicit fully Lagrangian meshfree structure model for consistent/accurate FSI simulations, in: Proceedings of the 15th International SPHERIC Workshop, 2021, pp. 60–67.
- [10.1016/j.enganabound.2021.10.023](https://doi.org/10.1016/j.enganabound.2021.10.023)
- [10.1090/S0025-5718-1968-0242392-2](https://doi.org/10.1090/S0025-5718-1968-0242392-2)
- [10.1007/BF02123482](https://doi.org/10.1007/BF02123482)
- [10.1007/s40722-016-0049-3](https://doi.org/10.1007/s40722-016-0049-3)
- [10.1016/j.euromechflu.2017.01.014](https://doi.org/10.1016/j.euromechflu.2017.01.014)
- [10.1016/j.coastaleng.2008.10.004](https://doi.org/10.1016/j.coastaleng.2008.10.004)
- [10.1016/j.apor.2010.01.001](https://doi.org/10.1016/j.apor.2010.01.001)
- [10.1016/j.jcp.2011.01.009](https://doi.org/10.1016/j.jcp.2011.01.009)
- [10.1016/j.compfluid.2013.05.001](https://doi.org/10.1016/j.compfluid.2013.05.001)
- [10.1016/j.coastaleng.2018.05.003](https://doi.org/10.1016/j.coastaleng.2018.05.003)
- [10.1080/21664250.2020.1815362](https://doi.org/10.1080/21664250.2020.1815362)
- [10.1016/j.compfluid.2020.104639](https://doi.org/10.1016/j.compfluid.2020.104639)
- [10.1002/nme.2222](https://doi.org/10.1002/nme.2222)
- [10.1016/j.jfluidstructs.2021.103342](https://doi.org/10.1016/j.jfluidstructs.2021.103342)
- [10.1145/1073204.1073216](https://doi.org/10.1145/1073204.1073216)
- [10.1016/j.cpc.2018.05.012](https://doi.org/10.1016/j.cpc.2018.05.012)
- [10.1016/j.compstruc.2007.01.002](https://doi.org/10.1016/j.compstruc.2007.01.002)
- [10.17736/ijope.2016.mk46](https://doi.org/10.17736/ijope.2016.mk46)
- [10.1016/S0045-7825(99)00441-7](https://doi.org/10.1016/S0045-7825(99)00441-7)
- [10.1007/s10444-004-1817-5](https://doi.org/10.1007/s10444-004-1817-5)
- [10.1002/1097-0207(20000810)48:10<1445::AID-NME831>3.0.CO;2-9](https://doi.org/10.1002/1097-0207(20000810)48:10<1445::AID-NME831>3.0.CO;2-9)
- [10.1002/nme.2744](https://doi.org/10.1002/nme.2744)
- [10.1016/j.compfluid.2019.06.023](https://doi.org/10.1016/j.compfluid.2019.06.023)
- [10.1016/S0045-7825(01)00254-7](https://doi.org/10.1016/S0045-7825(01)00254-7)
- [10.1016/j.cpc.2017.04.005](https://doi.org/10.1016/j.cpc.2017.04.005)
- [10.1016/j.jsv.2003.08.051](https://doi.org/10.1016/j.jsv.2003.08.051)
- [10.1007/s00466-008-0245-7](https://doi.org/10.1007/s00466-008-0245-7)
- [10.1016/j.jcp.2011.10.027](https://doi.org/10.1016/j.jcp.2011.10.027)
- [10.1016/j.compfluid.2018.10.018](https://doi.org/10.1016/j.compfluid.2018.10.018)
- [10.1016/j.enganabound.2019.03.012](https://doi.org/10.1016/j.enganabound.2019.03.012)
- [10.1016/j.enganabound.2019.03.033](https://doi.org/10.1016/j.enganabound.2019.03.033)
- [10.1016/j.piutam.2015.11.013](https://doi.org/10.1016/j.piutam.2015.11.013)
- [10.1007/s10494-020-00165-7](https://doi.org/10.1007/s10494-020-00165-7)
- [10.1016/j.cma.2021.114164](https://doi.org/10.1016/j.cma.2021.114164)
- [10.1016/j.oceaneng.2016.04.006](https://doi.org/10.1016/j.oceaneng.2016.04.006)

