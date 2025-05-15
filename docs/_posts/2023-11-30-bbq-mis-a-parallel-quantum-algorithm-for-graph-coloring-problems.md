---
layout: post
title: "BBQ-mIS: A Parallel Quantum Algorithm for Graph Coloring Problems"
date: 2023-11-30 00:00:00 +0100
permalink: bbq-mis-a-parallel-quantum-algorithm-for-graph-coloring-problems
year: 2023
authors: Chiara Vercellino, Giacomo Vitali, Paolo Viviani, Edoardo Giusto, Alberto Scionti, Andrea Scarabosio, Olivier Terzo, Bartolomeo Montrucchio
category: proceedings
---
 
## Authors
[Chiara Vercellino](authors/chiara-vercellino), [Giacomo Vitali](authors/giacomo-vitali), [Paolo Viviani](authors/paolo-viviani), [Edoardo Giusto](authors/edoardo-giusto), [Alberto Scionti](authors/alberto-scionti), [Andrea Scarabosio](authors/andrea-scarabosio), [Olivier Terzo](authors/olivier-terzo), [Bartolomeo Montrucchio](authors/bartolomeo-montrucchio)
 
## Abstract
Among the limitations of current quantum machines, the qubits count represents one of the most critical challenges for porting reasonably large computational problems, such as those coming from real-world applications, to the scale of the quantum hardware. In this regard, one possibility is to decompose the problems at hand and exploit parallelism over multiple size-limited quantum resources. To this purpose, we designed a hybrid quantum-classical algorithm, i.e., BBQ-mIS, to solve graph coloring problems on Rydberg atoms quantum machines. The BBQ-mIS algorithm combines the natural representation of Maximum Independent Set (MIS) problems onto the machine Hamiltonian with a Branch&Bound (BB) approach to identify a proper graph coloring. In the proposed solution, the graph representation emerges from qubit interactions (qubits represent vertexes of the graph), and the coloring is then retrieved by iteratively assigning one color to a maximal set of independent vertexes of the graph, still minimizing the number of colors with the Branch&Bound approach. We emulated real quantum hardware onto an IBM Power9-based cluster, with 32 cores/node and 256 GB/node, and exploited an MPI-enhanced library to implement the parallelism for the BBQ-mIS algorithm. Considering this use case, we also identify some technical requirements and challenges for an effective HPC-QC integration. The results show that our problem decomposition is effective in terms of graph coloring solutions quality, and provide a reference for applying this methodology to other quantum technologies or applications.
 
## Citation
- **Journal:** 2023 IEEE International Conference on Quantum Computing and Engineering (QCE)
- **Year:** 2023
- **Volume:** 
- **Issue:** 
- **Pages:** 141--147
- **Publisher:** IEEE
- **DOI:** [10.1109/qce57702.2023.10198](https://doi.org/10.1109/qce57702.2023.10198)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Vercellino_2023,
  title={{BBQ-mIS: A Parallel Quantum Algorithm for Graph Coloring Problems}},
  DOI={10.1109/qce57702.2023.10198},
  booktitle={{2023 IEEE International Conference on Quantum Computing and Engineering (QCE)}},
  publisher={IEEE},
  author={Vercellino, Chiara and Vitali, Giacomo and Viviani, Paolo and Giusto, Edoardo and Scionti, Alberto and Scarabosio, Andrea and Terzo, Olivier and Montrucchio, Bartolomeo},
  year={2023},
  pages={141--147}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/bbq-mis-a-parallel-quantum-algorithm-for-graph-coloring-problems.bib)
 
