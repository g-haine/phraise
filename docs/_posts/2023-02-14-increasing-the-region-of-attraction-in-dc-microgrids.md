---
title: "Increasing the region of attraction in DC microgrids"
date: 2023-02-14 00:00:00 +0100
permalink: increasing-the-region-of-attraction-in-dc-microgrids
year: 2023
authors: Joel Ferguson, Michele Cucuzzella, Jacquelien M.A. Scherpen
category: articles
tags:
  - Power systems stability
  - Decentralised and distributed control
  - Input-to-state stability
  - Disturbance rejection
  - Lagrangian and hamiltonian systems
  - Passivity-based control
---
 
## Authors
[Joel Ferguson](authors/joel-ferguson), [Michele Cucuzzella](authors/michele-cucuzzella), [Jacquelien M.A. Scherpen](authors/jacquelien-m-a-scherpen)
 
## Abstract
Based on the port-Hamiltonian framework, this paper proposes a novel control scheme for stabilising the voltage in DC networks affected by (i) unknown ZIP-loads, i.e., nonlinear loads consisting of the parallel combination of constant impedance (Z), current (I) and power (P) load types, and (ii) unknown (but bounded) time-varying disturbances. Differently from the results existing in the literature, where restrictive (sufficient) conditions on the load parameters, voltage trajectory and voltage reference are assumed to be satisfied, this is the first paper (to the best of our knowledge) proposing a controller that relaxes such conditions and guarantees the exponential stability of the desired equilibrium point, whose region of attraction can be increased by simply tuning the control gains. In the case the network is affected by unknown time-varying disturbances, local input-to-state stability (l-ISS) is ensured. Furthermore, if non-ideal P-loads are considered, excluding the unrealistic possibility that the load absorbs infinite current when the voltage approaches zero, the aforementioned stability results hold globally.
 
## Keywords
Power systems stability; Decentralised and distributed control; Input-to-state stability; Disturbance rejection; Lagrangian and hamiltonian systems; Passivity-based control
 
## Citation
- **Journal:** Automatica
- **Year:** 2023
- **Volume:** 151
- **Issue:** 
- **Pages:** 110883
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.automatica.2023.110883](https://doi.org/10.1016/j.automatica.2023.110883)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Ferguson_2023,
  title={{Increasing the region of attraction in DC microgrids}},
  volume={151},
  ISSN={0005-1098},
  DOI={10.1016/j.automatica.2023.110883},
  journal={Automatica},
  publisher={Elsevier BV},
  author={Ferguson, Joel and Cucuzzella, Michele and Scherpen, Jacquelien M.A.},
  year={2023},
  pages={110883}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/increasing-the-region-of-attraction-in-dc-microgrids.bib)
 
