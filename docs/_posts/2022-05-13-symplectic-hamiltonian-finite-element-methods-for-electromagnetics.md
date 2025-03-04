---
layout: post
title: "Symplectic Hamiltonian finite element methods for electromagnetics"
date: 2022-05-13 00:00:00 +0100
permalink: symplectic-hamiltonian-finite-element-methods-for-electromagnetics
year: 2022
authors: Manuel A. Sánchez, Shukai Du, Bernardo Cockburn, Ngoc-Cuong Nguyen, Jaime Peraire
category: journal-article
tag: Time-dependent Maxwell’s equations; Symplectic Hamiltonian finite element methods; Mixed methods; Discontinuous Galerkin methods; Hybridizable discontinuous Galerkin methods
---
 
## Authors
[Manuel A. Sánchez](authors/manuel-a-sanchez), [Shukai Du](authors/shukai-du), [Bernardo Cockburn](authors/bernardo-cockburn), [Ngoc-Cuong Nguyen](authors/ngoc-cuong-nguyen), [Jaime Peraire](authors/jaime-peraire)
 
## Abstract
We present several high-order accurate finite element methods for the Maxwell’s equations which provide time-invariant, non-drifting approximations to the total electric and magnetic charges, and to the total energy. We devise these methods by taking advantage of the Hamiltonian structures of the Maxwell’s equations as follows. First, we introduce spatial discretizations of the Maxwell’s equations using mixed finite element, discontinuous Galerkin, and hybridizable discontinuous Galerkin methods to obtain a semi-discrete system of equations which display discrete versions of the Hamiltonian structure of the Maxwell’s equations. Then we discretize the resulting semi-discrete system in time by using a symplectic integrator. This ensures the conservation properties of the fully discrete system of equations. For the Symplectic Hamiltonian HDG method, we present numerical experiments which confirm its optimal orders of convergence for all variables and its conservation properties for the total linear and angular momenta, as well as the total energy. Finally, we discuss the extension of our results to other boundary conditions and to numerical schemes defined by different weak formulations.
 
## Keywords
Time-dependent Maxwell’s equations; Symplectic Hamiltonian finite element methods; Mixed methods; Discontinuous Galerkin methods; Hybridizable discontinuous Galerkin methods
 
## Citation
- **Journal:** Computer Methods in Applied Mechanics and Engineering
- **Year:** 2022
- **Volume:** 396
- **Issue:** 
- **Pages:** 114969
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.cma.2022.114969](https://doi.org/10.1016/j.cma.2022.114969)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{S_nchez_2022,
  title={{Symplectic Hamiltonian finite element methods for electromagnetics}},
  volume={396},
  ISSN={0045-7825},
  DOI={10.1016/j.cma.2022.114969},
  journal={Computer Methods in Applied Mechanics and Engineering},
  publisher={Elsevier BV},
  author={Sánchez, Manuel A. and Du, Shukai and Cockburn, Bernardo and Nguyen, Ngoc-Cuong and Peraire, Jaime},
  year={2022},
  pages={114969}
}
{% endraw %}
{% endhighlight %}
 
