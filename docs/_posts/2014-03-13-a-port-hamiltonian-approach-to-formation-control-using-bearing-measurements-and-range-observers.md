---
layout: post
title: "A port-Hamiltonian approach to formation control using bearing measurements and range observers"
date: 2014-03-13 00:00:00 +0100
permalink: a-port-hamiltonian-approach-to-formation-control-using-bearing-measurements-and-range-observers
year: 2013
authors: Geoff Stacey, Robert Mahony
category: proceedings
---
 
## Authors
[Geoff Stacey](authors/geoff-stacey), [Robert Mahony](authors/robert-mahony)
 
## Abstract
In this paper we consider the problem of formation control using measurements of the bearings between vehicles. We design our system using port-Hamiltonian theory and the bondgraph modelling technique. Our approach builds upon the architecture presented in [22], which relied on partial measurements of relative position rather than position measurements with respect to an inertial frame. The previous work used a generalised form of the image Jacobians employed in image-based visual servo (IBVS) control literature to compute the desired control forces. However, the implementation of these measurement Jacobians requires unknown information about the relative positions of the vehicles. A key contribution of this paper is that we show how a depth observer can be integrated into the design to overcome this problem for the case where bearing measurements are available. Assuming that a single distance measurement is also available, we can specify a rigid goal formation in terms of the available measurements of relative positions. For this system, we prove local convergence to the desired configuration. We then provide a discussion regarding the implementation, and suggest that in practice, the distance measurement may be unnecessary. This discussion is supported by simulation results.
 
## Citation
- **Journal:** 52nd IEEE Conference on Decision and Control
- **Year:** 2013
- **Volume:** 
- **Issue:** 
- **Pages:** 7641--7646
- **Publisher:** IEEE
- **DOI:** [10.1109/cdc.2013.6761102](https://doi.org/10.1109/cdc.2013.6761102)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Stacey_2013,
  title={{A port-Hamiltonian approach to formation control using bearing measurements and range observers}},
  DOI={10.1109/cdc.2013.6761102},
  booktitle={{52nd IEEE Conference on Decision and Control}},
  publisher={IEEE},
  author={Stacey, Geoff and Mahony, Robert},
  year={2013},
  pages={7641--7646}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-port-hamiltonian-approach-to-formation-control-using-bearing-measurements-and-range-observers.bib)
 
