---
title: "Current-Constrained Control for PMSM Based on Port-Controlled Hamiltonion System and Deep Deterministic Policy Gradient"
date: 2021-10-08 00:00:00 +0100
permalink: current-constrained-control-for-pmsm-based-on-port-controlled-hamiltonion-system-and-deep-deterministic-policy-gradient
year: 2022
authors: Min Wang, Qi Wang, Bing Chu, Yanhong Liu
category: chapters
tags:
  - current-constrained controller, ddpg, ida-pbc, pch, pmsm
---
 
## Authors
[Min Wang](authors/min-wang), [Qi Wang](authors/qi-wang), [Bing Chu](authors/bing-chu), [Yanhong Liu](authors/yanhong-liu)
 
## Abstract
This paper proposes a current-constrained control approach on the basis of port-controlled Hamiltonion (PCH) system and deep deterministic policy gradient (DDPG) for permanent magnet synchronous motor (PMSM). PCH system of PMSM views the plant to control from the perspective of overall energy and the interconnection and damping assignment passivity-based (IDA-PBC) control approach based on PCH is single-loop, which has the advantages of simple controller design and fewer adjusting parameters, but causes the problem of overcurrent. The method proposed in this paper solves this problem by setting the coefficient of damping assignment matrix from reinforcement learning of DDPG. First, we give the Hamiltonian model of PMSM. Next, a current-constrained control approach on the basis of PCH and DDPG for PMSM is proposed. Finally, the validity of the method is verified by the simulations.
 
## Keywords
current-constrained controller, ddpg, ida-pbc, pch, pmsm
 
## Citation
- **ISBN:** 9789811663710
- **Publisher:** Springer Singapore
- **DOI:** [10.1007/978-981-16-6372-7_45](https://doi.org/10.1007/978-981-16-6372-7_45)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inbook{Wang_2021,
  title={{Current-Constrained Control for PMSM Based on Port-Controlled Hamiltonion System and Deep Deterministic Policy Gradient}},
  ISBN={9789811663727},
  ISSN={1876-1119},
  DOI={10.1007/978-981-16-6372-7_45},
  booktitle={{Proceedings of 2021 Chinese Intelligent Automation Conference}},
  publisher={Springer Singapore},
  author={Wang, Min and Wang, Qi and Chu, Bing and Liu, Yanhong},
  year={2021},
  pages={398--405}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/current-constrained-control-for-pmsm-based-on-port-controlled-hamiltonion-system-and-deep-deterministic-policy-gradient.bib)
 
## References
- Khorashadizadeh, S. & Sadeghijaleh, M. Adaptive fuzzy tracking control of robot manipulators actuated by permanent magnet synchronous motors. Computers &amp; Electrical Engineering 72, 100–111 (2018) -- [10.1016/j.compeleceng.2018.09.010](https://doi.org/10.1016/j.compeleceng.2018.09.010)
- A Zhou, Math. Probl. Eng. (2020)
- Trabelsi, M., Semail, E., Nguyen, N. K. & Meinguet, F. Open Switch Fault effects analysis in five-phase PMSM designed for aerospace application. 2016 International Symposium on Power Electronics, Electrical Drives, Automation and Motion (SPEEDAM) 14–21 (2016) doi:10.1109/speedam.2016.7525939 -- [10.1109/speedam.2016.7525939](https://doi.org/10.1109/speedam.2016.7525939)
- W Wang, IEEE Trans. Magn. (2021)
- Rath, B. N. & Subudhi, B. On‐line extreme learning algorithm based identification and non‐linear model predictive controller for way‐point tracking application of an autonomous underwater vehicle. Cognitive Comp and Systems 1, 61–71 (2019) -- [10.1049/ccs.2018.0008](https://doi.org/10.1049/ccs.2018.0008)
- Bamgbose, S. O., Li, X. & Qian, L. Neural network‐based non‐linear adaptive controller design for a class of bilinear system. Cognitive Comp and Systems 2, 1–11 (2020) -- [10.1049/ccs.2019.0015](https://doi.org/10.1049/ccs.2019.0015)
- Wang, C. & Zhu, Z. Q. Fuzzy Logic Speed Control of Permanent Magnet Synchronous Machine and Feedback Voltage Ripple Reduction in Flux-Weakening Operation Region. IEEE Trans. on Ind. Applicat. 56, 1505–1517 (2020) -- [10.1109/tia.2020.2967673](https://doi.org/10.1109/tia.2020.2967673)
- Changliang Xia, Chen Guo & Tingna Shi. A Neural-Network-Identifier and Fuzzy-Controller-Based Algorithm for Dynamic Decoupling Control of Permanent-Magnet Spherical Motor. IEEE Trans. Ind. Electron. 57, 2868–2878 (2010) -- [10.1109/tie.2009.2036030](https://doi.org/10.1109/tie.2009.2036030)
- Yin, Z., Gong, L., Du, C., Liu, J. & Zhong, Y. Integrated Position and Speed Loops Under Sliding-Mode Control Optimized by Differential Evolution Algorithm for PMSM Drives. IEEE Trans. Power Electron. 34, 8994–9005 (2019) -- [10.1109/tpel.2018.2889781](https://doi.org/10.1109/tpel.2018.2889781)
- Wang, Q. et al. A Low-Complexity Optimal Switching Time-Modulated Model-Predictive Control for PMSM With Three-Level NPC Converter. IEEE Trans. Transp. Electrific. 6, 1188–1198 (2020) -- [10.1109/tte.2020.3012352](https://doi.org/10.1109/tte.2020.3012352)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Batlle, C., Dòria-Cerezo, A., Espinosa-Pérez, G. & Ortega, R. Simultaneous interconnection and damping assignment passivity-based control: the induction machine case study. International Journal of Control 82, 241–255 (2009) -- [10.1080/00207170802050817](https://doi.org/10.1080/00207170802050817)
- [Zeng, J., Zhang, Z. & Qiao, W. An Interconnection and Damping Assignment Passivity-Based Controller for a DC–DC Boost Converter With a Constant Power Load. IEEE Trans. on Ind. Applicat. 50, 2314–2322 (2014)](an-interconnection-and-damping-assignment-passivity-based-controller-for-a-dc-dc-boost-converter-with-a-constant-power-load) -- [10.1109/tia.2013.2290872](https://doi.org/10.1109/tia.2013.2290872)
- Zhang, T. & Xia, J. Interconnection and Damping Assignment Passivity-Based Impedance Control of a Compliant Assistive Robot for Physical Human–Robot Interactions. IEEE Robot. Autom. Lett. 4, 538–545 (2019) -- [10.1109/lra.2019.2891434](https://doi.org/10.1109/lra.2019.2891434)

