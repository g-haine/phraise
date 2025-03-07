---
layout: post
title: "Distributed Control and Optimization of DC Microgrids: A Port-Hamiltonian Approach"
date: 2022-06-15 00:00:00 +0100
permalink: distributed-control-and-optimization-of-dc-microgrids-a-port-hamiltonian-approach
year: 2022
authors: Babak Abdolmaleki, Gilbert Bergna-Diaz
category: articles
---
 
## Authors
[Babak Abdolmaleki](authors/babak-abdolmaleki), [Gilbert Bergna-Diaz](authors/gilbert-bergna-diaz)
 
## Abstract
This article proposes a distributed secondary control scheme that drives a dc microgrid to an equilibrium point where the generators share optimal currents, and their voltages have a weighted average of nominal value. The scheme does not rely on the electric system topology nor its specifications; it guarantees plug-and-play design and functionality of the generators. First, the incremental model of the microgrid system with constant impedance, current, and power devices is shown to admit a port-Hamiltonian (pH) representation, and its passive output is determined. The economic dispatch problem is then solved by the Lagrange multipliers method; the Karush-Kuhn-Tucker conditions and weighted-average formation of voltages are then formulated as the control objectives. We propose a control scheme that is based on the Control by Interconnection design philosophy, where the consensus-based controller is viewed as a virtual pH system to be interconnected with the physical one. We prove the regional asymptotic stability of the closed-loop system using Lyapunov and LaSalle theorems. Equilibrium analysis is also conducted based on the concepts of graph theory and economic dispatch. Finally, the effectiveness of the presented scheme for different case studies is validated with a test microgrid system, simulated in both MATLAB/Simulink and OPAL-RT environments.
 
## Citation
- **Journal:** IEEE Access
- **Year:** 2022
- **Volume:** 10
- **Issue:** 
- **Pages:** 64222--64233
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/ACCESS.2022.3183209](https://doi.org/10.1109/ACCESS.2022.3183209)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Abdolmaleki_2022,
  title={{Distributed Control and Optimization of DC Microgrids: A Port-Hamiltonian Approach}},
  volume={10},
  ISSN={2169-3536},
  DOI={10.1109/access.2022.3183209},
  journal={IEEE Access},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Abdolmaleki, Babak and Bergna-Diaz, Gilbert},
  year={2022},
  pages={64222--64233}
}
{% endraw %}
{% endhighlight %}
 
