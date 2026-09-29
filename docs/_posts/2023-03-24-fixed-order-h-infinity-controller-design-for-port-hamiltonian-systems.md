---
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
- Aliyev N, Benner P, Mengi E, Schwerdtner P, Voigt M (2017) Large-Scale Computation of $\mathcal{L}_\infty$-Norms by a Greedy Subspace Method. SIAM J Matrix Anal Appl 38(4):1496–1516. https://doi.org/10.1137/16m1086200 -- [10.1137/16m1086200](https://doi.org/10.1137/16m1086200)
- Anderson BDO, Liu Y (1989) Controller reduction: concepts and approaches. IEEE Trans Automat Contr 34(8):802–812. https://doi.org/10.1109/9.29422 -- [10.1109/9.29422](https://doi.org/10.1109/9.29422)
- Apkarian P, Noll D (2006) Nonsmooth H
                    <sub>∞</sub>
                    Synthesis. IEEE Trans Automat Contr 51(1):71–86. https://doi.org/10.1109/tac.2005.860290 -- [10.1109/tac.2005.860290](https://doi.org/10.1109/tac.2005.860290)
- Apkarian P, Noll D (2018) Structured <i>H</i><sub><i>∞</i></sub>‐control of infinite‐dimensional systems. Intl J Robust &amp; Nonlinear 28(9):3212–3238. https://doi.org/10.1002/rnc.4073 -- [10.1002/rnc.4073](https://doi.org/10.1002/rnc.4073)
- Beattie, (2022)
- [Beattie C, Mehrmann V, Xu H, Zwart H (2018) Linear port-Hamiltonian descriptor systems. Math Control Signals Syst 30(4):17. https://doi.org/10.1007/s00498-018-0223-3](linear-port-hamiltonian-descriptor-systems) -- [10.1007/s00498-018-0223-3](https://doi.org/10.1007/s00498-018-0223-3)
- Benner P, Byers R, Losse P, Mehrmann V, Xu H (2011) Robust formulas for optimal \(H_{\infty}\) controllers. Automatica 47(12):2639–2646. https://doi.org/10.1016/j.automatica.2011.09.013 -- [10.1016/j.automatica.2011.09.013](https://doi.org/10.1016/j.automatica.2011.09.013)
- Benner P, Byers R, Mehrmann V, Xu H (2002) Numerical Computation of Deflating Subspaces of Skew-Hamiltonian/Hamiltonian Pencils. SIAM J Matrix Anal Appl 24(1):165–190. https://doi.org/10.1137/s0895479800367439 -- [10.1137/s0895479800367439](https://doi.org/10.1137/s0895479800367439)
- Benner P, Heiland J, Werner SWR (2022) Robust output-feedback stabilization for incompressible flows using low-dimensional $$\mathcal {H}_{\infty }$$-controllers. Comput Optim Appl 82(1):225–249. https://doi.org/10.1007/s10589-022-00359-x -- [10.1007/s10589-022-00359-x](https://doi.org/10.1007/s10589-022-00359-x)
- Benner P, Mitchell T, Overton ML (2018) Low-Order Control Design using a Reduced-Order Model with a Stability Constraint on the Full-Order Model. In: 2018 IEEE Conference on Decision and Control (CDC). IEEE, pp 3000–3005 -- [10.1109/cdc.2018.8619449](https://doi.org/10.1109/cdc.2018.8619449)
- Breiten, (2022)
- Burke JV, Henrion D, Lewis AS, Overton ML (2006) HIFOO - A MATLAB PACKAGE FOR FIXED-ORDER CONTROLLER DESIGN AND H OPTIMIZATION. IFAC Proceedings Volumes 39(9):339–344. https://doi.org/10.3182/20060705-3-fr-2907.00059 -- [10.3182/20060705-3-fr-2907.00059](https://doi.org/10.3182/20060705-3-fr-2907.00059)
- Cherifi, (2022)
- Coelho CP, Phillips J, Silveira LM (2004) A Convex Programming Approach for Generating Guaranteed Passive Approximations to Tabulated Frequency-Data. IEEE Trans Comput-Aided Des Integr Circuits Syst 23(2):293–301. https://doi.org/10.1109/tcad.2003.822107 -- [10.1109/tcad.2003.822107](https://doi.org/10.1109/tcad.2003.822107)
- Francis BA (ed) (1987) A Course in H∞ Control Theory. Springer-Verlag, Berlin/Heidelberg -- [10.1007/bfb0007371](https://doi.org/10.1007/bfb0007371)
- Gabarrou M, Alazard D, Noll D (2010) Structured flight control law design using non-smooth optimization. IFAC Proceedings Volumes 43(15):536–541. https://doi.org/10.3182/20100906-5-jp-2022.00091 -- [10.3182/20100906-5-jp-2022.00091](https://doi.org/10.3182/20100906-5-jp-2022.00091)
- Geromel JC, de Souza CC, Skelton RE (1998) Static output feedback controllers: stability and convexity. IEEE Trans Automat Contr 43(1):120–125. https://doi.org/10.1109/9.654912 -- [10.1109/9.654912](https://doi.org/10.1109/9.654912)
- [Gillis N, Sharma P (2018) Finding the Nearest Positive-Real System. SIAM J Numer Anal 56(2):1022–1047. https://doi.org/10.1137/17m1137176](finding-the-nearest-positive-real-system) -- [10.1137/17m1137176](https://doi.org/10.1137/17m1137176)
- Grivet-Talocia S (2004) Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Trans Circuits Syst I 51(9):1755–1769. https://doi.org/10.1109/tcsi.2004.834527 -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Grivet-Talocia, Passive macromodeling. (2015)
- [Gugercin S, Polyuga RV, Beattie C, van der Schaft A (2012) Structure-preserving tangential interpolation for model reduction of port-Hamiltonian systems. Automatica 48(9):1963–1974. https://doi.org/10.1016/j.automatica.2012.05.052](structure-preserving-tangential-interpolation-for-model-reduction-of-port-hamiltonian-systems) -- [10.1016/j.automatica.2012.05.052](https://doi.org/10.1016/j.automatica.2012.05.052)
- Guglielmi N, Gürbüzbalaban M, Overton ML (2013) Fast Approximation of the $H_\infty$ Norm via Optimization over Spectral Value Sets. SIAM J Matrix Anal Appl 34(2):709–737. https://doi.org/10.1137/120875752 -- [10.1137/120875752](https://doi.org/10.1137/120875752)
- Gustavsen B, Semlyen A (2001) Enforcing passivity for admittance matrices approximated by rational functions. IEEE Trans Power Syst 16(1):97–104. https://doi.org/10.1109/59.910786 -- [10.1109/59.910786](https://doi.org/10.1109/59.910786)
- [Hauschild S-A, Marheineke N, Mehrmann V, Mohring J, Badlyan AM, Rein M, Schmidt M (2020) Port-Hamiltonian Modeling of District Heating Networks. In: Differential-Algebraic Equations Forum. Springer International Publishing, Cham, pp 333–355](port-hamiltonian-modeling-of-district-heating-networks) -- [10.1007/978-3-030-53905-4_11](https://doi.org/10.1007/978-3-030-53905-4_11)
- Khalil, (2002)
- Kunkel, (2006)
- Leibfritz, (2004)
- [Mehl C, Mehrmann V, Wojtylak M (2021) Distance problems for dissipative Hamiltonian systems and related matrix polynomials. Linear Algebra and its Applications 623:335–366. https://doi.org/10.1016/j.laa.2020.05.026](distance-problems-for-dissipative-hamiltonian-systems-and-related-matrix-polynomials) -- [10.1016/j.laa.2020.05.026](https://doi.org/10.1016/j.laa.2020.05.026)
- [Mehrmann V, Morandin R, Olmi S, Schöll E (2018) Qualitative stability and synchronicity analysis of power network models in port-Hamiltonian form. Chaos: An Interdisciplinary Journal of Nonlinear Science 28(10):101102. https://doi.org/10.1063/1.5054850](qualitative-stability-and-synchronicity-analysis-of-power-network-models-in-port-hamiltonian-form) -- [10.1063/1.5054850](https://doi.org/10.1063/1.5054850)
- [Mehrmann V, Unger B (2023) Control of port-Hamiltonian differential-algebraic systems and applications. Acta Numerica 32:395–515. https://doi.org/10.1017/s0962492922000083](control-of-port-hamiltonian-differential-algebraic-systems-and-applications) -- [10.1017/s0962492922000083](https://doi.org/10.1017/s0962492922000083)
- Mitchell T, Overton ML (2015) Fixed Low-Order Controller Design and H∞Optimization for Large-Scale Dynamical Systems. IFAC-PapersOnLine 48(14):25–30. https://doi.org/10.1016/j.ifacol.2015.09.428 -- [10.1016/j.ifacol.2015.09.428](https://doi.org/10.1016/j.ifacol.2015.09.428)
- Mitchell T, Overton ML (2015) Hybrid expansion–contraction: a robust scaleable method for approximating the<i>H</i><sub>∞</sub>norm. IMA J Numer Anal 36(3):985–1014. https://doi.org/10.1093/imanum/drv046 -- [10.1093/imanum/drv046](https://doi.org/10.1093/imanum/drv046)
- K Mogensen P, N Riseth A (2018) Optim: A mathematical optimization package for Julia. JOSS 3(24):615. https://doi.org/10.21105/joss.00615 -- [10.21105/joss.00615](https://doi.org/10.21105/joss.00615)
- Moser, (2022)
- Mustafa D, Glover K (1991) Controller reduction by H/sub infinity /-balanced truncation. IEEE Trans Automat Contr 36(6):668–682. https://doi.org/10.1109/9.86941 -- [10.1109/9.86941](https://doi.org/10.1109/9.86941)
- O’Donoghue B, Chu E, Parikh N, Boyd S (2016) Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding. J Optim Theory Appl 169(3):1042–1068. https://doi.org/10.1007/s10957-016-0892-3 -- [10.1007/s10957-016-0892-3](https://doi.org/10.1007/s10957-016-0892-3)
- Oliveira GHC, Rodier C, Ihlenfeld LPRK (2016) LMI-Based Method for Estimating Passive Blackbox Models in Power Systems Transient Analysis. IEEE Trans Power Delivery 31(1):3–10. https://doi.org/10.1109/tpwrd.2014.2379444 -- [10.1109/tpwrd.2014.2379444](https://doi.org/10.1109/tpwrd.2014.2379444)
- [Ortega R, van der Schaft A, Castanos F, Astolfi A (2008) Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans Automat Contr 53(11):2527–2542. https://doi.org/10.1109/tac.2008.2006930](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- [Ramírez H, Le Gorrec Y, Maschke B, Couenne F (2016) On the passivity based control of irreversible processes: A port-Hamiltonian approach. Automatica 64:105–111. https://doi.org/10.1016/j.automatica.2015.07.002](on-the-passivity-based-control-of-irreversible-processes-a-port-hamiltonian-approach) -- [10.1016/j.automatica.2015.07.002](https://doi.org/10.1016/j.automatica.2015.07.002)
- Ravanbod L, Noll D (2012) Gain-scheduled two-loop autopilot for an aircraft. IFAC Proceedings Volumes 45(13):772–777. https://doi.org/10.3182/20120620-3-dk-2025.00060 -- [10.3182/20120620-3-dk-2025.00060](https://doi.org/10.3182/20120620-3-dk-2025.00060)
- Robu B, Budinger V, Baudouin L, Prieur C, Arzelier D (2010) Simultaneous H&lt;inf&gt;&amp;#x221E;&lt;/inf&gt; vibration control of fluid/plate system via reduced-order controller. In: 49th IEEE Conference on Decision and Control (CDC). IEEE, pp 3146–3151 -- [10.1109/cdc.2010.5718057](https://doi.org/10.1109/cdc.2010.5718057)
- [Schwerdtner P, Voigt M (2021) Adaptive Sampling for Structure-Preserving Model Order Reduction of Port-Hamiltonian Systems. IFAC-PapersOnLine 54(19):143–148. https://doi.org/10.1016/j.ifacol.2021.11.069](adaptive-sampling-for-structure-preserving-model-order-reduction-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2021.11.069](https://doi.org/10.1016/j.ifacol.2021.11.069)
- [Schwerdtner P, Voigt M (2023) SOBMOR: Structured Optimization-Based Model Order Reduction. SIAM J Sci Comput 45(2):A502–A529. https://doi.org/10.1137/20m1380235](sobmor-structured-optimization-based-model-order-reduction) -- [10.1137/20m1380235](https://doi.org/10.1137/20m1380235)
- Skogestad, (2005)
- Wang F-C, Chen H-T (2009) Design and implementation of fixed-order robust controllers for a proton exchange membrane fuel cell system. International Journal of Hydrogen Energy 34(6):2705–2717. https://doi.org/10.1016/j.ijhydene.2008.11.101 -- [10.1016/j.ijhydene.2008.11.101](https://doi.org/10.1016/j.ijhydene.2008.11.101)
- Werner, (2022)
- [Zhang M, Borja P, Ortega R, Liu Z, Su H (2018) PID Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans Automat Contr 63(4):1032–1044. https://doi.org/10.1109/tac.2017.2732283](pid-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2017.2732283](https://doi.org/10.1109/tac.2017.2732283)
- Zhou, (1996)

