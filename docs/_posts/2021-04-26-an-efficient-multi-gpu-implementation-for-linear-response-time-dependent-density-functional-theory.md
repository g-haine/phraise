---
layout: post
title: "An Efficient Multi-GPU Implementation for Linear-Response Time-Dependent Density Functional Theory"
date: 2021-04-26 00:00:00 +0100
permalink: an-efficient-multi-gpu-implementation-for-linear-response-time-dependent-density-functional-theory
year: 2020
authors: Qingcai Jiang, Lingyun Wan, Shizhe Jiao, Wei Hu, Junshi Chen, Hong An
category: proceedings
---
 
## Authors
[Qingcai Jiang](authors/qingcai-jiang), [Lingyun Wan](authors/lingyun-wan), [Shizhe Jiao](authors/shizhe-jiao), [Wei Hu](authors/wei-hu), [Junshi Chen](authors/junshi-chen), [Hong An](authors/hong-an)
 
## Abstract
Nowadays, Kohn-Sham density functional theory (DFT) calculation has drawn more and more attention in chemistry and material science simulations. However, due to the extreme large Hamiltonian matrix needed to be generated during the calculation, when the studied system increases, the cost of calculation becomes unbearable both in ground and excited state electronic structure simulations with large uniform basis. In this paper, we propose a high-performance multi-GPU approach for linear-response time-dependent density functional theory (LR-TDDFT) calculation to compute the excitation energies in molecules and solids with the plane wave basis set under the periodic boundary condition. We carefully design the parallel implementation, calculation steps and data distribution schemes in the naïve CPU implementation to maintain good scalability when the studied system expands, then port the most time-consuming part to multi-GPU platform along with several effective optimization steps. The results show that with dual V100 GPUs, the proposed approach can achieve an average of 6.68x speedup compared with dual 12-core Xeon CPU with bulk silicon systems that comprises thousands of atoms (1,024 atoms).
 
## Citation
- **Journal:** 2020 IEEE 22nd International Conference on High Performance Computing and Communications; IEEE 18th International Conference on Smart City; IEEE 6th International Conference on Data Science and Systems (HPCC/SmartCity/DSS)
- **Year:** 2020
- **Volume:** 
- **Issue:** 
- **Pages:** 197--205
- **Publisher:** IEEE
- **DOI:** [10.1109/hpcc-smartcity-dss50907.2020.00025](https://doi.org/10.1109/hpcc-smartcity-dss50907.2020.00025)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Jiang_2020,
  title={{An Efficient Multi-GPU Implementation for Linear-Response Time-Dependent Density Functional Theory}},
  DOI={10.1109/hpcc-smartcity-dss50907.2020.00025},
  booktitle={{2020 IEEE 22nd International Conference on High Performance Computing and Communications; IEEE 18th International Conference on Smart City; IEEE 6th International Conference on Data Science and Systems (HPCC/SmartCity/DSS)}},
  publisher={IEEE},
  author={Jiang, Qingcai and Wan, Lingyun and Jiao, Shizhe and Hu, Wei and Chen, Junshi and An, Hong},
  year={2020},
  pages={197--205}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/an-efficient-multi-gpu-implementation-for-linear-response-time-dependent-density-functional-theory.bib)
 
