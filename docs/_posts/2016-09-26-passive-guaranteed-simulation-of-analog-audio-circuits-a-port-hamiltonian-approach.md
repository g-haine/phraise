---
layout: post
title: "Passive Guaranteed Simulation of Analog Audio Circuits: A Port-Hamiltonian Approach"
date: 2016-09-26 00:00:00 +0100
permalink: passive-guaranteed-simulation-of-analog-audio-circuits-a-port-hamiltonian-approach
year: 2016
authors: Antoine Falaize, Thomas Hélie
category: journal-article
---
 
## Authors
[Antoine Falaize](authors/antoine-falaize), [Thomas Hélie](authors/thomas-helie)
 
## Abstract
We present a method that generates passive-guaranteed stable simulations of analog audio circuits from electronic schematics for real-time issues. On one hand, this method is based on a continuous-time power-balanced state-space representation structured into its energy-storing parts, dissipative parts, and external sources. On the other hand, a numerical scheme is especially designed to preserve this structure and the power balance. These state-space structures define the class of port-Hamiltonian systems. The derivation of this structured system associated with the electronic circuit is achieved by an automated analysis of the interconnection network combined with a dictionary of models for each elementary component. The numerical scheme is based on the combination of finite differences applied on the state (with respect to the time variable) and on the total energy (with respect to the state). This combination provides a discrete-time version of the power balance. This set of algorithms is valid for both the linear and nonlinear case. Finally, three applications of increasing complexities are given: a diode clipper, a common-emitter bipolar-junction transistor amplifier, and a wah pedal. The results are compared to offline simulations obtained from a popular circuit simulator.
 
## Citation
- **Journal:** Applied Sciences
- **Year:** 2016
- **Volume:** 6
- **Issue:** 10
- **Pages:** 273
- **Publisher:** MDPI AG
- **DOI:** [10.3390/app6100273](https://doi.org/10.3390/app6100273)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Falaize_2016,
  title={{Passive Guaranteed Simulation of Analog Audio Circuits: A Port-Hamiltonian Approach}},
  volume={6},
  ISSN={2076-3417},
  DOI={10.3390/app6100273},
  number={10},
  journal={Applied Sciences},
  publisher={MDPI AG},
  author={Falaize, Antoine and Hélie, Thomas},
  year={2016},
  pages={273}
}
{% endraw %}
{% endhighlight %}
 
