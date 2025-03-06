---
layout: post
title: "Mastering the complexity of an Ultrasonic Sealing System: The port-Hamiltonian approach"
date: 2011-04-12 00:00:00 +0100
permalink: mastering-the-complexity-of-an-ultrasonic-sealing-system-the-port-hamiltonian-approach
year: 2011
authors: Luca Gentili, Alessandro Macchelli, Claudio Melchiorri, Alberto Mameli
category:
  - articles
tags:
  - model reduction
  - port-hamiltonian systems
  - piezo-electric devices
  - modeling
  - simulation
---
 
## Authors
[Luca Gentili](authors/luca_gentili), [Alessandro Macchelli](authors/alessandro_macchelli), [Claudio Melchiorri](authors/claudio_melchiorri), [Alberto Mameli](authors/alberto_mameli)
 
## Abstract
This paper deals with the problem of simulating an Ultrasonic Sealing System (USS). The USS is a complex electromechanical system used to seal aseptic packages for liquid foods that is the core of the most advanced filling machines. Since the overall device is the result of the interconnection of several sub-systems that belong to different physical domains, the problem is tackled within the port-Hamiltonian framework, which is naturally multi-domain and multi-scale. On the other hand, the simulation of the whole sealing process is not a trivial task due to the presence of a Compact Transducer (CT) that can be modeled only by means of commercial finite-element software. Then, only extremely high-order models are available, which makes the simulation of the complete system impractical. Consequently, a novel model reduction procedure for port-Hamiltonian systems has been developed. The method is able to preserve the frequency behavior of the original system in a neighborhood of a predefined set of frequencies of interest. In this way, simulation times have been drastically shortened without loosing the essential dynamical information. The reduced order model can be adopted to test the validity of the controller, and to simulate and perform the diagnosis of the entire sealing process. The results of the model reduction algorithm have been experimentally validated. Moreover, also the complete USS model has been derived.
 
## Keywords
Model reduction; Port-Hamiltonian systems; Piezo-electric devices; Modeling; Simulation
 
## Citation
- **Journal:** Mechatronics
- **Year:** 2011
- **Volume:** 21
- **Issue:** 3
- **Pages:** 594--603
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.mechatronics.2011.02.009](https://doi.org/10.1016/j.mechatronics.2011.02.009)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gentili_2011,
  title={{Mastering the complexity of an Ultrasonic Sealing System: The port-Hamiltonian approach}},
  volume={21},
  ISSN={0957-4158},
  DOI={10.1016/j.mechatronics.2011.02.009},
  number={3},
  journal={Mechatronics},
  publisher={Elsevier BV},
  author={Gentili, Luca and Macchelli, Alessandro and Melchiorri, Claudio and Mameli, Alberto},
  year={2011},
  pages={594--603}
}
{% endraw %}
{% endhighlight %}
 
