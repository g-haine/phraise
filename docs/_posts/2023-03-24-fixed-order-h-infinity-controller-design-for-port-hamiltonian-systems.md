---
layout: post
title: "Fixed-order H-infinity controller design for port-Hamiltonian systems"
date: 2023-03-24 00:00:00 +0100
permalink: fixed-order-h-infinity-controller-design-for-port-hamiltonian-systems
year: 2023
authors: Paul Schwerdtner, Matthias Voigt
category: articles
tags:
  - Port-Hamiltonian systems
  - Large-scale systems
  - Robust control
  - H-infinity control
  - Fixed-order controllers
---
 
## Authors
[Paul Schwerdtner](authors/paul-schwerdtner), [Matthias Voigt](authors/matthias-voigt)
 
## Abstract
We present a new fixed-order H-infinity controller design method for potentially large-scale port-Hamiltonian (pH) plants. Our method computes controllers that are also pH (and thus passive) such that the resulting closed-loop systems is again passive, which ensures closed-loop stability simply from the structure of the plant and controller matrices. In this way, we can avoid computationally expensive eigenvalue computations that would otherwise be necessary. In combination with a sample-based objective function which allows us to avoid multiple evaluations of the H-infinity norm (which is typically the main computational burden in fixed-order H-infinity controller synthesis), this makes our method well-suited for plants with a high state–space dimension. In our numerical experiments, we show that applying a passivity-enforcing post-processing step after using well-established H-infinity synthesis methods often leads to a deteriorated H-infinity performance. By contrast, our method computes pH controllers, that are automatically passive and simultaneously aim to minimize the H-infinity norm of the closed-loop transfer function. Moreover, our experiments show that for large-scale plants, our method is significantly faster than the well-established fixed-order H-infinity controller synthesis methods.
 
## Keywords
Port-Hamiltonian systems; Large-scale systems; Robust control; H-infinity control; Fixed-order controllers
 
## Citation
- **Journal:** Automatica
- **Year:** 2023
- **Volume:** 152
- **Issue:** 
- **Pages:** 110918
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2023.110918](https://doi.org/10.1016/j.automatica.2023.110918)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Schwerdtner_2023,
  title={{Fixed-order H-infinity controller design for port-Hamiltonian systems}},
  volume={152},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2023.110918},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Schwerdtner, Paul and Voigt, Matthias},
  year={2023},
  pages={110918}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/fixed-order-h-infinity-controller-design-for-port-hamiltonian-systems.bib)
 
