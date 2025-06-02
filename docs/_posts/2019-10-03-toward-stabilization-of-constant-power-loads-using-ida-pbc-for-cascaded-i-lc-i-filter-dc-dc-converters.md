---
layout: post
title: "Toward Stabilization of Constant Power Loads Using IDA-PBC for Cascaded <i>LC</i> Filter DC/DC Converters"
date: 2019-10-03 00:00:00 +0100
permalink: toward-stabilization-of-constant-power-loads-using-ida-pbc-for-cascaded-i-lc-i-filter-dc-dc-converters
year: 2021
authors: Shengzhao Pang, Babak Nahid-Mobarakeh, Serge Pierfederici, Yigeng Huangfu, Guangzhao Luo, Fei Gao
category: articles
---
 
## Authors
[Shengzhao Pang](authors/shengzhao-pang), [Babak Nahid-Mobarakeh](authors/babak-nahid-mobarakeh), [Serge Pierfederici](authors/serge-pierfederici), [Yigeng Huangfu](authors/yigeng-huangfu), [Guangzhao Luo](authors/guangzhao-luo), [Fei Gao](authors/fei-gao)
 
## Abstract
This article proposes a modified interconnection and damping assignment passivity-based control (IDA-PBC) for dc/dc converter cascaded with an LC filter. The plant is modeled using the port-controlled Hamiltonian (PCH) form. The main objective is to stabilize the cascaded system in case the system supplies constant power load (CPL). To solve the instability issues caused by tightly controlled cascaded systems, the IDA-PBC based on an overall PCH model, including LC input filter and dc/dc converter, is established. Moreover, to ensure that the proposed IDA-PBC admits one unique solution, an adaptive interconnection matrix is designed to build the internal links in the PCH model. Furthermore, in order to improve the implementation on an onboard dc microgrid application with time-varying CPLs, a modified IDA-PBC algorithm is proposed based on the error between the state vector and the desired operating point, which might be variable. The closed-loop Hamiltonian function is chosen as the Lyapunov candidate function to guarantee that the system operates in a stable manner. The virtual damping assignment technique is addressed to tune the dynamic characteristic of the closed-loop system. Simulation and experimental results are carried out to illustrate the proposed method’s effectiveness.
 
## Citation
- **Journal:** IEEE Journal of Emerging and Selected Topics in Power Electronics
- **Year:** 2021
- **Volume:** 9
- **Issue:** 2
- **Pages:** 1302--1314
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/jestpe.2019.2945331](https://doi.org/10.1109/jestpe.2019.2945331)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Pang_2021,
  title={{Toward Stabilization of Constant Power Loads Using IDA-PBC for Cascaded LC Filter DC/DC Converters}},
  volume={9},
  ISSN={2168-6785},
  DOI={10.1109/jestpe.2019.2945331},
  number={2},
  journal={IEEE Journal of Emerging and Selected Topics in Power Electronics},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Pang, Shengzhao and Nahid-Mobarakeh, Babak and Pierfederici, Serge and Huangfu, Yigeng and Luo, Guangzhao and Gao, Fei},
  year={2021},
  pages={1302--1314}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/toward-stabilization-of-constant-power-loads-using-ida-pbc-for-cascaded-i-lc-i-filter-dc-dc-converters.bib)
 
