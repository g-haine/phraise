---
layout: post
title: "On the Equivalence Between PI-PBC and IOC Designs: An Application Involving Three-Phase Front-End Converters"
date: 2023-07-26 00:00:00 +0100
permalink: on-the-equivalence-between-pi-pbc-and-ioc-designs-an-application-involving-three-phase-front-end-converters
year: 2024
authors: Oscar Danilo Montoya, Federico M. Serra, Gerardo Espinosa-Pérez
category: articles
---
 
## Authors
[Oscar Danilo Montoya](authors/oscar-danilo-montoya), [Federico M. Serra](authors/federico-m-serra), [Gerardo Espinosa-Pérez](authors/gerardo-espinosa-perez)
 
## Abstract
This brief addressed the control design problem for a bilinear dynamical system with two approaches. The first approach is proportional-integral passivity-based control theory (PI-PBC), and the second control approach is based on inverse optimal control theory plus integral gain (IOC+I). PI-PBC theory is a well-known control design methodology for dealing with state variable regulation in dynamical systems that exhibit a port-Hamiltonian structure, with the main characteristic that a PI controller is designed by preserving the Hamiltonian properties in a closed loop while ensuring asymptotic stability. IOC+I allows for the design of feedback nonlinear controllers for dynamical systems, which in turn allows selecting the candidate Lyapunov function and the control matrix to obtain multiple nonlinear feedback controllers, with the main advantage that all of them ensure asymptotic stability, as the resulting control laws are optimal. This brief demonstrates that a PI-PBC design and IOC+I generate the same feedback control law if and only the candidate Lyapunov function of the IOC+I design is selected as the Hamiltonian function used in the PI-PBC design. The well-known three-phase front-end converter was selected as the test control system to demonstrate the equivalence between the control laws obtained with the PI-PBC and the IOC+I approaches.
 
## Citation
- **Journal:** IEEE Transactions on Circuits and Systems II: Express Briefs
- **Year:** 2024
- **Volume:** 71
- **Issue:** 1
- **Pages:** 241--245
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tcsii.2023.3299203](https://doi.org/10.1109/tcsii.2023.3299203)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Montoya_2024,
  title={{On the Equivalence Between PI-PBC and IOC Designs: An Application Involving Three-Phase Front-End Converters}},
  volume={71},
  ISSN={1558-3791},
  DOI={10.1109/tcsii.2023.3299203},
  number={1},
  journal={IEEE Transactions on Circuits and Systems II: Express Briefs},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Montoya, Oscar Danilo and Serra, Federico M. and Espinosa-Pérez, Gerardo},
  year={2024},
  pages={241--245}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-the-equivalence-between-pi-pbc-and-ioc-designs-an-application-involving-three-phase-front-end-converters.bib)
 
