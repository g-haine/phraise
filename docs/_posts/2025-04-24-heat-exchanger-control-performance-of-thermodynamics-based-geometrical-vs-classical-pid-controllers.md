---
title: "Heat exchanger control: Performance of thermodynamics-based geometrical vs classical PID controllers"
date: 2025-04-24 00:00:00 +0100
permalink: heat-exchanger-control-performance-of-thermodynamics-based-geometrical-vs-classical-pid-controllers
year: 2025
authors: Omar R. Gómez-Gómez, Marco A. Zárate-Navarro, J. Paulo García-Sandoval
category: articles
tags:
  - Heat exchanger
  - LabVIEW
  - Non-equilibrium thermodynamics
  - PID
---
 
## Authors
[Omar R. Gómez-Gómez](authors/omar-r-gomez-gomez), [Marco A. Zárate-Navarro](authors/marco-a-zarate-navarro), [J. Paulo García-Sandoval](authors/j-paulo-garcia-sandoval)
 
## Abstract
In this communication, a control problem based on thermodynamic principles is developed to control the output temperature of a heat exchanger in an experimental setup. The system is controlled through a nonlinear output error, which is proportional to the total entropy production within the heat exchanger. A lumped-parameter model of the heat exchanger allows to define the thermodynamic control scheme, with geometric control principles, a high-gain observer and an anti-windup scheme, which provides robustness against parametric uncertainties and disturbances. To make a comparison with classical control schemes, a Ziegler–Nichols PID controller was tuned for a First Order Plus Dead Time plant approximation. The experimental setup used a National Instruments Compact FieldPoint controller, and the control scheme was programmed in a LabVIEW interface. The performance of the proposed controller was tested under two criteria: energetic performance and total tracking control error. The results show that the classical controller has a better energy-saving performance, while the thermodynamic controller has a better tracking performance, making it more suitable for applications where temperature control needs to be more precise.
 
## Keywords
Heat exchanger; LabVIEW; Non-equilibrium thermodynamics; PID
 
## Citation
- **Journal:** Case Studies in Thermal Engineering
- **Year:** 2025
- **Volume:** 71
- **Issue:** 
- **Pages:** 106130
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.csite.2025.106130](https://doi.org/10.1016/j.csite.2025.106130)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{G_mez_G_mez_2025,
  title={{Heat exchanger control: Performance of thermodynamics-based geometrical vs classical PID controllers}},
  volume={71},
  ISSN={2214-157X},
  DOI={10.1016/j.csite.2025.106130},
  journal={Case Studies in Thermal Engineering},
  publisher={Elsevier BV},
  author={Gómez-Gómez, Omar R. and Zárate-Navarro, Marco A. and García-Sandoval, J. Paulo},
  year={2025},
  pages={106130}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/heat-exchanger-control-performance-of-thermodynamics-based-geometrical-vs-classical-pid-controllers.bib)
 