## References
- Strinati, G. Application of the Green’s functions method to the study of the optical properties of semiconductors. Riv. Nuovo Cim. 11, 1–86 (1988) -- [10.1007/bf02725962](https://doi.org/10.1007/bf02725962)
- Fu, H. et al. The Sunway TaihuLight supercomputer: system and applications. Sci. China Inf. Sci. 59, (2016) -- [10.1007/s11432-016-5588-7](https://doi.org/10.1007/s11432-016-5588-7)
- Kohn, W. & Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. Phys. Rev. 140, A1133–A1138 (1965) -- [10.1103/physrev.140.a1133](https://doi.org/10.1103/physrev.140.a1133)
- fetter, Quantum theory of many-particle systems. qtmp (1971)
- khatri, Solutions to some functional equations and their applications to characterization of probability distributions. Sankhya The Indian Journal of Statistics Series A (1968)
- Goedecker, S., Teter, M. & Hutter, J. Separable dual-space Gaussian pseudopotentials. Phys. Rev. B 54, 1703–1710 (1996) -- [10.1103/physrevb.54.1703](https://doi.org/10.1103/physrevb.54.1703)
- Hu, W., Lin, L., Banerjee, A. S., Vecharynski, E. & Yang, C. Adaptively Compressed Exchange Operator for Large-Scale Hybrid Density Functional Calculations with Applications to the Adsorption of Water on Silicene. J. Chem. Theory Comput. 13, 1188–1198 (2017) -- [10.1021/acs.jctc.6b01184](https://doi.org/10.1021/acs.jctc.6b01184)
- Hu, W., Lin, L. & Yang, C. DGDFT: A massively parallel method for large scale density functional theory calculations. The Journal of Chemical Physics 143, (2015) -- [10.1063/1.4931732](https://doi.org/10.1063/1.4931732)
- Lin, L., Lu, J., Ying, L. & E, W. Adaptive local basis set for Kohn–Sham density functional theory in a discontinuous Galerkin framework I: Total energy calculation. Journal of Computational Physics 231, 2140–2154 (2012) -- [10.1016/j.jcp.2011.11.032](https://doi.org/10.1016/j.jcp.2011.11.032)
- Nvidia dgx-1 with teslav100 system architecture (0)
- Gonze, X. et al. Recent developments in the ABINIT software package. Computer Physics Communications 205, 106–131 (2016) -- [10.1016/j.cpc.2016.04.003](https://doi.org/10.1016/j.cpc.2016.04.003)
- Ratcliff, L. E., Degomme, A., Flores-Livas, J. A., Goedecker, S. & Genovese, L. Affordable and accurate large-scale hybrid-functional calculations on GPU-accelerated supercomputers. J. Phys.: Condens. Matter 30, 095901 (2018) -- [10.1088/1361-648x/aaa8c9](https://doi.org/10.1088/1361-648x/aaa8c9)
- Shao, Y. et al. Advances in molecular quantum chemistry contained in the Q-Chem 4 program package. Molecular Physics 113, 184–215 (2014) -- [10.1080/00268976.2014.952696](https://doi.org/10.1080/00268976.2014.952696)
- Yabana, K. & Bertsch, G. F. Time-dependent local-density approximation in real time. Phys. Rev. B 54, 4484–4487 (1996) -- [10.1103/physrevb.54.4484](https://doi.org/10.1103/physrevb.54.4484)
- Deslippe, J. et al. BerkeleyGW: A massively parallel computer package for the calculation of the quasiparticle and optical properties of materials and nanostructures. Computer Physics Communications 183, 1269–1289 (2012) -- [10.1016/j.cpc.2011.12.006](https://doi.org/10.1016/j.cpc.2011.12.006)
- Ullrich, C. A. Time-Dependent Density-Functional Theory. (2011) doi:10.1093/acprof:oso/9780199563029.001.0001 -- [10.1093/acprof:oso/9780199563029.001.0001](https://doi.org/10.1093/acprof:oso/9780199563029.001.0001)
- Onida, G., Reining, L. & Rubio, A. Electronic excitations: density-functional versus many-body Green’s-function approaches. Rev. Mod. Phys. 74, 601–659 (2002) -- [10.1103/revmodphys.74.601](https://doi.org/10.1103/revmodphys.74.601)
- Jia, W., Wang, L.-W. & Lin, L. Parallel transport time-dependent density functional theory calculations with hybrid functional on summit. Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis 1–23 (2019) doi:10.1145/3295500.3356144 -- [10.1145/3295500.3356144](https://doi.org/10.1145/3295500.3356144)
- Beck, T. L. Real-space mesh techniques in density-functional theory. Rev. Mod. Phys. 72, 1041–1080 (2000) -- [10.1103/revmodphys.72.1041](https://doi.org/10.1103/revmodphys.72.1041)
- Sternheimer, R. M. Electronic Polarizabilities of Ions from the Hartree-Fock Wave Functions. Phys. Rev. 96, 951–968 (1954) -- [10.1103/physrev.96.951](https://doi.org/10.1103/physrev.96.951)
- casida, Recent advances in density functional methods. Computational Chemistry Reviews of Current Trends (1995)
- Andrade, X. et al. Time-dependent density-functional theory in massively parallel computer architectures: the octopus project. J. Phys.: Condens. Matter 24, 233202 (2012) -- [10.1088/0953-8984/24/23/233202](https://doi.org/10.1088/0953-8984/24/23/233202)
- Hohenberg, P. & Kohn, W. Inhomogeneous Electron Gas. Phys. Rev. 136, B864–B871 (1964) -- [10.1103/physrev.136.b864](https://doi.org/10.1103/physrev.136.b864)
- Runge, E. & Gross, E. K. U. Density-Functional Theory for Time-Dependent Systems. Phys. Rev. Lett. 52, 997–1000 (1984) -- [10.1103/physrevlett.52.997](https://doi.org/10.1103/physrevlett.52.997)
- Jia, W. et al. The analysis of a plane wave pseudopotential density functional theory code on a GPU machine. Computer Physics Communications 184, 9–18 (2013) -- [10.1016/j.cpc.2012.08.002](https://doi.org/10.1016/j.cpc.2012.08.002)
- romero, A performance study of quantum espresso&#x2019;s pwscf code on multi-core and gpu systems. International Workshop on Performance Modeling Benchmarking and Simulation of High Performance Computer Systems (2017)
- Jia, W. et al. Fast plane wave density functional theory molecular dynamics calculations on multi-GPU machines. Journal of Computational Physics 251, 102–115 (2013) -- [10.1016/j.jcp.2013.05.005](https://doi.org/10.1016/j.jcp.2013.05.005)
- Hacene, M. et al. Accelerating VASP electronic structure calculations using graphic processing units. J Comput Chem 33, 2581–2589 (2012) -- [10.1002/jcc.23096](https://doi.org/10.1002/jcc.23096)
- Hu, W. et al. High performance computing of DGDFT for tens of thousands of atoms using millions of cores on Sunway TaihuLight. Science Bulletin 66, 111–119 (2021) -- [10.1016/j.scib.2020.06.025](https://doi.org/10.1016/j.scib.2020.06.025)
- Valiev, M. et al. NWChem: A comprehensive and scalable open-source solution for large scale molecular simulations. Computer Physics Communications 181, 1477–1489 (2010) -- [10.1016/j.cpc.2010.04.018](https://doi.org/10.1016/j.cpc.2010.04.018)
- Hutchinson, M. & Widom, M. VASP on a GPU: Application to exact-exchange calculations of the stability of elemental boron. Computer Physics Communications 183, 1422–1426 (2012) -- [10.1016/j.cpc.2012.02.017](https://doi.org/10.1016/j.cpc.2012.02.017)

