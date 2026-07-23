---
title: "Physics-informed neural learning for IDA-PBC control of underactuated USVs under parameter uncertainty"
date: 2026-07-14 00:00:00 +0100
permalink: physics-informed-neural-learning-for-ida-pbc-control-of-underactuated-usvs-under-parameter-uncertainty
year: 2026
authors: Kai Yu, Kun Xie, Weidong Zhang, Zehua Jia
category: proceedings
---
 
## Authors
[Kai Yu](authors/kai-yu), [Kun Xie](authors/kun-xie), [Weidong Zhang](authors/weidong-zhang), [Zehua Jia](authors/zehua-jia)
 
## Abstract
To address the difficulty of obtaining accurate dynamics matrices for underactuated unmanned surface vehicles (USVs) and the structural inconsistency of conventional black-box data-driven models, this paper proposes a physics-informed learning and control framework under the Port-Hamiltonian (PH) formulation. A physics informed neural network (PINN) is constructed by embedding PH structural constraints into a Neural ODE architecture, so that the system matrices can be learned while preserving key physical properties, including symmetry, positive definiteness, and dissipativity. Utilizing the extracted dynamic parameters, an interconnection and damping assignment passivity-based control (IDA-PBC) law is synthesized to execute precise USV trajectory tracking. To validate the proposed methodology, a numerical simulation test is conducted. The findings confirm that our network successfully identifies the core physical characteristics, which in turn empowers the controller to track circular references robustly, even in the presence of parameter mismatches.
 
## Citation
- **Journal:** Second International Conference on Robotics and Sensor Networks (RoSeN 2026)
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 72
- **Publisher:** SPIE
- **DOI:** [10.1117/12.3118885](https://doi.org/10.1117/12.3118885)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Yu_2026,
  title={{Physics-informed neural learning for IDA-PBC control of underactuated USVs under parameter uncertainty}},
  DOI={10.1117/12.3118885},
  booktitle={{Second International Conference on Robotics and Sensor Networks (RoSeN 2026)}},
  publisher={SPIE},
  author={Yu, Kai and Xie, Kun and Zhang, Weidong and Jia, Zehua},
  editor={Zuo, Zhiqiang and Zhang, Xuebo and Xia, Chengyi},
  year={2026},
  pages={72}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/physics-informed-neural-learning-for-ida-pbc-control-of-underactuated-usvs-under-parameter-uncertainty.bib)
 
