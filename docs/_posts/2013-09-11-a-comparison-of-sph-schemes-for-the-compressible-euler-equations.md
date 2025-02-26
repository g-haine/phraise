---
layout: post
title: "A comparison of SPH schemes for the compressible Euler equations"
date: 2013-09-11 00:00:00 +0100
permalink: a-comparison-of-sph-schemes-for-the-compressible-euler-equations
year: 2014
authors: Kunal Puri, Prabhu Ramachandran
category: journal-article
tag: SPH; Particle method; Euler equations
---
 
## Authors
**Kunal Puri, Prabhu Ramachandran**
 
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
- [10.1111/j.1365-2966.2007.12183.x](https://doi.org/10.1111/j.1365-2966.2007.12183.x)
- [10.1016/0021-9991(91)90211-3](https://doi.org/10.1016/0021-9991(91)90211-3)
- [10.1090/S0025-5718-1980-0551290-1](https://doi.org/10.1090/S0025-5718-1980-0551290-1)
- [10.1046/j.1365-8711.2003.06266.x](https://doi.org/10.1046/j.1365-8711.2003.06266.x)
- [10.1111/j.1365-2966.2010.16200.x](https://doi.org/10.1111/j.1365-2966.2010.16200.x)
- [10.1006/jcph.2002.7152](https://doi.org/10.1006/jcph.2002.7152)
- [10.1016/0021-9991(84)90143-8](https://doi.org/10.1016/0021-9991(84)90143-8)
- [10.1016/S0021-9991(95)90221-X](https://doi.org/10.1016/S0021-9991(95)90221-X)
- [10.1111/j.1365-2966.2011.19021.x](https://doi.org/10.1111/j.1365-2966.2011.19021.x)
- [10.1016/0021-9991(78)90023-2](https://doi.org/10.1016/0021-9991(78)90023-2)
- [10.1093/mnras/181.3.375](https://doi.org/10.1093/mnras/181.3.375)
- [10.1006/jcph.2002.7053](https://doi.org/10.1006/jcph.2002.7053)
- [10.1016/j.jcp.2007.09.017](https://doi.org/10.1016/j.jcp.2007.09.017)
- [10.1006/jcph.1999.6256](https://doi.org/10.1006/jcph.1999.6256)
- [10.1111/j.1365-2966.2011.19588.x](https://doi.org/10.1111/j.1365-2966.2011.19588.x)
- [10.1086/172325](https://doi.org/10.1086/172325)
- [10.1137/0907039](https://doi.org/10.1137/0907039)
- [10.1111/j.1365-2966.2010.17158.x](https://doi.org/10.1111/j.1365-2966.2010.17158.x)
- [10.1007/s00193-003-0207-0](https://doi.org/10.1007/s00193-003-0207-0)
- [10.1086/112164](https://doi.org/10.1086/112164)
- [10.1016/0021-9991(85)90006-3](https://doi.org/10.1016/0021-9991(85)90006-3)
- [10.1016/0010-4655(88)90026-4](https://doi.org/10.1016/0010-4655(88)90026-4)
- [10.1146/annurev.aa.30.090192.002551](https://doi.org/10.1146/annurev.aa.30.090192.002551)
- [10.1006/jcph.1997.5732](https://doi.org/10.1006/jcph.1997.5732)
- [10.1088/0034-4885/68/8/R01](https://doi.org/10.1088/0034-4885/68/8/R01)
- [10.1016/0021-9991(83)90036-0](https://doi.org/10.1016/0021-9991(83)90036-0)
- [10.1006/jcph.1997.5690](https://doi.org/10.1006/jcph.1997.5690)
- [10.1093/mnras/270.1.1](https://doi.org/10.1093/mnras/270.1.1)
- [10.1007/s00193-006-0061-y](https://doi.org/10.1007/s00193-006-0061-y)
- [10.1016/j.jcp.2005.08.023](https://doi.org/10.1016/j.jcp.2005.08.023)
- [10.1016/j.jcp.2008.08.011](https://doi.org/10.1016/j.jcp.2008.08.011)
- [10.1016/j.jcp.2010.12.011](https://doi.org/10.1016/j.jcp.2010.12.011)
- [10.1111/j.1365-2966.2004.07345.x](https://doi.org/10.1111/j.1365-2966.2004.07345.x)
- [10.1016/S0045-7825(96)01090-0](https://doi.org/10.1016/S0045-7825(96)01090-0)
- [10.1111/j.1365-8711.2000.03927.x](https://doi.org/10.1111/j.1365-8711.2000.03927.x)
- [10.1016/0021-9991(90)90200-K](https://doi.org/10.1016/0021-9991(90)90200-K)
- [10.1086/323228](https://doi.org/10.1086/323228)
- [10.1086/508454](https://doi.org/10.1086/508454)
- [10.1016/j.jcp.2005.06.016](https://doi.org/10.1016/j.jcp.2005.06.016)
- [10.1111/j.1365-2966.2010.18133.x](https://doi.org/10.1111/j.1365-2966.2010.18133.x)
- [10.1006/jcph.1997.5704](https://doi.org/10.1006/jcph.1997.5704)
- [10.1111/j.1365-2966.2005.09655.x](https://doi.org/10.1111/j.1365-2966.2005.09655.x)
- [10.1146/annurev-astro-081309-130914](https://doi.org/10.1146/annurev-astro-081309-130914)
- [10.1046/j.1365-8711.2002.05445.x](https://doi.org/10.1046/j.1365-8711.2002.05445.x)
- [10.1063/1.1699639](https://doi.org/10.1063/1.1699639)
- [10.1016/0021-9991(87)90074-X](https://doi.org/10.1016/0021-9991(87)90074-X)
- [10.1016/0021-9991(84)90142-6](https://doi.org/10.1016/0021-9991(84)90142-6)

