---
title: "PyBERTHART: A Relativistic Real-Time Four-Component TDDFT Implementation Using Prototyping Techniques Based on Python"
date: 2020-02-26 00:00:00 +0100
permalink: pyberthart-a-relativistic-real-time-four-component-tddft-implementation-using-prototyping-techniques-based-on-python
year: 2020
authors: Matteo De Santis, Loriano Storchi, Leonardo Belpassi, Harry M. Quiney, Francesco Tarantelli
category: articles
---
 
## Authors
[Matteo De Santis](authors/matteo-de-santis), [Loriano Storchi](authors/loriano-storchi), [Leonardo Belpassi](authors/leonardo-belpassi), [Harry M. Quiney](authors/harry-m-quiney), [Francesco Tarantelli](authors/francesco-tarantelli)
 
## Abstract
We present a real-time time-dependent four-component Dirac-Kohn-Sham (RT-TDDKS) implementation based on the BERTHA code. This new implementation takes advantage of modern software engineering, including the prototyping techniques. The software design follows a three step approach: i) the prototype implementation of time-propagation algorithm in non-relativistic real-time TDDFT within the Psi4NumPy framework, which provides an easy-to-use environment for the creation of a clear, readable and easy to test reference code in Python, ii) the design of an original Python application programming interface for the relativistic four-component code BERTHA (PyBERTHA), which has an efficient computational kernel for relativistic integrals written in FORTRAN and iii) the porting of the time-propagation scheme eveloped within the Psi4NumPy framework to PyBERTHA. The propagation scheme consequently resides in a single readable Python computer code that is easy to maintain and in which the key quantities, such as the Dirac-Kohn-Sham and dipole matrices, can be accessed directly from the PyBERTHA module. For linear algebra operations (matrix-matrix multiplications and diagonalization) we use the highly optimized procedures implemented in the popular NumPy library. The overhead introduced by the Python interface to BERTHA is almost negligible (less than 1\% evaluated on the SCF procedure) and the inter-operability between different programming languages (FORTRAN, C and Python) does not affect the numerical stability of the time propagation scheme. Our new RT-TDDKS implementation has been employed to investigate the stability of the time propagation procedure in combination with density-fitting algorithm (both for the Coulomb and for the exchange-correlation matrix construction), which are employed in BERTHA to speed-up the Dirac-Kohn-Sham matrix evaluation. On the basis of systematic calculations, employing several density fitting basis sets of increasing accuracy, we showed that quantitative agreement can be achieved in combination with extended fitting basis sets, with an error in the Coulomb energy below 1 μ-hartree. Convergence of the transition energies increasing of quality of the fitting basis sets has been also observed. Our data suggest that the error in the Coulomb energy may also represent a good estimate of the fitting basis set quality for real-time electron dynamic simulations. Further, we study the applicability of the RT-TDDKS method in combination of both weak and extreme strong field regime. Numerical results of excited-state transitions for the Group 12 atoms are reported and compared with a previous real-time Dirac-Kohn-Sham implementation (Repisky et. al. J. Chem. Theory Comp. 2015, 11, 980-991.). Finally, calculations of high harmonic generation in the hydrogen molecule and Au dimer have been also carried out. We were able to generate high harmonics with relatively well-defined peaks up to 21th and 13th order in the case of H2 and Au2, respectively. Our findings show that the four-component structure of the Dirac-Kohn-Sham hamiltonian provides a suitable theoretical framework, with no intrinsic unfavorable features, to study molecules in the strong-field regime.
 
## Citation
- **Journal:** Journal of Chemical Theory and Computation
- **Year:** 2020
- **Volume:** 16
- **Issue:** 4
- **Pages:** 2410--2429
- **Publisher:** American Chemical Society (ACS)
- **DOI:** [10.1021/acs.jctc.0c00053](https://doi.org/10.1021/acs.jctc.0c00053)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{De_Santis_2020,
  title={{PyBERTHART: A Relativistic Real-Time Four-Component TDDFT Implementation Using Prototyping Techniques Based on Python}},
  volume={16},
  ISSN={1549-9626},
  DOI={10.1021/acs.jctc.0c00053},
  number={4},
  journal={Journal of Chemical Theory and Computation},
  publisher={American Chemical Society (ACS)},
  author={De Santis, Matteo and Storchi, Loriano and Belpassi, Leonardo and Quiney, Harry M. and Tarantelli, Francesco},
  year={2020},
  pages={2410--2429}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/pyberthart-a-relativistic-real-time-four-component-tddft-implementation-using-prototyping-techniques-based-on-python.bib)
 