## References
- [Sánchez, M. A., Ciuca, C., Nguyen, N. C., Peraire, J. & Cockburn, B. Symplectic Hamiltonian HDG methods for wave propagation phenomena. Journal of Computational Physics vol. 350 951–973 (2017)](symplectic-hamiltonian-hdg-methods-for-wave-propagation-phenomena) -- [10.1016/j.jcp.2017.09.010](https://doi.org/10.1016/j.jcp.2017.09.010)
- Sánchez, M. A., Cockburn, B., Nguyen, N.-C. & Peraire, J. Symplectic Hamiltonian finite element methods for linear elastodynamics. Computer Methods in Applied Mechanics and Engineering vol. 381 113843 (2021) -- [10.1016/j.cma.2021.113843](https://doi.org/10.1016/j.cma.2021.113843)
- Tang, Y. & Cohen, A. E. Optical Chirality and Its Interaction with Matter. Physical Review Letters vol. 104 (2010) -- [10.1103/PhysRevLett.104.163901](https://doi.org/10.1103/PhysRevLett.104.163901)
- ANDERSON, N. & ARTHURS, A. M. Helicity and variational principles for Maxwell’s equations. International Journal of Electronics vol. 54 861–864 (1983) -- [10.1080/00207218308938781](https://doi.org/10.1080/00207218308938781)
- Cameron, R. P., Barnett, S. M. & Yao, A. M. Optical helicity, optical spin and related quantities in electromagnetic theory. New Journal of Physics vol. 14 053050 (2012) -- [10.1088/1367-2630/14/5/053050](https://doi.org/10.1088/1367-2630/14/5/053050)
- Lipkin, D. M. Existence of a New Conservation Law in Electromagnetic Theory. Journal of Mathematical Physics vol. 5 696–700 (1964) -- [10.1063/1.1704165](https://doi.org/10.1063/1.1704165)
- Falk, R. S. & Richter, G. R. Explicit Finite Element Methods for Symmetric Hyperbolic Equations. SIAM Journal on Numerical Analysis vol. 36 935–952 (1999) -- [10.1137/S0036142997329463](https://doi.org/10.1137/S0036142997329463)
- Hesthaven, J. S. & Warburton, T. Nodal High-Order Methods on Unstructured Grids. Journal of Computational Physics vol. 181 186–221 (2002) -- [10.1006/jcph.2002.7118](https://doi.org/10.1006/jcph.2002.7118)
- Cockburn, B., Li, F. & Shu, C.-W. Locally divergence-free discontinuous Galerkin methods for the Maxwell equations. Journal of Computational Physics vol. 194 588–610 (2004) -- [10.1016/j.jcp.2003.09.007](https://doi.org/10.1016/j.jcp.2003.09.007)
- Hesthaven, J. S. & Warburton, T. High–order nodal discontinuous Galerkin methods for the Maxwell eigenvalue problem. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 362 493–524 (2004) -- [10.1098/rsta.2003.1332](https://doi.org/10.1098/rsta.2003.1332)
- Chen, M.-H., Cockburn, B. & Reitich, F. High-order RKDG Methods for Computational Electromagnetics. Journal of Scientific Computing vols 22–23 205–226 (2005) -- [10.1007/s10915-004-4152-6](https://doi.org/10.1007/s10915-004-4152-6)
- Kane Yee. Numerical solution of initial boundary value problems involving maxwell’s equations in isotropic media. IEEE Transactions on Antennas and Propagation vol. 14 302–307 (1966) -- [10.1109/TAP.1966.1138693](https://doi.org/10.1109/TAP.1966.1138693)
- Chen, W., Li, X. & Liang, D. Energy-Conserved Splitting Finite-Difference Time-Domain Methods for Maxwell’s Equations in Three Dimensions. SIAM Journal on Numerical Analysis vol. 48 1530–1554 (2010) -- [10.1137/090765857](https://doi.org/10.1137/090765857)
- McLachlan, R. Symplectic integration of Hamiltonian wave equations. Numerische Mathematik vol. 66 465–492 (1993) -- [10.1007/BF01385708](https://doi.org/10.1007/BF01385708)
- Bridges, T. J. & Reich, S. Numerical methods for Hamiltonian PDEs. Journal of Physics A: Mathematical and General vol. 39 5287–5320 (2006) -- [10.1088/0305-4470/39/19/S02](https://doi.org/10.1088/0305-4470/39/19/S02)
- Hirono, T., Wayne Lui, Seki, S. & Yoshikuni, Y. A three-dimensional fourth-order finite-difference time-domain scheme using a symplectic integrator propagator. IEEE Transactions on Microwave Theory and Techniques vol. 49 1640–1648 (2001) -- [10.1109/22.942578](https://doi.org/10.1109/22.942578)
- Sun, Y. & Tse, P. S. P. Symplectic and multisymplectic numerical methods for Maxwell’s equations. Journal of Computational Physics vol. 230 2076–2094 (2011) -- [10.1016/j.jcp.2010.12.006](https://doi.org/10.1016/j.jcp.2010.12.006)
- Fu, G. & Shu, C.-W. Optimal energy-conserving discontinuous Galerkin methods for linear symmetric hyperbolic systems. Journal of Computational Physics vol. 394 329–363 (2019) -- [10.1016/j.jcp.2019.05.050](https://doi.org/10.1016/j.jcp.2019.05.050)
- Cockburn, B. & Shu, C.-W. The Runge–Kutta Discontinuous Galerkin Method for Conservation Laws V. Journal of Computational Physics vol. 141 199–224 (1998) -- [10.1006/jcph.1998.5892](https://doi.org/10.1006/jcph.1998.5892)
- Cockburn, B. & Shu, C.-W. Journal of Scientific Computing vol. 16 173–261 (2001) -- [10.1023/A:1012873910884](https://doi.org/10.1023/A:1012873910884)
- [Xu, Y., van der Vegt, J. J. W. & Bokhove, O. Discontinuous Hamiltonian Finite Element Method for Linear Hyperbolic Systems. Journal of Scientific Computing vol. 35 241–265 (2008)](discontinuous-hamiltonian-finite-element-method-for-linear-hyperbolic-systems) -- [10.1007/s10915-008-9191-y](https://doi.org/10.1007/s10915-008-9191-y)
- Nedelec, J. C. Mixed finite elements in ?3. Numerische Mathematik vol. 35 315–341 (1980) -- [10.1007/BF01396415](https://doi.org/10.1007/BF01396415)
- Monk, P. B. A Mixed Method for Approximating Maxwell’s Equations. SIAM Journal on Numerical Analysis vol. 28 1610–1634 (1991) -- [10.1137/0728081](https://doi.org/10.1137/0728081)
- Chen, H., Qiu, W., Shi, K. & Solano, M. A Superconvergent HDG Method for the Maxwell Equations. Journal of Scientific Computing vol. 70 1010–1029 (2016) -- [10.1007/s10915-016-0272-z](https://doi.org/10.1007/s10915-016-0272-z)
- Du, S. & Sayas, F.-J. A Unified Error Analysis of Hybridizable Discontinuous Galerkin Methods for the Static Maxwell Equations. SIAM Journal on Numerical Analysis vol. 58 1367–1391 (2020) -- [10.1137/19M1290966](https://doi.org/10.1137/19M1290966)
- Cockburn, B. & Fu, G. A Systematic Construction of Finite Element Commuting Exact Sequences. SIAM Journal on Numerical Analysis vol. 55 1650–1688 (2017) -- [10.1137/16M1073352](https://doi.org/10.1137/16M1073352)
- N�d�lec, J. C. A new family of mixed finite elements in ?3. Numerische Mathematik vol. 50 57–81 (1986) -- [10.1007/BF01389668](https://doi.org/10.1007/BF01389668)
- Sanz-Serna, J. M. Symplectic Runge-Kutta and related methods: recent results. Physica D: Nonlinear Phenomena vol. 60 293–302 (1992) -- [10.1016/0167-2789(92)90245-I](https://doi.org/10.1016/0167-2789(92)90245-I)
- Schöberl, J. NETGEN An advancing front 2D/3D-mesh generator based on abstract rules. Computing and Visualization in Science vol. 1 41–52 (1997) -- [10.1007/s007910050004](https://doi.org/10.1007/s007910050004)
- Makridakis, Ch. G. & Monk, P. Time-discrete finite element schemes for Maxwell’s equations. ESAIM: Mathematical Modelling and Numerical Analysis vol. 29 171–197 (1995) -- [10.1051/m2an/1995290201711](https://doi.org/10.1051/m2an/1995290201711)
- Ruth, R. D. A Can0nical Integrati0n Technique. IEEE Transactions on Nuclear Science vol. 30 2669–2671 (1983) -- [10.1109/TNS.1983.4332919](https://doi.org/10.1109/TNS.1983.4332919)
- McLachlan, R. I. & Atela, P. The accuracy of symplectic integrators. Nonlinearity vol. 5 541–562 (1992) -- [10.1088/0951-7715/5/2/011](https://doi.org/10.1088/0951-7715/5/2/011)

