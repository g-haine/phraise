---
title: "Reinforcement Learning for Port-Hamiltonian Systems"
date: 2014-08-26 00:00:00 +0100
permalink: reinforcement-learning-for-port-hamiltonian-systems
year: 2015
authors: Olivier Sprangers, Robert Babuska, Subramanya P. Nageshrao, Gabriel A. D. Lopes
category: articles
---
 
## Authors
[Olivier Sprangers](authors/olivier-sprangers), [Robert Babuska](authors/robert-babuska), [Subramanya P. Nageshrao](authors/subramanya-p-nageshrao), [Gabriel A. D. Lopes](authors/gabriel-a-d-lopes)
 
## Abstract
Passivity-based control (PBC) for port-Hamiltonian systems provides an intuitive way of achieving stabilization by rendering a system passive with respect to a desired storage function. However, in most instances the control law is obtained without any performance considerations and it has to be calculated by solving a complex partial differential equation (PDE). In order to address these issues we introduce a reinforcement learning (RL) approach into the energy-balancing passivity-based control (EB-PBC) method, which is a form of PBC in which the closed-loop energy is equal to the difference between the stored and supplied energies. We propose a technique to parameterize EB-PBC that preserves the systems's PDE matching conditions, does not require the specification of a global desired Hamiltonian, includes performance criteria, and is robust. The parameters of the control law are found by using actor-critic (AC) RL, enabling the search for near-optimal control policies satisfying a desired closed-loop energy landscape. The advantage is that the solutions learned can be interpreted in terms of energy shaping and damping injection, which makes it possible to numerically assess stability using passivity theory. From the RL perspective, our proposal allows for the class of port-Hamiltonian systems to be incorporated in the AC framework, speeding up the learning thanks to the resulting parameterization of the policy. The method has been successfully applied to the pendulum swing-up problem in simulations and real-life experiments.
 
## Citation
- **Journal:** IEEE Transactions on Cybernetics
- **Year:** 2015
- **Volume:** 45
- **Issue:** 5
- **Pages:** 1017--1027
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tcyb.2014.2343194](https://doi.org/10.1109/tcyb.2014.2343194)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Sprangers_2015,
  title={{Reinforcement Learning for Port-Hamiltonian Systems}},
  volume={45},
  ISSN={2168-2275},
  DOI={10.1109/tcyb.2014.2343194},
  number={5},
  journal={IEEE Transactions on Cybernetics},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Sprangers, Olivier and Babuska, Robert and Nageshrao, Subramanya P. and Lopes, Gabriel A. D.},
  year={2015},
  pages={1017--1027}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/reinforcement-learning-for-port-hamiltonian-systems.bib)
 
