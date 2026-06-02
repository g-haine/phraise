---
title: "Hamiltonian-based energy shaping with attention-augmented fourier neural operators for adaptive torque control in ankle rehabilitation robot"
date: 2026-05-27 00:00:00 +0100
permalink: hamiltonian-based-energy-shaping-with-attention-augmented-fourier-neural-operators-for-adaptive-torque-control-in-ankle-rehabilitation-robot
year: 2026
authors: Naveed Ahmad Khan, Prashant K. Jamwal, Girija Chetty, Shahid Hussain
category: articles
tags:
  - attention-augmented fourier neural, deep learning, energy shaping control, human-robot interaction, operator, shaped potential energy, torque control, trajectory tracking
---
 
## Authors
[Naveed Ahmad Khan](authors/naveed-ahmad-khan), [Prashant K. Jamwal](authors/prashant-k-jamwal), [Girija Chetty](authors/girija-chetty), [Shahid Hussain](authors/shahid-hussain)
 
## Abstract
In rehabilitation robotics, control of energy flow is not merely a stability requirement but a therapeutic tool that shapes the quality and safety of human-robot interaction (HRI). The precise modulation of potential and kinetic energy within the coupled human–robot system governs how assistance is provided, how disturbances are rejected, and how patient effort is encouraged. Energy shaping approaches enable the controller to sculpt an artificial energy landscape anchored at a prescribed reference posture, so that restorative torques emerge naturally from the gradient of the shaped potential and disturbance-rich interactions are regulated within bounded, passive operating limits. This study presents a novel deep learning-based energy shaping framework for torque control in a three-degree-of-freedom (DOF) ankle rehabilitation robot. The proposed method is rooted in port-Hamiltonian mechanics. It employs interconnection and damping assignment-passivity-based control (IDA-PBC) to shape the energy landscape of the system, promoting practical stability and safe patient interaction. To address the limitations of static or heuristic energy shaping, we introduce a physics-informed data-driven approach in which the potential energy function is dynamically constructed through an Attention-Augmented Fourier Neural Operator (AFNO). This architecture learns mappings from spatiotemporal sensor data, including joint kinematics and interaction torques, to optimal shaping parameters that define the control energy field. The control strategy was experimentally validated on an ankle rehabilitation robot with ten healthy subjects (eight male, two female, aged 25–43), performing controlled movements across dorsiflexion/plantarflexion, inversion/eversion, and abduction/adduction. Experimental data confirmed that the shaped potential energy fields successfully guided joint trajectories toward the prescribed reference posture under disturbance-rich interaction conditions, while maintaining passivity and minimizing unnecessary energy expenditure.
 
## Keywords
attention-augmented fourier neural, deep learning, energy shaping control, human-robot interaction, operator, shaped potential energy, torque control, trajectory tracking
 
## Citation
- **Journal:** Advanced Engineering Informatics
- **Year:** 2026
- **Volume:** 75
- **Issue:** 
- **Pages:** 104857
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.aei.2026.104857](https://doi.org/10.1016/j.aei.2026.104857)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Khan_2026,
  title={{Hamiltonian-based energy shaping with attention-augmented fourier neural operators for adaptive torque control in ankle rehabilitation robot}},
  volume={75},
  ISSN={1474-0346},
  DOI={10.1016/j.aei.2026.104857},
  journal={Advanced Engineering Informatics},
  publisher={Elsevier BV},
  author={Khan, Naveed Ahmad and Jamwal, Prashant K. and Chetty, Girija and Hussain, Shahid},
  year={2026},
  pages={104857}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/hamiltonian-based-energy-shaping-with-attention-augmented-fourier-neural-operators-for-adaptive-torque-control-in-ankle-rehabilitation-robot.bib)
 