## References
- Hardin, B. E. et al. Increased light harvesting in dye-sensitized solar cells with energy relay dyes. Nature Photon 3, 406–411 (2009) -- [10.1038/nphoton.2009.96](https://doi.org/10.1038/nphoton.2009.96)
- Hagfeldt, A., Boschloo, G., Sun, L., Kloo, L. & Pettersson, H. Dye-Sensitized Solar Cells. Chem. Rev. 110, 6595–6663 (2010) -- [10.1021/cr900356p](https://doi.org/10.1021/cr900356p)
- Solarczyk, K. J., Zarębski, M. & Dobrucki, J. W. Inducing local DNA damage by visible light to study chromatin repair. DNA Repair 11, 996–1002 (2012) -- [10.1016/j.dnarep.2012.09.008](https://doi.org/10.1016/j.dnarep.2012.09.008)
- Salières, P. et al. Frequency-Domain Interferometry in the XUV with High-Order Harmonics. Phys. Rev. Lett. 83, 5483–5486 (1999) -- [10.1103/physrevlett.83.5483](https://doi.org/10.1103/physrevlett.83.5483)
- Paul, P. M. et al. Observation of a Train of Attosecond Pulses from High Harmonic Generation. Science 292, 1689–1692 (2001) -- [10.1126/science.1059413](https://doi.org/10.1126/science.1059413)
- Bass, M., Franken, P. A., Ward, J. F. & Weinreich, G. Optical Rectification. Phys. Rev. Lett. 9, 446–448 (1962) -- [10.1103/physrevlett.9.446](https://doi.org/10.1103/physrevlett.9.446)
- Kadlec, F., Kužel, P. & Coutaz, J.-L. Study of terahertz radiation generated by optical rectification on thin gold films. Opt. Lett. 30, 1402 (2005) -- [10.1364/ol.30.001402](https://doi.org/10.1364/ol.30.001402)
- Keldysh, L. V. Multiphoton ionization by a very short pulse. Phys.-Usp. 60, 1187–1193 (2017) -- [10.3367/ufne.2017.10.038229](https://doi.org/10.3367/ufne.2017.10.038229)
- Eberly, J. H., Javanainen, J. & Rza̧żewski, K. Above-threshold ionization. Physics Reports 204, 331–383 (1991) -- [10.1016/0370-1573(91)90131-5](https://doi.org/10.1016/0370-1573(91)90131-5)
- Gallmann, L., Cirelli, C. & Keller, U. Attosecond Science: Recent Highlights and Future Trends. Annu. Rev. Phys. Chem. 63, 447–469 (2012) -- [10.1146/annurev-physchem-032511-143702](https://doi.org/10.1146/annurev-physchem-032511-143702)
- Ramasesha, K., Leone, S. R. & Neumark, D. M. Real-Time Probing of Electron Dynamics Using Attosecond Time-Resolved Spectroscopy. Annu. Rev. Phys. Chem. 67, 41–63 (2016) -- [10.1146/annurev-physchem-040215-112025](https://doi.org/10.1146/annurev-physchem-040215-112025)
- Attar, A. R. et al. Femtosecond x-ray spectroscopy of an electrocyclic ring-opening reaction. Science 356, 54–59 (2017) -- [10.1126/science.aaj2198](https://doi.org/10.1126/science.aaj2198)
- Wolf, T. J. A. et al. The photochemical ring-opening of 1,3-cyclohexadiene imaged by ultrafast electron diffraction. Nat. Chem. 11, 504–509 (2019) -- [10.1038/s41557-019-0252-7](https://doi.org/10.1038/s41557-019-0252-7)
- Ruddock, J. M. et al. Simplicity Beneath Complexity: Counting Molecular Electrons Reveals Transients and Kinetics of Photodissociation Reactions. Angewandte Chemie 131, 6437–6441 (2019) -- [10.1002/ange.201902228](https://doi.org/10.1002/ange.201902228)
- Kim, K. H. et al. Direct observation of bond formation in solution with femtosecond X-ray scattering. Nature 518, 385–389 (2015) -- [10.1038/nature14163](https://doi.org/10.1038/nature14163)
- Sharifi, M. et al. Experimental and Theoretical Investigation of High-Power Laser Ionization and Dissociation of Methane. J. Phys. Chem. A 111, 9405–9416 (2007) -- [10.1021/jp074053f](https://doi.org/10.1021/jp074053f)
- Zigo, S., Le, A.-T., Timilsina, P. & Trallero-Herrero, C. A. Ionization Study of Isomeric Molecules in Strong-field Laser Pulses. Sci Rep 7, (2017) -- [10.1038/srep42149](https://doi.org/10.1038/srep42149)
- CASIDA, M. E. Time-Dependent Density Functional Response Theory for Molecules. Recent Advances in Computational Chemistry 155–192 (1995) doi:10.1142/9789812830586_0005 -- [10.1142/9789812830586_0005](https://doi.org/10.1142/9789812830586_0005)
- Goings, J. J., Lestrange, P. J. & Li, X. Real‐time time‐dependent electronic structure theory. WIREs Comput Mol Sci 8, (2017) -- [10.1002/wcms.1341](https://doi.org/10.1002/wcms.1341)
- Ekström, U., Visscher, L., Bast, R., Thorvaldsen, A. J. & Ruud, K. Arbitrary-Order Density Functional Response Theory from Automatic Differentiation. J. Chem. Theory Comput. 6, 1971–1980 (2010) -- [10.1021/ct100117s](https://doi.org/10.1021/ct100117s)
- Zhu, Y. & Herbert, J. M. Self-consistent predictor/corrector algorithms for stable and efficient integration of the time-dependent Kohn-Sham equation. The Journal of Chemical Physics 148, (2018) -- [10.1063/1.5004675](https://doi.org/10.1063/1.5004675)
- Gómez Pueyo, A., Marques, M. A. L., Rubio, A. & Castro, A. Propagators for the Time-Dependent Kohn–Sham Equations: Multistep, Runge–Kutta, Exponential Runge–Kutta, and Commutator Free Magnus Methods. J. Chem. Theory Comput. 14, 3040–3052 (2018) -- [10.1021/acs.jctc.8b00197](https://doi.org/10.1021/acs.jctc.8b00197)
- Sun, J., Song, J., Zhao, Y. & Liang, W.-Z. Real-time propagation of the reduced one-electron density matrix in atom-centered Gaussian orbitals: Application to absorption spectra of silicon clusters. The Journal of Chemical Physics 127, (2007) -- [10.1063/1.2805396](https://doi.org/10.1063/1.2805396)
- Li, X. et al. A time-dependent Hartree–Fock approach for studying the electronic optical response of molecules in intense fields. Phys. Chem. Chem. Phys. 7, 233–239 (2005) -- [10.1039/b415849k](https://doi.org/10.1039/b415849k)
- Eshuis, H., Balint-Kurti, G. G. & Manby, F. R. Dynamics of molecules in strong oscillating electric fields using time-dependent Hartree–Fock theory. The Journal of Chemical Physics 128, (2008) -- [10.1063/1.2850415](https://doi.org/10.1063/1.2850415)
- Theilhaber, J. Ab initiosimulations of sodium using time-dependent density-functional theory. Phys. Rev. B 46, 12990–13003 (1992) -- [10.1103/physrevb.46.12990](https://doi.org/10.1103/physrevb.46.12990)
- Yabana, K. & Bertsch, G. F. Time-dependent local-density approximation in real time. Phys. Rev. B 54, 4484–4487 (1996) -- [10.1103/physrevb.54.4484](https://doi.org/10.1103/physrevb.54.4484)
- Takimoto, Y., Vila, F. D. & Rehr, J. J. Real-time time-dependent density functional theory approach for frequency-dependent nonlinear optical response in photonic molecules. The Journal of Chemical Physics 127, (2007) -- [10.1063/1.2790014](https://doi.org/10.1063/1.2790014)
- Andrade, X. et al. Real-space grids and the Octopus code as tools for the development of new simulation approaches for electronic systems. Phys. Chem. Chem. Phys. 17, 31371–31396 (2015) -- [10.1039/c5cp00351b](https://doi.org/10.1039/c5cp00351b)
- Schleife, A., Draeger, E. W., Kanai, Y. & Correa, A. A. Plane-wave pseudopotential implementation of explicit integrators for time-dependent Kohn-Sham equations in large-scale simulations. The Journal of Chemical Physics 137, (2012) -- [10.1063/1.4758792](https://doi.org/10.1063/1.4758792)
- Liang, W., Chapman, C. T. & Li, X. Efficient first-principles electronic dynamics. The Journal of Chemical Physics 134, (2011) -- [10.1063/1.3589144](https://doi.org/10.1063/1.3589144)
- Morzan, U. N. et al. Electron dynamics in complex environments with real-time time dependent density functional theory in a QM-MM framework. The Journal of Chemical Physics 140, (2014) -- [10.1063/1.4871688](https://doi.org/10.1063/1.4871688)
- Lopata, K. & Govind, N. Modeling Fast Electron Dynamics with Real-Time Time-Dependent Density Functional Theory: Application to Small Molecules and Chromophores. J. Chem. Theory Comput. 7, 1344–1355 (2011) -- [10.1021/ct200137z](https://doi.org/10.1021/ct200137z)
- Nguyen, T. S. & Parkhill, J. Nonadiabatic Dynamics for Electrons at Second-Order: Real-Time TDDFT and OSCF2. J. Chem. Theory Comput. 11, 2918–2924 (2015) -- [10.1021/acs.jctc.5b00262](https://doi.org/10.1021/acs.jctc.5b00262)
- Lopata, K., Van Kuiken, B. E., Khalil, M. & Govind, N. Linear-Response and Real-Time Time-Dependent Density Functional Theory Studies of Core-Level Near-Edge X-Ray Absorption. J. Chem. Theory Comput. 8, 3284–3292 (2012) -- [10.1021/ct3005613](https://doi.org/10.1021/ct3005613)
- Ding, F., Van Kuiken, B. E., Eichinger, B. E. & Li, X. An efficient method for calculating dynamical hyperpolarizabilities using real-time time-dependent density functional theory. The Journal of Chemical Physics 138, (2013) -- [10.1063/1.4790583](https://doi.org/10.1063/1.4790583)
- Cheng, C.-L., Evans, J. S. & Van Voorhis, T. Simulating molecular conductance using real-time density functional theory. Phys. Rev. B 74, (2006) -- [10.1103/physrevb.74.155112](https://doi.org/10.1103/physrevb.74.155112)
- Isborn, C. M. & Li, X. Singlet−Triplet Transitions in Real-Time Time-Dependent Hartree−Fock/Density Functional Theory. J. Chem. Theory Comput. 5, 2415–2419 (2009) -- [10.1021/ct900264b](https://doi.org/10.1021/ct900264b)
- Goings, J. J. & Li, X. An atomic orbital based real-time time-dependent density functional theory for computing electronic circular dichroism band spectra. The Journal of Chemical Physics 144, (2016) -- [10.1063/1.4953668](https://doi.org/10.1063/1.4953668)
- Peralta, J. E., Hod, O. & Scuseria, G. E. Magnetization Dynamics from Time-Dependent Noncollinear Spin Density Functional Theory Calculations. J. Chem. Theory Comput. 11, 3661–3668 (2015) -- [10.1021/acs.jctc.5b00494](https://doi.org/10.1021/acs.jctc.5b00494)
- Li, X., Tully, J. C., Schlegel, H. B. & Frisch, M. J. Ab initioEhrenfest dynamics. The Journal of Chemical Physics 123, (2005) -- [10.1063/1.2008258](https://doi.org/10.1063/1.2008258)
- Kolesov, G., Grånäs, O., Hoyt, R., Vinichenko, D. & Kaxiras, E. Real-Time TD-DFT with Classical Ion Dynamics: Methodology and Applications. J. Chem. Theory Comput. 12, 466–476 (2015) -- [10.1021/acs.jctc.5b00969](https://doi.org/10.1021/acs.jctc.5b00969)
- Gao, J., Liu, W., Song, B. & Liu, C. Time-dependent four-component relativistic density functional theory for excitation energies. The Journal of Chemical Physics 121, 6658–6666 (2004) -- [10.1063/1.1788655](https://doi.org/10.1063/1.1788655)
- Gao, J. et al. Time-dependent four-component relativistic density-functional theory for excitation energies. II. The exchange-correlation kernel. The Journal of Chemical Physics 123, (2005) -- [10.1063/1.1940609](https://doi.org/10.1063/1.1940609)
- Bast, R., Jensen, H. J. Aa. & Saue, T. Relativistic adiabatic time‐dependent density functional theory using hybrid functionals and noncollinear spin magnetization. Int J of Quantum Chemistry 109, 2091–2112 (2009) -- [10.1002/qua.22065](https://doi.org/10.1002/qua.22065)
- Komorovsky, S., Cherry, P. J. & Repisky, M. Four-component relativistic time-dependent density-functional theory using a stable noncollinear DFT ansatz applicable to both closed- and open-shell systems. The Journal of Chemical Physics 151, (2019) -- [10.1063/1.5121713](https://doi.org/10.1063/1.5121713)
- Wang, F., Ziegler, T., van Lenthe, E., van Gisbergen, S. & Baerends, E. J. The calculation of excitation energies based on the relativistic two-component zeroth-order regular approximation and time-dependent density-functional with full use of symmetry. The Journal of Chemical Physics 122, (2005) -- [10.1063/1.1899143](https://doi.org/10.1063/1.1899143)
- Nakata, A., Tsuneda, T. & Hirao, K. Spin-orbit relativistic long-range corrected time-dependent density functional theory for investigating spin-forbidden transitions in photochemical reactions. The Journal of Chemical Physics 135, (2011) -- [10.1063/1.3665890](https://doi.org/10.1063/1.3665890)
- Kühn, M. & Weigend, F. Implementation of Two-Component Time-Dependent Density Functional Theory in TURBOMOLE. J. Chem. Theory Comput. 9, 5341–5348 (2013) -- [10.1021/ct400743r](https://doi.org/10.1021/ct400743r)
- Repisky, M. et al. Excitation Energies from Real-Time Propagation of the Four-Component Dirac–Kohn–Sham Equation. J. Chem. Theory Comput. 11, 980–991 (2015) -- [10.1021/ct501078d](https://doi.org/10.1021/ct501078d)
- Kadek, M., Konecny, L., Gao, B., Repisky, M. & Ruud, K. X-ray absorption resonances near L2,3-edges from real-time propagation of the Dirac–Kohn–Sham density matrix. Phys. Chem. Chem. Phys. 17, 22566–22570 (2015) -- [10.1039/c5cp03712c](https://doi.org/10.1039/c5cp03712c)
- Konecny, L. et al. Acceleration of Relativistic Electron Dynamics by Means of X2C Transformation: Application to the Calculation of Nonlinear Optical Properties. J. Chem. Theory Comput. 12, 5823–5833 (2016) -- [10.1021/acs.jctc.6b00740](https://doi.org/10.1021/acs.jctc.6b00740)
- Goings, J. J., Kasper, J. M., Egidi, F., Sun, S. & Li, X. Real time propagation of the exact two component time-dependent density functional theory. The Journal of Chemical Physics 145, (2016) -- [10.1063/1.4962422](https://doi.org/10.1063/1.4962422)
- Konecny, L., Kadek, M., Komorovsky, S., Ruud, K. & Repisky, M. Resolution-of-identity accelerated relativistic two- and four-component electron dynamics approach to chiroptical spectroscopies. The Journal of Chemical Physics 149, (2018) -- [10.1063/1.5051032](https://doi.org/10.1063/1.5051032)
- Belpassi, L., Storchi, L., Quiney, H. M. & Tarantelli, F. Recent advances and perspectives in four-component Dirac–Kohn–Sham calculations. Phys. Chem. Chem. Phys. 13, 12368 (2011) -- [10.1039/c1cp20569b](https://doi.org/10.1039/c1cp20569b)
- Relativistic Quantum Theory of Atoms and Molecules. Springer Series on Atomic, Optical, and Plasma Physics (Springer New York, 2007). doi:10.1007/978-0-387-35069-1 -- [10.1007/978-0-387-35069-1](https://doi.org/10.1007/978-0-387-35069-1)
- Van Rossum G., Python reference manual (1995)
- Castro, A., Marques, M. A. L. & Rubio, A. Propagators for the time-dependent Kohn–Sham equations. The Journal of Chemical Physics 121, 3425–3433 (2004) -- [10.1063/1.1774980](https://doi.org/10.1063/1.1774980)
- Meng, S. & Kaxiras, E. Real-time, local basis-set implementation of time-dependent density functional theory for excited state dynamics simulations. The Journal of Chemical Physics 129, (2008) -- [10.1063/1.2960628](https://doi.org/10.1063/1.2960628)
- Press W. H., Numerical recipes: The art of scientific computing (2007)
- Magnus, W. On the exponential solution of differential equations for a linear operator. Comm Pure Appl Math 7, 649–673 (1954) -- [10.1002/cpa.3160070404](https://doi.org/10.1002/cpa.3160070404)
- Casas, F. & Iserles, A. Explicit Magnus expansions for nonlinear equations. J. Phys. A: Math. Gen. 39, 5445–5461 (2006) -- [10.1088/0305-4470/39/19/s07](https://doi.org/10.1088/0305-4470/39/19/s07)
- Bader, P., Blanes, S. & Kopylov, N. Exponential propagators for the Schrödinger equation with a time-dependent potential. The Journal of Chemical Physics 148, (2018) -- [10.1063/1.5036838](https://doi.org/10.1063/1.5036838)
- Bandrauk, A. D., Chelkowski, S., Diestler, D. J., Manz, J. & Yuan, K.-J. Quantum simulation of high-order harmonic spectra of the hydrogen atom. Phys. Rev. A 79, (2009) -- [10.1103/physreva.79.023403](https://doi.org/10.1103/physreva.79.023403)
- Jacob, C. R. & Reiher, M. Spin in density‐functional theory. Int J of Quantum Chemistry 112, 3661–3684 (2012) -- [10.1002/qua.24309](https://doi.org/10.1002/qua.24309)
- Merali, Z. Computational science: ...Error. Nature 467, 775–777 (2010) -- [10.1038/467775a](https://doi.org/10.1038/467775a)
- Sun, Q. et al. P<scp>y</scp>SCF: the Python‐based simulations of chemistry framework. WIREs Comput Mol Sci 8, (2017) -- [10.1002/wcms.1340](https://doi.org/10.1002/wcms.1340)
- Smith, D. G. A. et al. P<scp>si</scp>4N<scp>um</scp>P<scp>y</scp>: An Interactive Quantum Chemistry Programming Environment for Reference Implementations and Rapid Development. J. Chem. Theory Comput. 14, 3504–3511 (2018) -- [10.1021/acs.jctc.8b00286](https://doi.org/10.1021/acs.jctc.8b00286)
- Parrish, R. M. et al. <scp>Psi4</scp> 1.1: An Open-Source Electronic Structure Program Emphasizing Automation, Advanced Libraries, and Interoperability. J. Chem. Theory Comput. 13, 3185–3197 (2017) -- [10.1021/acs.jctc.7b00174](https://doi.org/10.1021/acs.jctc.7b00174)
- Quiney, H. M., Skaane, H. & Grant, I. P. Ab initio relativistic quantum chemistry: four-components good, two-components bad! Advances in Quantum Chemistry 1–49 (1998) doi:10.1016/s0065-3276(08)60405-0 -- [10.1016/s0065-3276(08)60405-0](https://doi.org/10.1016/s0065-3276(08)60405-0)
- Brainerd, W. Fortran 77. Commun. ACM 21, 806–820 (1978) -- [10.1145/359619.359621](https://doi.org/10.1145/359619.359621)
- Belpassi, L., Storchi, L., Tarantelli, F., Sgamellotti, A. & Quiney, H. M. Parallelization of a relativistic DFT code. Future Generation Computer Systems 20, 739–747 (2004) -- [10.1016/j.future.2003.11.016](https://doi.org/10.1016/j.future.2003.11.016)
- Storchi, L., Belpassi, L., Tarantelli, F., Sgamellotti, A. & Quiney, H. M. An Efficient Parallel All-Electron Four-Component Dirac−Kohn−Sham Program Using a Distributed Matrix Approach. J. Chem. Theory Comput. 6, 384–394 (2010) -- [10.1021/ct900539m](https://doi.org/10.1021/ct900539m)
- Storchi, L., Rampino, S., Belpassi, L., Tarantelli, F. & Quiney, H. M. Efficient Parallel All-Electron Four-Component Dirac–Kohn–Sham Program Using a Distributed Matrix Approach II. J. Chem. Theory Comput. 9, 5356–5364 (2013) -- [10.1021/ct400752s](https://doi.org/10.1021/ct400752s)
- Rampino, S., Belpassi, L., Tarantelli, F. & Storchi, L. Full Parallel Implementation of an All-Electron Four-Component Dirac–Kohn–Sham Program. J. Chem. Theory Comput. 10, 3766–3776 (2014) -- [10.1021/ct500498m](https://doi.org/10.1021/ct500498m)
- Metcalf, M., Reid, J., Garcia, A., McKay, S. & Christian, W. Fortran 90 Explained. Comput. Phys. 10, 135 (1996) -- [10.1063/1.4822372](https://doi.org/10.1063/1.4822372)
- De Santis, M., Rampino, S., Quiney, H. M., Belpassi, L. & Storchi, L. Charge-Displacement Analysis via Natural Orbitals for Chemical Valence in the Four-Component Relativistic Framework. J. Chem. Theory Comput. 14, 1286–1296 (2018) -- [10.1021/acs.jctc.7b01077](https://doi.org/10.1021/acs.jctc.7b01077)
- Michalak, A., Mitoraj, M. & Ziegler, T. Bond Orbitals from Chemical Valence Theory. J. Phys. Chem. A 112, 1933–1939 (2008) -- [10.1021/jp075460u](https://doi.org/10.1021/jp075460u)
- Bruner, A., LaMaster, D. & Lopata, K. Accelerated Broadband Spectra Using Transition Dipole Decomposition and Padé Approximants. J. Chem. Theory Comput. 12, 3741–3750 (2016) -- [10.1021/acs.jctc.6b00511](https://doi.org/10.1021/acs.jctc.6b00511)
- Becke, A. D. Density-functional exchange-energy approximation with correct asymptotic behavior. Phys. Rev. A 38, 3098–3100 (1988) -- [10.1103/physreva.38.3098](https://doi.org/10.1103/physreva.38.3098)
- Lee, C., Yang, W. & Parr, R. G. Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density. Phys. Rev. B 37, 785–789 (1988) -- [10.1103/physrevb.37.785](https://doi.org/10.1103/physrevb.37.785)
- Grant, I. P. & Quiney, H. M. Rayleigh-Ritz approximation of the Dirac operator in atomic and molecular physics. Phys. Rev. A 62, (2000) -- [10.1103/physreva.62.022508](https://doi.org/10.1103/physreva.62.022508)
- Valiev, M. et al. NWChem: A comprehensive and scalable open-source solution for large scale molecular simulations. Computer Physics Communications 181, 1477–1489 (2010) -- [10.1016/j.cpc.2010.04.018](https://doi.org/10.1016/j.cpc.2010.04.018)
- Wu, X. et al. Simulating Electron Dynamics in Polarizable Environments. J. Chem. Theory Comput. 13, 3985–4002 (2017) -- [10.1021/acs.jctc.7b00251](https://doi.org/10.1021/acs.jctc.7b00251)
- Belpassi, L., Tarantelli, F., Sgamellotti, A. & Quiney, H. M. Electron density fitting for the Coulomb problem in relativistic density-functional theory. The Journal of Chemical Physics 124, (2006) -- [10.1063/1.2179420](https://doi.org/10.1063/1.2179420)
- Belpassi, L., Tarantelli, F., Sgamellotti, A. & Quiney, H. M. Poisson-transformed density fitting in relativistic four-component Dirac–Kohn–Sham theory. The Journal of Chemical Physics 128, (2008) -- [10.1063/1.2868770](https://doi.org/10.1063/1.2868770)
- Belpassi, L., Tarantelli, F., Sgamellotti, A. & Quiney, H. M. All-electron four-component Dirac-Kohn-Sham procedure for large molecules and clusters containing heavy elements. Phys. Rev. B 77, (2008) -- [10.1103/physrevb.77.233403](https://doi.org/10.1103/physrevb.77.233403)
- Schuchardt, K. L. et al. Basis Set Exchange:  A Community Database for Computational Sciences. J. Chem. Inf. Model. 47, 1045–1052 (2007) -- [10.1021/ci600510j](https://doi.org/10.1021/ci600510j)
- Pritchard, B. P., Altarawy, D., Didier, B., Gibson, T. D. & Windus, T. L. New Basis Set Exchange: An Open, Up-to-Date Resource for the Molecular Sciences Community. J. Chem. Inf. Model. 59, 4814–4820 (2019) -- [10.1021/acs.jcim.9b00725](https://doi.org/10.1021/acs.jcim.9b00725)
- Slater, J. C. A Simplification of the Hartree-Fock Method. Phys. Rev. 81, 385–390 (1951) -- [10.1103/physrev.81.385](https://doi.org/10.1103/physrev.81.385)
- Vosko, S. H., Wilk, L. & Nusair, M. Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis. Can. J. Phys. 58, 1200–1211 (1980) -- [10.1139/p80-159](https://doi.org/10.1139/p80-159)
- Weigend, F. & Ahlrichs, R. Balanced basis sets of split valence, triple zeta valence and quadruple zeta valence quality for H to Rn: Design and assessment of accuracy. Phys. Chem. Chem. Phys. 7, 3297 (2005) -- [10.1039/b508541a](https://doi.org/10.1039/b508541a)
- Pritchard, B. P., Altarawy, D., Didier, B., Gibson, T. D. & Windus, T. L. New Basis Set Exchange: An Open, Up-to-Date Resource for the Molecular Sciences Community. J. Chem. Inf. Model. 59, 4814–4820 (2019) -- [10.1021/acs.jcim.9b00725](https://doi.org/10.1021/acs.jcim.9b00725)
- Dyall, K. G. Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the 4d elements Y–Cd. Theor Chem Acc 117, 483–489 (2006) -- [10.1007/s00214-006-0174-5](https://doi.org/10.1007/s00214-006-0174-5)
- Dyall, K. G. & Gomes, A. S. P. Revised relativistic basis sets for the 5d elements Hf–Hg. Theor Chem Acc 125, 97–100 (2009) -- [10.1007/s00214-009-0717-7](https://doi.org/10.1007/s00214-009-0717-7)
- Sansonetti, J. E. & Martin, W. C. Handbook of Basic Atomic Spectroscopic Data. Journal of Physical and Chemical Reference Data 34, 1559–2259 (2005) -- [10.1063/1.1800011](https://doi.org/10.1063/1.1800011)
- Liu, W. & Xiao, Y. Relativistic time-dependent density functional theories. Chem. Soc. Rev. 47, 4481–4509 (2018) -- [10.1039/c8cs00175h](https://doi.org/10.1039/c8cs00175h)
- Petrone, A., Williams-Young, D. B., Sun, S., Stetina, T. F. & Li, X. An efficient implementation of two-component relativistic density functional theory with torque-free auxiliary variables. Eur. Phys. J. B 91, (2018) -- [10.1140/epjb/e2018-90170-1](https://doi.org/10.1140/epjb/e2018-90170-1)
- Luppi, E. & Head-Gordon, M. Computation of high-harmonic generation spectra of H2and N2in intense laser pulses using quantum chemistry methods and time-dependent density functional theory. Molecular Physics 110, 909–923 (2012) -- [10.1080/00268976.2012.675448](https://doi.org/10.1080/00268976.2012.675448)
- White, A. F., Heide, C. J., Saalfrank, P., Head-Gordon, M. & Luppi, E. Computation of high-harmonic generation spectra of the hydrogen molecule using time-dependent configuration-interaction. Molecular Physics 114, 947–956 (2015) -- [10.1080/00268976.2015.1119900](https://doi.org/10.1080/00268976.2015.1119900)
- Labeye, M. et al. Optimal Basis Set for Electron Dynamics in Strong Laser Fields: The case of Molecular Ion H2+. J. Chem. Theory Comput. 14, 5846–5858 (2018) -- [10.1021/acs.jctc.8b00656](https://doi.org/10.1021/acs.jctc.8b00656)
- Lewenstein, M., Balcou, Ph., Ivanov, M. Yu., L’Huillier, A. & Corkum, P. B. Theory of high-harmonic generation by low-frequency laser fields. Phys. Rev. A 49, 2117–2132 (1994) -- [10.1103/physreva.49.2117](https://doi.org/10.1103/physreva.49.2117)
- Bishea, G. A. & Morse, M. D. Spectroscopic studies of jet-cooled AgAu and Au2. The Journal of Chemical Physics 95, 5646–5659 (1991) -- [10.1063/1.461639](https://doi.org/10.1063/1.461639)
- Wesolowski, T. A. & Warshel, A. Frozen density functional approach for ab initio calculations of solvated molecules. J. Phys. Chem. 97, 8050–8053 (1993) -- [10.1021/j100132a040](https://doi.org/10.1021/j100132a040)
- Jacob, C. R., Neugebauer, J. & Visscher, L. A flexible implementation of frozen‐density embedding for use in multilevel simulations. J Comput Chem 29, 1011–1018 (2007) -- [10.1002/jcc.20861](https://doi.org/10.1002/jcc.20861)
- Krishtal, A., Ceresoli, D. & Pavanello, M. Subsystem real-time time dependent density functional theory. The Journal of Chemical Physics 142, (2015) -- [10.1063/1.4918276](https://doi.org/10.1063/1.4918276)

