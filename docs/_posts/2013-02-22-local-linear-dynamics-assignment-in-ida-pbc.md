---
layout: post
title: "Local linear dynamics assignment in IDA-PBC"
date: 2013-02-22 00:00:00 +0100
permalink: local-linear-dynamics-assignment-in-ida-pbc
year: 2013
authors: Paul Kotyczka
category: articles
tags:
  - Port-Hamiltonian systems
  - Passivity
  - Nonlinear control
  - Controller parameterization
  - Dynamics assignment
---
 
## Authors
[Paul Kotyczka](authors/paul-kotyczka)
 
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
 
[Download the bib file]({{ site.baseurl }}/assets/bib/local-linear-dynamics-assignment-in-ida-pbc.bib)
 
## References
- Acosta, J. A. & Astolfi, A. On the PDEs arising in IDA-PBC. Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference 2132–2137 (2009) doi:10.1109/cdc.2009.5400580 -- [10.1109/cdc.2009.5400580](https://doi.org/10.1109/cdc.2009.5400580)
- Acosta, J. A., Ortega, R., Astolfi, A. & Mahindrakar, A. D. Interconnection and damping assignment passivity-based control of mechanical systems with underactuation degree one. IEEE Transactions on Automatic Control vol. 50 1936–1955 (2005) -- [10.1109/tac.2005.860292](https://doi.org/10.1109/tac.2005.860292)
- BACCIOTTI, A. The Local Stabilizability Problem for Nonlinear Systems. IMA Journal of Mathematical Control and Information vol. 5 27–39 (1988) -- [10.1093/imamci/5.1.27](https://doi.org/10.1093/imamci/5.1.27)
- Cheng, D., Astolfi, A. & Ortega, R. On feedback equivalence to port controlled Hamiltonian systems. Systems &amp; Control Letters vol. 54 911–917 (2005) -- [10.1016/j.sysconle.2005.02.005](https://doi.org/10.1016/j.sysconle.2005.02.005)
- [Gómez-Estern, F. & Van der Schaft, A. J. Physical Damping in IDA-PBC Controlled Underactuated Mechanical Systems. European Journal of Control vol. 10 451–468 (2004)](physical-damping-in-ida-pbc-controlled-underactuated-mechanical-systems) -- [10.3166/ejc.10.451-468](https://doi.org/10.3166/ejc.10.451-468)
- Ho, Controlling a ball and wheel system using full-state-feedback linearization. IEEE Control Systems Magazine (2009)
- Isidori, (1995)
- Khalil, (1996)
- Kloiber, T. & Kotyczka, P. Estimating and enlarging the domain of attraction in IDA-PBC. 2012 IEEE 51st IEEE Conference on Decision and Control (CDC) 1852–1858 (2012) doi:10.1109/cdc.2012.6426473 -- [10.1109/cdc.2012.6426473](https://doi.org/10.1109/cdc.2012.6426473)
- Kotyczka, P. Local linear dynamics assignment in IDA-PBC for underactuated mechanical systems. IEEE Conference on Decision and Control and European Control Conference 6534–6539 (2011) doi:10.1109/cdc.2011.6160656 -- [10.1109/cdc.2011.6160656](https://doi.org/10.1109/cdc.2011.6160656)
- Kotyczka, P., Koch, G., Pellegrini, E. & Lohmann, B. Transparent Parametrization of Nonlinear IDA-PBC for a Hydraulic Actuator. IFAC Proceedings Volumes vol. 43 1122–1127 (2010) -- [10.3182/20100901-3-it-2016.00175](https://doi.org/10.3182/20100901-3-it-2016.00175)
- Kotyczka, P. & Lohmann, B. Parametrization of IDA-PBC by assignment of local linear dynamics. 2009 European Control Conference (ECC) 4721–4726 (2009) doi:10.23919/ecc.2009.7075146 -- [10.23919/ecc.2009.7075146](https://doi.org/10.23919/ecc.2009.7075146)
- Kotyczka, P., Volf, A. & Lohmann, B. Passivity based trajectory tracking control with predefined local linear error dynamics. Proceedings of the 2010 American Control Conference 3429–3434 (2010) doi:10.1109/acc.2010.5531100 -- [10.1109/acc.2010.5531100](https://doi.org/10.1109/acc.2010.5531100)
- Krstić, (1995)
- Kugi, (2001)
- Lévine, (2009)
- Nijmeijer, (1990)
- Ortega, (1998)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Prajna, S., van der Schaft, A. & Meinsma, G. An LMI approach to stabilization of linear port-controlled Hamiltonian systems. Systems &amp; Control Letters vol. 45 371–385 (2002) -- [10.1016/s0167-6911(01)00195-5](https://doi.org/10.1016/s0167-6911(01)00195-5)
- Sepulchre, (1997)
- Tiefensee, F., Monaco, S. & Normand-Cyrot, D. IDA-PBC under sampling for port-controlled hamiltonian systems. Proceedings of the 2010 American Control Conference 1811–1816 (2010) doi:10.1109/acc.2010.5531444 -- [10.1109/acc.2010.5531444](https://doi.org/10.1109/acc.2010.5531444)
- van der Schaft, (2000)
- Viola, G., Ortega, R., Banavar, R., Acosta, J. A. & Astolfi, A. Total Energy Shaping Control of Mechanical Systems: Simplifying the Matching Equations Via Coordinate Changes. IEEE Transactions on Automatic Control vol. 52 1093–1099 (2007) -- [10.1109/tac.2007.899064](https://doi.org/10.1109/tac.2007.899064)

