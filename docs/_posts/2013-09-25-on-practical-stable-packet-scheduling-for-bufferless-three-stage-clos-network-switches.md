---
layout: post
title: "On practical stable packet scheduling for bufferless three-stage Clos-network switches"
date: 2013-09-25 00:00:00 +0100
permalink: on-practical-stable-packet-scheduling-for-bufferless-three-stage-clos-network-switches
year: 2013
authors: Yu Xia, H. Jonathan Chao
category: proceedings
---
 
## Authors
[Yu Xia](authors/yu-xia), [H. Jonathan Chao](authors/h-jonathan-chao)
 
## Abstract
In this paper, we extend our previous work of StablePlus, a stable scheduling algorithm for single-stage packet switches, to bufferless three-stage Clos-network switches. StablePlus is based on an existing stable distributed scheduling algorithm, called DISQUO. We further improve the switching performance by incorporating a heuristic scheduling algorithm after the DISQUO scheduling. In a three-stage Clos-network switch, DISQUO is first used to solve the output contention which generates a stable matching between the input and output ports, then Karol's algorithm is used to find the feasible internal paths for the matched input and output pairs. However, the latter requires multiple mini-cycles to complete the path-finding task. Worse is that the number of mini-cycles increases as the switch size does, limiting the Clos-network to a small implementable size. By replacing the Hamiltonian Walk in DISQUO with time-division multiplexing (TDM) scheme, we show that the number of required mini-cycles for Karol's algorithm can be reduced to only two, independent of the switch size. Moreover, with the help of a parallel hardware approach, we can implement packet scheduling in O(1) time complexity. To support high data rates, e.g., 100 Gbps, we can also make the scheduling work on a frame basis. We prove that StablePlus can achieve 100% throughput under any admissible traffic, and by simulations we show that it also has good delay performance.
 
## Citation
- **Journal:** 2013 IEEE 14th International Conference on High Performance Switching and Routing (HPSR)
- **Year:** 2013
- **Volume:** 
- **Issue:** 
- **Pages:** 7--14
- **Publisher:** IEEE
- **DOI:** [10.1109/hpsr.2013.6602283](https://doi.org/10.1109/hpsr.2013.6602283)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Xia_2013,
  title={{On practical stable packet scheduling for bufferless three-stage Clos-network switches}},
  DOI={10.1109/hpsr.2013.6602283},
  booktitle={{2013 IEEE 14th International Conference on High Performance Switching and Routing (HPSR)}},
  publisher={IEEE},
  author={Xia, Yu and Chao, H. Jonathan},
  year={2013},
  pages={7--14}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-practical-stable-packet-scheduling-for-bufferless-three-stage-clos-network-switches.bib)
 
