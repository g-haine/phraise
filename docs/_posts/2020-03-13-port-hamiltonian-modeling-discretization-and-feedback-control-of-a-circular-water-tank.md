---
layout: post
title: "Port-Hamiltonian modeling, discretization and feedback control of a circular water tank"
date: 2020-03-13 00:00:00 +0100
permalink: port-hamiltonian-modeling-discretization-and-feedback-control-of-a-circular-water-tank
year: 2019
authors: Flavio Luiz Cardoso-Ribeiro, Andrea Brugnoli, Denis Matignon, Laurent Lefevre
category: proceedings
---
 
## Authors
[Flavio Luiz Cardoso-Ribeiro](authors/flavio-luiz-cardoso-ribeiro), [Andrea Brugnoli](authors/andrea-brugnoli), [Denis Matignon](authors/denis-matignon), [Laurent Lefevre](authors/laurent-lefevre)
 
## Abstract
This work presents the development of the nonlinear 2D Shallow Water Equations (SWE) in polar coordinates as a boundary port controlled Hamiltonian system. A geometric reduction by symmetry is obtained, simplifying the system to one-dimension. The recently developed Partitioned Finite Element Method is applied to semi-discretize the equations, preserving the boundary power-product of both the original 2D and the reduced 1D system. The main advantage of this power-preserving semi-discretization method is that it can be applied using well-established finite element software. In this work, we use FEniCS to solve the variational formulation, including the nonlinearity provided by the non-quadratic Hamiltonian of the SWE. A passive output-feedback controller using damping injection is used to dissipate the water waves.
 
## Citation
- **Journal:** 2019 IEEE 58th Conference on Decision and Control (CDC)
- **Year:** 2019
- **Volume:** 
- **Issue:** 
- **Pages:** 6881--6886
- **Publisher:** IEEE
- **DOI:** [10.1109/cdc40024.2019.9030007](https://doi.org/10.1109/cdc40024.2019.9030007)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Cardoso_Ribeiro_2019,
  title={{Port-Hamiltonian modeling, discretization and feedback control of a circular water tank}},
  DOI={10.1109/cdc40024.2019.9030007},
  booktitle={{2019 IEEE 58th Conference on Decision and Control (CDC)}},
  publisher={IEEE},
  author={Cardoso-Ribeiro, Flavio Luiz and Brugnoli, Andrea and Matignon, Denis and Lefevre, Laurent},
  year={2019},
  pages={6881--6886}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-modeling-discretization-and-feedback-control-of-a-circular-water-tank.bib)
 