## References
- Gil-González, W., Montoya, O. D. & Garces, A. Bilinear Control for Three-Phase Microgrids: A Proportional-Integral Passivity-Based Design. Electric Power Components and Systems vol. 48 447–458 (2020) -- [10.1080/15325008.2020.1793831](https://doi.org/10.1080/15325008.2020.1793831)
- Cisneros, R. et al. Global tracking passivity-based PI control of bilinear systems: Application to the interleaved boost and modular multilevel converters. Control Engineering Practice vol. 43 109–119 (2015) -- [10.1016/j.conengprac.2015.07.002](https://doi.org/10.1016/j.conengprac.2015.07.002)
- Xu, W., Qu, S. & Zhang, C. Fast Terminal Sliding Mode Current Control With Adaptive Extended State Disturbance Observer for PMSM System. IEEE Journal of Emerging and Selected Topics in Power Electronics vol. 11 418–431 (2023) -- [10.1109/jestpe.2022.3185777](https://doi.org/10.1109/jestpe.2022.3185777)
- Xu, S. et al. A Simultaneous Diagnosis Method for Power Switch and Current Sensor Faults in Grid-Connected Three-Level NPC Inverters. IEEE Transactions on Power Electronics vol. 38 1104–1118 (2023) -- [10.1109/tpel.2022.3200721](https://doi.org/10.1109/tpel.2022.3200721)
- Vazquez, S., Rodriguez, J., Rivera, M., Franquelo, L. G. & Norambuena, M. Model Predictive Control for Power Converters and Drives: Advances and Trends. IEEE Transactions on Industrial Electronics vol. 64 935–947 (2017) -- [10.1109/tie.2016.2625238](https://doi.org/10.1109/tie.2016.2625238)
- Bhattacharyya, D., Padhee, S. & Pati, K. C. Modeling of DC–DC Converter Using Exact Feedback Linearization Method: A Discussion. IETE Journal of Research vol. 65 843–854 (2018) -- [10.1080/03772063.2018.1454345](https://doi.org/10.1080/03772063.2018.1454345)
- Wang, X., Blaabjerg, F. & Loh, P. C. Passivity-Based Stability Analysis and Damping Injection for Multiparalleled VSCs with LCL Filters. IEEE Transactions on Power Electronics vol. 32 8922–8935 (2017) -- [10.1109/tpel.2017.2651948](https://doi.org/10.1109/tpel.2017.2651948)
- Vega, C. & Alzate, R. Inverse optimal control on electric power conversion. 2014 IEEE International Autumn Meeting on Power, Electronics and Computing (ROPEC) 1–5 (2014) doi:10.1109/ropec.2014.7036320 -- [10.1109/ropec.2014.7036320](https://doi.org/10.1109/ropec.2014.7036320)
- Johnson, M., Aghasadeghi, N. & Bretl, T. Inverse optimal control for deterministic continuous-time nonlinear systems. 52nd IEEE Conference on Decision and Control 2906–2913 (2013) doi:10.1109/cdc.2013.6760325 -- [10.1109/cdc.2013.6760325](https://doi.org/10.1109/cdc.2013.6760325)
- A novel droop control method to achieve maximum power output of photovoltaic for parallel inverter system. CSEE Journal of Power and Energy Systems (2021) doi:10.17775/cseejpes.2020.05070 -- [10.17775/cseejpes.2020.05070](https://doi.org/10.17775/cseejpes.2020.05070)
- Zhong, C., Zhou, Y., Chen, J. & Liu, Z. DC-side synchronous active power control of two-stage photovoltaic generation for frequency support in Islanded microgrids. Energy Reports vol. 8 8361–8371 (2022) -- [10.1016/j.egyr.2022.06.030](https://doi.org/10.1016/j.egyr.2022.06.030)
- Avila-Becerril, S. & Espinosa-Pérez, G. Control of islanded microgrids considering power converter dynamics. International Journal of Control vol. 94 2520–2530 (2020) -- [10.1080/00207179.2020.1713402](https://doi.org/10.1080/00207179.2020.1713402)
- Haddad, W. M., Nersesov, S. G. & Chellaboina, V. Energy-based control for hybrid port-controlled Hamiltonian systems. Automatica vol. 39 1425–1435 (2003) -- [10.1016/s0005-1098(03)00113-4](https://doi.org/10.1016/s0005-1098(03)00113-4)
- Serra, F. M. & De Angelo, C. H. IDA-PBC controller design for grid connected Front End Converters under non-ideal grid conditions. Electric Power Systems Research vol. 142 12–19 (2017) -- [10.1016/j.epsr.2016.08.041](https://doi.org/10.1016/j.epsr.2016.08.041)
- Serra, F. M., De Angelo, C. H. & Forchetti, D. G. Interconnection and damping assignment control of a three-phase front end converter. International Journal of Electrical Power &amp; Energy Systems vol. 60 317–324 (2014) -- [10.1016/j.ijepes.2014.03.033](https://doi.org/10.1016/j.ijepes.2014.03.033)
- Spinu, V., Dam, M. & Lazar, M. Observer design for DC/DC power converters with bilinear averaged model. IFAC Proceedings Volumes vol. 45 204–209 (2012) -- [10.3182/20120606-3-nl-3011.00091](https://doi.org/10.3182/20120606-3-nl-3011.00091)
- Avila-Becerril, S., Espinosa-Pérez, G. & Machado, J. E. A Hamiltonian control approach for electric microgrids with dynamic power flow solution. Automatica vol. 139 110192 (2022) -- [10.1016/j.automatica.2022.110192](https://doi.org/10.1016/j.automatica.2022.110192)
- Jouini, T., Rantzer, A. & Tegling, E. Inverse optimal control for angle stabilization in converter-based generation. 2022 American Control Conference (ACC) 4945–4950 (2022) doi:10.23919/acc53348.2022.9867726 -- [10.23919/acc53348.2022.9867726](https://doi.org/10.23919/acc53348.2022.9867726)
- Villegas-Ruvalcaba, M., Gurubel-Tun, K. & Coronado-Mendoza, A. Robust Inverse Optimal Control for a Boost Converter. Energies vol. 14 2507 (2021) -- [10.3390/en14092507](https://doi.org/10.3390/en14092507)
- Iwanski, G., Maciejewski, P. & Luszczyk, T. New Stationary Frame Transformation for Control of a Three-Phase Power Converter Under Unbalanced Grid Voltage Sags. IEEE Journal of Emerging and Selected Topics in Power Electronics vol. 9 4432–4446 (2021) -- [10.1109/jestpe.2020.3012971](https://doi.org/10.1109/jestpe.2020.3012971)

