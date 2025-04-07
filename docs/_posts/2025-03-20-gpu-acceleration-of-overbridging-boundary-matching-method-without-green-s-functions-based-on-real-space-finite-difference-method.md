---
layout: post
title: "GPU acceleration of overbridging boundary matching method without Green's functions based on real-space finite-difference method"
date: 2025-03-20 00:00:00 +0100
permalink: gpu-acceleration-of-overbridging-boundary-matching-method-without-green-s-functions-based-on-real-space-finite-difference-method
year: 2025
authors: Takanori Akamatsu, Mitsuharu Uemoto, Yoshiyuki Egami, Tomoya Ono
category: articles
tags:
  - GPU
  - OpenACC
  - DFT
  - First-principles calculation
  - Real-space method
  - Transport-property calculation
---
 
## Authors
[Takanori Akamatsu](authors/takanori-akamatsu), [Mitsuharu Uemoto](authors/mitsuharu-uemoto), [Yoshiyuki Egami](authors/yoshiyuki-egami), [Tomoya Ono](authors/tomoya-ono)
 
## Abstract
We present the graphics processing unit (GPU) acceleration of the overbridging boundary matching method for electron-transport property calculations, which is based on the density functional theory using the real-space finite-difference method. The execution of the implemented code using OpenACC and CUDA libraries on GPU is computationally more efficient and faster than a central processing unit. Furthermore, we achieve the ideal scalability in parallel execution from one to thirty-two nodes by adopting multiprocess parallelization schemes for two types of supercomputer with different configurations. To demonstrate the applicability of the accelerated code, the complex band structures of graphene and armchair carbon nanotubes with chiral indices (6, 6), (9, 9), and (12, 12) are calculated and compared with those obtained by the tight-binding method. We discuss the effects of the dispersion of evanescent waves on roll-up and axial strain in the carbon nanotubes.
 
## Keywords
GPU; OpenACC; DFT; First-principles calculation; Real-space method; Transport-property calculation
 
## Citation
- **Journal:** Computer Physics Communications
- **Year:** 2025
- **Volume:** 312
- **Issue:** 
- **Pages:** 109585
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.cpc.2025.109585](https://doi.org/10.1016/j.cpc.2025.109585)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Akamatsu_2025,
  title={{GPU acceleration of overbridging boundary matching method without Green’s functions based on real-space finite-difference method}},
  volume={312},
  ISSN={0010-4655},
  DOI={10.1016/j.cpc.2025.109585},
  journal={Computer Physics Communications},
  publisher={Elsevier BV},
  author={Akamatsu, Takanori and Uemoto, Mitsuharu and Egami, Yoshiyuki and Ono, Tomoya},
  year={2025},
  pages={109585}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/gpu-acceleration-of-overbridging-boundary-matching-method-without-green-s-functions-based-on-real-space-finite-difference-method.bib)
 
