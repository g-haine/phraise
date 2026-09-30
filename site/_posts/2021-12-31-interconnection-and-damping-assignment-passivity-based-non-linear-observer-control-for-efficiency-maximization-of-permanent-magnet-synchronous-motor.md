---
title: "Interconnection and damping assignment passivity-based non-linear observer control for efficiency maximization of permanent magnet synchronous motor"
date: 2021-12-31 00:00:00 +0100
permalink: interconnection-and-damping-assignment-passivity-based-non-linear-observer-control-for-efficiency-maximization-of-permanent-magnet-synchronous-motor
year: 2022
authors: Youcef Belkhier, Abdelyazid Achour, Miroslav Bures, Nasim Ullah, Mohit Bajaj, Hossam M. Zawbaa, Salah Kamel
category: articles
tags:
  - Passivity-based control
  - Interconnection and damping assignment
  - Permanent magnet synchronous motor
  - Non-linear observer
---
 
## Authors
[Youcef Belkhier](authors/youcef-belkhier), [Abdelyazid Achour](authors/abdelyazid-achour), [Miroslav Bures](authors/miroslav-bures), [Nasim Ullah](authors/nasim-ullah), [Mohit Bajaj](authors/mohit-bajaj), [Hossam M. Zawbaa](authors/hossam-m-zawbaa), [Salah Kamel](authors/salah-kamel)
 
## Abstract
The permanent magnet synchronous motor (PMSM) has several advantages over the DC motor and is gradually replacing it in the industry. The dynamics of the PMSM are described by non-linear equations; it is sensitive to unknown external disturbances (load), and its characteristics vary over time. All of these restrictions complicate the control task. Non-linear controls are required to adjust for non-linearities and the drawbacks mentioned above. This paper investigates an interconnection and damping assignment (IDA) passivity-based control (PBC) combined with a non-linear observer approach for the PMSM using the model represented in the dq-frame. The IDA-PBC approach has the inherent benefit of not canceling non-linear features but compensating them in a damped manner. The suggested PBC is in charge of creating the intended dynamic of the system, while the non-linear observer is in charge of reconstructing the recorded signals in order to compel the PMSM to track speed. The primary objective of this study is to synthesize the controller while accounting for the whole dynamic of the PMSM and making the system passive. It is performed by restructuring the energy of the proposed strategy and introducing a damping component that addresses the non-linear elements in a damped instead of deleted way, so providing a duality concept between both the IDA-PBC and the observer There are three methods for computing IDA-PBC: parametric, nonparametric, and algebraic. The parameterized IDA-PBC method is used to control the speed of the PMSM. This method uses the energy function in parameterized closed-loop in terms of some functions depending on the system’s state vector, such that the energy formation step is satisfied. Then, the original port-controlled Hamiltonian (PCH) dynamics in open-loop (OL) are equalized with the desired one in closed-loop (CL). The equalization process allows obtaining a set of solutions of the partial differential equations. The latter must be solved in terms of the parameters of the energy function of the closed-loop. Finally, the stability properties are studied using the Lyapunov theory. Generally, the proposed candidate offers high robustness, fast speed convergence, and high efficiency over the conventional benchmark strategies. The effectiveness of the proposed strategy is performed under extensive numerical investigation with MATLAB/Simulink software.
 
## Keywords
Passivity-based control; Interconnection and damping assignment; Permanent magnet synchronous motor; Non-linear observer
 
## Citation
- **Journal:** Energy Reports
- **Year:** 2022
- **Volume:** 8
- **Issue:** 
- **Pages:** 1350--1361
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.egyr.2021.12.057](https://doi.org/10.1016/j.egyr.2021.12.057)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Belkhier_2022,
  title={{Interconnection and damping assignment passivity-based non-linear observer control for efficiency maximization of permanent magnet synchronous motor}},
  volume={8},
  ISSN={2352-4847},
  DOI={10.1016/j.egyr.2021.12.057},
  journal={Energy Reports},
  publisher={Elsevier BV},
  author={Belkhier, Youcef and Achour, Abdelyazid and Bures, Miroslav and Ullah, Nasim and Bajaj, Mohit and Zawbaa, Hossam M. and Kamel, Salah},
  year={2022},
  pages={1350--1361}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/interconnection-and-damping-assignment-passivity-based-non-linear-observer-control-for-efficiency-maximization-of-permanent-magnet-synchronous-motor.bib)
 
