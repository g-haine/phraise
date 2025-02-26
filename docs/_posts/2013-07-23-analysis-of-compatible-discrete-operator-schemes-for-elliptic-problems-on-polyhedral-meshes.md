---
layout: post
title: "Analysis of Compatible Discrete Operator schemes for elliptic problems on polyhedral meshes"
date: 2013-07-23 00:00:00 +0100
permalink: analysis-of-compatible-discrete-operator-schemes-for-elliptic-problems-on-polyhedral-meshes
year: 2014
authors: Jérôme Bonelle, Alexandre Ern
category: journal-article
---
 
## Authors
**Jérôme Bonelle, Alexandre Ern**
 
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
 
## References
- Amrouche C., Bernardi C., Dauge M. and Girault V., Vector potentials in three-dimensional non-smooth domains.Math. Meth. Appl. Sci.21(1998) 823–864.
- Andreianov B., Boyer F. and Hubert F., Discrete duality finite volume schemes for Leray-Lions-type elliptic problems on general 2D meshes.Numer. Methods Partial Differ. Eqs.23(2007) 145–195.
- Arnold D.N., Falk R.S. and Winther R., Finite element exterior calculus, homological techniques, and applications.Acta Numerica15(2006) 1–155. -- [10.1017/S0962492906210018](https://doi.org/10.1017/S0962492906210018)
- A. Back, Étude théorique et numérique des équations de Vlasov–Maxwell dans le formalisme covariant. Ph.D. thesis, University of Strasbourg (2011).
- P. Bochev and J.M. Hyman, Principles of mimetic discretizations of differential operators,Compatible Spatial Discretization. In vol. 142 ofThe IMA Volumes Math. Appl., edited by D. Arnold, P. Bochev, R. Lehoucq, R.A. Nicolaides and M. Shashkov (2005) 89–120. -- [10.1007/0-387-38034-5_5](https://doi.org/10.1007/0-387-38034-5_5)
- A. Bossavit, On the geometry of electromagnetism.J. Japan Soc. Appl. Electromagn. Mech.6(1998) (no 1) 17–28, (no 2) 114–23, (no 3) 233–40, (no 4) 318–26.
- A. Bossavit, Computational electromagnetism and geometry.J. Japan Soc. Appl. Electromagn. Mech.7-8(1999–2000) (no 1) 150–9, (no 2) 294–301, (no 3) 401–8, (no 4) 102–9, (no 5) 203–9, (no 6) 372–7.
- Brezzi F., Buffa A. and Lipnikov K., Mimetic finite difference for elliptic problem.Math. Model. Numer. Anal.43(2009) 277–295. -- [10.1051/m2an:2008046](https://doi.org/10.1051/m2an:2008046)
- Brezzi F., Lipnikov K. and Shashkov M., Convergence of the mimetic finite difference method for diffusion problems on polyhedral meshes.SIAM J. Numer. Anal.43(2005) 1872–1896.
- Buffa A. and Christiansen S.H., A dual finite element complex on the barycentric refinement.Math. Comput.76(2007) 1743–1769.
- Christiansen S.H., A construction of spaces of compatible differential forms on cellular complexes.Math. Models Methods Appl. Sci.18(2008) 739–757.
- Christiansen S.H., Munthe-Kaas H.Z. and Owren B., Topics in structure-preserving discretization.Acta Numer.20(2011) 1–119.
- Codecasa L., Specogna R. and Trevisan F., Base functions and discrete constitutive relations for staggered polyhedral grids.Comput. Methods Appl. Mech. Engrg.198(2009) 1117–1123.
- Codecasa L., Specogna R. and Trevisan F., A new set of basis functions for the discrete geometric approach.J. Comput. Phys.229(2010) 7401–7410. -- [10.1016/j.jcp.2010.06.023](https://doi.org/10.1016/j.jcp.2010.06.023)
- Codecasa L. and Trevisan F., Convergence of electromagnetic problems modelled by discrete geometric approach.CMES58(2010) 15–44.
- M. Desbrun, A.N. Hirani, M. Leok and J.E. Marsden, Discrete Exterior Calculus. Technical report (2005).
- D.A. Di Pietro and A. Ern, Mathematical Aspects of Discontinuous Galerkin Methods, in vol. 69 ofSMAI Math. Appl.Springer (2012). -- [10.1007/978-3-642-22980-0](https://doi.org/10.1007/978-3-642-22980-0)
- Dodziuk J., Finite-difference approach to the Hodge theory of harmonic forms.Amer. J. Math.98(1976) 79–104. -- [10.2307/2373615](https://doi.org/10.2307/2373615)
- Domelevo K. and Omnes P., A finite volume method for the Laplace equation on almost arbitrary two-dimensional grids.ESAIM: M2AN39(2005) 1203–1249. -- [10.1051/m2an:2005047](https://doi.org/10.1051/m2an:2005047)
- Droniou J. and Eymard R., A mixed finite volume scheme for anisotropic diffusion problems on any grid.Numer. Math.105(2006) 35–71.
- Droniou J., Eymard R., Gallouët T. and Herbin R., A Unified Approach to Mimetic Finite Difference, Hybrid Finite Volume and Mixed Finite Volume Methods.Math. Models and Methods Appl. Sci.20(2010) 265–295.
- Eymard R., Gallouët T. and Herbin R., Discretization of heterogeneous and anisotropic diffusion problems on general nonconforming meshes SUSHI: a scheme using stabilization and hybrid interfaces.IMA J. Numer. Anal.30(2010) 1009–1043.
- Eymard R., Guichard C. and Herbin R., Small stencil 3d schemes for diffusive flows in porious media.ESAIM: M2AN46(2012) 265–290. -- [10.1051/m2an/2011040](https://doi.org/10.1051/m2an/2011040)
- R. Eymard, G. Henry, R. Herbin, F. Hubert, R. Klöfkorn and G. Manzini, 3d benchmark on discretization schemes for anisotropic diffusion problems on general grids, in vol. 2 ofFinite Volumes for Complex Applic. VI – Problems Perspectives. Springer (2011) 95–130. -- [10.1007/978-3-642-20671-9_89](https://doi.org/10.1007/978-3-642-20671-9_89)
- A. Gillette,Stability of dual discretization methods for partial differential equations. Ph.D. thesis, University of Texas at Austin (2011).
- Hiptmair R., Discrete hodge operators: An algebraic perspective.Progress In Electromagnetics Research32(2001) 247–269. -- [10.2528/PIER00080110](https://doi.org/10.2528/PIER00080110)
- Xiao Hua Hu and Nicolaides R.A., Covolume techniques for anisotropic media.Numer. Math.61(1992) 215–234.
- J. Hyman and J. Scovel, Deriving mimetic difference approximations to differential operators using algebraic topology. Los Alamos National Laboratory (1988).
- J. Kreeft, A. Palha and M. Gerritsma, Mimetic framework on curvilinear quadrilaterals of arbitrary order. Technical Report, Delft University (2011) ArXiv: 1111.4304v1.
- C. Mattiussi, The finite volume, finite element, and finite difference methods as numerical methods for physical field problems. In vol. 113 ofAdvances in Imaging and Electron Phys.Elsevier (2000) 1–146. -- [10.1016/S1076-5670(00)80012-9](https://doi.org/10.1016/S1076-5670(00)80012-9)
- Perot J.B. and Subramanian V., Discrete calculus methods for diffusion.J. Comput. Phys.224(2007) 59–81. -- [10.1016/j.jcp.2006.12.022](https://doi.org/10.1016/j.jcp.2006.12.022)
- Tarhasaari T., Kettunen L. and Bossavit A., Some realizations of a discrete hodge operator: A reinterpretation of finite element techniques.IEEE Transactions on Magnetics35(1999) 1494–1497. -- [10.1109/20.767250](https://doi.org/10.1109/20.767250)
- E. Tonti,On the formal structure of physical theories. Instituto di matematica, Politecnico, Milano (1975).
- Vohralík M. and Wohlmuth B., Mixed finite element methods: implementation with one unknown per element, local flux expressions, positivity, polygonal meshes, and relations to other methods.Math. Models Methods Appl. Sci.23(2013) 803–838.
- H. Whitney,Geometric integration theory. Princeton University Press, Princeton, N.J. (1957). -- [10.1515/9781400877577](https://doi.org/10.1515/9781400877577)
- S. Zaglmayr,High order finite element methods for electromagnetic field computation. Ph.D. thesis, Johannes Kepler Universität Linz (2006).

