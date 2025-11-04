---
title: "Passive simulation of the nonlinear port-Hamiltonian modeling of a Rhodes Piano"
date: 2016-12-08 00:00:00 +0100
permalink: passive-simulation-of-the-nonlinear-port-hamiltonian-modeling-of-a-rhodes-piano
year: 2017
authors: Antoine Falaize, Thomas Hélie
category: articles
tags:
  - Passive modeling
  - Numerical methods
  - Port-Hamiltonian systems
  - Multiphysics system
  - Time domain simulation
---
 
## Authors
[Antoine Falaize](authors/antoine-falaize), [Thomas Hélie](authors/thomas-helie)
 
## Abstract
This paper deals with the time-domain simulation of an electro-mechanical piano: the Fender Rhodes. A simplified description of this multi-physical system is considered. It is composed of a hammer (nonlinear mechanical component), a cantilever beam (linear damped vibrating component) and a pickup (nonlinear magneto-electronic transducer). The approach is to propose a power-balanced formulation of the complete system, from which a guaranteed-passive simulation is derived to generate physically-based realistic sound synthesis. Theses issues are addressed in four steps. First, a class of Port-Hamiltonian Systems is introduced: these input-to-output systems fulfill a power balance that can be decomposed into conservative, dissipative and source parts. Second, physical models are proposed for each component and are recast in the port-Hamiltonian formulation. In particular, a finite-dimensional model of the cantilever beam is derived, based on a standard modal decomposition applied to the Euler-Bernoulli model. Third, these systems are interconnected, providing a nonlinear finite-dimensional Port-Hamiltonian System of the piano. Fourth, a passive-guaranteed numerical method is proposed. This method is built to preserve the power balance in the discrete-time domain, and more precisely, its decomposition structured into conservative, dissipative and source parts. Finally, simulations are performed for a set of physical parameters, based on empirical but realistic values. They provide a variety of audio signals which are perceptively relevant and qualitatively similar to some signals measured on a real instrument.
 
## Keywords
Passive modeling; Numerical methods; Port-Hamiltonian systems; Multiphysics system; Time domain simulation
 
## Citation
- **Journal:** Journal of Sound and Vibration
- **Year:** 2017
- **Volume:** 390
- **Issue:** 
- **Pages:** 289--309
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jsv.2016.11.008](https://doi.org/10.1016/j.jsv.2016.11.008)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Falaize_2017,
  title={{Passive simulation of the nonlinear port-Hamiltonian modeling of a Rhodes Piano}},
  volume={390},
  ISSN={0022-460X},
  DOI={10.1016/j.jsv.2016.11.008},
  journal={Journal of Sound and Vibration},
  publisher={Elsevier BV},
  author={Falaize, Antoine and Hélie, Thomas},
  year={2017},
  pages={289--309}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/passive-simulation-of-the-nonlinear-port-hamiltonian-modeling-of-a-rhodes-piano.bib)
 
