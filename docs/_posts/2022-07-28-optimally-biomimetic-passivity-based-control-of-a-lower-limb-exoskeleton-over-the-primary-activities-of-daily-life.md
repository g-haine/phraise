---
layout: post
title: "Optimally Biomimetic Passivity-Based Control of a Lower-Limb Exoskeleton Over the Primary Activities of Daily Life"
date: 2022-07-28 00:00:00 +0100
permalink: optimally-biomimetic-passivity-based-control-of-a-lower-limb-exoskeleton-over-the-primary-activities-of-daily-life
year: 2022
authors: Jianping Lin, Nikhil V. Divekar, Gray C. Thomas, Robert D. Gregg
category: articles
---
 
## Authors
[Jianping Lin](authors/jianping-lin), [Nikhil V. Divekar](authors/nikhil-v-divekar), [Gray C. Thomas](authors/gray-c-thomas), [Robert D. Gregg](authors/robert-d-gregg)
 
## Abstract
Task-specific, trajectory-based control methods commonly used in exoskeletons may be appropriate for individuals with paraplegia, but they overly constrain the volitional motion of individuals with remnant voluntary ability (representing a far larger population). Human-exoskeleton systems can be represented in the form of the Euler-Lagrange equations or, equivalently, the port-controlled Hamiltonian equations to design control laws that provide task-invariant assistance across a continuum of activities/environments by altering energetic properties of the human body. We previously introduced a port-controlled Hamiltonian framework that parameterizes the control law through basis functions related to gravitational and gyroscopic terms, which are optimized to fit normalized able-bodied joint torques across multiple walking gaits on different ground inclines. However, this approach did not have the flexibility to reproduce joint torques for a broader set of activities, including stair climbing and stand-to-sit, due to strict assumptions related to input-output passivity, which ensures the human remains in control of energy growth in the closed-loop dynamics. To provide biomimetic assistance across all primary activities of daily life, this paper generalizes this energy shaping framework by incorporating vertical ground reaction forces and global planar orientation into the basis set, while preserving passivity between the human joint torques and human joint velocities. We present an experimental implementation on a powered knee-ankle exoskeleton used by three able-bodied human subjects during walking on various inclines, ramp ascent/descent, and stand-to-sit, demonstrating the versatility of this control approach and its effect on muscular effort.
 
## Citation
- **Journal:** IEEE Open Journal of Control Systems
- **Year:** 2022
- **Volume:** 1
- **Issue:** 
- **Pages:** 15--28
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/ojcsys.2022.3165733](https://doi.org/10.1109/ojcsys.2022.3165733)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Lin_2022,
  title={{Optimally Biomimetic Passivity-Based Control of a Lower-Limb Exoskeleton Over the Primary Activities of Daily Life}},
  volume={1},
  ISSN={2694-085X},
  DOI={10.1109/ojcsys.2022.3165733},
  journal={IEEE Open Journal of Control Systems},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Lin, Jianping and Divekar, Nikhil V. and Thomas, Gray C. and Gregg, Robert D.},
  year={2022},
  pages={15--28}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/optimally-biomimetic-passivity-based-control-of-a-lower-limb-exoskeleton-over-the-primary-activities-of-daily-life.bib)
 
