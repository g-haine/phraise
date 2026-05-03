---
title: "A combined Control by Interconnection—Model Predictive Control design for constrained Port-Hamiltonian systems"
date: 2022-08-06 00:00:00 +0100
permalink: a-combined-control-by-interconnection-model-predictive-control-design-for-constrained-port-hamiltonian-systems
year: 2022
authors: T.H. Pham, N.M.T. Vu, I. Prodan, L. Lefèvre
category: articles
tags:
  - constrained port-hamiltonian systems, control by interconnection, model predictive control, primal–dual gradient method
---
 
## Authors
[T.H. Pham](authors/thanh-hung-pham), [N.M.T. Vu](authors/ngoc-minh-trang-vu), [I. Prodan](authors/ionela-prodan), [L. Lefèvre](authors/laurent-lefevre)
 
## Abstract
This paper proposes a Control by Interconnection design, for a class of constrained Port-Hamiltonian systems, which is based on an associated Model Predictive Control optimization problem. This associated optimization problem allows to consider both state and input constraints simultaneously. Based on the first order Karush–Kuhn–Tucker optimality condition, the primal–dual gradient method is then used to build a passive feedback controller, derived from the MPC-induced optimization problem. The resulting passive controller is coupled with the original Port-Hamiltonian system through a power-preserving interconnection, in order to guarantee both the closed-loop stability and constraints satisfaction, but not the optimality anymore. Comments on parameters tuning for the proposed control design, together with validations of the approach through simulations first on a linear LC circuit, then on a nonlinear Permanent Magnet Synchronous Motor and comparisons with a classical MPC design, are provided to discuss the effectiveness of the approach.
 
## Keywords
constrained port-hamiltonian systems, control by interconnection, model predictive control, primal–dual gradient method
 
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
  journal={Systems \&amp; Control Letters},
  publisher={Elsevier BV},
  author={Pham, T.H. and Vu, N.M.T. and Prodan, I. and Lefèvre, L.},
  year={2022},
  pages={105336}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-combined-control-by-interconnection-model-predictive-control-design-for-constrained-port-hamiltonian-systems.bib)
 