## References
- [Wei, A. & Wang, Y. Stabilization and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si2.gif" display="inline" overflow="scroll"><mml:msub><mml:mrow><mml:mi>H</mml:mi></mml:mrow><mml:mrow><mml:mi>∞</mml:mi></mml:mrow></mml:msub></mml:math> control of nonlinear port-controlled Hamiltonian systems subject to actuator saturation. Automatica vol. 46 2008–2013 (2010)](stabilization-and-h-control-of-nonlinear-port-controlled-hamiltonian-systems-subject-to-actuator-saturation) -- [10.1016/j.automatica.2010.08.001](https://doi.org/10.1016/j.automatica.2010.08.001)
- A˚ström, K. J., Aracil, J. & Gordillo, F. A family of smooth controllers for swinging up a pendulum. Automatica vol. 44 1841–1848 (2008) -- [10.1016/j.automatica.2007.10.040](https://doi.org/10.1016/j.automatica.2007.10.040)
- Escobar, G., Ortega, R. & Sira-Ramirez, H. Output-feedback global stabilization of a nonlinear benchmark system using a saturated passivity-based controller. IEEE Transactions on Control Systems Technology vol. 7 289–293 (1999) -- [10.1109/87.748155](https://doi.org/10.1109/87.748155)
- Fujimoto, K. & Sugie, T. Iterative learning control of hamiltonian systems: I/O based optimal control approach. IEEE Transactions on Automatic Control vol. 48 1756–1761 (2003) -- [10.1109/tac.2003.817908](https://doi.org/10.1109/tac.2003.817908)
- macchelli, Port Hamiltonian systems: A unified approach for modeling and control finite and infinite dimensional physical systems. (2002)
- macchelli, A variable structure approach to energy shaping. Proc Eur Control Conf (2003)
- [Sun, W., Lin, Z. & Wang, Y. Global asymptotic and finite-gain L&lt;inf&gt;2&lt;/inf&gt; stabilization of port-controlled Hamiltonian systems subject to actuator saturation. 2009 American Control Conference 1894–1898 (2009) doi:10.1109/acc.2009.5160232](global-asymptotic-and-finite-gain-l-lt-inf-gt-2-lt-inf-gt-stabilization-of-port-controlled-hamiltonian-systems-subject-to-actuator-saturation) -- [10.1109/acc.2009.5160232](https://doi.org/10.1109/acc.2009.5160232)
- Hjalmarsson, H. Iterative feedback tuning—an overview. International Journal of Adaptive Control and Signal Processing vol. 16 373–395 (2002) -- [10.1002/acs.714](https://doi.org/10.1002/acs.714)
- fujimoto, Iterative feedback tuning for Hamiltonian systems. Proc 17th World Congr Int Fed Autom Control (2008)
- Yin, S., Luo, H. & Ding, S. X. Real-Time Implementation of Fault-Tolerant Control Systems With Performance Optimization. IEEE Transactions on Industrial Electronics vol. 61 2402–2411 (2014) -- [10.1109/tie.2013.2273477](https://doi.org/10.1109/tie.2013.2273477)
- konidaris, Value function approximation in reinforcement learning using the Fourier basis. (2008)
- Putting energy back in control. IEEE Control Systems vol. 21 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Koopman, J. & Jeltsema, D. Casimir-Based Control Beyond the Dissipation Obstacle. IFAC Proceedings Volumes vol. 45 173–177 (2012)](casimir-based-control-beyond-the-dissipation-obstacle) -- [10.3182/20120829-3-it-4022.00046](https://doi.org/10.3182/20120829-3-it-4022.00046)
- van der Schaft, A. L2 - Gain and Passivity Techniques in Nonlinear Control. Communications and Control Engineering (Springer London, 2000). doi:10.1007/978-1-4471-0507-7 -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- secchi, Control of Interactive Robotic Interfaces A Port-Hamiltonian Approach (2007)
- duindam, Port-based modeling and control for efficient bipedal walking robots (2009)
- Konda, V. R. & Tsitsiklis, J. N. OnActor-Critic Algorithms. SIAM Journal on Control and Optimization vol. 42 1143–1166 (2003) -- [10.1137/s0363012901385691](https://doi.org/10.1137/s0363012901385691)
- sutton, Reinforcement Learning An Introduction (1998)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Transactions on Automatic Control vol. 53 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- Grondman, I., Vaandrager, M., Busoniu, L., Babuska, R. & Schuitema, E. Efficient Model Learning Methods for Actor–Critic Control. IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics) vol. 42 591–602 (2012) -- [10.1109/tsmcb.2011.2170565](https://doi.org/10.1109/tsmcb.2011.2170565)
- Ortega, R. & Spong, M. W. Adaptive motion control of rigid robots: A tutorial. Automatica vol. 25 877–888 (1989) -- [10.1016/0005-1098(89)90054-x](https://doi.org/10.1016/0005-1098(89)90054-x)
- maschke, Port-controlled Hamiltonian systems: Modelling origins and system theoretic properties. Proc 3rd Conf Nonlin Control Syst (NOLCOS) (1992)
- Grondman, I., Busoniu, L. & Babuska, R. Model learning actor-critic algorithms: Performance evaluation in a motion control task. 2012 IEEE 51st IEEE Conference on Decision and Control (CDC) 5272–5277 (2012) doi:10.1109/cdc.2012.6426427 -- [10.1109/cdc.2012.6426427](https://doi.org/10.1109/cdc.2012.6426427)
- Van Der Schaft, A. J. & Maschke, B. M. On the Hamiltonian formulation of nonholonomic mechanical systems. Reports on Mathematical Physics vol. 34 225–233 (1994) -- [10.1016/0034-4877(94)90038-8](https://doi.org/10.1016/0034-4877(94)90038-8)
- Grondman, I., Busoniu, L., Lopes, G. A. D. & Babuska, R. A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) vol. 42 1291–1307 (2012) -- [10.1109/tsmcc.2012.2218595](https://doi.org/10.1109/tsmcc.2012.2218595)
- Barto, A. G., Sutton, R. S. & Anderson, C. W. Neuronlike adaptive elements that can solve difficult learning control problems. IEEE Transactions on Systems, Man, and Cybernetics vol. SMC-13 834–846 (1983) -- [10.1109/tsmc.1983.6313077](https://doi.org/10.1109/tsmc.1983.6313077)
- asmuth, A Bayesian sampling approach to exploration in reinforcement learning. Proc 25th Conf Uncertainty Artif Intell (2009)
- sutton, Policy gradient methods for reinforcement learning with function approximation. Advances in neural information processing systems (2000)

