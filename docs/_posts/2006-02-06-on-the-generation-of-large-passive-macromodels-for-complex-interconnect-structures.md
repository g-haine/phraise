---
layout: post
title: "On the Generation of Large Passive Macromodels for Complex Interconnect Structures"
date: 2006-02-06 00:00:00 +0100
permalink: on-the-generation-of-large-passive-macromodels-for-complex-interconnect-structures
year: 2006
authors: S. Grivet-Talocia, A. Ubolli
category: articles
---
 
## Authors
[S. Grivet-Talocia](authors/stefano-grivet-talocia), [A. Ubolli](authors/a-ubolli)
 
## Abstract
This paper addresses some issues related to the passivity of interconnect macromodels computed from measured or simulated port responses. The generation of such macromodels is usually performed via suitable least squares fitting algorithms. When the number of ports and the dynamic order of the macromodel is large, the inclusion of passivity constraints in the fitting process is cumbersome and results in excessive computational and storage requirements. Therefore, we consider in this work a post-processing approach for passivity enforcement, aimed at the detection and compensation of passivity violations without compromising the model accuracy. Two complementary issues are addressed. First, we consider the enforcement of asymptotic passivity at high frequencies based on the perturbation of the direct coupling term in the transfer matrix. We show how potential problems may arise when off-band poles are present in the model. Second, the enforcement of uniform passivity throughout the entire frequency axis is performed via an iterative perturbation scheme on the purely imaginary eigenvalues of associated Hamiltonian matrices. A special formulation of this spectral perturbation using possibly large but sparse matrices allows the passivity compensation to be performed at a cost which scales only linearly with the order of the system. This formulation involves a restarted Arnoldi iteration combined with a complex frequency hopping algorithm for the selective computation of the imaginary eigenvalues to be perturbed. Some examples of interconnect models are used to illustrate the performance of the proposed techniques.
 
## Citation
- **Journal:** IEEE Transactions on Advanced Packaging
- **Year:** 2006
- **Volume:** 29
- **Issue:** 1
- **Pages:** 39--54
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tadvp.2005.862659](https://doi.org/10.1109/tadvp.2005.862659)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Grivet_Talocia_2006,
  title={{On the Generation of Large Passive Macromodels for Complex Interconnect Structures}},
  volume={29},
  ISSN={1521-3323},
  DOI={10.1109/tadvp.2005.862659},
  number={1},
  journal={IEEE Transactions on Advanced Packaging},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Grivet-Talocia, S. and Ubolli, A.},
  year={2006},
  pages={39--54}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/on-the-generation-of-large-passive-macromodels-for-complex-interconnect-structures.bib)
 
