---
title: "An extensible interface for QM/MM molecular dynamics simulations with AMBER"
date: 2013-10-12 00:00:00 +0100
permalink: an-extensible-interface-for-qm-mm-molecular-dynamics-simulations-with-amber
year: 2014
authors: Andreas W. Götz, Matthew A. Clark, Ross C. Walker
category: articles
---
 
## Authors
[Andreas W. Götz](authors/andreas-w-gotz), [Matthew A. Clark](authors/matthew-a-clark), [Ross C. Walker](authors/ross-c-walker)
 
## Abstract
We present an extensible interface between the AMBER molecular dynamics (MD) software package and electronic structure software packages for quantum mechanical (QM) and mixed QM and classical molecular mechanical (MM) MD simulations within both mechanical and electronic embedding schemes. With this interface, ab initio wave function theory and density functional theory methods, as available in the supported electronic structure software packages, become available for QM/MM MD simulations with AMBER. The interface has been written in a modular fashion that allows straight forward extensions to support additional QM software packages and can easily be ported to other MD software. Data exchange between the MD and QM software is implemented by means of files and system calls or the message passing interface standard. Based on extensive tests, default settings for the supported QM packages are provided such that energy is conserved for typical QM/MM MD simulations in the microcanonical ensemble. Results for the free energy of binding of calcium ions to aspartate in aqueous solution comparing semiempirical and density functional Hamiltonians are shown to demonstrate features of this interface. © 2013 Wiley Periodicals, Inc.
 
## Citation
- **Journal:** Journal of Computational Chemistry
- **Year:** 2014
- **Volume:** 35
- **Issue:** 2
- **Pages:** 95--108
- **Publisher:** Wiley
- **DOI:** [10.1002/jcc.23444](https://doi.org/10.1002/jcc.23444)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{G_tz_2013,
  title={{An extensible interface for QM/MM molecular dynamics simulations with AMBER}},
  volume={35},
  ISSN={1096-987X},
  DOI={10.1002/jcc.23444},
  number={2},
  journal={Journal of Computational Chemistry},
  publisher={Wiley},
  author={Götz, Andreas W. and Clark, Matthew A. and Walker, Ross C.},
  year={2013},
  pages={95--108}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/an-extensible-interface-for-qm-mm-molecular-dynamics-simulations-with-amber.bib)
 