## References
- Allouche, A. et al. Mechanical Fault Diagnostic in PMSM from Only One Current Measurement: A Tacholess Order Tracking Approach. Sensors 20, 5011 (2020) -- [10.3390/s20175011](https://doi.org/10.3390/s20175011)
- Zhao, X., Wang, C., Duan, W. & Jiang, J. Research on sensorless control system of low speed and high power PMSM based on improved high frequency signal injection. Energy Reports 7, 499–504 (2021) -- [10.1016/j.egyr.2021.01.066](https://doi.org/10.1016/j.egyr.2021.01.066)
- Urbanski, K. & Janiszewski, D. Sensorless Control of the Permanent Magnet Synchronous Motor. Sensors 19, 3546 (2019) -- [10.3390/s19163546](https://doi.org/10.3390/s19163546)
- Li, Y., Zhao, C., Zhou, Y. & Qin, Y. Model predictive torque control of PMSM based on data drive. Energy Reports 6, 1370–1376 (2020) -- [10.1016/j.egyr.2020.11.019](https://doi.org/10.1016/j.egyr.2020.11.019)
- Scarcella, G., Scelba, G., Pulvirenti, M. & Lorenz, R. D. Fault-Tolerant Capability of Deadbeat-Direct Torque and Flux Control for Three-Phase PMSM Drives. IEEE Trans. on Ind. Applicat. 53, 5496–5508 (2017) -- [10.1109/tia.2017.2743070](https://doi.org/10.1109/tia.2017.2743070)
- Apte, A., Joshi, V. A., Mehta, H. & Walambe, R. Disturbance-Observer-Based Sensorless Control of PMSM Using Integral State Feedback Controller. IEEE Trans. Power Electron. 35, 6082–6090 (2020) -- [10.1109/tpel.2019.2949921](https://doi.org/10.1109/tpel.2019.2949921)
- Alfehaid, A. A., Strangas, E. G. & Khalil, H. K. Speed Control of Permanent Magnet Synchronous Motor With Uncertain Parameters and Unknown Disturbance. IEEE Trans. Contr. Syst. Technol. 29, 2639–2646 (2021) -- [10.1109/tcst.2020.3026569](https://doi.org/10.1109/tcst.2020.3026569)
- Smidl, V., Janous, S., Adam, L. & Peroutka, Z. Direct Speed Control of a PMSM Drive Using SDRE and Convex Constrained Optimization. IEEE Trans. Ind. Electron. 65, 532–542 (2018) -- [10.1109/tie.2017.2723872](https://doi.org/10.1109/tie.2017.2723872)
- Xu, W., Junejo, A. K., Liu, Y., Hussien, M. G. & Zhu, J. An Efficient Antidisturbance Sliding-Mode Speed Control Method for PMSM Drive Systems. IEEE Trans. Power Electron. 36, 6879–6891 (2021) -- [10.1109/tpel.2020.3039474](https://doi.org/10.1109/tpel.2020.3039474)
- Xu, W., Jiang, Y., Mu, C. & Blaabjerg, F. Improved Nonlinear Flux Observer-Based Second-Order SOIFO for PMSM Sensorless Control. IEEE Trans. Power Electron. 34, 565–579 (2019) -- [10.1109/tpel.2018.2822769](https://doi.org/10.1109/tpel.2018.2822769)
- Mani, P., Rajan, R., Shanmugam, L. & Joo, Y. H. Adaptive Fractional Fuzzy Integral Sliding Mode Control for PMSM Model. IEEE Trans. Fuzzy Syst. 27, 1674–1686 (2019) -- [10.1109/tfuzz.2018.2886169](https://doi.org/10.1109/tfuzz.2018.2886169)
- Junejo, A. K., Xu, W., Mu, C., Ismail, M. M. & Liu, Y. Adaptive Speed Control of PMSM Drive System Based a New Sliding-Mode Reaching Law. IEEE Trans. Power Electron. 35, 12110–12121 (2020) -- [10.1109/tpel.2020.2986893](https://doi.org/10.1109/tpel.2020.2986893)
- Nguyen, A. T., Basit, B. A., Choi, H. H. & Jung, J.-W. Disturbance Attenuation for Surface-Mounted PMSM Drives Using Nonlinear Disturbance Observer-Based Sliding Mode Control. IEEE Access 8, 86345–86356 (2020) -- [10.1109/access.2020.2992635](https://doi.org/10.1109/access.2020.2992635)
- Niu, S., Luo, Y., Fu, W. & Zhang, X. An Indirect Reference Vector-Based Model Predictive Control for a Three-Phase PMSM Motor. IEEE Access 8, 29435–29445 (2020) -- [10.1109/access.2020.2968949](https://doi.org/10.1109/access.2020.2968949)
- Yang, B. et al. Passivity-based sliding-mode control design for optimal power extraction of a PMSG based variable speed wind turbine. Renewable Energy 119, 577–589 (2018) -- [10.1016/j.renene.2017.12.047](https://doi.org/10.1016/j.renene.2017.12.047)
- Nicklasson, Passivity-based control of the general rotating electrical machine. (1994)
- Nicklasson, P. J., Ortega, R., Espinosa-Perez, G. & Jacobi, C. G. J. Passivity-based control of a class of Blondel-Park transformable electric machines. IEEE Trans. Automat. Contr. 42, 629–647 (1997) -- [10.1109/9.580867](https://doi.org/10.1109/9.580867)
- Achour, A. Y., Mendil, B., Bacha, S. & Munteanu, I. Passivity-based current controller design for a permanent-magnet synchronous motor. ISA Transactions 48, 336–346 (2009) -- [10.1016/j.isatra.2009.04.004](https://doi.org/10.1016/j.isatra.2009.04.004)
- Ramírez-Leyva, F. H., Peralta-Sánchez, E., Vásquez-Sanjuan, J. J. & Trujillo-Romero, F. Passivity-Based Speed Control for Permanent Magnet Motors. Procedia Technology 7, 215–222 (2013) -- [10.1016/j.protcy.2013.04.027](https://doi.org/10.1016/j.protcy.2013.04.027)
- Khanchoul, M., Hilairet, M. & Normand-Cyrot, D. A passivity-based controller under low sampling for speed control of PMSM. Control Engineering Practice 26, 20–27 (2014) -- [10.1016/j.conengprac.2013.12.013](https://doi.org/10.1016/j.conengprac.2013.12.013)
- Wang, Passivity-based control for rocket launcher position servo system based on ADRC optimized by IPSO-BP algorithm. Shock Vib. (2018)
- [Liu, X., Yu, H., Yu, J. & Zhao, Y. A Novel Speed Control Method Based on Port-Controlled Hamiltonian and Disturbance Observer for PMSM Drives. IEEE Access 7, 111115–111123 (2019)](a-novel-speed-control-method-based-on-port-controlled-hamiltonian-and-disturbance-observer-for-pmsm-drives) -- [10.1109/access.2019.2934987](https://doi.org/10.1109/access.2019.2934987)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Belkhier, Y., Achour, A., Hamoudi, F., Ullah, N. & Mendil, B. Robust energy‐based nonlinear observer and voltage control for grid‐connected permanent magnet synchronous generator in the tidal energy conversion system. Int J Energy Res 45, 13250–13268 (2021) -- [10.1002/er.6650](https://doi.org/10.1002/er.6650)
- Zakharov, Analysis of field oriented control of permanent magnet synchronous motor for a valveless pump-controlled actuator. Proceedings (2020)

