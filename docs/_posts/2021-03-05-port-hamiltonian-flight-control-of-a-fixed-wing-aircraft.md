---
layout: post
title: "Port-Hamiltonian Flight Control of a Fixed-Wing Aircraft"
date: 2021-03-05 00:00:00 +0100
permalink: port-hamiltonian-flight-control-of-a-fixed-wing-aircraft
year: 2022
authors: Jean-Michel Fahmi, Craig A. Woolsey
category:
  - articles
---
 
## Authors
[Jean-Michel Fahmi](authors/jean_michel_w_fahmi), [Craig A. Woolsey](authors/craig_a_woolsey)
 
## Abstract
This brief addresses the problem of stabilizing steady, wing level flight of a fixed-wing aircraft to a specified inertial velocity (speed, course, and climb angle). The aircraft is modeled as a port-Hamiltonian system and the passivity of this system is leveraged in devising the nonlinear control law. The aerodynamic force model in the port-Hamiltonian formulation is quite general; the static, state feedback control scheme requires only basic assumptions concerning lift, side force, and drag. Following an energy-shaping approach, the static state feedback control law is designed to leverage the open-loop system’s port-Hamiltonian structure in order to construct a control Lyapunov function. Asymptotic stability of the desired flight condition is guaranteed within a large region of attraction. Simulations comparing the proposed flight controller with dynamic inversion suggest it is more robust to uncertainty in aerodynamics.
 
## Citation
- **Journal:** IEEE Transactions on Control Systems Technology
- **Year:** 2022
- **Volume:** 30
- **Issue:** 1
- **Pages:** 408--415
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/TCST.2021.3059928](https://doi.org/10.1109/TCST.2021.3059928)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Fahmi_2022,
  title={{Port-Hamiltonian Flight Control of a Fixed-Wing Aircraft}},
  volume={30},
  ISSN={2374-0159},
  DOI={10.1109/tcst.2021.3059928},
  number={1},
  journal={IEEE Transactions on Control Systems Technology},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Fahmi, Jean-Michel and Woolsey, Craig A.},
  year={2022},
  pages={408--415}
}
{% endraw %}
{% endhighlight %}
 
