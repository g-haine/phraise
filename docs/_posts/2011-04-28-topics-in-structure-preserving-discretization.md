---
layout: post
title: "Topics in structure-preserving discretization"
date: 2011-04-28 00:00:00 +0100
permalink: topics-in-structure-preserving-discretization
year: 2011
authors: Snorre H. Christiansen, Hans Z. Munthe-Kaas, Brynjulf Owren
category: journal-article
---
 
## Authors
[Snorre H. Christiansen](authors/snorre-h-christiansen), [Hans Z. Munthe-Kaas](authors/hans-z-munthe-kaas), [Brynjulf Owren](authors/brynjulf-owren)
 
## Abstract
In the last few decades the concepts of structure-preserving discretization, geometric integration and compatible discretizations have emerged as subfields in the numerical approximation of ordinary and partial differential equations. The article discusses certain selected topics within these areas; discretization techniques both in space and time are considered. Lie group integrators are discussed with particular focus on the application to partial differential equations, followed by a discussion of how time integrators can be designed to preserve first integrals in the differential equation using discrete gradients and discrete variational derivatives.\n Lie group integrators depend crucially on fast and structure-preserving algorithms for computing matrix exponentials. Preservation of domain symmetries is of particular interest in the application of Lie group integrators to PDEs. The equivariance of linear operators and Fourier transforms on non-commutative groups is used to construct fast structure-preserving algorithms for computing exponentials. The theory of Weyl groups is employed in the construction of high-order spectral element discretizations, based on multivariate Chebyshev polynomials on triangles, simplexes and simplicial complexes.\n The theory of mixed finite elements is developed in terms of special inverse systems of complexes of differential forms, where the inclusion of cells corresponds to pullback of forms. The theory covers, for instance, composite piecewise polynomial finite elements of variable order over polyhedral grids. Under natural algebraic and metric conditions, interpolators and smoothers are constructed, which commute with the exterior derivative and whose product is uniformly stable in Lebesgue spaces. As a consequence we obtain not only eigenpair approximation for the Hodge–Laplacian in mixed form, but also variants of Sobolev injections and translation estimates adapted to variational discretizations.
 
## Citation
- **Journal:** Acta Numerica
- **Year:** 2011
- **Volume:** 20
- **Issue:** 
- **Pages:** 1--119
- **Publisher:** Cambridge University Press (CUP)
- **DOI:** [10.1017/S096249291100002X](https://doi.org/10.1017/S096249291100002X)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Christiansen_2011,
  title={{Topics in structure-preserving discretization}},
  volume={20},
  ISSN={1474-0508},
  DOI={10.1017/s096249291100002x},
  journal={Acta Numerica},
  publisher={Cambridge University Press (CUP)},
  author={Christiansen, Snorre H. and Munthe-Kaas, Hans Z. and Owren, Brynjulf},
  year={2011},
  pages={1--119}
}
{% endraw %}
{% endhighlight %}
 
