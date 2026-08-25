---
title: "Energy-Consistent Super-Twisting Sliding-Mode Control of a Grid-Forming LC Inverter: A Port-Hamiltonian Diagnostic Perspective"
date: 2026-08-20 00:00:00 +0100
permalink: energy-consistent-super-twisting-sliding-mode-control-of-a-grid-forming-lc-inverter-a-port-hamiltonian-diagnostic-perspective
year: 2026
authors: Ahmet Çakanel
category: proceedings
---
 
## Authors
[Ahmet Çakanel](authors/ahmet-cakanel)
 
## Abstract
This paper presents an energy-consistent super-twisting (ST) sliding-mode control design for a single-phase grid-forming inverter with an output LC filter, motivated by inverter-dominated low-inertia power-electronic applications. Throughout, energy-consistent refers to a sliding surface whose closed-loop motion is shaped to avoid large transient excursions of the filter Hamiltonian. The surface couples the voltage error, its integral, and the inductor current, and its design is informed by the port-Hamiltonian (PH) representation of the LC filter; the Hamiltonian is employed as a physically meaningful diagnostic rather than as a strict control structure. A super-twisting reaching law is used to provide continuous control action and finite-time convergence under bounded matched perturbations, with explicit gain conditions stated. An actuator saturation constraint is included in the model and its effect is reported. The proposed controller is benchmarked against a classical first-order SMC with boundary layer on the same sliding surface, isolating the contribution of the ST reaching law. Simulation studies on a grid-forming LC inverter subject to renewable-like disturbances and parameter uncertainties show that the ST controller reduces steady-state tracking error, control chatter, and Hamiltonian variation by a factor of two or more across the tested operating envelope, while the gain-sensitivity coefficient of variation of \\( \Delta {\mathcal{H}[[:space:]]} \\) stays below 3 over a [0.5,1.5]× nominal gain box.
 
## Citation
- **Journal:** 2026 IEEE 18th International Workshop on Variable Structure Systems (VSS)
- **Year:** 2026
- **Volume:** 
- **Issue:** 
- **Pages:** 335--340
- **Publisher:** IEEE
- **DOI:** [10.1109/vss69650.2026.11655837](https://doi.org/10.1109/vss69650.2026.11655837)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{_akanel_2026,
  title={{Energy-Consistent Super-Twisting Sliding-Mode Control of a Grid-Forming LC Inverter: A Port-Hamiltonian Diagnostic Perspective}},
  DOI={10.1109/vss69650.2026.11655837},
  booktitle={{2026 IEEE 18th International Workshop on Variable Structure Systems (VSS)}},
  publisher={IEEE},
  author={Çakanel, Ahmet},
  year={2026},
  pages={335--340}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/energy-consistent-super-twisting-sliding-mode-control-of-a-grid-forming-lc-inverter-a-port-hamiltonian-diagnostic-perspective.bib)
 
