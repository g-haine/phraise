---
title: "OFAR-CM: Efficient Dragonfly Networks with Simple Congestion Management"
date: 2013-10-17 00:00:00 +0100
permalink: ofar-cm-efficient-dragonfly-networks-with-simple-congestion-management
year: 2013
authors: Marina Garcia, Enrique Vallejo, Ramon Beivide, Mateo Valero, German Rodriguez
category: proceedings
---
 
## Authors
[Marina Garcia](authors/marina-garcia), [Enrique Vallejo](authors/enrique-vallejo), [Ramon Beivide](authors/ramon-beivide), [Mateo Valero](authors/mateo-valero), [German Rodriguez](authors/german-rodriguez)
 
## Abstract
Dragonfly networks are appealing topologies for large-scale Data center and HPC networks, that provide high throughput with low diameter and moderate cost. However, they are prone to congestion under certain frequent traffic patterns that saturate specific network links. Adaptive non-minimal routing can be used to avoid such congestion. That kind of routing employs longer paths to circumvent local or global congested links. However, if a distance-based deadlock avoidance mechanism is employed, more Virtual Channels (VCs) are required, what increases design complexity and cost. OFAR (On-the-Fly Adaptive Routing) is a previously proposed routing that decouples VCs from deadlock avoidance, making local and global misrouting affordable. However, the severity of congestion with OFAR is higher, as it relies on an escape sub network with low bisection bandwidth. Additionally, OFAR allows for unlimited misroutings on the escape sub network, leading to unbounded paths in the network and long latencies. In this paper we propose and evaluate OFAR-CM, a variant of OFAR combined with a simple congestion management (CM) mechanism which only relies on local information, specifically the credit count of the output ports in the local router. With simple escape sub networks such as a Hamiltonian ring or a tree, OFAR outperforms former proposals with distance-based deadlock avoidance. Additionally, although long paths are allowed in theory, in practice packets arrive at their destination in a small number of hops. Altogether, OFAR-CM constitutes the first practicable mechanism to the date that supports both local and global misrouting in Dragonfly networks.
 
## Citation
- **Journal:** 2013 IEEE 21st Annual Symposium on High-Performance Interconnects
- **Year:** 2013
- **Volume:** 
- **Issue:** 
- **Pages:** 55--62
- **Publisher:** IEEE
- **DOI:** [10.1109/hoti.2013.16](https://doi.org/10.1109/hoti.2013.16)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Garcia_2013,
  title={{OFAR-CM: Efficient Dragonfly Networks with Simple Congestion Management}},
  DOI={10.1109/hoti.2013.16},
  booktitle={{2013 IEEE 21st Annual Symposium on High-Performance Interconnects}},
  publisher={IEEE},
  author={Garcia, Marina and Vallejo, Enrique and Beivide, Ramon and Valero, Mateo and Rodriguez, German},
  year={2013},
  pages={55--62}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/ofar-cm-efficient-dragonfly-networks-with-simple-congestion-management.bib)
 
