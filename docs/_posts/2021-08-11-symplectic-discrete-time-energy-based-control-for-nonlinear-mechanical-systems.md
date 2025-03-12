---
layout: post
title: "Symplectic discrete-time energy-based control for nonlinear mechanical systems"
date: 2021-08-11 00:00:00 +0100
permalink: symplectic-discrete-time-energy-based-control-for-nonlinear-mechanical-systems
year: 2021
authors: Paul Kotyczka, Tobias Thoma
category: articles
tags:
  - Sampled-data systems
  - Discrete-time control
  - Structure-preserving methods
  - Symplectic integration
  - Störmer–Verlet
  - Nonlinear mechanical systems
  - Energy shaping
  - Passivity-based control
  - Computed torque
---
 
## Authors
[Paul Kotyczka](authors/paul-kotyczka), [Tobias Thoma](authors/tobias-thoma)
 
## Abstract
We present a novel approach for discrete-time state feedback control implementation which reduces the deteriorating effects of sampling on stability and performance in digitally controlled nonlinear mechanical systems. We translate the argument of energy shaping to discrete time by using the symplectic implicit midpoint rule. The method is motivated by recent results for linear systems, where feedback imposes closed-loop behavior that exactly represents the symplectic discretization of a desired target system. For the nonlinear case, the sampled system and the target dynamics are approximated with second order accuracy using the implicit midpoint rule. The implicit nature of the resulting state feedback requires the numerical solution of an in general nonlinear system of algebraic equations in every sampling interval. For an implementation with pure position feedback, the velocities/momenta have to be approximated in the sampling instants, which gives a clear interpretation of our approach in terms of the Störmer–Verlet integration scheme on a staggered grid. Both the Hamiltonian and the Lagrangian perspective are adopted. We present discrete-time versions of impedance or energy shaping plus damping injection control as well as computed torque tracking control in the simulation examples to illustrate the performance and stability gain compared to the quasi-continuous implementation. We discuss computational aspects and show the structural advantages of the implicit midpoint rule compared to other integration schemes in the appendix.
 
## Keywords
Sampled-data systems; Discrete-time control; Structure-preserving methods; Symplectic integration; Störmer–Verlet; Nonlinear mechanical systems; Energy shaping; Passivity-based control; Computed torque
 
## Citation
- **Journal:** Automatica
- **Year:** 2021
- **Volume:** 133
- **Issue:** 
- **Pages:** 109842
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2021.109842](https://doi.org/10.1016/j.automatica.2021.109842)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Kotyczka_2021,
  title={{Symplectic discrete-time energy-based control for nonlinear mechanical systems}},
  volume={133},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2021.109842},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Kotyczka, Paul and Thoma, Tobias},
  year={2021},
  pages={109842}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/symplectic-discrete-time-energy-based-control-for-nonlinear-mechanical-systems.bib)
 
