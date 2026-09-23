---
title: "Towards Step-size-free Distributed Optimization: a Port-Hamiltonian Approach"
date: 2026-04-23 00:00:00 +0100
permalink: towards-step-size-free-distributed-optimization-a-port-hamiltonian-approach
year: 2026
authors: Rodrigo Aldana-López, Alessandro Macchelli, Giuseppe Notarstefano, Rosario Aragüés, Carlos Sagüés
category: articles
---
 
## Authors
[Rodrigo Aldana-López](authors/rodrigo-aldana-lopez), [Alessandro Macchelli](authors/alessandro-macchelli), [Giuseppe Notarstefano](authors/giuseppe-notarstefano), [Rosario Aragüés](authors/rosario-aragues), [Carlos Sagüés](authors/carlos-sagues)
 
## Abstract
This paper presents a novel distributed optimization technique that, under suitable assumptions on problem and communication graph, is able to operate with any step-size parameter, a capability not evident in previous methods. Traditionally, selecting the step-size in distributed optimization often leads to a conservative performance, resulting in slow convergence or even divergence if the step-size is incorrectly chosen. In this work, we propose a systems theory approach based on the port-Hamiltonian formalism to develop algorithms for consensus optimization problems. Starting from a continuous-time flow, we propose a distributed algorithm based on a discretized Port-Hamiltonian system that works regardless of the step size. Additionally, we introduce Mixed Implicit Discretization, which lowers communication overhead while maintaining, under suitable conditions, the ability to converge with any step size. This feature is formally verified in specific scenarios and demonstrated experimentally in general cases with large step sizes. These results illustrate that the proposed method can utilize step sizes several orders of magnitude larger than those in previous work, where conventional methods fail, ultimately enhancing convergence speed.
 
## Citation
- **Journal:** IEEE Transactions on Automatic Control
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 1--15
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tac.2026.3687481](https://doi.org/10.1109/tac.2026.3687481)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Aldana_L_pez_2026,
  title={{Towards Step-size-free Distributed Optimization: a Port-Hamiltonian Approach}},
  ISSN={2334-3303},
  DOI={10.1109/tac.2026.3687481},
  journal={IEEE Transactions on Automatic Control},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Aldana-López, Rodrigo and Macchelli, Alessandro and Notarstefano, Giuseppe and Aragüés, Rosario and Sagüés, Carlos},
  year={2026},
  pages={1--15}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/towards-step-size-free-distributed-optimization-a-port-hamiltonian-approach.bib)
 
