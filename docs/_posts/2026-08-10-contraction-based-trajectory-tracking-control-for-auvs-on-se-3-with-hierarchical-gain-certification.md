---
title: "Contraction-Based Trajectory Tracking Control for AUVs on SE(3) with Hierarchical Gain Certification"
date: 2026-08-10 00:00:00 +0100
permalink: contraction-based-trajectory-tracking-control-for-auvs-on-se-3-with-hierarchical-gain-certification
year: 2026
authors: Jinjun Jia, Kang An, Yuchen Liao, Xun Yan, Tiedong Zhang, Dapeng Jiang
category: articles
---
 
## Authors
[Jinjun Jia](authors/jinjun-jia), [Kang An](authors/kang-an), [Yuchen Liao](authors/yuchen-liao), [Xun Yan](authors/xun-yan), [Tiedong Zhang](authors/tiedong-zhang), [Dapeng Jiang](authors/dapeng-jiang)
 
## Abstract
This paper develops a contraction-certified trajectory-tracking and gain-selection framework for fully actuated autonomous underwater vehicles on SE(3). The vehicle dynamics are represented in port-Hamiltonian form with a Rayleigh-type dissipation potential, and a dual potential shaping controller provides an energy-structured rotational–translational cascade. Regional contraction certificates are derived separately for the rotational and translational subsystems. The rotational analysis uses fixed left-trivialised momentum coordinates and retains anisotropic-inertia effects and the complete off-diagonal differential coupling. The translational analysis applies to a general known symmetric positive-definite inertia matrix through an attitude-cover semidefinite programme, with an exact endpoint reduction for isotropic inertia. A scaled composite metric combines the subsystem certificates and guarantees every strict complete-cascade rate below the slower subsystem rate. Large initial attitude errors are handled by an energy-entry phase followed by contraction within a prescribed tube, without controller switching. The four-dimensional gain-selection problem is decomposed into two independent two-dimensional offline searches using bisection and SDP/LMI feasibility tests. Numerical studies on the ODIN AUV quantify the region–gain–rate trade-off and examine small-angle, large-angle, and near-antipodal manoeuvres. The framework certifies complete-cascade rates of 0.042096s−1 and 0.008524s−1 for the 60∘/60∘ and 150∘/80∘ regions, respectively.
 
## Citation
- **Journal:** Journal of Marine Science and Engineering
- **Year:** 2026
- **Volume:** 14
- **Issue:** 16
- **Pages:** 1465
- **Publisher:** MDPI AG
- **DOI:** [10.3390/jmse14161465](https://doi.org/10.3390/jmse14161465)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Jia_2026,
  title={{Contraction-Based Trajectory Tracking Control for AUVs on SE(3) with Hierarchical Gain Certification}},
  volume={14},
  ISSN={2077-1312},
  DOI={10.3390/jmse14161465},
  number={16},
  journal={Journal of Marine Science and Engineering},
  publisher={MDPI AG},
  author={Jia, Jinjun and An, Kang and Liao, Yuchen and Yan, Xun and Zhang, Tiedong and Jiang, Dapeng},
  year={2026},
  pages={1465}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/contraction-based-trajectory-tracking-control-for-auvs-on-se-3-with-hierarchical-gain-certification.bib)
 
