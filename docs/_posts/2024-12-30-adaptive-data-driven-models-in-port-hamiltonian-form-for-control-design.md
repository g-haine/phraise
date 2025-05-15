---
layout: post
title: "Adaptive Data‐Driven Models in Port‐Hamiltonian Form for Control Design"
date: 2024-12-30 00:00:00 +0100
permalink: adaptive-data-driven-models-in-port-hamiltonian-form-for-control-design
year: 2025
authors: Annika Junker, Julia Timmermann, Ansgar Trächtler
category: articles
---
 
## Authors
[Annika Junker](authors/annika-junker), [Julia Timmermann](authors/julia-timmermann), [Ansgar Trächtler](authors/ansgar-trachtler)
 
## Abstract
Control engineering applications usually require a model that accurately represents the dynamics of the system. In addition to classical physical modeling, powerful data‐driven approaches are gaining popularity. However, the resulting models may not be ideal for control design due to their black‐box structure, which inherently limits interpretability. Formulating the system dynamics in port‐Hamiltonian form is highly beneficial, as its valuable property of passivity enables the straightforward design of globally stable controllers while ensuring physical interpretability. In a recently published article, we presented a method for data‐driven inference of port‐Hamiltonian models for complex mechatronic systems, requiring only fundamental physical prior knowledge. The resulting models accurately represent the nonlinear dynamics of the considered systems and are physically interpretable. In this contribution, we advance our previous work by including two key elements. Firstly, we demonstrate the application of the above described data‐driven PCHD models for controller design. Preserving the port‐Hamiltonian form in the closed loop not only guarantees global stability and robustness but also ensures desired speed and damping characteristics. Since control systems based on output measurements, which are continuously measured during operation due to the feedback structure, we secondly aim to use this data. Thus, we augment the existing modeling strategy with an intelligent adaptation approach to address uncertainties and (un)predictable system changes in mechatronic systems throughout their lifecycle, such as the installation of new components, wear, or temperature fluctuations during operation. Our proposed algorithm for recursively calculated data‐driven port‐Hamiltonian models utilizes a least‐squares approach with extensions such as automatically adjusting the forgetting factor and controlling the covariance matrix trace. We demonstrate the results through model‐based application on an academic example and experimental validation on a test bench.
 
## Citation
- **Journal:** PAMM
- **Year:** 2025
- **Volume:** 25
- **Issue:** 1
- **Pages:** 
- **Publisher:** Wiley
- **DOI:** [10.1002/pamm.202400154](https://doi.org/10.1002/pamm.202400154)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Junker_2024,
  title={{Adaptive Data‐Driven Models in Port‐Hamiltonian Form for Control Design}},
  volume={25},
  ISSN={1617-7061},
  DOI={10.1002/pamm.202400154},
  number={1},
  journal={PAMM},
  publisher={Wiley},
  author={Junker, Annika and Timmermann, Julia and Trächtler, Ansgar},
  year={2024}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/adaptive-data-driven-models-in-port-hamiltonian-form-for-control-design.bib)
 
