---
title: "Circuit extraction via time-domain vector fitting"
date: 2004-11-12 00:00:00 +0100
permalink: circuit-extraction-via-time-domain-vector-fitting
year: 2004
authors: S. Grivet-Talocia, F.G. Canavero, I.S. Stievano, I.A. Maio
category: proceedings
---
 
## Authors
[S. Grivet-Talocia](authors/stefano-grivet-talocia), [F.G. Canavero](authors/f-g-canavero), [I.S. Stievano](authors/i-s-stievano), [I.A. Maio](authors/i-a-maio)
 
## Abstract
This paper introduces a new algorithm for the automatic synthesis of SPICE-ready equivalent circuits of complex multiport lumped interconnect structures. The method is named time-domain vector fitting (TD-VF) due to its analogy to the well-known vector fitting algorithm, which operates in the frequency domain. The TD-VF computes a rational approximation of the transfer matrix for the structure under modeling using as raw data its transient port responses to suitable excitations. These include, e.g., the case of transient port scattering responses as typically obtained by full-wave electromagnetic solvers based on the finite-differences time-domain (FDTD) or finite integration (FIT) methods. The TD-VF algorithm works entirely in the time domain, without requiring any knowledge of the frequency-domain responses. This allows direct processing of possibly truncated transient responses, therefore allowing for short full-wave simulations. This paper shows that the accuracy level achievable by TD-VF is excellent. Hence, passivity can be enforced a posteriori using the spectral properties of associated Hamiltonian matrices. Several examples of package, connectors, and discontinuities are provided as illustration.
 
## Citation
- **Journal:** 2004 International Symposium on Electromagnetic Compatibility (IEEE Cat. No.04CH37559)
- **Year:** 2004
- **Volume:** 
- **Issue:** 
- **Pages:** 1005--1010
- **Publisher:** IEEE
- **DOI:** [10.1109/isemc.2004.1349964](https://doi.org/10.1109/isemc.2004.1349964)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Grivet_Talocia,
  series={ISEMC-04},
  title={{Circuit extraction via time-domain vector fitting}},
  DOI={10.1109/isemc.2004.1349964},
  booktitle={{2004 International Symposium on Electromagnetic Compatibility (IEEE Cat. No.04CH37559)}},
  publisher={IEEE},
  author={Grivet-Talocia, S. and Canavero, F.G. and Stievano, I.S. and Maio, I.A.},
  pages={1005--1010},
  collection={ISEMC-04}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/circuit-extraction-via-time-domain-vector-fitting.bib)
 
## References
- Grivet-Talocia, S. Package macromodeling via time-domain vector fitting. IEEE Microw. Wireless Compon. Lett. 13, 472–474 (2003) -- [10.1109/lmwc.2003.819378](https://doi.org/10.1109/lmwc.2003.819378)
- Grivet-Talocia, S. The Time-Domain Vector Fitting Algorithm for Linear Macromodeling. AEU - International Journal of Electronics and Communications 58, 293–295 (2004) -- [10.1078/1434-8411-54100245](https://doi.org/10.1078/1434-8411-54100245)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Trans. Circuits Syst. I 51, 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- grivet-talocia, Enforcing Passivity of Macromodels via Spectral Perturbation of Hamiltonian Matrices. 8th IEEE Workshop on Signal Propagation on Interconnects (SPI) (2003)
- Gustavsen, B. & Semlyen, A. Rational approximation of frequency domain responses by vector fitting. IEEE Trans. Power Delivery 14, 1052–1061 (1999) -- [10.1109/61.772353](https://doi.org/10.1109/61.772353)
- Achar, R. & Nakhla, M. S. Simulation of high-speed interconnects. Proc. IEEE 89, 693–728 (2001) -- [10.1109/5.929650](https://doi.org/10.1109/5.929650)
- [Grivet-Talocia, S., Stievano, I. S., Maio, I. A. & Canavero, F. Time-domain and frequency-domain macromodeling: application to package structures. 2003 IEEE Symposium on Electromagnetic Compatibility. Symposium Record (Cat. No.03CH37446) vol. 2 570–574](time-domain-and-frequency-domain-macromodeling-application-to-package-structures) -- [10.1109/isemc.2003.1236665](https://doi.org/10.1109/isemc.2003.1236665)
- CST Microwave Studio Manual. (2003)
- celik, IC Interconnect Analysis. (2002)

