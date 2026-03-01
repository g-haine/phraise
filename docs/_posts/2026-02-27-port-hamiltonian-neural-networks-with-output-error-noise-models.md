---
title: "Port-Hamiltonian neural networks with output error noise models"
date: 2026-02-27 00:00:00 +0100
permalink: port-hamiltonian-neural-networks-with-output-error-noise-models
year: 2026
authors: Sarvin Moradi, Gerben I. Beintema, Nick O. Jaensson, Roland Tóth, Maarten Schoukens
category: articles
tags:
  - machine learning, nonlinear system identification, port-hamiltonian neural networks, port-hamiltonian theory
---
 
## Authors
[Sarvin Moradi](authors/sarvin-moradi), [Gerben I. Beintema](authors/gerben-izaak-beintema), [Nick O. Jaensson](authors/nick-o-jaensson), [Roland Tóth](authors/roland-toth), [Maarten Schoukens](authors/maarten-schoukens)
 
## Abstract
Hamiltonian neural networks (HNNs) represent a promising class of physics-informed deep learning methods that utilize Hamiltonian theory as foundational knowledge within neural networks. However, their direct application to engineering systems is often challenged by practical issues, including the presence of external inputs, dissipation, and noisy measurements. This paper introduces a novel framework that enhances the capabilities of HNNs to address these real-life factors. We integrate port-Hamiltonian theory into the neural network structure, allowing for the inclusion of external inputs and dissipation, while mitigating the impact of measurement noise through an output-error (OE) model structure. The resulting output error port-Hamiltonian neural networks (OE-pHNNs) can be adapted to tackle modeling complex engineering systems with noisy measurements. Furthermore, we propose the identification of OE-pHNNs based on the subspace encoder approach (SUBNET), which efficiently approximates the complete simulation loss using subsections of the data and uses an encoder function to predict initial states. By integrating SUBNET with OE-pHNNs, we achieve consistent models of complex engineering systems under noisy measurements. In addition, we perform a consistency analysis to ensure the reliability of the proposed data-driven model learning method. We demonstrate the effectiveness of our approach on system identification benchmarks, showing its potential as a powerful tool for modeling dynamic systems in real-world applications.
 
## Keywords
machine learning, nonlinear system identification, port-hamiltonian neural networks, port-hamiltonian theory
 
## Citation
- **Journal:** Automatica
- **Year:** 2026
- **Volume:** 187
- **Issue:** 
- **Pages:** 112892
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2026.112892](https://doi.org/10.1016/j.automatica.2026.112892)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Moradi_2026,
  title={{Port-Hamiltonian neural networks with output error noise models}},
  volume={187},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2026.112892},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Moradi, Sarvin and Beintema, Gerben I. and Jaensson, Nick O. and Tóth, Roland and Schoukens, Maarten},
  year={2026},
  pages={112892}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-neural-networks-with-output-error-noise-models.bib)
 
