---
layout: post
title: "Semiempirical Quantum Chemical Calculations Accelerated on a Hybrid Multicore CPU–GPU Computing Platform"
date: 2012-05-25 00:00:00 +0100
permalink: semiempirical-quantum-chemical-calculations-accelerated-on-a-hybrid-multicore-cpu-gpu-computing-platform
year: 2012
authors: Xin Wu, Axel Koslowski, Walter Thiel
category: articles
---
 
## Authors
[Xin Wu](authors/xin-wu), [Axel Koslowski](authors/axel-koslowski), [Walter Thiel](authors/walter-thiel)
 
## Abstract
In this work, we demonstrate that semiempirical quantum chemical calculations can be accelerated significantly by leveraging the graphics processing unit (GPU) as a coprocessor on a hybrid multicore CPU-GPU computing platform. Semiempirical calculations using the MNDO, AM1, PM3, OM1, OM2, and OM3 model Hamiltonians were systematically profiled for three types of test systems (fullerenes, water clusters, and solvated crambin) to identify the most time-consuming sections of the code. The corresponding routines were ported to the GPU and optimized employing both existing library functions and a GPU kernel that carries out a sequence of noniterative Jacobi transformations during pseudodiagonalization. The overall computation times for single-point energy calculations and geometry optimizations of large molecules were reduced by one order of magnitude for all methods, as compared to runs on a single CPU core.
 
## Citation
- **Journal:** Journal of Chemical Theory and Computation
- **Year:** 2012
- **Volume:** 8
- **Issue:** 7
- **Pages:** 2272--2281
- **Publisher:** American Chemical Society (ACS)
- **DOI:** [10.1021/ct3001798](https://doi.org/10.1021/ct3001798)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Wu_2012,
  title={{Semiempirical Quantum Chemical Calculations Accelerated on a Hybrid Multicore CPU–GPU Computing Platform}},
  volume={8},
  ISSN={1549-9626},
  DOI={10.1021/ct3001798},
  number={7},
  journal={Journal of Chemical Theory and Computation},
  publisher={American Chemical Society (ACS)},
  author={Wu, Xin and Koslowski, Axel and Thiel, Walter},
  year={2012},
  pages={2272--2281}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/semiempirical-quantum-chemical-calculations-accelerated-on-a-hybrid-multicore-cpu-gpu-computing-platform.bib)
 