## References
- Rajamony, R., Stephenson, M. W. & Speight, W. E. The power 775 architecture at scale. Proceedings of the 27th international ACM conference on International conference on supercomputing 183–192 (2013) doi:10.1145/2464996.2465435 -- [10.1145/2464996.2465435](https://doi.org/10.1145/2464996.2465435)
- Karol, M., Hluchyj, M. & Morgan, S. Input Versus Output Queueing on a Space-Division Packet Switch. IEEE Trans. Commun. 35, 1347–1356 (1987) -- [10.1109/tcom.1987.1096719](https://doi.org/10.1109/tcom.1987.1096719)
- García, M. et al. Global misrouting policies in two-level hierarchical networks. Proceedings of the 2013 Interconnection Network Architecture: On-Chip, Multi-Chip 13–16 (2013) doi:10.1145/2482759.2482763 -- [10.1145/2482759.2482763](https://doi.org/10.1145/2482759.2482763)
- Minkenberg, C., Gusat, M. & Rodriguez, G. Adaptive Routing in Data Center Bridges. 2009 17th IEEE Symposium on High Performance Interconnects 33–41 (2009) doi:10.1109/hoti.2009.14 -- [10.1109/hoti.2009.14](https://doi.org/10.1109/hoti.2009.14)
- Lam, S. & Reiser, M. Congestion Control of Store-and-Forward Networks by Input Buffer Limits--An Analysis. IEEE Trans. Commun. 27, 127–134 (1979) -- [10.1109/tcom.1979.1094280](https://doi.org/10.1109/tcom.1979.1094280)
- Alizadeh, M. et al. Data center TCP (DCTCP). Proceedings of the ACM SIGCOMM 2010 conference (2010) doi:10.1145/1851182.1851192 -- [10.1145/1851182.1851192](https://doi.org/10.1145/1851182.1851192)
- Gran, E. G. et al. First experiences with congestion control in InfiniBand hardware. 2010 IEEE International Symposium on Parallel &amp; Distributed Processing (IPDPS) 1–12 (2010) doi:10.1109/ipdps.2010.5470419 -- [10.1109/ipdps.2010.5470419](https://doi.org/10.1109/ipdps.2010.5470419)
- Jacobson, V. Congestion avoidance and control. SIGCOMM Comput. Commun. Rev. 18, 314–329 (1988) -- [10.1145/52325.52356](https://doi.org/10.1145/52325.52356)
- IEEE standard for local and metropolitan area networks-virtual bridged local area networks-amendment: 10 congestion notification 802 .1Qau. IEEE Std (2010)
- faanes, Cray cascade: A scalable hpc system based on a dragonfly network. Intl Conf on High Performance Computing Networking Storage and Analysis (2012)
- Arimilli, B. et al. The PERCS High-Performance Interconnect. 2010 18th IEEE Symposium on High Performance Interconnects 75–82 (2010) doi:10.1109/hoti.2010.16 -- [10.1109/hoti.2010.16](https://doi.org/10.1109/hoti.2010.16)
- kim, Technology-driven, highlyscalable dragonfly topology. 35th International Symposium on Computer Architecture (ISCA'08) (2008)
- garc?a, Congestion management in hpc interconnection networks. HPC Advisory Council European Workshop Hamburg (2011)
- Jiang, N., Kim, J. & Dally, W. J. Indirect adaptive routing on large scale interconnection networks. Proceedings of the 36th annual international symposium on Computer architecture (2009) doi:10.1145/1555754.1555783 -- [10.1145/1555754.1555783](https://doi.org/10.1145/1555754.1555783)
- Carrion, C., Beivide, R., Gregorio, J. A. & Vallejo, F. A flow control mechanism to avoid message deadlock in k-ary n-cube networks. Proceedings Fourth International Conference on High-Performance Computing 322–329 doi:10.1109/hipc.1997.634510 -- [10.1109/hipc.1997.634510](https://doi.org/10.1109/hipc.1997.634510)
- Duato, J. & Pinkston, T. M. A general theory for deadlock-free adaptive routing using a mixed set of resources. IEEE Trans. Parallel Distrib. Syst. 12, 1219–1235 (2001) -- [10.1109/71.970556](https://doi.org/10.1109/71.970556)
- garc?a, On-thefly adaptive routing in high-radix hierarchical networks. The 41st International Conference on Parallel Processing (ICPP) 09 (2012)
- Gunther, K. Prevention of Deadlocks in Packet-Switched Data Transport Systems. IEEE Trans. Commun. 29, 512–524 (1981) -- [10.1109/tcom.1981.1095021](https://doi.org/10.1109/tcom.1981.1095021)
- Valiant, L. G. A Scheme for Fast Parallel Communication. SIAM J. Comput. 11, 350–361 (1982) -- [10.1137/0211027](https://doi.org/10.1137/0211027)