## References
- Chabassier, J., Chaigne, A. & Joly, P. Modeling and simulation of a grand piano. The Journal of the Acoustical Society of America vol. 134 648–665 (2013) -- [10.1121/1.4809649](https://doi.org/10.1121/1.4809649)
- Bilbao, S., Torin, A. & Chatziioannou, V. Numerical Modeling of Collisions in Musical Instruments. Acta Acustica united with Acustica vol. 101 155–173 (2015) -- [10.3813/aaa.918813](https://doi.org/10.3813/aaa.918813)
- Välimäki, V., Pakarinen, J., Erkut, C. & Karjalainen, M. Discrete-time modelling of musical instruments. Reports on Progress in Physics vol. 69 1–78 (2005) -- [10.1088/0034-4885/69/1/r01](https://doi.org/10.1088/0034-4885/69/1/r01)
- Fettweis, A. Wave digital filters: Theory and practice. Proceedings of the IEEE vol. 74 270–327 (1986) -- [10.1109/proc.1986.13458](https://doi.org/10.1109/proc.1986.13458)
- Smith, J. O., join(' ’. Physical Modeling Using Digital Waveguides. Computer Music Journal vol. 16 74 (1992) -- [10.2307/3680470](https://doi.org/10.2307/3680470)
- Fettweis, A. Pseudo-passivity, sensitivity, and stability of wave digital filters. IEEE Transactions on Circuit Theory vol. 19 668–673 (1972) -- [10.1109/tct.1972.1083555](https://doi.org/10.1109/tct.1972.1083555)
- [Maschke, B. M., Van Der Schaft, A. J. & Breedveld, P. C. An intrinsic hamiltonian formulation of network dynamics: non-standard poisson structures and gyrators. Journal of the Franklin Institute vol. 329 923–966 (1992)](an-intrinsic-hamiltonian-formulation-of-network-dynamics-non-standard-poisson-structures-and-gyrators) -- [10.1016/s0016-0032(92)90049-m](https://doi.org/10.1016/s0016-0032(92)90049-m)
- [van der Schaft, A. Port-Hamiltonian systems: an introductory survey. Proceedings of the International Congress of Mathematicians Madrid, August 22–30, 2006 1339–1365 (2007) doi:10.4171/022-3/65](port-hamiltonian-systems-an-introductory-survey) -- [10.4171/022-3/65](https://doi.org/10.4171/022-3/65)
- Duindam, (2009)
- Marsden, (2013)
- [Lopes, N., Hélie, T. & Falaize, A. Explicit second-order accurate method for the passive guaranteed simulation of port-Hamiltonian systems. IFAC-PapersOnLine vol. 48 223–228 (2015)](explicit-second-order-accurate-method-for-the-passive-guaranteed-simulation-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2015.10.243](https://doi.org/10.1016/j.ifacol.2015.10.243)
- Hart, H. C., Fuller, M. W. & Lusby, W. S. A Precision Study of Piano Touch and Tone. The Journal of the Acoustical Society of America vol. 6 80–94 (1934) -- [10.1121/1.1915706](https://doi.org/10.1121/1.1915706)
- Muenster, M., Pfeifle, F., Weinrich, T. & Keil, M. Nonlinearities and self-organization in the sound production of the Rhodes piano. The Journal of the Acoustical Society of America vol. 136 2164–2164 (2014) -- [10.1121/1.4899833](https://doi.org/10.1121/1.4899833)
- van der Schaft, (2014)
- Khalil, (1996)
- Graff, (1973)
- Kelly, (2006)
- Fletcher, (1998)
- Giordano, N. & Winans, J. P., II. Piano hammers and their force compression characteristics: Does a power law make sense? The Journal of the Acoustical Society of America vol. 107 2248–2255 (2000) -- [10.1121/1.428505](https://doi.org/10.1121/1.428505)
- Boutillon, X. Model for piano hammers: Experimental determination and digital simulation. The Journal of the Acoustical Society of America vol. 83 746–754 (1988) -- [10.1121/1.396117](https://doi.org/10.1121/1.396117)
- Stulov, A. Hysteretic model of the grand piano hammer felt. The Journal of the Acoustical Society of America vol. 97 2577–2585 (1995) -- [10.1121/1.411912](https://doi.org/10.1121/1.411912)
- [Macchelli, A. & Melchiorri, C. Modeling and Control of the Timoshenko Beam. The Distributed Port Hamiltonian Approach. SIAM Journal on Control and Optimization vol. 43 743–767 (2004)](modeling-and-control-of-the-timoshenko-beam-the-distributed-port-hamiltonian-approach) -- [10.1137/s0363012903429530](https://doi.org/10.1137/s0363012903429530)
- Curtain, (2012)
- [Hélie, T. & Matignon, D. Nonlinear damping models for linear conservative mechanical systems with preserved eigenspaces: a port-Hamiltonian formulation. IFAC-PapersOnLine vol. 48 200–205 (2015)](nonlinear-damping-models-for-linear-conservative-mechanical-systems-with-preserved-eigenspaces-a-port-hamiltonian-formulation) -- [10.1016/j.ifacol.2015.10.239](https://doi.org/10.1016/j.ifacol.2015.10.239)
- Meirovitch, (1997)
- Horton, N. G. & Moore, T. R. Modeling the magnetic pickup of an electric guitar. American Journal of Physics vol. 77 144–150 (2009) -- [10.1119/1.2990663](https://doi.org/10.1119/1.2990663)
- Paiva, Acoustics and modeling of pickups. J. Audio Eng. Soc. (2012)
- Hamill, D. C. Lumped equivalent circuits of magnetic components: the gyrator-capacitor approach. IEEE Transactions on Power Electronics vol. 8 97–103 (1993) -- [10.1109/63.223957](https://doi.org/10.1109/63.223957)
- [Cervera, J., van der Schaft, A. J. & Baños, A. Interconnection of port-Hamiltonian systems and composition of Dirac structures. Automatica vol. 43 212–225 (2007)](interconnection-of-port-hamiltonian-systems-and-composition-of-dirac-structures) -- [10.1016/j.automatica.2006.08.014](https://doi.org/10.1016/j.automatica.2006.08.014)
- Itoh, T. & Abe, K. Hamiltonian-conserving discrete canonical equations based on variational difference quotients. Journal of Computational Physics vol. 76 85–102 (1988) -- [10.1016/0021-9991(88)90132-5](https://doi.org/10.1016/0021-9991(88)90132-5)
- Quispel, G. R. W. & Turner, G. S. Discrete gradient methods for solving ODEs numerically while preserving a first integral. Journal of Physics A: Mathematical and General vol. 29 L341–L349 (1996) -- [10.1088/0305-4470/29/13/006](https://doi.org/10.1088/0305-4470/29/13/006)
- McLachlan, R. I., Quispel, G. R. W. & Robidoux, N. Geometric integration using discrete gradients. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 357 1021–1045 (1999) -- [10.1098/rsta.1999.0363](https://doi.org/10.1098/rsta.1999.0363)
- Budd, Geometric integration and its applications. Handb. Numer. Anal. (2003)
- Lambert, (1973)

