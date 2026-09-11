---
title: "Physics-informed thermodynamical Hamiltonian hybrid modeling method for vibration prediction of electric spindles"
date: 2026-09-09 00:00:00 +0100
permalink: physics-informed-thermodynamical-hamiltonian-hybrid-modeling-method-for-vibration-prediction-of-electric-spindles
year: 2026
authors: Xiaojian Liu, Xinyu Lu, Huishu Jia, Wei Zeng, Wentian Li, Yangjian Ji, Guodong Yi, Kang Wang, Lemiao Qiu, Shuyou Zhang
category: articles
tags:
  - dissipative hamiltonian system, electric spindles, hybrid modeling, non-linear dynamics, physics-informed neural network
---
 
## Authors
[Xiaojian Liu](authors/xiaojian-liu), [Xinyu Lu](authors/xinyu-lu), [Huishu Jia](authors/huishu-jia), [Wei Zeng](authors/wei-zeng), [Wentian Li](authors/wentian-li), [Yangjian Ji](authors/yangjian-ji), [Guodong Yi](authors/guodong-yi), [Kang Wang](authors/kang-wang), [Lemiao Qiu](authors/lemiao-qiu), [Shuyou Zhang](authors/shuyou-zhang)
 
## Abstract
Developing high-fidelity digital twin models for electric spindles requires rigorously predicting the coupled thermal-vibration dynamics, where friction-induced heat actively drives parameter drift such as thermal stiffening and viscosity reduction. While structure-preserving frameworks like Port-Hamiltonian Neural Networks and Dissipative Hamiltonian Neural Networks excel in energy-based modeling, they predominantly treat dissipation via resistive ports or energy sinks, implicitly assuming an isothermal environment, failing to capture the reciprocal thermo-mechanical feedback, leading to substantial errors in vibration predictions. To bridge this gap, we propose a Physics-Informed Thermodynamical Hybrid Modeling Method based on the GENERIC formalism and the dissipative Hamiltonian dynamics. A Thermodynamical Hamiltonian Neural Network (THNN) is introduced to identify temperature-dependent constitutive parameters within a thermodynamically consistent physical model, rigorously tracking the conversion of dissipated mechanical work into entropy and temperature evolution and thereby closing the thermo-mechanical loop by design. Through a comprehensive proof-of-concept validated under diverse benchmark scenarios, including noise robustness and parameter sensitivity analyses, we demonstrate that THNN reduces the MAE by 44.1% compared to state-of-the-art baselines while maintaining strict adherence to the First and Second Laws of Thermodynamics. The compact architecture (4.9 K parameters) achieves superior accuracy through physics-informed structural constraints rather than model capacity, establishing a methodological approach for vibration prediction of electric spindles.
 
## Keywords
dissipative hamiltonian system, electric spindles, hybrid modeling, non-linear dynamics, physics-informed neural network
 
## Citation
- **Journal:** Journal of Intelligent Manufacturing
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 
- **Publisher:** Springer Science and Business Media LLC
- **DOI:** [10.1007/s10845-026-02961-w](https://doi.org/10.1007/s10845-026-02961-w)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Liu_2026,
  title={{Physics-informed thermodynamical Hamiltonian hybrid modeling method for vibration prediction of electric spindles}},
  ISSN={1572-8145},
  DOI={10.1007/s10845-026-02961-w},
  journal={Journal of Intelligent Manufacturing},
  publisher={Springer Science and Business Media LLC},
  author={Liu, Xiaojian and Lu, Xinyu and Jia, Huishu and Zeng, Wei and Li, Wentian and Ji, Yangjian and Yi, Guodong and Wang, Kang and Qiu, Lemiao and Zhang, Shuyou},
  year={2026}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/physics-informed-thermodynamical-hamiltonian-hybrid-modeling-method-for-vibration-prediction-of-electric-spindles.bib)
 
