---
layout: post
title: "Nonisothermal Cahn–Hilliard Navier–Stokes system"
date: 2024-09-12 00:00:00 +0100
permalink: nonisothermal-cahn-hilliard-navier-stokes-system
year: 2024
authors: Aaron Brunk, Dennis Schumann
category: articles
---
 
## Authors
[Aaron Brunk](authors/aaron_brunk), [Dennis Schumann](authors/dennis_schumann)
 
## Abstract
In this research, we introduce and investigate an approximation method that preserves the structural integrity of the non‐isothermal Cahn–Hilliard–Navier–Stokes system. Our approach extends a previously proposed technique by Brunk and Schumann, which utilizes conforming (inf‐sup stable) finite elements in space, coupled with implicit time discretization employing convex‐concave splitting. Expanding upon this method, we incorporate the unstable pair for the Navier–Stokes contributions, integrating Brezzi–Pitkäranta stabilization. Additionally, we improve the enforcement of incompressibility conditions through grad–div stabilization. While these techniques are well‐established for Navier–Stokes equations, it becomes apparent that for non‐isothermal models, they introduce additional coupling terms to the equation governing internal energy. To ensure the conservation of total energy and maintain entropy production, these stabilization terms are appropriately integrated into the internal energy equation.
 
## Citation
- **Journal:** PAMM
- **Year:** 2024
- **Volume:** 24
- **Issue:** 2
- **Pages:** 
- **Publisher:** Wiley
- **DOI:** [10.1002/pamm.202400060](https://doi.org/10.1002/pamm.202400060)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Brunk_2024,
  title={{Nonisothermal Cahn–Hilliard Navier–Stokes system}},
  volume={24},
  ISSN={1617-7061},
  DOI={10.1002/pamm.202400060},
  number={2},
  journal={PAMM},
  publisher={Wiley},
  author={Brunk, Aaron and Schumann, Dennis},
  year={2024}
}
{% endraw %}
{% endhighlight %}
 
## References
- Brunk A. &Schumann D.(2024).Structure‐preserving approximation for the non‐isothermal Cahn‐Hilliard‐Navier‐Stokes system. InProceedings ENUMATH 2023. Manuscript submitted for publication.https://arxiv.org/abs/2402.00147
- Yang, Y., Kühn, P., Yi, M., Egger, H. & Xu, B.-X. Non-isothermal Phase-Field Modeling of Heat–Melt–Microstructure-Coupled Processes During Powder Bed Fusion. JOM vol. 72 1719–1733 (2020) -- [10.1007/s11837-019-03982-y](https://doi.org/10.1007/s11837-019-03982-y)
- Dadvand, A., Bagheri, M., Samkhaniani, N., Marschall, H. & Wörner, M. Advected phase-field method for bounded solution of the Cahn–Hilliard Navier–Stokes equations. Physics of Fluids vol. 33 (2021) -- [10.1063/5.0048614](https://doi.org/10.1063/5.0048614)
- Alt H. W. &Pawlow I.(1990).Dynamics of non‐isothermal phase separation. InK.‐H.Hoffmann &J.Sprekels(Eds.) Free boundary value problems: Proceedings of a conference held at the Mathematisches Forschungsinstitut Oberwolfach July 9–15 1989(pp.1–26).Birkhäuser.
- Alt, H. W. & Pawlow, I. A mathematical model of dynamics of non-isothermal phase separation. Physica D: Nonlinear Phenomena vol. 59 389–416 (1992) -- [10.1016/0167-2789(92)90078-2](https://doi.org/10.1016/0167-2789(92)90078-2)
- Brunk A. Habrich O. Oyedeji T. D. Yang Y. &Xu B.‐X.(2024).Variational approximation for a non‐isothermal coupled phase‐field system: Structure‐preservation & nonlinear stability.Computational Methods in Applied Mathematics. Manuscript submitted for publication. -- [10.1515/cmam-2023-0274](https://doi.org/10.1515/cmam-2023-0274)
- Charach, C. & Fife, P. C. Open Systems &amp; Information Dynamics vol. 5 99–123 (1998) -- [10.1023/A:1009652531731](https://doi.org/10.1023/A:1009652531731)
- Fabrizio, M., Giorgi, C. & Morro, A. A thermodynamic approach to non-isothermal phase-field evolution in continuum physics. Physica D: Nonlinear Phenomena vol. 214 144–156 (2006) -- [10.1016/j.physd.2006.01.002](https://doi.org/10.1016/j.physd.2006.01.002)
- Guo, Z. & Lin, P. A thermodynamically consistent phase-field model for two-phase flows with thermocapillary effects. Journal of Fluid Mechanics vol. 766 226–271 (2015) -- [10.1017/jfm.2014.696](https://doi.org/10.1017/jfm.2014.696)
- Sun, S., Li, J., Zhao, J. & Wang, Q. Structure-Preserving Numerical Approximations to a Non-isothermal Hydrodynamic Model of Binary Fluid Flows. Journal of Scientific Computing vol. 83 (2020) -- [10.1007/s10915-020-01229-6](https://doi.org/10.1007/s10915-020-01229-6)
- John, V. Finite Element Methods for Incompressible Flow Problems. Springer Series in Computational Mathematics (Springer International Publishing, 2016). doi:10.1007/978-3-319-45750-5 -- [10.1007/978-3-319-45750-5](https://doi.org/10.1007/978-3-319-45750-5)
- Brezzi F. &Pitkäranta J.(1984).On the stabilization of finite element approximations of the Stokes equations. InW.Hackbusch(Ed.) Efficient solutions of elliptic systems: Proceedings of a GAMM‐seminar Kiel January 27 –29 1984(pp.11–19).Vieweg+Teubner Verlag. -- [10.1007/978-3-663-14169-3_2](https://doi.org/10.1007/978-3-663-14169-3_2)

