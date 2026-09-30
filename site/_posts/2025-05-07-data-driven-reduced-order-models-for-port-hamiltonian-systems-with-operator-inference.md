---
title: "Data-driven reduced-order models for port-Hamiltonian systems with operator inference"
date: 2025-05-07 00:00:00 +0100
permalink: data-driven-reduced-order-models-for-port-hamiltonian-systems-with-operator-inference
year: 2025
authors: Yuwei Geng, Lili Ju, Boris Kramer, Zhu Wang
category: articles
tags:
  - Port-Hamiltonian system
  - Operator inference
  - Model order reduction
  - Data-driven modeling
---
 
## Authors
[Yuwei Geng](authors/yuwei-geng), [Lili Ju](authors/lili-ju), [Boris Kramer](authors/boris-kramer), [Zhu Wang](authors/zhu-wang)
 
## Abstract
Hamiltonian operator inference has been developed in Sharma et al. (2022) to learn structure-preserving reduced-order models (ROMs) for Hamiltonian systems. The method constructs a low-dimensional model using only data and knowledge of the functional form of the Hamiltonian. The resulting ROMs preserve the intrinsic structure of the system, ensuring that the mechanical and physical properties of the system are maintained. In this work, we extend this approach to port-Hamiltonian systems, which generalize Hamiltonian systems by including energy dissipation, external input, and output. Based on snapshots of the system’s state and output, together with the information about the functional form of the Hamiltonian, reduced operators are inferred through optimization and are then used to construct data-driven ROMs. To further alleviate the complexity of evaluating nonlinear terms in the ROMs, a hyper-reduction method via discrete empirical interpolation is applied. Accordingly, we derive error estimates for the ROM approximations of the state and output. Finally, we demonstrate the structure preservation, as well as the accuracy of the proposed port-Hamiltonian operator inference framework, through numerical experiments on a linear mass–spring-damper problem and a nonlinear Toda lattice problem.
 
## Keywords
Port-Hamiltonian system; Operator inference; Model order reduction; Data-driven modeling
 
## Citation
- **Journal:** Computer Methods in Applied Mechanics and Engineering
- **Year:** 2025
- **Volume:** 442
- **Issue:** 
- **Pages:** 118042
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.cma.2025.118042](https://doi.org/10.1016/j.cma.2025.118042)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Geng_2025,
  title={{Data-driven reduced-order models for port-Hamiltonian systems with operator inference}},
  volume={442},
  ISSN={0045-7825},
  DOI={10.1016/j.cma.2025.118042},
  journal={Computer Methods in Applied Mechanics and Engineering},
  publisher={Elsevier BV},
  author={Geng, Yuwei and Ju, Lili and Kramer, Boris and Wang, Zhu},
  year={2025},
  pages={118042}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/data-driven-reduced-order-models-for-port-hamiltonian-systems-with-operator-inference.bib)
 