## References
- Putting energy back in control. IEEE Control Systems vol. 21 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica vol. 38 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- García-Sandoval, J. P., Hudon, N., Dochain, D. & González-Álvarez, V. Stability analysis and passivity properties of a class of thermodynamic processes: An internal entropy production approach. Chemical Engineering Science vol. 139 261–272 (2016) -- [10.1016/j.ces.2015.07.039](https://doi.org/10.1016/j.ces.2015.07.039)
- García-Sandoval, J. P., Hudon, N. & Dochain, D. Generalized Hamiltonian representation of thermo-mechanical systems based on an entropic formulation. Journal of Process Control vol. 51 18–26 (2017) -- [10.1016/j.jprocont.2016.09.011](https://doi.org/10.1016/j.jprocont.2016.09.011)
- Romo-Hernández, A., Hudon, N., Ydstie, B. E. & Dochain, D. Thermodynamic Analysis and Feedback Stabilization for Irreversible Liquid–Vapor Systems. Industrial &amp; Engineering Chemistry Research vol. 59 2252–2260 (2020) -- [10.1021/acs.iecr.9b04869](https://doi.org/10.1021/acs.iecr.9b04869)
- Alonso, A. A. & Erik Ydstie, B. Process systems, passivity and the second law of thermodynamics. Computers &amp; Chemical Engineering vol. 20 S1119–S1124 (1996) -- [10.1016/0098-1354(96)00194-9](https://doi.org/10.1016/0098-1354(96)00194-9)
- Alonso, A. A. & Ydstie, B. E. Stabilization of distributed systems using irreversible thermodynamics. Automatica vol. 37 1739–1755 (2001) -- [10.1016/s0005-1098(01)00140-6](https://doi.org/10.1016/s0005-1098(01)00140-6)
- Bao, (2007)
- Sangi, R. & Müller, D. Application of the second law of thermodynamics to control: A review. Energy vol. 174 938–953 (2019) -- [10.1016/j.energy.2019.03.024](https://doi.org/10.1016/j.energy.2019.03.024)
- Favache, A., Dochain, D. & Winkin, J. J. Power-shaping control: Writing the system dynamics into the Brayton–Moser form. Systems &amp; Control Letters vol. 60 618–624 (2011) -- [10.1016/j.sysconle.2011.04.021](https://doi.org/10.1016/j.sysconle.2011.04.021)
- Hoang, H., Couenne, F., Jallut, C. & Le Gorrec, Y. Lyapunov-based control of non isothermal continuous stirred tank reactors using irreversible thermodynamics. Journal of Process Control vol. 22 412–422 (2012) -- [10.1016/j.jprocont.2011.12.007](https://doi.org/10.1016/j.jprocont.2011.12.007)
- Zárate-Navarro, M. A., García-Sandoval, J. P. & Hudon, N. A saturated feedforward/cascade controller for passive continuous reacting systems using entropy production shaping. European Journal of Control vol. 49 53–61 (2019) -- [10.1016/j.ejcon.2019.01.006](https://doi.org/10.1016/j.ejcon.2019.01.006)
- Zarate-Navarro, M. A., Dubljevic, S., Campos-Rodriguez, A., Aguilar-Garnica, E. & Garcia-Sandoval, J. P. Dissipative Boundary Control for an Adiabatic Plug Flow Reactor With Mass Recycle. IEEE Access vol. 10 30939–30948 (2022) -- [10.1109/access.2022.3157335](https://doi.org/10.1109/access.2022.3157335)
- [Ramirez, H. & Le Gorrec, Y. An Overview on Irreversible Port-Hamiltonian Systems. Entropy vol. 24 1478 (2022)](an-overview-on-irreversible-port-hamiltonian-systems) -- [10.3390/e24101478](https://doi.org/10.3390/e24101478)
- [Ramirez, H., Gorrec, Y. L. & Maschke, B. Boundary controlled irreversible port-Hamiltonian systems. Chemical Engineering Science vol. 248 117107 (2022)](boundary-controlled-irreversible-port-hamiltonian-systems) -- [10.1016/j.ces.2021.117107](https://doi.org/10.1016/j.ces.2021.117107)
- [Mora, L. A., Le Gorrec, Y. & Ramirez, H. Energy-shaping and entropy-assignment boundary control of the heat equation. Systems &amp; Control Letters vol. 189 105821 (2024)](energy-shaping-and-entropy-assignment-boundary-control-of-the-heat-equation) -- [10.1016/j.sysconle.2024.105821](https://doi.org/10.1016/j.sysconle.2024.105821)
- [Philipp, F. M., Schaller, M., Worthmann, K., Faulwasser, T. & Maschke, B. Optimal control of port-Hamiltonian systems: Energy, entropy, and exergy. Systems &amp; Control Letters vol. 194 105942 (2024)](optimal-control-of-port-hamiltonian-systems-energy-entropy-and-exergy) -- [10.1016/j.sysconle.2024.105942](https://doi.org/10.1016/j.sysconle.2024.105942)
- García-Morales, J. et al. Inverse artificial neural network control design for a double tube heat exchanger. Case Studies in Thermal Engineering vol. 34 102075 (2022) -- [10.1016/j.csite.2022.102075](https://doi.org/10.1016/j.csite.2022.102075)
- Kanoh, H., Itoh, T. & Abe, N. Nonlinear H∞ control for heat exchangers controlled by the manipulation of flow rate. Nonlinear Analysis: Theory, Methods &amp; Applications vol. 30 2237–2248 (1997) -- [10.1016/s0362-546x(97)00135-1](https://doi.org/10.1016/s0362-546x(97)00135-1)
- Oravec, J., Bakošová, M., Mészáros, A. & Míková, N. Experimental investigation of alternative robust model predictive control of a heat exchanger. Applied Thermal Engineering vol. 105 774–782 (2016) -- [10.1016/j.applthermaleng.2016.05.046](https://doi.org/10.1016/j.applthermaleng.2016.05.046)
- Dong, H., Li, X., He, X., Zeng, Z. & Wen, G. A two-degree-of-freedom controller for a high-precision air temperature control system with multiple disturbances. Case Studies in Thermal Engineering vol. 50 103442 (2023) -- [10.1016/j.csite.2023.103442](https://doi.org/10.1016/j.csite.2023.103442)
- Rsetam, K., Al-Rawi, M. & Cao, Z. Robust composite temperature control of electrical tube furnaces by using disturbance observer. Case Studies in Thermal Engineering vol. 30 101781 (2022) -- [10.1016/j.csite.2022.101781](https://doi.org/10.1016/j.csite.2022.101781)
- Cao, S., Zhao, W. & Zhu, A. Research on intervention PID control of VAV terminal based on LabVIEW. Case Studies in Thermal Engineering vol. 45 103002 (2023) -- [10.1016/j.csite.2023.103002](https://doi.org/10.1016/j.csite.2023.103002)
- Bhaskarwar, Automation of shell and tube type heat exchanger with PLC and LabVIEW. (2015)
- Sánchez, A. et al. A temperature control system for batch pretreatments of lignocellulosic biomass: proposal, implementation and evaluation. Cellulose vol. 30 2085–2095 (2023) -- [10.1007/s10570-022-05039-x](https://doi.org/10.1007/s10570-022-05039-x)
- Pérez-Pirela, Development of a simplified model for a distributed-parameter heat exchange system for thermodynamic principles-based control purposes. IFAC-Pap. (2018)
- Saleem, O., Ahmad, K. R. & Iqbal, J. Fuzzy-Augmented Model Reference Adaptive PID Control Law Design for Robust Voltage Regulation in DC–DC Buck Converters. Mathematics vol. 12 1893 (2024) -- [10.3390/math12121893](https://doi.org/10.3390/math12121893)
- Smith, (2005)

