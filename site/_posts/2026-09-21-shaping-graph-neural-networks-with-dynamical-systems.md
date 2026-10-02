---
title: "Shaping Graph Neural Networks with Dynamical Systems"
date: 2026-09-21 00:00:00 +0100
permalink: shaping-graph-neural-networks-with-dynamical-systems
year: 2026
authors: Alessio Gravina
category: articles
---
 
## Authors
[Alessio Gravina](authors/alessio-gravina)
 
## Abstract
The dynamics of information diffusion in Graph Neural Networks (GNNs) is a key issue that heavily influences graph representation learning, especially when long-range propagation is required. In this work, we present a unified dynamical-systems perspective for shaping approaches that explicitly control and regulate the degree of propagation, conservation, and dissipation of information throughout the neural flow. By interpreting GNN layers as discretizations of continuous-time differential equations defined over graphs, we leverage tools from stability theory, Hamiltonian mechanics, and wave dynamics to design architectures with principled (long-range) propagation properties. We review and analyze three complementary formulations: antisymmetric parameterizations that enforce non-dissipative behavior via spectral control of the Jacobian, port-Hamiltonian and oscillatory dynamics that embed conservation laws directly into the architecture. Across long-range graph transfer and graph property prediction benchmarks, these differential-equation-inspired GNNs consistently outperform classical message-passing and transformer-based models, maintaining stable information flow even in extreme propagation regimes. More broadly, this work highlights how neural differential equations provide a coherent theoretical framework for designing graph architectures with controllable stability, memory retention, and long-range information propagation guarantees.
 
## Citation
- **Journal:** Intelligenza Artificiale
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 17248035261488802
- **Publisher:** SAGE Publications
- **DOI:** [10.1177/17248035261488802](https://doi.org/10.1177/17248035261488802)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gravina_2026,
  title={{Shaping Graph Neural Networks with Dynamical Systems}},
  ISSN={2211-0097},
  DOI={10.1177/17248035261488802},
  journal={Intelligenza Artificiale},
  publisher={SAGE Publications},
  author={Gravina, Alessio},
  year={2026}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/shaping-graph-neural-networks-with-dynamical-systems.bib)
 
