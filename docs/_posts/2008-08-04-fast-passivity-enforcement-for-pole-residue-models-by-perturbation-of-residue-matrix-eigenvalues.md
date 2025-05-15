---
layout: post
title: "Fast Passivity Enforcement for Pole-Residue Models by Perturbation of Residue Matrix Eigenvalues"
date: 2008-08-04 00:00:00 +0100
permalink: fast-passivity-enforcement-for-pole-residue-models-by-perturbation-of-residue-matrix-eigenvalues
year: 2008
authors: B. Gustavsen
category: articles
---
 
## Authors
[B. Gustavsen](authors/b-gustavsen)
 
## Abstract
Rational models must be passive in order to avoid unstable time domain simulations. This paper introduces a fast approach for passivity enforcement of pole-residue models. This is achieved by perturbing the eigenvalues of the residue matrices, as opposed to the existing approach of perturbing matrix elements. This leads to large savings in computation time with only a small increase of the modeling error. This fast residue perturbation (FRP) approach is merged with the modal perturbation technique, leading to fast modal perturbation (FMP). Usage of FMP over FRP achieves to retain the relative accuracy of the admittance matrix eigenvalues. A complete approach is obtained by combining the passivity enforcement step with passivity assessment via the Hamiltonian matrix eigenvalues and a robust iteration scheme, giving a guaranteed passive model. Application of FMP to a six-port power transformer shows that the approach is able to remove large out-of band passivity violations without corrupting the in-band behavior. This is shown to mitigate an unstable simulation. The approach is also demonstrated for a high-speed interconnect and a transmission line.
 
## Citation
- **Journal:** IEEE Transactions on Power Delivery
- **Year:** 2008
- **Volume:** 23
- **Issue:** 4
- **Pages:** 2278--2285
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **DOI:** [10.1109/tpwrd.2008.919027](https://doi.org/10.1109/tpwrd.2008.919027)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Gustavsen_2008,
  title={{Fast Passivity Enforcement for Pole-Residue Models by Perturbation of Residue Matrix Eigenvalues}},
  volume={23},
  ISSN={1937-4208},
  DOI={10.1109/tpwrd.2008.919027},
  number={4},
  journal={IEEE Transactions on Power Delivery},
  publisher={Institute of Electrical and Electronics Engineers (IEEE)},
  author={Gustavsen, B.},
  year={2008},
  pages={2278--2285}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/fast-passivity-enforcement-for-pole-residue-models-by-perturbation-of-residue-matrix-eigenvalues.bib)
 
