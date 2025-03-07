---
layout: post
title: "Design of a Port-Hamiltonian Control for an Alt-Azimuth Liquid–Mirror Telescope"
date: 2023-08-08 00:00:00 +0100
permalink: design-of-a-port-hamiltonian-control-for-an-alt-azimuth-liquid-mirror-telescope
year: 2023
authors: Juan Cristobal Alcaraz Tapia, Carlos E. Castañeda, Héctor Vargas Rodriguez, P. Esquivel
category: articles
---
 
## Authors
[Juan Cristobal Alcaraz Tapia](authors/juan-cristobal-alcaraz-tapia), [Carlos E. Castañeda](authors/carlos-e-castaneda), [Héctor Vargas Rodriguez](authors/hector-vargas-rodriguez), [P. Esquivel](authors/p-esquivel)
 
## Abstract
In this work, we design a control strategy to be applied in a port-Hamilton representation of a liquid-mirror telescope for an alt-azimuth configuration. Starting from a dynamical model for an alt-azimuth liquid-mirror telescope based on Lagrange mechanics, a transformation to the port-Hamilton form is made. Such a dynamical model is obtained by computing the kinetic and potential energy of the telescope and substituting them in the Euler–Lagrange equation of motion. Then, for the transformation to the port-Hamiltonian form, we obtain the relation between the Hamiltonian and the Lagrangian. The resulting open-loop model based on the Hamiltonian function is controlled using an extension of the interconnection and damping-assignment passivity-based control aiming for a robust and accurate steady behavior in the closed loop while tracking a star’s position. For comparison purposes, two different control strategies are applied to the Lagrangian model, inverse-dynamics control and sliding mode super-twisting control. Since the light is collected by the principal mirror of the telescope while tracking a star, we make a description of the liquid mirror’s behavior. The tracking star’s position is described as a function of the observer’s position and the star’s coordinates as well as the date of observation. The simulations’ results show that the port-Hamilton control has a good transitory and steady response as well as great accuracy competing with that of inverse-dynamics control but with greater robustness and no chattering drawback.
 
## Citation
- **Journal:** Mathematics
- **Year:** 2023
- **Volume:** 11
- **Issue:** 16
- **Pages:** 3443
- **Publisher:** MDPI AG
- **DOI:** [10.3390/math11163443](https://doi.org/10.3390/math11163443)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Alcaraz_Tapia_2023,
  title={{Design of a Port-Hamiltonian Control for an Alt-Azimuth Liquid–Mirror Telescope}},
  volume={11},
  ISSN={2227-7390},
  DOI={10.3390/math11163443},
  number={16},
  journal={Mathematics},
  publisher={MDPI AG},
  author={Alcaraz Tapia, Juan Cristobal and Castañeda, Carlos E. and Vargas Rodriguez, Héctor and Esquivel, P.},
  year={2023},
  pages={3443}
}
{% endraw %}
{% endhighlight %}
 