## References
- Shen, Y., Panwar, S. & Chao, H. Design and performance analysis of a practical load-balanced switch. IEEE Trans. Commun. 57, 2420–2429 (2009) -- [10.1109/tcomm.2009.08.070477](https://doi.org/10.1109/tcomm.2009.08.070477)
- McKeown, N. The iSLIP scheduling algorithm for input-queued switches. IEEE/ACM Trans. Networking 7, 188–201 (1999) -- [10.1109/90.769767](https://doi.org/10.1109/90.769767)
- Rojas-Cessa, R., Oki, E. & Chao, H. J. On the Combined Input-Crosspoint Buffered Switch With Round-Robin Arbitration. IEEE Trans. Commun. 53, 1945–1951 (2005) -- [10.1109/tcomm.2005.858667](https://doi.org/10.1109/tcomm.2005.858667)
- Chao, H. J., Lam, C. H. & Guo, X. A fast arbitration scheme for terabit packet switches. Seamless Interconnection for Universal Services. Global Telecommunications Conference. GLOBECOM’99. (Cat. No.99CH37042) vol. 2 1236–1243 -- [10.1109/glocom.1999.829968](https://doi.org/10.1109/glocom.1999.829968)
- yu xia, Design and implementation of switch module for ns-3. Proc of VALUETOOLS 2009 (2009)
- Shunyuan Ye, Shen, Y. & Panwar, S. DISQUO: A distributed 100% throughput algorithm for a buffered crossbar switch. 2010 International Conference on High Performance Switching and Routing 75–81 (2010) doi:10.1109/hpsr.2010.5580261 -- [10.1109/hpsr.2010.5580261](https://doi.org/10.1109/hpsr.2010.5580261)
- Danger, J.-L., Guilley, S. & Hoogvorst, P. High speed true random number generator based on open loop structures in FPGAs. Microelectronics Journal 40, 1650–1656 (2009) -- [10.1016/j.mejo.2009.02.004](https://doi.org/10.1016/j.mejo.2009.02.004)
- Zheng, S. Q., Gumaste, A. & Lu, E. A practical fast parallel routing architecture for Clos networks. Proceedings of the 2006 ACM/IEEE symposium on Architecture for networking and communications systems 21–30 (2006) doi:10.1145/1185347.1185351 -- [10.1145/1185347.1185351](https://doi.org/10.1145/1185347.1185351)
- Hyun Yeop Lee, Hwang, F. K. & Carpinelli, J. D. A new decomposition algorithm for rearrangeable Clos interconnection networks. IEEE Trans. Commun. 44, 1572–1578 (1996) -- [10.1109/26.544474](https://doi.org/10.1109/26.544474)
- McKeown, N., Mekkittikul, A., Anantharam, V. & Walrand, J. Achieving 100% throughput in an input-queued switch. IEEE Trans. Commun. 47, 1260–1267 (1999) -- [10.1109/26.780463](https://doi.org/10.1109/26.780463)
- Pfister, G. F. & Norton, V. A. “Hot spot” contention and combining in multistage interconnection networks. IEEE Trans. Comput. C–34, 943–948 (1985) -- [10.1109/tc.1985.6312198](https://doi.org/10.1109/tc.1985.6312198)
- Leland, W. E., Taqqu, M. S., Willinger, W. & Wilson, D. V. On the self-similar nature of Ethernet traffic (extended version). IEEE/ACM Trans. Networking 2, 1–15 (1994) -- [10.1109/90.282603](https://doi.org/10.1109/90.282603)
- Chao, H. J. & Park, J. Flow Control in a Multi-Plane Multi-Stage Buffered Packet Switch. 2007 Workshop on High Performance Switching and Routing 1–6 (2007) doi:10.1109/hpsr.2007.4281256 -- [10.1109/hpsr.2007.4281256](https://doi.org/10.1109/hpsr.2007.4281256)
- MoSys 1T-SRAM (0)
- Karol, M. J. & Chih-Lin I. Performance analysis of a growable architecture for broadband packet (ATM) switching. IEEE Global Telecommunications Conference, 1989, and Exhibition. ’Communications Technology for the 1990s and Beyond 1173–1180 doi:10.1109/glocom.1989.64140 -- [10.1109/glocom.1989.64140](https://doi.org/10.1109/glocom.1989.64140)
- xia, Stableplus: A practical 100% throughput scheduling for input-queued switches. Proc of IEEE HPSR 2011 (2011)
- chrysos, End-to-end congestion management for non-blocking, multistage switching fabrics. Sympsium of ANCS 2010 (2010)
- chrysos, Congestion management for nonblocking clos networks. Symposium of ANCS 2007 (2007)
- Chrysos, N. & Katevenis, M. Scheduling in Non-Blocking Buffered Three-Stage Switching Fabrics. Proceedings IEEE INFOCOM 2006. 25TH IEEE International Conference on Computer Communications 1–13 (2006) doi:10.1109/infocom.2006.134 -- [10.1109/infocom.2006.134](https://doi.org/10.1109/infocom.2006.134)
- Xi, K., Kao, Y.-H. & Chao, H. J. A Petabit Bufferless Optical Switch for Data Center Networks. Optical Networks 135–154 (2012) doi:10.1007/978-1-4614-4630-9_8 -- [10.1007/978-1-4614-4630-9_8](https://doi.org/10.1007/978-1-4614-4630-9_8)
- Vsc3144 (0)