## References
- Snell, S. A., Enns, D. F. & Garrard, W. L., Jr. Nonlinear inversion flight control for a supermaneuverable aircraft. Journal of Guidance, Control, and Dynamics vol. 15 976–984 (1992) -- [10.2514/3.20932](https://doi.org/10.2514/3.20932)
- Nonlinear Systems. (Springer US, 1996). doi:10.1007/978-1-4613-1193-5 -- [10.1007/978-1-4613-1193-5](https://doi.org/10.1007/978-1-4613-1193-5)
- Hovakimyan, N. & Cao, C. ℒ1Adaptive Control Theory. (Society for Industrial and Applied Mathematics, 2010). doi:10.1137/1.9780898719376 -- [10.1137/1.9780898719376](https://doi.org/10.1137/1.9780898719376)
- van der Schaft, A. L2 - Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer London, 2000). doi:10.1007/978-1-4471-0507-7 -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- González, H., Duarte-Mermoud, M. A., Pelissier, I., Travieso-Torres, J. C. & Ortega, R. A novel induction motor control scheme using IDA-PBC. Journal of Control Theory and Applications vol. 6 59–68 (2008) -- [10.1007/s11768-008-7193-9](https://doi.org/10.1007/s11768-008-7193-9)
- Acosta, J. A., Sanchez, M. I. & Ollero, A. Robust control of underactuated Aerial Manipulators via IDA-PBC. 53rd IEEE Conference on Decision and Control 673–678 (2014) doi:10.1109/cdc.2014.7039459 -- [10.1109/CDC.2014.7039459](https://doi.org/10.1109/CDC.2014.7039459)
- Guerrero, M. E., Mercado, D. A., Lozano, R. & Garcia, C. D. IDA-PBC methodology for a quadrotor UAV transporting a cable-suspended payload. 2015 International Conference on Unmanned Aircraft Systems (ICUAS) 470–476 (2015) doi:10.1109/icuas.2015.7152325 -- [10.1109/ICUAS.2015.7152325](https://doi.org/10.1109/ICUAS.2015.7152325)
- Yuksel, B., Secchi, C., Bulthoff, H. H. & Franchi, A. Reshaping the physical properties of a quadrotor through IDA-PBC and its application to aerial physical interaction. 2014 IEEE International Conference on Robotics and Automation (ICRA) 6258–6265 (2014) doi:10.1109/icra.2014.6907782 -- [10.1109/ICRA.2014.6907782](https://doi.org/10.1109/ICRA.2014.6907782)
- Mersha, A. Y., Carloni, R. & Stramigioli, S. Port-based modeling and control of underactuated aerial vehicles. 2011 IEEE International Conference on Robotics and Automation 14–19 (2011) doi:10.1109/icra.2011.5980053 -- [10.1109/ICRA.2011.5980053](https://doi.org/10.1109/ICRA.2011.5980053)
- Munoz, L. E., Santos, O., Castillo, P. & Fantoni, I. Energy-based nonlinear control for a quadrotor rotorcraft. 2013 American Control Conference 1177–1182 (2013) doi:10.1109/acc.2013.6579995 -- [10.1109/ACC.2013.6579995](https://doi.org/10.1109/ACC.2013.6579995)
- Woolsey, C. A. & Techy, L. Cross-track control of a slender, underactuated AUV using potential shaping. Ocean Engineering vol. 36 82–91 (2009) -- [10.1016/j.oceaneng.2008.07.010](https://doi.org/10.1016/j.oceaneng.2008.07.010)
- Fahmi, J.-M. W. & Woolsey, C. A. Directional Stabilization of a Fixed-Wing Aircraft Using Potential Shaping. 2018 Atmospheric Flight Mechanics Conference (2018) doi:10.2514/6.2018-3620 -- [10.2514/6.2018-3620](https://doi.org/10.2514/6.2018-3620)
- [Valentinis, F., Donaire, A. & Perez, T. Energy-based motion control of a slender hull unmanned underwater vehicle. Ocean Engineering vol. 104 604–616 (2015)](energy-based-motion-control-of-a-slender-hull-unmanned-underwater-vehicle) -- [10.1016/j.oceaneng.2015.05.014](https://doi.org/10.1016/j.oceaneng.2015.05.014)
- [Valentinis, F., Donaire, A. & Perez, T. Energy-based guidance of an underactuated unmanned underwater vehicle on a helical trajectory. Control Engineering Practice vol. 44 138–156 (2015)](energy-based-guidance-of-an-underactuated-unmanned-underwater-vehicle-on-a-helical-trajectory) -- [10.1016/j.conengprac.2015.07.010](https://doi.org/10.1016/j.conengprac.2015.07.010)
- [Valentinis, F. & Woolsey, C. Nonlinear control of a subscale submarine in emergency ascent. Ocean Engineering vol. 171 646–662 (2019)](nonlinear-control-of-a-subscale-submarine-in-emergency-ascent) -- [10.1016/j.oceaneng.2018.11.029](https://doi.org/10.1016/j.oceaneng.2018.11.029)
- Fujimoto, K., Sakurama, K. & Sugie, T. Trajectory tracking control of port-controlled Hamiltonian systems via generalized canonical transformations. Automatica vol. 39 2059–2069 (2003) -- [10.1016/j.automatica.2003.07.005](https://doi.org/10.1016/j.automatica.2003.07.005)
- Battista, T., Jung, S., Woolsey, C. & Paterson, E. An energy-casimir approach to underwater vehicle depth and heading regulation in short crested waves. 2017 IEEE Conference on Control Technology and Applications (CCTA) 217–222 (2017) doi:10.1109/ccta.2017.8062466 -- [10.1109/CCTA.2017.8062466](https://doi.org/10.1109/CCTA.2017.8062466)
- Grauer, J. A. & Morelli, E. A. A Generic Nonlinear Aerodynamic Model for Aircraft. AIAA Atmospheric Flight Mechanics Conference (2014) doi:10.2514/6.2014-0542 -- [10.2514/6.2014-0542](https://doi.org/10.2514/6.2014-0542)
- Lane, S. H. & Stengel, R. F. Flight control design using non-linear inverse dynamics. Automatica vol. 24 471–483 (1988) -- [10.1016/0005-1098(88)90092-1](https://doi.org/10.1016/0005-1098(88)90092-1)

