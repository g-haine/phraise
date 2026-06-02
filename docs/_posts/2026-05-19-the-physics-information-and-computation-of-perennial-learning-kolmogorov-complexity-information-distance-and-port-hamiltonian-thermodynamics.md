---
title: "The Physics, Information, and Computation of Perennial Learning: Kolmogorov Complexity, Information Distance, and Port-Hamiltonian Thermodynamics"
date: 2026-05-19 00:00:00 +0100
permalink: the-physics-information-and-computation-of-perennial-learning-kolmogorov-complexity-information-distance-and-port-hamiltonian-thermodynamics
year: 2026
authors: Chandrajit Bajaj
category: articles
---
 
## Authors
[Chandrajit Bajaj](authors/chandrajit-bajaj)
 
## Abstract
Real-world autonomous agents learn under nonstationarity, safety constraints, and finite energetic budgets. We develop a framework for perennial learning—agents that continuously refine their models while provably controlling the cost of forgetting—by unifying three classical pillars: Kolmogorov complexity, which equates scientific discovery with algorithmic compression; Landauer’s principle, which assigns a minimal thermodynamic cost of kBTln2 per erased bit to every irreversible model update; and port-Hamiltonian (PH) dynamics, whose (J−R)∇H decomposition separates zero-cost reversible inference from costly irreversible forgetting by construction. The Maxwell demon analogy is formalized: each learning episode is a Szilard cycle in which information acquisition, belief transport, and memory erasure must balance thermodynamically. The information-distance framework, comprising the normalized information distance (NID) and normalized compression distance (NCD), provides a computable geometry for measuring learning progress and guiding curriculum design. We separate theideal uncomputable regularizer based on prefix complexity from the practical compressor/MDL (minimum description length) surrogate that appears in optimization and prove a calibration lemma linking the two under a mild uniform-accuracy assumption. Under explicit regularity, compact-sublevel, and non-energy-extracting assumptions, we prove a passivity speed limit for curriculum-induced contractions of the effective feasible set. Under local asymptotic normality, we reprove that Fisher information is a local posterior codelength proxy rather than an exact theorem about algorithmic entropy. A conditional sequential information-budget proposition shows that the per-stage sample requirement scales as O˜(Δkt/λ⋆), where Δkt is the number of materially changed model coordinates (not the total model complexity kt); the k3→Δk improvement is conditional on a warm-start assumption and a chosen cold-start baseline. A double-integrator running example with a moving obstacle illustrates the architecture.
 
## Citation
- **Journal:** Entropy
- **Year:** 2026
- **Volume:** 28
- **Issue:** 5
- **Pages:** 551
- **Publisher:** MDPI AG
- **DOI:** [10.3390/e28050551](https://doi.org/10.3390/e28050551)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Bajaj_2026,
  title={{The Physics, Information, and Computation of Perennial Learning: Kolmogorov Complexity, Information Distance, and Port-Hamiltonian Thermodynamics}},
  volume={28},
  ISSN={1099-4300},
  DOI={10.3390/e28050551},
  number={5},
  journal={Entropy},
  publisher={MDPI AG},
  author={Bajaj, Chandrajit},
  year={2026},
  pages={551}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/the-physics-information-and-computation-of-perennial-learning-kolmogorov-complexity-information-distance-and-port-hamiltonian-thermodynamics.bib)
 
