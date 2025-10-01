---
title: "Bayesian Port–Hamiltonian Surrogate for Three-Phase Reservoir Flow Simulation"
date: 2025-09-16 00:00:00 +0100
permalink: bayesian-port-hamiltonian-surrogate-for-three-phase-reservoir-flow-simulation
year: 2025
authors: Ryan Farell, J. Eric Bickel, Chandrajit Bajaj
category: proceedings
---
 
## Authors
[Ryan Farell](authors/ryan-farell), [J. Eric Bickel](authors/j-eric-bickel), [Chandrajit Bajaj](authors/chandrajit-bajaj)
 
## Abstract
 We present a learned structure-preserving surrogate operator in the form of a Hamiltonian Network that reproduces full-physics three-phase slightly-compressible flow simulations at roughly 10× lower computational cost while retaining fundamental conservation laws. We express the reservoir dynamics as a finite-volume port–Hamiltonian (pH) dynamic system and to progressively learn the Hamiltonian through its dynamic vector field with Bayesian optimization, and using a scalable mixture-of-Gaussian-process (MoGP) prior. The pH scaffold enforces mass balance, passivity, and Lyapunov stability by construction; the Bayesian GP treatment supplies calibrated epistemic uncertainty that propagates through the surrogate estimation state process and can be used to quantify forecast uncertainty in closed-loop reservoir management. Unlike previously published neural-operator and reduced-order surrogates, our method guarantees conservation without ad-hoc penalties and delivers analytic gradients for adjoint-free history matching.
 
## Citation
- **Journal:** Middle East Oil, Gas and Geosciences Show (MEOS GEO)
- **Year:** 2025
- **Volume:** 
- **Issue:** 
- **Pages:** 
- **Publisher:** SPE
- **DOI:** [10.2118/227802-ms](https://doi.org/10.2118/227802-ms)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Farell_2025,
  series={25MEOS},
  title={{Bayesian Port–Hamiltonian Surrogate for Three-Phase Reservoir Flow Simulation}},
  DOI={10.2118/227802-ms},
  booktitle={{Middle East Oil, Gas and Geosciences Show (MEOS GEO)}},
  publisher={SPE},
  author={Farell, Ryan and Eric Bickel, J. and Bajaj, Chandrajit},
  year={2025}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/bayesian-port-hamiltonian-surrogate-for-three-phase-reservoir-flow-simulation.bib)
 
## References
- Aziz, Petroleum Reservoir Simulation (1979)
- Badawi, D. & Gildin, E. Neural operator-based proxy for reservoir simulations considering varying well settings, locations, and permeability fields. Computers &amp; Geosciences 196, 105826 (2025) -- [10.1016/j.cageo.2024.105826](https://doi.org/10.1016/j.cageo.2024.105826)
- cardoso, M. A. . A. & Durlofsky, L. J. . J. Use of Reduced-Order Modeling Procedures for Production Optimization. SPE Journal 15, 426–435 (2009) -- [10.2118/119057-pa](https://doi.org/10.2118/119057-pa)
- Cardoso, M. A. & Durlofsky, L. J. Linearized reduced-order models for subsurface flow simulation. Journal of Computational Physics 229, 681–700 (2010) -- [10.1016/j.jcp.2009.10.004](https://doi.org/10.1016/j.jcp.2009.10.004)
- Rahimi, Random features for large-scale kernel machines. Advances in neural information processing systems (2007)
- Rasmussen, A. F. et al. The Open Porous Media Flow reservoir simulator. Computers &amp; Mathematics with Applications 81, 159–185 (2021) -- [10.1016/j.camwa.2020.05.014](https://doi.org/10.1016/j.camwa.2020.05.014)
- Roth, Stable port-hamiltonian neural networks. arXiv preprint arXiv:2502.02480 (2025)
- Li, Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010.08895 (2020)
- Lu, L., Jin, P., Pang, G., Zhang, Z. & Karniadakis, G. E. Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators. Nat Mach Intell 3, 218–229 (2021) -- [10.1038/s42256-021-00302-5](https://doi.org/10.1038/s42256-021-00302-5)
- Moradi, Port-hamiltonian neural networks with output error noise models. arXiv preprint arXiv:2502.14432 (2025)
- Nasir, Y. & Durlofsky, L. J. Deep reinforcement learning for optimal well control in subsurface systems with uncertain geology. Journal of Computational Physics 477, 111945 (2023) -- [10.1016/j.jcp.2023.111945](https://doi.org/10.1016/j.jcp.2023.111945)
- Odeh, A. S. Comparison of Solutions to a Three-Dimensional Black-Oil Reservoir Simulation Problem (includes associated paper 9741 ). Journal of Petroleum Technology 33, 13–25 (1981) -- [10.2118/9723-pa](https://doi.org/10.2118/9723-pa)
- Tang, M., Liu, Y. & Durlofsky, L. J. A deep-learning-based surrogate model for data assimilation in dynamic subsurface flow problems. Journal of Computational Physics 413, 109456 (2020) -- [10.1016/j.jcp.2020.109456](https://doi.org/10.1016/j.jcp.2020.109456)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. FnT in Systems and Control 1, 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Wang, N., Chang, H. & Zhang, D. Surrogate and inverse modeling for two-phase flow in porous media via theory-guided convolutional neural network. Journal of Computational Physics 466, 111419 (2022) -- [10.1016/j.jcp.2022.111419](https://doi.org/10.1016/j.jcp.2022.111419)
- Wen, G., Li, Z., Azizzadenesheli, K., Anandkumar, A. & Benson, S. M. U-FNO—An enhanced Fourier neural operator-based deep-learning model for multiphase flow. Advances in Water Resources 163, 104180 (2022) -- [10.1016/j.advwatres.2022.104180](https://doi.org/10.1016/j.advwatres.2022.104180)
- Zhu, Y. & Zabaras, N. Bayesian deep convolutional encoder–decoder networks for surrogate modeling and uncertainty quantification. Journal of Computational Physics 366, 415–447 (2018) -- [10.1016/j.jcp.2018.04.018](https://doi.org/10.1016/j.jcp.2018.04.018)