## References
- Bilbao, S. (2009). Numerical Sound Synthesis: Finite Difference Schemes and Simulation in Musical Acoustics, John Wiley & Sons Ltd. -- [10.1002/9780470749012](https://doi.org/10.1002/9780470749012)
- Bilbao, S. Conservative numerical methods for nonlinear strings. The Journal of the Acoustical Society of America vol. 118 3316–3327 (2005) -- [10.1121/1.2046787](https://doi.org/10.1121/1.2046787)
- Chabassier, J. & Joly, P. Energy preserving schemes for nonlinear Hamiltonian systems of wave equations: Application to the vibrating piano string. Computer Methods in Applied Mechanics and Engineering vol. 199 2779–2795 (2010) -- [10.1016/j.cma.2010.04.013](https://doi.org/10.1016/j.cma.2010.04.013)
- Välimäki, V., Pakarinen, J., Erkut, C. & Karjalainen, M. Discrete-time modelling of musical instruments. Reports on Progress in Physics vol. 69 1–78 (2005) -- [10.1088/0034-4885/69/1/R01](https://doi.org/10.1088/0034-4885/69/1/R01)
- Petrausch, S. & Rabenstein, R. Interconnection of state space structures and wave digital filters. IEEE Transactions on Circuits and Systems II: Express Briefs vol. 52 90–93 (2005) -- [10.1109/TCSII.2004.840286](https://doi.org/10.1109/TCSII.2004.840286)
- Yeh, D.T., and Smith, J.O. (2008, January 1–4). Simulating guitar distortion circuits using wave digital and nonlinear state-space formulations. Proceedings of the 1st International Conference on Digital Audio Effects (DAFx’08), Espoo, Finland.
- Fettweis, A. Wave digital filters: Theory and practice. Proceedings of the IEEE vol. 74 270–327 (1986) -- [10.1109/PROC.1986.13458](https://doi.org/10.1109/PROC.1986.13458)
- Sarti, A. & De Poli, G. Toward nonlinear wave digital filters. IEEE Transactions on Signal Processing vol. 47 1654–1668 (1999) -- [10.1109/78.765137](https://doi.org/10.1109/78.765137)
- Pedersini, F., Sarti, A. & Tubaro, S. Block-wise physical model synthesis for musicalacoustics. Electronics Letters vol. 35 1418–1419 (1999) -- [10.1049/el:19990933](https://doi.org/10.1049/el:19990933)
- Pakarinen, J., Tikander, M., and Karjalainen, M. (2009, January 1–4). Wave digital modeling of the output chain of a vacuum-tube amplifier. Proceedings of the 12th International Conference on Digital Audio Effects (DAFx’09), Como, Italy.
- Fettweis, A. Pseudo-passivity, sensitivity, and stability of wave digital filters. IEEE Transactions on Circuit Theory vol. 19 668–673 (1972) -- [10.1109/TCT.1972.1083555](https://doi.org/10.1109/TCT.1972.1083555)
- Bilbao, S., Bensa, J., and Kronland-Martinet, R. (2003, January 8–11). The wave digital reed: A passive formulation. Proceedings of the 6th International Conference on Digital Audio Effects (DAFx-03), London, UK.
- Schwerdtfeger, T., and Kummert, A. (2014, January 1–5). A multidimensional approach to wave digital filters with multiple nonlinearities. Proceedings of the 22nd European Signal Processing Conference (EUSIPCO), Lisbon, Portugal.
- Werner, K.J., Nangia, V., Bernardini, A., Smith, J.O., and Sarti, A. (November, January 29). An Improved and Generalized Diode Clipper Model for Wave Digital Filters. Proceedings of the 139th Convention of the Audio Engineering Society (AES), New York, NY, USA.
- Khalil, H.K. (2002). Nonlinear Systems, Prentice Hall.
- Cohen, I., and Helie, T. (2010, January 6–10). Real-time simulation of a guitar power amplifier. Proceedings of the 13th International Conference on Digital Audio Effects (DAFx-10), Graz, Austria.
- Yeh, D. T., Abel, J. S. & Smith, J. O. Automated Physical Modeling of Nonlinear Audio Circuits For Real-Time Audio Effects—Part I: Theoretical Development. IEEE Transactions on Audio, Speech, and Language Processing vol. 18 728–737 (2010) -- [10.1109/TASL.2009.2033978](https://doi.org/10.1109/TASL.2009.2033978)
- Borin, G., De Poli, G. & Rocchesso, D. Elimination of delay-free loops in discrete-time models of nonlinear acoustic systems. IEEE Transactions on Speech and Audio Processing vol. 8 597–605 (2000) -- [10.1109/89.861380](https://doi.org/10.1109/89.861380)
- Hélie, T. (2011, January 19–23). Lyapunov stability analysis of the Moog ladder filter and dissipativity aspects in numerical solutions. Proceedings of the 14th International Conference on Digital Audio Effects DAFx-11, Paris, France.
- Maschke, B. M., Van Der Schaft, A. J. & Breedveld, P. C. An intrinsic hamiltonian formulation of network dynamics: non-standard poisson structures and gyrators. Journal of the Franklin Institute vol. 329 923–966 (1992) -- [10.1016/S0016-0032(92)90049-M](https://doi.org/10.1016/S0016-0032(92)90049-M)
- Van der Schaft, A.J. (2006, January 22–30). Port-Hamiltonian systems: An introductory survey. Proceedings of the International Congress of Mathematicians, Madrid, Spain.
- Stramigioli, S., Duindam, V., and Macchelli, A. (2009). Modeling and Control of Complex Physical Systems: The Port-Hamiltonian Approach, Springer.
- Marsden, J.E., and Ratiu, T.S. (1999). Introduction to Mechanics and Symmetry: A Basic Exposition of Classical Mechanical Systems, Springer. -- [10.1007/978-0-387-21792-5](https://doi.org/10.1007/978-0-387-21792-5)
- Itoh, T. & Abe, K. Hamiltonian-conserving discrete canonical equations based on variational difference quotients. Journal of Computational Physics vol. 76 85–102 (1988) -- [10.1016/0021-9991(88)90132-5](https://doi.org/10.1016/0021-9991(88)90132-5)
- Desoer, C.A., and Kuh, E.S. (2009). Basic Circuit Theory, Tata McGraw-Hill Education.
- Karnopp, D. Power-conserving transformations: physical interpretations and applications using bond graphs. Journal of the Franklin Institute vol. 288 175–201 (1969) -- [10.1016/0016-0032(69)00246-8](https://doi.org/10.1016/0016-0032(69)00246-8)
- Breedveld, P. C. Multibond graph elements in physical systems theory. Journal of the Franklin Institute vol. 319 1–36 (1985) -- [10.1016/0016-0032(85)90062-6](https://doi.org/10.1016/0016-0032(85)90062-6)
- Falaize, A., and Hélie, T. (December, January 30). Guaranteed-passive simulation of an electro-mechanical piano: A port-Hamiltonian approach. Proceedings of the 18th International Conference on Digital Audio Effects (DAFx), Trondheim, Norway.
- Falaize, A., Lopes, N., Hélie, T., Matignon, D., and Maschke, B. (2014, January 11–12). Energy-balanced models for acoustic and audio systems: A port-Hamiltonian approach. Proceedings of the Unfold Mechanics for Sounds and Music, Paris, France.
- Vladimirescu, A. (1994). The SPICE Book, John Wiley & Sons, Inc.
- Diestel, R. (2010). Graph Theory, Springer. [4th ed.]. -- [10.1007/978-3-642-14279-6](https://doi.org/10.1007/978-3-642-14279-6)
- Do Carmo, M.P. (1976). Differential Geometry of Curves and Surfaces, Prentice-Hall.
- Hairer, E., Lubich, C., and Wanner, G. (2006). Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations, Springer Science & Business Media.
- Oppenheim, A.V., and Schafer, R.W. (2010). Discrete-Time Signal Processing, Pearson Higher Education. [3rd ed.].
- Jones, E., Oliphant, E., and Peterson, P. SciPy: Open Source Scientific Tools for Python, function scipy.optimize.root. Available online: http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html#scipy.optimize.root.
- Falaize, A. A comparison of numerical methods. Available online: http://recherche.ircam.fr/anasyn/falaize/applis/comparisonnumschemes/.
- Yeh, D. T. Automated Physical Modeling of Nonlinear Audio Circuits for Real-Time Audio Effects—Part II: BJT and Vacuum Tube Examples. IEEE Transactions on Audio, Speech, and Language Processing vol. 20 1207–1216 (2012) -- [10.1109/TASL.2011.2173677](https://doi.org/10.1109/TASL.2011.2173677)
- Butcher, J.C. (2008). Numerical Methods for Ordinary Differential Equations, John Wiley & Sons, Ltd. -- [10.1002/9780470753767](https://doi.org/10.1002/9780470753767)
- Holters, M., and Zölzer, U. (2011, January 19–23). Physical Modelling of a Wah–Wah Effect Pedal as a case study for Application of the nodal DK Method to circuits with variable parts. Proceedings of the 14th International Conference on Digital Audio Effects (DAFx-11), Paris, France.
- Falaize-Skrzek, A., and Hélie, T. (2013, January 17–20). Simulation of an analog circuit of a wah pedal: A port-Hamiltonian approach. Proceedings of the 135th Convention of the Audio Engineering Society, New York, NY, USA.
- Steinberg Media Technologies GmbH Virtual Studio Technology. Available online: http://www.steinberg.net/en/company/technologies/vst3.html.
- ROLI Ltd The JUCE framework. Available online: http://www.juce.com.
- Falaize, A. Companion web-site to the present article entitled "Passive Guaranteed Simulation of Analog Audio Circuits: A port-Hamiltonian Approach". Available online: http://recherche.ircam.fr/anasyn/falaize/applis/analogcircuits/.
- Aoues, S. (2014). Schémas d’intégration dédiés à l’étude, l’analyse et la synthèse dans le formalisme Hamiltonien à ports. [Ph.D. Thesis, INSA].

