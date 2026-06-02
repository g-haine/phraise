---
title: "ARISE: Continuous Port–Hamiltonian Damping at ESPA Injection for High Speed Flyby"
date: 2026-05-22 00:00:00 +0100
permalink: arise-continuous-port-hamiltonian-damping-at-espa-injection-for-high-speed-flyby
year: 2026
authors: Harish Vernekar, Leonard Vance, Jekan Thangavelautham
category: proceedings
---
 
## Authors
[Harish Vernekar](authors/harish-vernekar), [Leonard Vance](authors/leonard-vance), [Jekan Thangavelautham](authors/jekan-thangavelautham)
 
## Abstract
This paper presents Layer 1 of ARISE (Autonomous Reconfigurable Infrastructure for Swarm-based Exploration): a separation damping layer that rapidly suppresses post-release tip-off and drift in a carrier-deputy spacecraft swarm. We model each vehicle as a mechanical port-Hamiltonian (pH) system evolving on the Special Euclidean group \\( S E(3) \\) and shape a convex storage function about the desired relative pose. By injecting collocated damping through the body-wrench port, the closed loop is made strictly passive, so the shaped Hamiltonian serves as a Lyapunov storage that decreases monotonically. We provide compact passivity guarantees in continuous time and in sampled implementation, including a bounded-delay extension using a passivity observer/controller (PO/PC). To realize the commanded wrench under actuator limits, we use a constrained allocator posed as a bounded nonnegative least-squares (BNLS) problem and give a condition under which damping dominates allocation and saturation errors. In a representative near-Earth-object flyby separation case study (Apophis-2029 reference), the layer drives both carrier and deputies to low-rate, low-drift conditions within minutes and remains robust to thrust dispersion, inertia variation, saturation, and fixed command latency. These results show that a minimal, passivity-based realization can reliably drain separation transients and hand off the swarm to subsequent formation-setting and pointing phases with clear stability margins.
 
## Citation
- **Journal:** 2026 IEEE Aerospace Conference
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 1--13
- **Publisher:** IEEE
- **DOI:** [10.1109/aero66936.2026.11519786](https://doi.org/10.1109/aero66936.2026.11519786)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Vernekar_2026,
  title={{ARISE: Continuous Port–Hamiltonian Damping at ESPA Injection for High Speed Flyby}},
  DOI={10.1109/aero66936.2026.11519786},
  booktitle={{2026 IEEE Aerospace Conference}},
  publisher={IEEE},
  author={Vernekar, Harish and Vance, Leonard and Thangavelautham, Jekan},
  year={2026},
  pages={1--13}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/arise-continuous-port-hamiltonian-damping-at-espa-injection-for-high-speed-flyby.bib)
 
