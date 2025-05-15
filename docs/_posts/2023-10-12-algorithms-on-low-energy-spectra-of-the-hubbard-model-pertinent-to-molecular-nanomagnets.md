---
layout: post
title: "Algorithms on low energy spectra of the Hubbard model pertinent to molecular nanomagnets"
date: 2023-10-12 00:00:00 +0100
permalink: algorithms-on-low-energy-spectra-of-the-hubbard-model-pertinent-to-molecular-nanomagnets
year: 2024
authors: M. Antkowiak, Ł. Kucharski, R. Lemański, G. Kamieniarz
category: articles
---
 
## Authors
[M. Antkowiak](authors/m-antkowiak), [Ł. Kucharski](authors/l-kucharski), [R. Lemański](authors/r-lemanski), [G. Kamieniarz](authors/g-kamieniarz)
 
## Abstract
Computer supported design of materials with tailored properties is an important part of computational science so that developments of new effective algorithms is a key issue. Molecular magnetism deals with complex objects described by the quantum physics and their simulations come up against the computational constraints. In this work, we consider a numerical version of a recently developed hybrid approach that combines the ab initio DFT method with the exact diagonalization of the microscopic Hubbard model (HM). The latter avoids the prior perturbative framework but increases computing resources needed for solving the eigenvalue problem of the matrix representation of HM. We demonstrate that in the case of the ring‐shape molecular nanomagnets the computational demands can be curbed due to efficient numerical matrix construction algorithms provided. These algorithms pertain both to the calculation of the single nonzero matrix elements and to their localization in the final sparse matrix that is subsequently diagonalized. Their implementation executed on a simple six‐core‐computer system and the Mathematica environment leads to a significant gain in the computing time for the exemplary chromium‐based molecule denoted Cr, running the code sequentially. We claim, referring to the numerical diagonalization of the spin Hamiltonian matrices, that the parallelization flaws related to the high‐level programming approach can be all removed, porting the code to the appropriate HPC environment. A prospective implementation of the code, based on some dedicated and optimized mathematical libraries, will ultimately open a window for further applications of the Hubbard model in molecular magnetism.
 
## Citation
- **Journal:** Concurrency and Computation: Practice and Experience
- **Year:** 2024
- **Volume:** 36
- **Issue:** 4
- **Pages:** 
- **Publisher:** Wiley
- **DOI:** [10.1002/cpe.7931](https://doi.org/10.1002/cpe.7931)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Antkowiak_2023,
  title={{Algorithms on low energy spectra of the Hubbard model pertinent to molecular nanomagnets}},
  volume={36},
  ISSN={1532-0634},
  DOI={10.1002/cpe.7931},
  number={4},
  journal={Concurrency and Computation: Practice and Experience},
  publisher={Wiley},
  author={Antkowiak, M. and Kucharski, Ł. and Lemański, R. and Kamieniarz, G.},
  year={2023}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/algorithms-on-low-energy-spectra-of-the-hubbard-model-pertinent-to-molecular-nanomagnets.bib)
 
