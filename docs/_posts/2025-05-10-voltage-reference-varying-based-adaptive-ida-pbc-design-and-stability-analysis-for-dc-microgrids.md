---
title: "Voltage reference varying-based adaptive IDA-PBC design and stability analysis for DC microgrids"
date: 2025-05-10 00:00:00 +0100
permalink: voltage-reference-varying-based-adaptive-ida-pbc-design-and-stability-analysis-for-dc-microgrids
year: 2025
authors: Cong Yuan, Jean-Philippe Martin, Serge Pierfederici, Matheepot Phattanasak, Farid Meibody-Tabar, Shengzhao Pang
category: articles
tags:
  - constant power loads, dc microgrids, eigenvalues, ida-pbc, jacobian matrix, lyapunov function, stability analysis
---
 
## Authors
[Cong Yuan](authors/cong-yuan), [Jean-Philippe Martin](authors/jean-philippe-martin), [Serge Pierfederici](authors/serge-pierfederici), [Matheepot Phattanasak](authors/matheepot-phattanasak), [Farid Meibody-Tabar](authors/farid-meibody-tabar), [Shengzhao Pang](authors/shengzhao-pang)
 
## Abstract
Constant Power Loads (CPLs), which are widely present in DC microgrids, exhibit negative impedance characteristics, reducing the system’s stability margin and posing significant challenges to grid control and stability. To address this issue, we propose an Interconnection and Damping Assignment Passivity-Based Control (IDA-PBC) strategy. By reshaping system energy and injecting damping, the proposed controller ensures the attainment of the desired equilibrium point and dynamic performance, thereby enhancing the microgrid’s stability margin. Unlike conventional IDA-PBC methods, which typically modify the interconnection matrix by introducing a parameter K to obtain a unique control law solution, our approach achieves a unique solution by redefining the reference voltage. This strategy effectively eliminates singularity issues at the equilibrium point. Furthermore, we conduct a comprehensive stability analysis of the proposed IDA-PBC, derive the system’s stability margin, and design a trajectory-tracking controller to validate its advantages in improving stability. Finally, numerical simulations and experiments are performed to verify both the effectiveness of the proposed controller and the accuracy of the stability analysis.
 
## Keywords
constant power loads, dc microgrids, eigenvalues, ida-pbc, jacobian matrix, lyapunov function, stability analysis
 
## Citation
- **Journal:** Mathematics and Computers in Simulation
- **Year:** 2025
- **Volume:** 237
- **Issue:** 
- **Pages:** 355--372
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.matcom.2025.04.028](https://doi.org/10.1016/j.matcom.2025.04.028)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Yuan_2025,
  title={{Voltage reference varying-based adaptive IDA-PBC design and stability analysis for DC microgrids}},
  volume={237},
  ISSN={0378-4754},
  DOI={10.1016/j.matcom.2025.04.028},
  journal={Mathematics and Computers in Simulation},
  publisher={Elsevier BV},
  author={Yuan, Cong and Martin, Jean-Philippe and Pierfederici, Serge and Phattanasak, Matheepot and Meibody-Tabar, Farid and Pang, Shengzhao},
  year={2025},
  pages={355--372}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/voltage-reference-varying-based-adaptive-ida-pbc-design-and-stability-analysis-for-dc-microgrids.bib)
 
