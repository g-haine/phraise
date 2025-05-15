---
layout: post
title: "Providing 100% Throughput in a Buffered Crossbar Switch"
date: 2007-08-08 00:00:00 +0100
permalink: providing-100-throughput-in-a-buffered-crossbar-switch
year: 2007
authors: Yanming Shen, Shivendra S. Panwar, H. Jonathan Chao
category: proceedings
---
 
## Authors
[Yanming Shen](authors/yanming-shen), [Shivendra S. Panwar](authors/shivendra-s-panwar), [H. Jonathan Chao](authors/h-jonathan-chao)
 
## Abstract
Buffered crossbar switches have received great attention recently because they have become technologically feasible, have simpler scheduling algorithms, and achieve better performance than a bufferiess crossbar switch. Buffered crossbar switches have a buffer placed at each crosspoint. A cell is first delivered to a crosspoint buffer and then transferred to the output port. With a speedup of two, a buffered crossbar switch has previously been proved to provide 100% throughput. We propose what we believe is the first feasible scheduling scheme that can achieve 100% throughput without speedup and a finite crosspoint buffer. The proposed scheme is called SQUISH: a Stable Queue Input-output Scheduler with Hamiltonian walk. With SQUISH, each input/output first makes decisions based on the information from the virtual output queues and crosspoint buffers. Then it is compared with a Hamiltonian walk schedule to avoid possible "bad" states. We then prove that SQUISH can achieve 100% throughput with a speedup of one. Our simulation results also show good delay performance for SQUISH.
 
## Citation
- **Journal:** 2007 Workshop on High Performance Switching and Routing
- **Year:** 2007
- **Volume:** 
- **Issue:** 
- **Pages:** 1--8
- **Publisher:** IEEE
- **DOI:** [10.1109/hpsr.2007.4281262](https://doi.org/10.1109/hpsr.2007.4281262)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Shen_2007,
  title={{Providing 100% Throughput in a Buffered Crossbar Switch}},
  DOI={10.1109/hpsr.2007.4281262},
  booktitle={{2007 Workshop on High Performance Switching and Routing}},
  publisher={IEEE},
  author={Shen, Yanming and Panwar, Shivendra S. and Chao, H. Jonathan},
  year={2007},
  pages={1--8}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/providing-100-throughput-in-a-buffered-crossbar-switch.bib)
 