## References
- Matlab Release 14 User s Guide (0)
- Achar, R., Gunupudi, P. K., Nakhla, M. & Chiprout, E. Passive interconnect reduction algorithm for distributed/measured networks. IEEE Trans. Circuits Syst. II 47, 287–301 (2000) -- [10.1109/82.839664](https://doi.org/10.1109/82.839664)
- grivet-talocia, fast passivity enforcement for large and sparse macromodels. Proc 13th IEEE Topical Meeting on Electrical Performance of Electronic Packaging (2004)
- brockett, Finite Dimensional Linear Systems (1970)
- wilkinson, The Algebraic Eigenvalue Problem (1965)
- Saad, Y. Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. Linear Algebra and its Applications 34, 269–295 (1980) -- [10.1016/0024-3795(80)90169-x](https://doi.org/10.1016/0024-3795(80)90169-x)
- saad, Numerical Methods for Large Eigenvalue Problems (1992)
- golub, Matrix Computations (1996)
- Mehrmann, V. & Watkins, D. Structure-Preserving Methods for Computing Eigenpairs of Large Sparse Skew-Hamiltonian/Hamiltonian Pencils. SIAM J. Sci. Comput. 22, 1905–1925 (2001) -- [10.1137/s1064827500366434](https://doi.org/10.1137/s1064827500366434)
- [Grivet-Talocia, S., Canavero, F. G., Stievano, I. S. & Maio, I. A. Circuit extraction via time-domain vector fitting. 2004 International Symposium on Electromagnetic Compatibility (IEEE Cat. No.04CH37559) 1005–1010 doi:10.1109/isemc.2004.1349964](circuit-extraction-via-time-domain-vector-fitting) -- [10.1109/isemc.2004.1349964](https://doi.org/10.1109/isemc.2004.1349964)
- celik, IC Interconnect Analysis (2002)
- Achar, R. & Nakhla, M. S. Simulation of high-speed interconnects. Proc. IEEE 89, 693–728 (2001) -- [10.1109/5.929650](https://doi.org/10.1109/5.929650)
- belevitch, Classical Network Theory (1968)
- zhou, Robust and Optimal Control (1996)
- Morsey, J. & Cangellaris, A. C. PRIME: passive realization of interconnect models from measured data. IEEE 10th Topical Meeting on Electrical Performance of Electronic Packaging (Cat. No. 01TH8565) 47–50 doi:10.1109/epep.2001.967608 -- [10.1109/epep.2001.967608](https://doi.org/10.1109/epep.2001.967608)
- Gustavsen, B. & Semlyen, A. Enforcing passivity for admittance matrices approximated by rational functions. IEEE Trans. Power Syst. 16, 97–104 (2001) -- [10.1109/59.910786](https://doi.org/10.1109/59.910786)
- Coelho, C. P., Phillips, J. & Silveira, L. M. A Convex Programming Approach for Generating Guaranteed Passive Approximations to Tabulated Frequency-Data. IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst. 23, 293–301 (2004) -- [10.1109/tcad.2003.822107](https://doi.org/10.1109/tcad.2003.822107)
- Boyd, S., El Ghaoui, L., Feron, E. & Balakrishnan, V. Linear Matrix Inequalities in System and Control Theory. (1994) doi:10.1137/1.9781611970777 -- [10.1137/1.9781611970777](https://doi.org/10.1137/1.9781611970777)
- chen, enforcing bounded realness of s parameter through trace parameterization. Proc 12th IEEE Topical Meeting on Electrical Performance of Electronic Packaging (2003)
- Gustavsen, B. & Semlyen, A. Application of vector fitting to state equation representation of transformers for simulation of electromagnetic transients. IEEE Trans. Power Delivery 13, 834–842 (1998) -- [10.1109/61.686981](https://doi.org/10.1109/61.686981)
- Elzinga, M., Virga, K. L., Zhao, L. & Prince, J. L. Pole-residue formulation for transient simulation of high-frequency interconnects using householder LS curve-fitting techniques. IEEE Trans. Adv. Packag. 23, 142–147 (2000) -- [10.1109/6040.846624](https://doi.org/10.1109/6040.846624)
- Chiprout, E. & Nakhla, M. S. Analysis of interconnect networks using complex frequency hopping (CFH). IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst. 14, 186–200 (1995) -- [10.1109/43.370425](https://doi.org/10.1109/43.370425)
- do Couto Boaventura, W., Semlyen, A., Reza Iravani, M. & Lopes, A. Sparse network equivalent based on time-domain fitting. IEEE Trans. Power Delivery 17, 182–189 (2002) -- [10.1109/61.974206](https://doi.org/10.1109/61.974206)
- grivet-talocia, reduced-order macromodeling of complex multiport interconnects. URSI General Assembly (2002)
- Li, E.-P., Liu, E.-X., Li, L.-W. & Leong, M.-S. A Coupled Efficient and Systematic Full-Wave Time-Domain Macromodeling and Circuit Simulation Method for Signal Integrity Analysis of High-Speed Interconnects. IEEE Trans. Adv. Packag. 27, 213–223 (2004) -- [10.1109/tadvp.2004.825448](https://doi.org/10.1109/tadvp.2004.825448)
- Elzinga, M., Virga, K. L. & Prince, J. L. Improved global rational approximation macromodeling algorithm for networks characterized by frequency-sampled data. IEEE Trans. Microwave Theory Techn. 48, 1461–1468 (2000) -- [10.1109/22.868995](https://doi.org/10.1109/22.868995)
- Gustavsen, B. & Semlyen, A. Rational approximation of frequency domain responses by vector fitting. IEEE Trans. Power Delivery 14, 1052–1061 (1999) -- [10.1109/61.772353](https://doi.org/10.1109/61.772353)
- Grivet-Talocia, S. Package macromodeling via time-domain vector fitting. IEEE Microw. Wireless Compon. Lett. 13, 472–474 (2003) -- [10.1109/lmwc.2003.819378](https://doi.org/10.1109/lmwc.2003.819378)
- Choi, K. L. & Swaminathan, M. Development of model libraries for embedded passives using network synthesis. IEEE Trans. Circuits Syst. II 47, 249–260 (2000) -- [10.1109/82.839661](https://doi.org/10.1109/82.839661)
- [Grivet-Talocia, S. & Ubolli, A. On the Generation of Large Passive Macromodels for Complex Interconnect Structures. IEEE Trans. Adv. Packag. 29, 39–54 (2006)](on-the-generation-of-large-passive-macromodels-for-complex-interconnect-structures) -- [10.1109/tadvp.2005.862659](https://doi.org/10.1109/tadvp.2005.862659)
- Beyene, W. T. & Schutt-Aine, J. Accurate frequency-domain modeling and efficient circuit simulation of high-speed packaging interconnects. IEEE Trans. Microwave Theory Techn. 45, 1941–1947 (1997) -- [10.1109/22.641798](https://doi.org/10.1109/22.641798)
- Boyd, S., Balakrishnan, V. & Kabamba, P. A bisection method for computing the H∞ norm of a transfer matrix and related problems. Math. Control Signal Systems 2, 207–219 (1989) -- [10.1007/bf02551385](https://doi.org/10.1007/bf02551385)
- Saraswat, D., Achar, R. & Nakhla, M. Enforcing passivity for rational function based macromodels of tabulated data. Electrical Performance of Electrical Packaging (IEEE Cat. No. 03TH8710) (2003) doi:10.1109/epep.2003.1250053 -- [10.1109/epep.2003.1250053](https://doi.org/10.1109/epep.2003.1250053)
- grivet-talocia, enforcing passivity of macromodels via spectral perturbation of hamiltonian matrices. Proc 7th IEEE Workshop on Signal Propagation on Interconnects (2003)
- kailath, Linear Systems (1980)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Trans. Circuits Syst. I 51, 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Templates for the Solution of Algebraic Eigenvalue Problems. (2000) doi:10.1137/1.9780898719581 -- [10.1137/1.9780898719581](https://doi.org/10.1137/1.9780898719581)
- Arnoldi, W. E. The principle of minimized iterations in the solution of the matrix eigenvalue problem. Quart. Appl. Math. 9, 17–29 (1951) -- [10.1090/qam/42792](https://doi.org/10.1090/qam/42792)