## References
- Brunton, S. L. & Kutz, J. N. Data-Driven Science and Engineering. (2019) doi:10.1017/9781108380690 -- [10.1017/9781108380690](https://doi.org/10.1017/9781108380690)
- [Maschke, B. M. & van der Schaft, A. J. Port-Controlled Hamiltonian Systems: Modelling Origins and Systemtheoretic Properties. IFAC Proceedings Volumes 25, 359–365 (1992)](port-controlled-hamiltonian-systems-modelling-origins-and-systemtheoretic-properties) -- [10.1016/s1474-6670(17)52308-3](https://doi.org/10.1016/s1474-6670(17)52308-3)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Energy-shaping of port-controlled Hamiltonian systems by interconnection. Proceedings of the 38th IEEE Conference on Decision and Control (Cat. No.99CH36304) vol. 2 1646–1651](energy-shaping-of-port-controlled-hamiltonian-systems-by-interconnection) -- [10.1109/cdc.1999.830260](https://doi.org/10.1109/cdc.1999.830260)
- Khalil H. K., Nonlinear Control (2015)
- Junker, A., Timmermann, J. & Trachtler, A. Data-Driven Models for Control Engineering Applications Using the Koopman Operator. 2022 3rd International Conference on Artificial Intelligence, Robotics and Control (AIRC) 1–9 (2022) doi:10.1109/airc56195.2022.9836980 -- [10.1109/airc56195.2022.9836980](https://doi.org/10.1109/airc56195.2022.9836980)
- SCHMID, P. J. Dynamic mode decomposition of numerical and experimental data. J. Fluid Mech. 656, 5–28 (2010) -- [10.1017/s0022112010001217](https://doi.org/10.1017/s0022112010001217)
- Brunton, S. L., Brunton, B. W., Proctor, J. L. & Kutz, J. N. Koopman Invariant Subspaces and Finite Linear Representations of Nonlinear Dynamical Systems for Control. PLoS ONE 11, e0150171 (2016) -- [10.1371/journal.pone.0150171](https://doi.org/10.1371/journal.pone.0150171)
- Proctor, J. L., Brunton, S. L. & Kutz, J. N. Dynamic Mode Decomposition with Control. SIAM J. Appl. Dyn. Syst. 15, 142–161 (2016) -- [10.1137/15m1013857](https://doi.org/10.1137/15m1013857)
- Korda, M. & Mezić, I. Linear predictors for nonlinear dynamical systems: Koopman operator meets model predictive control. Automatica 93, 149–160 (2018) -- [10.1016/j.automatica.2018.03.046](https://doi.org/10.1016/j.automatica.2018.03.046)
- Williams, M. O., Kevrekidis, I. G. & Rowley, C. W. A Data–Driven Approximation of the Koopman Operator: Extending Dynamic Mode Decomposition. J Nonlinear Sci 25, 1307–1346 (2015) -- [10.1007/s00332-015-9258-5](https://doi.org/10.1007/s00332-015-9258-5)
- Mamakoukas, G., Castano, M., Tan, X. & Murphey, T. Local Koopman Operators for Data-Driven Control of Robotic Systems. Robotics: Science and Systems XV (2019) doi:10.15607/rss.2019.xv.054 -- [10.15607/rss.2019.xv.054](https://doi.org/10.15607/rss.2019.xv.054)
- [Junker, A., Timmermann, J. & Trächtler, A. Learning Data-Driven PCHD Models for Control Engineering Applications*. IFAC-PapersOnLine 55, 389–394 (2022)](learning-data-driven-pchd-models-for-control-engineering-applications) -- [10.1016/j.ifacol.2022.07.343](https://doi.org/10.1016/j.ifacol.2022.07.343)
- Landau, I. D., Lozano, R., M’Saad, M. & Karimi, A. Adaptive Control. Communications and Control Engineering (Springer London, 2011). doi:10.1007/978-0-85729-664-1 -- [10.1007/978-0-85729-664-1](https://doi.org/10.1007/978-0-85729-664-1)
- Åström K. J., Adaptive Control (2008)
- Maschke, B., Ortega, R. & Van Der Schaft, A. J. Energy-based Lyapunov functions for forced Hamiltonian systems with dissipation. IEEE Trans. Automat. Contr. 45, 1498–1502 (2000) -- [10.1109/9.871758](https://doi.org/10.1109/9.871758)
- Brunton, S. L., Proctor, J. L. & Kutz, J. N. Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proc. Natl. Acad. Sci. U.S.A. 113, 3932–3937 (2016) -- [10.1073/pnas.1517384113](https://doi.org/10.1073/pnas.1517384113)
- Junker, A., Fittkau, N., Timmermann, J. & Trachtler, A. Autonomous Golf Putting with Data-Driven and Physics-Based Methods. 2022 Sixth IEEE International Conference on Robotic Computing (IRC) 134–141 (2022) doi:10.1109/irc55401.2022.00031 -- [10.1109/irc55401.2022.00031](https://doi.org/10.1109/irc55401.2022.00031)
- Ortega, R. & Spong, M. W. Adaptive motion control of rigid robots: A tutorial. Automatica 25, 877–888 (1989) -- [10.1016/0005-1098(89)90054-x](https://doi.org/10.1016/0005-1098(89)90054-x)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Isermann, R. & Münchhof, M. Identification of Dynamic Systems. (Springer Berlin Heidelberg, 2011). doi:10.1007/978-3-540-78879-9 -- [10.1007/978-3-540-78879-9](https://doi.org/10.1007/978-3-540-78879-9)
- Junker, A., Pape, K., Timmermann, J. & Trächtler, A. Adaptive Koopman-Based Models for Holistic Controller and Observer Design. IFAC-PapersOnLine 56, 625–630 (2023) -- [10.1016/j.ifacol.2023.12.094](https://doi.org/10.1016/j.ifacol.2023.12.094)
- Cisneros, Pablo. S. G., Datar, A., Göttsch, P. & Werner, H. Data-Driven quasi-LPV Model Predictive Control Using Koopman Operator Techniques. IFAC-PapersOnLine 53, 6062–6068 (2020) -- [10.1016/j.ifacol.2020.12.1676](https://doi.org/10.1016/j.ifacol.2020.12.1676)
- Fortescue, T. R., Kershenbaum, L. S. & Ydstie, B. E. Implementation of self-tuning regulators with variable forgetting factors. Automatica 17, 831–835 (1981) -- [10.1016/0005-1098(81)90070-4](https://doi.org/10.1016/0005-1098(81)90070-4)
- Lozano-Leal, R. & Goodwin, G. A globally convergent adaptive pole placement algorithm without a persistency of excitation requirement. IEEE Trans. Automat. Contr. 30, 795–798 (1985) -- [10.1109/tac.1985.1104036](https://doi.org/10.1109/tac.1985.1104036)

