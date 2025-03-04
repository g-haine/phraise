---
layout: post
title: "A structure-preserving, operator splitting scheme for reaction-diffusion equations with detailed balance"
date: 2021-03-05 00:00:00 +0100
permalink: a-structure-preserving-operator-splitting-scheme-for-reaction-diffusion-equations-with-detailed-balance
year: 2021
authors: Chun Liu, Cheng Wang, Yiwei Wang
category: journal-article
tag: Reaction-diffusion system; Energetic variational approach (EnVarA); Logarithmic energy potential; Operator splitting; Positivity preserving; Energy stability
---
 
## Authors
[Chun Liu](authors/chun-liu), [Cheng Wang](authors/cheng-wang), [Yiwei Wang](authors/yiwei-wang)
 
## Abstract
In this paper, we propose and analyze a positivity-preserving, energy stable numerical scheme for a certain type of reaction-diffusion systems involving the Law of Mass Action with the detailed balance condition. The numerical scheme is constructed based on a recently developed energetic variational formulation, in which the reaction part is reformulated in terms of reaction trajectories. The fact that both the reaction and diffusion parts dissipate the same free energy opens a path of designing an energy stable, operator splitting scheme for these systems. At the reaction stage, we solve equations of reaction trajectories by treating all the logarithmic terms in the reformulated form implicitly due to their convex nature. The positivity-preserving property and unique solvability can be theoretically proved, based on the singular behavior of the logarithmic function around the limiting value. Moreover, the energy stability of this scheme at the reaction stage can be proved by a careful convexity analysis. Similar techniques are used to establish the positivity-preserving property and energy stability for the standard semi-implicit solver at the diffusion stage. As a result, a combination of these two stages leads to a positivity-preserving and energy stable numerical scheme for the original reaction-diffusion system. Several numerical examples are presented to demonstrate the robustness of the proposed operator splitting scheme.
 
## Keywords
Reaction-diffusion system; Energetic variational approach (EnVarA); Logarithmic energy potential; Operator splitting; Positivity preserving; Energy stability
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2021
- **Volume:** 436
- **Issue:** 
- **Pages:** 110253
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2021.110253](https://doi.org/10.1016/j.jcp.2021.110253)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Liu_2021,
  title={{A structure-preserving, operator splitting scheme for reaction-diffusion equations with detailed balance}},
  volume={436},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2021.110253},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Liu, Chun and Wang, Cheng and Wang, Yiwei},
  year={2021},
  pages={110253}
}
{% endraw %}
{% endhighlight %}
 
