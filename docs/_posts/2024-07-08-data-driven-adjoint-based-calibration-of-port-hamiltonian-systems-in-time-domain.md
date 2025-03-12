---
layout: post
title: "Data-driven adjoint-based calibration of port-Hamiltonian systems in time domain"
date: 2024-07-08 00:00:00 +0100
permalink: data-driven-adjoint-based-calibration-of-port-hamiltonian-systems-in-time-domain
year: 2024
authors: Michael Günther, Birgit Jacob, Claudia Totzeck
category: articles
tags:
  - Port-Hamiltonian systems
  - Data-driven approach
  - Optimal control
  - Adjoint-based calibration
  - Time domain
  - Coupled dynamical systems
  - Structure preservation
  - 37J06
  - 37M99
  - 49J15
  - 49K15
  - 49M29
  - 49Q12
  - 65P10
  - 93A30
  - 93B30
  - 93C05
---
 
## Authors
[Michael Günther](authors/michael-gunther), [Birgit Jacob](authors/birgit-jacob), [Claudia Totzeck](authors/claudia-totzeck)
 
## Abstract
We present a gradient-based calibration algorithm to identify the system matrices of a linear port-Hamiltonian system from given input–output time data. Aiming for a direct structure-preserving approach, we employ techniques from optimal control with ordinary differential equations and define a constrained optimization problem. The input-to-state stability is discussed which is the key step towards the existence of optimal controls. Further, we derive the first-order optimality system taking into account the port-Hamiltonian structure. Indeed, the proposed method preserves the skew symmetry and positive (semi)-definiteness of the system matrices throughout the optimization iterations. Numerical results with perturbed and unperturbed synthetic data, as well as an example from the PHS benchmark collection [ 17 ] demonstrate the feasibility of the approach.
 
## Keywords
Port-Hamiltonian systems; Data-driven approach; Optimal control; Adjoint-based calibration; Time domain; Coupled dynamical systems; Structure preservation; 37J06; 37M99; 49J15; 49K15; 49M29; 49Q12; 65P10; 93A30; 93B30; 93C05
 
## Citation
- **Journal:** Mathematics of Control, Signals, and Systems
- **Year:** 2024
- **Volume:** 36
- **Issue:** 4
- **Pages:** 957--977
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s00498-024-00389-2](https://doi.org/10.1007/s00498-024-00389-2)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{G_nther_2024,
  title={{Data-driven adjoint-based calibration of port-Hamiltonian systems in time domain}},
  volume={36},
  ISSN={1435-568X},
  DOI={10.1007/s00498-024-00389-2},
  number={4},
  journal={Mathematics of Control, Signals, and Systems},
  publisher={Springer Science and Business Media LLC},
  author={Günther, Michael and Jacob, Birgit and Totzeck, Claudia},
  year={2024},
  pages={957--977}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/data-driven-adjoint-based-calibration-of-port-hamiltonian-systems-in-time-domain.bib)
 