## References
- Hatziargyriou, N., Asano, H., Iravani, R. & Marnay, C. Microgrids. IEEE Power and Energy Magazine vol. 5 78–94 (2007) -- [10.1109/MPAE.2007.376583](https://doi.org/10.1109/MPAE.2007.376583)
- Abdolmaleki, B., Shafiee, Q., Arefi, M. M. & Dragicevic, T. An Instantaneous Event-Triggered Hz–Watt Control for Microgrids. IEEE Transactions on Power Systems vol. 34 3616–3625 (2019) -- [10.1109/TPWRS.2019.2904579](https://doi.org/10.1109/TPWRS.2019.2904579)
- Meng, L. et al. Review on Control of DC Microgrids. IEEE Journal of Emerging and Selected Topics in Power Electronics 1–1 (2017) doi:10.1109/jestpe.2017.2690219 -- [10.1109/JESTPE.2017.2690219](https://doi.org/10.1109/JESTPE.2017.2690219)
- Albea-Sánchez, C. Hybrid dynamical control based on consensus algorithms for current sharing in DC-bus microgrids. Nonlinear Analysis: Hybrid Systems vol. 39 100972 (2021) -- [10.1016/j.nahs.2020.100972](https://doi.org/10.1016/j.nahs.2020.100972)
- Han, Y., Ning, X., Yang, P. & Xu, L. Review of Power Sharing, Voltage Restoration and Stabilization Techniques in Hierarchical Controlled DC Microgrids. IEEE Access vol. 7 149202–149223 (2019) -- [10.1109/ACCESS.2019.2946706](https://doi.org/10.1109/ACCESS.2019.2946706)
- Molzahn, D. K. et al. A Survey of Distributed Optimization and Control Algorithms for Electric Power Systems. IEEE Transactions on Smart Grid vol. 8 2941–2962 (2017) -- [10.1109/TSG.2017.2720471](https://doi.org/10.1109/TSG.2017.2720471)
- Nasirian, V., Moayedi, S., Davoudi, A. & Lewis, F. L. Distributed Cooperative Control of DC Microgrids. IEEE Transactions on Power Electronics vol. 30 2288–2303 (2015) -- [10.1109/TPEL.2014.2324579](https://doi.org/10.1109/TPEL.2014.2324579)
- Sahoo, S. & Mishra, S. An Adaptive Event-Triggered Communication-Based Distributed Secondary Control for DC Microgrids. IEEE Transactions on Smart Grid vol. 9 6674–6683 (2018) -- [10.1109/TSG.2017.2717936](https://doi.org/10.1109/TSG.2017.2717936)
- Sahoo, S. & Mishra, S. A Distributed Finite-Time Secondary Average Voltage Regulation and Current Sharing Controller for DC Microgrids. IEEE Transactions on Smart Grid vol. 10 282–292 (2019) -- [10.1109/TSG.2017.2737938](https://doi.org/10.1109/TSG.2017.2737938)
- Abdolmaleki, B., Shafiee, Q., Sadabadi, M. S. & Dragicevic, T. Economical Secondary Control of DC Microgrids. 2020 IEEE 11th International Symposium on Power Electronics for Distributed Generation Systems (PEDG) 304–308 (2020) doi:10.1109/pedg48541.2020.9244360 -- [10.1109/PEDG48541.2020.9244360](https://doi.org/10.1109/PEDG48541.2020.9244360)
- Peng, J., Fan, B. & Liu, W. Voltage-Based Distributed Optimal Control for Generation Cost Minimization and Bounded Bus Voltage Regulation in DC Microgrids. IEEE Transactions on Smart Grid vol. 12 106–116 (2021) -- [10.1109/TSG.2020.3013303](https://doi.org/10.1109/TSG.2020.3013303)
- Peng, J., Fan, B., Yang, Q. & Liu, W. Distributed Event-Triggered Control of DC Microgrids. IEEE Systems Journal vol. 15 2504–2514 (2021) -- [10.1109/JSYST.2020.2994532](https://doi.org/10.1109/JSYST.2020.2994532)
- Han, R., Meng, L., Guerrero, J. M. & Vasquez, J. C. Distributed Nonlinear Control With Event-Triggered Communication to Achieve Current-Sharing and Voltage Regulation in DC Microgrids. IEEE Transactions on Power Electronics vol. 33 6416–6433 (2018) -- [10.1109/TPEL.2017.2749518](https://doi.org/10.1109/TPEL.2017.2749518)
- Han, R., Wang, H., Jin, Z., Meng, L. & Guerrero, J. M. Compromised Controller Design for Current Sharing and Voltage Regulation in DC Microgrid. IEEE Transactions on Power Electronics vol. 34 8045–8061 (2019) -- [10.1109/TPEL.2018.2878084](https://doi.org/10.1109/TPEL.2018.2878084)
- Sahoo, S., Pullaguram, D., Mishra, S., Wu, J. & Senroy, N. A containment based distributed finite-time controller for bounded voltage regulation &amp; proportionate current sharing in DC microgrids. Applied Energy vol. 228 2526–2538 (2018) -- [10.1016/j.apenergy.2018.06.081](https://doi.org/10.1016/j.apenergy.2018.06.081)
- Cucuzzella, M., Trip, S. & Scherpen, J. A Consensus-Based Controller for DC Power Networks. IFAC-PapersOnLine vol. 51 205–210 (2018) -- [10.1016/j.ifacol.2018.12.092](https://doi.org/10.1016/j.ifacol.2018.12.092)
- Cucuzzella, M., Kosaraju, K. C. & Scherpen, J. M. A. Distributed Passivity-Based Control of DC Microgrids. 2019 American Control Conference (ACC) 652–657 (2019) doi:10.23919/acc.2019.8814756 -- [10.23919/ACC.2019.8814756](https://doi.org/10.23919/ACC.2019.8814756)
- Trip, S. et al. Distributed Averaging Control for Voltage Regulation and Current Sharing in DC Microgrids: Modelling and Experimental Validation. IFAC-PapersOnLine vol. 51 242–247 (2018) -- [10.1016/j.ifacol.2018.12.042](https://doi.org/10.1016/j.ifacol.2018.12.042)
- Trip, S., Cucuzzella, M., Cheng, X. & Scherpen, J. Distributed Averaging Control for Voltage Regulation and Current Sharing in DC Microgrids. IEEE Control Systems Letters vol. 3 174–179 (2019) -- [10.1109/LCSYS.2018.2857559](https://doi.org/10.1109/LCSYS.2018.2857559)
- Silani, A., Cucuzzella, M., Scherpen, J. M. A. & Yazdanpanah, M. J. Passivity properties for regulation of DC networks with stochastic load demand. IFAC-PapersOnLine vol. 53 13113–13118 (2020) -- [10.1016/j.ifacol.2020.12.2274](https://doi.org/10.1016/j.ifacol.2020.12.2274)
- Trip, S., Cucuzzella, M., De Persis, C., Cheng, X. & Ferrara, A. Sliding Modes for Voltage Regulation and Current Sharing in DC Microgrids. 2018 Annual American Control Conference (ACC) 6778–6783 (2018) doi:10.23919/acc.2018.8431082 -- [10.23919/ACC.2018.8431082](https://doi.org/10.23919/ACC.2018.8431082)
- Cucuzzella, M. et al. A Robust Consensus Algorithm for Current Sharing and Voltage Regulation in DC Microgrids. IEEE Transactions on Control Systems Technology vol. 27 1583–1595 (2019) -- [10.1109/TCST.2018.2834878](https://doi.org/10.1109/TCST.2018.2834878)
- Nahata, P. & Ferrari-Trecate, G. On Existence of Equilibria, Voltage Balancing, and Current Sharing in Consensus-Based DC Microgrids. 2020 European Control Conference (ECC) 1216–1223 (2020) doi:10.23919/ecc51009.2020.9143766 -- [10.23919/ECC51009.2020.9143766](https://doi.org/10.23919/ECC51009.2020.9143766)
- Nahata, P., Turan, M. S. & Ferrari-Trecate, G. Consensus-Based Current Sharing and Voltage Balancing in DC Microgrids With Exponential Loads. IEEE Transactions on Control Systems Technology vol. 30 1668–1680 (2022) -- [10.1109/TCST.2021.3120321](https://doi.org/10.1109/TCST.2021.3120321)
- Sadabadi, M. S. A Distributed Control Strategy for Parallel DC-DC Converters. IEEE Control Systems Letters vol. 5 1231–1236 (2021) -- [10.1109/LCSYS.2020.3025411](https://doi.org/10.1109/LCSYS.2020.3025411)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Fu, B., Li, S., Wang, X. & Guo, L. Output feedback based simultaneous stabilization of two Port-controlled Hamiltonian systems with disturbances. Journal of the Franklin Institute vol. 356 8154–8166 (2019) -- [10.1016/j.jfranklin.2019.02.039](https://doi.org/10.1016/j.jfranklin.2019.02.039)
- Fu, B., Wang, X. & Wang, Q. Protocol design for group output consensus of disturbed port-controlled Hamiltonian multi-agent systems. Journal of the Franklin Institute vol. 358 9867–9889 (2021) -- [10.1016/j.jfranklin.2021.10.006](https://doi.org/10.1016/j.jfranklin.2021.10.006)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 53 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/TAC.2008.2006930](https://doi.org/10.1109/TAC.2008.2006930)
- Putting energy back in control. IEEE Control Systems vol. 21 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- Boyd, S. & Vandenberghe, L. Convex Optimization. (2004) doi:10.1017/cbo9780511804441 -- [10.1017/CBO9780511804441](https://doi.org/10.1017/CBO9780511804441)
- Abdolmaleki, B. & Shafiee, Q. Online Kron Reduction for Economical Frequency Control of Microgrids. IEEE Transactions on Industrial Electronics vol. 67 8461–8471 (2020) -- [10.1109/TIE.2019.2950860](https://doi.org/10.1109/TIE.2019.2950860)
- Olfati-Saber, R., Fax, J. A. & Murray, R. M. Consensus and Cooperation in Networked Multi-Agent Systems. Proceedings of the IEEE vol. 95 215–233 (2007) -- [10.1109/JPROC.2006.887293](https://doi.org/10.1109/JPROC.2006.887293)
- Abdolmaleki, B., Shafiee, Q., Seifi, A. R., Arefi, M. M. & Blaabjerg, F. A Zeno-Free Event-Triggered Secondary Control for AC Microgrids. IEEE Transactions on Smart Grid vol. 11 1905–1916 (2020) -- [10.1109/TSG.2019.2945250](https://doi.org/10.1109/TSG.2019.2945250)
- Sadabadi, M. S., Shafiee, Q. & Karimi, A. Plug-and-Play Robust Voltage Control of DC Microgrids. IEEE Transactions on Smart Grid vol. 9 6886–6896 (2018) -- [10.1109/TSG.2017.2728319](https://doi.org/10.1109/TSG.2017.2728319)
- Fridman, E. Introduction to Time-Delay Systems. Systems &amp; Control: Foundations &amp; Applications (Springer International Publishing, 2014). doi:10.1007/978-3-319-09393-2 -- [10.1007/978-3-319-09393-2](https://doi.org/10.1007/978-3-319-09393-2)
- Yang, T., Sun, N. & Fang, Y. Adaptive Fuzzy Control for a Class of MIMO Underactuated Systems With Plant Uncertainties and Actuator Deadzones: Design and Experiments. IEEE Transactions on Cybernetics vol. 52 8213–8226 (2022) -- [10.1109/TCYB.2021.3050475](https://doi.org/10.1109/TCYB.2021.3050475)
- Yang, T., Sun, N. & Fang, Y. Neuroadaptive Control for Complicated Underactuated Systems With Simultaneous Output and Velocity Constraints Exerted on Both Actuated and Unactuated States. IEEE Transactions on Neural Networks and Learning Systems vol. 34 4488–4498 (2023) -- [10.1109/TNNLS.2021.3115960](https://doi.org/10.1109/TNNLS.2021.3115960)