## References
- [Maschke BM, van der Schaft AJ. Port controlled Hamiltonian systems: modeling origins and system theoretic properties. In: Proceedings of the 3rd IFAC symposium on nonlinear control systems (NOLCOS 1992), Bordeaux, France; 1992. p. 282–8.](port-controlled-hamiltonian-systems-modelling-origins-and-systemtheoretic-properties-93) -- [10.1016/B978-0-08-041901-5.50064-6](https://doi.org/10.1016/B978-0-08-041901-5.50064-6)
- Dynasim AB. Dymola; 2008. <http://www.dynasim.se/>.
- Control Lab Products, 20-Sim; 2006. <http://www.20sim.com/>.
- SIMULIA, Abaqus Unified FEA; 2008. <http://www.simulia.com/>.
- [Gentili L, Bassi L, Macchelli A, Melchiorri C, Borsari R. Model reduction for high-order port-Hamiltonian systems. Application to piezo-electric systems. In: Proceedings of the 48th IEEE conference on decision and control, 2009 held jointly with the 2009 28th Chinese control conference (CDC/CCC 2009), Shanghai, PR China; 2009. p. 7285–90.](model-reduction-for-high-order-port-hamiltonian-systems-application-to-piezo-electric-systems) -- [10.1109/CDC.2009.5400573](https://doi.org/10.1109/CDC.2009.5400573)
- Gentili L, Bassi L, Macchelli A, Melchiorri C, Borsari R. Design and experimental validation of a model reduction algorithm for high-order port-Hamiltonian systems. In: Proceedings of the 8th IFAC symposium on nonlinear control systems (NOLCOS 2010), Bologna, Italy; 2010. -- [10.3182/20100901-3-IT-2016.00207](https://doi.org/10.3182/20100901-3-IT-2016.00207)
- Moore, B. Principal component analysis in linear systems: Controllability, observability, and model reduction. IEEE Transactions on Automatic Control vol. 26 17–32 (1981) -- [10.1109/TAC.1981.1102568](https://doi.org/10.1109/TAC.1981.1102568)
- Scherpen JMA. Balancing for nonlinear systems. Ph.D. thesis, University of Twente; 1994.
- van der Schaft, A. Balancing of Lossless and Passive Systems. IEEE Transactions on Automatic Control vol. 53 2153–2157 (2008) -- [10.1109/TAC.2008.930192](https://doi.org/10.1109/TAC.2008.930192)
- Van Der Schaft, A. J. & Maschke, B. M. On the Hamiltonian formulation of nonholonomic mechanical systems. Reports on Mathematical Physics vol. 34 225–233 (1994) -- [10.1016/0034-4877(94)90038-8](https://doi.org/10.1016/0034-4877(94)90038-8)
- Krysl, P., Lall, S. & Marsden, J. E. Dimensional model reduction in non‐linear finite element dynamics of solids and structures. International Journal for Numerical Methods in Engineering vol. 51 479–504 (2001) -- [10.1002/nme.167](https://doi.org/10.1002/nme.167)
- Lall, S., Marsden, J. E. & Glavaški, S. A subspace approach to balanced truncation for model reduction of nonlinear control systems. International Journal of Robust and Nonlinear Control vol. 12 519–535 (2002) -- [10.1002/rnc.657](https://doi.org/10.1002/rnc.657)
- Lall, S., Krysl, P. & Marsden, J. E. Structure-preserving model reduction for mechanical systems. Physica D: Nonlinear Phenomena vol. 184 304–318 (2003) -- [10.1016/S0167-2789(03)00227-6](https://doi.org/10.1016/S0167-2789(03)00227-6)
- Polyuga RV, van der Schaft AJ. Structure preserving model reduction for port-Hamiltonian systems. In: Proceedings of the 18th international symposium on mathematical theory of networks and systems (MTNS 2008), Blacksburg, VA, USA; 2008.
- Polyuga RV. Model reduction of port-Hamiltonian systems. Ph.D. thesis, University of Twente; April 2010.
- [van der Schaft, A. J. & Maschke, B. M. Hamiltonian formulation of distributed-parameter systems with boundary energy flow. Journal of Geometry and Physics vol. 42 166–194 (2002)](hamiltonian-formulation-of-distributed-parameter-systems-with-boundary-energy-flow) -- [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3)
- [Golo, G., Talasila, V., van der Schaft, A. & Maschke, B. Hamiltonian discretization of boundary control systems. Automatica vol. 40 757–771 (2004)](hamiltonian-discretization-of-boundary-control-systems) -- [10.1016/j.automatica.2003.12.017](https://doi.org/10.1016/j.automatica.2003.12.017)
- Piefort V. Finite element modelling of piezoelectric active structures. Ph.D. thesis, Université Libre De Bruxelles; 2001.
- Nemkov V, Madjarov N, Melandri A. Development of inductive power transfer for ultrasonic sealing (UIPT). Tech. Rep. DR0020251, Tetra Pak Packaging Solutions; January 2008.
- Amini J, Akerblom C, Wallentinsson AK, Strnad I, Tryding J. Energy dissipation in multi-layered board under ultrasonic sealing, Joint-competence study between Stora Enso and Tetra Pak; April 2010.

