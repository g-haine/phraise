---
layout: post
title: "Port–Hamiltonian Approach to Neural Network Training"
date: 2020-03-13 00:00:00 +0100
permalink: port-hamiltonian-approach-to-neural-network-training
year: 2019
authors: Stefano Massaroli, Michael Poli, Federico Califano, Angela Faragasso, Jinkyoo Park, Atsushi Yamashita, Hajime Asama
category: proceedings
---
 
## Authors
[Stefano Massaroli](authors/stefano-massaroli), [Michael Poli](authors/michael-poli), [Federico Califano](authors/federico-califano), [Angela Faragasso](authors/angela-faragasso), [Jinkyoo Park](authors/jinkyoo-park), [Atsushi Yamashita](authors/atsushi-yamashita), [Hajime Asama](authors/hajime-asama)
 
## Abstract
Neural networks are discrete entities: subdivided into discrete layers and parametrized by weights which are iteratively optimized via difference equations. Recent work proposes networks with layer outputs which are no longer quantized but are solutions of an ordinary differential equation (ODE); however, these networks are still optimized via discrete methods (e.g. gradient descent). In this paper, we explore a different direction: namely, we propose a novel framework for learning in which the parameters themselves are solutions of ODEs. By viewing the optimization process as the evolution of a port-Hamiltonian system, we can ensure convergence to a minimum of the objective function. Numerical experiments have been performed to show the validity and effectiveness of the proposed methods.
 