## References
- Atkinson, An introduction to numerical analysis. (1991)
- Beintema GI, Schoukens M, Tóth R (2023) Deep subspace encoders for nonlinear system identification. Automatica 156:111210. https://doi.org/10.1016/j.automatica.2023.11121 -- [10.1016/j.automatica.2023.111210](https://doi.org/10.1016/j.automatica.2023.111210)
- Billings, (2013)
- Butcher, Differential & difference equations. (2003)
- Champneys M, Beintema GI, Tóth R, Schoukens M, Rogers TJ (2024) Baseline Results for Selected Nonlinear System Identification Benchmarks. IFAC-PapersOnLine 58(15):474–479. https://doi.org/10.1016/j.ifacol.2024.08.57 -- [10.1016/j.ifacol.2024.08.574](https://doi.org/10.1016/j.ifacol.2024.08.574)
- Cheng CM, Peng ZK, Zhang WM, Meng G (2017) Volterra-series-based nonlinear system modeling and its engineering applications: A state-of-the-art review. Mechanical Systems and Signal Processing 87:340–364. https://doi.org/10.1016/j.ymssp.2016.10.02 -- [10.1016/j.ymssp.2016.10.029](https://doi.org/10.1016/j.ymssp.2016.10.029)
- Cherifi, (2025)
- Choudhary A, Lindner JF, Holliday EG, Miller ST, Sinha S, Ditto WL (2020) Physics-enhanced neural networks learn order and chaos. Phys Rev E 101(6). https://doi.org/10.1103/physreve.101.06220 -- [10.1103/physreve.101.062207](https://doi.org/10.1103/physreve.101.062207)
- [Desai SA, Mattheakis M, Sondak D, Protopapas P, Roberts SJ (2021) Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Phys Rev E 104(3). https://doi.org/10.1103/physreve.104.03431](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Forgione M, Piga D (2021) Continuous-time system identification with neural networks: Model structures and fitting criteria. European Journal of Control 59:69–81. https://doi.org/10.1016/j.ejcon.2021.01.00 -- [10.1016/j.ejcon.2021.01.008](https://doi.org/10.1016/j.ejcon.2021.01.008)
- Han C-D, Glaz B, Haile M, Lai Y-C (2021) Adaptable Hamiltonian neural networks. Phys Rev Research 3(2). https://doi.org/10.1103/physrevresearch.3.02315 -- [10.1103/physrevresearch.3.023156](https://doi.org/10.1103/physrevresearch.3.023156)
- Karagoz R, Batselier K (2020) Nonlinear system identification with regularized Tensor Network B-splines. Automatica 122:109300. https://doi.org/10.1016/j.automatica.2020.10930 -- [10.1016/j.automatica.2020.109300](https://doi.org/10.1016/j.automatica.2020.109300)
- Kon J, Tóth R, van de Wijdeven J, Heertjes M, Oomen T (2024) Guaranteeing Stability in Structured Input-Output Models: With Application to System Identification. IEEE Control Syst Lett 8:1565–1570. https://doi.org/10.1109/lcsys.2024.341014 -- [10.1109/lcsys.2024.3410143](https://doi.org/10.1109/lcsys.2024.3410143)
- Ljung L (1978) Convergence analysis of parametric identification methods. IEEE Trans Automat Contr 23(5):770–783. https://doi.org/10.1109/tac.1978.110184 -- [10.1109/tac.1978.1101840](https://doi.org/10.1109/tac.1978.1101840)
- Ljung, (1995)
- Ljung L (2010) Perspectives on system identification. Annual Reviews in Control 34(1):1–12. https://doi.org/10.1016/j.arcontrol.2009.12.00 -- [10.1016/j.arcontrol.2009.12.001](https://doi.org/10.1016/j.arcontrol.2009.12.001)
- Moradi S, Jaensson N, Tóth R, Schoukens M (2023) Physics-Informed Learning Using Hamiltonian Neural Networks with Output Error Noise Models. IFAC-PapersOnLine 56(2):5152–5157. https://doi.org/10.1016/j.ifacol.2023.10.10 -- [10.1016/j.ifacol.2023.10.108](https://doi.org/10.1016/j.ifacol.2023.10.108)
- Murray, (2013)
- Noronha, (2023)
- Pintelon, (2012)
- Rogers TJ, Holmes GR, Cross EJ, Worden K (2025) On a Grey Box Modelling Framework for Nonlinear System Identification. Special Topics in Structural Dynamics, Volume 6 167–17 -- [10.1007/978-3-319-53841-9_15](https://doi.org/10.1007/978-3-319-53841-9_15)
- Schön TB, Wills A, Ninness B (2011) System identification of nonlinear state-space models. Automatica 47(1):39–49. https://doi.org/10.1016/j.automatica.2010.10.01 -- [10.1016/j.automatica.2010.10.013](https://doi.org/10.1016/j.automatica.2010.10.013)
- Schoukens J, Ljung L (2019) Nonlinear System Identification: A User-Oriented Road Map. IEEE Control Syst 39(6):28–99. https://doi.org/10.1109/mcs.2019.293812 -- [10.1109/mcs.2019.2938121](https://doi.org/10.1109/mcs.2019.2938121)
- Sosanya, (2022)
- Svensson A, Schön TB (2017) A flexible state–space model for learning nonlinear dynamical systems. Automatica 80:189–199. https://doi.org/10.1016/j.automatica.2017.02.03 -- [10.1016/j.automatica.2017.02.030](https://doi.org/10.1016/j.automatica.2017.02.030)
- Tóth, (2010)
- van der Schaft, (2014)
- van Otterdijk, (2024)
- Weigand J, Deflorian M, Ruskowski M (2021) Input-to-state stability for system identification with continuous-time Runge–Kutta neural networks. International Journal of Control 96(1):24–40. https://doi.org/10.1080/00207179.2021.197855 -- [10.1080/00207179.2021.1978555](https://doi.org/10.1080/00207179.2021.1978555)
- Xiao, (2024)