## References
- Ren H, Zhang H (2023) Control strategy based on improved fuzzy algorithm for energy control of wrist rehabilitation robot. Alexandria Engineering Journal 77:634–644. https://doi.org/10.1016/j.aej.2023.07.02 -- [10.1016/j.aej.2023.07.024](https://doi.org/10.1016/j.aej.2023.07.024)
- Zhang S, Fan L, Ye J, Chen G, Fu C, Leng Y (2023) An Intelligent Rehabilitation Assessment Method for Stroke Patients Based on Lower Limb Exoskeleton Robot. IEEE Trans Neural Syst Rehabil Eng 31:3106–3117. https://doi.org/10.1109/tnsre.2023.329867 -- [10.1109/tnsre.2023.3298670](https://doi.org/10.1109/tnsre.2023.3298670)
- Rezayat Sorkhabadi SM, Smith M, Khodmbashi R, Lopez R, Raasch M, Maruyama T, Kwasnica C, Zhang W (2023) Learning Post-Stroke Gait Training Strategies by Modeling Patient-Therapist Interaction. IEEE Trans Neural Syst Rehabil Eng 31:1687–1696. https://doi.org/10.1109/tnsre.2023.325379 -- [10.1109/tnsre.2023.3253795](https://doi.org/10.1109/tnsre.2023.3253795)
- Lyu S, Cheah CC (2020) Human–Robot Interaction Control Based on a General Energy Shaping Method. IEEE Trans Contr Syst Technol 28(6):2445–2460. https://doi.org/10.1109/tcst.2019.294952 -- [10.1109/tcst.2019.2949525](https://doi.org/10.1109/tcst.2019.2949525)
- Fu J, Maimone G, Iovene E, Zhao J, Redaelli A, Ferrigno G, De Momi E (2025) Human-Inspired Active Compliant and Passive Shared Control Framework for Robotic Contact-Rich Tasks in Medical Applications. IEEE Trans Robot 41:2549–2568. https://doi.org/10.1109/tro.2025.354849 -- [10.1109/tro.2025.3548493](https://doi.org/10.1109/tro.2025.3548493)
- Lv G, Hanqi Zhu, Elery T, Luwei Li, Gregg RD (2016) Experimental implementation of underactuated potential energy shaping on a powered ankle-foot orthosis. 2016 IEEE International Conference on Robotics and Automation (ICRA) 3493–350 -- [10.1109/icra.2016.7487529](https://doi.org/10.1109/icra.2016.7487529)
- Lv G, Gregg RD (2018) Underactuated Potential Energy Shaping With Contact Constraints: Application to a Powered Knee-Ankle Orthosis. IEEE Trans Contr Syst Technol 26(1):181–193. https://doi.org/10.1109/tcst.2016.264631 -- [10.1109/tcst.2016.2646319](https://doi.org/10.1109/tcst.2016.2646319)
- Lin, Energy shaping control with virtual spring and damper for powered exoskeletons. (2019)
- Walters, An energetic approach to task-invariant ankle exoskeleton control. (2023)
- Lin J, Thomas GC, Divekar NV, Peddinti V, Gregg RD (2024) A Modular Framework for Task-Agnostic, Energy Shaping Control of Lower Limb Exoskeletons. IEEE Trans Contr Syst Technol 32(6):2359–2375. https://doi.org/10.1109/tcst.2024.342990 -- [10.1109/tcst.2024.3429908](https://doi.org/10.1109/tcst.2024.3429908)
- Khan NA, Jamwal PK, Hussain F, Spratford W, Hussain S (2025) Quantum Enhanced Transformer Network for Learning Transactive Energy During Physical Human-Robot Interaction. IEEE Trans Human-Mach Syst 55(6):930–939. https://doi.org/10.1109/thms.2025.362127 -- [10.1109/thms.2025.3621275](https://doi.org/10.1109/thms.2025.3621275)
- J. Harandi MR, Hassani A, Hosseini MI, Taghirad HD (2024) Adaptive Position Feedback Control of Parallel Robots in the Presence of Kinematics and Dynamics Uncertainties. IEEE Trans Automat Sci Eng 21(1):989–999. https://doi.org/10.1109/tase.2023.323589 -- [10.1109/tase.2023.3235895](https://doi.org/10.1109/tase.2023.3235895)
- Harandi MRJ, Taghirad HD (2023) Stabilization of a class of underactuated parallel robots via energy shaping: Application to cable driven manipulators. Automatica 156:111201. https://doi.org/10.1016/j.automatica.2023.11120 -- [10.1016/j.automatica.2023.111201](https://doi.org/10.1016/j.automatica.2023.111201)
- Tamburella F, Tagliamonte NL, Pisotta I, Masciullo M, Arquilla M, van Asseldonk EHF, van der Kooij H, Wu AR, Dzeladini F, Ijspeert AJ, Molinari M (2020) Neuromuscular Controller Embedded in a Powered Ankle Exoskeleton: Effects on Gait, Clinical Features and Subjective Perspective of Incomplete Spinal Cord Injured Subjects. IEEE Trans Neural Syst Rehabil Eng 28(5):1157–1167. https://doi.org/10.1109/tnsre.2020.298479 -- [10.1109/tnsre.2020.2984790](https://doi.org/10.1109/tnsre.2020.2984790)
- Chen K, Yi J, Song D (2023) Gaussian-Process-Based Control of Underactuated Balance Robots With Guaranteed Performance. IEEE Trans Robot 39(1):572–589. https://doi.org/10.1109/tro.2022.320362 -- [10.1109/tro.2022.3203625](https://doi.org/10.1109/tro.2022.3203625)
- Khader SA, Yin H, Falco P, Kragic D (2021) Learning Deep Energy Shaping Policies for Stability-Guaranteed Manipulation. IEEE Robot Autom Lett 6(4):8583–8590. https://doi.org/10.1109/lra.2021.311196 -- [10.1109/lra.2021.3111962](https://doi.org/10.1109/lra.2021.3111962)
- Lu R, Jiang Z, Wu H, Ding Y, Wang D, Zhang H-T (2023) Reward Shaping-Based Actor–Critic Deep Reinforcement Learning for Residential Energy Management. IEEE Trans Ind Inf 19(3):2662–2673. https://doi.org/10.1109/tii.2022.318380 -- [10.1109/tii.2022.3183802](https://doi.org/10.1109/tii.2022.3183802)
- Viquerat J, Rabault J, Kuhnle A, Ghraieb H, Larcher A, Hachem E (2021) Direct shape optimization through deep reinforcement learning. Journal of Computational Physics 428:110080. https://doi.org/10.1016/j.jcp.2020.11008 -- [10.1016/j.jcp.2020.110080](https://doi.org/10.1016/j.jcp.2020.110080)
- Khan NA, Goyal T, Hussain F, Jamwal PK, Hussain S (2025) Transformer-Based Approach for Predicting Transactive Energy in Neurorehabilitation. IEEE Trans Neural Syst Rehabil Eng 33:46–57. https://doi.org/10.1109/tnsre.2024.351517 -- [10.1109/tnsre.2024.3515175](https://doi.org/10.1109/tnsre.2024.3515175)
- Wang, Transfer learning fourier neural operator for solving parametric frequency-domain wave equations. IEEE Trans. Geosci. Remote Sens. (2024)
- Jamwal PK, Hussain S, Tsoi YH, Ghayesh MH, Xie SQ (2017) Musculoskeletal modelling of human ankle complex: Estimation of ankle joint moments. Clinical Biomechanics 44:75–82. https://doi.org/10.1016/j.clinbiomech.2017.03.01 -- [10.1016/j.clinbiomech.2017.03.010](https://doi.org/10.1016/j.clinbiomech.2017.03.010)
- Jamwal PK, Hussain S, Tsoi YH, Xie SQ (2020) Musculoskeletal Model for Path Generation and Modification of an Ankle Rehabilitation Robot. IEEE Trans Human-Mach Syst 50(5):373–383. https://doi.org/10.1109/thms.2020.298968 -- [10.1109/thms.2020.2989688](https://doi.org/10.1109/thms.2020.2989688)
- Jamwal PK, Xie SQ, Tsoi YH, Aw KC (2010) Forward kinematics modelling of a parallel ankle rehabilitation robot using modified fuzzy inference. Mechanism and Machine Theory 45(11):1537–1554. https://doi.org/10.1016/j.mechmachtheory.2010.06.01 -- [10.1016/j.mechmachtheory.2010.06.017](https://doi.org/10.1016/j.mechmachtheory.2010.06.017)
- Liu Q, Zuo J, Zhu C, Meng W, Ai Q, Xie SQ (2022) Design and Hierarchical Force-Position Control of Redundant Pneumatic Muscles-Cable-Driven Ankle Rehabilitation Robot. IEEE Robot Autom Lett 7(1):502–509. https://doi.org/10.1109/lra.2021.312374 -- [10.1109/lra.2021.3123747](https://doi.org/10.1109/lra.2021.3123747)
- Mishra H, Garofalo G, Giordano AM, De Stefano M, Ott C, Kugi A (2023) Reduced Euler-Lagrange Equations of Floating-Base Robots: Computation, Properties, &amp; Applications. IEEE Trans Robot 39(2):1439–1457. https://doi.org/10.1109/tro.2022.320671 -- [10.1109/tro.2022.3206716](https://doi.org/10.1109/tro.2022.3206716)
- Khan NA, Jamwal PK, Hussain F, Ghayesh MH, Hussain S (2025) Reinforcement Learning-Driven Path Generation for Ankle Rehabilitation Robot Using Musculoskeletal-Informed Energy Optimization. IEEE Trans Neural Syst Rehabil Eng 33:1774–1784. https://doi.org/10.1109/tnsre.2025.356641 -- [10.1109/tnsre.2025.3566418](https://doi.org/10.1109/tnsre.2025.3566418)
- Nalam V, Lee H (2019) Development of a Two-Axis Robotic Platform for the Characterization of Two-Dimensional Ankle Mechanics. IEEE/ASME Trans Mechatron 24(2):459–470. https://doi.org/10.1109/tmech.2019.289247 -- [10.1109/tmech.2019.2892472](https://doi.org/10.1109/tmech.2019.2892472)
- Lachner J, Allmendinger F, Hobert E, Hogan N, Stramigioli S (2021) Energy budgets for coordinate invariant robot control in physical human–robot interaction. The International Journal of Robotics Research 40(8–9):968–985. https://doi.org/10.1177/0278364921101163 -- [10.1177/02783649211011639](https://doi.org/10.1177/02783649211011639)
- [Duong T, Altawaitan A, Stanley J, Atanasov N (2024) Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control. IEEE Trans Robot 40:3695–3715. https://doi.org/10.1109/tro.2024.342843](port-hamiltonian-neural-ode-networks-on-lie-groups-for-robot-dynamics-learning-and-control) -- [10.1109/tro.2024.3428433](https://doi.org/10.1109/tro.2024.3428433)
- [Zeng J, Zhang Z, Qiao W (2014) An Interconnection and Damping Assignment Passivity-Based Controller for a DC–DC Boost Converter With a Constant Power Load. IEEE Trans on Ind Applicat 50(4):2314–2322. https://doi.org/10.1109/tia.2013.229087](an-interconnection-and-damping-assignment-passivity-based-controller-for-a-dc-dc-boost-converter-with-a-constant-power-load) -- [10.1109/tia.2013.2290872](https://doi.org/10.1109/tia.2013.2290872)
- Hu B, Jiang W, Zeng J, Cheng C, He L (2023) FOTCA: hybrid transformer-CNN architecture using AFNO for accurate plant leaf disease image recognition. Front Plant Sci 14. https://doi.org/10.3389/fpls.2023.123190 -- [10.3389/fpls.2023.1231903](https://doi.org/10.3389/fpls.2023.1231903)
- Zhang, A robot-driven computational model for estimating passive ankle torque with subject-specific adaptation. IEEE Trans. Biomed. Eng. (2015)
- Sanz-Pena I, Jeong H, Kim M (2023) Personalized Wearable Ankle Robot Using Modular Additive Manufacturing Design. IEEE Robot Autom Lett 8(8):4935–4942. https://doi.org/10.1109/lra.2023.329052 -- [10.1109/lra.2023.3290529](https://doi.org/10.1109/lra.2023.3290529)