## References
- Aliyev, N., Benner, P., Mengi, E., Schwerdtner, P. & Voigt, M. Large-Scale Computation of $\mathcal{L}_\infty$-Norms by a Greedy Subspace Method. SIAM Journal on Matrix Analysis and Applications vol. 38 1496–1516 (2017) -- [10.1137/16m1086200](https://doi.org/10.1137/16m1086200)
- Anderson, B. D. O. & Liu, Y. Controller reduction: concepts and approaches. IEEE Transactions on Automatic Control vol. 34 802–812 (1989) -- [10.1109/9.29422](https://doi.org/10.1109/9.29422)
- Apkarian, P. & Noll, D. Nonsmooth H∞Synthesis. IEEE Transactions on Automatic Control vol. 51 71–86 (2006) -- [10.1109/tac.2005.860290](https://doi.org/10.1109/tac.2005.860290)
- Apkarian, P. & Noll, D. Structured H∞‐control of infinite‐dimensional systems. International Journal of Robust and Nonlinear Control vol. 28 3212–3238 (2018) -- [10.1002/rnc.4073](https://doi.org/10.1002/rnc.4073)
- Beattie, (2022)
- [Beattie, C., Mehrmann, V., Xu, H. & Zwart, H. Linear port-Hamiltonian descriptor systems. Mathematics of Control, Signals, and Systems vol. 30 (2018)](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- Benner, P., Byers, R., Losse, P., Mehrmann, V. & Xu, H. Robust formulas for optimal <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si1.gif" display="inline" overflow="scroll"><mml:msub><mml:mrow><mml:mi>H</mml:mi></mml:mrow><mml:mrow><mml:mi>∞</mml:mi></mml:mrow></mml:msub></mml:math> controllers. Automatica vol. 47 2639–2646 (2011) -- [10.1016/j.automatica.2011.09.013](https://doi.org/10.1016/j.automatica.2011.09.013)
- Benner, P., Byers, R., Mehrmann, V. & Xu, H. Numerical Computation of Deflating Subspaces of Skew-Hamiltonian/Hamiltonian Pencils. SIAM Journal on Matrix Analysis and Applications vol. 24 165–190 (2002) -- [10.1137/s0895479800367439](https://doi.org/10.1137/s0895479800367439)
- Benner, P., Heiland, J. & Werner, S. W. R. Robust output-feedback stabilization for incompressible flows using low-dimensional $$\mathcal {H}_{\infty }$$-controllers. Computational Optimization and Applications vol. 82 225–249 (2022) -- [10.1007/s10589-022-00359-x](https://doi.org/10.1007/s10589-022-00359-x)
- Benner, P., Mitchell, T. & Overton, M. L. Low-Order Control Design using a Reduced-Order Model with a Stability Constraint on the Full-Order Model. 2018 IEEE Conference on Decision and Control (CDC) 3000–3005 (2018) doi:10.1109/cdc.2018.8619449 -- [10.1109/cdc.2018.8619449](https://doi.org/10.1109/cdc.2018.8619449)
- Breiten, (2022)
- Burke, J. V., Henrion, D., Lewis, A. S. & Overton, M. L. HIFOO - A MATLAB PACKAGE FOR FIXED-ORDER CONTROLLER DESIGN AND H OPTIMIZATION. IFAC Proceedings Volumes vol. 39 339–344 (2006) -- [10.3182/20060705-3-fr-2907.00059](https://doi.org/10.3182/20060705-3-fr-2907.00059)
- Cherifi, (2022)
- Coelho, C. P., Phillips, J. & Silveira, L. M. A Convex Programming Approach for Generating Guaranteed Passive Approximations to Tabulated Frequency-Data. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems vol. 23 293–301 (2004) -- [10.1109/tcad.2003.822107](https://doi.org/10.1109/tcad.2003.822107)
- A Course in H∞ Control Theory. Lecture Notes in Control and Information Sciences (Springer-Verlag, 1987). doi:10.1007/bfb0007371 -- [10.1007/bfb0007371](https://doi.org/10.1007/bfb0007371)
- Gabarrou, M., Alazard, D. & Noll, D. Structured flight control law design using non-smooth optimization. IFAC Proceedings Volumes vol. 43 536–541 (2010) -- [10.3182/20100906-5-jp-2022.00091](https://doi.org/10.3182/20100906-5-jp-2022.00091)
- Geromel, J. C., de Souza, C. C. & Skelton, R. E. Static output feedback controllers: stability and convexity. IEEE Transactions on Automatic Control vol. 43 120–125 (1998) -- [10.1109/9.654912](https://doi.org/10.1109/9.654912)
- [Gillis, N. & Sharma, P. Finding the Nearest Positive-Real System. SIAM Journal on Numerical Analysis vol. 56 1022–1047 (2018)](finding-the-nearest-positive-real-system) -- [10.1137/17m1137176](https://doi.org/10.1137/17m1137176)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Transactions on Circuits and Systems I: Regular Papers vol. 51 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Grivet-Talocia, Passive macromodeling. (2015)
- [Gugercin, S., Polyuga, R. V., Beattie, C. & van der Schaft, A. Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica vol. 48 1963–1974 (2012)](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Guglielmi, N., Gürbüzbalaban, M. & Overton, M. L. Fast Approximation of the $H_\infty$ Norm via Optimization over Spectral Value Sets. SIAM Journal on Matrix Analysis and Applications vol. 34 709–737 (2013) -- [10.1137/120875752](https://doi.org/10.1137/120875752)
- Gustavsen, B. & Semlyen, A. Enforcing passivity for admittance matrices approximated by rational functions. IEEE Transactions on Power Systems vol. 16 97–104 (2001) -- [10.1109/59.910786](https://doi.org/10.1109/59.910786)
- Hauschild, S.-A. et al. Port-Hamiltonian Modeling of District Heating Networks. Differential-Algebraic Equations Forum 333–355 (2020) doi:10.1007/978-3-030-53905-4_11 -- [10.1007/978-3-030-53905-4_11](https://doi.org/10.1007/978-3-030-53905-4_11)
- Khalil, (2002)
- Kunkel, (2006)
- Leibfritz, (2004)
- Mehl, C., Mehrmann, V. & Wojtylak, M. Distance problems for dissipative Hamiltonian systems and related matrix polynomials. Linear Algebra and its Applications vol. 623 335–366 (2021) -- [10.1016/j.laa.2020.05.026](https://doi.org/10.1016/j.laa.2020.05.026)
- [Mehrmann, V., Morandin, R., Olmi, S. & Schöll, E. Qualitative stability and synchronicity analysis of power network models in port-Hamiltonian form. Chaos: An Interdisciplinary Journal of Nonlinear Science vol. 28 (2018)](qualitative-stability-and-synchronicity-analysis-of-power-network-models-in-port-hamiltonian-form) -- [10.1063/1.5054850](https://doi.org/10.1063/1.5054850)
- [Mehrmann, V. & Unger, B. Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica vol. 32 395–515 (2023)](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- Mitchell, T. & Overton, M. L. Fixed Low-Order Controller Design and H∞Optimization for Large-Scale Dynamical Systems. IFAC-PapersOnLine vol. 48 25–30 (2015) -- [10.1016/j.ifacol.2015.09.428](https://doi.org/10.1016/j.ifacol.2015.09.428)
- Mitchell, T. & Overton, M. L. Hybrid expansion–contraction: a robust scaleable method for approximating theH∞norm. IMA Journal of Numerical Analysis vol. 36 985–1014 (2015) -- [10.1093/imanum/drv046](https://doi.org/10.1093/imanum/drv046)
- K Mogensen, P. & N Riseth, A. Optim: A mathematical optimization package for Julia. Journal of Open Source Software vol. 3 615 (2018) -- [10.21105/joss.00615](https://doi.org/10.21105/joss.00615)
- Moser, (2022)
- Mustafa, D. & Glover, K. Controller reduction by H/sub infinity /-balanced truncation. IEEE Transactions on Automatic Control vol. 36 668–682 (1991) -- [10.1109/9.86941](https://doi.org/10.1109/9.86941)
- O’Donoghue, B., Chu, E., Parikh, N. & Boyd, S. Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding. Journal of Optimization Theory and Applications vol. 169 1042–1068 (2016) -- [10.1007/s10957-016-0892-3](https://doi.org/10.1007/s10957-016-0892-3)
- Oliveira, G. H. C., Rodier, C. & Ihlenfeld, L. P. R. K. LMI-Based Method for Estimating Passive Blackbox Models in Power Systems Transient Analysis. IEEE Transactions on Power Delivery vol. 31 3–10 (2016) -- [10.1109/tpwrd.2014.2379444](https://doi.org/10.1109/tpwrd.2014.2379444)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 53 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- [Ramírez, H., Le Gorrec, Y., Maschke, B. & Couenne, F. On the passivity based control of irreversible processes: A port-Hamiltonian approach. Automatica vol. 64 105–111 (2016)](on-the-passivity-based-control-of-irreversible-processes-a-port-hamiltonian-approach) -- [10.1016/j.automatica.2015.07.002](https://doi.org/10.1016/j.automatica.2015.07.002)
- Ravanbod, L. & Noll, D. Gain-scheduled two-loop autopilot for an aircraft. IFAC Proceedings Volumes vol. 45 772–777 (2012) -- [10.3182/20120620-3-dk-2025.00060](https://doi.org/10.3182/20120620-3-dk-2025.00060)
- [Schwerdtner, P. & Voigt, M. Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine vol. 54 143–148 (2021)](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- [Schwerdtner, P. & Voigt, M. SOBMOR: Structured Optimization-Based Model Order Reduction. SIAM Journal on Scientific Computing vol. 45 A502–A529 (2023)](sobmor-structured-optimization-based-model-order-reduction) -- [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
- Skogestad, (2005)
- Wang, F.-C. & Chen, H.-T. Design and implementation of fixed-order robust controllers for a proton exchange membrane fuel cell system. International Journal of Hydrogen Energy vol. 34 2705–2717 (2009) -- [10.1016/j.ijhydene.2008.11.101](https://doi.org/10.1016/j.ijhydene.2008.11.101)
- Werner, (2022)
- [Zhang, M., Borja, P., Ortega, R., Liu, Z. & Su, H. PID Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 63 1032–1044 (2018)](pid-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2017.2732283](https://doi.org/10.1109/tac.2017.2732283)
- Zhou, (1996)