## References
- Grivet-Talocia, S. An Adaptive Sampling Technique for Passivity Characterization and Enforcement of Large Interconnect Macromodels. IEEE Trans. Adv. Packag. 30, 226–237 (2007) -- [10.1109/tadvp.2007.895990](https://doi.org/10.1109/tadvp.2007.895990)
- grivet-talocia, fast passivity enforcement for large and sparse macromodels. Proc 13th IEEE Topical Meeting on Electrical Performance of Electronic Packaging (2004)
- Grivet-Talocia, S. Package macromodeling via time-domain vector fitting. IEEE Microw. Wireless Compon. Lett. 13, 472–474 (2003) -- [10.1109/lmwc.2003.819378](https://doi.org/10.1109/lmwc.2003.819378)
- Deschrijver, D., Haegeman, B. & Dhaene, T. Orthonormal Vector Fitting: A Robust Macromodeling Tool for Rational Approximation of Frequency Domain Responses. IEEE Trans. Adv. Packag. 30, 216–225 (2007) -- [10.1109/tadvp.2006.879429](https://doi.org/10.1109/tadvp.2006.879429)
- Gustavsen, B. Improving the Pole Relocating Properties of Vector Fitting. IEEE Trans. Power Delivery 21, 1587–1592 (2006) -- [10.1109/tpwrd.2005.860281](https://doi.org/10.1109/tpwrd.2005.860281)
- Gustavsen, B. & Heitz, C. Rational modeling of multiport systems by modal vector fitting. 2007 IEEE Workshop on Signal Propagation on Interconnects 49–52 (2007) doi:10.1109/spi.2007.4512206 -- [10.1109/spi.2007.4512206](https://doi.org/10.1109/spi.2007.4512206)
- Coelho, C. P., Phillips, J. & Silveira, L. M. A Convex Programming Approach for Generating Guaranteed Passive Approximations to Tabulated Frequency-Data. IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst. 23, 293–301 (2004) -- [10.1109/tcad.2003.822107](https://doi.org/10.1109/tcad.2003.822107)
- Gustavsen, B. & Semlyen, A. Enforcing passivity for admittance matrices approximated by rational functions. IEEE Trans. Power Syst. 16, 97–104 (2001) -- [10.1109/59.910786](https://doi.org/10.1109/59.910786)
- Saraswat, D., Achar, R. & Nakhla, M. Enforcing passivity for rational function based macromodels of tabulated data. Electrical Performance of Electrical Packaging (IEEE Cat. No. 03TH8710) (2003) doi:10.1109/epep.2003.1250053 -- [10.1109/epep.2003.1250053](https://doi.org/10.1109/epep.2003.1250053)
- Gustavsen, B. Passivity Enforcement of Rational Models via Modal Perturbation. IEEE Trans. Power Delivery 23, 768–775 (2008) -- [10.1109/tpwrd.2008.916764](https://doi.org/10.1109/tpwrd.2008.916764)
- Lamecki, A. & Mrozowski, M. Equivalent SPICE Circuits With Guaranteed Passivity From Nonpassive Models. IEEE Trans. Microwave Theory Techn. 55, 526–532 (2007) -- [10.1109/tmtt.2006.890520](https://doi.org/10.1109/tmtt.2006.890520)
- Grivet-Talocia, S. Passivity Enforcement via Perturbation of Hamiltonian Matrices. IEEE Trans. Circuits Syst. I 51, 1755–1769 (2004) -- [10.1109/tcsi.2004.834527](https://doi.org/10.1109/tcsi.2004.834527)
- Maffucci, A., Miano, G. & Villone, F. An enhanced transmission line model for full-wave analysis of interconnects in non-homogeneous dielectrics. Proceedings. 45th Annual IEEE Symposium on Foundations of Computer Science 21–24 doi:10.1109/spi.2004.1408990 -- [10.1109/spi.2004.1408990](https://doi.org/10.1109/spi.2004.1408990)
- Morched, A. S., Ottevangers, J. H. & Marti, L. Multi-port frequency dependent network equivalents for the EMTP. IEEE Trans. Power Delivery 8, 1402–1412 (1993) -- [10.1109/61.252667](https://doi.org/10.1109/61.252667)
- gustavsen, interfacing convolution based linear models to an electromagnetic transients program. Proc Int Conf Power Systems Transients (2007)
- Morched, A., Gustavsen, B. & Tartibi, M. A universal model for accurate calculation of electromagnetic transients on overhead lines and underground cables. IEEE Trans. Power Delivery 14, 1032–1038 (1999) -- [10.1109/61.772350](https://doi.org/10.1109/61.772350)
- Bjerkan, E. & Høidalen, H. K. High frequency FEM-based power transformer modeling: Investigation of internal stresses due to network-initiated overvoltages. Electric Power Systems Research 77, 1483–1489 (2007) -- [10.1016/j.epsr.2006.08.031](https://doi.org/10.1016/j.epsr.2006.08.031)
- [Grivet-Talocia, S. & Ubolli, A. On the Generation of Large Passive Macromodels for Complex Interconnect Structures. IEEE Trans. Adv. Packag. 29, 39–54 (2006)](on-the-generation-of-large-passive-macromodels-for-complex-interconnect-structures) -- [10.1109/tadvp.2005.862659](https://doi.org/10.1109/tadvp.2005.862659)
- Noda, T. Identification of a Multiphase Network Equivalent for Electromagnetic Transient Calculations Using Partitioned Frequency Response. IEEE Trans. Power Delivery 20, 1134–1142 (2005) -- [10.1109/tpwrd.2004.834347](https://doi.org/10.1109/tpwrd.2004.834347)
- MANYAHI, M., LEIJON, M. & THOTTAPPILLIL, R. Transient response of transformer with XLPE insulation cable winding design. International Journal of Electrical Power &amp; Energy Systems 27, 69–80 (2005) -- [10.1016/j.ijepes.2004.07.010](https://doi.org/10.1016/j.ijepes.2004.07.010)
- Gustavsen, B. Wide Band Modeling of Power Transformers. IEEE Trans. Power Delivery 19, 414–422 (2004) -- [10.1109/tpwrd.2003.820197](https://doi.org/10.1109/tpwrd.2003.820197)
- Marti, J. Accurate Modelling of Frequency-Dependent Transmission Lines in Electromagnetic Transient Simulations. IEEE Trans. Power Appar. Syst. PAS-101, 147–157 (1982) -- [10.1109/tpas.1982.317332](https://doi.org/10.1109/tpas.1982.317332)
- Gustavsen, B. & Semlyen, A. Rational approximation of frequency domain responses by vector fitting. IEEE Trans. Power Delivery 14, 1052–1061 (1999) -- [10.1109/61.772353](https://doi.org/10.1109/61.772353)
- Semlyen, A. & Dabuleanu, A. Fast and accurate switching transient calculations on transmission lines with ground return using recursive convolutions. IEEE Trans. on Power Apparatus and Syst. 94, 561–571 (1975) -- [10.1109/t-pas.1975.31884](https://doi.org/10.1109/t-pas.1975.31884)
- Gustavsen, B. Computer Code for Passivity Enforcement of Rational Macromodels by Residue Perturbation. IEEE Trans. Adv. Packag. 30, 209–215 (2007) -- [10.1109/tadvp.2007.896014](https://doi.org/10.1109/tadvp.2007.896014)
- Boyd, S. & Chua, L. O. On the passivity criterion for lti N‐ports. Circuit Theory &amp; Apps 10, 323–333 (1982) -- [10.1002/cta.4490100404](https://doi.org/10.1002/cta.4490100404)
- Gustavsen, B. Fast passivity enforcement of rational macromodels by perturbation of residue matrix eigenvalues. 2007 IEEE Workshop on Signal Propagation on Interconnects 71–74 (2007) doi:10.1109/spi.2007.4512213 -- [10.1109/spi.2007.4512213](https://doi.org/10.1109/spi.2007.4512213)
- Boyd, S., El Ghaoui, L., Feron, E. & Balakrishnan, V. Linear Matrix Inequalities in System and Control Theory. (1994) doi:10.1137/1.9781611970777 -- [10.1137/1.9781611970777](https://doi.org/10.1137/1.9781611970777)
- Wedepohl, L. M., Nguyen, H. V. & Irwin, G. D. Frequency-dependent transformation matrices for untransposed transmission lines using Newton-Raphson method. IEEE Trans. Power Syst. 11, 1538–1546 (1996) -- [10.1109/59.535695](https://doi.org/10.1109/59.535695)
- Li, E.-P., Liu, E.-X., Li, L.-W. & Leong, M.-S. A Coupled Efficient and Systematic Full-Wave Time-Domain Macromodeling and Circuit Simulation Method for Signal Integrity Analysis of High-Speed Interconnects. IEEE Trans. Adv. Packag. 27, 213–223 (2004) -- [10.1109/tadvp.2004.825448](https://doi.org/10.1109/tadvp.2004.825448)
- Gustavsen, B. & Semlyen, A. A Robust Approach for System Identification in the Frequency Domain. IEEE Trans. Power Delivery 19, 1167–1173 (2004) -- [10.1109/tpwrd.2003.822530](https://doi.org/10.1109/tpwrd.2003.822530)