## References
- Warshel, A. & Levitt, M. Theoretical studies of enzymic reactions: Dielectric, electrostatic and steric stabilization of the carbonium ion in the reaction of lysozyme. Journal of Molecular Biology 103, 227–249 (1976) -- [10.1016/0022-2836(76)90311-9](https://doi.org/10.1016/0022-2836(76)90311-9)
- Singh, U. C. & Kollman, P. A. A combined ab initio quantum mechanical and molecular mechanical method for carrying out simulations on complex molecular systems: Applications to the CH3Cl + Cl− exchange reaction and gas phase protonation of polyethers. J Comput Chem 7, 718–730 (1986) -- [10.1002/jcc.540070604](https://doi.org/10.1002/jcc.540070604)
- Field, M. J., Bash, P. A. & Karplus, M. A combined quantum mechanical and molecular mechanical potential for molecular dynamics simulations. J Comput Chem 11, 700–733 (1990) -- [10.1002/jcc.540110605](https://doi.org/10.1002/jcc.540110605)
- Bakowies, D. & Thiel, W. Hybrid Models for Combined Quantum Mechanical and Molecular Mechanical Approaches. J. Phys. Chem. 100, 10580–10594 (1996) -- [10.1021/jp9536514](https://doi.org/10.1021/jp9536514)
- Sherwood P., Modern Methods and Algorithms of Quantum Chemistry Proceedings, Vol. 3 of NIC Series (2000)
- Gao, J. & Truhlar, D. G. Q<scp>UANTUM</scp>M<scp>ECHANICAL</scp>M<scp>ETHODS FOR</scp>E<scp>NZYME</scp>K<scp>INETICS</scp>. Annu. Rev. Phys. Chem. 53, 467–505 (2002) -- [10.1146/annurev.physchem.53.091301.150114](https://doi.org/10.1146/annurev.physchem.53.091301.150114)
- Friesner, R. A. & Guallar, V. AB INITIO QUANTUM CHEMICAL AND MIXED QUANTUM MECHANICS/MOLECULAR MECHANICS (QM/MM) METHODS FOR STUDYING ENZYMATIC CATALYSIS. Annu. Rev. Phys. Chem. 56, 389–427 (2005) -- [10.1146/annurev.physchem.55.091602.094410](https://doi.org/10.1146/annurev.physchem.55.091602.094410)
- Lin, H. & Truhlar, D. G. QM/MM: what have we learned, where are we, and where do we go from here? Theor Chem Acc 117, (2006) -- [10.1007/s00214-006-0143-z](https://doi.org/10.1007/s00214-006-0143-z)
- Thiel W., Multiscale Simulation Methods in Molecular Sciences, Vol. 42 of NIC series (2009)
- Senn, H. M. & Thiel, W. QM/MM Methods for Biomolecular Systems. Angew Chem Int Ed 48, 1198–1229 (2009) -- [10.1002/anie.200802019](https://doi.org/10.1002/anie.200802019)
- Bernstein, N., Kermode, J. R. & Csányi, G. Hybrid atomistic simulation methods for materials systems. Rep. Prog. Phys. 72, 026501 (2009) -- [10.1088/0034-4885/72/2/026501](https://doi.org/10.1088/0034-4885/72/2/026501)
- Zhang R., Advances in Quantum Chemistry (2010)
- Sousa, S. F., Fernandes, P. A. & Ramos, M. J. Computational enzymatic catalysis – clarifying enzymatic mechanisms with the help of computers. Phys. Chem. Chem. Phys. 14, 12431 (2012) -- [10.1039/c2cp41180f](https://doi.org/10.1039/c2cp41180f)
- Case D. A., Amber 12 (2012)
- Salomon‐Ferrer, R., Case, D. A. & Walker, R. C. An overview of the Amber biomolecular simulation package. WIREs Comput Mol Sci 3, 198–210 (2012) -- [10.1002/wcms.1121](https://doi.org/10.1002/wcms.1121)
- Walker, R. C., Crowley, M. F. & Case, D. A. The implementation of a fast and accurate QM/MM potential method in Amber. J Comput Chem 29, 1019–1031 (2007) -- [10.1002/jcc.20857](https://doi.org/10.1002/jcc.20857)
- Seabra, G. de M., Walker, R. C., Elstner, M., Case, D. A. & Roitberg, A. E. Implementation of the SCC-DFTB Method for Hybrid QM/MM Simulations within the Amber Molecular Dynamics Package. J. Phys. Chem. A 111, 5655–5664 (2007) -- [10.1021/jp070071l](https://doi.org/10.1021/jp070071l)
- Rossi, I. & Truhlar, D. G. Parameterization of NDDO wavefunctions using genetic algorithms. An evolutionary approach to parameterizing potential energy surfaces and direct dynamics calculations for organic reactions. Chemical Physics Letters 233, 231–236 (1995) -- [10.1016/0009-2614(94)01450-a](https://doi.org/10.1016/0009-2614(94)01450-a)
- Nam, K., Cui, Q., Gao, J. & York, D. M. Specific Reaction Parametrization of the AM1/d Hamiltonian for Phosphoryl Transfer Reactions:  H, O, and P Atoms. J. Chem. Theory Comput. 3, 486–504 (2007) -- [10.1021/ct6002466](https://doi.org/10.1021/ct6002466)
- Wei, D. & Salahub, D. R. A combined density functional and molecular dynamics simulation of a quantum water molecule in aqueous solution. Chemical Physics Letters 224, 291–296 (1994) -- [10.1016/0009-2614(94)00540-0](https://doi.org/10.1016/0009-2614(94)00540-0)
- Stanton, R. V., Little, L. R. & Merz, K. M., Jr. An Examination of a Hartree-Fock/Molecular Mechanical Coupled Potential. J. Phys. Chem. 99, 17344–17348 (1995) -- [10.1021/j100048a006](https://doi.org/10.1021/j100048a006)
- Stanton, R. V., Hartsough, D. S. & Merz, K. M., Jr. An examination of a density functional/molecular mechanical coupled potential. J Comput Chem 16, 113–128 (1995) -- [10.1002/jcc.540160110](https://doi.org/10.1002/jcc.540160110)
- Ryde, U. The coordination of the catalytic zinc ion in alcohol dehydrogenase studied by combined quantum-chemical and molecular mechanics calculations. J Computer-Aided Mol Des 10, 153–164 (1996) -- [10.1007/bf00402823](https://doi.org/10.1007/bf00402823)
- Lyne, P. D., Hodoscek, M. & Karplus, M. A Hybrid QM−MM Potential Employing Hartree−Fock or Density Functional Methods in the Quantum Region. J. Phys. Chem. A 103, 3462–3471 (1999) -- [10.1021/jp982115j](https://doi.org/10.1021/jp982115j)
- Eichinger, M., Tavan, P., Hutter, J. & Parrinello, M. A hybrid method for solutes in complex solvents: Density functional theory combined with empirical force fields. The Journal of Chemical Physics 110, 10452–10467 (1999) -- [10.1063/1.479049](https://doi.org/10.1063/1.479049)
- Laio, A., VandeVondele, J. & Rothlisberger, U. A Hamiltonian electrostatic coupling scheme for hybrid Car–Parrinello molecular dynamics simulations. The Journal of Chemical Physics 116, 6941–6947 (2002) -- [10.1063/1.1462041](https://doi.org/10.1063/1.1462041)
- Loferer, M. J., Loeffler, H. H. & Liedl, K. R. A QM–MM interface between CHARMM and TURBOMOLE: Implementation and application to systems in bulk phase and biologically active systems. J Comput Chem 24, 1240–1249 (2003) -- [10.1002/jcc.10283](https://doi.org/10.1002/jcc.10283)
- Biswas, P. K. & Gogonea, V. A regularized and renormalized electrostatic coupling Hamiltonian for hybrid quantum-mechanical–molecular-mechanical calculations. The Journal of Chemical Physics 123, (2005) -- [10.1063/1.2064907](https://doi.org/10.1063/1.2064907)
- Woodcock, H. L., III et al. Interfacing Q‐Chem and CHARMM to perform QM/MM reaction path calculations. J Comput Chem 28, 1485–1502 (2007) -- [10.1002/jcc.20587](https://doi.org/10.1002/jcc.20587)
- Lev, B., Zhang, R., de la Lande, A., Salahub, D. & Noskov, S. Y. The QM‐MM interface for CHARMM‐deMon. J Comput Chem 31, 1015–1023 (2009) -- [10.1002/jcc.21387](https://doi.org/10.1002/jcc.21387)
- Okamoto, T. et al. A minimal implementation of the AMBER–GAUSSIAN interface for ab initio QM/MM‐MD simulation. J Comput Chem 32, 932–942 (2010) -- [10.1002/jcc.21678](https://doi.org/10.1002/jcc.21678)
- Meier, K., Schmid, N. & van Gunsteren, W. F. Interfacing the GROMOS (bio)molecular simulation software to quantum‐chemical program packages. J Comput Chem 33, 2108–2117 (2012) -- [10.1002/jcc.23047](https://doi.org/10.1002/jcc.23047)
- Torras, J., Deumens, E. & Trickey, S. B. Software Integration in Multi-scale Simulations: the PUPIL System. J Computer-Aided Mater Des 13, 201–212 (2006) -- [10.1007/s10820-006-9011-3](https://doi.org/10.1007/s10820-006-9011-3)
- Sherwood, P. et al. QUASI: A general purpose implementation of the QM/MM approach and its application to problems in catalysis. Journal of Molecular Structure: THEOCHEM 632, 1–28 (2003) -- [10.1016/s0166-1280(03)00285-9](https://doi.org/10.1016/s0166-1280(03)00285-9)
- Stewart, J. J. P. Optimization of parameters for semiempirical methods V: Modification of NDDO approximations and application to 70 elements. J Mol Model 13, 1173–1213 (2007) -- [10.1007/s00894-007-0233-4](https://doi.org/10.1007/s00894-007-0233-4)
- Hu, L., Söderhjelm, P. & Ryde, U. On the Convergence of QM/MM Energies. J. Chem. Theory Comput. 7, 761–777 (2011) -- [10.1021/ct100530r](https://doi.org/10.1021/ct100530r)
- Ufimtsev, I. S. & Martinez, T. J. Quantum Chemistry on Graphical Processing Units. 2. Direct Self-Consistent-Field Implementation. J. Chem. Theory Comput. 5, 1004–1015 (2009) -- [10.1021/ct800526s](https://doi.org/10.1021/ct800526s)
- Ufimtsev, I. S. & Martinez, T. J. Quantum Chemistry on Graphical Processing Units. 3. Analytical Energy Gradients, Geometry Optimization, and First Principles Molecular Dynamics. J. Chem. Theory Comput. 5, 2619–2628 (2009) -- [10.1021/ct9003004](https://doi.org/10.1021/ct9003004)
- Isborn, C. M., Götz, A. W., Clark, M. A., Walker, R. C. & Martínez, T. J. Electronic Absorption Spectra from MM and ab Initio QM/MM Molecular Dynamics: Environmental Effects on the Absorption Spectrum of Photoactive Yellow Protein. J. Chem. Theory Comput. 8, 5092–5106 (2012) -- [10.1021/ct3006826](https://doi.org/10.1021/ct3006826)
- Park, K., Götz, A. W., Walker, R. C. & Paesani, F. Application of Adaptive QM/MM Methods to Molecular Dynamics Simulations of Aqueous Systems. J. Chem. Theory Comput. 8, 2868–2877 (2012) -- [10.1021/ct300331f](https://doi.org/10.1021/ct300331f)
- te Velde, G. et al. Chemistry with ADF. J Comput Chem 22, 931–967 (2001) -- [10.1002/jcc.1056](https://doi.org/10.1002/jcc.1056)
- Fonseca Guerra, C., Snijders, J. G., te Velde, G. & Baerends, E. J. Towards an order-. Theor Chem Acc 99, 391 (1998) -- [10.1007/s002140050021](https://doi.org/10.1007/s002140050021)
- ADF2012, SCM, Theoretical Chemistry
- Schmidt, M. W. et al. General atomic and molecular electronic structure system. J Comput Chem 14, 1347–1363 (1993) -- [10.1002/jcc.540141112](https://doi.org/10.1002/jcc.540141112)
- Gordon, M. S. & Schmidt, M. W. Advances in electronic structure theory. Theory and Applications of Computational Chemistry 1167–1189 (2005) doi:10.1016/b978-044451719-7/50084-6 -- [10.1016/b978-044451719-7/50084-6](https://doi.org/10.1016/b978-044451719-7/50084-6)
- Valiev, M. et al. NWChem: A comprehensive and scalable open-source solution for large scale molecular simulations. Computer Physics Communications 181, 1477–1489 (2010) -- [10.1016/j.cpc.2010.04.018](https://doi.org/10.1016/j.cpc.2010.04.018)
- Frisch M. J., Gaussian 09, Revision C.01 (2010)
- Neese, F. The ORCA program system. WIREs Comput Mol Sci 2, 73–78 (2011) -- [10.1002/wcms.81](https://doi.org/10.1002/wcms.81)
- Shao, Y. et al. Advances in methods and algorithms in a modern quantum chemistry program package. Phys. Chem. Chem. Phys. 8, 3172–3191 (2006) -- [10.1039/b517914a](https://doi.org/10.1039/b517914a)
- Still, W. C., Tempczyk, A., Hawley, R. C. & Hendrickson, T. Semianalytical treatment of solvation for molecular mechanics and dynamics. J. Am. Chem. Soc. 112, 6127–6129 (1990) -- [10.1021/ja00172a038](https://doi.org/10.1021/ja00172a038)
- Pellegrini, E. & Field, M. J. A Generalized-Born Solvation Model for Macromolecular Hybrid-Potential Calculations. J. Phys. Chem. A 106, 1316–1326 (2002) -- [10.1021/jp0135050](https://doi.org/10.1021/jp0135050)
- Darden, T., York, D. & Pedersen, L. Particle mesh Ewald: An N⋅log(N) method for Ewald sums in large systems. The Journal of Chemical Physics 98, 10089–10092 (1993) -- [10.1063/1.464397](https://doi.org/10.1063/1.464397)
- Nam, K., Gao, J. & York, D. M. An Efficient Linear-Scaling Ewald Method for Long-Range Electrostatic Interactions in Combined QM/MM Calculations. J. Chem. Theory Comput. 1, 2–13 (2004) -- [10.1021/ct049941i](https://doi.org/10.1021/ct049941i)
- Roux, B. The calculation of the potential of mean force using computer simulations. Computer Physics Communications 91, 275–282 (1995) -- [10.1016/0010-4655(95)00053-i](https://doi.org/10.1016/0010-4655(95)00053-i)
- Kästner, J. Umbrella sampling. WIREs Comput Mol Sci 1, 932–942 (2011) -- [10.1002/wcms.66](https://doi.org/10.1002/wcms.66)
- Mitsutake, A., Sugita, Y. & Okamoto, Y. Generalized-ensemble algorithms for molecular simulations of biopolymers. Biopolymers 60, 96–123 (2001) -- [10.1002/1097-0282(2001)60:2<96::aid-bip1007>3.0.co;2-f](https://doi.org/10.1002/1097-0282(2001)60:2<96::aid-bip1007>3.0.co;2-f)
- Nymeyer, H., Gnanakaran, S. & García, A. E. Atomic Simulations of Protein Folding, Using the Replica Exchange Algorithm. Methods in Enzymology 119–149 (2004) doi:10.1016/s0076-6879(04)83006-4 -- [10.1016/s0076-6879(04)83006-4](https://doi.org/10.1016/s0076-6879(04)83006-4)
- Ceperley, D. M. Path integrals in the theory of condensed helium. Rev. Mod. Phys. 67, 279–355 (1995) -- [10.1103/revmodphys.67.279](https://doi.org/10.1103/revmodphys.67.279)
- Berne, B. J. & Thirumalai, D. On the Simulation of Quantum Systems: Path Integral Methods. Annu. Rev. Phys. Chem. 37, 401–424 (1986) -- [10.1146/annurev.pc.37.100186.002153](https://doi.org/10.1146/annurev.pc.37.100186.002153)
- Pulay, P. & Fogarasi, G. Fock matrix dynamics. Chemical Physics Letters 386, 272–278 (2004) -- [10.1016/j.cplett.2004.01.069](https://doi.org/10.1016/j.cplett.2004.01.069)
- Herbert, J. M. & Head-Gordon, M. Accelerated, energy-conserving Born–Oppenheimer molecular dynamics via Fock matrix extrapolation. Phys. Chem. Chem. Phys. 7, 3269 (2005) -- [10.1039/b509494a](https://doi.org/10.1039/b509494a)
- Dewar, M. J. S. & Thiel, W. Ground states of molecules. 38. The MNDO method. Approximations and parameters. J. Am. Chem. Soc. 99, 4899–4907 (1977) -- [10.1021/ja00457a004](https://doi.org/10.1021/ja00457a004)
- Stewart, J. J. P. Optimization of parameters for semiempirical methods I. Method. J Comput Chem 10, 209–220 (1989) -- [10.1002/jcc.540100208](https://doi.org/10.1002/jcc.540100208)
- Becke, A. D. Density-functional exchange-energy approximation with correct asymptotic behavior. Phys. Rev. A 38, 3098–3100 (1988) -- [10.1103/physreva.38.3098](https://doi.org/10.1103/physreva.38.3098)
- Perdew, J. P. Density-functional approximation for the correlation energy of the inhomogeneous electron gas. Phys. Rev. B 33, 8822–8824 (1986) -- [10.1103/physrevb.33.8822](https://doi.org/10.1103/physrevb.33.8822)
- Lee, C., Yang, W. & Parr, R. G. Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density. Phys. Rev. B 37, 785–789 (1988) -- [10.1103/physrevb.37.785](https://doi.org/10.1103/physrevb.37.785)
- Becke, A. D. Density-functional thermochemistry. III. The role of exact exchange. The Journal of Chemical Physics 98, 5648–5652 (1993) -- [10.1063/1.464913](https://doi.org/10.1063/1.464913)
- Hehre, W. J., Ditchfield, R. & Pople, J. A. Self—Consistent Molecular Orbital Methods. XII. Further Extensions of Gaussian—Type Basis Sets for Use in Molecular Orbital Studies of Organic Molecules. The Journal of Chemical Physics 56, 2257–2261 (1972) -- [10.1063/1.1677527](https://doi.org/10.1063/1.1677527)
- Hariharan, P. C. & Pople, J. A. The influence of polarization functions on molecular orbital hydrogenation energies. Theoret. Chim. Acta 28, 213–222 (1973) -- [10.1007/bf00533485](https://doi.org/10.1007/bf00533485)
- Krishnan, R., Binkley, J. S., Seeger, R. & Pople, J. A. Self-consistent molecular orbital methods. XX. A basis set for correlated wave functions. The Journal of Chemical Physics 72, 650–654 (1980) -- [10.1063/1.438955](https://doi.org/10.1063/1.438955)
- Schäfer, A., Huber, C. & Ahlrichs, R. Fully optimized contracted Gaussian basis sets of triple zeta valence quality for atoms Li to Kr. The Journal of Chemical Physics 100, 5829–5835 (1994) -- [10.1063/1.467146](https://doi.org/10.1063/1.467146)
- Dunning, T. H., Jr. Gaussian basis sets for use in correlated molecular calculations. I. The atoms boron through neon and hydrogen. The Journal of Chemical Physics 90, 1007–1023 (1989) -- [10.1063/1.456153](https://doi.org/10.1063/1.456153)
- Kendall, R. A., Dunning, T. H., Jr. & Harrison, R. J. Electron affinities of the first-row atoms revisited. Systematic basis sets and wave functions. The Journal of Chemical Physics 96, 6796–6806 (1992) -- [10.1063/1.462569](https://doi.org/10.1063/1.462569)
- Jorgensen, W. L., Chandrasekhar, J., Madura, J. D., Impey, R. W. & Klein, M. L. Comparison of simple potential functions for simulating liquid water. The Journal of Chemical Physics 79, 926–935 (1983) -- [10.1063/1.445869](https://doi.org/10.1063/1.445869)
- Berendsen H. J. C., Interaction Models for Water in Relation to Protein Hydration (1981)
- Wu, Y., Tepper, H. L. & Voth, G. A. Flexible simple point-charge water model with improved liquid-state properties. The Journal of Chemical Physics 124, (2006) -- [10.1063/1.2136877](https://doi.org/10.1063/1.2136877)
- Hornak, V. et al. Comparison of multiple Amber force fields and development of improved protein backbone parameters. Proteins 65, 712–725 (2006) -- [10.1002/prot.21123](https://doi.org/10.1002/prot.21123)
- Grest, G. S. & Kremer, K. Molecular dynamics simulation for polymers in the presence of a heat bath. Phys. Rev. A 33, 3628–3631 (1986) -- [10.1103/physreva.33.3628](https://doi.org/10.1103/physreva.33.3628)
- Ryckaert, J.-P., Ciccotti, G. & Berendsen, H. J. C. Numerical integration of the cartesian equations of motion of a system with constraints: molecular dynamics of n-alkanes. Journal of Computational Physics 23, 327–341 (1977) -- [10.1016/0021-9991(77)90098-5](https://doi.org/10.1016/0021-9991(77)90098-5)
- Miyamoto, S. & Kollman, P. A. Settle: An analytical version of the SHAKE and RATTLE algorithm for rigid water models. J Comput Chem 13, 952–962 (1992) -- [10.1002/jcc.540130805](https://doi.org/10.1002/jcc.540130805)
- Berendsen, H. J. C., Postma, J. P. M., van Gunsteren, W. F., DiNola, A. & Haak, J. R. Molecular dynamics with coupling to an external bath. The Journal of Chemical Physics 81, 3684–3690 (1984) -- [10.1063/1.448118](https://doi.org/10.1063/1.448118)
- Kumar, S., Rosenberg, J. M., Bouzida, D., Swendsen, R. H. & Kollman, P. A. THE weighted histogram analysis method for free‐energy calculations on biomolecules. I. The method. J Comput Chem 13, 1011–1021 (1992) -- [10.1002/jcc.540130812](https://doi.org/10.1002/jcc.540130812)
- Humphrey, W., Dalke, A. & Schulten, K. VMD: Visual molecular dynamics. Journal of Molecular Graphics 14, 33–38 (1996) -- [10.1016/0263-7855(96)00018-5](https://doi.org/10.1016/0263-7855(96)00018-5)
- Dyke, T. R. & Muenter, J. S. Microwave spectrum and structure of hydrogen bonded water dimer. The Journal of Chemical Physics 60, 2929–2930 (1974) -- [10.1063/1.1681463](https://doi.org/10.1063/1.1681463)
- Curtiss, L. A., Frurip, D. J. & Blander, M. Studies of molecular association in H2O and D2O vapors by measurement of thermal conductivity. The Journal of Chemical Physics 71, 2703–2711 (1979) -- [10.1063/1.438628](https://doi.org/10.1063/1.438628)
- Kim, K. S., Mhin, B. J., Choi, U.-S. & Lee, K. Ab initio studies of the water dimer using large basis sets: The structure and thermodynamic energies. The Journal of Chemical Physics 97, 6649–6662 (1992) -- [10.1063/1.463669](https://doi.org/10.1063/1.463669)
- Liao, J. et al. Structural Insight into the Ion-Exchange Mechanism of the Sodium/Calcium Exchanger. Science 335, 686–690 (2012) -- [10.1126/science.1215759](https://doi.org/10.1126/science.1215759)
- Bulo, R. E. et al. “Site Binding” of Ca2+Ions to Polyacrylates in Water:  A Molecular Dynamics Study of Coiling and Aggregation. Macromolecules 40, 3437–3442 (2007) -- [10.1021/ma062467l](https://doi.org/10.1021/ma062467l)
- Tu, Y. & Laaksonen, A. On the effect of Lennard-Jones parameters on the quantum mechanical and molecular mechanical coupling in a hybrid molecular dynamics simulation of liquid water. The Journal of Chemical Physics 111, 7519–7525 (1999) -- [10.1063/1.480078](https://doi.org/10.1063/1.480078)
- Riccardi, D., Li, G. & Cui, Q. Importance of van der Waals Interactions in QM/MM Simulations. J. Phys. Chem. B 108, 6467–6478 (2004) -- [10.1021/jp037992q](https://doi.org/10.1021/jp037992q)
- Bulo, R. E., Ensing, B., Sikkema, J. & Visscher, L. Toward a Practical Method for Adaptive QM/MM Simulations. J. Chem. Theory Comput. 5, 2212–2221 (2009) -- [10.1021/ct900148e](https://doi.org/10.1021/ct900148e)