## References
- Barillaro, G. et al. Comparison of heuristic approaches to PCI planning for Quantum Computers. 2023 IEEE International Conference on Consumer Electronics (ICCE) 1–6 (2023) doi:10.1109/icce56470.2023.10043394 -- [10.1109/icce56470.2023.10043394](https://doi.org/10.1109/icce56470.2023.10043394)
- Khor, S. Application of graph colouring to biological networks. IET Syst. Biol. 4, 185–192 (2010) -- [10.1049/iet-syb.2009.0038](https://doi.org/10.1049/iet-syb.2009.0038)
- Grimm, R., Weidemüller, M. & Ovchinnikov, Y. B. Optical Dipole Traps for Neutral Atoms. Advances In Atomic, Molecular, and Optical Physics 95–170 (2000) doi:10.1016/s1049-250x(08)60186-x -- [10.1016/s1049-250x(08)60186-x](https://doi.org/10.1016/s1049-250x(08)60186-x)
- Dalyac, C. et al. Qualifying quantum approaches for hard industrial optimization problems. A case study in the field of smart-charging of electric vehicles. EPJ Quantum Technol. 8, (2021) -- [10.1140/epjqt/s40507-021-00100-3](https://doi.org/10.1140/epjqt/s40507-021-00100-3)
- Ciampini, D., Morsch, O. & Arimondo, E. Ultracold Rubidium Atoms Excited to Rydberg Levels. Jour. Atom. Mol. Conden. Nano Physics 2, 161–167 (2015) -- [10.26713/jamcnp.v2i3.336](https://doi.org/10.26713/jamcnp.v2i3.336)
- Picken, C. J., Legaie, R., McDonnell, K. & Pritchard, J. D. Entanglement of neutral-atom qubits with long ground-Rydberg coherence times. Quantum Sci. Technol. 4, 015011 (2018) -- [10.1088/2058-9565/aaf019](https://doi.org/10.1088/2058-9565/aaf019)
- Clark, B. N., Colbourn, C. J. & Johnson, D. S. Unit disk graphs. Discrete Mathematics 86, 165–177 (1990) -- [10.1016/0012-365x(90)90358-o](https://doi.org/10.1016/0012-365x(90)90358-o)
- Nguyen, M.-T. et al. Quantum Optimization with Arbitrary Connectivity Using Rydberg Atom Arrays. PRX Quantum 4, (2023) -- [10.1103/prxquantum.4.010316](https://doi.org/10.1103/prxquantum.4.010316)
- Vercellino, C. et al. Neural-powered unit disk graph embedding: qubits connectivity for some QUBO problems. 2022 IEEE International Conference on Quantum Computing and Engineering (QCE) 186–196 (2022) doi:10.1109/qce53715.2022.00038 -- [10.1109/qce53715.2022.00038](https://doi.org/10.1109/qce53715.2022.00038)
- Bixby, The gurobi optimizer. Transp. Re-search Part B (2007)
- Mugel, S. et al. Hybrid quantum investment optimization with minimal holding period. Sci Rep 11, (2021) -- [10.1038/s41598-021-98297-x](https://doi.org/10.1038/s41598-021-98297-x)
- Nakanishi, K. M., Fujii, K. & Todo, S. Sequential minimal optimization for quantum-classical hybrid algorithms. Phys. Rev. Research 2, (2020) -- [10.1103/physrevresearch.2.043158](https://doi.org/10.1103/physrevresearch.2.043158)
- Graham, T. M. et al. Multi-qubit entanglement and algorithms on a neutral-atom quantum computer. Nature 604, 457–462 (2022) -- [10.1038/s41586-022-04603-6](https://doi.org/10.1038/s41586-022-04603-6)
- Li, M.-W., Xu, D.-Y., Geng, J. & Hong, W.-C. A ship motion forecasting approach based on empirical mode decomposition method hybrid deep learning network and quantum butterfly optimization algorithm. Nonlinear Dyn 107, 2447–2467 (2022) -- [10.1007/s11071-021-07139-y](https://doi.org/10.1007/s11071-021-07139-y)
- de Keijzer, R., Tse, O. & Kokkelmans, S. Pulse based Variational Quantum Optimal Control for hybrid quantum computing. Quantum 7, 908 (2023) -- [10.22331/q-2023-01-26-908](https://doi.org/10.22331/q-2023-01-26-908)
- Silva, C., Aguiar, A., Lima, P. M. V. & Dutra, I. Mapping graph coloring to quantum annealing. Quantum Mach. Intell. 2, (2020) -- [10.1007/s42484-020-00028-4](https://doi.org/10.1007/s42484-020-00028-4)
- Więckowski, A., Deffner, S. & Gardas, B. Disorder-assisted graph coloring on quantum annealers. Phys. Rev. A 100, (2019) -- [10.1103/physreva.100.062304](https://doi.org/10.1103/physreva.100.062304)
- Titiloye, O. & Crispin, A. Parameter Tuning Patterns for Random Graph Coloring with Quantum Annealing. PLoS ONE 7, e50060 (2012) -- [10.1371/journal.pone.0050060](https://doi.org/10.1371/journal.pone.0050060)
- Kudo, K. Constrained quantum annealing of graph coloring. Phys. Rev. A 98, (2018) -- [10.1103/physreva.98.022301](https://doi.org/10.1103/physreva.98.022301)
- Titiloye, O. & Crispin, A. Quantum annealing of the graph coloring problem. Discrete Optimization 8, 376–384 (2011) -- [10.1016/j.disopt.2010.12.001](https://doi.org/10.1016/j.disopt.2010.12.001)
- Do, Planning for compilation of a quantum algorithm for graph coloring. arXiv preprint (2020)
- Mohar, B. & Poljak, S. Eigenvalues and the max-cut problem. Czech. Math. J. 40, 343–352 (1990) -- [10.21136/cmj.1990.102386](https://doi.org/10.21136/cmj.1990.102386)
- Tabi, Z. et al. Quantum Optimization for the Graph Coloring Problem with Space-Efficient Embedding. 2020 IEEE International Conference on Quantum Computing and Engineering (QCE) 56–62 (2020) doi:10.1109/qce49297.2020.00018 -- [10.1109/qce49297.2020.00018](https://doi.org/10.1109/qce49297.2020.00018)
- Wang, Y. & Perkowski, M. Improved Complexity of Quantum Oracles for Ternary Grover Algorithm for Graph Coloring. 2011 41st IEEE International Symposium on Multiple-Valued Logic 294–301 (2011) doi:10.1109/ismvl.2011.42 -- [10.1109/ismvl.2011.42](https://doi.org/10.1109/ismvl.2011.42)
- Bravyi, S., Kliesch, A., Koenig, R. & Tang, E. Hybrid quantum-classical algorithms for approximate graph coloring. Quantum 6, 678 (2022) -- [10.22331/q-2022-03-30-678](https://doi.org/10.22331/q-2022-03-30-678)
- Ardelean, S. M. & Udrescu, M. Graph coloring using the reduced quantum genetic algorithm. PeerJ Computer Science 7, e836 (2022) -- [10.7717/peerj-cs.836](https://doi.org/10.7717/peerj-cs.836)
- Jensen, T. R. & Toft, B. Graph Coloring Problems. (1994) doi:10.1002/9781118032497 -- [10.1002/9781118032497](https://doi.org/10.1002/9781118032497)
- Tarjan, R. E. & Trojanowski, A. E. Finding a Maximum Independent Set. SIAM J. Comput. 6, 537–546 (1977) -- [10.1137/0206038](https://doi.org/10.1137/0206038)
- Glover, F., Kochenberger, G. & Du, Y. A Tutorial on Formulating and Using QUBO Models. Preprint at https://doi.org/10.48550/ARXIV.1811.11538 (2018) -- [10.48550/arxiv.1811.11538](https://doi.org/10.48550/arxiv.1811.11538)
- De Lima, A. M. & Carmo, R. Exact Algorithms for the Graph Coloring Problem. RITA 25, 57 (2018) -- [10.22456/2175-2745.80721](https://doi.org/10.22456/2175-2745.80721)
- Christofides, N. An algorithm for the chromatic number of a graph. The Computer Journal 14, 38–39 (1971) -- [10.1093/comjnl/14.1.38](https://doi.org/10.1093/comjnl/14.1.38)
- Mitchem, J. On Various Algorithms for Estimating the Chromatic Number of a Graph. The Computer Journal 19, 182–183 (1976) -- [10.1093/comjnl/19.2.182](https://doi.org/10.1093/comjnl/19.2.182)
- Welsh, D. J. A. An upper bound for the chromatic number of a graph and its application to timetabling problems. The Computer Journal 10, 85–86 (1967) -- [10.1093/comjnl/10.1.85](https://doi.org/10.1093/comjnl/10.1.85)
- Hoffman, A. J. & Howes, L. ON EIGENVALUES AND COLORINGS OF GRAPHS, II. Ann NY Acad Sci 175, 238–242 (1970) -- [10.1111/j.1749-6632.1970.tb45136.x](https://doi.org/10.1111/j.1749-6632.1970.tb45136.x)
- Elphick, C. & Wocjan, P. An Inertial Lower Bound for the Chromatic Number of a Graph. Electron. J. Combin. 24, (2017) -- [10.37236/6404](https://doi.org/10.37236/6404)
- Edwards, C. S. & Elphick, C. H. Lower bounds for the clique and the chromatic numbers of a graph. Discrete Applied Mathematics 5, 51–64 (1983) -- [10.1016/0166-218x(83)90015-x](https://doi.org/10.1016/0166-218x(83)90015-x)
- Byskov, J. M. Enumerating maximal independent sets with applications to graph colouring. Operations Research Letters 32, 547–556 (2004) -- [10.1016/j.orl.2004.03.002](https://doi.org/10.1016/j.orl.2004.03.002)
- Serret, M. F., Marchand, B. & Ayral, T. Solving optimization problems with Rydberg analog quantum computers: Realistic requirements for quantum advantage using noisy simulation and classical benchmarks. Phys. Rev. A 102, (2020) -- [10.1103/physreva.102.052617](https://doi.org/10.1103/physreva.102.052617)
- Farhi, A quantum approximate optimization algorithm. arXiv preprint (2014)
- Silvério, H. et al. Pulser: An open-source package for the design of pulse sequences in programmable neutral-atom arrays. Quantum 6, 629 (2022) -- [10.22331/q-2022-01-24-629](https://doi.org/10.22331/q-2022-01-24-629)
- Humble, T. S. et al. Quantum Computers for High-Performance Computing. IEEE Micro 41, 15–23 (2021) -- [10.1109/mm.2021.3099140](https://doi.org/10.1109/mm.2021.3099140)
- Wurtz, Aquila: QuEras 256-qubit neutral-atom quantum computer (2023)
- QAOA and QAA to solve a QUBO problem (2023)
- Schulz, M., Ruefenacht, M., Kranzlmuller, D. & Schulz, L. B. Accelerating HPC With Quantum Computing: It Is a Software Challenge Too. Comput. Sci. Eng. 24, 60–64 (2022) -- [10.1109/mcse.2022.3221845](https://doi.org/10.1109/mcse.2022.3221845)
- Albash, T. & Lidar, D. A. Adiabatic quantum computation. Rev. Mod. Phys. 90, (2018) -- [10.1103/revmodphys.90.015002](https://doi.org/10.1103/revmodphys.90.015002)

