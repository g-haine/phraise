---
layout: post
title: "Physics-guided and Energy-based Learning of Interconnected Systems: from Lagrangian to Port-Hamiltonian Systems"
date: 2023-01-10 00:00:00 +0100
permalink: physics-guided-and-energy-based-learning-of-interconnected-systems-from-lagrangian-to-port-hamiltonian-systems
year: 2022
authors: Yajie Bao, Vaishnavi Thesma, Atul Kelkar, Javad Mohammadpour Velni
category:
  - proceedings
---
 
## Authors
[Yajie Bao](authors/yajie_bao), [Vaishnavi Thesma](authors/vaishnavi_thesma), [Atul Kelkar](authors/atul_kelkar), [Javad Mohammadpour Velni](authors/javad_mohammadpour_velni)
 
## Abstract
This paper presents a framework for physics-informed energy-based neural network (NN) design to learn models of interconnected systems under the port-Hamiltonian (pH) formalism. In particular, this paper focuses on mechanical systems and incorporates the physical knowledge of Lagrangians into the neural networks to facilitate learning of equations of motion from the data. Moreover, the transformation from the Lagrangian mechanics to the Hamiltonian mechanics is incorporated into the NN architecture and learned from the data such that the learned model is compatible with the pH framework. Then, the structure of input-state-output pH models is imposed on the NN, which guarantees the dissipativity of the learned model. Furthermore, modeling interconnected systems is facilitated by the compositionality property of the pH systems. Additionally, the consistency between the Hamiltonian and Lagrangian is employed for the energy estimation to enable energy-based control. The proposed approach is shown to be computationally more efficient than the existing Lagrangian-based NN design approaches. Furthermore, the learned models with energy estimation are employed for energy-based model predictive control (MPC) design purpose. Experimental results using single (and double) inverted pendulum on carts show that the proposed learning-based approach can achieve an improved performance of model identification compared to the Lagrangian neural networks, accurate estimation of energies and strong control performance.
 
## Citation
- **Journal:** 2022 IEEE 61st Conference on Decision and Control (CDC)
- **Year:** 2022
- **Volume:** 
- **Issue:** 
- **Pages:** 2815--2820
- **Publisher:** IEEE
- **DOI:** [10.1109/CDC51059.2022.9992803](https://doi.org/10.1109/CDC51059.2022.9992803)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Bao_2022,
  title={{Physics-guided and Energy-based Learning of Interconnected Systems: from Lagrangian to Port-Hamiltonian Systems}},
  DOI={10.1109/cdc51059.2022.9992803},
  booktitle={{2022 IEEE 61st Conference on Decision and Control (CDC)}},
  publisher={IEEE},
  author={Bao, Yajie and Thesma, Vaishnavi and Kelkar, Atul and Velni, Javad Mohammadpour},
  year={2022},
  pages={2815--2820}
}
{% endraw %}
{% endhighlight %}
 
## References
- Bertalan, T., Dietrich, F., Mezić, I. & Kevrekidis, I. G. On learning Hamiltonian systems from data. Chaos: An Interdisciplinary Journal of Nonlinear Science vol. 29 (2019) -- [10.1063/1.5128231](https://doi.org/10.1063/1.5128231)
- Bao, Y., Thesma, V. & Velni, J. M. Physics-guided and Neural Network Learning-based Sliding Mode Control. IFAC-PapersOnLine vol. 54 705–710 (2021) -- [10.1016/j.ifacol.2021.11.254](https://doi.org/10.1016/j.ifacol.2021.11.254)
- [van der Schaft, A. Port-Hamiltonian systems: an introductory survey. Proceedings of the International Congress of Mathematicians Madrid, August 22–30, 2006 1339–1365 (2007) doi:10.4171/022-3/65](port-hamiltonian-systems-an-introductory-survey) -- [10.4171/022-3/65](https://doi.org/10.4171/022-3/65)
- [Desai, S. A., Mattheakis, M., Sondak, D., Protopapas, P. & Roberts, S. J. Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Physical Review E vol. 104 (2021)](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/PhysRevE.104.034312](https://doi.org/10.1103/PhysRevE.104.034312)
- Ortega, R., Spong, M. W., Gomez-Estern, F. & Blankenstein, G. Stabilization of a class of underactuated mechanical systems via interconnection and damping assignment. IEEE Transactions on Automatic Control vol. 47 1218–1233 (2002) -- [10.1109/TAC.2002.800770](https://doi.org/10.1109/TAC.2002.800770)
- Wei Zhong & Rock, H. Energy and passivity based control of the double inverted pendulum on a cart. Proceedings of the 2001 IEEE International Conference on Control Applications (CCA’01) (Cat. No.01CH37204) 896–901 doi:10.1109/cca.2001.973983 -- [10.1109/CCA.2001.973983](https://doi.org/10.1109/CCA.2001.973983)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Lutter, M., Listmann, K. & Peters, J. Deep Lagrangian Networks for end-to-end learning of energy-based control for under-actuated systems. 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 7718–7725 (2019) doi:10.1109/iros40897.2019.8968268 -- [10.1109/IROS40897.2019.8968268](https://doi.org/10.1109/IROS40897.2019.8968268)
- Pattern Recognition and Machine Learning. (Springer US, 1971). doi:10.1007/978-1-4615-7566-5 -- [10.1007/978-1-4615-7566-5](https://doi.org/10.1007/978-1-4615-7566-5)
- Bao, Y., Mohammadpour Velni, J. & Shahbakhti, M. An Online Transfer Learning Approach for Identification and Predictive Control Design With Application to RCCI Engines. Volume 1: Adaptive/Intelligent Sys. Control; Driver Assistance/Autonomous Tech.; Control Design Methods; Nonlinear Control; Robotics; Assistive/Rehabilitation Devices; Biomedical/Neural Systems; Building Energy Systems; Connected Vehicle Systems; Control/Estimation of Energy Systems; Control Apps.; Smart Buildings/Microgrids; Education; Human-Robot Systems; Soft Mechatronics/Robotic Components/Systems; Energy/Power Systems; Energy Storage; Estimation/Identification; Vehicle Efficiency/Emissions (2020) doi:10.1115/dscc2020-3210 -- [10.1115/DSCC2020-3210](https://doi.org/10.1115/DSCC2020-3210)
- Biegler, L. T. Nonlinear Programming. (2010) doi:10.1137/1.9780898719383 -- [10.1137/1.9780898719383](https://doi.org/10.1137/1.9780898719383)
- Lucia, S., Tătulea-Codrean, A., Schoppmeyer, C. & Engell, S. Rapid development of modular and sustainable nonlinear model predictive control solutions. Control Engineering Practice vol. 60 51–62 (2017) -- [10.1016/j.conengprac.2016.12.009](https://doi.org/10.1016/j.conengprac.2016.12.009)

