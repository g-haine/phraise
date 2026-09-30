---
title: "A Novel Structure-Preserving Scheme for Three-Dimensional Maxwell’s Equations"
date: 2024-09-30 00:00:00 +0100
permalink: a-novel-structure-preserving-scheme-for-three-dimensional-maxwell-s-equations
year: 2024
authors: Chaolong Jiang, Wenjun Cai, Yushun Wang, Haochen Li
category: articles
---
 
## Authors
[Chaolong Jiang](authors/chaolong-jiang), [Wenjun Cai](authors/wenjun-cai), [Yushun Wang](authors/yushun-wang), [Haochen Li](authors/haochen-li)
 
## Abstract
In this paper, a novel structure-preserving scheme is proposed for solving the three-dimensional Maxwell’s equations. The proposed scheme can preserve all of the desired structures of the Maxwell’s equations numerically, including five energy conservation laws, two divergence-free fields, three momentum conservation laws and a symplectic conservation law. Firstly, the spatial derivatives of the Maxwell’s equations are approximated with Fourier pseudo-spectral methods. The resulting ordinary differential equations are cast into a canonical Hamiltonian system. Then, the fully discrete structure-preserving scheme is derived by integrating the Hamiltonian system using a sixth order average vector field method. Subsequently, an optimal error estimate is established based on the energy method, which demonstrates that the proposed scheme is of sixth order accuracy in time and spectral accuracy in space in the discrete \\( L^2 \\)-norm. The constant in the error estimate is proved to be only \\( \mathcal{O}(T), \\) where \\( T > 0 \\) is the time period. Furthermore, its numerical dispersion relation is analyzed in detail, and a customized fast solver is presented to efficiently solve the resulting discrete linear equations. Finally, numerical results are presented to validate our theoretical analysis.
 
## Citation
- **Journal:** CSIAM Transactions on Applied Mathematics
- **Year:** 2024
- **Volume:** 5
- **Issue:** 4
- **Pages:** 788--834
- **Publisher:** Global Science Press
- **DOI:** [10.4208/csiam-am.so-2023-0047](https://doi.org/10.4208/csiam-am.so-2023-0047)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Chaolong_Jiang_2024,
  title={{A Novel Structure-Preserving Scheme for Three-Dimensional Maxwell’s Equations}},
  volume={5},
  ISSN={2708-0560},
  DOI={10.4208/csiam-am.so-2023-0047},
  number={4},
  journal={CSIAM Transactions on Applied Mathematics},
  publisher={Global Science Press},
  author={Chaolong Jiang, Chaolong Jiang and Wenjun Cai, Wenjun Cai and Yushun Wang, Yushun Wang and Haochen Li, Haochen Li},
  year={2024},
  pages={788--834}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-novel-structure-preserving-scheme-for-three-dimensional-maxwell-s-equations.bib)
 