## References
- Diele, F., Lopez, L. & Peluso, R. Advances in Computational Mathematics vol. 8 317–334 (1998) -- [10.1023/A:1018908700358](https://doi.org/10.1023/A:1018908700358)
- Krogstad, S. Generalized integrating factor methods for stiff PDEs. Journal of Computational Physics vol. 203 72–88 (2005) -- [10.1016/j.jcp.2004.08.006](https://doi.org/10.1016/j.jcp.2004.08.006)
- Marthinsen, A. & Owren, B. Quadrature methods based on the Cayley transform. Applied Numerical Mathematics vol. 39 403–413 (2001) -- [10.1016/S0168-9274(01)00087-3](https://doi.org/10.1016/S0168-9274(01)00087-3)
- The stability of solitary waves. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences vol. 328 153–183 (1972) -- [10.1098/rspa.1972.0074](https://doi.org/10.1098/rspa.1972.0074)
- Bump, D. Lie Groups. Graduate Texts in Mathematics (Springer New York, 2004). doi:10.1007/978-1-4757-4094-3 -- [10.1007/978-1-4757-4094-3](https://doi.org/10.1007/978-1-4757-4094-3)
- Munthe-Kaas, H. Runge-Kutta methods on Lie groups. BIT Numerical Mathematics vol. 38 92–111 (1998) -- [10.1007/BF02510919](https://doi.org/10.1007/BF02510919)
- Olver, P. J. Applications of Lie Groups to Differential Equations. Graduate Texts in Mathematics (Springer New York, 1993). doi:10.1007/978-1-4612-4350-2 -- [10.1007/978-1-4612-4350-2](https://doi.org/10.1007/978-1-4612-4350-2)
- McLachlan, R. I. On the Numerical Integration of Ordinary Differential Equations by Symmetric Composition Methods. SIAM Journal on Scientific Computing vol. 16 151–168 (1995) -- [10.1137/0916010](https://doi.org/10.1137/0916010)
- Celledoni, E. Eulerian and semi-Lagrangian schemes based o
                    commutator-free exponential integrators. CRM Proceedings and Lecture Notes 77–90 (2005) doi:10.1090/crmp/039/06 -- [10.1090/crmp/039/06](https://doi.org/10.1090/crmp/039/06)
- Furihata, D. Finite Difference Schemes for ∂u∂t=(∂∂x)αδGδu That Inherit Energy Conservation or Dissipation Property. Journal of Computational Physics vol. 156 181–205 (1999) -- [10.1006/jcph.1999.6377](https://doi.org/10.1006/jcph.1999.6377)
- Courant, R., Friedrichs, K. & Lewy, H. �ber die partiellen Differenzengleichungen der mathematischen Physik. Mathematische Annalen vol. 100 32–74 (1928) -- [10.1007/BF01448839](https://doi.org/10.1007/BF01448839)
- Owren, B. & Marthinsen, A. Bit Numerical Mathematics vol. 39 116–142 (1999) -- [10.1023/A:1022325426017](https://doi.org/10.1023/A:1022325426017)
- Lopez, L. & Politi, T. Applications of the Cayley approach in the numerical solution of matrix differential systems on quadratic groups. Applied Numerical Mathematics vol. 36 35–55 (2001) -- [10.1016/S0168-9274(99)00049-5](https://doi.org/10.1016/S0168-9274(99)00049-5)
- Lewis, D. & Simo, J. C. Conserving algorithms for the dynamics of Hamiltonian systems on lie groups. Journal of Nonlinear Science vol. 4 253–299 (1994) -- [10.1007/BF02430634](https://doi.org/10.1007/BF02430634)
- LaBudde, R. A. & Greenspan, D. Discrete mechanics—A general treatment. Journal of Computational Physics vol. 15 134–167 (1974) -- [10.1016/0021-9991(74)90081-3](https://doi.org/10.1016/0021-9991(74)90081-3)
- Kuznetsov, Yu. & Repin, S. Convergence analysis and error estimates for mixed finite element method on distorted meshes. Journal of Numerical Mathematics vol. 13 (2005) -- [10.1515/1569395054068973](https://doi.org/10.1515/1569395054068973)
- Kennedy, C. A. & Carpenter, M. H. Additive Runge–Kutta schemes for convection–diffusion–reaction equations. Applied Numerical Mathematics vol. 44 139–181 (2003) -- [10.1016/S0168-9274(02)00138-1](https://doi.org/10.1016/S0168-9274(02)00138-1)
- Krogstad, S., Munthe-Kaas, H. Z. & Zanna, A. Generalized polar coordinates on Lie groups and numerical integrators. Numerische Mathematik vol. 114 161–187 (2009) -- [10.1007/s00211-009-0255-1](https://doi.org/10.1007/s00211-009-0255-1)
- Beerends, R. J. Chebyshev polynomials in several variables and the radial part of the Laplace-Beltrami operator. Transactions of the American Mathematical Society vol. 328 779–814 (1991) -- [10.1090/S0002-9947-1991-1019520-3](https://doi.org/10.1090/S0002-9947-1991-1019520-3)
- Hiptmair, R. Canonical construction of finite elements. Mathematics of Computation vol. 68 1325–1346 (1999) -- [10.1090/S0025-5718-99-01166-7](https://doi.org/10.1090/S0025-5718-99-01166-7)
- Munthe-Kaas, H. High order Runge-Kutta methods on manifolds. Applied Numerical Mathematics vol. 29 115–127 (1999) -- [10.1016/S0168-9274(98)00030-0](https://doi.org/10.1016/S0168-9274(98)00030-0)
- Matsuo, T. Dissipative/conservative Galerkin method using discrete partial derivatives for nonlinear evolution equations. Journal of Computational and Applied Mathematics vol. 218 506–521 (2008) -- [10.1016/j.cam.2007.08.001](https://doi.org/10.1016/j.cam.2007.08.001)
- Iserles, A. & Nørsett, S. P. On the solution of linear differential equations in Lie groups. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 357 983–1019 (1999) -- [10.1098/rsta.1999.0362](https://doi.org/10.1098/rsta.1999.0362)
- Hilbert, S. A mollifier useful for approximations in Sobolev spaces and some applications to approximating solutions of differential equations. Mathematics of Computation vol. 27 81–89 (1973) -- [10.1090/S0025-5718-1973-0331715-3](https://doi.org/10.1090/S0025-5718-1973-0331715-3)
- Crouch, P. E. & Grossman, R. Numerical integration of ordinary differential equations on manifolds. Journal of Nonlinear Science vol. 3 1–33 (1993) -- [10.1007/BF02429858](https://doi.org/10.1007/BF02429858)
- Hesthaven, J. S. From Electrostatics to Almost Optimal Nodal Sets for Polynomial Interpolation in a Simplex. SIAM Journal on Numerical Analysis vol. 35 655–676 (1998) -- [10.1137/S003614299630587X](https://doi.org/10.1137/S003614299630587X)
- Wensch, J., Knoth, O. & Galant, A. Multirate infinitesimal step methods for atmospheric flow simulation. BIT Numerical Mathematics vol. 49 449–473 (2009) -- [10.1007/s10543-009-0222-3](https://doi.org/10.1007/s10543-009-0222-3)
- Demkowicz, L. & Babuska, I. p Interpolation Error Estimates for Edge Finite Elements of Variable Order in Two Dimensions. SIAM Journal on Numerical Analysis vol. 41 1195–1208 (2003) -- [10.1137/S0036142901387932](https://doi.org/10.1137/S0036142901387932)
- Celledoni, E. Methods for the approximation of the matrix exponential in a Lie-algebraic setting. IMA Journal of Numerical Analysis vol. 21 463–488 (2001) -- [10.1093/imanum/21.2.463](https://doi.org/10.1093/imanum/21.2.463)
- Iserles, A. & Zanna, A. Efficient Computation of the Matrix Exponential by Generalized Polar Decompositions. SIAM Journal on Numerical Analysis vol. 42 2218–2256 (2005) -- [10.1137/S0036142902415936](https://doi.org/10.1137/S0036142902415936)
- Dubiner, M. Spectral methods on triangles and other domains. Journal of Scientific Computing vol. 6 345–390 (1991) -- [10.1007/BF01060030](https://doi.org/10.1007/BF01060030)
- Christiansen, S. H. & Winther, R. On Constraint Preservation in Numerical Simulations of Yang--Mills Equations. SIAM Journal on Scientific Computing vol. 28 75–101 (2006) -- [10.1137/040616887](https://doi.org/10.1137/040616887)
- Owren, B. Order conditions for commutator-free Lie group methods. Journal of Physics A: Mathematical and General vol. 39 5585–5599 (2006) -- [10.1088/0305-4470/39/19/S15](https://doi.org/10.1088/0305-4470/39/19/S15)
- Douglas, C. C. & Mandel, J. An abstract theory for the domain reduction method. Computing vol. 48 73–96 (1992) -- [10.1007/BF02241707](https://doi.org/10.1007/BF02241707)
- Furihata, D. A stable and conservative finite difference scheme for the Cahn-Hilliard equation. Numerische Mathematik vol. 87 675–699 (2001) -- [10.1007/PL00005429](https://doi.org/10.1007/PL00005429)
- Munthe-Kaas H. (1989), Symmetric FFTs: A general approach. In Topics in Linear Algebra for Vector and Parallel Computers, PhD thesis, NTNU, Trondheim, Norway. Available at: hans.munthe-kaas.no.
- Hochbruck, M. & Ostermann, A. Explicit Exponential Runge--Kutta Methods for Semilinear Parabolic Problems. SIAM Journal on Numerical Analysis vol. 43 1069–1090 (2005) -- [10.1137/040611434](https://doi.org/10.1137/040611434)
- Brezzi, F., Douglas, J., Jr. & Marini, L. D. Two families of mixed finite elements for second order elliptic problems. Numerische Mathematik vol. 47 217–235 (1985) -- [10.1007/BF01389710](https://doi.org/10.1007/BF01389710)
- Celledoni, E., Cohen, D. & Owren, B. Symmetric Exponential Integrators with an Application to the Cubic Schrödinger Equation. Foundations of Computational Mathematics vol. 8 303–317 (2007) -- [10.1007/s10208-007-9016-7](https://doi.org/10.1007/s10208-007-9016-7)
- Matsuo, T. & Furihata, D. Dissipative or Conservative Finite-Difference Schemes for Complex-Valued Nonlinear Partial Differential Equations. Journal of Computational Physics vol. 171 425–447 (2001) -- [10.1006/jcph.2001.6775](https://doi.org/10.1006/jcph.2001.6775)
- Buffa, A. & Christiansen, S. H. A dual finite element complex on the barycentric refinement. Mathematics of Computation vol. 76 1743–1770 (2007) -- [10.1090/S0025-5718-07-01965-5](https://doi.org/10.1090/S0025-5718-07-01965-5)
- Furihata, D. & Matsuo, T. A stable, convergent, conservative and linear finite difference scheme for the Cahn-Hilliard equation. Japan Journal of Industrial and Applied Mathematics vol. 20 65–85 (2003) -- [10.1007/BF03167463](https://doi.org/10.1007/BF03167463)
- Baker, H. F. Alternants and Continuous Groups. Proceedings of the London Mathematical Society vols s2-3 24–47 (1905) -- [10.1112/plms/s2-3.1.24](https://doi.org/10.1112/plms/s2-3.1.24)
- Minchev B. V. (2004), Exponential Integrators for Semilinear Problems, University of Bergen. PhD thesis, University of Bergen, Norway.
- Clément, Ph. Approximation by finite element functions using local regularization. Revue française d’automatique, informatique, recherche opérationnelle. Analyse numérique vol. 9 77–84 (1975) -- [10.1051/m2an/197509R200771](https://doi.org/10.1051/m2an/197509R200771)
- Blanes, S., Casas, F., Oteo, J. A. & Ros, J. The Magnus expansion and some of its applications. Physics Reports vol. 470 151–238 (2009) -- [10.1016/j.physrep.2008.11.001](https://doi.org/10.1016/j.physrep.2008.11.001)
- Bryant, R. An introduction to Lie groups and symplecti
                    geometry. IAS/Park City Mathematics Series 5–181 (1995) doi:10.1090/pcms/001/02 -- [10.1090/pcms/001/02](https://doi.org/10.1090/pcms/001/02)
- Trønnes A. (2005), Symmetries and generalized Fourier transforms applied to computing the matrix exponential. Master's thesis, University of Bergen, Norway.
- Warner, F. W. Foundations of Differentiable Manifolds and Lie Groups. Graduate Texts in Mathematics (Springer New York, 1983). doi:10.1007/978-1-4757-1799-0 -- [10.1007/978-1-4757-1799-0](https://doi.org/10.1007/978-1-4757-1799-0)
- Matsuo, T., Sugihara, M., Furihata, D. & Mori, M. Spatially accurate dissipative or conservative finite difference schemes derived by the discrete variational method. Japan Journal of Industrial and Applied Mathematics vol. 19 311–330 (2002) -- [10.1007/BF03167482](https://doi.org/10.1007/BF03167482)
- Owren, B. & Marthinsen, A. Integration methods based on canonical coordinates of the second kind. Numerische Mathematik vol. 87 763–790 (2001) -- [10.1007/PL00005432](https://doi.org/10.1007/PL00005432)
- Lawson, J. D. Generalized Runge-Kutta Processes for Stable Systems with Large Lipschitz Constants. SIAM Journal on Numerical Analysis vol. 4 372–380 (1967) -- [10.1137/0704033](https://doi.org/10.1137/0704033)
- Huybrechs, D. On the Fourier Extension of Nonperiodic Functions. SIAM Journal on Numerical Analysis vol. 47 4326–4355 (2010) -- [10.1137/090752456](https://doi.org/10.1137/090752456)
- Christiansen, S. H. Stability of Hodge decompositions in finite element spaces of differential forms in arbitrary dimension. Numerische Mathematik vol. 107 87–106 (2007) -- [10.1007/s00211-007-0081-2](https://doi.org/10.1007/s00211-007-0081-2)
- Christiansen, S. H. Éléments finis mixtes minimaux sur les polyèdres. Comptes Rendus. Mathématique vol. 348 217–221 (2010) -- [10.1016/j.crma.2010.01.017](https://doi.org/10.1016/j.crma.2010.01.017)
- Pasciak, J. E. & Vassilevski, P. S. Exact de Rham Sequences of Spaces Defined on Macro-Elements in Two and Three Spatial Dimensions. SIAM Journal on Scientific Computing vol. 30 2427–2446 (2008) -- [10.1137/070698178](https://doi.org/10.1137/070698178)
- Allgower, E. L., Georg, K., Miranda, R. & Tausch, J. Numerical Exploitation of Equivariance. ZAMM - Zeitschrift für Angewandte Mathematik und Mechanik vol. 78 795–806 (1998) -- [10.1002/(SICI)1521-4001(199812)78:12<795::AID-ZAMM795>3.0.CO;2-P](https://doi.org/10.1002/(SICI)1521-4001(199812)78:12<795::AID-ZAMM795>3.0.CO;2-P)
- Zanna, A. & Munthe-Kaas, H. Z. Generalized Polar Decompositions for the Approximation of the Matrix Exponential. SIAM Journal on Matrix Analysis and Applications vol. 23 840–862 (2002) -- [10.1137/S0895479800377551](https://doi.org/10.1137/S0895479800377551)
- Celledoni, E. & Iserles, A. Approximating the exponential from a Lie algebra to a Lie group. Mathematics of Computation vol. 69 1457–1481 (2000) -- [10.1090/S0025-5718-00-01223-0](https://doi.org/10.1090/S0025-5718-00-01223-0)
- Karlsen, K. H. & Karper, T. K. Convergence of a mixed method for a semi-stationary compressible Stokes system. Mathematics of Computation vol. 80 1459–1498 (2010) -- [10.1090/S0025-5718-2010-02446-9](https://doi.org/10.1090/S0025-5718-2010-02446-9)
- Celledoni, E. & Kometa, B. K. Semi-Lagrangian Runge-Kutta Exponential Integrators for Convection Dominated Problems. Journal of Scientific Computing vol. 41 139–164 (2009) -- [10.1007/s10915-009-9291-3](https://doi.org/10.1007/s10915-009-9291-3)
- Model equations for long waves in nonlinear dispersive systems. Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences vol. 272 47–78 (1972) -- [10.1098/rsta.1972.0032](https://doi.org/10.1098/rsta.1972.0032)
- Åhlander, K. & Munthe-Kaas, H. Applications of the Generalized Fourier Transform in Numerical Linear Algebra. BIT Numerical Mathematics vol. 45 819–850 (2005) -- [10.1007/s10543-005-0030-3](https://doi.org/10.1007/s10543-005-0030-3)
- Kang, F. & Zai-jiu, S. Volume-preserving algorithms for source-free dynamical systems. Numerische Mathematik vol. 71 451–463 (1995) -- [10.1007/s002110050153](https://doi.org/10.1007/s002110050153)
- Munthe-Kaas, H. Lie-Butcher theory for Runge-Kutta methods. BIT Numerical Mathematics vol. 35 572–587 (1995) -- [10.1007/BF01739828](https://doi.org/10.1007/BF01739828)
- [Gonzalez, O. Time integration and discrete Hamiltonian systems. Journal of Nonlinear Science vol. 6 449–467 (1996)](time-integration-and-discrete-hamiltonian-systems) -- [10.1007/BF02440162](https://doi.org/10.1007/BF02440162)
- Arnold, D., Falk, R. & Winther, R. Finite element exterior calculus: from Hodge theory to numerical stability. Bulletin of the American Mathematical Society vol. 47 281–354 (2010) -- [10.1090/S0273-0979-10-01278-4](https://doi.org/10.1090/S0273-0979-10-01278-4)
- Canuto, C., Hussaini, M. Y., Quarteroni, A. & Zang, T. A. Spectral Methods. Scientific Computation (Springer Berlin Heidelberg, 2006). doi:10.1007/978-3-540-30726-6 -- [10.1007/978-3-540-30726-6](https://doi.org/10.1007/978-3-540-30726-6)
- Celledoni, E., Marthinsen, A. & Owren, B. Commutator-free Lie group methods. Future Generation Computer Systems vol. 19 341–352 (2003) -- [10.1016/S0167-739X(02)00161-9](https://doi.org/10.1016/S0167-739X(02)00161-9)
- Matsuo, T. New conservative schemes with discrete variational derivatives for nonlinear wave equations. Journal of Computational and Applied Mathematics vol. 203 32–56 (2007) -- [10.1016/j.cam.2006.03.009](https://doi.org/10.1016/j.cam.2006.03.009)
- James, G. & Liebeck, M. Representations and Characters of Groups. (2001) doi:10.1017/cbo9780511814532 -- [10.1017/CBO9780511814532](https://doi.org/10.1017/CBO9780511814532)
- Strang, G. Approximation in the finite element method. Numerische Mathematik vol. 19 81–98 (1972) -- [10.1007/BF01395933](https://doi.org/10.1007/BF01395933)
- McLachlan, R. I., Quispel, G. R. W. & Robidoux, N. Geometric integration using discrete gradients. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 357 1021–1045 (1999) -- [10.1098/rsta.1999.0363](https://doi.org/10.1098/rsta.1999.0363)
- Ryland, B. N. & Munthe-Kaas, H. Z. On Multivariate Chebyshev Polynomials and Spectral Approximations on Triangles. Lecture Notes in Computational Science and Engineering 19–41 (2010) doi:10.1007/978-3-642-15337-2_2 -- [10.1007/978-3-642-15337-2_2](https://doi.org/10.1007/978-3-642-15337-2_2)
- Minesaki, Y. & Nakamura, Y. New numerical integrator for the Stäckel system conserving the same number of constants of motion as the degree of freedom. Journal of Physics A: Mathematical and General vol. 39 9453–9476 (2006) -- [10.1088/0305-4470/39/30/005](https://doi.org/10.1088/0305-4470/39/30/005)
- Varadarajan, V. S. Lie Groups, Lie Algebras, and Their Representations. Graduate Texts in Mathematics (Springer New York, 1984). doi:10.1007/978-1-4612-1126-6 -- [10.1007/978-1-4612-1126-6](https://doi.org/10.1007/978-1-4612-1126-6)
- McLachlan, R. I., Quispel, G. R. W. & Tse, P. S. P. Linearization-preserving self-adjoint and symplectic integrators. BIT Numerical Mathematics vol. 49 177–197 (2009) -- [10.1007/s10543-009-0214-3](https://doi.org/10.1007/s10543-009-0214-3)
- Moler, C. & Van Loan, C. Nineteen Dubious Ways to Compute the Exponential of a Matrix, Twenty-Five Years Later. SIAM Review vol. 45 3–49 (2003) -- [10.1137/S00361445024180](https://doi.org/10.1137/S00361445024180)
- ANDREIANOV, B., BENDAHMANE, M. & KARLSEN, K. H. DISCRETE DUALITY FINITE VOLUME SCHEMES FOR DOUBLY NONLINEAR DEGENERATE HYPERBOLIC-PARABOLIC EQUATIONS. Journal of Hyperbolic Differential Equations vol. 07 1–67 (2010) -- [10.1142/S0219891610002062](https://doi.org/10.1142/S0219891610002062)
- Zanna, A., Engø, K. & Munthe-Kaas, H. Z. Bit Numerical Mathematics vol. 41 395–421 (2001) -- [10.1023/A:1021950708869](https://doi.org/10.1023/A:1021950708869)
- Morton, K. W. The convection-diffusion Petrov-Galerkin story. IMA Journal of Numerical Analysis vol. 30 231–240 (2009) -- [10.1093/imanum/drp002](https://doi.org/10.1093/imanum/drp002)
- Munthe-Kaas, H. & Zanna, A. Numerical Integration of Differential Equations on Homogeneous Manifolds. Foundations of Computational Mathematics 305–315 (1997) doi:10.1007/978-3-642-60539-0_24 -- [10.1007/978-3-642-60539-0_24](https://doi.org/10.1007/978-3-642-60539-0_24)
- Munthe–Kaas, H. & Owren, B. Computations in a free Lie algebra. Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences vol. 357 957–981 (1999) -- [10.1098/rsta.1999.0361](https://doi.org/10.1098/rsta.1999.0361)
- Nedelec, J. C. Mixed finite elements in ?3. Numerische Mathematik vol. 35 315–341 (1980) -- [10.1007/BF01396415](https://doi.org/10.1007/BF01396415)
- Blanes, S. & Moan, P. C. Fourth- and sixth-order commutator-free Magnus integrators for linear and non-linear dynamical systems. Applied Numerical Mathematics vol. 56 1519–1537 (2006) -- [10.1016/j.apnum.2005.11.004](https://doi.org/10.1016/j.apnum.2005.11.004)
- Raviart, P. A. & Thomas, J. M. A mixed finite element method for 2-nd order elliptic problems. Lecture Notes in Mathematics 292–315 (1977) doi:10.1007/bfb0064470 -- [10.1007/BFb0064470](https://doi.org/10.1007/BFb0064470)
- Christiansen S. H. and Winther R. (2010), On variational eigenvalue approximation of semidefinite operators. Preprint: arXiv.org/abs/1005.2059.
- Ostermann, A., Thalhammer, M. & Wright, W. M. A Class of Explicit Exponential General Linear Methods. BIT Numerical Mathematics vol. 46 409–431 (2006) -- [10.1007/s10543-006-0054-3](https://doi.org/10.1007/s10543-006-0054-3)
- Georg, K. & Miranda, R. Exploiting Symmetry in Solving Linear Equations. Bifurcation and Symmetry 157–168 (1992) doi:10.1007/978-3-0348-7536-3_14 -- [10.1007/978-3-0348-7536-3_14](https://doi.org/10.1007/978-3-0348-7536-3_14)
- CHRISTIANSEN, S. H. A CONSTRUCTION OF SPACES OF COMPATIBLE DIFFERENTIAL FORMS ON CELLULAR COMPLEXES. Mathematical Models and Methods in Applied Sciences vol. 18 739–757 (2008) -- [10.1142/S021820250800284X](https://doi.org/10.1142/S021820250800284X)
- Schöberl J. and Sinwel A. (2007), Tangential-displacement and normal-normal-stress continuous mixed finite elements for elasticity. RICAM report.
- Serre, J.-P. Linear Representations of Finite Groups. Graduate Texts in Mathematics (Springer New York, 1977). doi:10.1007/978-1-4684-9458-7 -- [10.1007/978-1-4684-9458-7](https://doi.org/10.1007/978-1-4684-9458-7)
- Schöberl, J. A posteriori error estimates  for Maxwell equations. Mathematics of Computation vol. 77 633–650 (2007) -- [10.1090/S0025-5718-07-02030-3](https://doi.org/10.1090/S0025-5718-07-02030-3)
- Warburton, T. An explicit construction of interpolation nodes on the simplex. Journal of Engineering Mathematics vol. 56 247–262 (2006) -- [10.1007/s10665-006-9086-6](https://doi.org/10.1007/s10665-006-9086-6)
- Brezzi, F., Lipnikov, K. & Shashkov, M. Convergence of the Mimetic Finite Difference Method for Diffusion Problems on Polyhedral Meshes. SIAM Journal on Numerical Analysis vol. 43 1872–1896 (2005) -- [10.1137/040613950](https://doi.org/10.1137/040613950)
- Well, A. Sur les théorèmes de de Rham. Commentarii Mathematici Helvetici vol. 26 119–145 (1952) -- [10.1007/BF02564296](https://doi.org/10.1007/BF02564296)
- Whitney, H. Geometric Integration Theory. (Princeton University Press, 1957). doi:10.1515/9781400877577 -- [10.1515/9781400877577](https://doi.org/10.1515/9781400877577)
- Mixed and Hybrid Finite Element Methods. Springer Series in Computational Mathematics (Springer New York, 1991). doi:10.1007/978-1-4612-3172-1 -- [10.1007/978-1-4612-3172-1](https://doi.org/10.1007/978-1-4612-3172-1)
- Giraldo, F. X. & Warburton, T. A nodal triangle-based spectral element method for the shallow water equations on the sphere. Journal of Computational Physics vol. 207 129–150 (2005) -- [10.1016/j.jcp.2005.01.004](https://doi.org/10.1016/j.jcp.2005.01.004)
- Christiansen, S. H. & Winther, R. Smoothed projections   in finite element exterior calculus. Mathematics of Computation vol. 77 813–830 (2007) -- [10.1090/S0025-5718-07-02081-9](https://doi.org/10.1090/S0025-5718-07-02081-9)
- Munthe-Kaas, H. Z. On group Fourier analysis and symmetry preserving discretizations of PDEs. Journal of Physics A: Mathematical and General vol. 39 5563–5584 (2006) -- [10.1088/0305-4470/39/19/S14](https://doi.org/10.1088/0305-4470/39/19/S14)
- Eier, R. & Lidl, R. A class of orthogonal polynomials ink variables. Mathematische Annalen vol. 260 93–99 (1982) -- [10.1007/BF01475757](https://doi.org/10.1007/BF01475757)
- Christiansen, S. H. Foundations of Finite Element Methods for Wave Equations of Maxwell Type. Applied Wave Mathematics 335–393 (2009) doi:10.1007/978-3-642-00585-5_17 -- [10.1007/978-3-642-00585-5_17](https://doi.org/10.1007/978-3-642-00585-5_17)
- Allgower, E. L., Böhmer, K., Georg, K. & Miranda, R. Exploiting Symmetry in Boundary Element Methods. SIAM Journal on Numerical Analysis vol. 29 534–552 (1992) -- [10.1137/0729034](https://doi.org/10.1137/0729034)
- Furihata, D. Finite-difference schemes for nonlinear wave equation that inherit energy conservation property. Journal of Computational and Applied Mathematics vol. 134 37–57 (2001) -- [10.1016/S0377-0427(00)00527-6](https://doi.org/10.1016/S0377-0427(00)00527-6)
- Moler, C. & Van Loan, C. Nineteen Dubious Ways to Compute the Exponential of a Matrix. SIAM Review vol. 20 801–836 (1978) -- [10.1137/1020098](https://doi.org/10.1137/1020098)
- Norsett, S. P. An A-stable modification of the Adams-Bashforth methods. Lecture Notes in Mathematics 214–219 (1969) doi:10.1007/bfb0060031 -- [10.1007/BFb0060031](https://doi.org/10.1007/BFb0060031)
- Fässler, A. & Stiefel, E. Group Theoretical Methods and Their Applications. (Birkhäuser Boston, 1992). doi:10.1007/978-1-4612-0395-7 -- [10.1007/978-1-4612-0395-7](https://doi.org/10.1007/978-1-4612-0395-7)
- Yaguchi, T., Matsuo, T. & Sugihara, M. Conservative numerical schemes for the Ostrovsky equation. Journal of Computational and Applied Mathematics vol. 234 1036–1048 (2010) -- [10.1016/j.cam.2009.03.008](https://doi.org/10.1016/j.cam.2009.03.008)
- Hoffman, M. E. & Withers, W. D. Generalized Chebyshev polynomials associated with affine Weyl groups. Transactions of the American Mathematical Society vol. 308 91–104 (1988) -- [10.1090/S0002-9947-1988-0946432-3](https://doi.org/10.1090/S0002-9947-1988-0946432-3)
- Cox, S. M. & Matthews, P. C. Exponential Time Differencing for Stiff Systems. Journal of Computational Physics vol. 176 430–455 (2002) -- [10.1006/jcph.2002.6995](https://doi.org/10.1006/jcph.2002.6995)
- Christiansen, S. H. & Scheid, C. Convergence of a constrained finite element discretization of the Maxwell Klein Gordon equation. ESAIM: Mathematical Modelling and Numerical Analysis vol. 45 739–760 (2011) -- [10.1051/m2an/2010100](https://doi.org/10.1051/m2an/2010100)
- Koornwinder, T. H. Orthogonal polynomials in two variables which are eigenfunctions of two algebraically independent partial differential operators. I. Indagationes Mathematicae (Proceedings) vol. 77 48–58 (1974) -- [10.1016/1385-7258(74)90013-4](https://doi.org/10.1016/1385-7258(74)90013-4)
- DRONIOU, J., EYMARD, R., GALLOUËT, T. & HERBIN, R. A UNIFIED APPROACH TO MIMETIC FINITE DIFFERENCE, HYBRID FINITE VOLUME AND MIXED FINITE VOLUME METHODS. Mathematical Models and Methods in Applied Sciences vol. 20 265–295 (2010) -- [10.1142/S0218202510004222](https://doi.org/10.1142/S0218202510004222)
- Bossavit, A. Symmetry, groups, and boundary value problems. A progressive introduction to noncommutative harmonic analysis of partial differential equations in domains with geometrical symmetry. Computer Methods in Applied Mechanics and Engineering vol. 56 167–215 (1986) -- [10.1016/0045-7825(86)90119-2](https://doi.org/10.1016/0045-7825(86)90119-2)

