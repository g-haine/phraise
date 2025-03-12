---
layout: post
title: "Structure-preserving Galerkin POD reduced-order modeling of Hamiltonian systems"
date: 2016-11-27 00:00:00 +0100
permalink: structure-preserving-galerkin-pod-reduced-order-modeling-of-hamiltonian-systems
year: 2017
authors: Yuezheng Gong, Qi Wang, Zhu Wang
category: articles
tags:
  - Proper orthogonal decomposition
  - Model reduction
  - Hamiltonian systems
  - Structure-preserving algorithms
---
 
## Authors
[Yuezheng Gong](authors/yuezheng-gong), [Qi Wang](authors/qi-wang), [Zhu Wang](authors/zhu-wang)
 
## Abstract
The proper orthogonal decomposition reduced-order model (POD-ROM) has been widely used as a computationally efficient surrogate model in large-scale numerical simulations of complex systems. However, when it is applied to a Hamiltonian system, a naive application of the POD method can destroy the Hamiltonian structure in the reduced-order model. In this paper, we develop a new reduced-order modeling approach for Hamiltonian systems, which modifies the Galerkin projection-based POD-ROM so that the appropriate Hamiltonian structure is preserved. Since the POD truncation can degrade the approximation of the Hamiltonian function, we propose to use a POD basis from shifted snapshots to improve the approximation to the Hamiltonian function. We further derive a rigorous a priori error estimate for the structure-preserving ROM and demonstrate its effectiveness in several numerical examples. This approach can be readily extended to dissipative Hamiltonian systems, port-Hamiltonian systems, etc.
 
## Keywords
Proper orthogonal decomposition; Model reduction; Hamiltonian systems; Structure-preserving algorithms
 
## Citation
- **Journal:** Computer Methods in Applied Mechanics and Engineering
- **Year:** 2017
- **Volume:** 315
- **Issue:** 
- **Pages:** 780--798
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.cma.2016.11.016](https://doi.org/10.1016/j.cma.2016.11.016)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gong_2017,
  title={{Structure-preserving Galerkin POD reduced-order modeling of Hamiltonian systems}},
  volume={315},
  ISSN={0045-7825},
  DOI={10.1016/j.cma.2016.11.016},
  journal={Computer Methods in Applied Mechanics and Engineering},
  publisher={Elsevier BV},
  author={Gong, Yuezheng and Wang, Qi and Wang, Zhu},
  year={2017},
  pages={780--798}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/structure-preserving-galerkin-pod-reduced-order-modeling-of-hamiltonian-systems.bib)
 
