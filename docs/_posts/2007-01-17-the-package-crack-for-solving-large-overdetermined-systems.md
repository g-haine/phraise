---
title: "The package CRACK for solving large overdetermined systems"
date: 2007-01-17 00:00:00 +0100
permalink: the-package-crack-for-solving-large-overdetermined-systems
year: 2005
authors: Thomas Wolf
category: articles
---
 
## Authors
[Thomas Wolf](authors/thomas-wolf)
 
## Abstract
The program CRACK is a computer algebra package written in REDUCE for the solution of over-determined systems of algebraic, ordinary or partial differential equations with at most polynomial non-linearity. It is available as part of version 3.8 of the REDUCE system (dated April 2004) and the latest development version can be downloaded from http://lie.math.brocku.ca/crack/. The purpose of this poster is to accompany a software demonstration of CRACK at ISSAC 2005. The poster is supposed to give a graphical overview of CRACK, emphasizing features which are special to the package. Those are &amp;bull; a rich interface, with visualization aids for inspecting large systems, including - for each equation its properties, history and investigations that have already been done with the equation, - the occurrence of all derivatives of selected functions in any equation, - a statistical overview of the system (number of equations and functions in dependence of number of independent variables), - a matrix display of occurrences of unknown constants/functions in all equations, - a count of the total number of appearances of each unknown, - the determination of not under-determined subsystems, - a listing of all sub- and sub-sub-.. cases investigated so far, with their assumptions, number of steps and number of solutions, - graphical displays of size related measures of the computation done so far; &amp;bull; a discussion of possibilities to trade interactively or automatically the speed of the solution process versus safety (avoidance of expression swell): - only length-reducing versus complete Gr&amp;ouml;bner basis computation steps. - substitutions in shorter equations only, i.e. only in a sub-system versus substitutions in the complete system, - growth bounded substitutions versus general substitutions, - case splittings (induced by factorizations, substitutions with potentially vanishing coefficients or adhoc case distinctions) versus Gr&amp;ouml;bner basis steps, - an investment in the length reduction of equations to reach sparse systems with multiple benefits; &amp;bull; algorithmic extensions which include - the ability to collect and apply syzygies which result as a by-product in the process of computing a differential Gr&amp;ouml;bner basis to integrate linear PDEs. - the treatment of inequalities: their usage, active collection and derivation, and their constant update in an ongoing reduction process based on newly derived equations. - the capability added by Winfried Neun (ZIB Berlin) to run in a truly parallel mode on a beowulf cluster, recently also ported to 64bit AMD processors. - post-computation procedures, especially the possibility to merge solutions of parametric linear algebraic systems and to automate the production of web-pages for solutions that are found. - the ability to separate expressions with respect to independent variables which occur polynomially but with variable exponents, leading to automatically investigated case distinctions of exponents being equal or not; &amp;bull; safety enhancing measures as - the ability to backup and re-load the whole session, - the automatic storing of the complete keyboard input during a session with the opportunity to feed this stored input into a new session, - the possibility to impose time restrictions of notoriously slow sub-steps, like factorizations and sometimes the computation and reduction of S-polynomials in a Gr&amp;ouml;bner basis computations, - a method to interrupt an ongoing automatic computation and change it to interactive mode The poster in landscape format will display the above four topics in boxes. For some of the sub-items above a screen output will give a visual impression, like the matrix indicating occurrences of unknowns in equations. In the following publications the solution of large overdetermined systems was a crucial ingredient: &amp;bull; the solution of large bi-linear algebraic systems and automatic merging of obtained solutions: - Wolf, T., Efimovskaya, O. V.: Classification of integrable quadratic Hamiltonians on e(3), Regular and Chaotic Dynamics, vol 8, no 2 (2003), p 155--162. - Sokolov, V. V., Wolf, T.: Classification of integrable polynomial vector evolution equations, J. Phys. A: Math. Gen. 34 (2001) 11139--11148. - Tsuchida, T. and Wolf, T.: Classification of integrable coupled systems with one scalar and one vector unknown, preprint nlin.SI/0412003 (2004) 60 pages, to appear in J. Phys. A: Math. Gen. - Sokolov, V. V. and Wolf, T.: Integrable quadratic Hamiltonians on &lt;i&gt;so&lt;/i&gt;(4) and &lt;i&gt;so&lt;/i&gt;(3, 1), preprint (2004) 16 pages, nlin.SI/0405066. - Kiselev, A. and Wolf, T.: New recursive chains of N=1 homogeneous superequations, to appear in proceedings of "Symmetry in Nonlinear Mathematical Physics", Kyiv 2005. &amp;bull; the solution of extensive overdetermined ODE/PDE-systems: - Anco, S. and Wolf, T.: Some symmetry classifications of hyperbolic vector evolution equations, nlin.SI/0412015, JNMP, Volume 12, Supplement 1 (2005), p 13--31.
 
## Citation
- **Journal:** ACM SIGSAM Bulletin
- **Year:** 2005
- **Volume:** 39
- **Issue:** 3
- **Pages:** 95--96
- **Publisher:** Association for Computing Machinery (ACM)
- **DOI:** [10.1145/1113439.1113455](https://doi.org/10.1145/1113439.1113455)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@article{Wolf_2005,
  title={{The package CRACK for solving large overdetermined systems}},
  volume={39},
  ISSN={0163-5824},
  DOI={10.1145/1113439.1113455},
  number={3},
  journal={ACM SIGSAM Bulletin},
  publisher={Association for Computing Machinery (ACM)},
  author={Wolf, Thomas},
  year={2005},
  pages={95--96}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/the-package-crack-for-solving-large-overdetermined-systems.bib)
 
