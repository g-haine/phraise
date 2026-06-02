---
title: "Real-Time Simulation of a Model-Predictive Control for PWM-VSC"
date: 2026-05-11 00:00:00 +0100
permalink: real-time-simulation-of-a-model-predictive-control-for-pwm-vsc
year: 2026
authors: Jhon-Ronald Terreros-Barreto, Walter Gil-González, Alejandro Garcés-Ruiz, Luis M. Fernández-Ramírez, Pablo Horrillo-Quintero, David Carrasco-González
category: articles
---
 
## Authors
[Jhon-Ronald Terreros-Barreto](authors/jhon-ronald-terreros-barreto), [Walter Gil-González](authors/walter-julian-gil-gonzalez), [Alejandro Garcés-Ruiz](authors/alejandro-garces-ruiz), [Luis M. Fernández-Ramírez](authors/luis-m-fernandez-ramirez), [Pablo Horrillo-Quintero](authors/pablo-horrillo-quintero), [David Carrasco-González](authors/david-carrasco-gonzalez)
 
## Abstract
This paper proposes a passivity-based model predictive control (PB-MPC) strategy for a grid-connected photovoltaic system (PVS). The approach combines port-Hamiltonian modeling (pH) with the predictive and constraint-handling capabilities of MPC, preserving the system’s energy structure while enabling explicit constraint management. A discrete-time incremental pH formulation is derived, from which system passivity is theoretically established. The control problem is solved using a single-iteration Newton–Raphson scheme per sampling step, where control input constraints are enforced through projection onto the admissible control set, enabling real-time implementation. Simulation results demonstrate superior performance compared with conventional MPC and Porportional-Integral (PI) controllers, while additional analyzes confirm robustness, computational efficiency, and passivity preservation of the proposed controller. Real-time hardware-in-the-loop (HIL) validation using the OPAL-RT OP4512 platform further demonstrates improved dynamic response and reduced settling time.
 
## Citation
- **Journal:** IEEE Access
- **Year:** 2026
- **Volume:** 14
- **Issue:** 
- **Pages:** 72977--72991
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/access.2026.3692281](https://doi.org/10.1109/access.2026.3692281)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Terreros_Barreto_2026,
  title={{Real-Time Simulation of a Model-Predictive Control for PWM-VSC}},
  volume={14},
  ISSN={2169-3536},
  DOI={10.1109/access.2026.3692281},
  journal={IEEE Access},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Terreros-Barreto, Jhon-Ronald and Gil-González, Walter and Garcés-Ruiz, Alejandro and Fernández-Ramírez, Luis M. and Horrillo-Quintero, Pablo and Carrasco-González, David},
  year={2026},
  pages={72977--72991}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/real-time-simulation-of-a-model-predictive-control-for-pwm-vsc.bib)
 