## References
- Hairer, (2002)
- Feng, (2010)
- Bridges, T. J. & Reich, S. Numerical methods for Hamiltonian PDEs. Journal of Physics A: Mathematical and General vol. 39 5287–5320 (2006) -- [10.1088/0305-4470/39/19/s02](https://doi.org/10.1088/0305-4470/39/19/s02)
- Wang, Multi-symplectic algorithms for Hamiltonian partial differential equations. Commun. Appl. Math. Comput. (2013)
- [Gonzalez, O. Time integration and discrete Hamiltonian systems. Journal of Nonlinear Science vol. 6 449–467 (1996)](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- McLachlan, R. I., Quispel, G. R. W. & Robidoux, N. Geometric integration using discrete gradients. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 357 1021–1045 (1999) -- [10.1098/rsta.1999.0363](https://doi.org/10.1098/rsta.1999.0363)
- Quispel, G. R. W. & McLaren, D. I. A new class of energy-preserving numerical integration methods. Journal of Physics A: Mathematical and Theoretical vol. 41 045206 (2008) -- [10.1088/1751-8113/41/4/045206](https://doi.org/10.1088/1751-8113/41/4/045206)
- Hairer, Energy-preserving variant of collocation methods. J. Numer. Anal. Ind. Appl. Math. (2010)
- Cohen, D. & Hairer, E. Linear energy-preserving integrators for Poisson systems. BIT Numerical Mathematics vol. 51 91–101 (2011) -- [10.1007/s10543-011-0310-z](https://doi.org/10.1007/s10543-011-0310-z)
- Celledoni, E. et al. Preserving energy resp. dissipation in numerical PDEs using the “Average Vector Field” method. Journal of Computational Physics vol. 231 6770–6789 (2012) -- [10.1016/j.jcp.2012.06.022](https://doi.org/10.1016/j.jcp.2012.06.022)
- Furihata, D. Finite Difference Schemes for ∂u∂t=(∂∂x)αδGδu That Inherit Energy Conservation or Dissipation Property. Journal of Computational Physics vol. 156 181–205 (1999) -- [10.1006/jcph.1999.6377](https://doi.org/10.1006/jcph.1999.6377)
- Matsuo, T. & Furihata, D. Dissipative or Conservative Finite-Difference Schemes for Complex-Valued Nonlinear Partial Differential Equations. Journal of Computational Physics vol. 171 425–447 (2001) -- [10.1006/jcph.2001.6775](https://doi.org/10.1006/jcph.2001.6775)
- Furihata, Discrete variational derivative method. A structure-preserving numerical method for partial differential equations. Chapman & Hall/CRC Numer. Anal. Sci. Comput. (2011)
- Dahlby, M. & Owren, B. A General Framework for Deriving Integral Preserving Numerical Methods for PDEs. SIAM Journal on Scientific Computing vol. 33 2318–2340 (2011) -- [10.1137/100810174](https://doi.org/10.1137/100810174)
- Gong, Y., Cai, J. & Wang, Y. Some new structure-preserving algorithms for general multi-symplectic formulations of Hamiltonian PDEs. Journal of Computational Physics vol. 279 80–102 (2014) -- [10.1016/j.jcp.2014.09.001](https://doi.org/10.1016/j.jcp.2014.09.001)
- Bui-Thanh, T., Willcox, K., Ghattas, O. & van Bloemen Waanders, B. Goal-oriented, model-constrained optimization for reduction of large-scale systems. Journal of Computational Physics vol. 224 880–896 (2007) -- [10.1016/j.jcp.2006.10.026](https://doi.org/10.1016/j.jcp.2006.10.026)
- Carlberg, K. & Farhat, C. A low‐cost, goal‐oriented ‘compact proper orthogonal decomposition’ basis for model reduction of static systems. International Journal for Numerical Methods in Engineering vol. 86 381–402 (2010) -- [10.1002/nme.3074](https://doi.org/10.1002/nme.3074)
- Chaturantabut, S. & Sorensen, D. C. Nonlinear Model Reduction via Discrete Empirical Interpolation. SIAM Journal on Scientific Computing vol. 32 2737–2764 (2010) -- [10.1137/090766498](https://doi.org/10.1137/090766498)
- Daescu, D. N. & Navon, I. M. A Dual-Weighted Approach to Order Reduction in 4DVAR Data Assimilation. Monthly Weather Review vol. 136 1026–1041 (2008) -- [10.1175/2007mwr2102.1](https://doi.org/10.1175/2007mwr2102.1)
- Holmes, (1996)
- Iollo, A., Lanteri, S. & Désidéri, J.-A. Stability Properties of POD-Galerkin Approximations for the Compressible Navier-Stokes Equations. Theoretical and Computational Fluid Dynamics vol. 13 377–396 (2000) -- [10.1007/s001620050119](https://doi.org/10.1007/s001620050119)
- Kunisch, K. & Volkwein, S. Galerkin proper orthogonal decomposition methods for parabolic problems. Numerische Mathematik vol. 90 117–148 (2001) -- [10.1007/s002110100282](https://doi.org/10.1007/s002110100282)
- Sirisup, S. & Karniadakis, G. E. A spectral viscosity method for correcting the long-term behavior of POD models. Journal of Computational Physics vol. 194 92–116 (2004) -- [10.1016/j.jcp.2003.08.021](https://doi.org/10.1016/j.jcp.2003.08.021)
- Lassila, Model order reduction in fluid dynamics: challenges and perspectives. (2014)
- Attia, The reduced-order hybrid Monte Carlo sampling smoother. Internat. J. Numer. Methods Fluids (2016)
- Balajewicz, M., Tezaur, I. & Dowell, E. Minimal subspace rotation on the Stiefel manifold for stabilization and enhancement of projection-based reduced order models for the compressible Navier–Stokes equations. Journal of Computational Physics vol. 321 224–241 (2016) -- [10.1016/j.jcp.2016.05.037](https://doi.org/10.1016/j.jcp.2016.05.037)
- Rowley, C. W., Colonius, T. & Murray, R. M. Model reduction for compressible flows using POD and Galerkin projection. Physica D: Nonlinear Phenomena vol. 189 115–129 (2004) -- [10.1016/j.physd.2003.03.001](https://doi.org/10.1016/j.physd.2003.03.001)
- Barone, M. F., Kalashnikova, I., Segalman, D. J. & Thornquist, H. K. Stable Galerkin reduced order models for linearized compressible flow. Journal of Computational Physics vol. 228 1932–1946 (2009) -- [10.1016/j.jcp.2008.11.015](https://doi.org/10.1016/j.jcp.2008.11.015)
- Serre, G., Lafon, P., Gloerfelt, X. & Bailly, C. Reliable reduced-order models for time-dependent linearized Euler equations. Journal of Computational Physics vol. 231 5176–5194 (2012) -- [10.1016/j.jcp.2012.04.019](https://doi.org/10.1016/j.jcp.2012.04.019)
- Beattie, C. & Gugercin, S. Interpolatory projection methods for structure-preserving model reduction. Systems &amp; Control Letters vol. 58 225–232 (2009) -- [10.1016/j.sysconle.2008.10.016](https://doi.org/10.1016/j.sysconle.2008.10.016)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Beattie, Structure-preserving model reduction for nonlinear port-Hamiltonian systems. (2011)
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- Peng, L. & Mohseni, K. Symplectic Model Reduction of Hamiltonian Systems. SIAM Journal on Scientific Computing vol. 38 A1–A27 (2016) -- [10.1137/140978922](https://doi.org/10.1137/140978922)
- Carlberg, K., Tuminaro, R. & Boggs, P. Preserving Lagrangian Structure in Nonlinear Model Reduction with Application to Structural Dynamics. SIAM Journal on Scientific Computing vol. 37 B153–B184 (2015) -- [10.1137/140959602](https://doi.org/10.1137/140959602)
- Farhat, C., Chapman, T. & Avery, P. Structure‐preserving, stability, and accuracy properties of the energy‐conserving sampling and weighting method for the hyper reduction of nonlinear finite element dynamic models. International Journal for Numerical Methods in Engineering vol. 102 1077–1110 (2015) -- [10.1002/nme.4820](https://doi.org/10.1002/nme.4820)
- Wang, Z., McBee, B. & Iliescu, T. Approximate partitioned method of snapshots for POD. Journal of Computational and Applied Mathematics vol. 307 374–384 (2016) -- [10.1016/j.cam.2015.11.023](https://doi.org/10.1016/j.cam.2015.11.023)
- Chaturantabut, S. & Sorensen, D. C. A State Space Error Estimate for POD-DEIM Nonlinear Model Reduction. SIAM Journal on Numerical Analysis vol. 50 46–63 (2012) -- [10.1137/110822724](https://doi.org/10.1137/110822724)
- Carlberg, K., Farhat, C., Cortial, J. & Amsallem, D. The GNAT method for nonlinear model reduction: Effective implementation and application to computational fluid dynamics and turbulent flows. Journal of Computational Physics vol. 242 623–647 (2013) -- [10.1016/j.jcp.2013.02.028](https://doi.org/10.1016/j.jcp.2013.02.028)
- Karasözen, B. & Şimşek, G. Energy preserving integration of bi-Hamiltonian partial differential equations. Applied Mathematics Letters vol. 26 1125–1133 (2013) -- [10.1016/j.aml.2013.06.005](https://doi.org/10.1016/j.aml.2013.06.005)
- Wang, Z., Akhtar, I., Borggaard, J. & Iliescu, T. Proper orthogonal decomposition closure models for turbulent flows: A numerical comparison. Computer Methods in Applied Mechanics and Engineering vols 237–240 10–26 (2012) -- [10.1016/j.cma.2012.04.015](https://doi.org/10.1016/j.cma.2012.04.015)