## References
- Maschke, Port-controlled Hamiltonian systems: Modelling origins and system theoretic properties. (1993)
- [van der Schaft A (2020) Port-Hamiltonian Modeling for Control. Annu Rev Control Robot Auton Syst 3(1):393–416. https://doi.org/10.1146/annurev-control-081219-09225](port-hamiltonian-modeling-for-control) -- [10.1146/annurev-control-081219-092250](https://doi.org/10.1146/annurev-control-081219-092250)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Ortega R, van der Schaft A, Castanos F, Astolfi A (2008) Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans Automat Contr 53(11):2527–2542. https://doi.org/10.1109/tac.2008.200693](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- [Borja P, Cisneros R, Ortega R (2016) A constructive procedure for energy shaping of port—Hamiltonian systems. Automatica 72:230–234. https://doi.org/10.1016/j.automatica.2016.05.02](a-constructive-procedure-for-energy-shaping-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2016.05.028](https://doi.org/10.1016/j.automatica.2016.05.028)
- Ortega R, García-Canseco E (2004) Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10(5):432–450. https://doi.org/10.3166/ejc.10.432-45 -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- [Wang Z-M, Wei A, Zong G, Zhao X, Li H (2020) Finite-time stabilization and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si5.svg"><mml:msub><mml:mi mathvariant="bold-script">H</mml:mi><mml:mi>∞</mml:mi></mml:msub></mml:math> control for a class of switched nonlinear port-controlled Hamiltonian systems subject to actuator saturation. Journal of the Franklin Institute 357(16):11807–11829. https://doi.org/10.1016/j.jfranklin.2019.11.05](finite-time-stabilization-andh-control-for-a-class-of-switched-nonlinear-port-controlled-hamiltonian-systems-subject-to-actuator-saturation) -- [10.1016/j.jfranklin.2019.11.055](https://doi.org/10.1016/j.jfranklin.2019.11.055)
- [Stegink T, De Persis C, van der Schaft A (2017) A Unifying Energy-Based Approach to Stability of Power Grids With Market Dynamics. IEEE Trans Automat Contr 62(6):2612–2622. https://doi.org/10.1109/tac.2016.261390](a-unifying-energy-based-approach-to-stability-of-power-grids-with-market-dynamics) -- [10.1109/tac.2016.2613901](https://doi.org/10.1109/tac.2016.2613901)
- [Benedito E, del Puerto-Flores D, Dòria-Cerezo A, Scherpen JMA (2019) Port-Hamiltonian based Optimal Power Flow algorithm for multi-terminal DC networks. Control Engineering Practice 83:141–150. https://doi.org/10.1016/j.conengprac.2018.10.01](port-hamiltonian-based-optimal-power-flow-algorithm-for-multi-terminal-dc-networks) -- [10.1016/j.conengprac.2018.10.018](https://doi.org/10.1016/j.conengprac.2018.10.018)
- van der Schaft, (2000)
- [Wu Y, Hamroun B, Le Gorrec Y, Maschke B (2021) Reduced Order LQG Control Design for Infinite Dimensional Port Hamiltonian Systems. IEEE Trans Automat Contr 66(2):865–871. https://doi.org/10.1109/tac.2020.299737](reduced-order-lqg-control-design-for-infinite-dimensional-port-hamiltonian-systems) -- [10.1109/tac.2020.2997373](https://doi.org/10.1109/tac.2020.2997373)
- [Stegink TW, Persis CD, van der Schaft AJ (2015) Port-Hamiltonian Formulation of the Gradient Method Applied to Smart Grids. IFAC-PapersOnLine 48(13):13–18. https://doi.org/10.1016/j.ifacol.2015.10.20](port-hamiltonian-formulation-of-the-gradient-method-applied-to-smart-grids) -- [10.1016/j.ifacol.2015.10.207](https://doi.org/10.1016/j.ifacol.2015.10.207)
- [Kölsch L, Jané Soneira P, Strehle F, Hohmann S (2021) Optimal control of port-Hamiltonian systems: A continuous-time learning approach. Automatica 130:109725. https://doi.org/10.1016/j.automatica.2021.10972](optimal-control-of-port-hamiltonian-systems-a-continuous-time-learning-approach) -- [10.1016/j.automatica.2021.109725](https://doi.org/10.1016/j.automatica.2021.109725)
- Gao, Optimal control of the hydraulic actuated boom system based on port-Hamiltonian formulation. (2020)
- Mayne DQ (2014) Model predictive control: Recent developments and future promise. Automatica 50(12):2967–2986. https://doi.org/10.1016/j.automatica.2014.10.12 -- [10.1016/j.automatica.2014.10.128](https://doi.org/10.1016/j.automatica.2014.10.128)
- Falugi, Model predictive control: A passive scheme. (2014)
- Pangborn, Passivity and decentralized MPC of switched graph-based power flow systems. (2018)
- Yoshida K, Inoue M, Hatanaka T (2019) Instant MPC for Linear Systems and Dissipativity-Based Stability Analysis. IEEE Control Syst Lett 3(4):811–816. https://doi.org/10.1109/lcsys.2019.291809 -- [10.1109/lcsys.2019.2918095](https://doi.org/10.1109/lcsys.2019.2918095)
- Arrow, (1958)
- Boyd, (2004)
- Rawlings, (2009)
- Kotyczka, Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems Control Lett. (2019)
- [Venkatraman A, van der Schaft AJ (2010) Full-order observer design for a class of port-Hamiltonian systems. Automatica 46(3):555–561. https://doi.org/10.1016/j.automatica.2010.01.01](full-order-observer-design-for-a-class-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2010.01.019](https://doi.org/10.1016/j.automatica.2010.01.019)
- [Vincent B, Hudon N, Lefèvre L, Dochain D (2016) Port-Hamiltonian observer design for plasma profile estimation in tokamaks. IFAC-PapersOnLine 49(24):93–98. https://doi.org/10.1016/j.ifacol.2016.10.76](port-hamiltonian-observer-design-for-plasma-profile-estimation-in-tokamaks) -- [10.1016/j.ifacol.2016.10.761](https://doi.org/10.1016/j.ifacol.2016.10.761)
- Pfeifer, (2021)
- Aguilera, On stability and performance of finite control set MPC for power converters. (2011)

