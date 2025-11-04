---
title: "Robust Nonlinear Control of STATCOMs"
date: 2014-12-01 00:00:00 +0100
permalink: robust-nonlinear-control-of-statcoms
year: 2015
authors: Yonghao Gui, Chunghun Kim, Youngseong Han, Chung Choo Chung
category: chapters
tags:
  - input–output feedback linearization, nonlinear feedback controller, passivity-based control, port-controlled hamiltonian, statcom
---
 
## Authors
[Yonghao Gui](authors/yonghao-gui), [Chunghun Kim](authors/chunghun-kim), [Youngseong Han](authors/youngseong-han), [Chung Choo Chung](authors/chung-choo-chung)
 
## Abstract
Many nonlinear control techniques for STATCOM systems are available nowadays. In this chapter several nonlinear feedback controller design techniques relatively simpler and more robust are to be introduced: input–output feedback linearization (IOL) method, passivity-based control (PBC) method, port-controlled Hamiltonian (PCH) method with dynamics extension method. The IOL method has been applied to STATCOM and it shows uniform transient performance. However, the oscillatory response owing to the lightly damped internal dynamics could negatively affect the life cycle of the system and power quality. A modified IOL control scheme is introduced to improve the damping of internal dynamics of performance while preserving overall system stability. Although the IOL methods improve the performance of type 2 STATCOM systems, these methods are sensitive to parameter uncertainty. Moreover, when the system is working in the inductive operating range, undesired oscillatory transient response appears in the DC voltage due to its lightly damped internal dynamics with the IOL method. The PBC method considers the dynamics characteristics of type 2 STATCOM systems, in particular its passive characteristics. Employing the PBC method improves the robustness of controller implementation and simplifies implementation compared to the IOL method in such a way that it avoids canceling the system nonlinearities exactly. However, since the previous methods are designed based on an approximated model of type 2 STATCOM systems, the closed-loop system has a locally stable equilibrium point. Moreover, the stability region is numerically extensively determined. To overcome the aforementioned problem, PCH with the dynamics extension method is developed for a robust and simple structure of nonlinear controller with the non-approximated model of STATCOM systems in order to improve the performance in time domain and enlarge the stability region.
 
## Keywords
input–output feedback linearization, nonlinear feedback controller, passivity-based control, port-controlled hamiltonian, statcom
 
## Citation
- **ISBN:** 9789812872807
- **Publisher:** Springer Singapore
- **DOI:** [10.1007/978-981-287-281-4_6](https://doi.org/10.1007/978-981-287-281-4_6)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inbook{Gui_2014,
  title={{Robust Nonlinear Control of STATCOMs}},
  ISBN={9789812872814},
  ISSN={1860-4676},
  DOI={10.1007/978-981-287-281-4_6},
  booktitle={{Static Compensators (STATCOMs) in Power Systems}},
  publisher={Springer Singapore},
  author={Gui, Yonghao and Kim, Chunghun and Han, Youngseong and Chung, Chung Choo},
  year={2014},
  pages={187--223}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/robust-nonlinear-control-of-statcoms.bib)
 
