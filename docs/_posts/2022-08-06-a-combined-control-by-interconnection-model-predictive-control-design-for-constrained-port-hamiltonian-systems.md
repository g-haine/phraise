---
layout: post
title: "A combined Control by Interconnection—Model Predictive Control design for constrained Port-Hamiltonian systems"
date: 2022-08-06 00:00:00 +0100
permalink: a-combined-control-by-interconnection-model-predictive-control-design-for-constrained-port-hamiltonian-systems
year: 2022
authors: T.H. Pham, N.M.T. Vu, I. Prodan, L. Lefèvre
category:
  - articles
tags:
  - constrained port-hamiltonian systems
  - control by interconnection
  - model predictive control
  - primal–dual gradient method
---
 
## Authors
[T.H. Pham](authors/thanh_hung_pham), [N.M.T. Vu](authors/ngoc_minh_trang_vu), [I. Prodan](authors/ionela_prodan), [L. Lefèvre](authors/laurent_lefevre)
 
## Abstract
This paper proposes a Control by Interconnection design, for a class of constrained Port-Hamiltonian systems, which is based on an associated Model Predictive Control optimization problem. This associated optimization problem allows to consider both state and input constraints simultaneously. Based on the first order Karush–Kuhn–Tucker optimality condition, the primal–dual gradient method is then used to build a passive feedback controller, derived from the MPC-induced optimization problem. The resulting passive controller is coupled with the original Port-Hamiltonian system through a power-preserving interconnection, in order to guarantee both the closed-loop stability and constraints satisfaction, but not the optimality anymore. Comments on parameters tuning for the proposed control design, together with validations of the approach through simulations first on a linear LC circuit, then on a nonlinear Permanent Magnet Synchronous Motor and comparisons with a classical MPC design, are provided to discuss the effectiveness of the approach.
 
## Keywords
Constrained Port-Hamiltonian systems; Control by Interconnection; Model Predictive Control; Primal–dual gradient method
 
## Citation
- **Journal:** Systems &amp; Control Letters
- **Year:** 2022
- **Volume:** 167
- **Issue:** 
- **Pages:** 105336
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.sysconle.2022.105336](https://doi.org/10.1016/j.sysconle.2022.105336)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Pham_2022,
  title={{A combined Control by Interconnection—Model Predictive Control design for constrained Port-Hamiltonian systems}},
  volume={167},
  ISSN={0167-6911},
  DOI={10.1016/j.sysconle.2022.105336},
  journal={Systems &amp; Control Letters},
  publisher={Elsevier BV},
  author={Pham, T.H. and Vu, N.M.T. and Prodan, I. and Lefèvre, L.},
  year={2022},
  pages={105336}
}
{% endraw %}
{% endhighlight %}
 
