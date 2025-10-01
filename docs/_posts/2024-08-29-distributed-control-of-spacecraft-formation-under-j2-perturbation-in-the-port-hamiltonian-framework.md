---
title: "Distributed control of spacecraft formation under \\\\( J2 \\\\) perturbation in the port-Hamiltonian framework"
date: 2024-08-29 00:00:00 +0100
permalink: distributed-control-of-spacecraft-formation-under-j2-perturbation-in-the-port-hamiltonian-framework
year: 2024
authors: Wenkang Hao, Qifeng Chen, Caisheng Wei, Yuxin Liao
category: articles
tags:
  - Port-Hamiltonian system
  - \\( J2 \\) perturbation
  - Nonlinear model
  - Spacecraft formation
  - Distributed
  - Passive control
---
 
## Authors
[Wenkang Hao](authors/wenkang-hao), [Qifeng Chen](authors/qifeng-chen), [Caisheng Wei](authors/caisheng-wei), [Yuxin Liao](authors/yuxin-liao)
 
## Abstract
To control the relative position and relative velocity of spacecraft formation, a time-varying nonlinear relative motion model under J 2 perturbation in an elliptical orbit is established in the port-Hamiltonian (PH) framework, and a distributed control law for spacecraft formation is developed using the consensus algorithm for parameter estimation and the passivity-based control (PBC) method based on the state-error interconnection and damping assignment (IDA) technique. First, the influence of J 2 perturbation on the potential energy and orbit parameters in the model is considered when the relative motion model is built in the PH frame, and the expression of the relative motion acceleration under J 2 perturbation is given. Second, to solve the problem that the state of the chief spacecraft cannot be directly obtained from the deputy spacecraft under distributed communication, a consensus-based parameter estimation method is introduced, the estimated parameter of the chief spacecraft is applied to the relative motion model in the PH frame, and a state error model with the estimated parameters derived from the consistency algorithm is established. Then, after the stability analysis is conducted on the desired PH system containing the estimated parameter values, the desired Hamiltonian energy function with the estimated parameters is designed according to the time-varying errors of the relative equilibrium states of the deputy spacecraft and the errors between deputy spacecraft, and the distributed control law of spacecraft formation is derived based on the state-error IDA-PBC method. Finally, the expected relative motion trajectory designed based on the TH equation is used to simulate a spacecraft formation under J 2 perturbation, and the results indicate that the spacecraft can quickly converge to the expected formation under the influence of the control law.
 
## Keywords
Port-Hamiltonian system; \\( J2 \\) perturbation; Nonlinear model; Spacecraft formation; Distributed; Passive control
 