## References
- N Hingorani, Understanding facts: concepts and technology of flexible AC transmission systems (2000)
- Schauder, C. & Mehta, H. Vector analysis and control of advanced static VAR compensators. IEE Proc. C Gener. Transm. Distrib. UK 140, 299 (1993) -- [10.1049/ip-c.1993.0044](https://doi.org/10.1049/ip-c.1993.0044)
- Isidori, A. Nonlinear Control Systems. Communications and Control Engineering (Springer London, 1995). doi:10.1007/978-1-84628-615-5 -- [10.1007/978-1-84628-615-5](https://doi.org/10.1007/978-1-84628-615-5)
- H Khalil, Nonlinear systems (2002)
- Petitclair, P., Bacha, S. & Rognon, J. p. Averaged modelling and nonlinear control of an ASVC (advanced static VAr compensator). PESC Record. 27th Annual IEEE Power Electronics Specialists Conference vol. 1 753–758 -- [10.1109/pesc.1996.548666](https://doi.org/10.1109/pesc.1996.548666)
- Petitclair, P., Bacha, S. & Ferrieux, J.-P. Optimized linearization via feedback control law for a STATCOM. IAS ’97. Conference Record of the 1997 IEEE Industry Applications Conference Thirty-Second IAS Annual Meeting vol. 2 880–885 -- [10.1109/ias.1997.628965](https://doi.org/10.1109/ias.1997.628965)
- Han, Youngseong., Lee, Y. O. & Chung, C. C. A modified nonlinear damping of zero &amp;#x2014; Dynamics via feedback control for a STATCOM. 2009 IEEE Bucharest PowerTech 1–8 (2009) doi:10.1109/ptc.2009.5282114 -- [10.1109/ptc.2009.5282114](https://doi.org/10.1109/ptc.2009.5282114)
- Han, Y., Lee, Y. O. & Chung, C. C. Modified non-linear damping of internal dynamics via feedback linearisation for static synchronous compensator. IET Gener. Transm. Distrib. 5, 930–940 (2011) -- [10.1049/iet-gtd.2010.0551](https://doi.org/10.1049/iet-gtd.2010.0551)
- Ortega, R. & García-Canseco, E. Interconnection and Damping Assignment Passivity-Based Control: A Survey. European Journal of Control 10, 432–450 (2004) -- [10.3166/ejc.10.432-450](https://doi.org/10.3166/ejc.10.432-450)
- Ortega, R., Loría, A., Nicklasson, P. J. & Sira-Ramírez, H. Passivity-Based Control of Euler-Lagrange Systems. Communications and Control Engineering (Springer London, 1998). doi:10.1007/978-1-4471-3603-3 -- [10.1007/978-1-4471-3603-3](https://doi.org/10.1007/978-1-4471-3603-3)
- Lee, T.-S. Lagrangian Modeling and Passivity-Based Control of Three-Phase AC/DC Voltage-Source Converters. IEEE Trans. Ind. Electron. 51, 892–902 (2004) -- [10.1109/tie.2004.831753](https://doi.org/10.1109/tie.2004.831753)
- Gui, Y., Lee, Y. O., Han, Y., Kim, W. & Chung, C. C. Passivity-based control with nonlinear damping for STATCOM system. 2012 IEEE 51st IEEE Conference on Decision and Control (CDC) 1715–1720 (2012) doi:10.1109/cdc.2012.6425928 -- [10.1109/cdc.2012.6425928](https://doi.org/10.1109/cdc.2012.6425928)
- J Slotine, Applied nonlinear control (1991)
- Lee, Y. O., Han, Y. & Chung, C. C. Output tracking control with enhanced damping of internal dynamics and its output boundedness for static synchronous compensator system. IET Control Theory Appl. 6, 1445–1455 (2012) -- [10.1049/iet-cta.2011.0340](https://doi.org/10.1049/iet-cta.2011.0340)
- Hamdan, A. M. A. An investigation of the significance of singular value decomposition in power system dynamics. International Journal of Electrical Power &amp; Energy Systems 21, 417–424 (1999) -- [10.1016/s0142-0615(99)00011-3](https://doi.org/10.1016/s0142-0615(99)00011-3)
- Lee, Y. O. & Chung, C. C. Uniform output regulation via approximated input–output linearisation for lightly damped internal dynamics. International Journal of Control 86, 159–171 (2013) -- [10.1080/00207179.2012.721565](https://doi.org/10.1080/00207179.2012.721565)
- Lee, Y. O., Han, Y. & Chung, C. C. Output tracking control with enhanced damping of internal dynamics and its output boundedness. 49th IEEE Conference on Decision and Control (CDC) 3964–3971 (2010) doi:10.1109/cdc.2010.5716997 -- [10.1109/cdc.2010.5716997](https://doi.org/10.1109/cdc.2010.5716997)
- J Marsden, Elementary classical analysis (1993)