## References
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. FnT in Systems and Control 1, 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Duindam, (2009)
- Hairer, E., Hochbruck, M., Iserles, A. & Lubich, C. Geometric Numerical Integration. Oberwolfach Rep. 3, 805–882 (2006) -- [10.4171/owr/2006/14](https://doi.org/10.4171/owr/2006/14)
- Quarteroni, (2015)
- Holmes, (2012)
- Kutz, (2016)
- Schmid, P. J. Dynamic Mode Decomposition and Its Variants. Annu. Rev. Fluid Mech. 54, 225–254 (2022) -- [10.1146/annurev-fluid-030121-015835](https://doi.org/10.1146/annurev-fluid-030121-015835)
- Kramer, B., Peherstorfer, B. & Willcox, K. E. Learning Nonlinear Reduced Models from Data with Operator Inference. Annu. Rev. Fluid Mech. 56, 521–548 (2024) -- [10.1146/annurev-fluid-121021-025220](https://doi.org/10.1146/annurev-fluid-121021-025220)
- Peherstorfer, B. & Willcox, K. Data-driven operator inference for nonintrusive projection-based model reduction. Computer Methods in Applied Mechanics and Engineering 306, 196–215 (2016) -- [10.1016/j.cma.2016.03.025](https://doi.org/10.1016/j.cma.2016.03.025)
- Antoulas, (2005)
- Antoulas, (2020)
- Benner, P., Gugercin, S. & Willcox, K. A Survey of Projection-Based Model Reduction Methods for Parametric Dynamical Systems. SIAM Rev. 57, 483–531 (2015) -- [10.1137/130932715](https://doi.org/10.1137/130932715)
- Hesthaven, (2016)
- Lall, S., Krysl, P. & Marsden, J. E. Structure-preserving model reduction for mechanical systems. Physica D: Nonlinear Phenomena 184, 304–318 (2003) -- [10.1016/s0167-2789(03)00227-6](https://doi.org/10.1016/s0167-2789(03)00227-6)
- Carlberg, K., Tuminaro, R. & Boggs, P. Preserving Lagrangian Structure in Nonlinear Model Reduction with Application to Structural Dynamics. SIAM J. Sci. Comput. 37, B153–B184 (2015) -- [10.1137/140959602](https://doi.org/10.1137/140959602)
- [Gong, Y., Wang, Q. & Wang, Z. Structure-preserving Galerkin POD reduced-order modeling of Hamiltonian systems. Computer Methods in Applied Mechanics and Engineering 315, 780–798 (2017)](structure-preserving-galerkin-pod-reduced-order-modeling-of-hamiltonian-systems) -- [10.1016/j.cma.2016.11.016](https://doi.org/10.1016/j.cma.2016.11.016)
- Miyatake, Y. Structure-preserving model reduction for dynamical systems with a first integral. Japan J. Indust. Appl. Math. 36, 1021–1037 (2019) -- [10.1007/s13160-019-00378-y](https://doi.org/10.1007/s13160-019-00378-y)
- Barbulescu, Efficient model reduction of myelinated compartments as port-Hamiltonian systems. (2021)
- Beattie, Structure-preserving model reduction for nonlinear port-Hamiltonian systems. (2011)
- [Chaturantabut, S., Beattie, C. & Gugercin, S. Structure-Preserving Model Reduction for Nonlinear Port-Hamiltonian Systems. SIAM J. Sci. Comput. 38, B837–B865 (2016)](structure-preserving-model-reduction-for-nonlinear-port-hamiltonian-systems) -- [10.1137/15m1055085](https://doi.org/10.1137/15m1055085)
- Peng, L. & Mohseni, K. Symplectic Model Reduction of Hamiltonian Systems. SIAM J. Sci. Comput. 38, A1–A27 (2016) -- [10.1137/140978922](https://doi.org/10.1137/140978922)
- Gruber, A. & Tezaur, I. Variationally Consistent Hamiltonian Model Reduction. SIAM J. Appl. Dyn. Syst. 24, 376–414 (2025) -- [10.1137/24m1652490](https://doi.org/10.1137/24m1652490)
- Afkham, B. M. & Hesthaven, J. S. Structure Preserving Model Reduction of Parametric Hamiltonian Systems. SIAM J. Sci. Comput. 39, A2616–A2644 (2017) -- [10.1137/17m1111991](https://doi.org/10.1137/17m1111991)
- Hesthaven, J. S. & Pagliantini, C. Structure-preserving reduced basis methods for Poisson systems. Math. Comp. 90, 1701–1740 (2021) -- [10.1090/mcom/3618](https://doi.org/10.1090/mcom/3618)
- Pagliantini, C. Dynamical reduced basis methods for Hamiltonian systems. Numer. Math. 148, 409–448 (2021) -- [10.1007/s00211-021-01211-w](https://doi.org/10.1007/s00211-021-01211-w)
- Hesthaven, J. S., Pagliantini, C. & Rozza, G. Reduced basis methods for time-dependent problems. Acta Numerica 31, 265–345 (2022) -- [10.1017/s0962492922000058](https://doi.org/10.1017/s0962492922000058)
- Barrault, M., Maday, Y., Nguyen, N. C. & Patera, A. T. An ‘empirical interpolation’ method: application to efficient reduced-basis discretization of partial differential equations. Comptes Rendus. Mathématique 339, 667–672 (2004) -- [10.1016/j.crma.2004.08.006](https://doi.org/10.1016/j.crma.2004.08.006)
- Chaturantabut, S. & Sorensen, D. C. Nonlinear Model Reduction via Discrete Empirical Interpolation. SIAM J. Sci. Comput. 32, 2737–2764 (2010) -- [10.1137/090766498](https://doi.org/10.1137/090766498)
- Pagliantini, C. & Vismara, F. Gradient-Preserving Hyper-Reduction of Nonlinear Dynamical Systems via Discrete Empirical Interpolation. SIAM J. Sci. Comput. 45, A2725–A2754 (2023) -- [10.1137/22m1503890](https://doi.org/10.1137/22m1503890)
- Sharma, H. et al. Symplectic model reduction of Hamiltonian systems using data-driven quadratic manifolds. Computer Methods in Applied Mechanics and Engineering 417, 116402 (2023) -- [10.1016/j.cma.2023.116402](https://doi.org/10.1016/j.cma.2023.116402)
- Yıldız, S., Goyal, P., Bendokat, T. & Benner, P. DATA-DRIVEN IDENTIFICATION OF QUADRATIC REPRESENTATIONS FOR NONLINEAR HAMILTONIAN SYSTEMS USING WEAKLY SYMPLECTIC LIFTINGS. J Mach Learn Model Comput 5, 45–71 (2024) -- [10.1615/jmachlearnmodelcomput.2024052810](https://doi.org/10.1615/jmachlearnmodelcomput.2024052810)
- Buchfink, P., Glas, S. & Haasdonk, B. Symplectic Model Reduction of Hamiltonian Systems on Nonlinear Manifolds and Approximation with Weakly Symplectic Autoencoder. SIAM J. Sci. Comput. 45, A289–A311 (2023) -- [10.1137/21m1466657](https://doi.org/10.1137/21m1466657)
- Sharma, H., Wang, Z. & Kramer, B. Hamiltonian operator inference: Physics-preserving learning of reduced-order models for canonical Hamiltonian systems. Physica D: Nonlinear Phenomena 431, 133122 (2022) -- [10.1016/j.physd.2021.133122](https://doi.org/10.1016/j.physd.2021.133122)
- Gruber, A. & Tezaur, I. Canonical and noncanonical Hamiltonian operator inference. Computer Methods in Applied Mechanics and Engineering 416, 116334 (2023) -- [10.1016/j.cma.2023.116334](https://doi.org/10.1016/j.cma.2023.116334)
- Geng, Y., Singh, J., Ju, L., Kramer, B. & Wang, Z. Gradient preserving Operator Inference: Data-driven reduced-order models for equations with gradient structure. Computer Methods in Applied Mechanics and Engineering 427, 117033 (2024) -- [10.1016/j.cma.2024.117033](https://doi.org/10.1016/j.cma.2024.117033)
- Vijaywargiya, (2025)
- [Cherifi, K., Goyal, P. & Benner, P. A non-intrusive method to inferring linear port-Hamiltonian realizations using time-domain data. etna 56, 102–116 (2022)](a-non-intrusive-method-to-inferring-linear-port-hamiltonian-realizations-using-time-domain-data) -- [10.1553/etna_vol56s102](https://doi.org/10.1553/etna_vol56s102)
- [Morandin, R., Nicodemus, J. & Unger, B. Port-Hamiltonian Dynamic Mode Decomposition. SIAM J. Sci. Comput. 45, A1690–A1710 (2023)](port-hamiltonian-dynamic-mode-decomposition) -- [10.1137/22m149329x](https://doi.org/10.1137/22m149329x)
- Berkooz, G., Holmes, P. & Lumley, J. L. The Proper Orthogonal Decomposition in the Analysis of Turbulent Flows. Annu. Rev. Fluid Mech. 25, 539–575 (1993) -- [10.1146/annurev.fl.25.010193.002543](https://doi.org/10.1146/annurev.fl.25.010193.002543)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48, 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Drmač, Z. & Gugercin, S. A New Selection Operator for the Discrete Empirical Interpolation Method---Improved A Priori Error Bound and Extensions. SIAM J. Sci. Comput. 38, A631–A648 (2016) -- [10.1137/15m1019271](https://doi.org/10.1137/15m1019271)
- Helmberg, C., Rendl, F., Vanderbei, R. J. & Wolkowicz, H. An Interior-Point Method for Semidefinite Programming. SIAM J. Optim. 6, 342–361 (1996) -- [10.1137/0806020](https://doi.org/10.1137/0806020)
- Chaturantabut, S. & Sorensen, D. C. A State Space Error Estimate for POD-DEIM Nonlinear Model Reduction. SIAM J. Numer. Anal. 50, 46–63 (2012) -- [10.1137/110822724](https://doi.org/10.1137/110822724)
- Dahlquist, (1958)
- Kunisch, K. & Volkwein, S. Galerkin proper orthogonal decomposition methods for parabolic problems. Numerische Mathematik 90, 117–148 (2001) -- [10.1007/s002110100282](https://doi.org/10.1007/s002110100282)
- Singler, J. R. New POD Error Expressions, Error Bounds, and Asymptotic Results for Reduced Order Models of Parabolic PDEs. SIAM J. Numer. Anal. 52, 852–876 (2014) -- [10.1137/120886947](https://doi.org/10.1137/120886947)
- Peherstorfer, B. Sampling Low-Dimensional Markovian Dynamics for Preasymptotically Recovering Reduced Models from Data with Operator Inference. SIAM J. Sci. Comput. 42, A3489–A3515 (2020) -- [10.1137/19m1292448](https://doi.org/10.1137/19m1292448)
- Polyuga, (2010)
- ApS, Mosek optimization toolbox for matlab. User’s Guid. Ref. Man. Vers. (2019)
- Diamond, CVXPY: A Python-embedded modeling language for convex optimization. J. Mach. Learn. Res. (2016)
- Agrawal, A., Verschueren, R., Diamond, S. & Boyd, S. A rewriting system for convex optimization problems. Journal of Control and Decision 5, 42–60 (2018) -- [10.1080/23307706.2017.1397554](https://doi.org/10.1080/23307706.2017.1397554)
- Farhat, C., Chapman, T. & Avery, P. Structure‐preserving, stability, and accuracy properties of the energy‐conserving sampling and weighting method for the hyper reduction of nonlinear finite element dynamic models. Numerical Meth Engineering 102, 1077–1110 (2015) -- [10.1002/nme.4820](https://doi.org/10.1002/nme.4820)