## References
- Razmi D, Babayomi O, Davari A, Rahimi T, Miao Y, Zhang Z (2022) Review of Model Predictive Control of Distributed Energy Resources in Microgrids. Symmetry 14(8):1735. https://doi.org/10.3390/sym1408173 -- [10.3390/sym14081735](https://doi.org/10.3390/sym14081735)
- Seneviratne C, Ozansoy C (2016) Frequency response due to a large generator loss with the increasing penetration of wind/PV generation – A literature review. Renewable and Sustainable Energy Reviews 57:659–668. https://doi.org/10.1016/j.rser.2015.12.05 -- [10.1016/j.rser.2015.12.051](https://doi.org/10.1016/j.rser.2015.12.051)
- Singh B, Pathak G, Panigrahi BK (2018) Seamless Transfer of Renewable-Based Microgrid Between Utility Grid and Diesel Generator. IEEE Trans Power Electron 33(10):8427–8437. https://doi.org/10.1109/tpel.2017.277810 -- [10.1109/tpel.2017.2778104](https://doi.org/10.1109/tpel.2017.2778104)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Cisneros R, Pirro M, Bergna G, Ortega R, Ippoliti G, Molinas M (2015) Global tracking passivity-based PI control of bilinear systems: Application to the interleaved boost and modular multilevel converters. Control Engineering Practice 43:109–119. https://doi.org/10.1016/j.conengprac.2015.07.00 -- [10.1016/j.conengprac.2015.07.002](https://doi.org/10.1016/j.conengprac.2015.07.002)
- Gil-González W, Montoya OD, Garces A (2020) Standard passivity-based control for multi-hydro-turbine governing systems with surge tank. Applied Mathematical Modelling 79:1–17. https://doi.org/10.1016/j.apm.2019.11.01 -- [10.1016/j.apm.2019.11.010](https://doi.org/10.1016/j.apm.2019.11.010)
- Li P, Wang J, Bai J (2018) A Passivity-Based Control Strategy for Three-Phase Current Source Inverter Based on Interconnection and Damping Assignment. 2018 10th International Conference on Modelling, Identification and Control (ICMIC) 1– -- [10.1109/icmic.2018.8530001](https://doi.org/10.1109/icmic.2018.8530001)
- Mancilla-David F, Ortega R (2012) Adaptive passivity-based control for maximum power extraction of stand-alone windmill systems. Control Engineering Practice 20(2):173–181. https://doi.org/10.1016/j.conengprac.2011.10.00 -- [10.1016/j.conengprac.2011.10.008](https://doi.org/10.1016/j.conengprac.2011.10.008)
- Cortes P, Kazmierkowski MP, Kennel RM, Quevedo DE, Rodriguez J (2008) Predictive Control in Power Electronics and Drives. IEEE Trans Ind Electron 55(12):4312–4324. https://doi.org/10.1109/tie.2008.200748 -- [10.1109/tie.2008.2007480](https://doi.org/10.1109/tie.2008.2007480)
- Ahmed K, Seyedmahmoudian M, Mekhilef S, M. Mubarak N, Stojcevski A (2021) A Review on Primary and Secondary Controls of Inverter-interfaced Microgrid. Journal of Modern Power Systems and Clean Energy 9(5):969–985. https://doi.org/10.35833/mpce.2020.00006 -- [10.35833/mpce.2020.000068](https://doi.org/10.35833/mpce.2020.000068)
- Erika Twining, Holmes DG (2003) Grid current regulation of a three-phase voltage source inverter with an LCL input filter. IEEE Trans Power Electron 18(3):888–895. https://doi.org/10.1109/tpel.2003.81083 -- [10.1109/tpel.2003.810838](https://doi.org/10.1109/tpel.2003.810838)
- Saccomando G, Svensson J Transient operation of grid-connected voltage source converter under unbalanced voltage conditions. Conference Record of the 2001 IEEE Industry Applications Conference. 36th IAS Annual Meeting (Cat. No.01CH37248) 4:2419–242 -- [10.1109/ias.2001.955960](https://doi.org/10.1109/ias.2001.955960)
- Blaabjerg F, Teodorescu R, Liserre M, Timbus AV (2006) Overview of Control and Grid Synchronization for Distributed Power Generation Systems. IEEE Trans Ind Electron 53(5):1398–1409. https://doi.org/10.1109/tie.2006.88199 -- [10.1109/tie.2006.881997](https://doi.org/10.1109/tie.2006.881997)
- Hai Lin, Lipo TA, Byung-il Kwon, Sung Rock Cheon (2012) Three-level hysteresis current control for a three-phase permanent magnet synchronous motor drive. Proceedings of The 7th International Power Electronics and Motion Control Conference 1004–100 -- [10.1109/ipemc.2012.6258938](https://doi.org/10.1109/ipemc.2012.6258938)
- Malesani L, Tenti P (1990) A novel hysteresis control method for current-controlled voltage-source PWM inverters with constant modulation frequency. IEEE Trans on Ind Applicat 26(1):88–92. https://doi.org/10.1109/28.5267 -- [10.1109/28.52678](https://doi.org/10.1109/28.52678)
- Mattavelli P, Spiazzi G, Tenti P (2005) Predictive Digital Control of Power Factor Preregulators With Input Voltage Estimation Using Disturbance Observers. IEEE Trans Power Electron 20(1):140–147. https://doi.org/10.1109/tpel.2004.83982 -- [10.1109/tpel.2004.839821](https://doi.org/10.1109/tpel.2004.839821)
- Zmood DN, Holmes DG, Bode G Frequency domain analysis of three phase linear current regulators. Conference Record of the 1999 IEEE Industry Applications Conference. Thirty-Forth IAS Annual Meeting (Cat. No.99CH36370) 2:818–82 -- [10.1109/ias.1999.801601](https://doi.org/10.1109/ias.1999.801601)
- Kazmierkowski, Control in Power Electronics: Selected problems (2002)
- Fukuda S, Yoda T (2001) A novel current-tracking method for active filters based on a sinusoidal internal model [for PWM invertors]. IEEE Trans on Ind Applicat 37(3):888–895. https://doi.org/10.1109/28.92477 -- [10.1109/28.924772](https://doi.org/10.1109/28.924772)
- Campanhol LBG, da Silva SAO, de Oliveira AA, Bacon VD (2017) Single-Stage Three-Phase Grid-Tied PV System With Universal Filtering Capability Applied to DG Systems and AC Microgrids. IEEE Trans Power Electron 32(12):9131–9142. https://doi.org/10.1109/tpel.2017.265938 -- [10.1109/tpel.2017.2659381](https://doi.org/10.1109/tpel.2017.2659381)
- Sanchis P, Ursaea A, Gubia E, Marroyo L (2005) Boost DC–AC Inverter: A New Control Strategy. IEEE Trans Power Electron 20(2):343–353. https://doi.org/10.1109/tpel.2004.84300 -- [10.1109/tpel.2004.843000](https://doi.org/10.1109/tpel.2004.843000)
- Shih-Liang Jung, Hsiang-Sung Huang, Meng-Yueh Chang, Ying-Yu Tzou DSP-based multiple-loop control strategy for single-phase inverters used in AC power sources. PESC97. Record 28th Annual IEEE Power Electronics Specialists Conference. Formerly Power Conditioning Specialists Conference 1970-71. Power Processing and Electronic Specialists Conference 1972 1:706–71 -- [10.1109/pesc.1997.616798](https://doi.org/10.1109/pesc.1997.616798)
- Azli NA, Ning WS Application of fuzzy logic in an optimal PWM based control scheme for a multilevel inverter. The Fifth International Conference on Power Electronics and Drive Systems, 2003. PEDS 2003. 2:1280–128 -- [10.1109/peds.2003.1283162](https://doi.org/10.1109/peds.2003.1283162)
- Xiao Sun, Chow MHL, Leung FHF, Dehong Xu, Yousheng Wang, Yim-Shu Lee (2002) Analogue implementation of a neural network controller for UPS inverter applications. IEEE Trans Power Electron 17(3):305–313. https://doi.org/10.1109/tpel.2002.100423 -- [10.1109/tpel.2002.1004238](https://doi.org/10.1109/tpel.2002.1004238)
- Perry AG, Feng G, Liu Y-F, Sen PC A new design method for PI-like fuzzy logic controllers for DC-to-DC converters. 2004 IEEE 35th Annual Power Electronics Specialists Conference (IEEE Cat. No.04CH37551) 3751–375 -- [10.1109/pesc.2004.1355138](https://doi.org/10.1109/pesc.2004.1355138)
- En-Chih Chang, Tsomg-Jau Liang, Jiann-Fuh Chen, Ray-Lee Lin A sliding-mode controller based on fuzzy logic for PWM inverters. The 2004 IEEE Asia-Pacific Conference on Circuits and Systems, 2004. Proceedings. 2:965–96 -- [10.1109/apccas.2004.1413041](https://doi.org/10.1109/apccas.2004.1413041)
- Agbemuko AJ, Dominguez-Garcia JL, Gomis-Bellmunt O, Harnefors L (2021) Passivity-Based Analysis and Performance Enhancement of a Vector Controlled VSC Connected to a Weak AC Grid. IEEE Trans Power Delivery 36(1):156–167. https://doi.org/10.1109/tpwrd.2020.298249 -- [10.1109/tpwrd.2020.2982498](https://doi.org/10.1109/tpwrd.2020.2982498)
- [Gil-Gonzalez W, Garces A, Fosso OB (2020) Passivity-Based Control for Small Hydro-Power Generation With PMSG and VSC. IEEE Access 8:153001–153010. https://doi.org/10.1109/access.2020.301802](passivity-based-control-for-small-hydro-power-generation-with-pmsg-and-vsc) -- [10.1109/access.2020.3018027](https://doi.org/10.1109/access.2020.3018027)
- Vazquez S, Leon JI, Franquelo LG, Rodriguez J, Young HA, Marquez A, Zanchetta P (2014) Model Predictive Control: A Review of Its Applications in Power Electronics. EEE Ind Electron Mag 8(1):16–31. https://doi.org/10.1109/mie.2013.229013 -- [10.1109/mie.2013.2290138](https://doi.org/10.1109/mie.2013.2290138)
- Tarisciotti L, Zanchetta P, Watson A, Clare JC, Degano M, Bifaretti S (2015) Modulated Model Predictive Control for a Three-Phase Active Rectifier. IEEE Trans on Ind Applicat 51(2):1610–1620. https://doi.org/10.1109/tia.2014.233939 -- [10.1109/tia.2014.2339397](https://doi.org/10.1109/tia.2014.2339397)
- Hammoud I, Hentzelt S, Xu K, Oehlschlagel T, Abdelrahem M, Hackl C, Kennel R (2022) On Continuous-Set Model Predictive Control of Permanent Magnet Synchronous Machines. IEEE Trans Power Electron 37(9):10360–10371. https://doi.org/10.1109/tpel.2022.316496 -- [10.1109/tpel.2022.3164968](https://doi.org/10.1109/tpel.2022.3164968)
- Karamanakos P, Liegmann E, Geyer T, Kennel R (2020) Model Predictive Control of Power Electronic Systems: Methods, Results, and Challenges. IEEE Open J Ind Applicat 1:95–114. https://doi.org/10.1109/ojia.2020.302018 -- [10.1109/ojia.2020.3020184](https://doi.org/10.1109/ojia.2020.3020184)
- Schuetz DA, Carnielutti F de M, Aly M, Norambuena M, Rodriguez J, Pinheiro H (2024) Fast FCS-MPC for neutral-point clamped converters with switching constraints. Control Engineering Practice 150:106006. https://doi.org/10.1016/j.conengprac.2024.10600 -- [10.1016/j.conengprac.2024.106006](https://doi.org/10.1016/j.conengprac.2024.106006)
- Zamani H, Abbaszadeh K, Gyselinck J, Karimi M (2023) Robust Continuous Control Set Model Predictive Control in Synchronous Reference Frame for Grid-Tied Inverters. IEEE J Emerg Sel Top Ind Electron 4(1):209–218. https://doi.org/10.1109/jestie.2022.318347 -- [10.1109/jestie.2022.3183474](https://doi.org/10.1109/jestie.2022.3183474)
- Zhu Y, Wen H, Yang Y, Mao J, Wang P, Huang W, Rodriguez J (2024) Decoupled Continuous Control Set Model Predictive Control for T-Type Three-Phase Four-Leg Three-Level Inverters Driving Constant Power Loads. IEEE Trans Power Electron 39(6):7002–7015. https://doi.org/10.1109/tpel.2024.337952 -- [10.1109/tpel.2024.3379521](https://doi.org/10.1109/tpel.2024.3379521)
- Ren B, Zhu Y, Sun X, Pan Z, Zhao W (2023) Dynamic Performance Improvement of Continuous Control Set Model Predictive Control for High-Frequency Link Matrix Converter. IEEE Trans Ind Electron 70(9):9057–9066. https://doi.org/10.1109/tie.2022.321544 -- [10.1109/tie.2022.3215447](https://doi.org/10.1109/tie.2022.3215447)
- Trabelsi M, Bayhan S, Ghazi KA, Abu-Rub H, Ben-Brahim L (2016) Finite-Control-Set Model Predictive Control for Grid-Connected Packed-U-Cells Multilevel Inverter. IEEE Trans Ind Electron 63(11):7286–7295. https://doi.org/10.1109/tie.2016.255814 -- [10.1109/tie.2016.2558142](https://doi.org/10.1109/tie.2016.2558142)
- Kanouni B, Badoud AE, Mekhilef S (2022) A multi-objective model predictive current control with two-step horizon for double-stage grid-connected inverter PEMFC system. International Journal of Hydrogen Energy 47(4):2685–2707. https://doi.org/10.1016/j.ijhydene.2021.10.18 -- [10.1016/j.ijhydene.2021.10.182](https://doi.org/10.1016/j.ijhydene.2021.10.182)
- Urrutia M, Cardenas R, Clare JC, Watson A (2021) Circulating Current Control for the Modular Multilevel Matrix Converter Based on Model Predictive Control. IEEE J Emerg Sel Topics Power Electron 9(5):6069–6085. https://doi.org/10.1109/jestpe.2021.307196 -- [10.1109/jestpe.2021.3071964](https://doi.org/10.1109/jestpe.2021.3071964)
- Tarisciotti L, Zanchetta P, Watson A, Bifaretti S, Clare JC (2014) Modulated Model Predictive Control for a Seven-Level Cascaded H-Bridge Back-to-Back Converter. IEEE Trans Ind Electron 61(10):5375–5383. https://doi.org/10.1109/tie.2014.230005 -- [10.1109/tie.2014.2300056](https://doi.org/10.1109/tie.2014.2300056)
- Kadhum H, Watson AJ, Rivera M, Zanchetta P, Wheeler P (2024) Model Predictive Control of a Modular Multilevel Converter with Reduced Computational Burden. Energies 17(11):2519. https://doi.org/10.3390/en1711251 -- [10.3390/en17112519](https://doi.org/10.3390/en17112519)
- Alharbi Y, Darwish A, Ma X (2025) A Review of Model Predictive Control for Grid-Connected PV Applications. Electronics 14(4):667. https://doi.org/10.3390/electronics1404066 -- [10.3390/electronics14040667](https://doi.org/10.3390/electronics14040667)
- Sajadian S, Ahmadi R (2016) Model Predictive-Based Maximum Power Point Tracking for Grid-Tied Photovoltaic Applications Using a &lt;italic&gt;Z&lt;/italic&gt;-Source Inverter. IEEE Trans Power Electron 31(11):7611–7620. https://doi.org/10.1109/tpel.2016.253781 -- [10.1109/tpel.2016.2537814](https://doi.org/10.1109/tpel.2016.2537814)
- Errouissi R, Al-Durra A, Muyeen SM (2016) A Robust Continuous-Time MPC of a DC–DC Boost Converter Interfaced With a Grid-Connected Photovoltaic System. IEEE J Photovoltaics 6(6):1619–1629. https://doi.org/10.1109/jphotov.2016.259827 -- [10.1109/jphotov.2016.2598271](https://doi.org/10.1109/jphotov.2016.2598271)
- Oyuela-Ocampo J-C, Garcés-Ruiz A, Sanchez-Acevedo S, Ljøkelsøy K, D’Arco S (2025) Continuous Control-Set Model-Predictive Control with stability guarantee for the PWM-VSC. Control Engineering Practice 157:106246. https://doi.org/10.1016/j.conengprac.2025.10624 -- [10.1016/j.conengprac.2025.106246](https://doi.org/10.1016/j.conengprac.2025.106246)
- Astolfi A, Karagiannis D, Ortega R (2008) Nonlinear and Adaptive Control with Applications. Springer Londo -- [10.1007/978-1-84800-066-7](https://doi.org/10.1007/978-1-84800-066-7)
- [van der Schaft A (2007) Port-Hamiltonian systems: an introductory survey. Proceedings of the International Congress of Mathematicians Madrid, August 22–30, 2006 1339–136](port-hamiltonian-systems-an-introductory-survey) -- [10.4171/022-3/65](https://doi.org/10.4171/022-3/65)
- Yang B, Yu T, Shu H, Zhu D, Sang Y, Jiang L (2018) Passivity-based fractional-order sliding-mode control design and implementation of grid-connected photovoltaic systems. Journal of Renewable and Sustainable Energy 10(4). https://doi.org/10.1063/1.503226 -- [10.1063/1.5032266](https://doi.org/10.1063/1.5032266)
- [Gil-González W, Montoya OD, Garces A (2019) Direct power control for VSC-HVDC systems: An application of the global tracking passivity-based PI approach. International Journal of Electrical Power &amp; Energy Systems 110:588–597. https://doi.org/10.1016/j.ijepes.2019.03.04](direct-power-control-for-vsc-hvdc-systems-an-application-of-the-global-tracking-passivity-based-pi-approach) -- [10.1016/j.ijepes.2019.03.042](https://doi.org/10.1016/j.ijepes.2019.03.042)
- Garces-Ruiz, Discrete-time port-Hamiltonian systems for power and energy applications the work of the first author was partially supported by the maestría en ingeniería eléctrica de la universidad tecnológica de pereira and the project climat-amsud: Mitigating climate change with power electronics and smart-technologies financed by minciencias. The work of second and third authors was supported by dgapa-unam under grants in117123 and in109622. IFAC-PapersOnLine (2024)

