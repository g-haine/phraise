---
title: "A fast and accurate sampler built on Bayesian inference and optimized Hamiltonian Monte Carlo for voltage sag assessment in power systems"
date: 2023-06-12 00:00:00 +0100
permalink: a-fast-and-accurate-sampler-built-on-bayesian-inference-and-optimized-hamiltonian-monte-carlo-for-voltage-sag-assessment-in-power-systems
year: 2023
authors: Diogo J.F. Reis, José Eduardo O. Pessanha
category: articles
tags:
  - Gibbs
  - Hamiltonian Monte Carlo
  - Importance Sampling
  - Metropolis-Hastings
  - SARFI-X
  - Voltage sag
---
 
## Authors
[Diogo J.F. Reis](authors/diogo-j-f-reis), [José Eduardo O. Pessanha](authors/jose-eduardo-o-pessanha)
 
## Abstract
Sampling is recognized as one of the most time-consuming parts of Monte Carlo Simulations (MCS), especially for high-dimensional complex distributions. Therefore, efforts have been made on developing new techniques, or modifying existing ones to improve efficiency and accuracy of the simulations. There are sampling methods that have been explored by the power engineering community for many years, such as Importance Sampling (a Monte Carlo approximation), Metropolis-Hastings and Gibbs. On the other hand, a powerful method referred to as Hamiltonian Monte Carlo (HMC) has been successfully explored in different areas of science, but very little in power systems. This paper intends to further disseminate the qualities of HMC to the power systems community through a new HMC version for voltage sags studies, comprising a coefficient of variation for efficiency purposes and an optimization strategy to avoid manual fine-tuning of the integrator stepsize (usually a time-consuming task). It is verified through numerical experiments with small and large-port power systems that the average performance of the proposed algorithm is superior to other existing techniques for the problem of interest.
 
## Keywords
Gibbs; Hamiltonian Monte Carlo; Importance Sampling; Metropolis-Hastings; SARFI-X; Voltage sag
 
## Citation
- **Journal:** International Journal of Electrical Power &amp; Energy Systems
- **Year:** 2023
- **Volume:** 153
- **Issue:** 
- **Pages:** 109297
- **Publisher:** Elsevier BV
- **DOI:** [10.1016/j.ijepes.2023.109297](https://doi.org/10.1016/j.ijepes.2023.109297)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Reis_2023,
  title={{A fast and accurate sampler built on Bayesian inference and optimized Hamiltonian Monte Carlo for voltage sag assessment in power systems}},
  volume={153},
  ISSN={0142-0615},
  DOI={10.1016/j.ijepes.2023.109297},
  journal={International Journal of Electrical Power &amp; Energy Systems},
  publisher={Elsevier BV},
  author={Reis, Diogo J.F. and Pessanha, José Eduardo O.},
  year={2023},
  pages={109297}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/a-fast-and-accurate-sampler-built-on-bayesian-inference-and-optimized-hamiltonian-monte-carlo-for-voltage-sag-assessment-in-power-systems.bib)
 
