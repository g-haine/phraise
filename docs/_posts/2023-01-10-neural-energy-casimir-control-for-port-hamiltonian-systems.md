---
layout: post
title: "Neural Energy Casimir Control for Port-Hamiltonian Systems"
date: 2023-01-10 00:00:00 +0100
permalink: neural-energy-casimir-control-for-port-hamiltonian-systems
year: 2022
authors: Liang Xu, Muhammad Zakwan, Giancarlo Ferrari-Trecate
category: proceedings
---
 
## Authors
[Liang Xu](authors/liang-xu), [Muhammad Zakwan](authors/muhammad-zakwan), [Giancarlo Ferrari-Trecate](authors/giancarlo-ferrari-trecate)
 
## Abstract
The energy Casimir method is an effective controller design approach to stabilize port-Hamiltonian systems at a desired equilibrium. However, its application relies on the availability of suitable Casimir and Lyapunov functions, whose computation are generally intractable. In this paper, we propose a neural network-based framework to learn these functions. We show how to achieve equilibrium assignment by adding suitable regularization terms in the training cost. We also propose a parameterization of Casimir functions for reducing the training complexity. Moreover, the distance between the equilibrium of the learned Lyapunov function and the desired equilibrium is analyzed, which indicates that for small suboptimality gaps, the distance decreases linearly with respect to the training loss. Our methods are backed up by simulations on a pendulum system.
 
## Citation
- **Journal:** 2022 IEEE 61st Conference on Decision and Control (CDC)
- **Year:** 2022
- **Volume:** 
- **Issue:** 
- **Pages:** 4053--4058
- **Publisher:** IEEE
- **DOI:** [10.1109/cdc51059.2022.9992784](https://doi.org/10.1109/cdc51059.2022.9992784)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Xu_2022,
  title={{Neural Energy Casimir Control for Port-Hamiltonian Systems}},
  DOI={10.1109/cdc51059.2022.9992784},
  booktitle={{2022 IEEE 61st Conference on Decision and Control (CDC)}},
  publisher={IEEE},
  author={Xu, Liang and Zakwan, Muhammad and Ferrari-Trecate, Giancarlo},
  year={2022},
  pages={4053--4058}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/neural-energy-casimir-control-for-port-hamiltonian-systems.bib)
 