## References
- Hirose, (2005)
- Fujimoto, Phys. Rev. B (2003)
- Ono, Phys. Rev. B (2012)
- Ono, T. et al. Real-space electronic structure calculations with full-potential all-electron precision for transition metals. Physical Review B vol. 82 (2010) -- [10.1103/physrevb.82.205115](https://doi.org/10.1103/physrevb.82.205115)
- Kohn, W. & Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. Physical Review vol. 140 A1133–A1138 (1965) -- [10.1103/physrev.140.a1133](https://doi.org/10.1103/physrev.140.a1133)
- Tsukamoto, S., Ono, T. & Blügel, S. Improvement of accuracy in the wave-function-matching method for transport calculations. Physical Review B vol. 97 (2018) -- [10.1103/physrevb.97.115450](https://doi.org/10.1103/physrevb.97.115450)
- Tsukamoto, S., Hirose, K. & Blügel, S. Real-space finite-difference calculation method of generalized Bloch wave functions and complex band structures with reduced computational cost. Physical Review E vol. 90 (2014) -- [10.1103/physreve.90.013306](https://doi.org/10.1103/physreve.90.013306)
- Sakurai, T. & Sugiura, H. A projection method for generalized eigenvalue problems using numerical integration. Journal of Computational and Applied Mathematics vol. 159 119–128 (2003) -- [10.1016/s0377-0427(03)00565-x](https://doi.org/10.1016/s0377-0427(03)00565-x)
- Ikegami, T., Sakurai, T. & Nagashima, U. A filter diagonalization for generalized eigenvalue problems based on the Sakurai–Sugiura projection method. Journal of Computational and Applied Mathematics vol. 233 1927–1936 (2010) -- [10.1016/j.cam.2009.09.029](https://doi.org/10.1016/j.cam.2009.09.029)
- Asakura, J., Sakurai, T., Tadano, H., Ikegami, T. & Kimura, K. A numerical method for nonlinear eigenvalue problems using contour integrals. JSIAM Letters vol. 1 52–55 (2009) -- [10.14495/jsiaml.1.52](https://doi.org/10.14495/jsiaml.1.52)
- Slater, J. C. & Koster, G. F. Simplified LCAO Method for the Periodic Potential Problem. Physical Review vol. 94 1498–1524 (1954) -- [10.1103/physrev.94.1498](https://doi.org/10.1103/physrev.94.1498)
- Harrison, (2012)
- Uemoto, M., Nishiura, M. & Ono, T. Valley filters using graphene blister defects from first principles. Journal of Physics: Condensed Matter vol. 36 095301 (2023) -- [10.1088/1361-648x/ad0d26](https://doi.org/10.1088/1361-648x/ad0d26)
- Rezaei, H. & Phirouznia, A. Modified spin–orbit couplings in uniaxially strained graphene. The European Physical Journal B vol. 91 (2018) -- [10.1140/epjb/e2018-80663-2](https://doi.org/10.1140/epjb/e2018-80663-2)
- Ribeiro, R. M., Pereira, V. M., Peres, N. M. R., Briddon, P. R. & Castro Neto, A. H. Strained graphene: tight-binding and density functional calculations. New Journal of Physics vol. 11 115002 (2009) -- [10.1088/1367-2630/11/11/115002](https://doi.org/10.1088/1367-2630/11/11/115002)
- Diniz, G. S., Guassi, M. R. & Qu, F. Engineering the quantum anomalous Hall effect in graphene with uniaxial strains. Journal of Applied Physics vol. 114 (2013) -- [10.1063/1.4854415](https://doi.org/10.1063/1.4854415)
- Tsukamoto, S., Ono, T., Iwase, S. & Blügel, S. Complex band structure calculations based on the overbridging boundary matching method without using Green’s functions. Physical Review B vol. 98 (2018) -- [10.1103/physrevb.98.195422](https://doi.org/10.1103/physrevb.98.195422)
- Yamamoto, J. Phys. Soc. Jpn. (2008)
- Frommer, A. BiCGStab(?) for Families of Shifted Linear Systems. Computing vol. 70 87–109 (2003) -- [10.1007/s00607-003-1472-6](https://doi.org/10.1007/s00607-003-1472-6)
- SAKURAI, T. & TADANO, H. CIRR: a Rayleigh-Ritz type method with contour integral for generalized eigenvalue problems. Hokkaido Mathematical Journal vol. 36 (2007) -- [10.14492/hokmj/1272848031](https://doi.org/10.14492/hokmj/1272848031)
- Ikegami, T. & Sakurai, T. CONTOUR INTEGRAL EIGENSOLVER FOR NON-HERMITIAN SYSTEMS: A RAYLEIGH-RITZ-TYPE APPROACH. Taiwanese Journal of Mathematics vol. 14 (2010) -- [10.11650/twjm/1500405869](https://doi.org/10.11650/twjm/1500405869)
- Imakura, A. & Sakurai, T. Block Krylov-type complex moment-based eigensolvers for solving generalized eigenvalue problems. Numerical Algorithms vol. 75 413–433 (2016) -- [10.1007/s11075-016-0241-5](https://doi.org/10.1007/s11075-016-0241-5)
- Nagai, Y., Shinohara, Y., Futamura, Y., Ota, Y. & Sakurai, T. Numerical Construction of a Low-Energy Effective Hamiltonian in a Self-Consistent Bogoliubov–de Gennes Approach of Superconductivity. Journal of the Physical Society of Japan vol. 82 094701 (2013) -- [10.7566/jpsj.82.094701](https://doi.org/10.7566/jpsj.82.094701)
- Chelikowsky, J. R., Troullier, N. & Saad, Y. Finite-difference-pseudopotential method: Electronic structure calculations without a basis. Physical Review Letters vol. 72 1240–1243 (1994) -- [10.1103/physrevlett.72.1240](https://doi.org/10.1103/physrevlett.72.1240)
- Chelikowsky, J. R., Troullier, N., Wu, K. & Saad, Y. Higher-order finite-difference pseudopotential method: An application to diatomic molecules. Physical Review B vol. 50 11355–11364 (1994) -- [10.1103/physrevb.50.11355](https://doi.org/10.1103/physrevb.50.11355)
- NVIDIA,
- NVIDIA,
- NVIDIA,
- NVIDIA,
- Vosko, S. H., Wilk, L. & Nusair, M. Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis. Canadian Journal of Physics vol. 58 1200–1211 (1980) -- [10.1139/p80-159](https://doi.org/10.1139/p80-159)
- Hohenberg, P. & Kohn, W. Inhomogeneous Electron Gas. Physical Review vol. 136 B864–B871 (1964) -- [10.1103/physrev.136.b864](https://doi.org/10.1103/physrev.136.b864)
- Troullier, N. & Martins, J. L. Efficient pseudopotentials for plane-wave calculations. Physical Review B vol. 43 1993–2006 (1991) -- [10.1103/physrevb.43.1993](https://doi.org/10.1103/physrevb.43.1993)
- Kobayashi, K. Norm-conserving pseudopotential database (NCPS97). Computational Materials Science vol. 14 72–76 (1999) -- [10.1016/s0927-0256(98)00074-3](https://doi.org/10.1016/s0927-0256(98)00074-3)
- Harris,
- Si, C., Sun, Z. & Liu, F. Strain engineering of graphene: a review. Nanoscale vol. 8 3207–3217 (2016) -- [10.1039/c5nr07755a](https://doi.org/10.1039/c5nr07755a)