## References
- Dörfler F, Chertkov M, Bullo F (2013) Synchronization in complex oscillator networks and smart grids. Proc Natl Acad Sci USA 110(6):2005–2010. https://doi.org/10.1073/pnas.121213411 -- [10.1073/pnas.1212134110](https://doi.org/10.1073/pnas.1212134110)
- Milano F, Dörfler F, Hug G, Hill DJ, Verbič G (2018) Foundations and Challenges of Low-Inertia Systems (Invited Paper). 2018 Power Systems Computation Conference (PSCC) 1–2 -- [10.23919/pscc.2018.8450880](https://doi.org/10.23919/pscc.2018.8450880)
- Hatziargyriou N, Milanovic J, Rahmann C, Ajjarapu V, Canizares C, Erlich I, Hill D, Hiskens I, Kamwa I, Pal B, Pourbeik P, Sanchez-Gasca J, Stankovic A, Van Cutsem T, Vittal V, Vournas C (2021) Definition and Classification of Power System Stability – Revisited &amp; Extended. IEEE Trans Power Syst 36(4):3271–3281. https://doi.org/10.1109/tpwrs.2020.304177 -- [10.1109/tpwrs.2020.3041774](https://doi.org/10.1109/tpwrs.2020.3041774)
- Lasseter RH MicroGrids. 2002 IEEE Power Engineering Society Winter Meeting. Conference Proceedings (Cat. No.02CH37309) 1:305–30 -- [10.1109/pesw.2002.985003](https://doi.org/10.1109/pesw.2002.985003)
- Lasseter RH, Chen Z, Pattabiraman D (2020) Grid-Forming Inverters: A Critical Asset for the Power Grid. IEEE J Emerg Sel Topics Power Electron 8(2):925–935. https://doi.org/10.1109/jestpe.2019.295927 -- [10.1109/jestpe.2019.2959271](https://doi.org/10.1109/jestpe.2019.2959271)
- Rocabert J, Luna A, Blaabjerg F, Rodríguez P (2012) Control of Power Converters in AC Microgrids. IEEE Trans Power Electron 27(11):4734–4749. https://doi.org/10.1109/tpel.2012.219933 -- [10.1109/tpel.2012.2199334](https://doi.org/10.1109/tpel.2012.2199334)
- Utkin V (1977) Variable structure systems with sliding modes. IEEE Trans Automat Contr 22(2):212–222. https://doi.org/10.1109/tac.1977.110144 -- [10.1109/tac.1977.1101446](https://doi.org/10.1109/tac.1977.1101446)
- LEVANT A (1993) Sliding order and sliding accuracy in sliding mode control. International Journal of Control 58(6):1247–1263. https://doi.org/10.1080/0020717930892305 -- [10.1080/00207179308923053](https://doi.org/10.1080/00207179308923053)
- Levant A (2003) Higher-order sliding modes, differentiation and output-feedback control. International Journal of Control 76(9–10):924–941. https://doi.org/10.1080/002071703100009902 -- [10.1080/0020717031000099029](https://doi.org/10.1080/0020717031000099029)
- Shtessel Y, Edwards C, Fridman L, Levant A (2014) Sliding Mode Control and Observation. Springer New Yor -- [10.1007/978-0-8176-4893-0](https://doi.org/10.1007/978-0-8176-4893-0)
- Moreno JA, Osorio M (2012) Strict Lyapunov Functions for the Super-Twisting Algorithm. IEEE Trans Automat Contr 57(4):1035–1040. https://doi.org/10.1109/tac.2012.218617 -- [10.1109/tac.2012.2186179](https://doi.org/10.1109/tac.2012.2186179)
- Levant A (2010) Chattering Analysis. IEEE Trans Automat Contr 55(6):1380–1389. https://doi.org/10.1109/tac.2010.204197 -- [10.1109/tac.2010.2041973](https://doi.org/10.1109/tac.2010.2041973)
- Bartolini G, Ferrara A, Usai E, Utkin VI (2000) On multi-input chattering-free second-order sliding mode control. IEEE Trans Automat Contr 45(9):1711–1717. https://doi.org/10.1109/9.88062 -- [10.1109/9.880629](https://doi.org/10.1109/9.880629)
- Fridman LM (2001) An averaging approach to chattering. IEEE Trans Automat Contr 46(8):1260–1265. https://doi.org/10.1109/9.94093 -- [10.1109/9.940930](https://doi.org/10.1109/9.940930)
- Luo W, Zhao T, Li X, Wang Z, Wu L (2019) Adaptive super‐twisting sliding mode control of three‐phase power rectifiers in active front end applications. IET Control Theory &amp; Appl 13(10):1483–1490. https://doi.org/10.1049/iet-cta.2018.614 -- [10.1049/iet-cta.2018.6141](https://doi.org/10.1049/iet-cta.2018.6141)
- Guerrero JM, Vasquez JC, Matas J, de Vicuna LG, Castilla M (2011) Hierarchical Control of Droop-Controlled AC and DC Microgrids—A General Approach Toward Standardization. IEEE Trans Ind Electron 58(1):158–172. https://doi.org/10.1109/tie.2010.206653 -- [10.1109/tie.2010.2066534](https://doi.org/10.1109/tie.2010.2066534)
- Blaabjerg F, Teodorescu R, Liserre M, Timbus AV (2006) Overview of Control and Grid Synchronization for Distributed Power Generation Systems. IEEE Trans Ind Electron 53(5):1398–1409. https://doi.org/10.1109/tie.2006.88199 -- [10.1109/tie.2006.881997](https://doi.org/10.1109/tie.2006.881997)
- van der Schaft A (2000) L2 - Gain and Passivity Techniques in Nonlinear Control. Springer Londo -- [10.1007/978-1-4471-0507-7](https://doi.org/10.1007/978-1-4471-0507-7)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- (2001) Putting energy back in control. IEEE Control Syst 21(2):18–33. https://doi.org/10.1109/37.91539 -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Ortega R, van der Schaft A, Maschke B, Escobar G (2002) Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38(4):585–596. https://doi.org/10.1016/s0005-1098(01)00278-](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- Ortega, Passivity-Based Control of Euler–Lagrange Systems: Mechanical electrical and electromechanical., Mechanical, Electrical and Electromechanical Applications (2013)
- Yazdani A, Iravani R (2010) Voltage‐Sourced Converters in Power System -- [10.1002/9780470551578](https://doi.org/10.1002/9780470551578)