## References
- Gateway: About. NASA (2025)
- NASA Planetary Defense Strategy and Action P lan, NASA Technical Report. support of the National Preparedness Strategy and Action Plan for Near-Earth Object Hazards and Planetary Defense (2023)
- (2023) Near-Earth Objects and Planetary Defenc -- [10.18356/9789213587577](https://doi.org/10.18356/9789213587577)
- Baker-McEvilly B, Bhadauria S, Canales D, Frueh C (2024) A comprehensive review on Cislunar expansion and space domain awareness. Progress in Aerospace Sciences 147:101019. https://doi.org/10.1016/j.paerosci.2024.10101 -- [10.1016/j.paerosci.2024.101019](https://doi.org/10.1016/j.paerosci.2024.101019)
- Nolan, OSIRIS-APEX: An OSIRIS-REx Extended Mission to Apophis. Asteroids, Comets, Meteors Conference 2023 (2023)
- Apophis (2024)
- Vernekar H, Vance L, Thangavelautham J (2025) A Low Cost Apophis Precursor Mission Using CubeSat Swarms. AIAA SCITECH 2025 Foru -- [10.2514/6.2025-2738](https://doi.org/10.2514/6.2025-2738)
- Vernekar H, Fritzler A, Chawdagor P, Vance L, Thangavelautham J (2025) Reusable CubeSat Constellation for (99942) Apophis 2029 Observation and Beyond. IAF Space Exploration Symposium 937–95 -- [10.52202/083076-0104](https://doi.org/10.52202/083076-0104)
- Vernekar, Adaptive Swarm Reconfiguration Using Relative Orbit Element (ROE) Space for Enhanced Space Observation. AAS/AIAA Space Flight Mechanics Meeting (GNC) (2025)
- Vance, Low-Cost Reconstructive Topography of Near Earth Objects Using High-Speed Flyby Swarms. AAS 2025 Conference Proceedings (2025)
- van der Schaft, Port-Hamiltonian nonlinear systems (2024)
- [Fujimoto K, Takeuchi T, Matsumoto Y (2015) On port-Hamiltonian modeling and control of quaternion systems. IFAC-PapersOnLine 48(13):39–44. https://doi.org/10.1016/j.ifacol.2015.10.21](on-port-hamiltonian-modeling-and-control-of-quaternion-systems) -- [10.1016/j.ifacol.2015.10.211](https://doi.org/10.1016/j.ifacol.2015.10.211)
- [Dirksz DA, Scherp JMA (2010) Adaptive tracking control of fully actuated port-Hamiltonian mechanical systems. 2010 IEEE International Conference on Control Applications 1678–168](adaptive-tracking-control-of-fully-actuated-port-hamiltonian-mechanical-systems) -- [10.1109/cca.2010.5611301](https://doi.org/10.1109/cca.2010.5611301)
- Kang Z, Shen Q, Wu S, Damaren CJ (2024) Saturated adaptive pose tracking control of spacecraft on SE(3) under attitude constraints and obstacle-avoidance constraints. Automatica 159:111367. https://doi.org/10.1016/j.automatica.2023.11136 -- [10.1016/j.automatica.2023.111367](https://doi.org/10.1016/j.automatica.2023.111367)
- Duong T, Atanasov N (2022) Adaptive Control of SE(3) Hamiltonian Dynamics With Learned Disturbance Features. IEEE Control Syst Lett 6:2773–2778. https://doi.org/10.1109/lcsys.2022.317715 -- [10.1109/lcsys.2022.3177156](https://doi.org/10.1109/lcsys.2022.3177156)
- [Rashad R, Califano F, Stramigioli S (2019) Port-Hamiltonian Passivity-Based Control on SE(3) of a Fully Actuated UAV for Aerial Physical Interaction Near-Hovering. IEEE Robot Autom Lett 4(4):4378–4385. https://doi.org/10.1109/lra.2019.293286](port-hamiltonian-passivity-based-control-on-se-3-of-a-fully-actuated-uav-for-aerial-physical-interaction-near-hovering) -- [10.1109/lra.2019.2932864](https://doi.org/10.1109/lra.2019.2932864)
- Takegaki M, Arimoto S (1981) A New Feedback Method for Dynamic Control of Manipulators. Journal of Dynamic Systems, Measurement, and Control 103(2):119–125. https://doi.org/10.1115/1.313965 -- [10.1115/1.3139651](https://doi.org/10.1115/1.3139651)
- {"status":"error" -- [10.1109/tcst.2013.2283372](https://doi.org/10.1109/tcst.2013.2283372)
- Johansen TA, Fossen TI (2013) Control allocation—A survey. Automatica 49(5):1087–1103. https://doi.org/10.1016/j.automatica.2013.01.03 -- [10.1016/j.automatica.2013.01.035](https://doi.org/10.1016/j.automatica.2013.01.035)
- Härkegård O, Glad ST (2005) Resolving actuator redundancy—optimal control vs. control allocation. Automatica 41(1):137–144. https://doi.org/10.1016/j.automatica.2004.09.00 -- [10.1016/j.automatica.2004.09.007](https://doi.org/10.1016/j.automatica.2004.09.007)
- Cheng, Lyapunov-based switched systems control (2015)
- Hespanha JP, Morse AS Stability of switched systems with average dwell-time. Proceedings of the 38th IEEE Conference on Decision and Control (Cat. No.99CH36304) 3:2655–266 -- [10.1109/cdc.1999.831330](https://doi.org/10.1109/cdc.1999.831330)
- RAFTI TM user guide: Refuelable spacecraft requirements specification. Orbit Fab, Technical Report (2020)
- Capps, An Analysis and Simulation of Launch Vehicle Separation Dynamics Including Thrust Transients (2011)