## References
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Guerrero-Sánchez ME, Hernández-González O, Valencia-Palomo G, Mercado-Ravell DA, López-Estrada FR, Hoyo-Montaño JA (2021) Robust IDA-PBC for under-actuated systems with inertia matrix dependent of the unactuated coordinates: application to a UAV carrying a load. Nonlinear Dyn 105(4):3225–3238. https://doi.org/10.1007/s11071-021-06776- -- [10.1007/s11071-021-06776-7](https://doi.org/10.1007/s11071-021-06776-7)
- [Guerrero-Sánchez ME, Montoya-Morales JR, Valencia-Palomo G, Hernández-González O (2024) Robust IDA-PBC for non-separable PCH systems under time-varying external disturbances. Nonlinear Dyn 113(4):3499–3510. https://doi.org/10.1007/s11071-024-10380-](robust-ida-pbc-for-non-separable-pch-systems-under-time-varying-external-disturbances) -- [10.1007/s11071-024-10380-w](https://doi.org/10.1007/s11071-024-10380-w)
- [Donaire A, Perez T (2012) Dynamic positioning of marine craft using a port-Hamiltonian framework. Automatica 48(5):851–856. https://doi.org/10.1016/j.automatica.2012.02.02](dynamic-positioning-of-marine-craft-using-a-port-hamiltonian-framework) -- [10.1016/j.automatica.2012.02.022](https://doi.org/10.1016/j.automatica.2012.02.022)
- Desai RP, Manjarekar NS (2024) Interconnection and damping assignment passivity‐based control for dynamic steering position stabilization of an underactuated AUV. Adv Control Appl 6(3). https://doi.org/10.1002/adc2.22 -- [10.1002/adc2.225](https://doi.org/10.1002/adc2.225)
- [Fujimoto K, Sakurama K, Sugie T (2003) Trajectory tracking control of port-controlled Hamiltonian systems via generalized canonical transformations. Automatica 39(12):2059–2069. https://doi.org/10.1016/j.automatica.2003.07.00](trajectory-tracking-control-of-port-controlled-hamiltonian-systems-via-generalized-canonical-transformations) -- [10.1016/j.automatica.2003.07.005](https://doi.org/10.1016/j.automatica.2003.07.005)
- [Donaire A, Romero JG, Perez T (2017) Trajectory tracking passivity-based control for marine vehicles subject to disturbances. Journal of the Franklin Institute 354(5):2167–2182. https://doi.org/10.1016/j.jfranklin.2017.01.01](trajectory-tracking-passivity-based-control-for-marine-vehicles-subject-to-disturbances) -- [10.1016/j.jfranklin.2017.01.012](https://doi.org/10.1016/j.jfranklin.2017.01.012)
- [Donaire A, Guadalupe Romero J, Perez T (2015) Passivity-based Trajectory-tracking for Marine Craft with Disturbance Rejection. IFAC-PapersOnLine 48(16):19–24. https://doi.org/10.1016/j.ifacol.2015.10.25](passivity-based-trajectory-tracking-for-marine-craft-with-disturbance-rejection) -- [10.1016/j.ifacol.2015.10.252](https://doi.org/10.1016/j.ifacol.2015.10.252)
- Lv C, Yu H, Chen J, Zhao N, Chi J (2022) Trajectory tracking control for unmanned surface vessel with input saturation and disturbances via robust state error IDA-PBC approach. Journal of the Franklin Institute 359(5):1899–1924. https://doi.org/10.1016/j.jfranklin.2022.01.03 -- [10.1016/j.jfranklin.2022.01.036](https://doi.org/10.1016/j.jfranklin.2022.01.036)
- Bullo F, Murray RM (1999) Tracking for fully actuated mechanical systems: a geometric framework. Automatica 35(1):17–34. https://doi.org/10.1016/s0005-1098(98)00119- -- [10.1016/s0005-1098(98)00119-8](https://doi.org/10.1016/s0005-1098(98)00119-8)
- Sanyal A, Nordkvist N, Chyba M (2011) An Almost Global Tracking Control Scheme for Maneuverable Autonomous Vehicles and its Discretization. IEEE Trans Automat Contr 56(2):457–462. https://doi.org/10.1109/tac.2010.209019 -- [10.1109/tac.2010.2090190](https://doi.org/10.1109/tac.2010.2090190)
- Maithripala DHS, Berg JM (2015) An intrinsic PID controller for mechanical systems on Lie groups. Automatica 54:189–200. https://doi.org/10.1016/j.automatica.2015.01.00 -- [10.1016/j.automatica.2015.01.005](https://doi.org/10.1016/j.automatica.2015.01.005)
- Liao Y, Yan X, An K, Wang Z, Zhang T, Wu S, Jiang D (2024) Fixed-time geometric tracking control of autonomous underwater vehicles on SE(3). Ocean Engineering 311:118757. https://doi.org/10.1016/j.oceaneng.2024.11875 -- [10.1016/j.oceaneng.2024.118757](https://doi.org/10.1016/j.oceaneng.2024.118757)
- [Yaghmaei A, Yazdanpanah MJ (2017) Trajectory tracking for a class of contractive port Hamiltonian systems. Automatica 83:331–336. https://doi.org/10.1016/j.automatica.2017.06.03](trajectory-tracking-for-a-class-of-contractive-port-hamiltonian-systems) -- [10.1016/j.automatica.2017.06.039](https://doi.org/10.1016/j.automatica.2017.06.039)
- [Barabanov N, Ortega R, Pyrkin A (2019) On contraction of time-varying port-Hamiltonian systems. Systems &amp; Control Letters 133:104545. https://doi.org/10.1016/j.sysconle.2019.10454](on-contraction-of-time-varying-port-hamiltonian-systems) -- [10.1016/j.sysconle.2019.104545](https://doi.org/10.1016/j.sysconle.2019.104545)
- [Yaghmaei A, Yazdanpanah MJ (2024) On Contractive Port-Hamiltonian Systems With State-Modulated Interconnection and Damping Matrices. IEEE Trans Automat Contr 69(1):622–628. https://doi.org/10.1109/tac.2023.327339](on-contractive-port-hamiltonian-systems-with-state-modulated-interconnection-and-damping-matrices) -- [10.1109/tac.2023.3273394](https://doi.org/10.1109/tac.2023.3273394)
- Manchester IR, Slotine J-JE (2017) Control Contraction Metrics: Convex and Intrinsic Criteria for Nonlinear Feedback Design. IEEE Trans Automat Contr 62(6):3046–3053. https://doi.org/10.1109/tac.2017.266838 -- [10.1109/tac.2017.2668380](https://doi.org/10.1109/tac.2017.2668380)
- Wu D, Yi B, Manchester IR (2024) Control Contraction Metrics on Submanifolds. 2024 IEEE 63rd Conference on Decision and Control (CDC) 3735–374 -- [10.1109/cdc56724.2024.10886040](https://doi.org/10.1109/cdc56724.2024.10886040)
- Vang B, Tron R (2019) Geometric Attitude Control via Contraction on Manifolds with Automatic Gain Selection. 2019 IEEE 58th Conference on Decision and Control (CDC) 6138–614 -- [10.1109/cdc40024.2019.9029723](https://doi.org/10.1109/cdc40024.2019.9029723)
- Vang B, Tron R (2020) Global Attitude Control via Contraction on Manifolds with Reference Trajectory and Optimization. 2020 59th IEEE Conference on Decision and Control (CDC) 2006–201 -- [10.1109/cdc42340.2020.9303862](https://doi.org/10.1109/cdc42340.2020.9303862)
- [Yaghmaei A, Yazdanpanah MJ (2015) Trajectory tracking of a class of port Hamiltonian systems using Timed IDA-PBC technique. 2015 54th IEEE Conference on Decision and Control (CDC) 5037–504](trajectory-tracking-of-a-class-of-port-hamiltonian-systems-using-timed-ida-pbc-technique) -- [10.1109/cdc.2015.7403007](https://doi.org/10.1109/cdc.2015.7403007)
- LOHMILLER W, SLOTINE J-JE (1998) On Contraction Analysis for Non-linear Systems. Automatica 34(6):683–696. https://doi.org/10.1016/s0005-1098(98)00019- -- [10.1016/s0005-1098(98)00019-3](https://doi.org/10.1016/s0005-1098(98)00019-3)
- Simpson-Porco JW, Bullo F (2014) Contraction theory on Riemannian manifolds. Systems &amp; Control Letters 65:74–80. https://doi.org/10.1016/j.sysconle.2013.12.01 -- [10.1016/j.sysconle.2013.12.016](https://doi.org/10.1016/j.sysconle.2013.12.016)
- Slotine JE (2003) Modular stability tools for distributed computation and control. Adaptive Control &amp; Signal 17(6):397–416. https://doi.org/10.1002/acs.75 -- [10.1002/acs.754](https://doi.org/10.1002/acs.754)
- Fossen TI (2011) Handbook of Marine Craft Hydrodynamics and Motion Contro -- [10.1002/9781119994138](https://doi.org/10.1002/9781119994138)
- [Duong T, Altawaitan A, Stanley J, Atanasov N (2024) Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control. IEEE Trans Robot 40:3695–3715. https://doi.org/10.1109/tro.2024.342843](port-hamiltonian-neural-ode-networks-on-lie-groups-for-robot-dynamics-learning-and-control) -- [10.1109/tro.2024.3428433](https://doi.org/10.1109/tro.2024.3428433)
- Lee T (2012) Exponential stability of an attitude tracking control system on SO(3) for large-angle rotational maneuvers. Systems &amp; Control Letters 61(1):231–237. https://doi.org/10.1016/j.sysconle.2011.10.01 -- [10.1016/j.sysconle.2011.10.017](https://doi.org/10.1016/j.sysconle.2011.10.017)
- Lee JM (2018) Introduction to Riemannian Manifolds. Springer International Publishin -- [10.1007/978-3-319-91755-9](https://doi.org/10.1007/978-3-319-91755-9)

