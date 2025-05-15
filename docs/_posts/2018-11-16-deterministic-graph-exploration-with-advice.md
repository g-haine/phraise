---
layout: post
title: "Deterministic Graph Exploration with Advice"
date: 2018-11-16 00:00:00 +0100
permalink: deterministic-graph-exploration-with-advice
year: 2019
authors: Barun Gorain, Andrzej Pelc
category: articles
---
 
## Authors
[Barun Gorain](authors/barun-gorain), [Andrzej Pelc](authors/andrzej-pelc)
 
## Abstract
 We consider the fundamental task of graph exploration. An n -node graph has unlabeled nodes, and all ports at any node of degree d are arbitrarily numbered 0,…, d −1. A mobile agent, initially situated at some starting node v , has to visit all nodes and stop. The time of the exploration is the number of edge traversals. We consider the problem of how much knowledge the agent has to have a priori , to explore the graph in a given time, using a deterministic algorithm. Following the paradigm of algorithms with advice , this a priori information (advice) is provided to the agent by an oracle , in the form of a binary string, whose length is called the size of advice . We consider two types of oracles. The instance oracle knows the entire instance of the exploration problem, i.e., the port-numbered map of the graph and the starting node of the agent in this map. The map oracle knows the port-numbered map of the graph but does not know the starting node of the agent. What is the minimum size of advice that must be given to the agent by each of these oracles, so that the agent explores the graph in a given time?   We first determine the minimum size of advice to achieve exploration in polynomial time. We prove that some advice of size log log log n − c , for any constant c , is sufficient for polynomial exploration, and that no advice of size log log log n −ϕ ( n ), where ϕ is any function diverging to infinity, can help to do this. These results hold both for the instance and for the map oracles.   On the other side of the spectrum, when advice is large, there are two natural time thresholds: Θ ( n 2 ) for a map oracle, and Θ ( n ) for an instance oracle. This is because, in both cases, these time benchmarks can be achieved with sufficiently large advice (advice of size O ( n log n ) suffices). We show that, with a map oracle, time Θ ( n 2 ) cannot be improved in general, regardless of the size of advice. What is then the smallest advice to achieve time Θ ( n 2 ) with a map oracle? We show that this smallest size of advice is larger than n δ , for any δ &lt; 1/3.   For large advice, the situation changes significantly when we allow an instance oracle instead of a map oracle. In this case, advice of size O ( n log n ) is enough to achieve time O ( n ). Is such a large advice needed to achieve linear time? We answer this question affirmatively. Indeed, we show more: with any advice of size o ( n log n ), the time of exploration must be at least n ϵ , for any ϵ &lt; 2, and with any advice of size O ( n ), the time must be Ω( n 2 ).   We finally look at Hamiltonian graphs, as for them it is possible to achieve the absolutely optimal exploration time n −1, when sufficiently large advice (of size o ( n log n )) is given by an instance oracle. We show that a map oracle cannot achieve this: regardless of the size of advice, the time of exploration must be Ω( n 2 ), for some Hamiltonian graphs. However, even for the instance oracle, with advice of size o ( n log n ), optimal time n −1 cannot be achieved: Indeed, we show that the time of exploration with such advice must sometimes exceed the optimal time n −1 by a summand n ϵ , for any ϵ &lt; 1. 
 
## Citation
- **Journal:** ACM Transactions on Algorithms
- **Year:** 2019
- **Volume:** 15
- **Issue:** 1
- **Pages:** 1--17
- **Publisher:** Association for Computing Machinery (ACM)
- **DOI:** [10.1145/3280823](https://doi.org/10.1145/3280823)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gorain_2018,
  title={{Deterministic Graph Exploration with Advice}},
  volume={15},
  ISSN={1549-6333},
  DOI={10.1145/3280823},
  number={1},
  journal={ACM Transactions on Algorithms},
  publisher={Association for Computing Machinery (ACM)},
  author={Gorain, Barun and Pelc, Andrzej},
  year={2018},
  pages={1--17}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/deterministic-graph-exploration-with-advice.bib)
 