## References
- [Meng, Y., Shang, S., Zhang, H., Cui, Y. & Wang, X. IDA‐PB control with integral action of Y‐connected modular multilevel converter for fractional frequency transmission application. IET Generation Trans &amp;amp; Dist 12, 3385–3397 (2017)](ida-pb-control-with-integral-action-of-y-connected-modular-multilevel-converter-for-fractional-frequency-transmission-application) -- [10.1049/iet-gtd.2017.0573](https://doi.org/10.1049/iet-gtd.2017.0573)
- Gui, Y., Wei, B., Li, M., Guerrero, J. M. & Vasquez, J. C. Passivity-based coordinated control for islanded AC microgrid. Applied Energy 229, 551–561 (2018) -- [10.1016/j.apenergy.2018.07.115](https://doi.org/10.1016/j.apenergy.2018.07.115)
- [Zeng, J., Zhang, Z. & Qiao, W. An Interconnection and Damping Assignment Passivity-Based Controller for a DC–DC Boost Converter With a Constant Power Load. IEEE Trans. on Ind. Applicat. 50, 2314–2322 (2014)](an-interconnection-and-damping-assignment-passivity-based-controller-for-a-dc-dc-boost-converter-with-a-constant-power-load) -- [10.1109/tia.2013.2290872](https://doi.org/10.1109/tia.2013.2290872)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- [Zhang, Q. & Liu, G. Precise Control of Elastic Joint Robot Using an Interconnection and Damping Assignment Passivity-Based Approach. IEEE/ASME Trans. Mechatron. 21, 2728–2736 (2016)](precise-control-of-elastic-joint-robot-using-an-interconnection-and-damping-assignment-passivity-based-approach) -- [10.1109/tmech.2016.2578287](https://doi.org/10.1109/tmech.2016.2578287)
- [Meshram, R. V. et al. Port-Controlled Phasor Hamiltonian Modeling and IDA-PBC Control of Solid-State Transformer. IEEE Trans. Contr. Syst. Technol. 27, 161–174 (2019)](port-controlled-phasor-hamiltonian-modeling-and-ida-pbc-control-of-solid-state-transformer) -- [10.1109/tcst.2017.2761866](https://doi.org/10.1109/tcst.2017.2761866)
- Huangfu, Y. et al. Analysis and Design of an Active Stabilizer for a Boost Power Converter System. Energies 9, 934 (2016) -- [10.3390/en9110934](https://doi.org/10.3390/en9110934)
- Hassan, M. A. et al. Adaptive Passivity-Based Control of dc–dc Buck Power Converter With Constant Power Load in DC Microgrid Systems. IEEE J. Emerg. Sel. Topics Power Electron. 7, 2029–2040 (2019) -- [10.1109/jestpe.2018.2874449](https://doi.org/10.1109/jestpe.2018.2874449)
- Areerak, K. et al. Adaptive Stabilization of Uncontrolled Rectifier Based AC–DC Power Systems Feeding Constant Power Loads. IEEE Trans. Power Electron. 33, 8927–8935 (2018) -- [10.1109/tpel.2017.2779541](https://doi.org/10.1109/tpel.2017.2779541)
- [Pang, S. et al. Interconnection and Damping Assignment Passivity-Based Control Applied to On-Board DC–DC Power Converter System Supplying Constant Power Load. IEEE Trans. on Ind. Applicat. 55, 6476–6485 (2019)](interconnection-and-damping-assignment-passivity-based-control-applied-to-on-board-dc-dc-power-converter-system-supplying-constant-power-load) -- [10.1109/tia.2019.2938149](https://doi.org/10.1109/tia.2019.2938149)
- [Pang, S. et al. IDA-Passivity-Based Control for On-board DC Power Converter System with Constant Power Load. 2018 IEEE Industry Applications Society Annual Meeting (IAS) 1–6 (2018) doi:10.1109/ias.2018.8544662](ida-passivity-based-control-for-on-board-dc-power-converter-system-with-constant-power-load) -- [10.1109/ias.2018.8544662](https://doi.org/10.1109/ias.2018.8544662)
- Vafamand, N., Khooban, M. H., Dragicevic, T. & Blaabjerg, F. Networked Fuzzy Predictive Control of Power Buffers for Dynamic Stabilization of DC Microgrids. IEEE Trans. Ind. Electron. 66, 1356–1362 (2019) -- [10.1109/tie.2018.2826485](https://doi.org/10.1109/tie.2018.2826485)
- Yousefizadeh, S. et al. EKF-Based Predictive Stabilization of Shipboard DC Microgrids With Uncertain Time-Varying Load. IEEE J. Emerg. Sel. Topics Power Electron. 7, 901–909 (2019) -- [10.1109/jestpe.2018.2889971](https://doi.org/10.1109/jestpe.2018.2889971)
- Zhang, M. et al. Voltage Stability Analysis and Sliding-Mode Control Method for Rectifier in DC Systems With Constant Power Loads. IEEE J. Emerg. Sel. Topics Power Electron. 5, 1621–1630 (2017) -- [10.1109/jestpe.2017.2723482](https://doi.org/10.1109/jestpe.2017.2723482)
- Vafamand, N., Khooban, M. H., Dragicevic, T., Blaabjerg, F. & Boudjadar, J. Robust Non-Fragile Fuzzy Control of Uncertain DC Microgrids Feeding Constant Power Loads. IEEE Trans. Power Electron. 34, 11300–11308 (2019) -- [10.1109/tpel.2019.2896019](https://doi.org/10.1109/tpel.2019.2896019)
- Vafamand, N., Khayatian, A. & Khooban, M. H. Stabilisation and transient performance improvement of DC MGs with CPLs: non‐linear reset control approach. IET Generation Trans &amp;amp; Dist 13, 3169–3176 (2019) -- [10.1049/iet-gtd.2018.6739](https://doi.org/10.1049/iet-gtd.2018.6739)
- Cisneros, R., Mancilla-David, F. & Ortega, R. Passivity-Based Control of a Grid-Connected Small-Scale Windmill With Limited Control Authority. IEEE J. Emerg. Sel. Topics Power Electron. 1, 247–259 (2013) -- [10.1109/jestpe.2013.2285376](https://doi.org/10.1109/jestpe.2013.2285376)
- Herrera, L., Zhang, W. & Wang, J. Stability Analysis and Controller Design of DC Microgrids With Constant Power Loads. IEEE Trans. Smart Grid 1–1 (2015) doi:10.1109/tsg.2015.2457909 -- [10.1109/tsg.2015.2457909](https://doi.org/10.1109/tsg.2015.2457909)
- Xu, R. et al. A Novel Control Method for Transformerless H-Bridge Cascaded STATCOM With Star Configuration. IEEE Trans. Power Electron. 30, 1189–1202 (2015) -- [10.1109/tpel.2014.2320251](https://doi.org/10.1109/tpel.2014.2320251)
- Xu, H. et al. Analysis, Comparison, and Discussion of Control Strategies for Dual Stator-Winding Induction Generator DC Generating System. IEEE J. Emerg. Sel. Topics Power Electron. 4, 1007–1014 (2016) -- [10.1109/jestpe.2015.2497272](https://doi.org/10.1109/jestpe.2015.2497272)
- Wang, K.-W., Zhang, X. & Chung, H. S.-H. Solid-State Single-Port Series Damping Device for Power Converters in DC Microgrid Systems. IEEE Trans. Power Electron. 34, 192–203 (2019) -- [10.1109/tpel.2018.2811941](https://doi.org/10.1109/tpel.2018.2811941)
- Petrovic, V., Ortega, R. & Stankovi, A. M. Interconnection and damping assignment approach to control of PM synchronous motors. IEEE Trans. Contr. Syst. Technol. 9, 811–820 (2001) -- [10.1109/87.960344](https://doi.org/10.1109/87.960344)
- [Pang, S. et al. IDA-Passivity-Based Control for Boost Converter with LC Filter Supplying Constant Power Load. 2018 IEEE International Conference on Electrical Systems for Aircraft, Railway, Ship Propulsion and Road Vehicles &amp; International Transportation Electrification Conference (ESARS-ITEC) 1–6 (2018) doi:10.1109/esars-itec.2018.8607674](ida-passivity-based-control-for-boost-converter-with-lc-filter-supplying-constant-power-load) -- [10.1109/esars-itec.2018.8607674](https://doi.org/10.1109/esars-itec.2018.8607674)
- Bai, H., Wang, X., Blaabjerg, F. & Loh, P. C. Harmonic Analysis and Mitigation of Low-Frequency Switching Voltage Source Inverter With Auxiliary VSI. IEEE J. Emerg. Sel. Topics Power Electron. 6, 1355–1365 (2018) -- [10.1109/jestpe.2018.2789982](https://doi.org/10.1109/jestpe.2018.2789982)
- Huangfu, Y. et al. Stability Analysis and Active Stabilization of On-board DC Power Converter System with Input Filter. IEEE Trans. Ind. Electron. 65, 790–799 (2018) -- [10.1109/tie.2017.2703663](https://doi.org/10.1109/tie.2017.2703663)
- Gao, F., Bozhko, S., Asher, G., Wheeler, P. & Patel, C. An Improved Voltage Compensation Approach in A Droop-Controlled DC Power System for the More Electric Aircraft. IEEE Trans. Power Electron. 1–1 (2015) doi:10.1109/tpel.2015.2510285 -- [10.1109/tpel.2015.2510285](https://doi.org/10.1109/tpel.2015.2510285)
- Pang, S. et al. Fault-tolerant consideration and active stabilization for floating interleaved boost converter system. IECON 2017 - 43rd Annual Conference of the IEEE Industrial Electronics Society 7947–7952 (2017) doi:10.1109/iecon.2017.8217393 -- [10.1109/iecon.2017.8217393](https://doi.org/10.1109/iecon.2017.8217393)
- Yousefizadeh, S. et al. Tracking Control for a DC Microgrid Feeding Uncertain Loads in More Electric Aircraft: Adaptive Backstepping Approach. IEEE Trans. Ind. Electron. 66, 5644–5652 (2019) -- [10.1109/tie.2018.2880666](https://doi.org/10.1109/tie.2018.2880666)
- Adamou-Mitiche, A. B. H. & Mitiche, L. Multivariable Systems Model Reduction Based on the Dominant Modes and Genetic Algorithm. IEEE Trans. Ind. Electron. 64, 1617–1619 (2017) -- [10.1109/tie.2016.2618783](https://doi.org/10.1109/tie.2016.2618783)
- Du, W., Zhang, J., Zhang, Y. & Qian, Z. Stability Criterion for Cascaded System With Constant Power Load. IEEE Trans. Power Electron. 28, 1843–1851 (2013) -- [10.1109/tpel.2012.2211619](https://doi.org/10.1109/tpel.2012.2211619)
- Chang, Y.-C., Chen, C.-H., Zhu, Z.-C. & Huang, Y.-W. Speed Control of the Surface-Mounted Permanent-Magnet Synchronous Motor Based on Takagi–Sugeno Fuzzy Models. IEEE Trans. Power Electron. 31, 6504–6510 (2016) -- [10.1109/tpel.2015.2504392](https://doi.org/10.1109/tpel.2015.2504392)
- [Pang, S. et al. Improving the Stability of Cascaded DC-DC Converter Systems via the Viewpoints of Passivity-Based Control and Port-Controlled Hamiltonian Framework. 2019 IEEE Industry Applications Society Annual Meeting 1–6 (2019) doi:10.1109/ias.2019.8911961](improving-the-stability-of-cascaded-dc-dc-converter-systems-via-the-viewpoints-of-passivity-based-control-and-port-controlled-hamiltonian-framework) -- [10.1109/ias.2019.8911961](https://doi.org/10.1109/ias.2019.8911961)
- Loop, B. P., Sudhoff, S. D., Zak, S. H. & Zivi, E. L. Estimating Regions of Asymptotic Stability of Power Electronics Systems Using Genetic Algorithms. IEEE Trans. Contr. Syst. Technol. 18, 1011–1022 (2010) -- [10.1109/tcst.2009.2031325](https://doi.org/10.1109/tcst.2009.2031325)
- Gu, Y., Li, W. & He, X. Passivity-Based Control of DC Microgrid for Self-Disciplined Stabilization. IEEE Trans. Power Syst. 30, 2623–2632 (2015) -- [10.1109/tpwrs.2014.2360300](https://doi.org/10.1109/tpwrs.2014.2360300)
- khalil, Nonlinear Systems (2002)