## References
- [van der Schaft, A. Port-Hamiltonian Modeling for Control. Annual Review of Control, Robotics, and Autonomous Systems vol. 3 393–416 (2020)](port-hamiltonian-modeling-for-control) -- [10.1146/annurev-control-081219-092250](https://doi.org/10.1146/annurev-control-081219-092250)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 53 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/TAC.2008.2006930](https://doi.org/10.1109/TAC.2008.2006930)
- [Borja, P., Cisneros, R. & Ortega, R. A constructive procedure for energy shaping of port—Hamiltonian systems. Automatica vol. 72 230–234 (2016)](a-constructive-procedure-for-energy-shaping-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2016.05.028](https://doi.org/10.1016/j.automatica.2016.05.028)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Wang, Z.-M., Wei, A., Zong, G., Zhao, X. & Li, H. Finite-time stabilization and<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si5.svg"><mml:msub><mml:mi mathvariant="bold-script">H</mml:mi><mml:mi>∞</mml:mi></mml:msub></mml:math>control for a class of switched nonlinear port-controlled Hamiltonian systems subject to actuator saturation. Journal of the Franklin Institute vol. 357 11807–11829 (2020) -- [10.1016/j.jfranklin.2019.11.055](https://doi.org/10.1016/j.jfranklin.2019.11.055)
- [Stegink, T., De Persis, C. & van der Schaft, A. A Unifying Energy-Based Approach to Stability of Power Grids With Market Dynamics. IEEE Transactions on Automatic Control vol. 62 2612–2622 (2017)](a-unifying-energy-based-approach-to-stability-of-power-grids-with-market-dynamics) -- [10.1109/TAC.2016.2613901](https://doi.org/10.1109/TAC.2016.2613901)
- [Benedito, E., del Puerto-Flores, D., Dòria-Cerezo, A. & Scherpen, J. M. A. Port-Hamiltonian based Optimal Power Flow algorithm for multi-terminal DC networks. Control Engineering Practice vol. 83 141–150 (2019)](port-hamiltonian-based-optimal-power-flow-algorithm-for-multi-terminal-dc-networks) -- [10.1016/j.conengprac.2018.10.018](https://doi.org/10.1016/j.conengprac.2018.10.018)
- R.E. Kalman, When is a linear control system optimal? in: Joint Automatic Control Conference, (1), 1963, pp. 1–15.
- N.M.T. Vu, L. Lefèvre, A connection between optimal control and IDA-PBC design, in: 6th IFAC Workshop on Lagrangian and Hamiltonian Methods for Non Linear Control, Valparaiso, Chile, May 1-4, (3), 2018, pp. 1017–1022.
- [Wu, Y., Hamroun, B., Le Gorrec, Y. & Maschke, B. Reduced Order LQG Control Design for Infinite Dimensional Port Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 66 865–871 (2021)](reduced-order-lqg-control-design-for-infinite-dimensional-port-hamiltonian-systems) -- [10.1109/TAC.2020.2997373](https://doi.org/10.1109/TAC.2020.2997373)
- [Stegink, T. W., Persis, C. D. & van der Schaft, A. J. Port-Hamiltonian Formulation of the Gradient Method Applied to Smart Grids. IFAC-PapersOnLine vol. 48 13–18 (2015)](port-hamiltonian-formulation-of-the-gradient-method-applied-to-smart-grids) -- [10.1016/j.ifacol.2015.10.207](https://doi.org/10.1016/j.ifacol.2015.10.207)
- [Kölsch, L., Jané Soneira, P., Strehle, F. & Hohmann, S. Optimal control of port-Hamiltonian systems: A continuous-time learning approach. Automatica vol. 130 109725 (2021)](optimal-control-of-port-hamiltonian-systems-a-continuous-time-learning-approach) -- [10.1016/j.automatica.2021.109725](https://doi.org/10.1016/j.automatica.2021.109725)
- Mayne, D. Q. Model predictive control: Recent developments and future promise. Automatica vol. 50 2967–2986 (2014) -- [10.1016/j.automatica.2014.10.128](https://doi.org/10.1016/j.automatica.2014.10.128)
- Yoshida, K., Inoue, M. & Hatanaka, T. Instant MPC for Linear Systems and Dissipativity-Based Stability Analysis. IEEE Control Systems Letters vol. 3 811–816 (2019) -- [10.1109/LCSYS.2019.2918095](https://doi.org/10.1109/LCSYS.2019.2918095)
- [Venkatraman, A. & van der Schaft, A. J. Full-order observer design for a class of port-Hamiltonian systems. Automatica vol. 46 555–561 (2010)](full-order-observer-design-for-a-class-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2010.01.019](https://doi.org/10.1016/j.automatica.2010.01.019)
- [Vincent, B., Hudon, N., Lefèvre, L. & Dochain, D. Port-Hamiltonian observer design for plasma profile estimation in tokamaks. IFAC-PapersOnLine vol. 49 93–98 (2016)](port-hamiltonian-observer-design-for-plasma-profile-estimation-in-tokamaks) -- [10.1016/j.ifacol.2016.10.761](https://doi.org/10.1016/j.ifacol.2016.10.761)