## References
- li, Exhaustive service matching algorithms for input queued switches. Proceedings of IEEE IEEE Workshop on High Performance Switching and Routing (2004)
- chuang, Practical algorithms for performance guarantees in buffered crossbars. Proceedings of IEEE Infocom (2005)
- Turner, J. Strong Performance Guarantees for Asynchronous Crossbar Schedulers. Proceedings IEEE INFOCOM 2006. 25TH IEEE International Conference on Computer Communications 1–11 (2006) doi:10.1109/infocom.2006.135 -- [10.1109/infocom.2006.135](https://doi.org/10.1109/infocom.2006.135)
- Berger, M. S. Delivering 100% throughput in a buffered crossbar with round robin scheduling. 2006 Workshop on High Performance Switching and Routing 5 pp. (2006) doi:10.1109/hpsr.2006.1709743 -- [10.1109/hpsr.2006.1709743](https://doi.org/10.1109/hpsr.2006.1709743)
- Javidi, T., Magill, R. & Hrabik, T. A high-throughput scheduling algorithm for a buffered crossbar switch fabric. ICC 2001. IEEE International Conference on Communications. Conference Record (Cat. No.01CH37240) vol. 5 1586–1591 -- [10.1109/icc.2001.937187](https://doi.org/10.1109/icc.2001.937187)
- Rojas-Cessa, R., Oki, E. & Chao, H. J. On the Combined Input-Crosspoint Buffered Switch With Round-Robin Arbitration. IEEE Trans. Commun. 53, 1945–1951 (2005) -- [10.1109/tcomm.2005.858667](https://doi.org/10.1109/tcomm.2005.858667)
- Giaccone, P., Leonardi, E. & Shah, D. On the maximal throughput of networks with finite buffers and its application to buffered crossbars. Proceedings IEEE 24th Annual Joint Conference of the IEEE Computer and Communications Societies. vol. 2 971–980 -- [10.1109/infcom.2005.1498326](https://doi.org/10.1109/infcom.2005.1498326)
- nijenhuis, Combinatorial algorithms: for computers and calculators. (1978)
- Rojas-Cessa, R., Oki, E., Zhigang Jing & Chao, H. J. CIXB-1: combined input-one-cell-crosspoint buffered switch. 2001 IEEE Workshop on High Performance Switching and Routing (IEEE Cat. No.01TH8552) 324–329 doi:10.1109/hpsr.2001.923655 -- [10.1109/hpsr.2001.923655](https://doi.org/10.1109/hpsr.2001.923655)
- Baranowska, A. et al. Performance evaluation of the multiple output queueing switch under different traffic patterns. GLOBECOM ’05. IEEE Global Telecommunications Conference, 2005. 5 pp. – 613 (2005) doi:10.1109/glocom.2005.1577696 -- [10.1109/glocom.2005.1577696](https://doi.org/10.1109/glocom.2005.1577696)
- Dai, J. G. & Prabhakar, B. The throughput of data switches with and without speedup. Proceedings IEEE INFOCOM 2000. Conference on Computer Communications. Nineteenth Annual Joint Conference of the IEEE Computer and Communications Societies (Cat. No.00CH37064) vol. 2 556–564 -- [10.1109/infcom.2000.832229](https://doi.org/10.1109/infcom.2000.832229)
- McKeown, N., Mekkittikul, A., Anantharam, V. & Walrand, J. Achieving 100% throughput in an input-queued switch. IEEE Trans. Commun. 47, 1260–1267 (1999) -- [10.1109/26.780463](https://doi.org/10.1109/26.780463)
- McKeown, N. The iSLIP scheduling algorithm for input-queued switches. IEEE/ACM Trans. Networking 7, 188–201 (1999) -- [10.1109/90.769767](https://doi.org/10.1109/90.769767)
- Leonardi, E., Mellia, M., Neri, F. & Marsan, M. A. On the stability of input-queued switches with speed-up. IEEE/ACM Trans. Networking 9, 104–118 (2001) -- [10.1109/90.909028](https://doi.org/10.1109/90.909028)
- Tassiulas, L. Linear complexity algorithms for maximum throughput in radio networks and input queued switches. Proceedings. IEEE INFOCOM ’98, the Conference on Computer Communications. Seventeenth Annual Joint Conference of the IEEE Computer and Communications Societies. Gateway to the 21st Century (Cat. No.98CH36169) vol. 2 533–539 -- [10.1109/infcom.1998.665071](https://doi.org/10.1109/infcom.1998.665071)
- li, On the performance of a dual round-robin switch. Proceedings of IEEE INFOCOM 2001 (2001)
- Tassiulas, L. & Ephremides, A. Stability properties of constrained queueing systems and scheduling policies for maximum throughput in multihop radio networks. IEEE Trans. Automat. Contr. 37, 1936–1948 (1992) -- [10.1109/9.182479](https://doi.org/10.1109/9.182479)
- Karol, M., Hluchyj, M. & Morgan, S. Input Versus Output Queueing on a Space-Division Packet Switch. IEEE Trans. Commun. 35, 1347–1356 (1987) -- [10.1109/tcom.1987.1096719](https://doi.org/10.1109/tcom.1987.1096719)
- giaccone, Toward simple, highperformance schedulers for high-aggregate bandwidth switches. Proc IEEE Infocom IEEE (2002)
- Mhamdi, L. & Hamdi, M. MCBF: a high-performance scheduling algorithm for buffered crossbar switches. IEEE Commun. Lett. 7, 451–453 (2003) -- [10.1109/lcomm.2003.815665](https://doi.org/10.1109/lcomm.2003.815665)
- Kumar, P. R. & Meyn, S. P. Stability of queueing networks and scheduling policies. IEEE Trans. Automat. Contr. 40, 251–260 (1995) -- [10.1109/9.341782](https://doi.org/10.1109/9.341782)