## Citation
- **Journal:** Advances in Space Research
- **Year:** 2024
- **Volume:** 74
- **Issue:** 11
- **Pages:** 5767--5778
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.asr.2024.08.061](https://doi.org/10.1016/j.asr.2024.08.061)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Hao_2024,
  title={{Distributed control of spacecraft formation under <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si14.svg"><mml:mrow><mml:msub><mml:mrow><mml:mi>J</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math> perturbation in the port-Hamiltonian framework}},
  volume={74},
  ISSN={0273-1177},
  DOI={10.1016/j.asr.2024.08.061},
  number={11},
  journal={Advances in Space Research},
  publisher={Elsevier BV},
  author={Hao, Wenkang and Chen, Qifeng and Wei, Caisheng and Liao, Yuxin},
  year={2024},
  pages={5767--5778}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/distributed-control-of-spacecraft-formation-under-j2-perturbation-in-the-port-hamiltonian-framework.bib)
 
## References
- Alfriend, Chapter 4 - nonlinear models of relative dynamics. (2010)
- [Borja, P., Ortega, R. & Scherpen, J. M. A. New Results on Stabilization of Port-Hamiltonian Systems via PID Passivity-Based Control. IEEE Transactions on Automatic Control vol. 66 625–636 (2021)](new-results-on-stabilization-of-port-hamiltonian-systems-via-pid-passivity-based-control) -- [10.1109/tac.2020.2986731](https://doi.org/10.1109/tac.2020.2986731)
- Cao, L. & Chen, X. Minimum sliding mode error feedback control for inner-formation satellite system with J 2 and small eccentricity. Science China Information Sciences vol. 59 (2016) -- [10.1007/s11432-016-5573-1](https://doi.org/10.1007/s11432-016-5573-1)
- Chen, J., Wu, B., Sun, Z. & Wang, D. Distributed safe trajectory optimization for large-scale spacecraft formation reconfiguration. Acta Astronautica vol. 214 125–136 (2024) -- [10.1016/j.actaastro.2023.10.012](https://doi.org/10.1016/j.actaastro.2023.10.012)
- Chen, Q., Meng, Y., Liao, Y. & Wei, C. Intersatellite Distance-Keeping Control Based on Relative Motion Geometry. Journal of Guidance, Control, and Dynamics vol. 46 177–185 (2023) -- [10.2514/1.g006765](https://doi.org/10.2514/1.g006765)
- [Fahmi, J.-M. & Woolsey, C. A. Port-Hamiltonian Flight Control of a Fixed-Wing Aircraft. IEEE Transactions on Control Systems Technology vol. 30 408–415 (2022)](port-hamiltonian-flight-control-of-a-fixed-wing-aircraft) -- [10.1109/tcst.2021.3059928](https://doi.org/10.1109/tcst.2021.3059928)
- [Fujimoto, K., Sakata, N., Maruta, I. & Ferguson, J. A Passivity Based Sliding Mode Controller for Simple Port-Hamiltonian Systems. IEEE Control Systems Letters vol. 5 839–844 (2021)](a-passivity-based-sliding-mode-controller-for-simple-port-hamiltonian-systems) -- [10.1109/lcsys.2020.3005327](https://doi.org/10.1109/lcsys.2020.3005327)
- Inalhan, G., Tillerson, M. & How, J. P. Relative Dynamics and Control of Spacecraft Formations in Eccentric Orbits. Journal of Guidance, Control, and Dynamics vol. 25 48–59 (2002) -- [10.2514/2.4874](https://doi.org/10.2514/2.4874)
- [Javanmardi, N., Yaghmaei, A. & Yazdanpanah, M. J. Spacecraft formation flying in the port-Hamiltonian framework. Nonlinear Dynamics vol. 99 2765–2783 (2020)](spacecraft-formation-flying-in-the-port-hamiltonian-framework) -- [10.1007/s11071-019-05445-0](https://doi.org/10.1007/s11071-019-05445-0)
- Jia, Q., Shu, R., Ahn, C. K. & Zhang, C. Learning Neural Network-Based Fault-Tolerant Formation Control for Elliptical Orbit Spacecraft. IEEE Transactions on Aerospace and Electronic Systems vol. 60 1937–1950 (2024) -- [10.1109/taes.2023.3344390](https://doi.org/10.1109/taes.2023.3344390)
- [Jin, L., Yu, S., Zhao, Q., Shi, G. & Wu, X. Fixed-time <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si1.svg"><mml:mrow><mml:msub><mml:mi>H</mml:mi><mml:mi>∞</mml:mi></mml:msub></mml:mrow></mml:math> tracking control of unmanned underwater vehicles with disturbance rejection via Port-Hamiltonian framework. Ocean Engineering vol. 293 116533 (2024)](fixed-time-h-infty-tracking-control-of-unmanned-underwater-vehicles-with-disturbance) -- [10.1016/j.oceaneng.2023.116533](https://doi.org/10.1016/j.oceaneng.2023.116533)
- Li, S., Zhang, X., Liu, W. & Cui, N. Optimization-based iterative and robust strategy for spacecraft relative navigation in elliptical orbit. Aerospace Science and Technology vol. 133 108138 (2023) -- [10.1016/j.ast.2023.108138](https://doi.org/10.1016/j.ast.2023.108138)
- [Lv, C., Chen, J., Yu, H., Chi, J. & Yang, Z. Adaptive NN state error PCH trajectory tracking control for unmanned surface vessel with uncertainties and input saturation. Asian Journal of Control vol. 25 3903–3919 (2023)](adaptive-nn-state-error-pch-trajectory-tracking-control-for-unmanned-surface-vessel-with-uncertainties-and-input-saturation) -- [10.1002/asjc.3076](https://doi.org/10.1002/asjc.3076)
- [Lv, C. et al. Robust state‐error port‐controlled Hamiltonian trajectory tracking control for unmanned surface vehicle with disturbance uncertainties. Asian Journal of Control vol. 24 320–332 (2020)](robust-state-error-port-controlled-hamiltonian-trajectory-tracking-control-for-unmanned-surface-vehicle-with-disturbance-uncertainties) -- [10.1002/asjc.2467](https://doi.org/10.1002/asjc.2467)
- Menegatti, D., Giuseppi, A. & Pietrabissa, A. Model Predictive Control for Collision-free Spacecraft Formation with Artificial Potential Functions. 2022 30th Mediterranean Conference on Control and Automation (MED) 564–570 (2022) doi:10.1109/med54222.2022.9837252 -- [10.1109/med54222.2022.9837252](https://doi.org/10.1109/med54222.2022.9837252)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control vol. 10 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Pereira, P., Guerreiro, B. J. & Lourenço, P. Distributed Model Predictive Control Method for Spacecraft Formation Flying in a Leader–Follower Formation. IEEE Transactions on Aerospace and Electronic Systems vol. 59 3213–3223 (2023) -- [10.1109/taes.2022.3224692](https://doi.org/10.1109/taes.2022.3224692)
- [Pham, T. H., Vu, N. M. T., Prodan, I. & Lefèvre, L. A combined Control by Interconnection—Model Predictive Control design for constrained Port-Hamiltonian systems. Systems &amp; Control Letters vol. 167 105336 (2022)](a-combined-control-by-interconnection-model-predictive-control-design-for-constrained-port-hamiltonian-systems) -- [10.1016/j.sysconle.2022.105336](https://doi.org/10.1016/j.sysconle.2022.105336)
- [Rashad, R., Califano, F. & Stramigioli, S. Port-Hamiltonian Passivity-Based Control on SE(3) of a Fully Actuated UAV for Aerial Physical Interaction Near-Hovering. IEEE Robotics and Automation Letters vol. 4 4378–4385 (2019)](port-hamiltonian-passivity-based-control-on-se-3-of-a-fully-actuated-uav-for-aerial-physical-interaction-near-hovering) -- [10.1109/lra.2019.2932864](https://doi.org/10.1109/lra.2019.2932864)
- Ren, W. Multi-vehicle consensus with a time-varying reference state. Systems &amp; Control Letters vol. 56 474–483 (2007) -- [10.1016/j.sysconle.2007.01.002](https://doi.org/10.1016/j.sysconle.2007.01.002)
- van der Schaft, (2017)
- van der Schaft, (2014)
- [Schwerdtner, P. & Voigt, M. Fixed-order H-infinity controller design for port-Hamiltonian systems. Automatica vol. 152 110918 (2023)](fixed-order-h-infinity-controller-design-for-port-hamiltonian-systems) -- [10.1016/j.automatica.2023.110918](https://doi.org/10.1016/j.automatica.2023.110918)
- Sun, G., Zhou, M. & Jiang, X. Non-cooperative spacecraft proximity control considering target behavior uncertainty. Astrodynamics vol. 6 399–411 (2022) -- [10.1007/s42064-022-0133-5](https://doi.org/10.1007/s42064-022-0133-5)
- Sun, J., Meng, Y., Huang, J., Liu, F. & Li, S. Distributed cooperative control with collision avoidance for spacecraft swarm reconfiguration via reinforcement learning. Acta Astronautica vol. 205 95–109 (2023) -- [10.1016/j.actaastro.2023.01.017](https://doi.org/10.1016/j.actaastro.2023.01.017)
- [Wang, J., Zheng, W., Zhou, Q. & Shao, J. PID Passive-Based Control of Spacecraft Formation Flying in the Port-Hamiltonian Framework. 2023 42nd Chinese Control Conference (CCC) 820–825 (2023) doi:10.23919/ccc58697.2023.10240864](pid-passive-based-control-of-spacecraft-formation-flying-in-the-port-hamiltonian-framework) -- [10.23919/ccc58697.2023.10240864](https://doi.org/10.23919/ccc58697.2023.10240864)
- Wang, W. Distributed Formation Control for Multiple Spacecraft with Event-triggered Communication. 2023 IEEE 13th International Conference on Electronics Information and Emergency Communication (ICEIEC) 246–250 (2023) doi:10.1109/iceiec58029.2023.10200085 -- [10.1109/iceiec58029.2023.10200085](https://doi.org/10.1109/iceiec58029.2023.10200085)
- Wang, W., Li, C. & Guo, Y. Relative position coordinated control for spacecraft formation flying with obstacle/collision avoidance. Nonlinear Dynamics vol. 104 1329–1342 (2021) -- [10.1007/s11071-021-06348-9](https://doi.org/10.1007/s11071-021-06348-9)
- Wu, J., Qiu, S., Liu, M., Li, H. & Liu, Y. Finite-time velocity-free relative position coordinated control of spacecraft formation with dynamic event triggered transmission. Mathematical Biosciences and Engineering vol. 19 6883–6906 (2022) -- [10.3934/mbe.2022324](https://doi.org/10.3934/mbe.2022324)
- Xu, G. & Wang, D. Nonlinear Dynamic Equations of Satellite Relative Motion  Around an Oblate Earth. Journal of Guidance, Control, and Dynamics vol. 31 1521–1524 (2008) -- [10.2514/1.33616](https://doi.org/10.2514/1.33616)
- YANG, C., ZHANG, H. & FU, W. Pattern control for large-scale spacecraft swarms in elliptic orbits via density fields. Chinese Journal of Aeronautics vol. 35 367–379 (2022) -- [10.1016/j.cja.2021.03.020](https://doi.org/10.1016/j.cja.2021.03.020)
- ZHENG, M., LUO, J. & DANG, Z. Optimal impulsive rendezvous for highly elliptical orbits using linear primer vector theory. Chinese Journal of Aeronautics vol. 37 194–207 (2024) -- [10.1016/j.cja.2023.09.025](https://doi.org/10.1016/j.cja.2023.09.025)
- Zhou, H., Jiao, B., Dang, Z. & Yuan, J. Parametric formation control of multiple nanosatellites for cooperative observation of China Space Station. Astrodynamics vol. 8 77–95 (2024) -- [10.1007/s42064-023-0173-5](https://doi.org/10.1007/s42064-023-0173-5)

