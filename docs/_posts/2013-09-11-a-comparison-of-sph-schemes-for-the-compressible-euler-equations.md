---
layout: post
title: "A comparison of SPH schemes for the compressible Euler equations"
date: 2013-09-11 00:00:00 +0100
permalink: a-comparison-of-sph-schemes-for-the-compressible-euler-equations
year: 2014
authors: Kunal Puri, Prabhu Ramachandran
category:
  - articles
tags:
  - sph
  - particle method
  - euler equations
---
 
## Authors
[Kunal Puri](authors/kunal_puri), [Prabhu Ramachandran](authors/prabhu_ramachandran)
 
## Abstract
We review the current state-of-the-art Smoothed Particle Hydrodynamics (SPH) schemes for the compressible Euler equations. We identify three prototypical schemes and apply them to a suite of test problems in one and two dimensions. The schemes are in order, standard SPH with an adaptive density kernel estimation (ADKE) technique introduced Sigalotti et al. (2008) [44], the variational SPH formulation of Price (2012) [33] (referred herein as the MPM scheme) and the Godunov type SPH (GSPH) scheme of Inutsuka (2002) [12]. The tests investigate the accuracy of the inviscid discretizations, shock capturing ability and the particle settling behavior. The schemes are found to produce nearly identical results for the 1D shock tube problems with the MPM and GSPH schemes being the most robust. The ADKE scheme requires parameter values which must be tuned to the problem at hand. We propose an addition of an artificial heating term to the GSPH scheme to eliminate unphysical spikes in the thermal energy at the contact discontinuity. The resulting modification is simple and can be readily incorporated in existing codes. In two dimensions, the differences between the schemes is more evident with the quality of results determined by the particle distribution. In particular, the ADKE scheme shows signs of particle clumping and irregular motion for the 2D strong shock and Sedov point explosion tests. The noise in particle data is linked with the particle distribution which remains regular for the Hamiltonian formulations (MPM and GSPH) and becomes irregular for the ADKE scheme. In the interest of reproducibility, we make available our implementation of the algorithms and test problems discussed in this work.
 
## Keywords
SPH; Particle method; Euler equations
 
## Citation
- **Journal:** Journal of Computational Physics
- **Year:** 2014
- **Volume:** 256
- **Issue:** 
- **Pages:** 308--333
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.jcp.2013.08.060](https://doi.org/10.1016/j.jcp.2013.08.060)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Puri_2014,
  title={{A comparison of SPH schemes for the compressible Euler equations}},
  volume={256},
  ISSN={0021-9991},
  DOI={10.1016/j.jcp.2013.08.060},
  journal={Journal of Computational Physics},
  publisher={Elsevier BV},
  author={Puri, Kunal and Ramachandran, Prabhu},
  year={2014},
  pages={308--333}
}
{% endraw %}
{% endhighlight %}
 