## References
- Bredow, T. & Jug, K. Theory and range of modern semiempirical molecular orbital methods. Theor Chem Acc 113, 1–14 (2004) -- [10.1007/s00214-004-0610-3](https://doi.org/10.1007/s00214-004-0610-3)
- Clark, T. Quo Vadis semiempirical MO-theory? Journal of Molecular Structure: THEOCHEM 530, 1–10 (2000) -- [10.1016/s0166-1280(00)00581-9](https://doi.org/10.1016/s0166-1280(00)00581-9)
- Thiel, W. Perspectives on Semiempirical Molecular Orbital Theory. Advances in Chemical Physics 703–757 (1996) doi:10.1002/9780470141526.ch10 -- [10.1002/9780470141526.ch10](https://doi.org/10.1002/9780470141526.ch10)
- Thiel, W. Semiempirical methods: current status and perspectives. Tetrahedron 44, 7393–7408 (1988) -- [10.1016/s0040-4020(01)86235-9](https://doi.org/10.1016/s0040-4020(01)86235-9)
- Dewar, M. J. S. & Thiel, W. A semiempirical model for the two-center repulsion integrals in the NDDO approximation. Theoret. Chim. Acta 46, 89–104 (1977) -- [10.1007/bf00548085](https://doi.org/10.1007/bf00548085)
- NVIDIA CUDA C Programming Guide (2010)
- Stone, J. E., Hardy, D. J., Ufimtsev, I. S. & Schulten, K. GPU-accelerated molecular modeling coming of age. Journal of Molecular Graphics and Modelling 29, 116–125 (2010) -- [10.1016/j.jmgm.2010.06.010](https://doi.org/10.1016/j.jmgm.2010.06.010)
- Farber, R. M. Topical perspective on massive threading and parallelism. Journal of Molecular Graphics and Modelling 30, 82–89 (2011) -- [10.1016/j.jmgm.2011.06.007](https://doi.org/10.1016/j.jmgm.2011.06.007)
- van der Spoel, D. & Hess, B. GROMACS—the road ahead. WIREs Comput Mol Sci 1, 710–715 (2011) -- [10.1002/wcms.50](https://doi.org/10.1002/wcms.50)
- Anderson, A. G., Goddard, W. A., III & Schröder, P. Quantum Monte Carlo on graphical processing units. Computer Physics Communications 177, 298–306 (2007) -- [10.1016/j.cpc.2007.03.004](https://doi.org/10.1016/j.cpc.2007.03.004)
- Ufimtsev, I. S. & Martínez, T. J. Graphical Processing Units for Quantum Chemistry. Comput. Sci. Eng. 10, 26–34 (2008) -- [10.1109/mcse.2008.148](https://doi.org/10.1109/mcse.2008.148)
- Ufimtsev, I. S. & Martínez, T. J. Quantum Chemistry on Graphical Processing Units. 1. Strategies for Two-Electron Integral Evaluation. J. Chem. Theory Comput. 4, 222–231 (2008) -- [10.1021/ct700268q](https://doi.org/10.1021/ct700268q)
- Ufimtsev, I. S. & Martinez, T. J. Quantum Chemistry on Graphical Processing Units. 2. Direct Self-Consistent-Field Implementation. J. Chem. Theory Comput. 5, 1004–1015 (2009) -- [10.1021/ct800526s](https://doi.org/10.1021/ct800526s)
- Ufimtsev, I. S. & Martinez, T. J. Quantum Chemistry on Graphical Processing Units. 3. Analytical Energy Gradients, Geometry Optimization, and First Principles Molecular Dynamics. J. Chem. Theory Comput. 5, 2619–2628 (2009) -- [10.1021/ct9003004](https://doi.org/10.1021/ct9003004)
- Luehr, N., Ufimtsev, I. S. & Martínez, T. J. Dynamic Precision for Electron Repulsion Integral Evaluation on Graphical Processing Units (GPUs). J. Chem. Theory Comput. 7, 949–954 (2011) -- [10.1021/ct100701w](https://doi.org/10.1021/ct100701w)
- Isborn, C. M., Luehr, N., Ufimtsev, I. S. & Martínez, T. J. Excited-State Electronic Structure with Configuration Interaction Singles and Tamm–Dancoff Time-Dependent Density Functional Theory on Graphical Processing Units. J. Chem. Theory Comput. 7, 1814–1823 (2011) -- [10.1021/ct200030k](https://doi.org/10.1021/ct200030k)
- Yasuda, K. Two‐electron integral evaluation on the graphics processor unit. J Comput Chem 29, 334–342 (2007) -- [10.1002/jcc.20779](https://doi.org/10.1002/jcc.20779)
- Yasuda, K. Accelerating Density Functional Calculations with Graphics Processing Unit. J. Chem. Theory Comput. 4, 1230–1236 (2008) -- [10.1021/ct8001046](https://doi.org/10.1021/ct8001046)
- Asadchev, A. et al. Uncontracted Rys Quadrature Implementation of up to G Functions on Graphical Processing Units. J. Chem. Theory Comput. 6, 696–704 (2010) -- [10.1021/ct9005079](https://doi.org/10.1021/ct9005079)
- Vogt, L. et al. Accelerating Resolution-of-the-Identity Second-Order Møller−Plesset Quantum Chemistry Calculations with Graphical Processing Units. J. Phys. Chem. A 112, 2049–2057 (2008) -- [10.1021/jp0776762](https://doi.org/10.1021/jp0776762)
- Olivares-Amaya, R. et al. Accelerating Correlated Quantum Chemistry Calculations Using Graphical Processing Units and a Mixed Precision Matrix Multiplication Library. J. Chem. Theory Comput. 6, 135–144 (2009) -- [10.1021/ct900543q](https://doi.org/10.1021/ct900543q)
- DePrince, A. E., III & Hammond, J. R. Coupled Cluster Theory on Graphics Processing Units I. The Coupled Cluster Doubles Method. J. Chem. Theory Comput. 7, 1287–1295 (2011) -- [10.1021/ct100584w](https://doi.org/10.1021/ct100584w)
- Ma, W., Krishnamoorthy, S., Villa, O. & Kowalski, K. GPU-Based Implementations of the Noniterative Regularized-CCSD(T) Corrections: Applications to Strongly Correlated Systems. J. Chem. Theory Comput. 7, 1316–1327 (2011) -- [10.1021/ct1007247](https://doi.org/10.1021/ct1007247)
- Wilkinson, K. A., Sherwood, P., Guest, M. F. & Naidoo, K. J. Acceleration of the GAMESS‐UK electronic structure package on graphical processing units. J Comput Chem 32, 2313–2318 (2011) -- [10.1002/jcc.21815](https://doi.org/10.1002/jcc.21815)
- Thiel W., MNDO99 CVS Development Version (2012)
- Dewar, M. J. S. & Thiel, W. Ground states of molecules. 38. The MNDO method. Approximations and parameters. J. Am. Chem. Soc. 99, 4899–4907 (1977) -- [10.1021/ja00457a004](https://doi.org/10.1021/ja00457a004)
- Dewar, M. J. S. & Thiel, W. Ground states of molecules. 39. MNDO results for molecules containing hydrogen, carbon, nitrogen, and oxygen. J. Am. Chem. Soc. 99, 4907–4917 (1977) -- [10.1021/ja00457a005](https://doi.org/10.1021/ja00457a005)
- Dewar, M. J. S., Zoebisch, E. G., Healy, E. F. & Stewart, J. J. P. Development and use of quantum mechanical molecular models. 76. AM1: a new general purpose quantum mechanical molecular model. J. Am. Chem. Soc. 107, 3902–3909 (1985) -- [10.1021/ja00299a024](https://doi.org/10.1021/ja00299a024)
- Stewart, J. J. P. Optimization of parameters for semiempirical methods I. Method. J Comput Chem 10, 209–220 (1989) -- [10.1002/jcc.540100208](https://doi.org/10.1002/jcc.540100208)
- Stewart, J. J. P. Optimization of parameters for semiempirical methods II. Applications. J Comput Chem 10, 221–264 (1989) -- [10.1002/jcc.540100209](https://doi.org/10.1002/jcc.540100209)
- Kolb, M. & Thiel, W. Beyond the MNDO model: Methodical considerations and numerical results. J Comput Chem 14, 775–789 (1993) -- [10.1002/jcc.540140704](https://doi.org/10.1002/jcc.540140704)
- Weber, W. & Thiel, W. Orthogonalization corrections for semiempirical methods. Theoretical Chemistry Accounts: Theory, Computation, and Modeling (Theoretica Chimica Acta) 103, 495–506 (2000) -- [10.1007/s002149900083](https://doi.org/10.1007/s002149900083)
- Bakowies, D. & Thiel, W. MNDO study of large carbon clusters. J. Am. Chem. Soc. 113, 3704–3714 (1991) -- [10.1021/ja00010a012](https://doi.org/10.1021/ja00010a012)
- Bakowies, D., Buehl, M. & Thiel, W. Can Large Fullerenes Be Spherical? J. Am. Chem. Soc. 117, 10113–10118 (1995) -- [10.1021/ja00145a025](https://doi.org/10.1021/ja00145a025)
- Martínez, L., Andrade, R., Birgin, E. G. & Martínez, J. M. P<scp>ACKMOL</scp>: A package for building initial configurations for molecular dynamics simulations. J Comput Chem 30, 2157–2164 (2009) -- [10.1002/jcc.21224](https://doi.org/10.1002/jcc.21224)
- CUDA CUBLAS Library (2010)
- Tomov S., MAGMA Users’ Guide (2010)
- Pople, J. A., Santry, D. P. & Segal, G. A. Approximate Self-Consistent Molecular Orbital Theory. I. Invariant Procedures. The Journal of Chemical Physics 43, S129–S135 (1965) -- [10.1063/1.1701475](https://doi.org/10.1063/1.1701475)
- Otte, N., Scholten, M. & Thiel, W. Looking at Self-Consistent-Charge Density Functional Tight Binding from a Semiempirical Perspective. J. Phys. Chem. A 111, 5751–5755 (2007) -- [10.1021/jp0700130](https://doi.org/10.1021/jp0700130)
- Korth, M. & Thiel, W. Benchmarking Semiempirical Methods for Thermochemistry, Kinetics, and Noncovalent Interactions: OMx Methods Are Almost As Accurate and Robust As DFT-GGA Methods for Organic Molecules. J. Chem. Theory Comput. 7, 2929–2936 (2011) -- [10.1021/ct200434a](https://doi.org/10.1021/ct200434a)
- Silva-Junior, M. R. & Thiel, W. Benchmark of Electronically Excited States for Semiempirical Methods: MNDO, AM1, PM3, OM1, OM2, OM3, INDO/S, and INDO/S2. J. Chem. Theory Comput. 6, 1546–1564 (2010) -- [10.1021/ct100030j](https://doi.org/10.1021/ct100030j)
- Pulay, P. Improved <scp>SCF</scp> convergence acceleration. J Comput Chem 3, 556–560 (1982) -- [10.1002/jcc.540030413](https://doi.org/10.1002/jcc.540030413)
- Stewart, J. J. P., Császár, P. & Pulay, P. Fast semiempirical calculations. J Comput Chem 3, 227–228 (1982) -- [10.1002/jcc.540030214](https://doi.org/10.1002/jcc.540030214)
- Anderson, E. et al. LAPACK Users’ Guide. (1999) doi:10.1137/1.9780898719604 -- [10.1137/1.9780898719604](https://doi.org/10.1137/1.9780898719604)
- Modi, J. J. & Parkinson, D. Study of Jacobi methods for eigenvalues and singular value decomposition on DAP. Computer Physics Communications 26, 317–320 (1982) -- [10.1016/0010-4655(82)90122-9](https://doi.org/10.1016/0010-4655(82)90122-9)
- Berry, M. & Sameh, A. An overview of parallel algorithms for the singular value and symmetric eigenvalue problems. Journal of Computational and Applied Mathematics 27, 191–213 (1989) -- [10.1016/0377-0427(89)90366-x](https://doi.org/10.1016/0377-0427(89)90366-x)
- Eberlein, P. J. & Park, H. Efficient implementation of Jacobi algorithms and Jacobi sets on distributed memory architectures. Journal of Parallel and Distributed Computing 8, 358–366 (1990) -- [10.1016/0743-7315(90)90134-b](https://doi.org/10.1016/0743-7315(90)90134-b)

