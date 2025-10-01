---
title: "Analysis of Compatible Discrete Operator schemes for elliptic problems on polyhedral meshes"
date: 2013-07-23 00:00:00 +0100
permalink: analysis-of-compatible-discrete-operator-schemes-for-elliptic-problems-on-polyhedral-meshes
year: 2014
authors: Jérôme Bonelle, Alexandre Ern
category: articles
---
 
## Authors
[Jérôme Bonelle](authors/jerome-bonelle), [Alexandre Ern](authors/alexandre-ern)
 
## Abstract
Compatible schemes localize degrees of freedom according to the physical nature of the underlying fields and operate a clear distinction between topological laws and closure relations. For elliptic problems, the cornerstone in the scheme design is the discrete Hodge operator linking gradients to fluxes by means of a dual mesh, while a structure-preserving discretization is employed for the gradient and divergence operators. The discrete Hodge operator is sparse, symmetric positive definite and is assembled cellwise from local operators. We analyze two schemes depending on whether the potential degrees of freedom are attached to the vertices or to the cells of the primal mesh. We derive new functional analysis results on the discrete gradient that are the counterpart of the Sobolev embeddings. Then, we identify the two design properties of the local discrete Hodge operators yielding optimal discrete energy error estimates. Additionally, we show how these operators can be built from local nonconforming gradient reconstructions using a dual barycentric mesh. In this case, we also prove an optimal L 2 -error estimate for the potential for smooth solutions. Links with existing schemes (finite elements, finite volumes, mimetic finite differences) are discussed. Numerical results are presented on three-dimensional polyhedral meshes. The detailed material is available from http://hal.archives-ouvertes.fr/hal-00751284
 
## Citation
- **Journal:** ESAIM: Mathematical Modelling and Numerical Analysis
- **Year:** 2014
- **Volume:** 48
- **Issue:** 2
- **Pages:** 553--581
- **Publisher:** EDP Sciences
- **DOI:** [10.1051/m2an/2013104](https://doi.org/10.1051/m2an/2013104)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Bonelle_2014,
  title={{Analysis of Compatible Discrete Operator schemes for elliptic problems on polyhedral meshes}},
  volume={48},
  ISSN={1290-3841},
  DOI={10.1051/m2an/2013104},
  number={2},
  journal={ESAIM: Mathematical Modelling and Numerical Analysis},
  publisher={EDP Sciences},
  author={Bonelle, Jérôme and Ern, Alexandre},
  year={2014},
  pages={553--581}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/analysis-of-compatible-discrete-operator-schemes-for-elliptic-problems-on-polyhedral-meshes.bib)
 
## References
- Arnold, D. N., Falk, R. S. & Winther, R. Finite element exterior calculus, homological techniques, and applications. Acta Numerica vol. 15 1–155 (2006) -- [10.1017/s0962492906210018](https://doi.org/10.1017/s0962492906210018)
- Bochev, P. B. & Hyman, J. M. Principles of Mimetic Discretizations of Differential Operators. The IMA Volumes in Mathematics and its Applications 89–119 doi:10.1007/0-387-38034-5_5 -- [10.1007/0-387-38034-5_5](https://doi.org/10.1007/0-387-38034-5_5)
- Brezzi, F., Buffa, A. & Lipnikov, K. Mimetic finite differences for elliptic problems. ESAIM: Mathematical Modelling and Numerical Analysis vol. 43 277–295 (2008) -- [10.1051/m2an:2008046](https://doi.org/10.1051/m2an:2008046)
- Codecasa, L., Specogna, R. & Trevisan, F. A new set of basis functions for the discrete geometric approach. Journal of Computational Physics vol. 229 7401–7410 (2010) -- [10.1016/j.jcp.2010.06.023](https://doi.org/10.1016/j.jcp.2010.06.023)
- Di Pietro, D. A. & Ern, A. Mathematical Aspects of Discontinuous Galerkin Methods. Mathématiques et Applications (Springer Berlin Heidelberg, 2012). doi:10.1007/978-3-642-22980-0 -- [10.1007/978-3-642-22980-0](https://doi.org/10.1007/978-3-642-22980-0)
- Dodziuk, J. Finite-Difference Approach to the Hodge Theory of Harmonic Forms. American Journal of Mathematics vol. 98 79 (1976) -- [10.2307/2373615](https://doi.org/10.2307/2373615)
- Domelevo, K. & Omnes, P. A finite volume method for the Laplace equation on almost arbitrary two-dimensional grids. ESAIM: Mathematical Modelling and Numerical Analysis vol. 39 1203–1249 (2005) -- [10.1051/m2an:2005047](https://doi.org/10.1051/m2an:2005047)
- Eymard, R., Guichard, C. & Herbin, R. Small-stencil 3D schemes for diffusive flows in porous media. ESAIM: Mathematical Modelling and Numerical Analysis vol. 46 265–290 (2011) -- [10.1051/m2an/2011040](https://doi.org/10.1051/m2an/2011040)
- Eymard, R. et al. 3D Benchmark on Discretization Schemes for Anisotropic Diffusion Problems on General Grids. Springer Proceedings in Mathematics 895–930 (2011) doi:10.1007/978-3-642-20671-9_89 -- [10.1007/978-3-642-20671-9_89](https://doi.org/10.1007/978-3-642-20671-9_89)
- Hiptmair, R. Discrete Hodge-Operators: An Algebraic Perspective. Progress In Electromagnetics Research vol. 32 247–269 (2001) -- [10.2528/pier00080110](https://doi.org/10.2528/pier00080110)
- Mattiussi, C. The finite volume, finite element, and finite difference methods as numerical methods for physical field problems. Advances in Imaging and Electron Physics 1–146 (2000) doi:10.1016/s1076-5670(00)80012-9 -- [10.1016/s1076-5670(00)80012-9](https://doi.org/10.1016/s1076-5670(00)80012-9)
- Perot, J. B. & Subramanian, V. Discrete calculus methods for diffusion. Journal of Computational Physics vol. 224 59–81 (2007) -- [10.1016/j.jcp.2006.12.022](https://doi.org/10.1016/j.jcp.2006.12.022)
- Tarhasaari, T., Kettunen, L. & Bossavit, A. Some realizations of a discrete Hodge operator: a reinterpretation of finite element techniques [for EM field analysis]. IEEE Transactions on Magnetics vol. 35 1494–1497 (1999) -- [10.1109/20.767250](https://doi.org/10.1109/20.767250)
- Whitney, H. Geometric Integration Theory. (Princeton University Press, 1957). doi:10.1515/9781400877577 -- [10.1515/9781400877577](https://doi.org/10.1515/9781400877577)

