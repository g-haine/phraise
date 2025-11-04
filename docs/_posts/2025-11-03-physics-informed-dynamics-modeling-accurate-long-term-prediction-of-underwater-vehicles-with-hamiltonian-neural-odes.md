---
title: "Physics-Informed Dynamics Modeling: Accurate Long-Term Prediction of Underwater Vehicles with Hamiltonian Neural ODEs"
date: 2025-11-03 00:00:00 +0100
permalink: physics-informed-dynamics-modeling-accurate-long-term-prediction-of-underwater-vehicles-with-hamiltonian-neural-odes
year: 2025
authors: Xiang Jin, Zeyu Lyu, Jiayi Liu, Yu Lu
category: articles
---
 
## Authors
[Xiang Jin](authors/xiang-jin), [Zeyu Lyu](authors/zeyu-lyu), [Jiayi Liu](authors/jiayi-liu), [Yu Lu](authors/yu-lu)
 
## Abstract
Accurately predicting the long-term behavior of complex dynamical systems is a central challenge for safety-critical applications like autonomous navigation. Mechanistic models are often brittle, relying on difficult-to-measure parameters, while standard deep learning models are black boxes that fail to generalize, producing physically inconsistent predictions. Here, we introduce a physics-informed framework that learns the continuous-time dynamics of an Autonomous Underwater Vehicle (AUV) by discovering its underlying energy landscape. We embed the structure of Port-Hamiltonian mechanics into a neural ordinary differential equation (NODE) architecture, learning not to imitate trajectories but rather to identify the system’s Hamiltonian and its constituent physical matrices from observational data. Geometric consistency is enforced by representing rotational dynamics on the SE(3) manifold, preventing numerical error accumulation. Experimental validation reveals a stark performance divide. While a state-of-the-art black-box model matches our accuracy in simple, interpolative maneuvers, its predictions fail catastrophically under complex controls. Quantitatively, our physics-informed model maintained a mean 10 s position error of a mere 3.3 cm, whereas the black-box model’s error diverged to 5.4 m—an over 160-fold performance gap. This work establishes that the key to robust, generalizable models lies not in bigger data or deeper networks but in the principled integration of physical laws, providing a clear path to overcoming the brittleness of black-box models in critical engineering simulations.
 
## Citation
- **Journal:** Journal of Marine Science and Engineering
- **Year:** 2025
- **Volume:** 13
- **Issue:** 11
- **Pages:** 2091
- **Publisher:** MDPI AG
- **DOI:** [10.3390/jmse13112091](https://doi.org/10.3390/jmse13112091)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Jin_2025,
  title={{Physics-Informed Dynamics Modeling: Accurate Long-Term Prediction of Underwater Vehicles with Hamiltonian Neural ODEs}},
  volume={13},
  ISSN={2077-1312},
  DOI={10.3390/jmse13112091},
  number={11},
  journal={Journal of Marine Science and Engineering},
  publisher={MDPI AG},
  author={Jin, Xiang and Lyu, Zeyu and Liu, Jiayi and Lu, Yu},
  year={2025},
  pages={2091}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/physics-informed-dynamics-modeling-accurate-long-term-prediction-of-underwater-vehicles-with-hamiltonian-neural-odes.bib)
 