## References
-  -- [10.1007/s11071-023-08618-0](https://doi.org/10.1007/s11071-023-08618-0)
- Abbasi A, Kambali PN, Shahidi P, Nataraj C (2024) Physics-informed machine learning for modeling multidimensional dynamics. Nonlinear Dyn 112(24):21565–21585. https://doi.org/10.1007/s11071-024-10163- -- [10.1007/s11071-024-10163-3](https://doi.org/10.1007/s11071-024-10163-3)
- Aggogeri F, Merlo A, Pellegrini N (2020) Modeling the thermo-mechanical deformations of machine tool structures in CFRP material adopting data-driven prediction schemes. Mechatronics 71:102436. https://doi.org/10.1016/j.mechatronics.2020.10243 -- [10.1016/j.mechatronics.2020.102436](https://doi.org/10.1016/j.mechatronics.2020.102436)
- Badlyan AM, Zimmer C (2018) Operator-GENERIC Formulation of Thermodynamics of Irreversible Processe -- [10.48550/arxiv.1807.09822](https://doi.org/10.48550/arxiv.1807.09822)
- Baur U, Benner P, Feng L (2014) Model Order Reduction for Linear and Nonlinear Systems: A System-Theoretic Perspective. Arch Computat Methods Eng 21(4):331–358. https://doi.org/10.1007/s11831-014-9111- -- [10.1007/s11831-014-9111-2](https://doi.org/10.1007/s11831-014-9111-2)
- Bermejo-Barbanoj C, Moya B, Badías A, Chinesta F, Cueto E (2024) Thermodynamics-informed super-resolution of scarce temporal dynamics data. Computer Methods in Applied Mechanics and Engineering 430:117210. https://doi.org/10.1016/j.cma.2024.11721 -- [10.1016/j.cma.2024.117210](https://doi.org/10.1016/j.cma.2024.117210)
- Cao H (2025) Dynamic Modeling of Rolling Bearings under Dynamic Contact Conditions. ACE 172(1):52–58. https://doi.org/10.54254/2755-2721/2025.gl2447 -- [10.54254/2755-2721/2025.gl24473](https://doi.org/10.54254/2755-2721/2025.gl24473)
- Chen Z, Zhang J, Arjovsky M, Bottou L (2019) Symplectic Recurrent Neural Networks. arXiv. https://doi.org/10.48550/ARXIV.1909.1333 -- [10.48550/arxiv.1909.13334](https://doi.org/10.48550/arxiv.1909.13334)
- Cranmer M, Greydanus S, Hoyer S, Battaglia P, Spergel D, Ho S (2020) Lagrangian Neural Network -- [10.48550/arxiv.2003.04630](https://doi.org/10.48550/arxiv.2003.04630)
- DiPietro R, Hager GD (2020) Deep learning: RNNs and LSTM. Handbook of Medical Image Computing and Computer Assisted Intervention 503–51 -- [10.1016/b978-0-12-816176-0.00026-0](https://doi.org/10.1016/b978-0-12-816176-0.00026-0)
- (2017) The Effect of Damping and Stiffness of Bearing on the Natural Frequencies of Rotor-bearing System. IJE 30(3). https://doi.org/10.5829/idosi.ije.2017.30.03c.1 -- [10.5829/idosi.ije.2017.30.03c.15](https://doi.org/10.5829/idosi.ije.2017.30.03c.15)
- Feng Z, Min X, Jiang W, Song F, Li X (2023) Study on Thermal Error Modeling for CNC Machine Tools Based on the Improved Radial Basis Function Neural Network. Applied Sciences 13(9):5299. https://doi.org/10.3390/app1309529 -- [10.3390/app13095299](https://doi.org/10.3390/app13095299)
- Greydanus S, Dzamba M, Yosinski J (2019) Hamiltonian Neural Network -- [10.48550/arxiv.1906.01563](https://doi.org/10.48550/arxiv.1906.01563)
- Grmela M (2018) GENERIC guide to the multiscale dynamics and thermodynamics. J Phys Commun 2(3):032001. https://doi.org/10.1088/2399-6528/aab64 -- [10.1088/2399-6528/aab642](https://doi.org/10.1088/2399-6528/aab642)
- Grmela M, Öttinger HC (1997) Dynamics and thermodynamics of complex fluids.  I. Development of a general formalism. Phys Rev E 56(6):6620–6632. https://doi.org/10.1103/physreve.56.662 -- [10.1103/physreve.56.6620](https://doi.org/10.1103/physreve.56.6620)
- Hernández Q, Badías A, Chinesta F, Cueto E (2024) Thermodynamics-Informed Graph Neural Networks. IEEE Trans Artif Intell 5(3):967–976. https://doi.org/10.1109/tai.2022.317968 -- [10.1109/tai.2022.3179681](https://doi.org/10.1109/tai.2022.3179681)
- Hernández Q, Badías A, González D, Chinesta F, Cueto E (2021) Structure-preserving neural networks. Journal of Computational Physics 426:109950. https://doi.org/10.1016/j.jcp.2020.10995 -- [10.1016/j.jcp.2020.109950](https://doi.org/10.1016/j.jcp.2020.109950)
- Hornik K, Stinchcombe M, White H (1990) Universal approximation of an unknown mapping and its derivatives using multilayer feedforward networks. Neural Networks 3(5):551–560. https://doi.org/10.1016/0893-6080(90)90005- -- [10.1016/0893-6080(90)90005-6](https://doi.org/10.1016/0893-6080(90)90005-6)
- Jiang S, Mao H (2010) Investigation of variable optimum preload for a machine tool spindle. International Journal of Machine Tools and Manufacture 50(1):19–28. https://doi.org/10.1016/j.ijmachtools.2009.10.00 -- [10.1016/j.ijmachtools.2009.10.001](https://doi.org/10.1016/j.ijmachtools.2009.10.001)
- JIN B, XU X (2025) LATE AND EARLY INDICA RICE’S PRICE FORECASTS THROUGH NEURAL NETWORKS. Int J Big Data Mini Glob Warm 07(02). https://doi.org/10.1142/s263053482550005 -- [10.1142/s2630534825500056](https://doi.org/10.1142/s2630534825500056)
- Jin B, Xu X (2025) Chinese energy security index price forecasting through the neural network. Innov Emerg Technol 12. https://doi.org/10.1142/s273759942550036 -- [10.1142/s2737599425500367](https://doi.org/10.1142/s2737599425500367)
- B Jin, Quality & Quantity (2026)
- Jin B, Xu X (2026) Contemporaneous Causal Analysis of Housing Prices Across Guangdong’s Major Cities: Employing Vector Error-Correction Modeling and Directed Acyclic Graphs. J Uncert Sys. https://doi.org/10.1142/s175289092650004 -- [10.1142/s1752890926500042](https://doi.org/10.1142/s1752890926500042)
- Jin L, Zhai X, Wang K, Zhang K, Wu D, Nazir A, Jiang J, Liao W-H (2024) Big data, machine learning, and digital twin assisted additive manufacturing: A review. Materials &amp; Design 244:113086. https://doi.org/10.1016/j.matdes.2024.11308 -- [10.1016/j.matdes.2024.113086](https://doi.org/10.1016/j.matdes.2024.113086)
- Jones D, Snider C, Nassehi A, Yon J, Hicks B (2020) Characterising the Digital Twin: A systematic literature review. CIRP Journal of Manufacturing Science and Technology 29:36–52. https://doi.org/10.1016/j.cirpj.2020.02.00 -- [10.1016/j.cirpj.2020.02.002](https://doi.org/10.1016/j.cirpj.2020.02.002)
- Lee CG, Park SC (2014) Survey on the virtual commissioning of manufacturing systems. Journal of Computational Design and Engineering 1(3):213–222. https://doi.org/10.7315/jcde.2014.02 -- [10.7315/jcde.2014.021](https://doi.org/10.7315/jcde.2014.021)
- Lu L, Pestourie R, Yao W, Wang Z, Verdugo F, Johnson SG (2021) Physics-informed neural networks with hard constraints for inverse desig -- [10.48550/arxiv.2102.04626](https://doi.org/10.48550/arxiv.2102.04626)
- Mahbubul IM, Saidur R, Amalina MA (2012) Latest developments on the viscosity of nanofluids. International Journal of Heat and Mass Transfer 55(4):874–885. https://doi.org/10.1016/j.ijheatmasstransfer.2011.10.02 -- [10.1016/j.ijheatmasstransfer.2011.10.021](https://doi.org/10.1016/j.ijheatmasstransfer.2011.10.021)
- Massaroli S, Poli M, Califano F, Faragasso A, Park J, Yamashita A, Asama H (2019) Port-Hamiltonian Approach to Neural Network Trainin -- [10.48550/arxiv.1909.02702](https://doi.org/10.48550/arxiv.1909.02702)
- Mayr J, Jedrzejewski J, Uhlmann E, Alkan Donmez M, Knapp W, Härtig F, Wendt K, Moriwaki T, Shore P, Schmitt R, Brecher C, Würz T, Wegener K (2012) Thermal issues in machine tools. CIRP Annals 61(2):771–791. https://doi.org/10.1016/j.cirp.2012.05.00 -- [10.1016/j.cirp.2012.05.008](https://doi.org/10.1016/j.cirp.2012.05.008)
- Minguzzi E (2015) Rayleigh’s dissipation function at work. Eur J Phys 36(3):035014. https://doi.org/10.1088/0143-0807/36/3/03501 -- [10.1088/0143-0807/36/3/035014](https://doi.org/10.1088/0143-0807/36/3/035014)
- Öttinger HC (2018) GENERIC: Review of successful applications and a challenge for the future. arXiv. https://doi.org/10.48550/ARXIV.1810.0847 -- [10.48550/arxiv.1810.08470](https://doi.org/10.48550/arxiv.1810.08470)
- Öttinger HC, Grmela M (1997) Dynamics and thermodynamics of complex fluids.  II. Illustrations of a general formalism. Phys Rev E 56(6):6633–6655. https://doi.org/10.1103/physreve.56.663 -- [10.1103/physreve.56.6633](https://doi.org/10.1103/physreve.56.6633)
- Qi S, Sarris CD (2023) Electromagnetic-Thermal Analysis With FDTD and Physics-Informed Neural Networks. IEEE J Multiscale Multiphys Comput Tech 8:49–59. https://doi.org/10.1109/jmmct.2023.323694 -- [10.1109/jmmct.2023.3236946](https://doi.org/10.1109/jmmct.2023.3236946)
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.04 -- [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
- [Ramirez H, Le Gorrec Y (2022) An Overview on Irreversible Port-Hamiltonian Systems. Entropy 24(10):1478. https://doi.org/10.3390/e2410147](an-overview-on-irreversible-port-hamiltonian-systems) -- [10.3390/e24101478](https://doi.org/10.3390/e24101478)
- Roth FJ, Klein DK, Kannapinn M, Peters J, Weeger O (2025) Stable Port-Hamiltonian Neural Network -- [10.48550/arxiv.2502.02480](https://doi.org/10.48550/arxiv.2502.02480)
- Sosanya A, Greydanus S (2022) Dissipative Hamiltonian Neural Networks: Learning Dissipative and Conservative Dynamics Separatel -- [10.48550/arxiv.2201.10085](https://doi.org/10.48550/arxiv.2201.10085)
- Srikantha Phani A, Adhikari S (2008) Rayleigh Quotient and Dissipative Systems. Journal of Applied Mechanics 75(6). https://doi.org/10.1115/1.291089 -- [10.1115/1.2910898](https://doi.org/10.1115/1.2910898)
- von Hahn T, Mechefske CK (2022) Machine Learning in CNC Machining: Best Practices. Machines 10(12):1233. https://doi.org/10.3390/machines1012123 -- [10.3390/machines10121233](https://doi.org/10.3390/machines10121233)
- Wang K, Liang X, Xu J, Zhang S, Tan J (2026) Style-augmented large-scale vision model with domain-generalized knowledge fusion for anomaly detection in powder bed additive manufacturing. Information Fusion 130:104108. https://doi.org/10.1016/j.inffus.2025.10410 -- [10.1016/j.inffus.2025.104108](https://doi.org/10.1016/j.inffus.2025.104108)
- Wang K, Lin H, Fang N, Xu J, Zhang S, Tan J, Qin J, Liang X (2025) Cross-patch graph transformer enforced by contrastive information fusion for energy demand forecasting towards sustainable additive manufacturing. Journal of Industrial Information Integration 45:100795. https://doi.org/10.1016/j.jii.2025.10079 -- [10.1016/j.jii.2025.100795](https://doi.org/10.1016/j.jii.2025.100795)
- Wang K, Liu L, Xu C, Zou J, Lin H, Fang N, Jiang J (2025) Towards label-free defect detection in additive manufacturing via dual-classifier semi-supervised learning for vision-language models. J Intell Manuf 37(3):1163–1178. https://doi.org/10.1007/s10845-025-02589- -- [10.1007/s10845-025-02589-2](https://doi.org/10.1007/s10845-025-02589-2)
- Wang K, Wang Z, Song X, Zhang Y, Liu X, Xu J, Zhang S, Tan J (2026) Physical-wavelet contextualized learning for isomerous locus decoupling in additive manufacturing. Expert Systems with Applications 327:132830. https://doi.org/10.1016/j.eswa.2026.13283 -- [10.1016/j.eswa.2026.132830](https://doi.org/10.1016/j.eswa.2026.132830)
- Xi S, Cao H, Chen X (2019) Dynamic modeling of spindle bearing system and vibration response investigation. Mechanical Systems and Signal Processing 114:486–511. https://doi.org/10.1016/j.ymssp.2018.05.02 -- [10.1016/j.ymssp.2018.05.028](https://doi.org/10.1016/j.ymssp.2018.05.028)
- Xu X, Zhang Y (2021) Individual time series and composite forecasting of the Chinese stock index. Machine Learning with Applications 5:100035. https://doi.org/10.1016/j.mlwa.2021.10003 -- [10.1016/j.mlwa.2021.100035](https://doi.org/10.1016/j.mlwa.2021.100035)
- Yang H, Ni J (2005) Dynamic neural network modeling for nonlinear, nonstationary machine tool thermally induced error. International Journal of Machine Tools and Manufacture 45(4–5):455–465. https://doi.org/10.1016/j.ijmachtools.2004.09.00 -- [10.1016/j.ijmachtools.2004.09.004](https://doi.org/10.1016/j.ijmachtools.2004.09.004)
- Zahedi A, Movahhedy MR (2012) Thermo-mechanical modeling of high speed spindles. Scientia Iranica 19(2):282–293. https://doi.org/10.1016/j.scient.2012.01.00 -- [10.1016/j.scient.2012.01.004](https://doi.org/10.1016/j.scient.2012.01.004)
- Zhang Y, Xu X (2022) Machine learning surface roughnesses in turning processes of brass metals. Int J Adv Manuf Technol 121(3–4):2437–2444. https://doi.org/10.1007/s00170-022-09498- -- [10.1007/s00170-022-09498-1](https://doi.org/10.1007/s00170-022-09498-1)
- Zhang Z, Shin Y, Em Karniadakis G (2022) GFINNs: GENERIC formalism informed neural networks for deterministic and stochastic dynamical systems. Phil Trans R Soc A 380(2229). https://doi.org/10.1098/rsta.2021.020 -- [10.1098/rsta.2021.0207](https://doi.org/10.1098/rsta.2021.0207)