## References
- Breyer C, Khalili S, Bogdanov D, Ram M, Oyewo AS, Aghahosseini A, Gulagi A, Solomon AA, Keiner D, Lopez G, Ostergaard PA, Lund H, Mathiesen BV, Jacobson MZ, Victoria M, Teske S, Pregger T, Fthenakis V, Raugei M, Holttinen H, Bardi U, Hoekstra A, Sovacool BK (2022) On the History and Future of 100% Renewable Energy Systems Research. IEEE Access 10:78176–78218. https://doi.org/10.1109/access.2022.319340 -- [10.1109/access.2022.3193402](https://doi.org/10.1109/access.2022.3193402)
- Al-Ismail FS (2021) DC Microgrid Planning, Operation, and Control: A Comprehensive Review. IEEE Access 9:36154–36172. https://doi.org/10.1109/access.2021.306284 -- [10.1109/access.2021.3062840](https://doi.org/10.1109/access.2021.3062840)
- Yuan C, Bai H, Ma R, Huangfu Y (2022) Large-Signal Stability Analysis and Design of Finite-Time Controller for the Electric Vehicle DC Power System. IEEE Trans on Ind Applicat 58(1):868–878. https://doi.org/10.1109/tia.2021.312562 -- [10.1109/tia.2021.3125621](https://doi.org/10.1109/tia.2021.3125621)
- Li H, Liu Q, Zhang Z, Liu C, Li Z, Yang Z, Zheng TQ (2022) A Describing Function-Based Stability Analysis Method for Cascaded DC-DC Converters. IEEE Open J Ind Electron Soc 3:484–495. https://doi.org/10.1109/ojies.2022.319190 -- [10.1109/ojies.2022.3191906](https://doi.org/10.1109/ojies.2022.3191906)
- Triggianese M, Carbonnier H, Tonicello F (2019) Revised stability criteria for cascaded DC-DC converters in space applications. 2019 European Space Power Conference (ESPC) 1– -- [10.1109/espc.2019.8932078](https://doi.org/10.1109/espc.2019.8932078)
- Wang, Continuous nonsingular terminal sliding mode control of DC–DC boost converters subject to time-varying disturbances. IEEE Trans. Circuits Syst. II: Express Briefs (2020)
- Xu Q, Jiang W, Blaabjerg F, Zhang C, Zhang X, Fernando T (2020) Backstepping Control for Large Signal Stability of High Boost Ratio Interleaved Converter Interfaced DC Microgrids With Constant Power Loads. IEEE Trans Power Electron 35(5):5397–5407. https://doi.org/10.1109/tpel.2019.294388 -- [10.1109/tpel.2019.2943889](https://doi.org/10.1109/tpel.2019.2943889)
- Yuan C, Huangfu Y, Bai H, Pang S, Shi W, Zhang H (2023) Stability Analysis and Stabilization Improvement of the DC Power System for Unmanned Aerial Vehicle Based on the Finite-Time Controller. IEEE Trans on Ind Applicat 59(6):7570–7583. https://doi.org/10.1109/tia.2023.329926 -- [10.1109/tia.2023.3299261](https://doi.org/10.1109/tia.2023.3299261)
- Cespedes M, Xing L, Sun J (2011) Constant-Power Load System Stabilization by Passive Damping. IEEE Trans Power Electron 26(7):1832–1836. https://doi.org/10.1109/tpel.2011.215188 -- [10.1109/tpel.2011.2151880](https://doi.org/10.1109/tpel.2011.2151880)
- Iyer VM, Gulur S, Bhattacharya S (2019) Small-Signal Stability Assessment and Active Stabilization of a Bidirectional Battery Charger. IEEE Trans on Ind Applicat 55(1):563–574. https://doi.org/10.1109/tia.2018.287110 -- [10.1109/tia.2018.2871101](https://doi.org/10.1109/tia.2018.2871101)
- Lorzadeh O, Lorzadeh I, Soltani MN, Hajizadeh A (2021) Source-Side Virtual RC Damper-Based Stabilization Technique for Cascaded Systems in DC Microgrids. IEEE Trans Energy Convers 36(3):1883–1895. https://doi.org/10.1109/tec.2021.305589 -- [10.1109/tec.2021.3055897](https://doi.org/10.1109/tec.2021.3055897)
- [Pang S, Nahid-Mobarakeh B, Hashjin SA, Pierfederici S, Martin J-P, Liu Y, Huangfu Y, Luo G, Gao F (2021) Stability Improvement of Cascaded Power Conversion Systems Based on Hamiltonian Energy Control Theory. IEEE Trans on Ind Applicat 57(1):1081–1093. https://doi.org/10.1109/tia.2020.303835](stability-improvement-of-cascaded-power-conversion-systems-based-on-hamiltonian-energy-control-theory) -- [10.1109/tia.2020.3038355](https://doi.org/10.1109/tia.2020.3038355)
- Pang S, Hashjin SA, Nahid-Mobarakeh B, Pierfederici S, Huangfu Y, Luo G, Gao F (2021) Large-Signal Stabilization of Power Converters Cascaded Input Filter Using Adaptive Energy Shaping Control. IEEE Trans Transp Electrific 7(2):838–853. https://doi.org/10.1109/tte.2020.302195 -- [10.1109/tte.2020.3021954](https://doi.org/10.1109/tte.2020.3021954)
- Pang S, Nahid-Mobarakeh B, Pierfederici S, Huangfu Y, Luo G, Gao F (2021) Large-Signal Stable Nonlinear Control of DC/DC Power Converter With Online Estimation of Uncertainties. IEEE J Emerg Sel Topics Power Electron 9(6):7355–7368. https://doi.org/10.1109/jestpe.2020.301089 -- [10.1109/jestpe.2020.3010895](https://doi.org/10.1109/jestpe.2020.3010895)
- Song Q, Chen J, Loo K-H, Chen J, Chen P (2024) Large-Signal Stability Analysis of Two-Stage Cascaded DC/DC Converter Systems Using Sum-of-Squares Programming. IEEE Trans Power Electron 39(2):2076–2085. https://doi.org/10.1109/tpel.2023.333084 -- [10.1109/tpel.2023.3330841](https://doi.org/10.1109/tpel.2023.3330841)
- Tang WH, Li WW, Zheng JH, Wu CQ, Wang LX, Wei QL, Wu QH (2022) A composite voltage stability index for integrated energy systems based on L-index and the minimum eigenvalue of reduced Jacobian matrix. International Journal of Electrical Power &amp; Energy Systems 141:108136. https://doi.org/10.1016/j.ijepes.2022.10813 -- [10.1016/j.ijepes.2022.108136](https://doi.org/10.1016/j.ijepes.2022.108136)
- Maschke, Port-controlled Hamiltonian systems: modelling origins and systemtheoretic properties. (1993)

