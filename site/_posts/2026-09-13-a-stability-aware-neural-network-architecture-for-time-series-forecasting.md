---
title: "A Stability-Aware Neural Network Architecture for Time Series Forecasting"
date: 2026-09-13 00:00:00 +0100
permalink: a-stability-aware-neural-network-architecture-for-time-series-forecasting
year: 2027
authors: Eric Wang, Jiang Li
category: proceedings
tags:
  - attention, port-hamiltonian neural networks, stability, stochastic modeling, structured dynamics, time series forecasting
---
 
## Authors
[Eric Wang](authors/eric-wang), [Jiang Li](authors/jiang-li)
 
## Abstract
Time series forecasting models often struggle to remain stable over long horizons, especially for physical and stochastic systems where dynamics are structured but uncertain. We propose a stability-aware neural network architecture for time series forecasting, instantiated as Attention-Augmented Stochastic Port-Hamiltonian Neural Networks (ASpHNN), which captures long-range temporal dependencies while respecting energy structure. ASpHNN combines a stochastic port-Hamiltonian backbone with an attention-driven input port and a learnable diffusion term to model history-dependent forcing and uncertainty. The model is trained with one-step prediction and moment-matching losses together with energy- and structure-regularization. We provide an expectation-level passivity and energy-balance analysis, and further study an implicit midpoint discretization in the supplementary appendix. Experiments on five standard multivariate forecasting benchmarks (Weather, Traffic, ETTm1, Electricity, and Exchange Rate) under a small-sample setting show that ASpHNN outperforms strong Transformer and linear baselines on four datasets while remaining competitive on Exchange Rate.
 
## Keywords
attention, port-hamiltonian neural networks, stability, stochastic modeling, structured dynamics, time series forecasting
 