## References
- [Mahony, R. & Stramigioli, S. A port-Hamiltonian approach to image-based visual servo control for dynamic systems. The International Journal of Robotics Research 31, 1303–1319 (2012)](a-port-hamiltonian-approach-to-image-based-visual-servo-control-for-dynamic-systems) -- [10.1177/0278364912455074](https://doi.org/10.1177/0278364912455074)
- khalil, Nonlinear Systems (2002)
- Leonard, N. E. & Fiorelli, E. Virtual leaders, artificial potentials and coordinated control of groups. Proceedings of the 40th IEEE Conference on Decision and Control (Cat. No.01CH37228) vol. 3 2968–2973 -- [10.1109/cdc.2001.980728](https://doi.org/10.1109/cdc.2001.980728)
- Ibuki, T., Hatanaka, T., Fujita, M. & Spong, M. W. Visual feedback pose synchronization with a generalized camera model. IEEE Conference on Decision and Control and European Control Conference 4999–5004 (2011) doi:10.1109/cdc.2011.6160748 -- [10.1109/cdc.2011.6160748](https://doi.org/10.1109/cdc.2011.6160748)
- Johnson, E. N., Calise, A. J., Sattigeri, R., Watanabe, Y. & Madyastha, V. Approaches to vision-based formation control. 2004 43rd IEEE Conference on Decision and Control (CDC) (IEEE Cat. No.04CH37601) 1643-1648 Vol.2 (2004) doi:10.1109/cdc.2004.1430280 -- [10.1109/cdc.2004.1430280](https://doi.org/10.1109/cdc.2004.1430280)
- Fujita, M., Kawai, H. & Spong, M. W. Passivity-Based Dynamic Visual Feedback Control for Three-Dimensional Target Tracking: Stability and $L_{2}$-Gain Performance Analysis. IEEE Trans. Contr. Syst. Technol. 15, 40–52 (2007) -- [10.1109/tcst.2006.883236](https://doi.org/10.1109/tcst.2006.883236)
- Hatanaka, T., Igarashi, Y., Fujita, M. & Spong, M. W. Passivity-Based Pose Synchronization in Three Dimensions. IEEE Trans. Automat. Contr. 57, 360–375 (2012) -- [10.1109/tac.2011.2166668](https://doi.org/10.1109/tac.2011.2166668)
- Franchi, A. et al. Modeling and Control of UAV Bearing Formations with Bilateral High-level Steering. The International Journal of Robotics Research 31, 1504–1525 (2012) -- [10.1177/0278364912462493](https://doi.org/10.1177/0278364912462493)
- Franchi, A., Secchi, C., Hyoung Il Son, Bulthoff, H. H. & Giordano, P. R. Bilateral Teleoperation of Groups of Mobile Robots With Time-Varying Topology. IEEE Trans. Robot. 28, 1019–1033 (2012) -- [10.1109/tro.2012.2196304](https://doi.org/10.1109/tro.2012.2196304)
- Secchi, C., Franchi, A., Bulthoff, H. H. & Giordano, P. R. Bilateral teleoperation of a group of UAVs with communication delays and switching topology. 2012 IEEE International Conference on Robotics and Automation 4307–4314 (2012) doi:10.1109/icra.2012.6225304 -- [10.1109/icra.2012.6225304](https://doi.org/10.1109/icra.2012.6225304)
- Ren, W. & Beard, R. W. Decentralized Scheme for Spacecraft Formation Flying via the Virtual Structure Approach. Journal of Guidance, Control, and Dynamics 27, 73–82 (2004) -- [10.2514/1.9287](https://doi.org/10.2514/1.9287)
- stacey, A bondgraph approach to formation control using relative state measurements. European Control Conference (2013)
- Tanner, H. G., Jadbabaie, A. & Pappas, G. J. Flocking in Fixed and Switching Networks. IEEE Trans. Automat. Contr. 52, 863–868 (2007) -- [10.1109/tac.2007.895948](https://doi.org/10.1109/tac.2007.895948)
- Turpin, M., Michael, N. & Kumar, V. Decentralized formation control with variable shapes for aerial robots. 2012 IEEE International Conference on Robotics and Automation 23–30 (2012) doi:10.1109/icra.2012.6225196 -- [10.1109/icra.2012.6225196](https://doi.org/10.1109/icra.2012.6225196)
- [van der Schaft, A. J. & Maschke, B. M. Port-Hamiltonian Systems on Graphs. SIAM J. Control Optim. 51, 906–937 (2013)](port-hamiltonian-systems-on-graphs) -- [10.1137/110840091](https://doi.org/10.1137/110840091)
- zelazo, Rigidity maintenance control for multi-robot systems. Robotics Science and Systems (2012)
- Borutzky, W. Bond Graph Modelling And Simulation Of Mechatronic Systems An Introduction Into The Methodology. ECMS 2006 Proceedings edited by: W. Borutzky, A. Orsoni, R. Zobel 17–28 (2006) doi:10.7148/2006-0017 -- [10.7148/2006-0017](https://doi.org/10.7148/2006-0017)
- Beard, R. W., Lawton, J. & Hadaegh, F. Y. A coordination architecture for spacecraft formation control. IEEE Trans. Contr. Syst. Technol. 9, 777–790 (2001) -- [10.1109/87.960341](https://doi.org/10.1109/87.960341)
- Franchi, A. & Giordano, P. R. Decentralized control of parallel rigid formations with direction constraints and bearing measurements. 2012 IEEE 51st IEEE Conference on Decision and Control (CDC) 5310–5317 (2012) doi:10.1109/cdc.2012.6426034 -- [10.1109/cdc.2012.6426034](https://doi.org/10.1109/cdc.2012.6426034)
- Balch, T. & Arkin, R. C. Behavior-based formation control for multirobot teams. IEEE Trans. Robot. Automat. 14, 926–939 (1998) -- [10.1109/70.736776](https://doi.org/10.1109/70.736776)
- Corke, P. I. & Hutchinson, S. A. A new partitioned approach to image-based visual servo control. IEEE Trans. Robot. Automat. 17, 507–515 (2001) -- [10.1109/70.954764](https://doi.org/10.1109/70.954764)
- Chaumette, F. & Hutchinson, S. Visual servo control. II. Advanced approaches [Tutorial]. IEEE Robot. Automat. Mag. 14, 109–118 (2007) -- [10.1109/mra.2007.339609](https://doi.org/10.1109/mra.2007.339609)
- Chaumette, F. & Hutchinson, S. Visual servo control. I. Basic approaches. IEEE Robot. Automat. Mag. 13, 82–90 (2006) -- [10.1109/mra.2006.250573](https://doi.org/10.1109/mra.2006.250573)
- Cao, M., Yu, C. & Anderson, B. D. O. Formation control using range-only measurements. Automatica 47, 776–781 (2011) -- [10.1016/j.automatica.2011.01.067](https://doi.org/10.1016/j.automatica.2011.01.067)
- Fink, J., Michael, N., Kim, S. & Kumar, V. Planning and control for cooperative manipulation and transportation with aerial robots. The International Journal of Robotics Research 30, 324–334 (2010) -- [10.1177/0278364910382803](https://doi.org/10.1177/0278364910382803)
- Das, A. K. et al. A vision-based formation control framework. IEEE Trans. Robot. Automat. 18, 813–825 (2002) -- [10.1109/tra.2002.803463](https://doi.org/10.1109/tra.2002.803463)