## References
- AL-Nussairi, M. Kh., Bayindir, R., Padmanaban, S., Mihet-Popa, L. & Siano, P. Constant Power Loads (CPL) with Microgrids: Problem Definition, Stability Analysis and Compensation Techniques. Energies vol. 10 1656 (2017) -- [10.3390/en10101656](https://doi.org/10.3390/en10101656)
- Cucuzzella, M., Kosaraju, K. C. & Scherpen, J. M. A. Voltage Control of DC Microgrids: Robustness for Unknown ZIP-Loads. IEEE Control Systems Letters vol. 7 139–144 (2023) -- [10.1109/lcsys.2022.3187925](https://doi.org/10.1109/lcsys.2022.3187925)
- Cucuzzella, M. et al. A Robust Consensus Algorithm for Current Sharing and Voltage Regulation in DC Microgrids. IEEE Transactions on Control Systems Technology vol. 27 1583–1595 (2019) -- [10.1109/tcst.2018.2834878](https://doi.org/10.1109/tcst.2018.2834878)
- Dashkovskiy, S. N. & Rüffer, B. S. Local ISS of large-scale interconnections and estimates for stability regions. Systems &amp; Control Letters vol. 59 241–247 (2010) -- [10.1016/j.sysconle.2010.02.001](https://doi.org/10.1016/j.sysconle.2010.02.001)
- De Persis, C., Weitenberg, E. R. A. & Dörfler, F. A power consensus algorithm for DC microgrids. Automatica vol. 89 364–375 (2018) -- [10.1016/j.automatica.2017.12.026](https://doi.org/10.1016/j.automatica.2017.12.026)
- Dragičević, DC microgrids–Part I: A review of control strategies and stabilization techniques. IEEE Transactions on Power Electronics (2016)
- [Ferguson, J., Cucuzzella, M. & Scherpen, J. M. A. Exponential Stability and Local ISS for DC Networks. IEEE Control Systems Letters vol. 5 893–898 (2021)](exponential-stability-and-local-iss-for-dc-networks) -- [10.1109/lcsys.2020.3007222](https://doi.org/10.1109/lcsys.2020.3007222)
- [Ferguson, J., Donaire, A. & Middleton, R. H. Integral Control of Port-Hamiltonian Systems: Nonpassive Outputs Without Coordinate Transformation. IEEE Transactions on Automatic Control vol. 62 5947–5953 (2017)](integral-control-of-port-hamiltonian-systems-nonpassive-outputs-without-coordinate-transformation) -- [10.1109/tac.2017.2700995](https://doi.org/10.1109/tac.2017.2700995)
- [Ferguson, J., Donaire, A., Ortega, R. & Middleton, R. H. Robust integral action of port-Hamiltonian systems. IFAC-PapersOnLine vol. 51 181–186 (2018)](robust-integral-action-of-port-hamiltonian-systems) -- [10.1016/j.ifacol.2018.06.050](https://doi.org/10.1016/j.ifacol.2018.06.050)
- Jeeninga, (2020)
- Jusoh, The instability effect of constant power loads. (2004)
- Khalil, (2002)
- Kosaraju, K. C., Cucuzzella, M., Scherpen, J. M. A. & Pasumarthy, R. Differentiation and Passivity for Control of Brayton–Moser Systems. IEEE Transactions on Automatic Control vol. 66 1087–1101 (2021) -- [10.1109/tac.2020.2994317](https://doi.org/10.1109/tac.2020.2994317)
- Machado, An adaptive observer-based controller design for active damping of a DC network with a constant power load. IEEE Transactions on Control Systems Technology (2020)
- Meng, Review on Control of DC Microgrids and Multiple Microgrid Clusters. IEEE Journal of Emerging and Selected Topics in Power Electronics (2017)
- [Monshizadeh, P., Machado, J. E., Ortega, R. & van der Schaft, A. Power-controlled Hamiltonian systems: Application to electrical systems with constant power loads. Automatica vol. 109 108527 (2019)](power-controlled-hamiltonian-systems-application-to-electrical-systems-with-constant-power-loads) -- [10.1016/j.automatica.2019.108527](https://doi.org/10.1016/j.automatica.2019.108527)
- Nahata, P., Soloperto, R., Tucci, M., Martinelli, A. & Ferrari-Trecate, G. A passivity-based approach to voltage stabilization in DC microgrids with ZIP loads. Automatica vol. 113 108770 (2020) -- [10.1016/j.automatica.2019.108770](https://doi.org/10.1016/j.automatica.2019.108770)
- Sadabadi, M. S., Shafiee, Q. & Karimi, A. Plug-and-Play Robust Voltage Control of DC Microgrids. IEEE Transactions on Smart Grid vol. 9 6886–6896 (2018) -- [10.1109/tsg.2017.2728319](https://doi.org/10.1109/tsg.2017.2728319)
- Silani, A., Cucuzzella, M., Scherpen, J. M. A. & Yazdanpanah, M. J. Robust output regulation for voltage control in DC networks with time-varying loads. Automatica vol. 135 109997 (2022) -- [10.1016/j.automatica.2021.109997](https://doi.org/10.1016/j.automatica.2021.109997)
- Singh, S., Gautam, A. R. & Fulwani, D. Constant power loads and their effects in DC distributed power systems: A review. Renewable and Sustainable Energy Reviews vol. 72 407–421 (2017) -- [10.1016/j.rser.2017.01.027](https://doi.org/10.1016/j.rser.2017.01.027)
- Sontag, E. D. & Yuan Wang. New characterizations of input-to-state stability. IEEE Transactions on Automatic Control vol. 41 1283–1294 (1996) -- [10.1109/9.536498](https://doi.org/10.1109/9.536498)
- Strehle, A scalable port-Hamiltonian approach to plug-and-play voltage stabilization in DC microgrids. (2020)
- Tucci, M., Riverso, S. & Ferrari-Trecate, G. Line-Independent Plug-and-Play Controllers for Voltage Stabilization in DC Microgrids. IEEE Transactions on Control Systems Technology vol. 26 1115–1123 (2018) -- [10.1109/tcst.2017.2695167](https://doi.org/10.1109/tcst.2017.2695167)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control vol. 1 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Zhao, J. & Dörfler, F. Distributed control and optimization in DC microgrids. Automatica vol. 61 18–26 (2015) -- [10.1016/j.automatica.2015.07.015](https://doi.org/10.1016/j.automatica.2015.07.015)