## References
- Hickson, P. et al. The Large Zenith Telescope: A 6 m Liquid‐Mirror Telescope. Publications of the Astronomical Society of the Pacific vol. 119 444–455 (2007) -- [10.1086/517621](https://doi.org/10.1086/517621)
- Borra, E. F. Liquid mirrors. Canadian Journal of Physics vol. 73 109–125 (1995) -- [10.1139/p95-017](https://doi.org/10.1139/p95-017)
- Surdej, J. et al. The 4-m International Liquid Mirror Telescope. Bulletin de la Société Royale des Sciences de Liège 68–79 (2018) doi:10.25518/0037-9565.7498 -- [10.25518/0037-9565.7498](https://doi.org/10.25518/0037-9565.7498)
- Spong, M.W., Hutchinson, S., and Vidyasagar, M. (2020). Robot Modeling and Control, John Wiley & Sons.
- Sciavicco, L., and Siciliano, B. (2001). Modelling and Control of Robot Manipulators, Springer Science & Business Media. -- [10.1007/978-1-4471-0449-0](https://doi.org/10.1007/978-1-4471-0449-0)
- Utkin, V., Guldner, J., and Shi, J. (2017). Sliding Mode Control in Electro-Mechanical Systems, CRC Press. -- [10.1201/9781420065619](https://doi.org/10.1201/9781420065619)
- Perruquetti, W., and Barbot, J.P. (2002). Sliding Mode Control in Engineering, Marcel Dekker. -- [10.1201/9780203910856](https://doi.org/10.1201/9780203910856)
- Liu, J. et al. Sliding Mode Control of Grid-Connected Neutral-Point-Clamped Converters Via High-Gain Observer. IEEE Transactions on Industrial Electronics vol. 69 4010–4021 (2022) -- [10.1109/TIE.2021.3070496](https://doi.org/10.1109/TIE.2021.3070496)
- Wang, T., Wang, B., Yu, Y. & Xu, D. Fast High-Order Terminal Sliding-Mode Current Controller for Disturbance Compensation and Rapid Convergence in Induction Motor Drives. IEEE Transactions on Power Electronics vol. 38 9593–9605 (2023) -- [10.1109/TPEL.2023.3277886](https://doi.org/10.1109/TPEL.2023.3277886)
- Wang, B., Wang, T., Yu, Y. & Xu, D. Second-Order Terminal Sliding-Mode Speed Controller for Induction Motor Drives With Nonlinear Control Gain. IEEE Transactions on Industrial Electronics vol. 70 10923–10934 (2023) -- [10.1109/TIE.2022.3231248](https://doi.org/10.1109/TIE.2022.3231248)
- Swikir, A., and Utkin, V. (2016, January 1–4). Chattering analysis of conventional and super twisting sliding mode control algorithm. Proceedings of the 2016 14th International Workshop on Variable Structure Systems (VSS), Nanjing, China. -- [10.1109/VSS.2016.7506898](https://doi.org/10.1109/VSS.2016.7506898)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- [Duindam, V., Macchelli, A., Stramigioli, S., and Bruyninckx, H. (2009). Modeling and Control of Complex Physical Systems the Port-Hamiltonian Approach, Springer.](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Ortega, R., Van der Schaft, A., Maschke, B., and Escobar, G. (1999, January 7–10). Energy-shaping of port-controlled Hamiltonian systems by interconnection. Proceedings of the 38th IEEE Conference on Decision and Control (Cat. No. 99CH36304), Phoenix, AZ, USA.
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/S0005-1098(01)00278-3](https://doi.org/10.1016/S0005-1098(01)00278-3)
- Chi, J., Yu, H. & Yu, J. Hybrid Tracking Control of 2-DOF SCARA Robot via Port-Controlled Hamiltonian and Backstepping. IEEE Access vol. 6 17354–17360 (2018) -- [10.1109/ACCESS.2018.2820681](https://doi.org/10.1109/ACCESS.2018.2820681)
- [Gómez-Estern, F. & Van der Schaft, A. J. Physical Damping in IDA-PBC Controlled Underactuated Mechanical Systems. European Journal of Control vol. 10 451–468 (2004)](physical-damping-in-ida-pbc-controlled-underactuated-mechanical-systems) -- [10.3166/ejc.10.451-468](https://doi.org/10.3166/ejc.10.451-468)
- Donaire, A., Romero, J. G., Ortega, R., Siciliano, B. & Crespo, M. Robust IDA-PBC for underactuated mechanical systems subject to matched disturbances. International Journal of Robust and Nonlinear Control vol. 27 1000–1016 (2016) -- [10.1002/rnc.3615](https://doi.org/10.1002/rnc.3615)
- Acosta, J.Á., Sanchez, M., and Ollero, A. (2014, January 15–17). Robust control of underactuated aerial manipulators via IDA-PBC. Proceedings of the 53rd IEEE Conference on Decision and Control, Los Angeles, CA, USA. -- [10.1109/CDC.2014.7039459](https://doi.org/10.1109/CDC.2014.7039459)
- [Yaghmaei, A. & Yazdanpanah, M. J. Trajectory tracking for a class of contractive port Hamiltonian systems. Automatica vol. 83 331–336 (2017)](trajectory-tracking-for-a-class-of-contractive-port-hamiltonian-systems) -- [10.1016/j.automatica.2017.06.039](https://doi.org/10.1016/j.automatica.2017.06.039)
- Khalil, H.K. (2015). Nonlinear Control, Pearson.
- Dokht Shakibjoo, A., Moradzadeh, M., Moussavi, S. Z., Mohammadzadeh, A. & Vandevelde, L. Load frequency control for multi-area power systems: A new type-2 fuzzy approach based on Levenberg–Marquardt algorithm. ISA Transactions vol. 121 40–52 (2022) -- [10.1016/j.isatra.2021.03.044](https://doi.org/10.1016/j.isatra.2021.03.044)
- Khalil, H.K. (2002). Nonlinear Systems, Patience Hall. [3rd ed.].
- Loukianov, A. G. Robust block decomposition sliding mode control design. Mathematical Problems in Engineering vol. 8 349–365 (2002) -- [10.1080/10241230306732](https://doi.org/10.1080/10241230306732)
- Morfin, O. A. et al. Real-Time SOSM Super-Twisting Combined With Block Control for Regulating Induction Motor Velocity. IEEE Access vol. 6 25898–25907 (2018) -- [10.1109/ACCESS.2018.2812187](https://doi.org/10.1109/ACCESS.2018.2812187)
- Goldstein, H., Poole, C., and Safko, J. (2013). Classical Mechanics Pearson New International Edition, Pearson Education, Limited.
- Nise, N.S. (2020). Control Systems Engineering, John Wiley & Sons.
- Dávila, A., Moreno, J.A., and Fridman, L. (2009, January 15–18). Optimal Lyapunov function selection for reaching time estimation of super twisting algorithm. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) Held Jointly with 2009 28th Chinese Control Conference, Shanghai, China. -- [10.1109/CDC.2009.5400466](https://doi.org/10.1109/CDC.2009.5400466)
- Garduño, O.A.M., Cruz, R.R., Murillo, F.A.V., Betancour, R.R., Hernández, C.E.C., and Téllez, F.O. (2023). Robust cascade controller for the power factor of the three-phase supply and the induction motor velocity. ISA Trans.
- Moché, D.L. (2009). Astronomy, Wiley.
- Morfin, O.A., Castañeda, C.E., Valderrabano-Gonzalez, A., Hernandez-Gonzalez, M., and Valenzuela, F.A. (2017). A real-time SOSM super-twisting technique for a compound DC motor velocity controller. Energies, 10. -- [10.3390/en10091286](https://doi.org/10.3390/en10091286)
- Cristobal, J., Tapia, A., Castañeda, C., and Vargas-Rodríguez, H. (2018, January 21–23). An alternative approach for determining the motor rotation rates for an altazimuth telescope mount. Proceedings of the Herramientas y Tecnologias Especificas Para Beneficio de las Instituciones y Comunidades, Cuernavaca, Mexico.