## References
- Gatteschi, D., Sessoli, R. & Villain, J. Molecular Nanomagnets. (2006) doi:10.1093/acprof:oso/9780198567530.001.0001 -- [10.1093/acprof:oso/9780198567530.001.0001](https://doi.org/10.1093/acprof:oso/9780198567530.001.0001)
- Furrer, A. & Waldmann, O. Magnetic cluster excitations. Rev. Mod. Phys. 85, 367–420 (2013) -- [10.1103/revmodphys.85.367](https://doi.org/10.1103/revmodphys.85.367)
- Molecular Nanomagnets and Related Phenomena. Structure and Bonding (Springer Berlin Heidelberg, 2015). doi:10.1007/978-3-662-45723-8 -- [10.1007/978-3-662-45723-8](https://doi.org/10.1007/978-3-662-45723-8)
- Baker, M. L. et al. Spin dynamics of molecular nanomagnets unravelled at atomic scale by four-dimensional inelastic neutron scattering. Nature Phys 8, 906–911 (2012) -- [10.1038/nphys2431](https://doi.org/10.1038/nphys2431)
- Bellini, V. & Affronte, M. A Density-Functional Study of Heterometallic Cr-Based Molecular Rings. J. Phys. Chem. B 114, 14797–14806 (2010) -- [10.1021/jp107544z](https://doi.org/10.1021/jp107544z)
- Baker, M. L. et al. A classification of spin frustration in molecular magnets from a physical study of large odd-numbered-metal, odd electron rings. Proc. Natl. Acad. Sci. U.S.A. 109, 19113–19118 (2012) -- [10.1073/pnas.1213127109](https://doi.org/10.1073/pnas.1213127109)
- Antkowiak, M. et al. Detection of ground states in frustrated molecular rings by in-field local magnetization profiles. Phys. Rev. B 87, (2013) -- [10.1103/physrevb.87.184430](https://doi.org/10.1103/physrevb.87.184430)
- Chiesa, A., Carretta, S., Santini, P., Amoretti, G. & Pavarini, E. Many-Body Models for Molecular Nanomagnets. Phys. Rev. Lett. 110, (2013) -- [10.1103/physrevlett.110.157204](https://doi.org/10.1103/physrevlett.110.157204)
- Brzostowski, B., Lemański, R., Ślusarski, T., Tomecka, D. & Kamieniarz, G. Chromium-based rings within the DFT and Falicov–Kimball model approach. J Nanopart Res 15, (2013) -- [10.1007/s11051-013-1528-2](https://doi.org/10.1007/s11051-013-1528-2)
- Brzostowski, B. et al. DFT and Falicov-Kimball Model Approach to Cr_{9} Molecular Ring. Acta Phys. Pol. A 126, 270–271 (2014) -- [10.12693/aphyspola.126.270](https://doi.org/10.12693/aphyspola.126.270)
- Tomecka, D. M. et al. Ab initiostudy on a chain model of the<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline"><mml:mrow><mml:msub><mml:mrow><mml:mtext>Cr</mml:mtext></mml:mrow><mml:mn>8</mml:mn></mml:msub></mml:mrow></mml:math>molecular magnet. Phys. Rev. B 77, (2008) -- [10.1103/physrevb.77.224401](https://doi.org/10.1103/physrevb.77.224401)
- Cao, C., Hill, S. & Cheng, H.-P. Strongly Correlated Electrons in the<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline"><mml:mo stretchy="false">[</mml:mo><mml:mi>Ni</mml:mi><mml:mo stretchy="false">(</mml:mo><mml:mi>hmp</mml:mi><mml:mo stretchy="false">)</mml:mo><mml:mo stretchy="false">(</mml:mo><mml:mi>R</mml:mi><mml:mi>OH</mml:mi><mml:mo stretchy="false">)</mml:mo><mml:mi mathvariant="normal">X</mml:mi><mml:msub><mml:mo stretchy="false">]</mml:mo><mml:mn>4</mml:mn></mml:msub></mml:math>Single Molecule Magnet: A<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline"><mml:mi>DFT</mml:mi><mml:mo>+</mml:mo><mml:mi>U</mml:mi></mml:math>Study. Phys. Rev. Lett. 100, (2008) -- [10.1103/physrevlett.100.167206](https://doi.org/10.1103/physrevlett.100.167206)
- Himmetoglu, B., Floris, A., de Gironcoli, S. & Cococcioni, M. Hubbard-corrected DFT energy functionals: The LDA+U description of correlated systems. Int. J. Quantum Chem. 114, 14–49 (2013) -- [10.1002/qua.24521](https://doi.org/10.1002/qua.24521)
- Chiesa, A., Carretta, S., Santini, P., Amoretti, G. & Pavarini, E. Many-bodyab initiostudy of antiferromagnetic<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:mo>{</mml:mo><mml:msub><mml:mi mathvariant="bold">Cr</mml:mi><mml:mn>7</mml:mn></mml:msub><mml:mi>M</mml:mi><mml:mo>}</mml:mo></mml:mrow></mml:math>molecular rings. Phys. Rev. B 94, (2016) -- [10.1103/physrevb.94.224422](https://doi.org/10.1103/physrevb.94.224422)
- Weissman, S., Antkowiak, M., Brzostowski, B., Kamieniarz, G. & Kronik, L. Accurate Magnetic Couplings in Chromium-Based Molecular Rings from Broken-Symmetry Calculations within Density Functional Theory. J. Chem. Theory Comput. 15, 4885–4895 (2019) -- [10.1021/acs.jctc.9b00459](https://doi.org/10.1021/acs.jctc.9b00459)
- Held, K. et al. Realistic investigations of correlated electron systems with LDA + DMFT. Physica Status Solidi (b) 243, 2599–2631 (2006) -- [10.1002/pssb.200642053](https://doi.org/10.1002/pssb.200642053)
- Matysiak, J. & Lemański, R. Description of molecular nanomagnets by the multiorbital Hubbard model with correlated hopping. Phys. Rev. B 104, (2021) -- [10.1103/physrevb.104.014431](https://doi.org/10.1103/physrevb.104.014431)
- Lemański, R. & Antkowiak, M. Description of Magnetic Nanomolecules by the Extended Multi-orbital Hubbard Model: Perturbative vs Numerical Approach. Lecture Notes in Computer Science 382–391 (2023) doi:10.1007/978-3-031-30445-3_32 -- [10.1007/978-3-031-30445-3_32](https://doi.org/10.1007/978-3-031-30445-3_32)
- Oleś, A. M. Antiferromagnetism and correlation of electrons in transition metals. Phys. Rev. B 28, 327–339 (1983) -- [10.1103/physrevb.28.327](https://doi.org/10.1103/physrevb.28.327)
- Frésard, R. & Kotliar, G. Interplay of Mott transition and ferromagnetism in the orbitally degenerate Hubbard model. Phys. Rev. B 56, 12909–12915 (1997) -- [10.1103/physrevb.56.12909](https://doi.org/10.1103/physrevb.56.12909)
- Lieb E, Two soluble models of an antiferromagnetic chain. Ann Phys Rehabil Med (1961)
- Lieb, E. & Mattis, D. Ordering Energy Levels of Interacting Spin Systems. Journal of Mathematical Physics 3, 749–751 (1962) -- [10.1063/1.1724276](https://doi.org/10.1063/1.1724276)
- Kamieniarz, G., Florek, W. & Antkowiak, M. Universal sequence of ground states validating the classification of frustration in antiferromagnetic rings with a single bond defect. Phys. Rev. B 92, (2015) -- [10.1103/physrevb.92.140411](https://doi.org/10.1103/physrevb.92.140411)
- Florek, W., Antkowiak, M. & Kamieniarz, G. Sequences of ground states and classification of frustration in odd-numbered antiferromagnetic rings. Phys. Rev. B 94, (2016) -- [10.1103/physrevb.94.224421](https://doi.org/10.1103/physrevb.94.224421)
- Ristov, S., Prodan, R., Gusev, M. & Skala, K. Superlinear Speedup in HPC Systems: why and when? Annals of Computer Science and Information Systems vol. 8 889–898 (2016) -- [10.15439/2016f498](https://doi.org/10.15439/2016f498)
- Kucharski, Ł., Kamieniarz, G., Antkowiak, M. & Drzewiński, A. Single-Ion Anisotropy Estimates for the Rhenium(IV-Based) Molecular Magnets: Modeling and Simulations Studies. J. Phys. Soc. Jpn. 83, 064702 (2014) -- [10.7566/jpsj.83.064702](https://doi.org/10.7566/jpsj.83.064702)
- Antkowiak, M., Kucharski, Ł. & Kamieniarz, G. Genetic Algorithm and Exact Diagonalization Approach for Molecular Nanomagnets Modelling. Lecture Notes in Computer Science 312–320 (2016) doi:10.1007/978-3-319-32152-3_29 -- [10.1007/978-3-319-32152-3_29](https://doi.org/10.1007/978-3-319-32152-3_29)
- Kamieniarz, G., Matysiak, R., Gegenwart, P., Ochiai, A. & Steglich, F. Bose glass behavior in<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mo>(</mml:mo><mml:mrow><mml:msub><mml:mi>Yb</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Lu</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mrow><mml:mo>)</mml:mo></mml:mrow><mml:mn>4</mml:mn></mml:msub><mml:msub><mml:mi>As</mml:mi><mml:mn>3</mml:mn></mml:msub></mml:mrow></mml:math>representing randomly diluted quantum spin-<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mfrac><mml:mn>1</mml:mn><mml:mn>2</mml:mn></mml:mfrac></mml:math>chains. Phys. Rev. B 94, (2016) -- [10.1103/physrevb.94.100403](https://doi.org/10.1103/physrevb.94.100403)
- Antkowiak, M., Kucharski, Ł. & Haglauer, M. clique: A Parallel Tool for the Molecular Nanomagnets Simulation and Modelling. Lecture Notes in Computer Science 312–322 (2020) doi:10.1007/978-3-030-43222-5_27 -- [10.1007/978-3-030-43222-5_27](https://doi.org/10.1007/978-3-030-43222-5_27)
- Matysiak, R. et al. Specific heat of segmented Heisenberg quantum spin chains in (Yb<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:msub><mml:mrow/><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:math>Lu<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:msub><mml:mrow/><mml:mi>x</mml:mi></mml:msub></mml:math>)<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:msub><mml:mrow/><mml:mn>4</mml:mn></mml:msub></mml:math>As<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:msub><mml:mrow/><mml:mn>3</mml:mn></mml:msub></mml:math>. Phys. Rev. B 88, (2013) -- [10.1103/physrevb.88.224414](https://doi.org/10.1103/physrevb.88.224414)
- Novoa, J. J., Deumal, M. & Jornet-Somoza, J. Calculation of microscopic exchange interactions and modelling of macroscopic magnetic properties in molecule-based magnets. Chem. Soc. Rev. 40, 3182 (2011) -- [10.1039/c0cs00112k](https://doi.org/10.1039/c0cs00112k)
- Atanasov, M., Ganyushin, D., Pantazis, D. A., Sivalingam, K. & Neese, F. Detailed Ab Initio First-Principles Study of the Magnetic Anisotropy in a Family of Trigonal Pyramidal Iron(II) Pyrrolide Complexes. Inorg. Chem. 50, 7460–7477 (2011) -- [10.1021/ic200196k](https://doi.org/10.1021/ic200196k)
- Zadrozny, J. M. et al. Magnetic blocking in a linear iron(I) complex. Nature Chem 5, 577–581 (2013) -- [10.1038/nchem.1630](https://doi.org/10.1038/nchem.1630)
- Bunting, P. C. et al. A linear cobalt(II) complex with maximal orbital angular momentum from a non-Aufbau ground state. Science 362, (2018) -- [10.1126/science.aat7319](https://doi.org/10.1126/science.aat7319)

