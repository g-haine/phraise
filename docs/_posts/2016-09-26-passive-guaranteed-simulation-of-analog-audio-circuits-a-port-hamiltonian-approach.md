---
layout: post
title: "Passive Guaranteed Simulation of Analog Audio Circuits: A Port-Hamiltonian Approach"
date: 2016-09-26 00:00:00 +0100
permalink: passive-guaranteed-simulation-of-analog-audio-circuits-a-port-hamiltonian-approach
year: 2016
authors: Antoine Falaize, Thomas Hélie
category: articles
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
 
[Download the bib file]({{ site.baseurl }}/assets/bib/passive-guaranteed-simulation-of-analog-audio-circuits-a-port-hamiltonian-approach.bib)
 
## References
- Bilbao, S. Numerical Sound Synthesis. (2009) doi:10.1002/9780470749012 -- [10.1002/9780470749012](https://doi.org/10.1002/9780470749012)
- Bilbao, S. Conservative numerical methods for nonlinear strings. The Journal of the Acoustical Society of America vol. 118 3316–3327 (2005) -- [10.1121/1.2046787](https://doi.org/10.1121/1.2046787)
- Chabassier, J. & Joly, P. Energy preserving schemes for nonlinear Hamiltonian systems of wave equations: Application to the vibrating piano string. Computer Methods in Applied Mechanics and Engineering vol. 199 2779–2795 (2010) -- [10.1016/j.cma.2010.04.013](https://doi.org/10.1016/j.cma.2010.04.013)
- Välimäki, V., Pakarinen, J., Erkut, C. & Karjalainen, M. Discrete-time modelling of musical instruments. Reports on Progress in Physics vol. 69 1–78 (2005) -- [10.1088/0034-4885/69/1/r01](https://doi.org/10.1088/0034-4885/69/1/r01)
- Petrausch, S. & Rabenstein, R. Interconnection of state space structures and wave digital filters. IEEE Transactions on Circuits and Systems II: Express Briefs vol. 52 90–93 (2005) -- [10.1109/tcsii.2004.840286](https://doi.org/10.1109/tcsii.2004.840286)
- Fettweis, A. Wave digital filters: Theory and practice. Proceedings of the IEEE vol. 74 270–327 (1986) -- [10.1109/proc.1986.13458](https://doi.org/10.1109/proc.1986.13458)
- Sarti, A. & De Poli, G. Toward nonlinear wave digital filters. IEEE Transactions on Signal Processing vol. 47 1654–1668 (1999) -- [10.1109/78.765137](https://doi.org/10.1109/78.765137)
- Pedersini, F., Sarti, A. & Tubaro, S. Block-wise physical model synthesis for musicalacoustics. Electronics Letters vol. 35 1418–1419 (1999) -- [10.1049/el:19990933](https://doi.org/10.1049/el:19990933)
- Pakarinen, Real-time audio transformer emulation for virtual tube amplifiers. EURASIP J. Adv. Signal Process. (2011)
- Fettweis, A. Pseudo-passivity, sensitivity, and stability of wave digital filters. IEEE Transactions on Circuit Theory vol. 19 668–673 (1972) -- [10.1109/tct.1972.1083555](https://doi.org/10.1109/tct.1972.1083555)
- Yeh, D. T., Abel, J. S. & Smith, J. O. Automated Physical Modeling of Nonlinear Audio Circuits For Real-Time Audio Effects—Part I: Theoretical Development. IEEE Transactions on Audio, Speech, and Language Processing vol. 18 728–737 (2010) -- [10.1109/tasl.2009.2033978](https://doi.org/10.1109/tasl.2009.2033978)
- Borin, G., De Poli, G. & Rocchesso, D. Elimination of delay-free loops in discrete-time models of nonlinear acoustic systems. IEEE Transactions on Speech and Audio Processing vol. 8 597–605 (2000) -- [10.1109/89.861380](https://doi.org/10.1109/89.861380)
- Maschke, B. M., Van Der Schaft, A. J. & Breedveld, P. C. An intrinsic hamiltonian formulation of network dynamics: non-standard poisson structures and gyrators. Journal of the Franklin Institute vol. 329 923–966 (1992) -- [10.1016/s0016-0032(92)90049-m](https://doi.org/10.1016/s0016-0032(92)90049-m)
- Marsden, J. E. & Ratiu, T. S. Introduction to Mechanics and Symmetry. Texts in Applied Mathematics (Springer New York, 1999). doi:10.1007/978-0-387-21792-5 -- [10.1007/978-0-387-21792-5](https://doi.org/10.1007/978-0-387-21792-5)
- Itoh, T. & Abe, K. Hamiltonian-conserving discrete canonical equations based on variational difference quotients. Journal of Computational Physics vol. 76 85–102 (1988) -- [10.1016/0021-9991(88)90132-5](https://doi.org/10.1016/0021-9991(88)90132-5)
- Tellegen, A general network theorem, with applications. Philips Res. Rep. (1952)
- Karnopp, D. Power-conserving transformations: physical interpretations and applications using bond graphs. Journal of the Franklin Institute vol. 288 175–201 (1969) -- [10.1016/0016-0032(69)00246-8](https://doi.org/10.1016/0016-0032(69)00246-8)
- Breedveld, P. C. Multibond graph elements in physical systems theory. Journal of the Franklin Institute vol. 319 1–36 (1985) -- [10.1016/0016-0032(85)90062-6](https://doi.org/10.1016/0016-0032(85)90062-6)
- Diestel, R. Graph Theory. Graduate Texts in Mathematics (Springer Berlin Heidelberg, 2010). doi:10.1007/978-3-642-14279-6 -- [10.1007/978-3-642-14279-6](https://doi.org/10.1007/978-3-642-14279-6)
- Yeh, D. T. Automated Physical Modeling of Nonlinear Audio Circuits for Real-Time Audio Effects—Part II: BJT and Vacuum Tube Examples. IEEE Transactions on Audio, Speech, and Language Processing vol. 20 1207–1216 (2012) -- [10.1109/tasl.2011.2173677](https://doi.org/10.1109/tasl.2011.2173677)
- Butcher, J. C. Numerical Methods for Ordinary Differential Equations. (2008) doi:10.1002/9780470753767 -- [10.1002/9780470753767](https://doi.org/10.1002/9780470753767)