## References
- Chen, S. et al. Adaptive Robust Cascade Force Control of 1-DOF Hydraulic Exoskeleton for Human Performance Augmentation. IEEE/ASME Trans. Mechatron. 22, 589–600 (2017) -- [10.1109/tmech.2016.2614987](https://doi.org/10.1109/tmech.2016.2614987)
- Laschowski, B., Razavian, R. S. & McPhee, J. Simulation of Stand-to-Sit Biomechanics for Robotic Exoskeletons and Prostheses With Energy Regeneration. IEEE Trans. Med. Robot. Bionics 3, 455–462 (2021) -- [10.1109/tmrb.2021.3058323](https://doi.org/10.1109/tmrb.2021.3058323)
- Yu, S. et al. Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton With High Backdrivability and High Bandwidth. IEEE/ASME Trans. Mechatron. 25, 1794–1802 (2020) -- [10.1109/tmech.2020.2995134](https://doi.org/10.1109/tmech.2020.2995134)
- Embry, K. R., Villarreal, D. J., Macaluso, R. L. & Gregg, R. D. Modeling the Kinematics of Human Locomotion Over Continuously Varying Speeds and Inclines. IEEE Trans. Neural Syst. Rehabil. Eng. 26, 2342–2350 (2018) -- [10.1109/tnsre.2018.2879570](https://doi.org/10.1109/tnsre.2018.2879570)
- He, B., Thomas, G. C., Paine, N. & Sentis, L. Modeling and Loop Shaping of Single-Joint Amplification Exoskeleton with Contact Sensing and Series Elastic Actuation. 2019 American Control Conference (ACC) 4580–4587 (2019) doi:10.23919/acc.2019.8814421 -- [10.23919/acc.2019.8814421](https://doi.org/10.23919/acc.2019.8814421)
- Weiss, P., Zenker, P. & Maehle, E. Feed-forward friction and inertia compensation for improving backdrivability of motors. 2012 12th International Conference on Control Automation Robotics &amp; Vision (ICARCV) 288–293 (2012) doi:10.1109/icarcv.2012.6485173 -- [10.1109/icarcv.2012.6485173](https://doi.org/10.1109/icarcv.2012.6485173)
- Nagarajan, U., Aguirre-Ollinger, G. & Goswami, A. Integral admittance shaping: A unified framework for active exoskeleton control. Robotics and Autonomous Systems 75, 310–324 (2016) -- [10.1016/j.robot.2015.09.015](https://doi.org/10.1016/j.robot.2015.09.015)
- Embry, K. R., Villarreal, D. J. & Gregg, R. D. A unified parameterization of human gait across ambulation modes. 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) 2179–2183 (2016) doi:10.1109/embc.2016.7591161 -- [10.1109/embc.2016.7591161](https://doi.org/10.1109/embc.2016.7591161)
- Murray, R. M., Li, Z. & Sastry, S. S. A Mathematical Introduction to Robotic Manipulation. (CRC Press, 2017). doi:10.1201/9781315136370 -- [10.1201/9781315136370](https://doi.org/10.1201/9781315136370)
- Molinaro, D. D., Kang, I., Camargo, J., Gombolay, M. C. & Young, A. J. Subject-Independent, Biological Hip Moment Estimation During Multimodal Overground Ambulation Using Deep Learning. IEEE Trans. Med. Robot. Bionics 4, 219–229 (2022) -- [10.1109/tmrb.2022.3144025](https://doi.org/10.1109/tmrb.2022.3144025)
- Zhu, H., Nesler, C., Divekar, N., Peddinti, V. & Gregg, R. D. Design Principles for Compact, Backdrivable Actuation in Partial-Assist Powered Knee Orthoses. IEEE/ASME Trans. Mechatron. 26, 3104–3115 (2021) -- [10.1109/tmech.2021.3053226](https://doi.org/10.1109/tmech.2021.3053226)
- Camargo, J., Ramanathan, A., Flanagan, W. & Young, A. A comprehensive, open-source dataset of lower limb biomechanics in multiple conditions of stairs, ramps, and level-ground ambulation and transitions. Journal of Biomechanics 119, 110320 (2021) -- [10.1016/j.jbiomech.2021.110320](https://doi.org/10.1016/j.jbiomech.2021.110320)
- Lv, G., Zhu, H. & Gregg, R. D. On the Design and Control of Highly Backdrivable Lower-Limb Exoskeletons: A Discussion of Past and Ongoing Work. IEEE Control Syst. 38, 88–113 (2018) -- [10.1109/mcs.2018.2866605](https://doi.org/10.1109/mcs.2018.2866605)
- Braun, D. J. & Goldfarb, M. A Control Approach for Actuated Dynamic Walking in Biped Robots. IEEE Trans. Robot. 25, 1292–1303 (2009) -- [10.1109/tro.2009.2028762](https://doi.org/10.1109/tro.2009.2028762)
- kolakowsky-hayner, Safety and feasibility of using the EksoTM bionic exoskeleton to aid ambulation after spinal cord injury. The Spine Journal (2013)
- Zeilig, G. et al. Safety and tolerance of the ReWalk™exoskeleton suit for ambulation by people with complete spinal cord injury: A pilot study. The Journal of Spinal Cord Medicine 35, 96–101 (2012) -- [10.1179/2045772312y.0000000003](https://doi.org/10.1179/2045772312y.0000000003)
- Aguirre-Ollinger, G., Colgate, J. E., Peshkin, M. A. & Goswami, A. Inertia Compensation Control of a One-Degree-of-Freedom Exoskeleton for Lower-Limb Assistance: Initial Experiments. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 68–77 (2012) -- [10.1109/tnsre.2011.2176960](https://doi.org/10.1109/tnsre.2011.2176960)
- Kumar, S., Zwall, M., Bolivar-Nieto, E., Gregg, R. D. & Gans, N. Extremum Seeking Control for Stiffness Auto-Tuning of a Quasi-Passive Ankle Exoskeleton. IEEE Robot. Autom. Lett. 1–1 (2020) doi:10.1109/lra.2020.3001541 -- [10.1109/lra.2020.3001541](https://doi.org/10.1109/lra.2020.3001541)
- Thomas, G. C. et al. Formulating and Deploying Strength Amplification Controllers for Lower-Body Walking Exoskeletons. Front. Robot. AI 8, (2021) -- [10.3389/frobt.2021.720231](https://doi.org/10.3389/frobt.2021.720231)
- yang, Electromyographic amplitude normalization methods: Improving their sensitivity as diagnostic tools in gait analysis. Arch Phys Med Rehabil (1984)
- Bloch, A. M., Leonard, N. E. & Marsden, J. E. Stabilization of mechanical systems using controlled Lagrangians. Proceedings of the 36th IEEE Conference on Decision and Control vol. 3 2356–2361 -- [10.1109/cdc.1997.657135](https://doi.org/10.1109/cdc.1997.657135)
- Murray, S. A., Ha, K. H., Hartigan, C. & Goldfarb, M. An Assistive Control Approach for a Lower-Limb Exoskeleton to Facilitate Recovery of Walking Following Stroke. IEEE Trans. Neural Syst. Rehabil. Eng. 23, 441–449 (2015) -- [10.1109/tnsre.2014.2346193](https://doi.org/10.1109/tnsre.2014.2346193)
- Divekar, N. V., Lin, J., Nesler, C., Borboa, S. & Gregg, R. D. A Potential Energy Shaping Controller with Ground Reaction Force Feedback for a Multi-Activity Knee-Ankle Exoskeleton. 2020 8th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob) 997–1003 (2020) doi:10.1109/biorob49111.2020.9224341 -- [10.1109/biorob49111.2020.9224341](https://doi.org/10.1109/biorob49111.2020.9224341)
- Lv, G. & Gregg, R. D. Underactuated Potential Energy Shaping With Contact Constraints: Application to a Powered Knee-Ankle Orthosis. IEEE Trans. Contr. Syst. Technol. 26, 181–193 (2018) -- [10.1109/tcst.2016.2646319](https://doi.org/10.1109/tcst.2016.2646319)
- Lv, G., Lin, J. & Gregg, R. D. Trajectory-Free Control of Lower-Limb Exoskeletons Through Underactuated Total Energy Shaping. IEEE Access 9, 95427–95443 (2021) -- [10.1109/access.2021.3094979](https://doi.org/10.1109/access.2021.3094979)
- Lin, J., Lv, G. & Gregg, R. D. Contact-Invariant Total Energy Shaping Control for Powered Exoskeletons. 2019 American Control Conference (ACC) 664–670 (2019) doi:10.23919/acc.2019.8815003 -- [10.23919/acc.2019.8815003](https://doi.org/10.23919/acc.2019.8815003)
- Ortega, R., Loría, A., Nicklasson, P. J. & Sira-Ramírez, H. Passivity-Based Control of Euler-Lagrange Systems. Communications and Control Engineering (Springer London, 1998). doi:10.1007/978-1-4471-3603-3 -- [10.1007/978-1-4471-3603-3](https://doi.org/10.1007/978-1-4471-3603-3)
- Lenzi, T., Carrozza, M. C. & Agrawal, S. K. Powered Hip Exoskeletons Can Reduce the User’s Hip and Ankle Muscle Activations During Walking. IEEE Trans. Neural Syst. Rehabil. Eng. 21, 938–948 (2013) -- [10.1109/tnsre.2013.2248749](https://doi.org/10.1109/tnsre.2013.2248749)
- MacLean, M. K. & Ferris, D. P. Human muscle activity and lower limb biomechanics of overground walking at varying levels of simulated reduced gravity and gait speeds. PLoS ONE 16, e0253467 (2021) -- [10.1371/journal.pone.0253467](https://doi.org/10.1371/journal.pone.0253467)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Putting energy back in control. IEEE Control Syst. 21, 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- Lin, J., Divekar, N., Lv, G. & Gregg, R. D. Energy Shaping Control with Virtual Spring and Damper for Powered Exoskeletons. 2019 IEEE 58th Conference on Decision and Control (CDC) 3039–3045 (2019) doi:10.1109/cdc40024.2019.9029624 -- [10.1109/cdc40024.2019.9029624](https://doi.org/10.1109/cdc40024.2019.9029624)
- khalil, Nonlinear Systems (2002)
- [Lin, J., Divekar, N. V., Lv, G. & Gregg, R. D. Optimal Task-Invariant Energetic Control for a Knee-Ankle Exoskeleton. IEEE Control Syst. Lett. 5, 1711–1716 (2021)](optimal-task-invariant-energetic-control-for-a-knee-ankle-exoskeleton) -- [10.1109/lcsys.2020.3043838](https://doi.org/10.1109/lcsys.2020.3043838)
- Lee, Y. et al. Flexible sliding frame for gait enhancing mechatronic system (GEMS). 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) 598–602 (2016) doi:10.1109/embc.2016.7590773 -- [10.1109/embc.2016.7590773](https://doi.org/10.1109/embc.2016.7590773)
- Mooney, L. M., Rouse, E. J. & Herr, H. M. Autonomous exoskeleton reduces metabolic cost of human walking during load carriage. J NeuroEngineering Rehabil 11, (2014) -- [10.1186/1743-0003-11-80](https://doi.org/10.1186/1743-0003-11-80)
- Wang, J. et al. Comfort-Centered Design of a Lightweight and Backdrivable Knee Exoskeleton. IEEE Robot. Autom. Lett. 3, 4265–4272 (2018) -- [10.1109/lra.2018.2864352](https://doi.org/10.1109/lra.2018.2864352)
- Yan, T., Cempini, M., Oddo, C. M. & Vitiello, N. Review of assistive strategies in powered lower-limb orthoses and exoskeletons. Robotics and Autonomous Systems 64, 120–136 (2015) -- [10.1016/j.robot.2014.09.032](https://doi.org/10.1016/j.robot.2014.09.032)
- Harib, O. et al. Feedback Control of an Exoskeleton for Paraplegics: Toward Robustly Stable, Hands-Free Dynamic Walking. IEEE Control Syst. 38, 61–87 (2018) -- [10.1109/mcs.2018.2866604](https://doi.org/10.1109/mcs.2018.2866604)
- Kusuda, Y. In quest of mobility – Honda to develop walking assist devices. Industrial Robot: An International Journal 36, 537–539 (2009) -- [10.1108/01439910910994597](https://doi.org/10.1108/01439910910994597)
- Tucker, M. R. et al. Control strategies for active lower extremity prosthetics and orthotics: a review. J NeuroEngineering Rehabil 12, 1 (2015) -- [10.1186/1743-0003-12-1](https://doi.org/10.1186/1743-0003-12-1)
- millington, Biomechanical analysis of the sit-to-stand motion in elderly persons. Arch Phys Med Rehabil (1992)

