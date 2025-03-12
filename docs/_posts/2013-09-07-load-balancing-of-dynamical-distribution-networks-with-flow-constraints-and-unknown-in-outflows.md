---
layout: post
title: "Load balancing of dynamical distribution networks with flow constraints and unknown in/outflows"
date: 2013-09-07 00:00:00 +0100
permalink: load-balancing-of-dynamical-distribution-networks-with-flow-constraints-and-unknown-in-outflows
year: 2013
authors: J. Wei, A.J. van der Schaft
category: articles
tags:
  - PI controllers
  - Flow constraints
  - Directed graphs
  - Port-Hamiltonian systems
  - Consensus algorithms
  - Lyapunov stability
---
 
## Authors
[J. Wei](authors/jieqiang-wei), [A.J. van der Schaft](authors/arjan-van-der-schaft)
 
## Abstract
We consider a basic model of a dynamical distribution network, modeled as a directed graph with storage variables corresponding to every vertex and flow inputs corresponding to every edge, subject to unknown but constant inflows and outflows. As a preparatory result it is shown how a distributed proportional–integral controller structure, associating with every edge of the graph a controller state, will regulate the state variables of the vertices, irrespective of the unknown constant inflows and outflows, in the sense that the storage variables converge to the same value (load balancing or consensus). This will be proved by identifying the closed-loop system as a port-Hamiltonian system, and modifying the Hamiltonian function into a Lyapunov function, dependent on the value of the vector of constant inflows and outflows. In the main part of the paper the same problem will be addressed for the case that the input flow variables are constrained to take value in an arbitrary interval. We will derive sufficient and necessary conditions for load balancing, which only depend on the structure of the network in relation with the flow constraints.
 
## Keywords
PI controllers; Flow constraints; Directed graphs; Port-Hamiltonian systems; Consensus algorithms; Lyapunov stability
 
## Citation
- **Journal:** Systems &amp; Control Letters
- **Year:** 2013
- **Volume:** 62
- **Issue:** 11
- **Pages:** 1001--1008
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.sysconle.2013.08.001](https://doi.org/10.1016/j.sysconle.2013.08.001)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Wei_2013,
  title={{Load balancing of dynamical distribution networks with flow constraints and unknown in/outflows}},
  volume={62},
  ISSN={0167-6911},
  DOI={10.1016/j.sysconle.2013.08.001},
  number={11},
  journal={Systems &amp; Control Letters},
  publisher={Elsevier BV},
  author={Wei, J. and van der Schaft, A.J.},
  year={2013},
  pages={1001--1008}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/load-balancing-of-dynamical-distribution-networks-with-flow-constraints-and-unknown-in-outflows.bib)
 
## References
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM Journal on Control and Optimization vol. 51 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- van der Schaft, A. J. & Maschke, B. M. Conservation laws and open systems on higher-dimensional networks. 2008 47th IEEE Conference on Decision and Control 799–804 (2008) doi:10.1109/cdc.2008.4738952 -- [10.1109/cdc.2008.4738952](https://doi.org/10.1109/cdc.2008.4738952)
- van der Schaft, (2009)
- van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Dynamics on Graphs: Consensus and Coordination Control Algorithms. IFAC Proceedings Volumes vol. 43 175–178 (2010) -- [10.3182/20100913-2-fr-4014.00012](https://doi.org/10.3182/20100913-2-fr-4014.00012)
- Burger, M., Zelazo, D. & Allgower, F. Network clustering: A dynamical systems and saddle-point perspective. IEEE Conference on Decision and Control and European Control Conference 7825–7830 (2011) doi:10.1109/cdc.2011.6161045 -- [10.1109/cdc.2011.6161045](https://doi.org/10.1109/cdc.2011.6161045)
- Zelazo, D. & Mesbahi, M. Edge Agreement: Graph-Theoretic Performance Bounds and Passivity Analysis. IEEE Transactions on Automatic Control vol. 56 544–555 (2011) -- [10.1109/tac.2010.2056730](https://doi.org/10.1109/tac.2010.2056730)
- van der Schaft, A. J. & Wei, J. A Hamiltonian perspective on the control of dynamical distribution networks. IFAC Proceedings Volumes vol. 45 24–29 (2012) -- [10.3182/20120829-3-it-4022.00033](https://doi.org/10.3182/20120829-3-it-4022.00033)
- Bollobas, (1998)
- van der Schaft, The Hamiltonian formulation of energy conserving physical systems with external ports. Archiv für Elektronik und Übertragungstechnik (1995)
- van der Schaft, (1996)
- Romero, J. G., Donaire, A. & Ortega, R. Robustifying energy shaping control of mechanical systems. 2012 IEEE 51st IEEE Conference on Decision and Control (CDC) 4424–4429 (2012) doi:10.1109/cdc.2012.6425923 -- [10.1109/cdc.2012.6425923](https://doi.org/10.1109/cdc.2012.6425923)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 53 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- Jayawardhana, B., Ortega, R., García-Canseco, E. & Castaños, F. Passivity of nonlinear incremental systems: Application to PI stabilization of nonlinear RLC circuits. Systems &amp; Control Letters vol. 56 618–622 (2007) -- [10.1016/j.sysconle.2007.03.011](https://doi.org/10.1016/j.sysconle.2007.03.011)
- Blanchini, F., Miani, S. & Ukovich, W. Control of production-distribution systems with unknown inputs and system failures. IEEE Transactions on Automatic Control vol. 45 1072–1081 (2000) -- [10.1109/9.863593](https://doi.org/10.1109/9.863593)
- Ren, W. On Consensus Algorithms for Double-Integrator Dynamics. IEEE Transactions on Automatic Control vol. 53 1503–1509 (2008) -- [10.1109/tac.2008.924961](https://doi.org/10.1109/tac.2008.924961)
- De Persis, C. Balancing time-varying demand-supply in distribution networks: An internal model approach. 2013 European Control Conference (ECC) 748–753 (2013) doi:10.23919/ecc.2013.6669480 -- [10.23919/ecc.2013.6669480](https://doi.org/10.23919/ecc.2013.6669480)