## References
- Maeda, K., Hosotani, N., Tamura, K. & Ando, H. Wave making properties of circular basin. Proceedings of the 2004 International Symposium on Underwater Technology (IEEE Cat. No.04EX869) 349–354 doi:10.1109/ut.2004.1405603 -- [10.1109/ut.2004.1405603](https://doi.org/10.1109/ut.2004.1405603)
- Ingram, D., Wallace, R., Robinson, A. & Bryden, I. The design and commissioning of the first, circular, combined current and wave test basin. OCEANS 2014 - TAIPEI 1–7 (2014) doi:10.1109/oceans-taipei.2014.6964577 -- [10.1109/oceans-taipei.2014.6964577](https://doi.org/10.1109/oceans-taipei.2014.6964577)
- noble, Spatial variation in currents generated in the FloWave Ocean Energy Research Facility. Proc of the European Wave and Tidal Energy Conference (2015)
- salter, Absorbing wave-makers and wide tanks. Proc Directional Wave Spectra Appl Conf (1981)
- Spinneken, J., Christou, M. & Swan, C. Force-controlled absorption in a fully-nonlinear numerical wave tank. Journal of Computational Physics vol. 272 127–148 (2014) -- [10.1016/j.jcp.2014.04.018](https://doi.org/10.1016/j.jcp.2014.04.018)
- Gyongy, I., Bruce, T. & Bryden, I. Numerical analysis of force-feedback control in a circular tank. Applied Ocean Research vol. 47 329–343 (2014) -- [10.1016/j.apor.2014.07.002](https://doi.org/10.1016/j.apor.2014.07.002)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Courant, T. J. Dirac manifolds. Transactions of the American Mathematical Society vol. 319 631–661 (1990) -- [10.1090/s0002-9947-1990-0998124-1](https://doi.org/10.1090/s0002-9947-1990-0998124-1)
- Schaft, A. J. Port-Hamiltonian Systems: Network Modeling and Control of Nonlinear Physical Systems. Advanced Dynamics and Control of Structures and Machines 127–167 (2004) doi:10.1007/978-3-7091-2774-2_9 -- [10.1007/978-3-7091-2774-2_9](https://doi.org/10.1007/978-3-7091-2774-2_9)
- Scruggs, J. & Jacob, P. Harvesting Ocean Wave Energy. Science vol. 323 1176–1178 (2009) -- [10.1126/science.1168245](https://doi.org/10.1126/science.1168245)
- Cho, Y.-S., Sohn, D.-H. & Lee, S. O. Practical modified scheme of linear shallow-water equations for distant propagation of tsunamis. Ocean Engineering vol. 34 1769–1777 (2007) -- [10.1016/j.oceaneng.2006.08.014](https://doi.org/10.1016/j.oceaneng.2006.08.014)
- Schäffer, H. A. Second-order wavemaker theory for irregular waves. Ocean Engineering vol. 23 47–88 (1996) -- [10.1016/0029-8018(95)00013-b](https://doi.org/10.1016/0029-8018(95)00013-b)
- Warnitchai, P. & Pinkaew, T. Modelling of liquid sloshing in rectangular tanks with flow-dampening devices. Engineering Structures vol. 20 593–600 (1998) -- [10.1016/s0141-0296(97)00068-0](https://doi.org/10.1016/s0141-0296(97)00068-0)
- Spinneken, J. & Swan, C. Second-order wave maker theory using force-feedback control. Part I: A new theory for regular wave generation. Ocean Engineering vol. 36 539–548 (2009) -- [10.1016/j.oceaneng.2009.01.019](https://doi.org/10.1016/j.oceaneng.2009.01.019)
- Spinneken, J. & Swan, C. Second-order wave maker theory using force-feedback control. Part I: A new theory for regular wave generation. Ocean Engineering vol. 36 539–548 (2009) -- [10.1016/j.oceaneng.2009.01.019](https://doi.org/10.1016/j.oceaneng.2009.01.019)
- Clifford, M., Horton, C. & Schmitz, J. SWAFS: shallow water analysis and forecast system. Proceedings of OCEANS’94 vol. 3 III/82-III/87 -- [10.1109/oceans.1994.364176](https://doi.org/10.1109/oceans.1994.364176)
- naito, Evaluation of performance of new wave-making basin. Proc of the Ninth Inter Offshore and Polar Engineering Conf (1999)
- robles, Sloshing mechanical model for stability and handling qualities evaluation of the C295 aircraft with the OSD system. Proceedings of 29th Congress of the International Council of the Aeronautical Sciences (2014)
- Hamroun, B., Lefevre, L. & Mendes, E. Port-based modelling and geometric reduction for open channel irrigation systems. 2007 46th IEEE Conference on Decision and Control 1578–1583 (2007) doi:10.1109/cdc.2007.4434237 -- [10.1109/cdc.2007.4434237](https://doi.org/10.1109/cdc.2007.4434237)
- [Pasumarthy, R., Ambati, V. R. & van der Schaft, A. J. Port-Hamiltonian discretization for open channel flows. Systems &amp; Control Letters vol. 61 950–958 (2012)](port-hamiltonian-discretization-for-open-channel-flows) -- [10.1016/j.sysconle.2012.05.003](https://doi.org/10.1016/j.sysconle.2012.05.003)
- [Hamroun, B., Dimofte, A., Lefèvre, L. & Mendes, E. Control by Interconnection and Energy-Shaping Methods of Port Hamiltonian Models. Application to the Shallow Water Equations. European Journal of Control vol. 16 545–563 (2010)](control-by-interconnection-and-energy-shaping-methods-of-port-hamiltonian-models-application-to-the-shallow-water-equations) -- [10.3166/ejc.16.545-563](https://doi.org/10.3166/ejc.16.545-563)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Lefèvre, L. A structure-preserving Partitioned Finite Element Method for the 2D wave equation. IFAC-PapersOnLine vol. 51 119–124 (2018)](a-structure-preserving-partitioned-finite-element-method-for-the-2d-wave-equation) -- [10.1016/j.ifacol.2018.06.033](https://doi.org/10.1016/j.ifacol.2018.06.033)
- [Cardoso-Ribeiro, F. L., Matignon, D. & Pommier-Budinger, V. A port-Hamiltonian model of liquid sloshing in moving containers and application to a fluid-structure system. Journal of Fluids and Structures vol. 69 402–427 (2017)](a-port-hamiltonian-model-of-liquid-sloshing-in-moving-containers-and-application-to-a-fluid-structure-system) -- [10.1016/j.jfluidstructs.2016.12.007](https://doi.org/10.1016/j.jfluidstructs.2016.12.007)
- alnæs, The FEniCS Project Version 1.5. Archive of Numerical Software (2015)
- cardoso-ribeiro, A Partitioned Finite-Element Method (PFEM) for power-preserving discretization of open systems of conservation laws. (2019)