## Citation
- **ISBN:** 9783032384003
- **Publisher:** Springer Nature Switzerland
- **DOI:** [10.1007/978-3-032-38401-0_5](https://doi.org/10.1007/978-3-032-38401-0_5)
- **Note:** International Conference on Artificial Neural Networks
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inbook{Wang_2026,
  title={{A Stability-Aware Neural Network Architecture for Time Series Forecasting}},
  ISBN={9783032384010},
  ISSN={1611-3349},
  DOI={10.1007/978-3-032-38401-0_5},
  booktitle={{Artificial Neural Networks and Machine Learning – ICANN 2026}},
  publisher={Springer Nature Switzerland},
  author={Wang, Eric and Li, Jiang},
  year={2026},
  pages={54--66}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-stability-aware-neural-network-architecture-for-time-series-forecasting.bib)
 
## References
- Akiba T, Sano S, Yanase T, Ohta T, Koyama M (2019) Optuna. Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining 2623–2631 -- [10.1145/3292500.3330701](https://doi.org/10.1145/3292500.3330701)
- Benidis, K., et al.: Neural forecasting: introduction and literature overview, vol. 6, p. 1. arXiv preprint arXiv:2004.10240 (2020)
- Chiu P-H, Wong JC, Ooi C, Dao MH, Ong Y-S (2022) CAN-PINN: A fast physics-informed neural network based on coupled-automatic–numerical differentiation method. Computer Methods in Applied Mechanics and Engineering 395:114909. https://doi.org/10.1016/j.cma.2022.114909 -- [10.1016/j.cma.2022.114909](https://doi.org/10.1016/j.cma.2022.114909)
- Persio LD, Ehrhardt M, Outaleb Y, Rizzotto S (2025) Port-Hamiltonian Neural Networks: From Theory to Simulation of Interconnected Stochastic Systems -- [10.21203/rs.3.rs-7572939/v1](https://doi.org/10.21203/rs.3.rs-7572939/v1)
- Persio, D., Ehrhardt, L., Rizzotto, M., S.: Integrating port-hamiltonian systems with neural networks: from deterministic to stochastic frameworks. arXiv preprint arXiv:2403.16737 (2024)
- Farea A, Yli-Harja O, Emmert-Streib F (2024) Understanding Physics-Informed Neural Networks: Techniques, Applications, Trends, and Challenges. AI 5(3):1534–1557. https://doi.org/10.3390/ai5030074 -- [10.3390/ai5030074](https://doi.org/10.3390/ai5030074)
- Jia F, Wang K, Zheng Y, Cao D, Liu Y (2024) GPT4MTS: Prompt-based Large Language Model for Multimodal Time-series Forecasting. AAAI 38(21):23343–23351. https://doi.org/10.1609/aaai.v38i21.30383 -- [10.1609/aaai.v38i21.30383](https://doi.org/10.1609/aaai.v38i21.30383)
- Jin, M., et al.: Time-llm: time series forecasting by reprogramming large language models. In: International Conference on Learning Representations (ICLR) (2024)
- Jin, M., et al.: Large models for time series and spatio-temporal data: a survey and outlook. arXiv preprint arXiv:2310.10196 (2023)
- Lawal ZK, Yassin H, Lai DTC, Che Idris A (2022) Physics-Informed Neural Network (PINN) Evolution and Beyond: A Systematic Literature Review and Bibliometric Analysis. BDCC 6(4):140. https://doi.org/10.3390/bdcc6040140 -- [10.3390/bdcc6040140](https://doi.org/10.3390/bdcc6040140)
- Lim B, Zohren S (2021) Time-series forecasting with deep learning: a survey. Phil Trans R Soc A 379(2194):20200209. https://doi.org/10.1098/rsta.2020.0209 -- [10.1098/rsta.2020.0209](https://doi.org/10.1098/rsta.2020.0209)
- Liu, Y., Zhang, H., Li, C., Huang, X., Wang, J., Long, M.: Timer: generative pre-trained transformers are large time series models. arXiv preprint arXiv:2402.02368 (2024)
- Lorenz, E.N.: Predictability: a problem partly solved. In: Proceedings of the Seminar on Predictability, vol. 1, pp. 1–18 (1996)
- Mahmoud A, Mohammed A (2020) A Survey on Deep Learning for Time-Series Forecasting. Studies in Big Data 365–392 -- [10.1007/978-3-030-59338-4_19](https://doi.org/10.1007/978-3-030-59338-4_19)
- Nie, Y., Nguyen, N.H., Sinthong, P., Kalagnanam, J.: A time series is worth 64 words: long-term forecasting with transformers. arXiv preprint arXiv:2211.14730 (2022)
- Pan, Z., Jiang, Y., Garg, S., Schneider, A., Nevmyvaka, Y., Song, D.: S2 IP-LLM: semantic space informed prompt learning with llm for time series forecasting. In: Forty-First International Conference on Machine Learning (2024)
- Su, J., et al.: Large language models for forecasting and anomaly detection: a systematic literature review. arXiv preprint arXiv:2402.10350 (2024)
- Tan M, Merrill M, Gupta V, Althoff T, Hartvigsen T (2024) Are Language Models Actually Useful for Time Series Forecasting? Advances in Neural Information Processing Systems 37 60162–60191 -- [10.52202/079017-1922](https://doi.org/10.52202/079017-1922)
- Toscano JD, Oommen V, Varghese AJ, Zou Z, Ahmadi Daryakenari N, Wu C, Karniadakis GE (2025) From PINNs to PIKANs: recent advances in physics-informed machine learning. Mach Learn Comput Sci Eng 1(1). https://doi.org/10.1007/s44379-025-00015-1 -- [10.1007/s44379-025-00015-1](https://doi.org/10.1007/s44379-025-00015-1)
- Toth, P., Rezende, D.J., Jaegle, A., Racanière, S., Botev, A., Higgins, I.: Hamiltonian generative networks. arXiv preprint arXiv:1909.13789 (2019)
- Vaswani, A., et al.: Attention is all you need. Adv. Neural Inf. Process. Syst. 5998–6008 (2017)
- Wilks DS (2005) Effects of stochastic parametrizations in the Lorenz ’96 system. Quart J Royal Meteoro Soc 131(606):389–407. https://doi.org/10.1256/qj.04.03 -- [10.1256/qj.04.03](https://doi.org/10.1256/qj.04.03)
- Wu, H., Xu, J., Wang, J., Long, M.: Autoformer: decomposition transformers with auto-correlation for long-term series forecasting. Adv. Neural Inf. Process. Syst. 34, 22419–22430 (2021)
- Zeng A, Chen M, Zhang L, Xu Q (2023) Are Transformers Effective for Time Series Forecasting? AAAI 37(9):11121–11128. https://doi.org/10.1609/aaai.v37i9.26317 -- [10.1609/aaai.v37i9.26317](https://doi.org/10.1609/aaai.v37i9.26317)
- Zhou H, Zhang S, Peng J, Zhang S, Li J, Xiong H, Zhang W (2021) Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. AAAI 35(12):11106–11115. https://doi.org/10.1609/aaai.v35i12.17325 -- [10.1609/aaai.v35i12.17325](https://doi.org/10.1609/aaai.v35i12.17325)