## References
- Billinton, R. & Tang, X. Selected considerations in utilizing Monte Carlo simulation in quantitative reliability evaluation of composite power systems. Electric Power Systems Research 69, 205–211 (2004) -- [10.1016/j.epsr.2003.08.012](https://doi.org/10.1016/j.epsr.2003.08.012)
- Canizes, Hybrid fuzzy Monte Carlo technique for reliability assessment in transmission power systems. Energy (2012)
- Krupenev, Improvement in the computational efficiency of a technique for assessing the reliability of electric power systems based on the Monte Carlo method. Reliab Eng Syst (2020)
- Salgado Duarte, Y., Szpytko, J. & del Castillo Serpa, A. M. Monte Carlo simulation model to coordinate the preventive maintenance scheduling of generating units in isolated distributed Power Systems. Electric Power Systems Research 182, 106237 (2020) -- [10.1016/j.epsr.2020.106237](https://doi.org/10.1016/j.epsr.2020.106237)
- Billinton, R. & Li, W. Introduction. Reliability Assessment of Electric Power Systems Using Monte Carlo Methods 1–7 (1994) doi:10.1007/978-1-4899-1346-3_1 -- [10.1007/978-1-4899-1346-3_1](https://doi.org/10.1007/978-1-4899-1346-3_1)
- Tokdar, S. T. & Kass, R. E. Importance sampling: a review. WIREs Computational Stats 2, 54–60 (2009) -- [10.1002/wics.56](https://doi.org/10.1002/wics.56)
- Agapiou, S., Papaspiliopoulos, O., Sanz-Alonso, D. & Stuart, A. M. Importance Sampling: Intrinsic Dimension and Computational Cost. Statist. Sci. 32, (2017) -- [10.1214/17-sts611](https://doi.org/10.1214/17-sts611)
- Robert, C. P. Th            <scp>M</scp            etropolis            <scp>H</scp            astings Algorithm. Wiley StatsRef: Statistics Reference Online 1–15 (2015) doi:10.1002/9781118445112.stat07834 -- [10.1002/9781118445112.stat07834](https://doi.org/10.1002/9781118445112.stat07834)
- Chib, S. & Greenberg, E. Understanding the Metropolis-Hastings Algorithm. The American Statistician 49, 327–335 (1995) -- [10.1080/00031305.1995.10476177](https://doi.org/10.1080/00031305.1995.10476177)
- Rubinstein, (2007)
- Bremaud, (1999)
- Duane, S., Kennedy, A. D., Pendleton, B. J. & Roweth, D. Hybrid Monte Carlo. Physics Letters B 195, 216–222 (1987) -- [10.1016/0370-2693(87)91197-x](https://doi.org/10.1016/0370-2693(87)91197-x)
- Betancourt, A Conceptual Introduction to Hamiltonian Monte Carlo. Retrieved July 22 (2021)
- Neal, R. M. MCMC Using Hamiltonian Dynamics. Handbook of Markov Chain Monte Carlo 113–162 (2011) doi:10.1201/b10905-6 -- [10.1201/b10905-6](https://doi.org/10.1201/b10905-6)
- Reis, Implementing the Hamiltonian Monte Carlo sampling algorithm in stochastic assessment of power systems. JCAE (2022)
- Yu, D. C., Nguyen, T. C. & Haddawy, P. Bayesian network model for reliability assessment of power systems. IEEE Trans. Power Syst. 14, 426–432 (1999) -- [10.1109/59.761860](https://doi.org/10.1109/59.761860)
- Zuluaga, C. D. & Alvarez, M. A. Bayesian Probabilistic Power Flow Analysis Using Jacobian Approximate Bayesian Computation. IEEE Trans. Power Syst. 33, 5217–5225 (2018) -- [10.1109/tpwrs.2018.2810641](https://doi.org/10.1109/tpwrs.2018.2810641)
- Nagi, R., Huan, X. & Chen, Y. C. Bayesian Inference of Parameters in Power System Dynamic Models Using Trajectory Sensitivities. IEEE Trans. Power Syst. 37, 1253–1263 (2022) -- [10.1109/tpwrs.2021.3104536](https://doi.org/10.1109/tpwrs.2021.3104536)
- Radivojević, T. & Akhmatskaya, E. Modified Hamiltonian Monte Carlo for Bayesian inference. Stat Comput 30, 377–404 (2019) -- [10.1007/s11222-019-09885-x](https://doi.org/10.1007/s11222-019-09885-x)
- Beskos, A., Pillai, N., Roberts, G., Sanz-Serna, J.-M. & Stuart, A. Optimal tuning of the hybrid Monte Carlo algorithm. Bernoulli 19, (2013) -- [10.3150/12-bej414](https://doi.org/10.3150/12-bej414)
- Bollen, (1999)
- Oliphant, A Bayesian perspective on estimating mean, variance, and standard-deviation from data. All Faculty Publications (2006)
- Leite da Silva, A. M. & de Castro, A. M. Risk Assessment in Probabilistic Load Flow via Monte Carlo Simulation and Cross-Entropy Method. IEEE Trans. Power Syst. 34, 1193–1202 (2019) -- [10.1109/tpwrs.2018.2869769](https://doi.org/10.1109/tpwrs.2018.2869769)
- Perninge, M., Lindskog, F. & Soder, L. Importance Sampling of Injected Powers for Electric Power System Security Analysis. IEEE Trans. Power Syst. 27, 3–11 (2012) -- [10.1109/tpwrs.2011.2162654](https://doi.org/10.1109/tpwrs.2011.2162654)
- Huang, J., Xue, Y., Dong, Z. Y. & Wong, K. P. An adaptive importance sampling method for probabilistic optimal power flow. 2011 IEEE Power and Energy Society General Meeting 1–6 (2011) doi:10.1109/pes.2011.6039167 -- [10.1109/pes.2011.6039167](https://doi.org/10.1109/pes.2011.6039167)
- Xia, M., Sun, J. & Chen, Q. Outlier Reconstruction Based Distribution System State Estimation Using Equivalent Model of Long Short-term Memory and Metropolis-Hastings Sampling. Journal of Modern Power Systems and Clean Energy 10, 1625–1636 (2022) -- [10.35833/mpce.2020.000932](https://doi.org/10.35833/mpce.2020.000932)
- Xu, Y. et al. Response-Surface-Based Bayesian Inference for Power System Dynamic Parameter Estimation. IEEE Trans. Smart Grid 10, 5899–5909 (2019) -- [10.1109/tsg.2019.2892464](https://doi.org/10.1109/tsg.2019.2892464)
- Wang, Y. An Enhanced Markov Chain Monte Carlo-Integrated Cross-Entropy Method with a Partially Collapsed Gibbs Sampler for Probabilistic Spinning Reserve Adequacy Evaluation of Generating Systems. Electric Power Components and Systems 45, 1617–1628 (2017) -- [10.1080/15325008.2017.1404660](https://doi.org/10.1080/15325008.2017.1404660)
- Yun, S.-Y. & Kim, J.-C. An evaluation method of voltage sag using a risk assessment model in power distribution systems. International Journal of Electrical Power &amp; Energy Systems 25, 829–839 (2003) -- [10.1016/s0142-0615(03)00063-2](https://doi.org/10.1016/s0142-0615(03)00063-2)
- dos Santos, A. & Correia de Barros, M. T. Voltage sag prediction for network planning. Electric Power Systems Research 140, 976–983 (2016) -- [10.1016/j.epsr.2016.03.033](https://doi.org/10.1016/j.epsr.2016.03.033)
- Bordalo, U. A., Rodrigues, A. B. & DaSilva, M. G. A New Methodology for Probabilistic Short-Circuit Evaluation With Applications in Power Quality Analysis. IEEE Trans. Power Syst. 21, 474–479 (2006) -- [10.1109/tpwrs.2006.873055](https://doi.org/10.1109/tpwrs.2006.873055)
- Olguin, G., Karlsson, D. & Leborgne, R. Stochastic assessment of voltage dips (Sags): The method of fault positions versus a Monte Carlo simulation approach. 2005 IEEE Russia Power Tech 1–7 (2005) doi:10.1109/ptc.2005.4524564 -- [10.1109/ptc.2005.4524564](https://doi.org/10.1109/ptc.2005.4524564)
- Moschakis, M. N. & Hatziargyriou, N. D. Analytical Calculation and Stochastic Assessment of Voltage Sags. IEEE Trans. Power Delivery 21, 1727–1734 (2006) -- [10.1109/tpwrd.2006.874108](https://doi.org/10.1109/tpwrd.2006.874108)
- Ribeiro Baptista, J. E., Rodrigues, A. B. & da Silva, M. da G. Two probabilistic methods for voltage sag estimation in distribution systems. 2016 Power Systems Computation Conference (PSCC) 1–7 (2016) doi:10.1109/pscc.2016.7540905 -- [10.1109/pscc.2016.7540905](https://doi.org/10.1109/pscc.2016.7540905)
- Aly, E.-E. A. A. & Öztürk, A. Hodges—Lehmann quantile-quantile plots. Computational Statistics &amp; Data Analysis 6, 99–108 (1988) -- [10.1016/0167-9473(88)90040-0](https://doi.org/10.1016/0167-9473(88)90040-0)
- Fichtner, A tutorial introduction to the Hamiltonian Monte Carlo solution of weakly nonlinear inverse problems. California Digital Library (CDL) (2018)
- Flegal, J. M. & Jones, G. L. Batch means and spectral variance estimators in Markov chain Monte Carlo. Ann. Statist. 38, (2010) -- [10.1214/09-aos735](https://doi.org/10.1214/09-aos735)
- Santos, A. dos, Rosa, T. & Correia de Barros, M. T. Stochastic Characterization of Voltage Sag Occurrence Based on Field Data. IEEE Trans. Power Delivery 34, 496–504 (2019) -- [10.1109/tpwrd.2018.2878997](https://doi.org/10.1109/tpwrd.2018.2878997)
- Girolami, M. & Calderhead, B. Riemann Manifold Langevin and Hamiltonian Monte Carlo Methods. Journal of the Royal Statistical Society Series B: Statistical Methodology 73, 123–214 (2011) -- [10.1111/j.1467-9868.2010.00765.x](https://doi.org/10.1111/j.1467-9868.2010.00765.x)
- Betancourt, M. & Girolami, M. Hamiltonian Monte Carlo for Hierarchical Models. Current Trends in Bayesian Methodology with Applications 79–101 (2015) doi:10.1201/b18502-5 -- [10.1201/b18502-5](https://doi.org/10.1201/b18502-5)

