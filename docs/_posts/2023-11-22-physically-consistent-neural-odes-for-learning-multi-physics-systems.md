---
layout: post
title: "Physically Consistent Neural ODEs for Learning Multi-Physics Systems"
date: 2023-11-22 00:00:00 +0100
permalink: physically-consistent-neural-odes-for-learning-multi-physics-systems
year: 2023
authors: M. Zakwan, L. Di Natale, B. Svetozarevic, P. Heer, C.N. Jones, G. Ferrari Trecate
category: journal-article
tag: Machine Learning; Neural networks; Multi-physics; Thermodynamics; Data-driven Modelling; Irreversible port-Hamiltonian systems
---
 
## Authors
[M. Zakwan](authors/muhammad-zakwan), [L. Di Natale](authors/l-di-natale), [B. Svetozarevic](authors/b-svetozarevic), [P. Heer](authors/p-heer), [C.N. Jones](authors/c-n-jones), [G. Ferrari Trecate](authors/g-ferrari-trecate)
 
## Abstract
Despite the immense success of neural networks in modeling system dynamics from data, they often remain physics-agnostic black boxes. In the particular case of physical systems, they might consequently make physically inconsistent predictions, which makes them unreliable in practice. In this paper, we leverage the framework of Irreversible port-Hamiltonian Systems (IPHS), which can describe most multi-physics systems, and rely on Neural Ordinary Differential Equations (NODEs) to learn their parameters from data. Since IPHS models are consistent with the first and second principles of thermodynamics by design, so are the proposed Physically Consistent NODEs (PC-NODEs). Furthermore, the NODE training procedure allows us to seamlessly incorporate prior knowledge of the system properties in the learned dynamics. We demonstrate the effectiveness of the proposed method by learning the thermodynamics of a building from the real-world measurements and the dynamics of a simulated gas-piston system. Thanks to the modularity and flexibility of the IPHS framework, PC-NODEs can be extended to learn physically consistent models of multi-physics distributed systems.
 
## Keywords
Machine Learning; Neural networks; Multi-physics; Thermodynamics; Data-driven Modelling; Irreversible port-Hamiltonian systems
 
## Citation
- **Journal:** IFAC-PapersOnLine
- **Year:** 2023
- **Volume:** 56
- **Issue:** 2
- **Pages:** 5855--5860
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ifacol.2023.10.079](https://doi.org/10.1016/j.ifacol.2023.10.079)
- **Note:** 22nd IFAC World Congress- Yokohama, Japan, July 9-14, 2023
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Zakwan_2023,
  title={{Physically Consistent Neural ODEs for Learning Multi-Physics Systems*}},
  volume={56},
  ISSN={2405-8963},
  DOI={10.1016/j.ifacol.2023.10.079},
  number={2},
  journal={IFAC-PapersOnLine},
  publisher={Elsevier BV},
  author={Zakwan, M. and Natale, L. Di and Svetozarevic, B. and Heer, P. and Jones, C.N. and Trecate, G. Ferrari},
  year={2023},
  pages={5855--5860}
}
{% endraw %}
{% endhighlight %}
 
## References
- Di Natale, L., Svetozarevic, B., Heer, P. & Jones, C. N. Physically Consistent Neural Networks for building thermal modeling: Theory and analysis. Applied Energy vol. 325 119806 (2022) -- [10.1016/j.apenergy.2022.119806](https://doi.org/10.1016/j.apenergy.2022.119806)
- Empa (2021). NEST. Accessed: 01.10.2022. URL https://www.empa.ch/web/nest/overview.
- Fazlyab, M., Morari, M. & Pappas, G. J. Safety Verification and Robustness Analysis of Neural Networks via Quadratic Constraints and Semidefinite Programming. IEEE Transactions on Automatic Control vol. 67 1–15 (2022) -- [10.1109/TAC.2020.3046193](https://doi.org/10.1109/TAC.2020.3046193)
- Geirhos, R. et al. Shortcut learning in deep neural networks. Nature Machine Intelligence vol. 2 665–673 (2020) -- [10.1038/s42256-020-00257-z](https://doi.org/10.1038/s42256-020-00257-z)
- Haber, E. & Ruthotto, L. Stable architectures for deep neural networks. Inverse Problems vol. 34 014004 (2017) -- [10.1088/1361-6420/aa9a90](https://doi.org/10.1088/1361-6420/aa9a90)
- Masi, F., Stefanou, I., Vannucci, P. & Maffi-Berthier, V. Thermodynamics-based Artificial Neural Networks for constitutive modeling. Journal of the Mechanics and Physics of Solids vol. 147 104277 (2021) -- [10.1016/j.jmps.2020.104277](https://doi.org/10.1016/j.jmps.2020.104277)
- Merema, B., Saelens, D. & Breesch, H. Demonstration of an MPC framework for all-air systems in non-residential buildings. Building and Environment vol. 217 109053 (2022) -- [10.1016/j.buildenv.2022.109053](https://doi.org/10.1016/j.buildenv.2022.109053)
- Paszke, A., Gross, S., Chintala, S., Chanan, G., Yang, E., DeVito, Z., Lin, Z., Desmaison, A., Antiga, L., and Lerer, A. (2017). Automatic differentiation in pytorch. NIPS 2017 Autodiff Workshop.
- [Ramirez, H., Maschke, B. & Sbarbaro, D. Irreversible port-Hamiltonian systems: A general formulation of irreversible processes with application to the CSTR. Chemical Engineering Science vol. 89 223–234 (2013)](irreversible-port-hamiltonian-systems-a-general-formulation-of-irreversible-processes-with-application-to-the-cstr) -- [10.1016/j.ces.2012.12.002](https://doi.org/10.1016/j.ces.2012.12.002)
- [Ramirez, H., Maschke, B. & Sbarbaro, D. Modelling and control of multi-energy systems: An irreversible port-Hamiltonian approach. European Journal of Control vol. 19 513–520 (2013)](modelling-and-control-of-multi-energy-systems-an-irreversible-port-hamiltonian-approach) -- [10.1016/j.ejcon.2013.09.009](https://doi.org/10.1016/j.ejcon.2013.09.009)
- Zakwan, M., Xu, L. & Ferrari-Trecate, G. Robust Classification Using Contractive Hamiltonian Neural ODEs. IEEE Control Systems Letters vol. 7 145–150 (2023) -- [10.1109/LCSYS.2022.3186959](https://doi.org/10.1109/LCSYS.2022.3186959)

