---
title: "A Risk-Aligned Hybrid Time-Domain Model for Multi-Body Gap Resonance"
date: 2026-09-28 00:00:00 +0100
permalink: a-risk-aligned-hybrid-time-domain-model-for-multi-body-gap-resonance
year: 2026
authors: Yang Chen, Bo Peng, Guangmo Yi, Zhen-Zhong Hu, Zhengru Ren
category: proceedings
---
 
## Authors
[Yang Chen](authors/yang-chen), [Bo Peng](authors/bo-peng), [Guangmo Yi](authors/guangmo-yi), [Zhen-Zhong Hu](authors/zhen-zhong-hu), [Zhengru Ren](authors/zhengru-ren)
 
## Abstract
While potential flow theory and Computational Fluid Dynamics (CFD) are standard approaches for marine hydrodynamics, they face significant limitations in multi-body gap resonance scenarios. Potential flow exhibits singular behavior at resonance, CFD entails prohibitive computational costs for real-time applications, and simplified linearized damping models fail to generalize across varying sea states. A novel risk-aligned hybrid time-domain framework is proposed to address these challenges and bridge the gap between physical fidelity and computational stability. The framework decouples the system into a linear hydrodynamic baseline, which captures the broadband background wave-body interactions, and an embedded nonlinear subsystem that explicitly reconstructs the resonant gap fluid oscillation. Crucially, the baseline is identified via a Virtual Work algorithm specifically weighted for the collision-prone “squeeze mode,” prioritizing squeeze-mode energy alignment, while the linear manifold is constrained by the Kalman-Yakubovich-Popov lemma to enforce passivity. By integrating these components within a Port-Hamiltonian architecture, the system provides an energy-consistent modeling structure. Numerical experiments on a twin-barge system demonstrate the efficacy of the framework: it successfully isolates about 90% of nonlinear resonance energy, maintains prediction errors below 0.5% across varying wave heights without parameter re-calibration, and exhibits stable energy behavior with relative energy error below 0.22% in long-duration simulations (3 hours). The proposed model is a numerically promising candidate framework for real-time-oriented marine simulation under the tested benchmark conditions.
 
## Citation
- **Journal:** Volume 5A: Ocean Engineering
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** V05AT06A060
- **Publisher:** American Society of Mechanical Engineers
- **DOI:** [10.1115/omae2026-180315](https://doi.org/10.1115/omae2026-180315)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Chen_2026,
  series={OMAE2026},
  title={{A Risk-Aligned Hybrid Time-Domain Model for Multi-Body Gap Resonance}},
  DOI={10.1115/omae2026-180315},
  booktitle={{Volume 5A: Ocean Engineering}},
  publisher={American Society of Mechanical Engineers},
  author={Chen, Yang and Peng, Bo and Yi, Guangmo and Hu, Zhen-Zhong and Ren, Zhengru},
  year={2026}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-risk-aligned-hybrid-time-domain-model-for-multi-body-gap-resonance.bib)
 