## References
- Ascher UM, McLachlan RI (2004) Multisymplectic box schemes and the Korteweg–de Vries equation. Applied Numerical Mathematics 48(3-4):255–269. https://doi.org/10.1016/j.apnum.2003.09.002 -- [10.1016/j.apnum.2003.09.002](https://doi.org/10.1016/j.apnum.2003.09.002)
- Cai J, Hong J, Wang Y, Gong Y (2015) Two Energy-Conserved Splitting Methods for Three-Dimensional Time-Domain Maxwell's Equations and the Convergence Analysis. SIAM J Numer Anal 53(4):1918–1940. https://doi.org/10.1137/140971609 -- [10.1137/140971609](https://doi.org/10.1137/140971609)
- Cai J, Wang Y, Gong Y (2015) Numerical Analysis of AVF Methods for Three-Dimensional Time-Domain Maxwell’s Equations. J Sci Comput 66(1):141–176. https://doi.org/10.1007/s10915-015-0016-5 -- [10.1007/s10915-015-0016-5](https://doi.org/10.1007/s10915-015-0016-5)
- Cai W, Wang Y, Song Y (2013) Numerical dispersion analysis of a multi-symplectic scheme for the three dimensional Maxwell’s equations. Journal of Computational Physics 234:330–352. https://doi.org/10.1016/j.jcp.2012.09.043 -- [10.1016/j.jcp.2012.09.043](https://doi.org/10.1016/j.jcp.2012.09.043)
- Canuto C, Quarteroni A (1982) Approximation results for orthogonal polynomials in Sobolev spaces. Math Comp 38(157):67–86. https://doi.org/10.1090/s0025-5718-1982-0637287-3 -- [10.1090/s0025-5718-1982-0637287-3](https://doi.org/10.1090/s0025-5718-1982-0637287-3)
- Celledoni E, Grimm V, McLachlan RI, McLaren DI, O’Neale D, Owren B, Quispel GRW (2012) Preserving energy resp. dissipation in numerical PDEs using the “Average Vector Field” method. Journal of Computational Physics 231(20):6770–6789. https://doi.org/10.1016/j.jcp.2012.06.022 -- [10.1016/j.jcp.2012.06.022](https://doi.org/10.1016/j.jcp.2012.06.022)
- Celledoni E, McLachlan RI, Owren B, Quispel GRW (2010) Energy-Preserving Integrators and the Structure of B-series. Found Comput Math 10(6):673–693. https://doi.org/10.1007/s10208-010-9073-1 -- [10.1007/s10208-010-9073-1](https://doi.org/10.1007/s10208-010-9073-1)
- [8] P. Chartier, E. Hairer, and G. Vilmart, A substitution law for B-series vector fields, Research Report RR-5498, INRIA, 2005.
- [9] J. Chen and M. Qin, Multi-symplectic Fourier pseudospectral method for the nonlinear Schrödinger equation, Electron. Trans. Numer. Anal., 12:193–204, 2001.
- Chen W, Li X, Liang D (2007) Energy-conserved splitting FDTD methods for Maxwell’s equations. Numer Math 108(3):445–485. https://doi.org/10.1007/s00211-007-0123-9 -- [10.1007/s00211-007-0123-9](https://doi.org/10.1007/s00211-007-0123-9)
- Chen W, Li X, Liang D (2010) Energy-Conserved Splitting Finite-Difference Time-Domain Methods for Maxwell's Equations in Three Dimensions. SIAM J Numer Anal 48(4):1530–1554. https://doi.org/10.1137/090765857 -- [10.1137/090765857](https://doi.org/10.1137/090765857)
- Dahlby M, Owren B (2011) A General Framework for Deriving Integral Preserving Numerical Methods for PDEs. SIAM J Sci Comput 33(5):2318–2340. https://doi.org/10.1137/100810174 -- [10.1137/100810174](https://doi.org/10.1137/100810174)
- [13] K. Feng, Difference schemes for Hamiltonian formalism and symplectic geometry, J. Comput. Math., 4:279–289, 1986.
- Feng K, Qin M (2010) Symplectic Geometric Algorithms for Hamiltonian Systems. Springer Berlin Heidelberg, Berlin, Heidelberg -- [10.1007/978-3-642-01777-3](https://doi.org/10.1007/978-3-642-01777-3)
- Gao L, Zhang B (2013) Optimal error estimates and modified energy conservation identities of the ADI-FDTD scheme on staggered grids for 3D Maxwell’s equations. Sci China Math 56(8):1705–1726. https://doi.org/10.1007/s11425-013-4609-x -- [10.1007/s11425-013-4609-x](https://doi.org/10.1007/s11425-013-4609-x)
- [16] E. Hairer, C. Lubich, and G. Wanner, Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations, Springer-Verlag, 2006.
- Hirono T, Wayne Lui, Seki S, Yoshikuni Y (2001) A three-dimensional fourth-order finite-difference time-domain scheme using a symplectic integrator propagator. IEEE Trans Microwave Theory Techn 49(9):1640–1648. https://doi.org/10.1109/22.942578 -- [10.1109/22.942578](https://doi.org/10.1109/22.942578)
- Hong J, Ji L, Kong L (2014) Energy-dissipation splitting finite-difference time-domain method for Maxwell equations with perfectly matched layers. Journal of Computational Physics 269:201–214. https://doi.org/10.1016/j.jcp.2014.03.025 -- [10.1016/j.jcp.2014.03.025](https://doi.org/10.1016/j.jcp.2014.03.025)
- Kong L, Hong J, Zhang J (2010) Splitting multisymplectic integrators for Maxwell’s equations. Journal of Computational Physics 229(11):4259–4278. https://doi.org/10.1016/j.jcp.2010.02.010 -- [10.1016/j.jcp.2010.02.010](https://doi.org/10.1016/j.jcp.2010.02.010)
- Li H, Wang Y, Qin M (2016) A Sixth Order Averaged Vector Field Method. JCM 34(5):479–498. https://doi.org/10.4208/jcm.1601-m2015-0265 -- [10.4208/jcm.1601-m2015-0265](https://doi.org/10.4208/jcm.1601-m2015-0265)
- Liang D, Yuan Q (2013) The spatial fourth-order energy-conserved S-FDTD scheme for Maxwell’s equations. Journal of Computational Physics 243:344–364. https://doi.org/10.1016/j.jcp.2013.02.040 -- [10.1016/j.jcp.2013.02.040](https://doi.org/10.1016/j.jcp.2013.02.040)
- McLachlan RI, Quispel GRW, Robidoux N (1999) Geometric integration using discrete gradients. Philosophical Transactions of the Royal Society of London Series A: Mathematical, Physical and Engineering Sciences 357(1754):1021–1045. https://doi.org/10.1098/rsta.1999.0363 -- [10.1098/rsta.1999.0363](https://doi.org/10.1098/rsta.1999.0363)
- Monk P, Süli E (1994) A Convergence Analysis of Yee’s Scheme on Nonuniform Grids. SIAM J Numer Anal 31(2):393–412. https://doi.org/10.1137/0731021 -- [10.1137/0731021](https://doi.org/10.1137/0731021)
- Namiki T (1999) A new FDTD algorithm based on alternating-direction implicit method. IEEE Trans Microwave Theory Techn 47(10):2003–2007. https://doi.org/10.1109/22.795075 -- [10.1109/22.795075](https://doi.org/10.1109/22.795075)
- [25] M. Qin and Y. Wang, Structure-Preserving Algorithms for Partial Differential Equations, Zhejiang Science and Technology Publishing House, 2011. (in Chinese)
- Quispel GRW, McLaren DI (2008) A new class of energy-preserving numerical integration methods. J Phys A: Math Theor 41(4):045206. https://doi.org/10.1088/1751-8113/41/4/045206 -- [10.1088/1751-8113/41/4/045206](https://doi.org/10.1088/1751-8113/41/4/045206)
- Sha W, Huang Z, Wu X, Chen M (2007) Application of the symplectic finite-difference time-domain scheme to electromagnetic simulation. Journal of Computational Physics 225(1):33–50. https://doi.org/10.1016/j.jcp.2006.11.027 -- [10.1016/j.jcp.2006.11.027](https://doi.org/10.1016/j.jcp.2006.11.027)
- Shen J, Tang T, Wang L-L (2011) Spectral Methods. Springer Berlin Heidelberg, Berlin, Heidelberg -- [10.1007/978-3-540-71041-7](https://doi.org/10.1007/978-3-540-71041-7)
- Sheu TWH, Chung YW, Li JH, Wang YC (2016) Development of an explicit non-staggered scheme for solving three-dimensional Maxwell’s equations. Computer Physics Communications 207:258–273. https://doi.org/10.1016/j.cpc.2016.07.017 -- [10.1016/j.cpc.2016.07.017](https://doi.org/10.1016/j.cpc.2016.07.017)
- Shibayama J, Muraki M, Yamauchi J, Nakano H (2005) Efficient implicit FDTD algorithm based on locally one-dimensional scheme. Electron Lett 41(19):1046–1047. https://doi.org/10.1049/el:20052381 -- [10.1049/el:20052381](https://doi.org/10.1049/el:20052381)
- Stern A, Tong Y, Desbrun M, Marsden JE (2015) Geometric Computational Electrodynamics with Variational Integrators and Discrete Differential Forms. In: Fields Institute Communications. Springer New York, New York, NY, pp 437–475 -- [10.1007/978-1-4939-2441-7_19](https://doi.org/10.1007/978-1-4939-2441-7_19)
- [32] H. Su, M. Qin, and R. Scherer, A multisymplectic geometry and a multisymplectic scheme for Maxwell’s equations, Int. J. Pure Appl. Math., 34:1–17, 2007.
- Sun Y, Tse PSP (2011) Symplectic and multisymplectic numerical methods for Maxwell’s equations. Journal of Computational Physics 230(5):2076–2094. https://doi.org/10.1016/j.jcp.2010.12.006 -- [10.1016/j.jcp.2010.12.006](https://doi.org/10.1016/j.jcp.2010.12.006)
- [34] A. Taflove and S. C. Hagness, Computational Electrodynamics, Artech House, 2005.
- Trefethen LN (1982) Group Velocity in Finite Difference Schemes. SIAM Rev 24(2):113–136. https://doi.org/10.1137/1024038 -- [10.1137/1024038](https://doi.org/10.1137/1024038)
- [36] G. B. Whitham, Linear and Nonlinear Waves, John Wiley & Sons Inc., 2011.
- Wu X, You X, Wang B (2013) Structure-Preserving Algorithms for Oscillatory Differential Equations. Springer Berlin Heidelberg, Berlin, Heidelberg -- [10.1007/978-3-642-35338-3](https://doi.org/10.1007/978-3-642-35338-3)
- Yang H, Zeng X, Wu X (2021) A novel class of explicit divergence-free time-domain methods for efficiently solving Maxwell's equations. Computer Physics Communications 268:108101. https://doi.org/10.1016/j.cpc.2021.108101 -- [10.1016/j.cpc.2021.108101](https://doi.org/10.1016/j.cpc.2021.108101)
- Kane Yee (1966) Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. IEEE Trans Antennas Propagat 14(3):302–307. https://doi.org/10.1109/tap.1966.1138693 -- [10.1109/tap.1966.1138693](https://doi.org/10.1109/tap.1966.1138693)
- Fenghua Zhen, Zhizhang Chen, Jiazong Zhang (2000) Toward the development of a three-dimensional unconditionally stable finite-difference time-domain method. IEEE Trans Microwave Theory Techn 48(9):1550–1558. https://doi.org/10.1109/22.869007 -- [10.1109/22.869007](https://doi.org/10.1109/22.869007)
- Zhu H, Song S, Chen Y (2011) Multi-Symplectic Wavelet Collocation Method for Maxwell's Equations. Adv Appl Math Mech 3(6):663–688. https://doi.org/10.4208/aamm.11-m1183 -- [10.4208/aamm.11-m1183](https://doi.org/10.4208/aamm.11-m1183)