## References
- Agertz, O. et al. Fundamental differences between SPH and grid methods. Monthly Notices of the Royal Astronomical Society vol. 380 963–978 (2007) -- [10.1111/j.1365-2966.2007.12183.x](https://doi.org/10.1111/j.1365-2966.2007.12183.x)
- Einfeldt, B., Munz, C. D., Roe, P. L. & Sjögreen, B. On Godunov-type methods near low densities. Journal of Computational Physics vol. 92 273–295 (1991) -- [10.1016/0021-9991(91)90211-3](https://doi.org/10.1016/0021-9991(91)90211-3)
- Engquist, B. & Osher, S. Stable and entropy satisfying approximations for transonic flow calculations. Mathematics of Computation vol. 34 45–75 (1980) -- [10.1090/S0025-5718-1980-0551290-1](https://doi.org/10.1090/S0025-5718-1980-0551290-1)
- Cha, S.-H. & Whitworth, A. P. Implementations and tests of Godunov-type particle hydrodynamics. Monthly Notices of the Royal Astronomical Society vol. 340 73–90 (2003) -- [10.1046/j.1365-8711.2003.06266.x](https://doi.org/10.1046/j.1365-8711.2003.06266.x)
- Cha, S.-H., Inutsuka, S.-I. & Nayakshin, S. Kelvin-Helmholtz instabilities with Godunov smoothed particle hydrodynamics. Monthly Notices of the Royal Astronomical Society vol. 403 1165–1174 (2010) -- [10.1111/j.1365-2966.2010.16200.x](https://doi.org/10.1111/j.1365-2966.2010.16200.x)
- Chaniotis, A. K., Poulikakos, D. & Koumoutsakos, P. Remeshed Smoothed Particle Hydrodynamics for the Simulation of Viscous and Heat Conducting Flows. Journal of Computational Physics vol. 182 67–90 (2002) -- [10.1006/jcph.2002.7152](https://doi.org/10.1006/jcph.2002.7152)
- Colella, P. & Woodward, P. R. The Piecewise Parabolic Method (PPM) for gas-dynamical simulations. Journal of Computational Physics vol. 54 174–201 (1984) -- [10.1016/0021-9991(84)90143-8](https://doi.org/10.1016/0021-9991(84)90143-8)
- Balsara, D. S. von Neumann stability analysis of smoothed particle hydrodynamics—suggestions for optimal algorithms. Journal of Computational Physics vol. 121 357–372 (1995) -- [10.1016/S0021-9991(95)90221-X](https://doi.org/10.1016/S0021-9991(95)90221-X)
- Murante, G., Borgani, S., Brunino, R. & Cha, S.-H. Hydrodynamic simulations with the Godunov smoothed particle hydrodynamics. Monthly Notices of the Royal Astronomical Society vol. 417 136–153 (2011) -- [10.1111/j.1365-2966.2011.19021.x](https://doi.org/10.1111/j.1365-2966.2011.19021.x)
- Sod, G. A. A survey of several finite difference methods for systems of nonlinear hyperbolic conservation laws. Journal of Computational Physics vol. 27 1–31 (1978) -- [10.1016/0021-9991(78)90023-2](https://doi.org/10.1016/0021-9991(78)90023-2)
- Gingold, R. A. & Monaghan, J. J. Smoothed particle hydrodynamics: theory and application to non-spherical stars. Monthly Notices of the Royal Astronomical Society vol. 181 375–389 (1977) -- [10.1093/mnras/181.3.375](https://doi.org/10.1093/mnras/181.3.375)
- Inutsuka, S. Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. Journal of Computational Physics vol. 179 238–267 (2002) -- [10.1006/jcph.2002.7053](https://doi.org/10.1006/jcph.2002.7053)
- Cheng, J. & Shu, C.-W. A high order ENO conservative Lagrangian type scheme for the compressible Euler equations. Journal of Computational Physics vol. 227 1567–1596 (2007) -- [10.1016/j.jcp.2007.09.017](https://doi.org/10.1016/j.jcp.2007.09.017)
- Lombardi, J. C., Jr., Sills, A., Rasio, F. A. & Shapiro, S. L. Tests of Spurious Transport in Smoothed Particle Hydrodynamics. Journal of Computational Physics vol. 152 687–735 (1999) -- [10.1006/jcph.1999.6256](https://doi.org/10.1006/jcph.1999.6256)
- Iwasaki, K. & Inutsuka, S. Smoothed particle magnetohydrodynamics with a Riemann solver and the method of characteristics. Monthly Notices of the Royal Astronomical Society vol. 418 1668–1688 (2011) -- [10.1111/j.1365-2966.2011.19588.x](https://doi.org/10.1111/j.1365-2966.2011.19588.x)
- Hernquist, L. Some cautionary remarks about smoothed particle hydrodynamics. The Astrophysical Journal vol. 404 717 (1993) -- [10.1086/172325](https://doi.org/10.1086/172325)
- Lattanzio, J. C., Monaghan, J. J., Pongracic, H. & Schwarz, M. P. Controlling Penetration. SIAM Journal on Scientific and Statistical Computing vol. 7 591–598 (1986) -- [10.1137/0907039](https://doi.org/10.1137/0907039)
- Cullen, L. & Dehnen, W. Inviscid smoothed particle hydrodynamics. Monthly Notices of the Royal Astronomical Society vol. 408 669–683 (2010) -- [10.1111/j.1365-2966.2010.17158.x](https://doi.org/10.1111/j.1365-2966.2010.17158.x)
- Liu, M. B., Liu, G. R. & Lam, K. Y. A one-dimensional meshfree particle formulation for simulating shock waves. Shock Waves vol. 13 201–211 (2003) -- [10.1007/s00193-003-0207-0](https://doi.org/10.1007/s00193-003-0207-0)
- Lucy, L. B. A numerical approach to the testing of the fission hypothesis. The Astronomical Journal vol. 82 1013 (1977) -- [10.1086/112164](https://doi.org/10.1086/112164)
- Monaghan, J. J. Extrapolating B splines for interpolation. Journal of Computational Physics vol. 60 253–262 (1985) -- [10.1016/0021-9991(85)90006-3](https://doi.org/10.1016/0021-9991(85)90006-3)
- Monaghan, J. J. An introduction to SPH. Computer Physics Communications vol. 48 89–96 (1988) -- [10.1016/0010-4655(88)90026-4](https://doi.org/10.1016/0010-4655(88)90026-4)
- Monaghan, J. J. Smoothed Particle Hydrodynamics. Annual Review of Astronomy and Astrophysics vol. 30 543–574 (1992) -- [10.1146/annurev.aa.30.090192.002551](https://doi.org/10.1146/annurev.aa.30.090192.002551)
- Monaghan, J. J. SPH and Riemann Solvers. Journal of Computational Physics vol. 136 298–307 (1997) -- [10.1006/jcph.1997.5732](https://doi.org/10.1006/jcph.1997.5732)
- Monaghan, J. J. Smoothed particle hydrodynamics. Reports on Progress in Physics vol. 68 1703–1759 (2005) -- [10.1088/0034-4885/68/8/R01](https://doi.org/10.1088/0034-4885/68/8/R01)
- Monaghan, J. J. & Gingold, R. A. Shock simulation by the particle method SPH. Journal of Computational Physics vol. 52 374–389 (1983) -- [10.1016/0021-9991(83)90036-0](https://doi.org/10.1016/0021-9991(83)90036-0)
- Morris, J. P. & Monaghan, J. J. A Switch to Reduce SPH Viscosity. Journal of Computational Physics vol. 136 41–50 (1997) -- [10.1006/jcph.1997.5690](https://doi.org/10.1006/jcph.1997.5690)
- Nelson, R. P. & Papaloizou, J. C. B. Variable smoothing lengths and energy conservation in smoothed particle hydrodynamics. Monthly Notices of the Royal Astronomical Society vol. 270 1–20 (1994) -- [10.1093/mnras/270.1.1](https://doi.org/10.1093/mnras/270.1.1)
- Omang, M., Børve, S. & Trulsen, J. Numerical simulations of shock wave reflection phenomena in non-stationary flows using regularized smoothed particle hydrodynamics (RSPH). Shock Waves vol. 16 167–177 (2006) -- [10.1007/s00193-006-0061-y](https://doi.org/10.1007/s00193-006-0061-y)
- Omang, M., Børve, S. & Trulsen, J. SPH in spherical and cylindrical coordinates. Journal of Computational Physics vol. 213 391–412 (2006) -- [10.1016/j.jcp.2005.08.023](https://doi.org/10.1016/j.jcp.2005.08.023)
- Price, D. J. Modelling discontinuities and Kelvin–Helmholtz instabilities in SPH. Journal of Computational Physics vol. 227 10040–10057 (2008) -- [10.1016/j.jcp.2008.08.011](https://doi.org/10.1016/j.jcp.2008.08.011)
- Price, D. J. Smoothed particle hydrodynamics and magnetohydrodynamics. Journal of Computational Physics vol. 231 759–794 (2012) -- [10.1016/j.jcp.2010.12.011](https://doi.org/10.1016/j.jcp.2010.12.011)
- Price, D. J. & Monaghan, J. J. Smoothed Particle Magnetohydrodynamics - I. Algorithm and tests in one dimension. Monthly Notices of the Royal Astronomical Society vol. 348 123–138 (2004) -- [10.1111/j.1365-2966.2004.07345.x](https://doi.org/10.1111/j.1365-2966.2004.07345.x)
- Randles, P. W. & Libersky, L. D. Smoothed Particle Hydrodynamics: Some recent improvements and applications. Computer Methods in Applied Mechanics and Engineering vol. 139 375–408 (1996) -- [10.1016/S0045-7825(96)01090-0](https://doi.org/10.1016/S0045-7825(96)01090-0)
- Thacker, R. J., Tittley, E. R., Pearce, F. R., Couchman, H. M. P. & Thomas, P. A. Smoothed Particle Hydrodynamics in cosmology: a comparative study of implementations. Monthly Notices of the Royal Astronomical Society vol. 319 619–648 (2000) -- [10.1111/j.1365-8711.2000.03927.x](https://doi.org/10.1111/j.1365-8711.2000.03927.x)
- Roberts, T. W. The behavior of flux difference splitting schemes near slowly moving shock waves. Journal of Computational Physics vol. 90 141–160 (1990) -- [10.1016/0021-9991(90)90200-K](https://doi.org/10.1016/0021-9991(90)90200-K)
- Borve, S., Omang, M. & Trulsen, J. Regularized Smoothed Particle Hydrodynamics: A New Approach to Simulating Magnetohydrodynamic Shocks. The Astrophysical Journal vol. 561 82–93 (2001) -- [10.1086/323228](https://doi.org/10.1086/323228)
- Borve, S., Omang, M. & Trulsen, J. Multidimensional MHD Shock Tests of Regularized Smoothed Particle Hydrodynamics. The Astrophysical Journal vol. 652 1306–1317 (2006) -- [10.1086/508454](https://doi.org/10.1086/508454)
- Sigalotti, L. D. G., López, H., Donoso, A., Sira, E. & Klapp, J. A shock-capturing SPH scheme based on adaptive kernel estimation. Journal of Computational Physics vol. 212 124–149 (2006) -- [10.1016/j.jcp.2005.06.016](https://doi.org/10.1016/j.jcp.2005.06.016)
- Abel, T. rpSPH: a novel smoothed particle hydrodynamics algorithm. Monthly Notices of the Royal Astronomical Society vol. 413 271–285 (2011) -- [10.1111/j.1365-2966.2010.18133.x](https://doi.org/10.1111/j.1365-2966.2010.18133.x)
- van Leer, B. Towards the Ultimate Conservative Difference Scheme. Journal of Computational Physics vol. 135 229–248 (1997) -- [10.1006/jcph.1997.5704](https://doi.org/10.1006/jcph.1997.5704)
- Springel, V. The cosmological simulation code gadget-2. Monthly Notices of the Royal Astronomical Society vol. 364 1105–1134 (2005) -- [10.1111/j.1365-2966.2005.09655.x](https://doi.org/10.1111/j.1365-2966.2005.09655.x)
- Springel, V. Smoothed Particle Hydrodynamics in Astrophysics. Annual Review of Astronomy and Astrophysics vol. 48 391–430 (2010) -- [10.1146/annurev-astro-081309-130914](https://doi.org/10.1146/annurev-astro-081309-130914)
- Springel, V. & Hernquist, L. Cosmological smoothed particle hydrodynamics simulations: the entropy equation. Monthly Notices of the Royal Astronomical Society vol. 333 649–664 (2002) -- [10.1046/j.1365-8711.2002.05445.x](https://doi.org/10.1046/j.1365-8711.2002.05445.x)
- VonNeumann, J. & Richtmyer, R. D. A Method for the Numerical Calculation of Hydrodynamic Shocks. Journal of Applied Physics vol. 21 232–237 (1950) -- [10.1063/1.1699639](https://doi.org/10.1063/1.1699639)
- Noh, W. F. Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. Journal of Computational Physics vol. 72 78–120 (1987) -- [10.1016/0021-9991(87)90074-X](https://doi.org/10.1016/0021-9991(87)90074-X)
- Woodward, P. & Colella, P. The numerical simulation of two-dimensional fluid flow with strong shocks. Journal of Computational Physics vol. 54 115–173 (1984) -- [10.1016/0021-9991(84)90142-6](https://doi.org/10.1016/0021-9991(84)90142-6)