## References
- Li M, Vitányi P (1995) A New Approach to Formal Language Theory by Kolmogorov Complexity. SIAM J Comput 24(2):398–410. https://doi.org/10.1137/s009753979324485 -- [10.1137/s009753979324485x](https://doi.org/10.1137/s009753979324485x)
- (1996) Reversibility and adiabatic computation: trading time and space for energy. Proc R Soc Lond A 452(1947):769–789. https://doi.org/10.1098/rspa.1996.003 -- [10.1098/rspa.1996.0039](https://doi.org/10.1098/rspa.1996.0039)
- Li M, Chen X, Li X, Ma B, Vitanyi PMB (2004) The Similarity Metric. IEEE Trans Inform Theory 50(12):3250–3264. https://doi.org/10.1109/tit.2004.83810 -- [10.1109/tit.2004.838101](https://doi.org/10.1109/tit.2004.838101)
- Vereshchagin NK, Vitanyi PMB (2004) Kolmogorov’s Structure Functions and Model Selection. IEEE Trans Inform Theory 50(12):3265–3290. https://doi.org/10.1109/tit.2004.83834 -- [10.1109/tit.2004.838346](https://doi.org/10.1109/tit.2004.838346)
- Cilibrasi R, Vitanyi PMB (2005) Clustering by Compression. IEEE Trans Inform Theory 51(4):1523–1545. https://doi.org/10.1109/tit.2005.84405 -- [10.1109/tit.2005.844059](https://doi.org/10.1109/tit.2005.844059)
- Parisi GI, Kemker R, Part JL, Kanan C, Wermter S (2019) Continual lifelong learning with neural networks: A review. Neural Networks 113:54–71. https://doi.org/10.1016/j.neunet.2019.01.01 -- [10.1016/j.neunet.2019.01.012](https://doi.org/10.1016/j.neunet.2019.01.012)
- Thrun S, Mitchell TM (1995) Lifelong robot learning. Robotics and Autonomous Systems 15(1–2):25–46. https://doi.org/10.1016/0921-8890(95)00004- -- [10.1016/0921-8890(95)00004-y](https://doi.org/10.1016/0921-8890(95)00004-y)
- Kirkpatrick J, Pascanu R, Rabinowitz N, Veness J, Desjardins G, Rusu AA, Milan K, Quan J, Ramalho T, Grabska-Barwinska A, Hassabis D, Clopath C, Kumaran D, Hadsell R (2017) Overcoming catastrophic forgetting in neural networks. Proc Natl Acad Sci USA 114(13):3521–3526. https://doi.org/10.1073/pnas.161183511 -- [10.1073/pnas.1611835114](https://doi.org/10.1073/pnas.1611835114)
- Reif JH (1979) Complexity of the mover’s problem and generalizations. 20th Annual Symposium on Foundations of Computer Science (sfcs 1979) 421–42 -- [10.1109/sfcs.1979.10](https://doi.org/10.1109/sfcs.1979.10)
- Canny J, Donald B, Reif J, Xavier P (1988) On the complexity of kinodynamic planning. [Proceedings 1988] 29th Annual Symposium on Foundations of Computer Science 306–31 -- [10.1109/sfcs.1988.21947](https://doi.org/10.1109/sfcs.1988.21947)
- Arnold VI (1989) Mathematical Methods of Classical Mechanics. Springer New Yor -- [10.1007/978-1-4757-2063-1](https://doi.org/10.1007/978-1-4757-2063-1)
- Still S, Sivak DA, Bell AJ, Crooks GE (2012) Thermodynamics of Prediction. Phys Rev Lett 109(12). https://doi.org/10.1103/physrevlett.109.12060 -- [10.1103/physrevlett.109.120604](https://doi.org/10.1103/physrevlett.109.120604)
- Wolpert DH Information Theory ― The Bridge Connecting Bounded Rational Game Theory and Statistical Physics. Understanding Complex Systems 262–29 -- [10.1007/3-540-32834-3_12](https://doi.org/10.1007/3-540-32834-3_12)
- Parrondo JMR, Horowitz JM, Sagawa T (2015) Thermodynamics of information. Nature Phys 11(2):131–139. https://doi.org/10.1038/nphys323 -- [10.1038/nphys3230](https://doi.org/10.1038/nphys3230)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2–3):173–378. https://doi.org/10.1561/260000000](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Todorov E (2009) Efficient computation of optimal actions. Proc Natl Acad Sci USA 106(28):11478–11483. https://doi.org/10.1073/pnas.071074310 -- [10.1073/pnas.0710743106](https://doi.org/10.1073/pnas.0710743106)
- {"status":"error" -- [10.1088/1742-5468/2005/11/p11011](https://doi.org/10.1088/1742-5468/2005/11/p11011)
- Fisac JF, Akametalu AK, Zeilinger MN, Kaynama S, Gillula J, Tomlin CJ (2019) A General Safety Framework for Learning-Based Control in Uncertain Robotic Systems. IEEE Trans Automat Contr 64(7):2737–2752. https://doi.org/10.1109/tac.2018.287638 -- [10.1109/tac.2018.2876389](https://doi.org/10.1109/tac.2018.2876389)
- [Desai SA, Mattheakis M, Sondak D, Protopapas P, Roberts SJ (2021) Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. Phys Rev E 104(3). https://doi.org/10.1103/physreve.104.03431](port-hamiltonian-neural-networks-for-learning-explicit-time-dependent-dynamical-systems) -- [10.1103/physreve.104.034312](https://doi.org/10.1103/physreve.104.034312)
- Bajaj C (1986) Proving geometric algorithm non-solvability: An application of factoring polynomials. Journal of Symbolic Computation 2(1):99–102. https://doi.org/10.1016/s0747-7171(86)80015- -- [10.1016/s0747-7171(86)80015-3](https://doi.org/10.1016/s0747-7171(86)80015-3)
- Bajaj C (1987) Geometric optimization and the polynomial hierarchy. Theoretical Computer Science 54(1):87–102. https://doi.org/10.1016/0304-3975(87)90020- -- [10.1016/0304-3975(87)90020-x](https://doi.org/10.1016/0304-3975(87)90020-x)
- Bajaj C, Li M (1989) Geometric optimization andD P -completeness. Discrete Comput Geom 4(1):3–13. https://doi.org/10.1007/bf0218771 -- [10.1007/bf02187711](https://doi.org/10.1007/bf02187711)
- Li M, Vitányi P (2019) An Introduction to Kolmogorov Complexity and Its Applications. Springer International Publishin -- [10.1007/978-3-030-11298-1](https://doi.org/10.1007/978-3-030-11298-1)
- Conditional Kolmogorov complexity and universal probability. Theor. Comput. Sci. (2013)
- Grünwald PD (2007) The Minimum Description Length Principl -- [10.7551/mitpress/4643.001.0001](https://doi.org/10.7551/mitpress/4643.001.0001)
- Landauer R (1961) Irreversibility and Heat Generation in the Computing Process. IBM J Res &amp; Dev 5(3):183–191. https://doi.org/10.1147/rd.53.018 -- [10.1147/rd.53.0183](https://doi.org/10.1147/rd.53.0183)
- Bennett CH (1982) The thermodynamics of computation—a review. Int J Theor Phys 21(12):905–940. https://doi.org/10.1007/bf0208415 -- [10.1007/bf02084158](https://doi.org/10.1007/bf02084158)
- Fredkin E, Toffoli T (1982) Conservative logic. Int J Theor Phys 21(3–4):219–253. https://doi.org/10.1007/bf0185772 -- [10.1007/bf01857727](https://doi.org/10.1007/bf01857727)
- Boyd AB, Mandal D, Riechers PM, Crutchfield JP (2017) Transient Dissipation and Structural Costs of Physical Information Transduction. Phys Rev Lett 118(22). https://doi.org/10.1103/physrevlett.118.22060 -- [10.1103/physrevlett.118.220602](https://doi.org/10.1103/physrevlett.118.220602)
- Morrison PJ (1986) A paradigm for joined Hamiltonian and dissipative systems. Physica D: Nonlinear Phenomena 18(1–3):410–419. https://doi.org/10.1016/0167-2789(86)90209- -- [10.1016/0167-2789(86)90209-5](https://doi.org/10.1016/0167-2789(86)90209-5)
- Bajaj C (2026) Computer Algebra Meets Hamiltonian Geometry. Maple Trans 6(1). https://doi.org/10.5206/mt.v6i1.2424 -- [10.5206/mt.v6i1.24248](https://doi.org/10.5206/mt.v6i1.24248)
- Li M, M.B. Vitányi P (1992) Inductive reasoning and kolmogorov complexity. Journal of Computer and System Sciences 44(2):343–384. https://doi.org/10.1016/0022-0000(92)90026- -- [10.1016/0022-0000(92)90026-f](https://doi.org/10.1016/0022-0000(92)90026-f)
- Boyd, Thermodynamics of Modularity: Structural Costs Beyond the Landauer Bound. Phys. Rev. X (2018)
- Crutchfield JP (1994) The calculi of emergence: computation, dynamics and induction. Physica D: Nonlinear Phenomena 75(1–3):11–54. https://doi.org/10.1016/0167-2789(94)90273- -- [10.1016/0167-2789(94)90273-9](https://doi.org/10.1016/0167-2789(94)90273-9)
- Szilard L (1929) �ber die Entropieverminderung in einem thermodynamischen System bei Eingriffen intelligenter Wesen. Z Physik 53(11–12):840–856. https://doi.org/10.1007/bf0134128 -- [10.1007/bf01341281](https://doi.org/10.1007/bf01341281)
- Boyd AB, Mandal D, Crutchfield JP (2017) Correlation-powered information engines and the thermodynamics of self-correction. Phys Rev E 95(1). https://doi.org/10.1103/physreve.95.01215 -- [10.1103/physreve.95.012152](https://doi.org/10.1103/physreve.95.012152)
- Lázaro-Camí J-A, Ortega J-P (2008) Stochastic hamiltonian dynamical systems. Reports on Mathematical Physics 61(1):65–122. https://doi.org/10.1016/s0034-4877(08)80003- -- [10.1016/s0034-4877(08)80003-1](https://doi.org/10.1016/s0034-4877(08)80003-1)
- [Cordoni F, Di Persio L, Muradore R (2022) Stochastic Port-Hamiltonian Systems. J Nonlinear Sci 32(6). https://doi.org/10.1007/s00332-022-09853-](stochastic-port-hamiltonian-systems) -- [10.1007/s00332-022-09853-2](https://doi.org/10.1007/s00332-022-09853-2)
- Hsu AS, Chater N, Vitányi P (2013) Language Learning From Positive Evidence, Reconsidered: A Simplicity‐Based Approach. Topics in Cognitive Science 5(1):35–55. https://doi.org/10.1111/tops.1200 -- [10.1111/tops.12005](https://doi.org/10.1111/tops.12005)
- Bajaj C, Nguyen M (2024) Physics-Informed Neural Networks via Stochastic Hamiltonian Dynamics Learning. Lecture Notes in Networks and Systems 182–19 -- [10.1007/978-3-031-66428-1_11](https://doi.org/10.1007/978-3-031-66428-1_11)
- BAEZ J, STAY M (2012) Algorithmic thermodynamics. Math Struct Comp Sci 22(5):771–787. https://doi.org/10.1017/s096012951100052 -- [10.1017/s0960129511000521](https://doi.org/10.1017/s0960129511000521)
- Quispel GRW, McLaren DI (2008) A new class of energy-preserving numerical integration methods. J Phys A: Math Theor 41(4):045206. https://doi.org/10.1088/1751-8113/41/4/04520 -- [10.1088/1751-8113/41/4/045206](https://doi.org/10.1088/1751-8113/41/4/045206)
- Evensen G (2009) Data Assimilation. Springer Berlin Heidelber -- [10.1007/978-3-642-03711-5](https://doi.org/10.1007/978-3-642-03711-5)
- Reich S, Cotter C (2015) Probabilistic Forecasting and Bayesian Data Assimilatio -- [10.1017/cbo9781107706804](https://doi.org/10.1017/cbo9781107706804)
- Bédard CA, Bergeron G (2022) An Algorithmic Approach to Emergence. Entropy 24(7):985. https://doi.org/10.3390/e2407098 -- [10.3390/e24070985](https://doi.org/10.3390/e24070985)