## Citation
- **Journal:** 2019 IEEE 58th Conference on Decision and Control (CDC)
- **Year:** 2019
- **Volume:** 
- **Issue:** 
- **Pages:** 6799--6806
- **Publisher:** IEEE
- **DOI:** [10.1109/cdc40024.2019.9030017](https://doi.org/10.1109/cdc40024.2019.9030017)
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inproceedings{Massaroli_2019,
  title={{Port–Hamiltonian Approach to Neural Network Training}},
  DOI={10.1109/cdc40024.2019.9030017},
  booktitle={{2019 IEEE 58th Conference on Decision and Control (CDC)}},
  publisher={IEEE},
  author={Massaroli, Stefano and Poli, Michael and Califano, Federico and Faragasso, Angela and Park, Jinkyoo and Yamashita, Atsushi and Asama, Hajime},
  year={2019},
  pages={6799--6806}
}
{% endraw %}
{% endhighlight %}
 
[Download the bib file]({{ site.baseurl }}/assets/bib/port-hamiltonian-approach-to-neural-network-training.bib)
 
## References
- eldan, The power of depth for feedforward neural networks. Conference on Learning Theory (2016)
- Neural Information Processing. Lecture Notes in Computer Science (Springer International Publishing, 2017). doi:10.1007/978-3-319-70139-4 -- [10.1007/978-3-319-70139-4](https://doi.org/10.1007/978-3-319-70139-4)
- The Duffing Equation. (2011) doi:10.1002/9780470977859 -- [10.1002/9780470977859](https://doi.org/10.1002/9780470977859)
- Goebel, R., Sanfelice, R. G. & Teel, A. R. Hybrid dynamical systems. IEEE Control Syst. 29, 28–93 (2009) -- [10.1109/mcs.2008.931718](https://doi.org/10.1109/mcs.2008.931718)
- li, Visualizing the loss landscape of neural nets. Advances in neural information processing systems (2018)
- blum, Training a 3-node neural network is np-complete. Advances in neural information processing systems (1989)
- [Maschke, B. M. & van der Schaft, A. J. Port-Controlled Hamiltonian Systems: Modelling Origins and Systemtheoretic Properties. IFAC Proceedings Volumes 25, 359–365 (1992)](port-controlled-hamiltonian-systems-modelling-origins-and-systemtheoretic-properties) -- [10.1016/s1474-6670(17)52308-3](https://doi.org/10.1016/s1474-6670(17)52308-3)
- duindam, Modeling and control of complex physical systems: the port-Hamiltonian approach. (2009)
- [van der Schaft, A. & Jeltsema, D. Port-Hamiltonian Systems Theory: An Introductory Overview. FnT in Systems and Control 1, 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Putting energy back in control. IEEE Control Syst. 21, 18–33 (2001) -- [10.1109/37.915398](https://doi.org/10.1109/37.915398)
- [Ortega, R., van der Schaft, A., Maschke, B. & Escobar, G. Interconnection and damping assignment passivity-based control of port-controlled Hamiltonian systems. Automatica 38, 585–596 (2002)](interconnection-and-damping-assignment-passivity-based-control-of-port-controlled-hamiltonian-systems) -- [10.1016/s0005-1098(01)00278-3](https://doi.org/10.1016/s0005-1098(01)00278-3)
- [Ortega, R., van der Schaft, A., Castanos, F. & Astolfi, A. Control by Interconnection and Standard Passivity-Based Control of Port-Hamiltonian Systems. IEEE Trans. Automat. Contr. 53, 2527–2542 (2008)](control-by-interconnection-and-standard-passivity-based-control-of-port-hamiltonian-systems) -- [10.1109/tac.2008.2006930](https://doi.org/10.1109/tac.2008.2006930)
- chen, Neural ordinary differential equations. Advances in neural information processing systems (2018)
- ruthotto, Deep neural networks motivated by partial differential equations. (2018)
- krogh, A simple weight decay can improve generalization. Advances in neural information processing systems (1992)
- brock, Large scale gan training for high fidelity natural image synthesis. (2018)
- Golub, G. H., Hansen, P. C. & O’Leary, D. P. Tikhonov Regularization and Total Least Squares. SIAM J. Matrix Anal. &amp; Appl. 21, 185–194 (1999) -- [10.1137/s0895479897326432](https://doi.org/10.1137/s0895479897326432)
- He, K., Gkioxari, G., Dollar, P. & Girshick, R. Mask R-CNN. 2017 IEEE International Conference on Computer Vision (ICCV) (2017) doi:10.1109/iccv.2017.322 -- [10.1109/iccv.2017.322](https://doi.org/10.1109/iccv.2017.322)
- devlin, Bert:Pre-training of deep bidirectional transformers for language understanding. (2018)
- van der Schaft, A. & Schumacher, H. An Introduction to Hybrid Dynamical Systems. Lecture Notes in Control and Information Sciences (Springer London, 2000). doi:10.1007/bfb0109998 -- [10.1007/bfb0109998](https://doi.org/10.1007/bfb0109998)
- He, K., Zhang, X., Ren, S. & Sun, J. Deep Residual Learning for Image Recognition. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2016) doi:10.1109/cvpr.2016.90 -- [10.1109/cvpr.2016.90](https://doi.org/10.1109/cvpr.2016.90)
- tieleman, Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude. COURSERA Neural Networks for Machine Learning (2012)
- kingma, Adam: A method for stochastic optimization. International Conference on Learning Representations ICLR 2015 (2015)
- Rumelhart, D. E., Hinton, G. E. & Williams, R. J. Learning Internal Representations by Error Propagation. http://dx.doi.org/10.21236/ADA164453 (1985) doi:10.21236/ada164453 -- [10.21236/ada164453](https://doi.org/10.21236/ada164453)
- liu, On the variance of the adaptive learning rate and beyond. (2019)
- Hornik, K., Stinchcombe, M. & White, H. Multilayer feedforward networks are universal approximators. Neural Networks 2, 359–366 (1989) -- [10.1016/0893-6080(89)90020-8](https://doi.org/10.1016/0893-6080(89)90020-8)
- greydanus, Hamiltonian neural networks. (2019)
- howse, Gradient and hamiltonian dynamics applied to learning in neural networks. Advances in neural information processing systems (1996)
- Chaudhari, P., Oberman, A., Osher, S., Soatto, S. & Carlier, G. Deep relaxation: partial differential equations for optimizing deep neural networks. Res Math Sci 5, (2018) -- [10.1007/s40687-018-0148-y](https://doi.org/10.1007/s40687-018-0148-y)
- Ackley, D. H., Hinton, G. E. & Sejnowski, T. J. A Learning Algorithm for Boltzmann Machines*. Cognitive Science 9, 147–169 (1985) -- [10.1207/s15516709cog0901_7](https://doi.org/10.1207/s15516709cog0901_7)
- Sienko, W., Citko, W. & Jakóbczak, D. Learning and System Modeling via Hamiltonian Neural Networks. Lecture Notes in Computer Science 266–271 (2004) doi:10.1007/978-3-540-24844-6_36 -- [10.1007/978-3-540-24844-6_36](https://doi.org/10.1007/978-3-540-24844-6_36)
- moon, Theory of holors: A generalization of tensors. (2005)
- Hopfield, J. J. Neural networks and physical systems with emergent collective computational abilities. Proc. Natl. Acad. Sci. U.S.A. 79, 2554–2558 (1982) -- [10.1073/pnas.79.8.2554](https://doi.org/10.1073/pnas.79.8.2554)