## References
- Lv, Identification method of hydrodynamic coefficients of underwater vehicles based on Kalman filter. J. Wuhan Univ. Technol. Transp. Sci. Eng. (2021)
- Harris, Z. J., Paine, T. M. & Whitcomb, L. L. Preliminary Evaluation of Null-Space Dynamic Process Model Identification with Application to Cooperative Navigation of Underwater Vehicles. 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 3453–3459 (2018) doi:10.1109/iros.2018.8594257 -- [10.1109/iros.2018.8594257](https://doi.org/10.1109/iros.2018.8594257)
- Chu, Parameter identification of unmanned boat maneuvering response model based on UKF. J. Wuhan Univ. Technol. Transp. Sci. Eng. (2019)
- Ramirez, W. A., Kocijan, J., Leong, Z. Q., Nguyen, H. D. & Jayasinghe, S. G. Dynamic System Identification of Underwater Vehicles Using Multi-Output Gaussian Processes. Int. J. Autom. Comput. 18, 681–693 (2021) -- [10.1007/s11633-021-1308-x](https://doi.org/10.1007/s11633-021-1308-x)
- Shafiei, M. H. & Binazadeh, T. Application of neural network and genetic algorithm in identification of a model of a variable mass underwater vehicle. Ocean Engineering 96, 173–180 (2015) -- [10.1016/j.oceaneng.2014.12.021](https://doi.org/10.1016/j.oceaneng.2014.12.021)
- Zhao, A method for identifying hydrodynamic parameters of underwater vehicles based on experimental data. J. Under. Unmanned Syst. (2018)
- Silver, D. et al. Mastering the game of Go without human knowledge. Nature 550, 354–359 (2017) -- [10.1038/nature24270](https://doi.org/10.1038/nature24270)
- Lu, L., Jin, P., Pang, G., Zhang, Z. & Karniadakis, G. E. Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators. Nat Mach Intell 3, 218–229 (2021) -- [10.1038/s42256-021-00302-5](https://doi.org/10.1038/s42256-021-00302-5)
- Bronstein, M. M., Bruna, J., LeCun, Y., Szlam, A. & Vandergheynst, P. Geometric Deep Learning: Going beyond Euclidean data. IEEE Signal Process. Mag. 34, 18–42 (2017) -- [10.1109/msp.2017.2693418](https://doi.org/10.1109/msp.2017.2693418)
- Veeling, B. S., Linmans, J., Winkens, J., Cohen, T. & Welling, M. Rotation Equivariant CNNs for Digital Pathology. Lecture Notes in Computer Science 210–218 (2018) doi:10.1007/978-3-030-00934-2_24 -- [10.1007/978-3-030-00934-2_24](https://doi.org/10.1007/978-3-030-00934-2_24)
- Sirignano, J. & Spiliopoulos, K. DGM: A deep learning algorithm for solving partial differential equations. Journal of Computational Physics 375, 1339–1364 (2018) -- [10.1016/j.jcp.2018.08.029](https://doi.org/10.1016/j.jcp.2018.08.029)
- Raissi, M., Perdikaris, P. & Karniadakis, G. E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378, 686–707 (2019) -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- Geneva, N. & Zabaras, N. Modeling the dynamics of PDE systems with physics-constrained deep auto-regressive networks. Journal of Computational Physics 403, 109056 (2020) -- [10.1016/j.jcp.2019.109056](https://doi.org/10.1016/j.jcp.2019.109056)
- McLain, T. W. & Rock, S. M. Development and Experimental Validation of an Underwater Manipulator Hydrodynamic Model. The International Journal of Robotics Research 17, 748–759 (1998) -- [10.1177/027836499801700705](https://doi.org/10.1177/027836499801700705)
- McLain, T. W., Rock, S. M. & Lee, M. J. Experiments in the coordinated control of an underwater arm/vehicle system. Auton Robot 3, 213–232 (1996) -- [10.1007/bf00141156](https://doi.org/10.1007/bf00141156)
- Fossen, T. I. Handbook of Marine Craft Hydrodynamics and Motion Control. (2011) doi:10.1002/9781119994138 -- [10.1002/9781119994138](https://doi.org/10.1002/9781119994138)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- [Jia, Z., Qiao, L. & Zhang, W. Adaptive tracking control of unmanned underwater vehicles with compensation for external perturbations and uncertainties using Port-Hamiltonian theory. Ocean Engineering 209, 107402 (2020)](adaptive-tracking-control-of-unmanned-underwater-vehicles-with-compensation-for-external-perturbations-and-uncertainties-using-port-hamiltonian-theory) -- [10.1016/j.oceaneng.2020.107402](https://doi.org/10.1016/j.oceaneng.2020.107402)
- Duong, T. & Atanasov, N. Hamiltonian-based Neural ODE Networks on the SE(3) Manifold For Dynamics Learning and Control. Robotics: Science and Systems XVII (2021) doi:10.15607/rss.2021.xvii.086 -- [10.15607/rss.2021.xvii.086](https://doi.org/10.15607/rss.2021.xvii.086)
- Duong, T. & Atanasov, N. Adaptive Control of SE(3) Hamiltonian Dynamics With Learned Disturbance Features. IEEE Control Syst. Lett. 6, 2773–2778 (2022) -- [10.1109/lcsys.2022.3177156](https://doi.org/10.1109/lcsys.2022.3177156)
- Saviolo, A., Li, G. & Loianno, G. Physics-Inspired Temporal Learning of Quadrotor Dynamics for Accurate Model Predictive Trajectory Tracking. IEEE Robot. Autom. Lett. 7, 10256–10263 (2022) -- [10.1109/lra.2022.3192609](https://doi.org/10.1109/lra.2022.3192609)