## References
- Abiteboul, S., Alstrup, S., Kaplan, H., Milo, T. & Rauhe, T. Compact Labeling Scheme for Ancestor Queries. SIAM J. Comput. 35, 1295–1309 (2006) -- [10.1137/s0097539703437211](https://doi.org/10.1137/s0097539703437211)
- Albers, S. & Henzinger, M. R. Exploring Unknown Environments. SIAM J. Comput. 29, 1164–1188 (2000) -- [10.1137/s009753979732428x](https://doi.org/10.1137/s009753979732428x)
- Aleliunas, R., Karp, R. M., Lipton, R. J., Lovasz, L. & Rackoff, C. Random walks, universal traversal sequences, and the complexity of maze problems. 20th Annual Symposium on Foundations of Computer Science (sfcs 1979) 218–223 (1979) doi:10.1109/sfcs.1979.34 -- [10.1109/sfcs.1979.34](https://doi.org/10.1109/sfcs.1979.34)
- Awerbuch, B., Betke, M., Rivest, R. L. & Singh, M. Piecemeal Graph Exploration by a Mobile Robot. Information and Computation 152, 155–172 (1999) -- [10.1006/inco.1999.2795](https://doi.org/10.1006/inco.1999.2795)
- Bareli, E., Berman, P., Fiat, A. & Yan, P. Y. Online Navigation in a Room. Journal of Algorithms 17, 319–341 (1994) -- [10.1006/jagm.1994.1039](https://doi.org/10.1006/jagm.1994.1039)
- Bender, M. A., Fernández, A., Ron, D., Sahai, A. & Vadhan, S. The Power of a Pebble: Exploring and Mapping Directed Graphs. Information and Computation 176, 1–21 (2002) -- [10.1006/inco.2001.3081](https://doi.org/10.1006/inco.2001.3081)
- Bender, M. A. & Slonim, D. K. The power of team exploration: two robots can learn unlabeled directed graphs. Proceedings 35th Annual Symposium on Foundations of Computer Science 75–85 doi:10.1109/sfcs.1994.365703 -- [10.1109/sfcs.1994.365703](https://doi.org/10.1109/sfcs.1994.365703)
- Betke, M., Rivest, R. L. & Singh, M. Piecemeal learning of an unknown environment. Mach Learn 18, 231–254 (1995) -- [10.1007/bf00993411](https://doi.org/10.1007/bf00993411)
- Blum, A., Raghavan, P. & Schieber, B. Navigating in Unfamiliar Geometric Terrain. SIAM J. Comput. 26, 110–137 (1997) -- [10.1137/s0097539791194931](https://doi.org/10.1137/s0097539791194931)
- Borodin, A., Ruzzo, W. L. & Tompat, M. Lower bounds on the length of universal traversal sequences. Journal of Computer and System Sciences 45, 180–203 (1992) -- [10.1016/0022-0000(92)90046-l](https://doi.org/10.1016/0022-0000(92)90046-l)
- Boyar, J., Favrholdt, L. M., Kudahl, C., Larsen, K. S. & Mikkelsen, J. W. Online Algorithms with Advice. ACM Comput. Surv. 50, 1–34 (2017) -- [10.1145/3056461](https://doi.org/10.1145/3056461)
- Chalopin J., Proceeedings of the 14th International Conference on Principles of Distributed Systems (OPODIS’10)
- Deng, X., Kameda, T. & Papadimitriou, C. How to learn an unknown environment. I. J. ACM 45, 215–245 (1998) -- [10.1145/274787.274788](https://doi.org/10.1145/274787.274788)
- Dereniowski, D. & Pelc, A. Drawing maps with advice. Journal of Parallel and Distributed Computing 72, 132–143 (2012) -- [10.1016/j.jpdc.2011.10.004](https://doi.org/10.1016/j.jpdc.2011.10.004)
- Diks, K., Fraigniaud, P., Kranakis, E. & Pelc, A. Tree exploration with little memory. Journal of Algorithms 51, 38–63 (2004) -- [10.1016/j.jalgor.2003.10.002](https://doi.org/10.1016/j.jalgor.2003.10.002)
- Dieudonné, Y. & Pelc, A. Impact of Knowledge on Election Time in Anonymous Networks. Proceedings of the 29th ACM Symposium on Parallelism in Algorithms and Architectures 207–215 (2017) doi:10.1145/3087556.3087563 -- [10.1145/3087556.3087563](https://doi.org/10.1145/3087556.3087563)
- Dobrev, S., Královič, R. & Markou, E. Online Graph Exploration with Advice. Lecture Notes in Computer Science 267–278 (2012) doi:10.1007/978-3-642-31104-8_23 -- [10.1007/978-3-642-31104-8_23](https://doi.org/10.1007/978-3-642-31104-8_23)
- Duncan, C. A., Kobourov, S. G. & Kumar, V. S. A. Optimal constrained graph exploration. ACM Trans. Algorithms 2, 380–402 (2006) -- [10.1145/1159892.1159897](https://doi.org/10.1145/1159892.1159897)
- Emek, Y., Fraigniaud, P., Korman, A. & Rosén, A. Online computation with advice. Theoretical Computer Science 412, 2642–2656 (2011) -- [10.1016/j.tcs.2010.08.007](https://doi.org/10.1016/j.tcs.2010.08.007)
- Fraigniaud, P., Gavoille, C., Ilcinkas, D. & Pelc, A. Distributed computing with advice: information sensitivity of graph coloring. Distrib. Comput. 21, 395–403 (2009) -- [10.1007/s00446-008-0076-y](https://doi.org/10.1007/s00446-008-0076-y)
- Fraigniaud, P., Ilcinkas, D. & Pelc, A. Communication algorithms with advice. Journal of Computer and System Sciences 76, 222–232 (2010) -- [10.1016/j.jcss.2009.07.002](https://doi.org/10.1016/j.jcss.2009.07.002)
- Fraigniaud, P., Ilcinkas, D. & Pelc, A. Tree exploration with advice. Information and Computation 206, 1276–1287 (2008) -- [10.1016/j.ic.2008.07.005](https://doi.org/10.1016/j.ic.2008.07.005)
- Fraigniaud, P., Korman, A. & Lebhar, E. Local MST Computation with Short Advice. Theory Comput Syst 47, 920–933 (2010) -- [10.1007/s00224-010-9280-9](https://doi.org/10.1007/s00224-010-9280-9)
- Fraigniaud P., Proceedings of the 21st Symposium on Theoretical Aspects of Computer Science (STACS’04)
- DOI not foun -- [10.5555/3118756.3119007](https://doi.org/10.5555/3118756.3119007)
- Fusco, E. G., Pelc, A. & Petreschi, R. Topology recognition with advice. Information and Computation 247, 254–265 (2016) -- [10.1016/j.ic.2016.01.005](https://doi.org/10.1016/j.ic.2016.01.005)
- Gavoille, C., Peleg, D., Pérennes, S. & Raz, R. Distance labeling in graphs. Journal of Algorithms 53, 85–112 (2004) -- [10.1016/j.jalgor.2004.05.002](https://doi.org/10.1016/j.jalgor.2004.05.002)
- Glacet C., Proceedings of the 27th Annual ACM-SIAM Symposium on Discrete Algorithms (SODA’16)
- Ilcinkas, D., Kowalski, D. R. & Pelc, A. Fast radio broadcasting with advice. Theoretical Computer Science 411, 1544–1557 (2010) -- [10.1016/j.tcs.2010.01.004](https://doi.org/10.1016/j.tcs.2010.01.004)
- Komm, D., Královič, R., Královič, R. & Smula, J. Treasure Hunt with Advice. Lecture Notes in Computer Science 328–341 (2015) doi:10.1007/978-3-319-25258-2_23 -- [10.1007/978-3-319-25258-2_23](https://doi.org/10.1007/978-3-319-25258-2_23)
- Korman, A., Kutten, S. & Peleg, D. Proof labeling schemes. Distrib. Comput. 22, 215–233 (2010) -- [10.1007/s00446-010-0095-3](https://doi.org/10.1007/s00446-010-0095-3)
- Megow, N., Mehlhorn, K. & Schweitzer, P. Online graph exploration: New results on old and new algorithms. Theoretical Computer Science 463, 62–72 (2012) -- [10.1016/j.tcs.2012.06.034](https://doi.org/10.1016/j.tcs.2012.06.034)
- Nisse, N. & Soguet, D. Graph searching with advice. Theoretical Computer Science 410, 1307–1318 (2009) -- [10.1016/j.tcs.2008.08.020](https://doi.org/10.1016/j.tcs.2008.08.020)
- Panaite, P. & Pelc, A. Exploring Unknown Undirected Graphs. Journal of Algorithms 33, 281–295 (1999) -- [10.1006/jagm.1999.1043](https://doi.org/10.1006/jagm.1999.1043)
- Panaite, P. & Pelc, A. Optimal Broadcasting in Faulty Trees. Journal of Parallel and Distributed Computing 60, 566–584 (2000) -- [10.1006/jpdc.2000.1625](https://doi.org/10.1006/jpdc.2000.1625)
- PELC, A. & TIANE, A. EFFICIENT GRID EXPLORATION WITH A STATIONARY TOKEN. Int. J. Found. Comput. Sci. 25, 247–262 (2014) -- [10.1142/s0129054114500129](https://doi.org/10.1142/s0129054114500129)
- Rao N. S. V., Oak Ridge National Laboratory (1993)
- Reingold, O. Undirected connectivity in log-space. J. ACM 55, 1–24 (2008) -- [10.1145/1391289.1391291](https://doi.org/10.1145/1391289.1391291)