## References
- Antoulas, A. C., Lefteriu, S. & Ionita, A. C. Chapter 8: A Tutorial Introduction to the Loewner Framework for Model Reduction. Model Reduction and Approximation 335–376 (2017) doi:10.1137/1.9781611974829.ch8 -- [10.1137/1.9781611974829.ch8](https://doi.org/10.1137/1.9781611974829.ch8)
- Absil, P.-A., Mahony, R. & Sepulchre, R. Optimization Algorithms on Matrix Manifolds. (2008) doi:10.1515/9781400830244 -- [10.1515/9781400830244](https://doi.org/10.1515/9781400830244)
- [Benner, P., Goyal, P. & Van Dooren, P. Identification of port-Hamiltonian systems from frequency response data. Systems &amp; Control Letters vol. 143 104741 (2020)](identification-of-port-hamiltonian-systems-from-frequency-response-data) -- [10.1016/j.sysconle.2020.104741](https://doi.org/10.1016/j.sysconle.2020.104741)
- N Boumal. Boumal N, Mishra B, Absil P-A, Sepulchre R (2014) Manopt, a Matlab toolbox for optimization on manifolds. Journal of Machine Learning Research 15(42):1455–1459 (2014)
- [Cherifi, K., Goyal, P. & Benner, P. A non-intrusive method to inferring linear port-Hamiltonian realizations using time-domain data. ETNA - Electronic Transactions on Numerical Analysis vol. 56 102–116 (2022)](a-non-intrusive-method-to-inferring-linear-port-hamiltonian-realizations-using-time-domain-data) -- [10.1553/etna_vol56s102](https://doi.org/10.1553/etna_vol56s102)
- [Cherifi, K., Gernandt, H. & Hinsen, D. The difference between port-Hamiltonian, passive and positive real descriptor systems. Mathematics of Control, Signals, and Systems vol. 36 451–482 (2023)](the-difference-between-port-hamiltonian-passive-and-positive-real-descriptor-systems) -- [10.1007/s00498-023-00373-2](https://doi.org/10.1007/s00498-023-00373-2)
- Cherifi, K., Mehrmann, V. & Hariche, K. Numerical methods to compute a minimal realization of a port-Hamiltonian system. Preprint at https://doi.org/10.48550/ARXIV.1903.07042 (2019) -- [10.48550/arxiv.1903.07042](https://doi.org/10.48550/arxiv.1903.07042)
- [Duindam, V., Macchelli, A., Stramigioli, S. & Bruyninckx, H. Modeling and Control of Complex Physical Systems. (Springer Berlin Heidelberg, 2009). doi:10.1007/978-3-642-03196-0](modeling-and-control-of-complex-physical-systems) -- [10.1007/978-3-642-03196-0](https://doi.org/10.1007/978-3-642-03196-0)
- Eberard, D., Maschke, B. M. & van der Schaft, A. J. An extension of Hamiltonian systems to the thermodynamic phase space: Towards a geometry of nonreversible processes. Reports on Mathematical Physics vol. 60 175–198 (2007) -- [10.1016/s0034-4877(07)00024-9](https://doi.org/10.1016/s0034-4877(07)00024-9)
- Günther, M., Jacob, B. & Totzeck, C. Structure-preserving identification of port-Hamiltonian systems -- a sensitivity-based approach. Preprint at https://doi.org/10.48550/ARXIV.2301.02019 (2023) -- [10.48550/arxiv.2301.02019](https://doi.org/10.48550/arxiv.2301.02019)
- M Hinze. Hinze M, Pinnau R, Ulbrich M, Ulbrich S (2008) Optimization with PDE constraints. Springer (2008)
- Lennart Ljung. Ljung Lennart (1999) System Identification: Theory for the User. Prentice-Hall Inc, USA (1999)
- Mehrmann, V. & Morandin, R. Structure-preserving discretization for port-Hamiltonian descriptor systems. 2019 IEEE 58th Conference on Decision and Control (CDC) 6863–6868 (2019) doi:10.1109/cdc40024.2019.9030180 -- [10.1109/cdc40024.2019.9030180](https://doi.org/10.1109/cdc40024.2019.9030180)
- [Morandin, R., Nicodemus, J. & Unger, B. Port-Hamiltonian Dynamic Mode Decomposition. SIAM Journal on Scientific Computing vol. 45 A1690–A1710 (2023)](port-hamiltonian-dynamic-mode-decomposition) -- [10.1137/22m149329x](https://doi.org/10.1137/22m149329x)
- Sato, H. Riemannian Conjugate Gradient Methods: General Framework and Specific Algorithms with Convergence Analyses. SIAM Journal on Optimization vol. 32 2690–2717 (2022) -- [10.1137/21m1464178](https://doi.org/10.1137/21m1464178)
- Schwerdtner P (2021) Port-Hamiltonian system identification from noisy frequency response data. arXiv:2106.11355
- Schwerdtner P, Port-Hamiltonian benchmark systems, 8.12.2022. https://github.com/Algopaul/PortHamiltonianBenchmarkSystems.jl
- Teschl, G. Ordinary Differential Equations and Dynamical Systems. Graduate Studies in Mathematics (2012) doi:10.1090/gsm/140 -- [10.1090/gsm/140](https://doi.org/10.1090/gsm/140)
- F Tröltzsch. Tröltzsch F (2010) Optimal control of partial differential equations: theory, methods, and applications. American Mathematical Soc (2010)
- A van der Schaft. van der Schaft A (2006) Port-Hamiltonian systems: an introductory survey. In Proceedings on the International Congress of Mathematicians 3:1339–1366 (2006)
- Willems, J. C. Dissipative dynamical systems Part II: Linear systems with quadratic supply rates. Archive for Rational Mechanics and Analysis vol. 45 352–393 (1972) -- [10.1007/bf00276494](https://doi.org/10.1007/bf00276494)

