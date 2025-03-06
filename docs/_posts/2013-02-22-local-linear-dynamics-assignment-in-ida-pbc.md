---
layout: post
title: "Local linear dynamics assignment in IDA-PBC"
date: 2013-02-22 00:00:00 +0100
permalink: local-linear-dynamics-assignment-in-ida-pbc
year: 2013
authors: Paul Kotyczka
category:
  - articles
tags:
  - port-hamiltonian systems
  - passivity
  - nonlinear control
  - controller parameterization
  - dynamics assignment
---
 
## Authors
[Paul Kotyczka](authors/paul_kotyczka)
 
## Abstract
In this paper, the technique of local linear dynamics assignment is presented, which complements the powerful Interconnection and Damping Assignment Passivity Based Control (IDA-PBC) methodology. In IDA-PBC, nonlinear state feedback controllers are designed by matching the system’s dynamics with a desired Port-Hamiltonian (PH) state representation. The latter consists of an energy function, which serves as the closed-loop Lyapunov function, as well as matrices, describing the virtual internal exchange and dissipation of the energy. A major difficulty in IDA-PBC is how to determine reasonable values for the large number of free design parameters. Local linear dynamics assignment offers a solution to this problem with a number of advantages. (i) Invoking the closed-loop Jacobian linearization to fix the parameter values provides transparency with respect to the resulting local dynamic behavior. (ii) An appropriate state transformation isolates the coordinates available for energy shaping. (iii) A related local linear state transformation makes the resulting system of design equations linear. (iv) Assigning a Hurwitz closed-loop Jacobian and ensuring positive semi-definiteness of the closed-loop dissipation matrix, the tedious definiteness check of the energy is omitted. The design steps are illustrated with the Ball on Wheel example.
 
## Keywords
Port-Hamiltonian systems; Passivity; Nonlinear control; Controller parameterization; Dynamics assignment
 
## Citation
- **Journal:** Automatica
- **Year:** 2013
- **Volume:** 49
- **Issue:** 4
- **Pages:** 1037--1044
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2013.01.028](https://doi.org/10.1016/j.automatica.2013.01.028)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Kotyczka_2013,
  title={{Local linear dynamics assignment in IDA-PBC}},
  volume={49},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2013.01.028},
  number={4},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Kotyczka, Paul},
  year={2013},
  pages={1037--1044}
}
{% endraw %}
{% endhighlight %}
 
## References
- Acosta, J.A., & Astolfi, A. (2009). On the PDEs arising in IDA-PBC. In Proceedings of the conference on decision and control/Chinese control conference (pp. 2132–2137). Shanghai. -- [10.1109/CDC.2009.5400580](https://doi.org/10.1109/CDC.2009.5400580)
- Acosta, J. A., Ortega, R., Astolfi, A. & Mahindrakar, A. D. Interconnection and damping assignment passivity-based control of mechanical systems with underactuation degree one. IEEE Transactions on Automatic Control vol. 50 1936–1955 (2005) -- [10.1109/TAC.2005.860292](https://doi.org/10.1109/TAC.2005.860292)
- BACCIOTTI, A. The Local Stabilizability Problem for Nonlinear Systems. IMA Journal of Mathematical Control and Information vol. 5 27–39 (1988) -- [10.1093/imamci/5.1.27](https://doi.org/10.1093/imamci/5.1.27)
- Boyd, S. (2005). Linear dynamical systems. In Lecture notes, Stanford University. www.stanford.edu/class/ee363/notes/lq-lyap-notes.pdf.
- Cheng, D., Astolfi, A. & Ortega, R. On feedback equivalence to port controlled Hamiltonian systems. Systems &amp; Control Letters vol. 54 911–917 (2005) -- [10.1016/j.sysconle.2005.02.005](https://doi.org/10.1016/j.sysconle.2005.02.005)
- [Gómez-Estern, F. & Van der Schaft, A. J. Physical Damping in IDA-PBC Controlled Underactuated Mechanical Systems. European Journal of Control vol. 10 451–468 (2004)](physical-damping-in-ida-pbc-controlled-underactuated-mechanical-systems) -- [10.3166/ejc.10.451-468](https://doi.org/10.3166/ejc.10.451-468)
- Höffner, K. (2011). Geometric aspects of interconnection and damping assignment — passivity-based control. Ph.D. Thesis, Queen’s University, Kingston.
- Kloiber, T., & Kotyczka, P. (2012). Estimating and enlarging the domain of attraction in IDA-PBC. In Proceedings of the IEEE conference on decision and control (pp. 1852–1858). Maui. -- [10.1109/CDC.2012.6426473](https://doi.org/10.1109/CDC.2012.6426473)
- Kotyczka, P. (2011). Local linear dynamics assignment in IDA-PBC for underactuated mechanical systems. In Proceedings of the IEEE conference on decision and control/European control conference (pp. 6534–6539). Orlando. -- [10.1109/CDC.2011.6160656](https://doi.org/10.1109/CDC.2011.6160656)
- Kotyczka, P., Koch, G., Pellegrini, E., & Lohmann, B. (2010). Transparent parametrization of nonlinear IDA-PBC for a hydraulic actuator. In Proceedings of the IFAC symposium on nonlinear control systems (pp. 1122–1127). Bologna. -- [10.3182/20100901-3-IT-2016.00175](https://doi.org/10.3182/20100901-3-IT-2016.00175)
- Kotyczka, P., & Lohmann, B. (2009). Parametrization of IDA-PBC by assignment of local linear dynamics. In Proceedings of the European control conference (pp. 4721–4726). Budapest. -- [10.23919/ECC.2009.7075146](https://doi.org/10.23919/ECC.2009.7075146)
- Kotyczka, P., Volf, A., & Lohmann, B. (2010). Passivity based trajectory tracking control with predefined local linear error dynamics. In Proceedings of the American control conference (pp. 3429–3434). Baltimore. -- [10.1109/ACC.2010.5531100](https://doi.org/10.1109/ACC.2010.5531100)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/S0005-1098(01)00278-3](https://doi.org/10.1016/S0005-1098(01)00278-3)
- Prajna, S., van der Schaft, A. & Meinsma, G. An LMI approach to stabilization of linear port-controlled Hamiltonian systems. Systems &amp; Control Letters vol. 45 371–385 (2002) -- [10.1016/S0167-6911(01)00195-5](https://doi.org/10.1016/S0167-6911(01)00195-5)
- Tiefensee, F., Monaco, S., & Normand-Cyrot, D. (2010). IDA-PBC under sampling for port-controlled Hamiltonian systems. In Proceedings of the American control conference (pp. 1811–1816). Baltimore. -- [10.1109/ACC.2010.5531444](https://doi.org/10.1109/ACC.2010.5531444)
- Viola, G., Ortega, R., Banavar, R., Acosta, J. A. & Astolfi, A. Total Energy Shaping Control of Mechanical Systems: Simplifying the Matching Equations Via Coordinate Changes. IEEE Transactions on Automatic Control vol. 52 1093–1099 (2007) -- [10.1109/TAC.2007.899064](https://doi.org/10.1109/TAC.2007.899064)