## References
- Alexander, R. Diagonally Implicit Runge–Kutta Methods for Stiff O.D.E.’s. SIAM Journal on Numerical Analysis vol. 14 1006–1021 (1977) -- [10.1137/0714068](https://doi.org/10.1137/0714068)
- Anderson, D. F., Craciun, G., Gopalkrishnan, M. & Wiuf, C. Lyapunov Functions, Stationary Distributions, and Non-equilibrium Potential for Reaction Networks. Bulletin of Mathematical Biology vol. 77 1744–1767 (2015) -- [10.1007/s11538-015-0102-8](https://doi.org/10.1007/s11538-015-0102-8)
- Badia, S., Planas, R. & Gutiérrez‐Santacreu, J. V. Unconditionally stable operator splitting algorithms for the incompressible magnetohydrodynamics system discretized by a stabilized finite element formulation based on projections. International Journal for Numerical Methods in Engineering vol. 93 302–328 (2012) -- [10.1002/nme.4392](https://doi.org/10.1002/nme.4392)
- Bao, W., Jin, S. & Markowich, P. A. On Time-Splitting Spectral Approximations for the Schrödinger Equation in the Semiclassical Regime. Journal of Computational Physics vol. 175 487–524 (2002) -- [10.1006/jcph.2001.6956](https://doi.org/10.1006/jcph.2001.6956)
- BARZILAI, J. & BORWEIN, J. M. Two-Point Step Size Gradient Methods. IMA Journal of Numerical Analysis vol. 8 141–148 (1988) -- [10.1093/imanum/8.1.141](https://doi.org/10.1093/imanum/8.1.141)
- Baskaran, A. et al. Energy stable and efficient finite-difference nonlinear multigrid schemes for the modified phase field crystal equation. Journal of Computational Physics vol. 250 270–292 (2013) -- [10.1016/j.jcp.2013.04.024](https://doi.org/10.1016/j.jcp.2013.04.024)
- Baskaran, A., Lowengrub, J. S., Wang, C. & Wise, S. M. Convergence Analysis of a Second Order Convex Splitting Scheme for the Modified Phase Field Crystal Equation. SIAM Journal on Numerical Analysis vol. 51 2851–2873 (2013) -- [10.1137/120880677](https://doi.org/10.1137/120880677)
- Bataille, J., Edelen, D. G. B. & Kestin, J. Nonequilibrium Thermodynamics of the Nonlinear Equations of Chemical Kinetics. Journal of Non-Equilibrium Thermodynamics vol. 3 (1978) -- [10.1515/jnet.1978.3.3.153](https://doi.org/10.1515/jnet.1978.3.3.153)
- Bátkai, A., Csomós, P. & Farkas, B. Operator splitting for nonautonomous delay equations. Computers &amp; Mathematics with Applications vol. 65 315–324 (2013) -- [10.1016/j.camwa.2012.05.001](https://doi.org/10.1016/j.camwa.2012.05.001)
- Benamou, J.-D., Carlier, G. & Laborde, M. An augmented Lagrangian approach to Wasserstein gradient flows and applications. ESAIM: Proceedings and Surveys vol. 54 1–17 (2016) -- [10.1051/proc/201654001](https://doi.org/10.1051/proc/201654001)
- Bertolazzi, E. Positive and conservative schemes for mass action kinetics. Computers &amp; Mathematics with Applications vol. 32 29–43 (1996) -- [10.1016/0898-1221(96)00142-3](https://doi.org/10.1016/0898-1221(96)00142-3)
- Besse, C., Bidégaray, B. & Descombes, S. Order Estimates in Time of Splitting Methods for the Nonlinear Schrödinger Equation. SIAM Journal on Numerical Analysis vol. 40 26–40 (2002) -- [10.1137/S0036142900381497](https://doi.org/10.1137/S0036142900381497)
- Biot, M. A. Variational-Lagrangian irreversible thermodynamics of initially-stressed solids with thermomolecular diffusion and chemical reactions. Journal of the Mechanics and Physics of Solids vol. 25 289–307 (1977) -- [10.1016/0022-5096(77)90014-X](https://doi.org/10.1016/0022-5096(77)90014-X)
- Biot, M. A. Thermodynamic principle of virtual dissipation and the dynamics of physical-chemical fluid mixtures including radiation pressure. Quarterly of Applied Mathematics vol. 39 517–540 (1982) -- [10.1090/qam/644105](https://doi.org/10.1090/qam/644105)
- Carrillo, J. A., Düring, B., Matthes, D. & McCormick, D. S. A Lagrangian Scheme for the Solution of Nonlinear Diffusion Equations Using Moving Simplex Meshes. Journal of Scientific Computing vol. 75 1463–1499 (2017) -- [10.1007/s10915-017-0594-5](https://doi.org/10.1007/s10915-017-0594-5)
- Chen, W., Conde, S., Wang, C., Wang, X. & Wise, S. M. A Linear Energy Stable Scheme for a Thin Film Model Without Slope Selection. Journal of Scientific Computing vol. 52 546–562 (2011) -- [10.1007/s10915-011-9559-2](https://doi.org/10.1007/s10915-011-9559-2)
- Chen, W., Liu, Y., Wang, C. & Wise, S. M. Convergence analysis of a fully discrete finite difference scheme for the Cahn-Hilliard-Hele-Shaw equation. Mathematics of Computation vol. 85 2231–2257 (2015) -- [10.1090/mcom3052](https://doi.org/10.1090/mcom3052)
- Chipot, M., Kinderlehrer, D. & Kowalczyk, M. Meccanica vol. 38 505–518 (2003) -- [10.1023/A:1024719028273](https://doi.org/10.1023/A:1024719028273)
- Descombes, S. Convergence of a splitting method of high order for reaction-diffusion systems. Mathematics of Computation vol. 70 1481–1501 (2000) -- [10.1090/S0025-5718-00-01277-1](https://doi.org/10.1090/S0025-5718-00-01277-1)
- Descombes, S. & Massot, M. Operator splitting for nonlinear reaction-diffusion systems with an entropic structure : singular perturbation and order reduction. Numerische Mathematik vol. 97 667–698 (2004) -- [10.1007/s00211-003-0496-3](https://doi.org/10.1007/s00211-003-0496-3)
- Desvillettes, L. & Fellner, K. Exponential decay toward equilibrium via entropy methods for reaction–diffusion equations. Journal of Mathematical Analysis and Applications vol. 319 157–176 (2006) -- [10.1016/j.jmaa.2005.07.003](https://doi.org/10.1016/j.jmaa.2005.07.003)
- Desvillettes, L., Fellner, K. & Tang, B. Q. Trend to Equilibrium for Reaction-Diffusion Systems Arising from Complex Balanced Chemical Reaction Networks. SIAM Journal on Mathematical Analysis vol. 49 2666–2709 (2017) -- [10.1137/16M1073935](https://doi.org/10.1137/16M1073935)
- Diegel, A. E., Wang, C., Wang, X. & Wise, S. M. Convergence analysis and error estimates for a second order accurate finite element method for the Cahn–Hilliard–Navier–Stokes system. Numerische Mathematik vol. 137 495–534 (2017) -- [10.1007/s00211-017-0887-5](https://doi.org/10.1007/s00211-017-0887-5)
- Diegel, A. E., Wang, C. & Wise, S. M. Stability and convergence of a second-order mixed finite element method for the Cahn–Hilliard equation. IMA Journal of Numerical Analysis vol. 36 1867–1897 (2015) -- [10.1093/imanum/drv065](https://doi.org/10.1093/imanum/drv065)
- Dong, L., Wang, C., Zhang, H. & Zhang, Z. A positivity-preserving, energy stable and convergent numerical scheme for the Cahn–Hilliard equation with a Flory–Huggins–Degennes energy. Communications in Mathematical Sciences vol. 17 921–939 (2019) -- [10.4310/CMS.2019.v17.n4.a3](https://doi.org/10.4310/CMS.2019.v17.n4.a3)
- Lixiu Dong, L. D., Cheng Wang, C. W., Hui Zhang, H. Z. & Zhengru Zhang, Z. Z. A Positivity-Preserving Second-Order BDF Scheme for the Cahn-Hilliard Equation with Variable Interfacial Parameters. Communications in Computational Physics vol. 28 967–998 (2020) -- [10.4208/cicp.OA-2019-0037](https://doi.org/10.4208/cicp.OA-2019-0037)
- Ederer, M. & Gilles, E. D. Thermodynamically Feasible Kinetic Models of Reaction Networks. Biophysical Journal vol. 92 1846–1857 (2007) -- [10.1529/biophysj.106.094094](https://doi.org/10.1529/biophysj.106.094094)
- Einkemmer, L. & Ostermann, A. An almost symmetric Strang splitting scheme for nonlinear evolution equations. Computers &amp; Mathematics with Applications vol. 67 2144–2157 (2014) -- [10.1016/j.camwa.2014.02.027](https://doi.org/10.1016/j.camwa.2014.02.027)
- Einkemmer, L. & Ostermann, A. Convergence Analysis of Strang Splitting for Vlasov-Type Equations. SIAM Journal on Numerical Analysis vol. 52 140–155 (2014) -- [10.1137/130918599](https://doi.org/10.1137/130918599)
- Eisenberg, B., Hyon, Y. & Liu, C. Energy variational analysis of ions in water and channels: Field theory for primitive models of complex ionic fluids. The Journal of Chemical Physics vol. 133 (2010) -- [10.1063/1.3476262](https://doi.org/10.1063/1.3476262)
- Ericksen, J. L. Introduction to the Thermodynamics of Solids. Applied Mathematical Sciences (Springer New York, 1998). doi:10.1007/978-1-4612-1614-8 -- [10.1007/978-1-4612-1614-8](https://doi.org/10.1007/978-1-4612-1614-8)
- Formaggia, L. & Scotti, A. Positivity and Conservation Properties of Some Integration Schemes for Mass Action Kinetics. SIAM Journal on Numerical Analysis vol. 49 1267–1288 (2011) -- [10.1137/100789592](https://doi.org/10.1137/100789592)
- Ge, H. & Qian, H. Mathematical Formalism of Nonequilibrium Thermodynamics for Nonlinear Chemical Reaction Systems with General Rate Law. Journal of Statistical Physics vol. 166 190–209 (2016) -- [10.1007/s10955-016-1678-6](https://doi.org/10.1007/s10955-016-1678-6)
- Glitzky, A. & Mielke, A. A gradient structure for systems coupling reaction–diffusion effects in bulk and interfaces. Zeitschrift für angewandte Mathematik und Physik vol. 64 29–52 (2012) -- [10.1007/s00033-012-0207-y](https://doi.org/10.1007/s00033-012-0207-y)
- Gorban, A. N., Mirkes, E. M. & Yablonsky, G. S. Thermodynamics in the limit of irreversible reactions. Physica A: Statistical Mechanics and its Applications vol. 392 1318–1335 (2013) -- [10.1016/j.physa.2012.10.009](https://doi.org/10.1016/j.physa.2012.10.009)
- Gu, Y. & Shen, J. Bound preserving and energy dissipative schemes for porous medium equation. Journal of Computational Physics vol. 410 109378 (2020) -- [10.1016/j.jcp.2020.109378](https://doi.org/10.1016/j.jcp.2020.109378)
- Guan, Z., Heinonen, V., Lowengrub, J., Wang, C. & Wise, S. M. An energy stable, hexagonal finite difference scheme for the 2D phase field crystal amplitude equations. Journal of Computational Physics vol. 321 1026–1054 (2016) -- [10.1016/j.jcp.2016.06.007](https://doi.org/10.1016/j.jcp.2016.06.007)
- Guan, Z., Lowengrub, J. S., Wang, C. & Wise, S. M. Second order convex splitting schemes for periodic nonlocal Cahn–Hilliard and Allen–Cahn equations. Journal of Computational Physics vol. 277 48–71 (2014) -- [10.1016/j.jcp.2014.08.001](https://doi.org/10.1016/j.jcp.2014.08.001)
- Guan, Z., Wang, C. & Wise, S. M. A convergent convex splitting scheme for the periodic nonlocal Cahn-Hilliard equation. Numerische Mathematik vol. 128 377–406 (2014) -- [10.1007/s00211-014-0608-2](https://doi.org/10.1007/s00211-014-0608-2)
- Guo, J., Wang, C., Wise, S. M. & Yue, X. An $H^2$ convergence of a second-order convex-splitting, finite difference scheme for the three-dimensional Cahn–Hilliard equation. Communications in Mathematical Sciences vol. 14 489–515 (2016) -- [10.4310/CMS.2016.v14.n2.a8](https://doi.org/10.4310/CMS.2016.v14.n2.a8)
- Hao, W. & Xue, C. Spatial pattern formation in reaction–diffusion models: a computational approach. Journal of Mathematical Biology vol. 80 521–543 (2020) -- [10.1007/s00285-019-01462-0](https://doi.org/10.1007/s00285-019-01462-0)
- Haskovec, J., Hittmeir, S., Markowich, P. & Mielke, A. Decay to Equilibrium for Energy-Reaction-Diffusion Systems. SIAM Journal on Mathematical Analysis vol. 50 1037–1075 (2018) -- [10.1137/16M1062065](https://doi.org/10.1137/16M1062065)
- Hawkins‐Daarud, A., van der Zee, K. G. & Tinsley Oden, J. Numerical simulation of a thermodynamically consistent four‐species tumor growth model. International Journal for Numerical Methods in Biomedical Engineering vol. 28 3–24 (2011) -- [10.1002/cnm.1467](https://doi.org/10.1002/cnm.1467)
- Hu, Z., Wise, S. M., Wang, C. & Lowengrub, J. S. Stable and efficient finite-difference nonlinear-multigrid schemes for the phase field crystal equation. Journal of Computational Physics vol. 228 5323–5339 (2009) -- [10.1016/j.jcp.2009.04.020](https://doi.org/10.1016/j.jcp.2009.04.020)
- Huang, J. & Shu, C.-W. Positivity-Preserving Time Discretizations for Production–Destruction Equations with Applications to Non-equilibrium Flows. Journal of Scientific Computing vol. 78 1811–1839 (2018) -- [10.1007/s10915-018-0852-1](https://doi.org/10.1007/s10915-018-0852-1)
- Jülicher, F., Ajdari, A. & Prost, J. Modeling molecular motors. Reviews of Modern Physics vol. 69 1269–1282 (1997) -- [10.1103/RevModPhys.69.1269](https://doi.org/10.1103/RevModPhys.69.1269)
- Junge, O., Matthes, D. & Osberger, H. A Fully Discrete Variational Scheme for Solving Nonlinear Fokker--Planck Equations in Multiple Space Dimensions. SIAM Journal on Numerical Analysis vol. 55 419–443 (2017) -- [10.1137/16M1056560](https://doi.org/10.1137/16M1056560)
- Koleva, M. N. & Vulkov, L. G. Operator splitting kernel based numerical method for a generalized Leland’s model. Journal of Computational and Applied Mathematics vol. 275 294–303 (2015) -- [10.1016/j.cam.2014.07.019](https://doi.org/10.1016/j.cam.2014.07.019)
- Kondo, S. & Miura, T. Reaction-Diffusion Model as a Framework for Understanding Biological Pattern Formation. Science vol. 329 1616–1620 (2010) -- [10.1126/science.1179047](https://doi.org/10.1126/science.1179047)
- Lee, H. G. & Lee, J.-Y. A second order operator splitting method for Allen–Cahn type equations with nonlinear source terms. Physica A: Statistical Mechanics and its Applications vol. 432 24–34 (2015) -- [10.1016/j.physa.2015.03.012](https://doi.org/10.1016/j.physa.2015.03.012)
- Li, X., Qiao, Z. & Zhang, H. Convergence of a Fast Explicit Operator Splitting Method for the Epitaxial Growth Model with Slope Selection. SIAM Journal on Numerical Analysis vol. 55 265–285 (2017) -- [10.1137/15M1041122](https://doi.org/10.1137/15M1041122)
- Liu, C., Wang, C., Wise, S., Yue, X. & Zhou, S. A positivity-preserving, energy stable and convergent numerical scheme for the Poisson-Nernst-Planck system. Mathematics of Computation vol. 90 2071–2106 (2021) -- [10.1090/mcom/3642](https://doi.org/10.1090/mcom/3642)
- Liu, C. & Wang, Y. On Lagrangian schemes for porous medium type generalized diffusion equations: A discrete energetic variational approach. Journal of Computational Physics vol. 417 109566 (2020) -- [10.1016/j.jcp.2020.109566](https://doi.org/10.1016/j.jcp.2020.109566)
- Liu, C. & Wu, H. An Energetic Variational Approach for the Cahn–Hilliard Equation with Dynamic Boundary Condition: Model Derivation and Mathematical Analysis. Archive for Rational Mechanics and Analysis vol. 233 167–247 (2019) -- [10.1007/s00205-019-01356-x](https://doi.org/10.1007/s00205-019-01356-x)
- Liu, J.-G., Tang, M., Wang, L. & Zhou, Z. An accurate front capturing scheme for tumor growth models with a free boundary limit. Journal of Computational Physics vol. 364 73–94 (2018) -- [10.1016/j.jcp.2018.03.013](https://doi.org/10.1016/j.jcp.2018.03.013)
- Liu, Y., Chen, W., Wang, C. & Wise, S. M. Error analysis of a mixed finite element method for a Cahn–Hilliard–Hele–Shaw system. Numerische Mathematik vol. 135 679–709 (2016) -- [10.1007/s00211-016-0813-2](https://doi.org/10.1007/s00211-016-0813-2)
- Lo, W.-C., Chen, L., Wang, M. & Nie, Q. A robust and efficient method for steady state patterns in reaction–diffusion systems. Journal of Computational Physics vol. 231 5062–5077 (2012) -- [10.1016/j.jcp.2012.04.006](https://doi.org/10.1016/j.jcp.2012.04.006)
- Lubich, C. On splitting methods for Schrödinger-Poisson and cubic nonlinear Schrödinger equations. Mathematics of Computation vol. 77 2141–2153 (2008) -- [10.1090/S0025-5718-08-02101-7](https://doi.org/10.1090/S0025-5718-08-02101-7)
- Mielke, A. A gradient structure for reaction–diffusion systems and for energy-drift-diffusion systems. Nonlinearity vol. 24 1329–1346 (2011) -- [10.1088/0951-7715/24/4/016](https://doi.org/10.1088/0951-7715/24/4/016)
- Mielke, A., Patterson, R. I. A., Peletier, M. A. & Michiel Renger, D. R. Non-equilibrium Thermodynamical Principles for Chemical Reactions with Mass-Action Kinetics. SIAM Journal on Applied Mathematics vol. 77 1562–1585 (2017) -- [10.1137/16M1102240](https://doi.org/10.1137/16M1102240)
- Nie, Q., Zhang, Y.-T. & Zhao, R. Efficient semi-implicit schemes for stiff systems. Journal of Computational Physics vol. 214 521–537 (2006) -- [10.1016/j.jcp.2005.09.030](https://doi.org/10.1016/j.jcp.2005.09.030)
- Onsager, L. Reciprocal Relations in Irreversible Processes. I. Physical Review vol. 37 405–426 (1931) -- [10.1103/PhysRev.37.405](https://doi.org/10.1103/PhysRev.37.405)
- Onsager, L. Reciprocal Relations in Irreversible Processes. II. Physical Review vol. 38 2265–2279 (1931) -- [10.1103/PhysRev.38.2265](https://doi.org/10.1103/PhysRev.38.2265)
- Oster, G. F. & Perelson, A. S. Chemical reaction dynamics. Archive for Rational Mechanics and Analysis vol. 55 230–274 (1974) -- [10.1007/BF00281751](https://doi.org/10.1007/BF00281751)
- Pearson, J. E. Complex Patterns in a Simple System. Science vol. 261 189–192 (1993) -- [10.1126/science.261.5118.189](https://doi.org/10.1126/science.261.5118.189)
- Peller, L. & Alberty, R. A. Multiple Intermediates in Steady State Enzyme Kinetics.1,2 I. The Mechanism Involving a Single Substrate and Product. Journal of the American Chemical Society vol. 81 5907–5914 (1959) -- [10.1021/ja01531a017](https://doi.org/10.1021/ja01531a017)
- Perthame, B., Quirós, F. & Vázquez, J. L. The Hele–Shaw Asymptotics for Mechanical Models of Tumor Growth. Archive for Rational Mechanics and Analysis vol. 212 93–127 (2014) -- [10.1007/s00205-013-0704-y](https://doi.org/10.1007/s00205-013-0704-y)
- Rayleigh, Lord. Note on the Numerical Calculation of the Roots of Fluctuating Functions. Proceedings of the London Mathematical Society vols s1-5 119–124 (1873) -- [10.1112/plms/s1-5.1.119](https://doi.org/10.1112/plms/s1-5.1.119)
- Sandu, A. Positive Numerical Integration Methods for Chemical Kinetic Systems. Journal of Computational Physics vol. 170 589–602 (2001) -- [10.1006/jcph.2001.6750](https://doi.org/10.1006/jcph.2001.6750)
- Shear, D. An analog of the Boltzmann H-theorem (a Liapunov function) for systems of coupled chemical reactions. Journal of Theoretical Biology vol. 16 212–228 (1967) -- [10.1016/0022-5193(67)90005-7](https://doi.org/10.1016/0022-5193(67)90005-7)
- Shen, J., Wang, C., Wang, X. & Wise, S. M. Second-order Convex Splitting Schemes for Gradient Flows with Ehrlich–Schwoebel Type Energy: Application to Thin Film Epitaxy. SIAM Journal on Numerical Analysis vol. 50 105–125 (2012) -- [10.1137/110822839](https://doi.org/10.1137/110822839)
- Shen, J. & Wang, Z.-Q. Error Analysis of the Strang Time-Splitting Laguerre–Hermite/Hermite Collocation Methods for the Gross–Pitaevskii Equation. Foundations of Computational Mathematics vol. 13 99–137 (2012) -- [10.1007/s10208-012-9124-x](https://doi.org/10.1007/s10208-012-9124-x)
- Shen, J., Xu, J. & Yang, J. A New Class of Efficient and Robust Energy Stable Schemes for Gradient Flows. SIAM Review vol. 61 474–506 (2019) -- [10.1137/17M1150153](https://doi.org/10.1137/17M1150153)
- Thalhammer, M. Convergence Analysis of High-Order Time-Splitting Pseudospectral Methods for Nonlinear Schrödinger Equations. SIAM Journal on Numerical Analysis vol. 50 3231–3258 (2012) -- [10.1137/120866373](https://doi.org/10.1137/120866373)
- Wang, C. et al. Unconditionally stable schemes for equations of thin film epitaxy. Discrete &amp; Continuous Dynamical Systems - A vol. 28 405–423 (2010) -- [10.3934/dcds.2010.28.405](https://doi.org/10.3934/dcds.2010.28.405)
- Wise, S. M., Wang, C. & Lowengrub, J. S. An Energy-Stable and Convergent Finite-Difference Scheme for the Phase Field Crystal Equation. SIAM Journal on Numerical Analysis vol. 47 2269–2288 (2009) -- [10.1137/080738143](https://doi.org/10.1137/080738143)
- A Second-Order Energy Stable BDF Numerical Scheme for the Cahn-Hilliard Equation. Communications in Computational Physics vol. 23 572–602 (2018) -- [10.4208/cicp.OA-2016-0197](https://doi.org/10.4208/cicp.OA-2016-0197)
- Zhang, C., Huang, J., Wang, C. & Yue, X. On the Operator Splitting and Integral Equation Preconditioned Deferred Correction Methods for the “Good” Boussinesq Equation. Journal of Scientific Computing vol. 75 687–712 (2017) -- [10.1007/s10915-017-0552-2](https://doi.org/10.1007/s10915-017-0552-2)
- Zhang, C., Wang, H., Huang, J., Wang, C. & Yue, X. A second order operator splitting numerical scheme for the “good” Boussinesq equation. Applied Numerical Mathematics vol. 119 179–193 (2017) -- [10.1016/j.apnum.2017.04.006](https://doi.org/10.1016/j.apnum.2017.04.006)
- Zhao, J., Yang, X., Shen, J. & Wang, Q. A decoupled energy stable scheme for a hydrodynamic phase-field model of mixtures of nematic liquid crystals and viscous fluids. Journal of Computational Physics vol. 305 539–556 (2016) -- [10.1016/j.jcp.2015.09.044](https://doi.org/10.1016/j.jcp.2015.09.044)
- Zhao, S. Operator splitting ADI schemes for pseudo-time coupled nonlinear solvation simulations. Journal of Computational Physics vol. 257 1000–1021 (2014) -- [10.1016/j.jcp.2013.09.043](https://doi.org/10.1016/j.jcp.2013.09.043)
- Zhao, S., Ovadia, J., Liu, X., Zhang, Y.-T. & Nie, Q. Operator splitting implicit integration factor methods for stiff reaction–diffusion–advection systems. Journal of Computational Physics vol. 230 5996–6009 (2011) -- [10.1016/j.jcp.2011.04.009](https://doi.org/10.1016/j.jcp.2011.04.009)