## References
- Albu-Schäffer, A., Ott, C. & Hirzinger, G. A Unified Passivity-based Control Framework for Position, Torque and                 Impedance Control of Flexible Joint Robots. The International Journal of Robotics Research vol. 26 23–39 (2007) -- [10.1177/0278364907073776](https://doi.org/10.1177/0278364907073776)
- [Aoues, S., Matignon, D. & Alazard, D. Control of a flexible spacecraft using discrete IDA-PBC design. IFAC-PapersOnLine vol. 48 188–193 (2015)](control-of-a-flexible-spacecraft-using-discrete-ida-pbc-design) -- [10.1016/j.ifacol.2015.10.237](https://doi.org/10.1016/j.ifacol.2015.10.237)
- Arnold, (1989)
- Bloch, Controlled Lagrangians and potential shaping for stabilization of discrete mechanical systems. (2006)
- Bona, Friction compensation in robotics: an overview. (2005)
- Canudas de Wit, (1996)
- Chen, Frequency response of discrete-time robot systems – Limitations of PD controllers and improvements by lag-lead compensation. (1987)
- Chyba, M., Hairer, E. & Vilmart, G. The role of symplectic integrators in optimal control. Optimal Control Applications and Methods vol. 30 367–382 (2008) -- [10.1002/oca.855](https://doi.org/10.1002/oca.855)
- De Vogelaere, (1956)
- Englert, T., Völz, A., Mesmer, F., Rhein, S. & Graichen, K. A software framework for embedded nonlinear model predictive control using a gradient-based augmented Lagrangian approach (GRAMPC). Optimization and Engineering vol. 20 769–809 (2019) -- [10.1007/s11081-018-9417-2](https://doi.org/10.1007/s11081-018-9417-2)
- [Gonzalez, O. Time integration and discrete Hamiltonian systems. Journal of Nonlinear Science vol. 6 449–467 (1996)](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/bf02440162](https://doi.org/10.1007/bf02440162)
- [Hairer, E., Lubich, C. & Wanner, G. Geometric numerical integration illustrated by the Störmer–Verlet method. Acta Numerica vol. 12 399–450 (2003)](geometric-numerical-integration-illustrated-by-the-stormer-verlet-method) -- [10.1017/s0962492902000144](https://doi.org/10.1017/s0962492902000144)
- Hairer, (2006)
- Hairer, (1993)
- Hogan, Impedance control: An approach to manipulation. (1984)
- Iserles, (2009)
- [Kotyczka, P. & Lefèvre, L. Discrete-time port-Hamiltonian systems: A definition based on symplectic integration. Systems &amp; Control Letters vol. 133 104530 (2019)](discrete-time-port-hamiltonian-systems-a-definition-based-on-symplectic-integration) -- [10.1016/j.sysconle.2019.104530](https://doi.org/10.1016/j.sysconle.2019.104530)
- Kotyczka, P. & Lefèvre, L. Discrete-Time Control Design Based on Symplectic Integration: Linear Systems. IFAC-PapersOnLine vol. 53 7563–7568 (2020) -- [10.1016/j.ifacol.2020.12.1352](https://doi.org/10.1016/j.ifacol.2020.12.1352)
- Lew, A., Marsden, J. E., Ortiz, M. & West, M. Variational time integrators. International Journal for Numerical Methods in Engineering vol. 60 153–212 (2004) -- [10.1002/nme.958](https://doi.org/10.1002/nme.958)
- Loria, On tracking control of rigid and flexible joints robots. Applied Mathematics and Computer Science (1995)
- Monaco, S. & Normand-Cyrot, D. Advanced Tools for Nonlinear Sampled-Data Systems’ Analysis and Control. European Journal of Control vol. 13 221–241 (2007) -- [10.3166/ejc.13.221-241](https://doi.org/10.3166/ejc.13.221-241)
- Müller, Stability of mechanical systems. (1972)
- Neuman, C. P. & Tourassis, V. D. Discrete dynamic robot models. IEEE Transactions on Systems, Man, and Cybernetics vol. SMC-15 193–204 (1985) -- [10.1109/tsmc.1985.6313349](https://doi.org/10.1109/tsmc.1985.6313349)
- Nicosia, S., Tomei, P. & Tornamb�, A. Discrete-time modeling and control of robotic manipulators. Journal of Intelligent and Robotic Systems vol. 2 (1989) -- [10.1007/bf00247916](https://doi.org/10.1007/bf00247916)
- Ober-Blöbaum, Discrete mechanics and optimal control: An analysis. ESAIM: Control, Optimisation and Calculus of Variations (2010)
- Ortega, (1998)
- Ortega, R., Spong, M. W., Gomez-Estern, F. & Blankenstein, G. Stabilization of a class of underactuated mechanical systems via interconnection and damping assignment. IEEE Transactions on Automatic Control vol. 47 1218–1233 (2002) -- [10.1109/tac.2002.800770](https://doi.org/10.1109/tac.2002.800770)
- Peng, H., Gao, Q., Wu, Z. & Zhong, W. Symplectic Approaches for Solving Two-Point Boundary-Value Problems. Journal of Guidance, Control, and Dynamics vol. 35 653–659 (2012) -- [10.2514/1.55795](https://doi.org/10.2514/1.55795)
- Siciliano, (2016)
- Spong, (2008)
- Störmer, C. Sur les trajectoires des corpuscules électrisés dans l’espace. Applications à l’aurore boréale et aux perturbations magnétiques. Le Radium vol. 4 2–5 (1907) -- [10.1051/radium:01907004010201](https://doi.org/10.1051/radium:01907004010201)
- Takegaki, M. & Arimoto, S. A New Feedback Method for Dynamic Control of Manipulators. Journal of Dynamic Systems, Measurement, and Control vol. 103 119–125 (1981) -- [10.1115/1.3139651](https://doi.org/10.1115/1.3139651)
- Verlet, L. Computer ‘Experiments’ on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules. Physical Review vol. 159 98–103 (1967) -- [10.1103/physrev.159.98](https://doi.org/10.1103/physrev.159.98)
- Viola, G., Ortega, R., Banavar, R., Acosta, J. A. & Astolfi, A. Total Energy Shaping Control of Mechanical Systems: Simplifying the Matching Equations Via Coordinate Changes. IEEE Transactions on Automatic Control vol. 52 1093–1099 (2007) -- [10.1109/tac.2007.899064](https://doi.org/10.1109/tac.2007.899064)
- Woolsey, C. et al. Controlled Lagrangian Systems with Gyroscopic Forcing and Dissipation. European Journal of Control vol. 10 478–496 (2004) -- [10.3166/ejc.10.478-496](https://doi.org/10.3166/ejc.10.478-496)