## References
- Abu-El-Haija S. Perozzi B. Kapoor A. Alipourfard N. Lerman K. Harutyunyan H. Ver Steeg G. Galstyan A. (2019). Mixhop: Higher-order graph convolutional architectures via sparsified neighborhood mixing. In International conference on machine learning (pp. 21–29). PMLR.
- Alon U. Yahav E. (2021). On the bottleneck of graph neural networks and its practical implications. In International conference on learning representations. https://openreview.net/forum?id=i80OPhOCVH2.
- Arnold V., Vogtmann K., Weinstein A. (2013). Mathematical methods of classical mechanics. Graduate Texts in Mathematics. Springer New York.
- Arroyo A, Gravina A, Gutteridge B, Barbero F, Gallicchio C, Dong X, Bronstein M, Vandergheynst P (2025) On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: Bridging Recurrent and Graph Learning. Advances in Neural Information Processing Systems 38 82705–82742 -- [10.52202/085713-2495](https://doi.org/10.52202/085713-2495)
- Ascher UM (2008) Numerical Methods for Evolutionary Differential Equations -- [10.1137/1.9780898718911](https://doi.org/10.1137/1.9780898718911)
- Ascher UM, Petzold LR (1998) Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations -- [10.1137/1.9781611971392](https://doi.org/10.1137/1.9781611971392)
- Bacciu D, Errica F, Gravina A, Madeddu L, Podda M, Stilo G (2024) Deep Graph Networks for Drug Repurposing With Multi-Protein Targets. IEEE Trans Emerg Topics Comput 12(1):177–189. https://doi.org/10.1109/tetc.2023.3238963 -- [10.1109/tetc.2023.3238963](https://doi.org/10.1109/tetc.2023.3238963)
- Bacciu D, Errica F, Micheli A, Podda M (2020) A gentle introduction to deep learning for graphs. Neural Networks 129:203–221. https://doi.org/10.1016/j.neunet.2020.06.006 -- [10.1016/j.neunet.2020.06.006](https://doi.org/10.1016/j.neunet.2020.06.006)
- Barabási A-L, Oltvai ZN (2004) Network biology: understanding the cell’s functional organization. Nat Rev Genet 5(2):101–113. https://doi.org/10.1038/nrg1272 -- [10.1038/nrg1272](https://doi.org/10.1038/nrg1272)
- Barbero F, Banino A, Kapturowski S, Kumaran D, Araújo J, Vitvitskyi A, Pascanu R, Velickovic P (2024) Transformers need glasses! Information over-squashing in language tasks. Advances in Neural Information Processing Systems 37 98111–98142 -- [10.52202/079017-3114](https://doi.org/10.52202/079017-3114)
- Barbero F. Velingker A. Saberi A. Bronstein M. M. Giovanni F. D. (2024b). Locality-aware graph rewiring in GNNs. In: The Twelfth International conference on learning representations. https://openreview.net/forum?id=4Ua4hKiAJX.
- Bellman R (1958) On a routing problem. Quart Appl Math 16(1):87–90. https://doi.org/10.1090/qam/102435 -- [10.1090/qam/102435](https://doi.org/10.1090/qam/102435)
- Black M. Wan Z. Nayyeri A. Wang Y. (2023). Understanding oversquashing in gnns through the lens of effective resistance. In Proceedings of the 40th international conference on machine learning.
- Bondy JA, Murty USR (1976) Graph Theory with Applications. Macmillan Education UK -- [10.1007/978-1-349-03521-2](https://doi.org/10.1007/978-1-349-03521-2)
- Bruna J. Zaremba W. Szlam A. LeCun Y. (2014). Spectral networks and locally connected networks on graphs. arXiv preprint arXiv:1312.6203.
- Cai C. Wang Y. (2020). A note on over-smoothing for graph neural networks. arXiv preprint arXiv:2006.13318.
- Chamberlain B. P. Rowbottom J. Gorinova M. Webb S. Rossi E. Bronstein M. M. (2021). GRAND: Graph neural diffusion. In International conference on machine learning (ICML) (pp. 1407–1418). PMLR.
- Chang B. Chen M. Haber E. Chi E. H. (2019). AntisymmetricRNN: A dynamical system view on recurrent neural networks. In International conference on learning representations. https://openreview.net/forum?id=ryxepo0cFX.
- Chen M. Wei Z. Huang Z. Ding B. Li Y. (2020). Simple and deep graph convolutional networks. In H. D. III & A. Singh (Eds.) Proceedings of the 37th international conference on machine learning Proceedings of Machine Learning Research (Vol. 119 pp. 1725–1735). PMLR.
- Chen R. T. Q. Rubanova Y. Bettencourt J. Duvenaud D. K. (2018). Neural ordinary differential equations. In S. Bengio H. Wallach H. Larochelle K. Grauman N. Cesa-Bianchi & R. Garnett (Eds.) Advances in neural information processing systems (Vol. 31). Curran Associates Inc.
- Cormen T. H., Leiserson C. E., Rivest R. L., Stein C. (2009). Introduction to algorithms, third edition. 3rd Edition. The MIT Press.
- Defferrard M. Bresson X. Vandergheynst P. (2016). Convolutional neural networks on graphs with fast localized spectral filtering. In Advances in neural information processing systems (Vol. 29). Curran Associates Inc.
- Derrow-Pinion A, She J, Wong D, Lange O, Hester T, Perez L, Nunkesser M, Lee S, Guo X, Wiltshire B, Battaglia PW, Gupta V, Li A, Xu Z, Sanchez-Gonzalez A, Li Y, Velickovic P (2021) ETA Prediction with Graph Neural Networks in Google Maps. Proceedings of the 30th ACM International Conference on Information & Knowledge Management 3767–3776 -- [10.1145/3459637.3481916](https://doi.org/10.1145/3459637.3481916)
- [Desai SA, Mattheakis M, Sondak D, Protopapas P, Roberts SJ (2021) Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Phys Rev E 104(3). https://doi.org/10.1103/physreve.104.034312](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Di Giovanni F. Giusti L. Barbero F. Luise G. Liò P. Bronstein M. (2023). On over-squashing in message passing neural networks: the impact of width depth and topology. In Proceedings of the 40th International conference on machine learning ICML’23. JMLR.org.
- Dijkstra EW (1959) A note on two problems in connexion with graphs. Numer Math 1(1):269–271. https://doi.org/10.1007/bf01386390 -- [10.1007/bf01386390](https://doi.org/10.1007/bf01386390)
- Ding Y. Orvieto A. He B. Hofmann T. (2024). Recurrent distance filtering for graph representation learning. In Forty-first international conference on machine learning.
- Dwivedi V. P., Bresson X. (2021). A generalization of transformer networks to graphs. AAAI Workshop on Deep Learning on Graphs: Methods and Applications.
- Dwivedi VP, Rampášek L, Galkin M, Parviz A, Wolf G, Luu AT, Beaini D (2022) Long Range Graph Benchmark. Advances in Neural Information Processing Systems 35 22326–22340 -- [10.52202/068431-1622](https://doi.org/10.52202/068431-1622)
- Eliasof M. Gravina A. Ceni A. Gallicchio C. Bacciu D. Schönlieb C. B. (2025). Graph adaptive autoregressive moving average models. In Forty-second international conference on machine learning. https://openreview.net/forum?id=UFlyLkvyAE.
- Errica F. Christiansen H. Zaverkin V. Maruyama T. Niepert M. Alesiani F. (2024). Adaptive message passing: A general framework to mitigate oversmoothing oversquashing and underreaching. arXiv preprint arXiv:2312.16560.
- Errica F, Gravina A, Bacciu D, Micheli A (2023) Hidden Markov Models for Temporal Graph Representation Learning. ESANN 2023 proceesdings 29–34 -- [10.14428/esann/2023.es2023-35](https://doi.org/10.14428/esann/2023.es2023-35)
- Evans L. C. (1998). Partial differential equations. San Francisco: American Mathematical Society.
- Finkelshtein B. Huang X. Bronstein M. M. Ceylan I. I. (2024). Cooperative graph neural networks. In Forty-first international conference on machine learning. https://openreview.net/forum?id=ZQcqXCuoxD.
- Friedman J, Tillich J-P (2004) Wave equations for graphs and the edge-based Laplacian. Pacific J Math 216(2):229–266. https://doi.org/10.2140/pjm.2004.216.229 -- [10.2140/pjm.2004.216.229](https://doi.org/10.2140/pjm.2004.216.229)
- Gasteiger J. Weißenberger S. Günnemann S. (2019). Diffusion improves graph learning. In Advances in neural information processing systems (Vol. 32). Curran Associates Inc.
- Gilmer J. Schoenholz S. S. Riley P. F. Vinyals O. Dahl G. E. (2017). Neural message passing for Quantum chemistry. In Proceedings of the 34th conference on machine learning ICML’17 (Vol. 70 p. 1263–1272). JMLR.org.
- Glendinning P (1994) Stability, Instability and Chaos -- [10.1017/cbo9780511626296](https://doi.org/10.1017/cbo9780511626296)
- Gravina A, Bacciu D (2024) Deep Learning for Dynamic Graphs: Models and Benchmarks. IEEE Trans Neural Netw Learning Syst 35(9):11788–11801. https://doi.org/10.1109/tnnls.2024.3379735 -- [10.1109/tnnls.2024.3379735](https://doi.org/10.1109/tnnls.2024.3379735)
- Gravina A. Bacciu D. Gallicchio C. (2023). Anti-Symmetric DGN: a stable architecture for Deep Graph Networks. In The Eleventh international conference on learning representations. https://openreview.net/forum?id=J3Y7cgZOOS.
- Gravina A, Eliasof M, Gallicchio C, Bacciu D, Schönlieb C-B (2025) On Oversquashing in Graph Neural Networks Through the Lens of Dynamical Systems. AAAI 39(16):16906–16914. https://doi.org/10.1609/aaai.v39i16.33858 -- [10.1609/aaai.v39i16.33858](https://doi.org/10.1609/aaai.v39i16.33858)
- Gravina A, Gallicchio C, Bacciu D (2025) Non-dissipative Propagation by Randomized Anti-symmetric Deep Graph Networks. Communications in Computer and Information Science 25–36 -- [10.1007/978-3-031-74643-7_3](https://doi.org/10.1007/978-3-031-74643-7_3)
- Gravina A. Lovisotto G. Gallicchio C. Bacciu D. Grohnfeldt C. (2024a). Long range propagation on continuous-time dynamic graphs. In Proceedings of the 41st international conference on machine learning Proceedings of Machine Learning Research (Vol. 235 pp. 16206–16225). PMLR. https://proceedings.mlr.press/v235/gravina24a.html
- Gravina A, Wilson JL, Bacciu D, Grimes KJ, Priami C (2022) Controlling astrocyte-mediated synaptic pruning signals for schizophrenia drug repurposing with deep graph networks. PLoS Comput Biol 18(5):e1009531. https://doi.org/10.1371/journal.pcbi.1009531 -- [10.1371/journal.pcbi.1009531](https://doi.org/10.1371/journal.pcbi.1009531)
- Gravina A, Zambon D, Bacciu D, Alippi C (2024) Temporal Graph ODEs for Irregularly-Sampled Time Series. Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial Intelligence 4025–4034 -- [10.24963/ijcai.2024/445](https://doi.org/10.24963/ijcai.2024/445)
- Gutteridge B. Dong X. Bronstein M. M. Di Giovanni F. (2023). Drew: Dynamically rewired message passing with delay. In International conference on machine learning (pp. 12252–12267). PMLR.
- Haber E, Ruthotto L (2017) Stable architectures for deep neural networks. Inverse Problems 34(1):014004. https://doi.org/10.1088/1361-6420/aa9a90 -- [10.1088/1361-6420/aa9a90](https://doi.org/10.1088/1361-6420/aa9a90)
- Hamilton W. L. Ying R. Leskovec J. (2017). Inductive representation learning on large graphs. In Proceedings of the 31st international conference on neural information processing systems NIPS’17 (pp. 1025–1035). Curran Associates Inc.
- Hariri A, Arroyo A, Gravina A, Eliasof M, Schönlieb C-B, Bacciu D, Dong X, Azizzadenesheli K, Vandergheynst P (2025) Return of ChebNet: Understanding and Improving an Overlooked GNN on Long Range Tasks. Advances in Neural Information Processing Systems 38 150940–150970 -- [10.52202/085713-4545](https://doi.org/10.52202/085713-4545)
- He K, Zhang X, Ren S, Sun J (2016) Deep Residual Learning for Image Recognition. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 770–778 -- [10.1109/cvpr.2016.90](https://doi.org/10.1109/cvpr.2016.90)
- He M, Wei Z, Wen J-R (2022) Convolutional Neural Networks on Graphs with Chebyshev Approximation, Revisited. Advances in Neural Information Processing Systems 35 7264–7276 -- [10.52202/068431-0527](https://doi.org/10.52202/068431-0527)
- He X. Hooi B. Laurent T. Perold A. LeCun Y. Bresson X. (2023). A generalization of vit/mlp-mixer to graphs. In Proceedings of the 40th international conference on machine learning ICML’23.
- Heilig S. Gravina A. Trenta A. Gallicchio C. Bacciu D. (2025). Port-Hamiltonian architectural bias for long-range propagation in deep graph networks. In The Thirteenth international conference on learning representations. https://openreview.net/forum?id=03EkqSCKuO.
- Hoang T. Trenta A. Gravina A. Freymuth N. Becker P. Bacciu D. Neumann G. (2026). Improving long-range interactions in graph neural simulators via hamiltonian dynamics. In The Fourteenth international conference on learning representations. https://openreview.net/forum?id=x66u6TEDUw.
- Huang Z. Sun Y. Wang W. (2020). Learning Continuous System Dynamics from Irregularly-Sampled Partial Observations. In H. Larochelle M. Ranzato R. Hadsell M. Balcan & H. Lin (Eds.) Advances in neural information processing systems (Vol. 33 pp. 16177–16187). Curran Associates Inc.
- Humphries AR, Stuart AM (1994) Runge–Kutta Methods for Dissipative and Gradient Dynamical Systems. SIAM J Numer Anal 31(5):1452–1485. https://doi.org/10.1137/0731075 -- [10.1137/0731075](https://doi.org/10.1137/0731075)
- Karhadkar K. Banerjee P. K. Montufar G. (2023). FoSR: First-order spectral rewiring for addressing oversquashing in GNNs. In The eleventh international conference on learning representations. https://openreview.net/forum?id=3YjQfCLdrzz.
- Kipf T. N. Welling M. (2017). Semi-supervised classification with graph convolutional networks. In International conference on learning representations. https://openreview.net/forum?id=SJU4ayYgl.
- Kreuzer D., Beaini D., Hamilton W., Létourneau V., Tossou P. (2021). Rethinking graph transformers with spectral attention. Advances in Neural Information Processing Systems, 34, 21618–21629.
- Leeney W, Gravina A, Bacciu D (2025) Non-Dissipative Graph Propagation for Non-Local Community Detection. 2025 International Joint Conference on Neural Networks (IJCNN) 1–8 -- [10.1109/ijcnn64981.2025.11228363](https://doi.org/10.1109/ijcnn64981.2025.11228363)
- Linkerhägner J. Freymuth N. Scheikl P. M. Mathis-Ullrich F. Neumann G. (2023). Grounding graph network simulators using physical sensor observations. In The eleventh international conference on learning representations. https://openreview.net/forum?id=jsZsEd8VEY.
- Ma L. Lin C. Lim D. Romero-Soriano A. Dokania P. K. Coates M. Torr P. Lim S. N. (2023). Graph inductive biases in transformers without message passing. In Proceedings of the 40th international conference on machine learning Proceedings of Machine Learning Research (Vol. 202 pp. 23321–23337). PMLR.
- Marisca I, Bamberger J, Alippi C, Bronstein M (2025) Over-squashing in Spatiotemporal Graph Neural Networks. Advances in Neural Information Processing Systems 38 38213–38243 -- [10.52202/085713-1141](https://doi.org/10.52202/085713-1141)
- Mattheij R, Molenaar J (2002) Ordinary Differential Equations in Theory and Practice -- [10.1137/1.9780898719178](https://doi.org/10.1137/1.9780898719178)
- Micheli A (2009) Neural Network for Graphs: A Contextual Constructive Approach. IEEE Trans Neural Netw 20(3):498–511. https://doi.org/10.1109/tnn.2008.2010350 -- [10.1109/tnn.2008.2010350](https://doi.org/10.1109/tnn.2008.2010350)
- Miglior L. Tolloso M. Gravina A. Bacciu D. (2026). Can you hear me now? a benchmark for long-range graph propagation. In The Fourteenth international conference on learning representations. https://openreview.net/forum?id=DgkWFPZMPp.
- Minaee S. Mikolov T. Nikzad N. Chenaghlu M. Socher R. Amatriain X. Gao J. (2025). Large language models: A survey. arXiv preprint arXiv:2402.06196.
- Monti F. Frasca F. Eynard D. Mannion D. Bronstein M. M. (2019). Fake News Detection on Social Media using Geometric Deep Learning. arXiv preprint arXiv:1902.06673.
- Oh Y, Kam S, Lee J, Lim D-Y, Kim S, Bui AAT (2025) Comprehensive Review of Neural Differential Equations for Time Series Analysis. Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence 10621–10631 -- [10.24963/ijcai.2025/1179](https://doi.org/10.24963/ijcai.2025/1179)
- Oono K. Suzuki T. (2020). Graph neural networks exponentially lose expressive power for node classification. In International conference on learning representations. https://openreview.net/forum?id=S1ldO2EFPr.
- Pfaff T. Fortunato M. Sanchez-Gonzalez A. Battaglia P. (2021). Learning mesh-based simulation with graph networks. In International conference on learning representations. https://openreview.net/forum?id=roNqYL0_XP.
- Rampášek L, Galkin M, Dwivedi VP, Luu AT, Wolf G, Beaini D (2022) Recipe for a General, Powerful, Scalable Graph Transformer. Advances in Neural Information Processing Systems 35 14501–14515 -- [10.52202/068431-1054](https://doi.org/10.52202/068431-1054)
- Ross S. (1984). Differential equations. Wiley.
- Rubanova Y. Chen R. T. Q. Duvenaud D. K. (2019). Latent ordinary differential equations for irregularly-sampled time series. In Advances in neural information processing systems (Vol. 32). Curran Associates Inc.
- Rumelhart DE, Hinton GE, Williams RJ (1986) Learning representations by back-propagating errors. Nature 323(6088):533–536. https://doi.org/10.1038/323533a0 -- [10.1038/323533a0](https://doi.org/10.1038/323533a0)
- Rusch T. K. Bronstein M. M. Mishra S. (2023). A Survey on Oversmoothing in Graph Neural Networks. arXiv preprint arXiv:2303.10993.
- Rusch T. K. Chamberlain B. Rowbottom J. Mishra S. Bronstein M. (2022). Graph-coupled oscillator networks. In International conference on machine learning (pp. 18888–18909). PMLR.
- Scarselli F, Gori M, Ah Chung Tsoi, Hagenbuchner M, Monfardini G (2009) The Graph Neural Network Model. IEEE Trans Neural Netw 20(1):61–80. https://doi.org/10.1109/tnn.2008.2005605 -- [10.1109/tnn.2008.2005605](https://doi.org/10.1109/tnn.2008.2005605)
- Shi Y, Huang Z, Feng S, Zhong H, Wang W, Sun Y (2021) Masked Label Prediction: Unified Message Passing Model for Semi-Supervised Classification. Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence 1548–1554 -- [10.24963/ijcai.2021/214](https://doi.org/10.24963/ijcai.2021/214)
- Shirzad H. Velingker A. Venkatachalam B. Sutherland D. J. Sinop A. K. (2023). Exphormer: Sparse transformers for graphs. In International conference on machine learning (pp. 31613–31632). PMLR.
- Southern J. Giovanni F. D. Bronstein M. M. Lutzeyer J. F. (2025). Understanding virtual nodes: Oversquashing and node heterogeneity. In The thirteenth international conference on learning representations. https://openreview.net/forum?id=NmcOAwRyH5.
- Tönshoff J. Ritzert M. Rosenbluth E. Grohe M. (2023). Where did the gap go? reassessing the long-range graph benchmark. In The second learning on graphs conference. https://openreview.net/forum?id=rIUjwxc5lj.
- Topping J. Giovanni F. D. Chamberlain B. P. Dong X. Bronstein M. M. (2022). Understanding over-squashing and bottlenecks on graphs via curvature. In International conference on learning representations. https://openreview.net/forum?id=7UmjRGzp-A.
- Trenta A, Gravina A, Bacciu D (2025) SONAR: Long-Range Graph Propagation Through Information Waves. Advances in Neural Information Processing Systems 38 161017–161050 -- [10.52202/085713-4854](https://doi.org/10.52202/085713-4854)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview](port-hamiltonian-systems-theory-an-introductory-overview0) -- [10.1561/9781601987877](https://doi.org/10.1561/9781601987877)
- Vaswani A., Shazeer N., Parmar N., Uszkoreit J., Jones L., Gomez A. N., Kaiser Ł., Polosukhin I. (2017). Attention is all you need. In Advances in Neural Information Processing Systems, (Vol. 30). Curran Associates, Inc.
- Velickovic P. Cucurull G. Casanova A. Romero A. Liò P. Bengio Y. (2018). Graph attention networks. In International conference on learning representations. https://openreview.net/forum?id=rJXMpikCZ.
- Wang Y. Wang Y. Yang J. Lin Z. (2021). Dissecting the diffusion process in linear graph convolutional networks. In Advances in neural information processing systems (Vol. 34 pp. 5758–5769). Curran Associates Inc.
- Wasserman S, Faust K (1994) Social Network Analysis -- [10.1017/cbo9780511815478](https://doi.org/10.1017/cbo9780511815478)
- Xu K. Hu W. Leskovec J. Jegelka S. (2019). How powerful are graph neural networks? In International conference on learning representations. https://openreview.net/forum?id=ryGs6iA5Km.
- Ying C., Cai T., Luo S., Zheng S., Ke G., He D., Shen Y., Liu T. Y. (2021). Do transformers really perform badly for graph representation?. Advances in Neural Information Processing Systems, 34, 28877–28888.
- Yu Y. Y. Choi J. Cho W. Lee K. Kim N. Chang K. Woo C. Kim I. Lee S. Yang J. Y. Yoon S. Park N. (2024). Learning flexible body collision dynamics with hierarchical contact mesh transformer. In The Twelfth international conference on learning representations. https://openreview.net/forum?id=90yw2uM6J5.
- Zhou D. Kharlamov E. Kostylev E. V. (2025). GLora: A benchmark to evaluate the ability to learn long-range dependencies in graphs. In: The Thirteenth international conference on learning representations. https://openreview.net/forum?id=2jf5x5XoYk.
- Zitnik M, Agrawal M, Leskovec J (2018) Modeling polypharmacy side effects with graph convolutional networks. Bioinformatics 34(13):i457–i466. https://doi.org/10.1093/bioinformatics/bty294 -- [10.1093/bioinformatics/bty294](https://doi.org/10.1093/bioinformatics/bty294)