## References
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- [Schaller, M., Philipp, F., Faulwasser, T., Worthmann, K. & Maschke, B. Control of port-Hamiltonian systems with minimal energy supply. European Journal of Control vol. 62 33–40 (2021)](control-of-port-hamiltonian-systems-with-minimal-energy-supply) -- [10.1016/j.ejcon.2021.06.017](https://doi.org/10.1016/j.ejcon.2021.06.017)
- [Tsolakis, A. & Keviczky, T. Distributed IDA-PBC for a Class of Nonholonomic Mechanical Systems. IFAC-PapersOnLine vol. 54 275–280 (2021)](distributed-ida-pbc-for-a-class-of-nonholonomic-mechanical-systems) -- [10.1016/j.ifacol.2021.10.365](https://doi.org/10.1016/j.ifacol.2021.10.365)
- [Strehle, F., Pfeifer, M., Malan, A. J., Krebs, S. & Hohmann, S. A Scalable Port-Hamiltonian Approach to Plug-and-Play Voltage Stabilization in DC Microgrids. 2020 IEEE Conference on Control Technology and Applications (CCTA) 787–794 (2020) doi:10.1109/ccta41146.2020.9206323](a-scalable-port-hamiltonian-approach-to-plug-and-play-voltage-stabilization-in-dc-microgrids) -- [10.1109/ccta41146.2020.9206323](https://doi.org/10.1109/ccta41146.2020.9206323)
- [Padilla, G. P., Flores Paredes, J. C. & Donkers, M. C. F. A Port-Hamiltonian Approach to Complete Vehicle Energy Management: A Battery Electric Vehicle Case Study. 2020 American Control Conference (ACC) 288–294 (2020) doi:10.23919/acc45564.2020.9147748](a-port-hamiltonian-approach-to-complete-vehicle-energy-management-a-battery-electric-vehicle-case-study) -- [10.23919/acc45564.2020.9147748](https://doi.org/10.23919/acc45564.2020.9147748)
- Brogliato, B., Lozano, R., Maschke, B. & Egeland, O. Correction to: Dissipative Systems Analysis and Control. Communications and Control Engineering C1–C1 (2022) doi:10.1007/978-3-030-19420-8_10 -- [10.1007/978-3-030-19420-8_10](https://doi.org/10.1007/978-3-030-19420-8_10)
- van der Schaft, A. L2-Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer International Publishing, 2017). doi:10.1007/978-3-319-49992-5 -- [10.1007/978-3-319-49992-5](https://doi.org/10.1007/978-3-319-49992-5)
- Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Energy-shaping of port-controlled Hamiltonian systems by interconnection. Proceedings of the 38th IEEE Conference on Decision and Control (Cat. No.99CH36304) vol. 2 1646–1651 -- [10.1109/cdc.1999.830260](https://doi.org/10.1109/cdc.1999.830260)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 53 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- [Wu, C., van der Schaft, A. & Chen, J. Stabilization of Port-Hamiltonian Systems Based on Shifted Passivity via Feedback. IEEE Transactions on Automatic Control vol. 66 2219–2226 (2021)](stabilization-of-port-hamiltonian-systems-based-on-shifted-passivity-via-feedback) -- [10.1109/tac.2020.3005156](https://doi.org/10.1109/tac.2020.3005156)
- Chang, Neural Lyapunov control. Proceedings of the 33rd International Conference on Neural Information Processing Systems
- Dai, H., Landry, B., Yang, L., Pavone, M. & Tedrake, R. Lyapunov-stable neural-network control. Robotics: Science and Systems XVII (2021) doi:10.15607/rss.2021.xvii.063 -- [10.15607/rss.2021.xvii.063](https://doi.org/10.15607/rss.2021.xvii.063)
- Yin, H., Seiler, P. & Arcak, M. Stability Analysis Using Quadratic Constraints for Systems With Neural Network Controllers. IEEE Transactions on Automatic Control vol. 67 1980–1987 (2022) -- [10.1109/tac.2021.3069388](https://doi.org/10.1109/tac.2021.3069388)
- Pauli, P., Gramlich, D., Berberich, J. & Allgower, F. Linear systems with neural network nonlinearities: Improved stability analysis via acausal Zames-Falb multipliers. 2021 60th IEEE Conference on Decision and Control (CDC) 3611–3618 (2021) doi:10.1109/cdc45484.2021.9683341 -- [10.1109/cdc45484.2021.9683341](https://doi.org/10.1109/cdc45484.2021.9683341)
- Yang, F. & Matni, N. Communication Topology Co-Design in Graph Recurrent Neural Network based Distributed Control. 2021 60th IEEE Conference on Decision and Control (CDC) 3619–3626 (2021) doi:10.1109/cdc45484.2021.9683779 -- [10.1109/cdc45484.2021.9683779](https://doi.org/10.1109/cdc45484.2021.9683779)
- Gama, Graph neural networks for distributed linear-quadratic control. Learning for Dynamics and Control (2021)
- Richards, The Lyapunov neural network: Adaptive stability certification for safe learning of dynamical systems. Conference on Robot Learning
- Chen, S., Fazlyab, M., Morari, M., Pappas, G. J. & Preciado, V. M. Learning Region of Attraction for Nonlinear Systems. 2021 60th IEEE Conference on Decision and Control (CDC) 6477–6484 (2021) doi:10.1109/cdc45484.2021.9682880 -- [10.1109/cdc45484.2021.9682880](https://doi.org/10.1109/cdc45484.2021.9682880)
- Khader, S. A., Yin, H., Falco, P. & Kragic, D. Learning Deep Energy Shaping Policies for Stability-Guaranteed Manipulation. IEEE Robotics and Automation Letters vol. 6 8583–8590 (2021) -- [10.1109/lra.2021.3111962](https://doi.org/10.1109/lra.2021.3111962)
- Lee, J. M. Introduction to Smooth Manifolds. Graduate Texts in Mathematics (Springer New York, 2012). doi:10.1007/978-1-4419-9982-5 -- [10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5)
- Kingma, Adam: A method for stochastic optimization. (2014)
- Galimberti, C. L., Furieri, L., Xu, L. & Ferrari-Trecate, G. Hamiltonian Deep Neural Networks Guaranteeing Nonvanishing Gradients by Design. IEEE Transactions on Automatic Control vol. 68 3155–3162 (2023) -- [10.1109/tac.2023.3239430](https://doi.org/10.1109/tac.2023.3239430)

