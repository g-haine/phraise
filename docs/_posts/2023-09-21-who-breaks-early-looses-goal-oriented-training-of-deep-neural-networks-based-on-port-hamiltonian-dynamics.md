---
layout: post
title: "Who Breaks Early, Looses: Goal Oriented Training of Deep Neural Networks Based on Port Hamiltonian Dynamics"
date: 2023-09-21 00:00:00 +0100
permalink: who-breaks-early-looses-goal-oriented-training-of-deep-neural-networks-based-on-port-hamiltonian-dynamics
year: 2023
authors: Julian Burghoff, Marc Heinrich Monells, Hanno Gottschalk
category: book-chapter
tag: neural nets; momentum; goal oriented search; port Hamilton systems
---
 
## Authors
**Julian Burghoff, Marc Heinrich Monells, Hanno Gottschalk**
 
## Abstract
The highly structured energy landscape of the loss as a function of parameters for deep neural networks makes it necessary to use sophisticated optimization strategies in order to discover (local) minima that guarantee reasonable performance. Overcoming less suitable local minima is an important prerequisite and often momentum methods are employed to achieve this. As in other non local optimization procedures, this however creates the necessity to balance between exploration and exploitation. In this work, we suggest an event based control mechanism for switching from exploration to exploitation based on reaching a predefined reduction of the loss function. As we give the momentum method a port Hamiltonian interpretation, we apply the ’heavy ball with friction’ interpretation and trigger breaking (or friction) when achieving certain goals. We benchmark our method against standard stochastic gradient descent and provide experimental evidence for improved performance of deep neural networks when our strategy is applied.
 
## Keywords
neural nets; momentum; goal oriented search; port Hamilton systems
 
## Citation
- **ISBN:** 9783031442032
- **Publisher:** Springer Nature Switzerland
- **DOI:** [10.1007/978-3-031-44204-9_38](https://doi.org/10.1007/978-3-031-44204-9_38)
- **Note:** International Conference on Artificial Neural Networks
 
## BibTeX
{% highlight bibtex %}
{% raw %}
@inbook{Burghoff_2023,
  title={{Who Breaks Early, Looses: Goal Oriented Training of Deep Neural Networks Based on Port Hamiltonian Dynamics}},
  ISBN={9783031442049},
  ISSN={1611-3349},
  DOI={10.1007/978-3-031-44204-9_38},
  booktitle={{Artificial Neural Networks and Machine Learning – ICANN 2023}},
  publisher={Springer Nature Switzerland},
  author={Burghoff, Julian and Monells, Marc Heinrich and Gottschalk, Hanno},
  year={2023},
  pages={454--465}
}
{% endraw %}
{% endhighlight %}
 
## References
- LeCun, Y., Bottou, L., Bengio, Y., Haffner, P.: Gradient-based learning applied to document recognition. Proc. IEEE 86(11), 2278–2324 (1998) -- [10.1109/5.726791](https://doi.org/10.1109/5.726791)
- Krizhevsky, A., Hinton, G.: Learning multiple layers of features from tiny images (2009)
- Xiao, H., Rasul, K., Vollgraf, R.: Fashion-MNIST: a novel image dataset for benchmarking machine learning algorithms. CoRR, vol. abs/1708.07747 (2017). arXiv: 1708.07747
- Werbos, P.J.: Applications of advances in nonlinear sensitivity analysis. In: Drenick, R.F., Kozin, F. (eds.) System Modeling and Optimization. Lecture Notes in Control and Information Sciences, vol. 38, pp. 762–770. Springer, Heidelberg (2005). https://doi.org/10.1007/BFb0006203 -- [10.1007/BFb0006203](https://doi.org/10.1007/BFb0006203)
- Goodfellow, I., Bengio, Y., Courville, A.: Deep Learning. MIT Press, Cambridge (2016)
- Bazaraa, M.S., Sherali, H.D., Shetty, C.M.: Nonlinear Programming - Theory and Algorithms, 3rd edn. Wiley, Hoboken (2006) -- [10.1002/0471787779](https://doi.org/10.1002/0471787779)
- Wright, S., Nocedal, J., et al.: Numerical Optimization, vol. 35, no. 67–68, p. 7. Springer, New York (1999) -- [10.1007/b98874](https://doi.org/10.1007/b98874)
- Li, M., Zhang, T., Chen, Y., Smola, A.J.: Efficient mini-batch training for stochastic optimization. In: Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 661–670 (2014) -- [10.1145/2623330.2623612](https://doi.org/10.1145/2623330.2623612)
- Saad, D.: Online algorithms and stochastic approximations. Online Learn. 5(3), 6 (1998)
- Shalev-Shwartz, S., Ben-David, S.: Understanding Machine Learning: From Theory to Algorithms. Cambridge University Press, Cambridge (2014) -- [10.1017/CBO9781107298019](https://doi.org/10.1017/CBO9781107298019)
- Becker, S., Zhang, Y.: Geometry of energy landscapes and the optimizability of deep neural networks. Phys. Rev. Lett. 124(10), 108301 (2020) -- [10.1103/PhysRevLett.124.108301](https://doi.org/10.1103/PhysRevLett.124.108301)
- Nesterov, Y.: A method for unconstrained convex minimization problem with the rate of convergence o (1/$$\hat{	ext{k}}$$2). In: Doklady an USSR, vol. 269, pp. 543–547 (1983)
- Goh, G.: Why momentum really works. Distill 2(4), e6 (2017) -- [10.23915/distill.00006](https://doi.org/10.23915/distill.00006)
- Qian, N.: On the momentum term in gradient descent learning algorithms. Neural Netw. 12(1), 145–151 (1999) -- [10.1016/S0893-6080(98)00116-6](https://doi.org/10.1016/S0893-6080(98)00116-6)
- Antipin, A.: Second order proximal differential systems with feedback control. Differ. Equ. 29, 1597–1607 (1993)
- Attouch, H., Chbani, Z., Peypouquet, J., Redont, P.: Fast convergence of inertial dynamics and algorithms with asymptotic vanishing viscosity. Math. Program. 168, 123–175 (2018) -- [10.1007/s10107-016-0992-8](https://doi.org/10.1007/s10107-016-0992-8)
- Polyack, B.: Some methods of speeding up the convergence of iterative methods. Z. Vylist Math. Fiz. 4, 1–17 (1964)
- Ochs, P., Chen, Y., Brox, T., Pock, T.: IPiano: inertial proximal algorithm for non-convex optimization. SIAM J. Imag. Sci. 7, 1388–1419 (2014) -- [10.1137/130942954](https://doi.org/10.1137/130942954)
- Ochs, P.: Local convergence of the heavy-ball method and iPiano for nonconvex optimization. J. Optim. Theory Appl. 177, 153–180 (2018) -- [10.1007/s10957-018-1272-y](https://doi.org/10.1007/s10957-018-1272-y)
- Ochs, P., Pock, T.: Adaptive FISTA for non-convex optimization. SIAM J. Optim. 29, 2482–2503 (2019) -- [10.1137/17M1156678](https://doi.org/10.1137/17M1156678)
- Massaroli, S., et al.: Port-Hamiltonian approach to neural network training. In: 2019 IEEE 58th Conference on Decision and Control (CDC), IEEE, pp. 6799–6806 (2019) -- [10.1109/CDC40024.2019.9030017](https://doi.org/10.1109/CDC40024.2019.9030017)
- Poli, M., Massaroli, S., Yamashita, A., Asama, H., Park, J.: Port-Hamiltonian gradient flows. In: ICLR 2020 Workshop on Integration of Deep Neural Models and Differential Equations (2020)
- Kovachki, N.B., Stuart, A.M.: Continuous time analysis of momentum methods. J. Mach. Learn. Res. 22, 1–40 (2021)
- [Van Der Schaft, A., Jeltsema, D.: Port-Hamiltonian systems theory: an introductory overview. Found. Trends® Syst. Control 1(2–3), 173–378 (2014)](port-hamiltonian-systems-theory-an-introductory-overview-journal) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Bengio, Y.: Practical recommendations for gradient-based training of deep architectures. In: Montavon, G., Orr, G.B., Müller, K.-R. (eds.) Neural Networks: Tricks of the Trade. LNCS, vol. 7700, pp. 437–478. Springer, Heidelberg (2012). https://doi.org/10.1007/978-3-642-35289-8_26 -- [10.1007/978-3-642-35289-8_26](https://doi.org/10.1007/978-3-642-35289-8_26)
- Darken, C., Moody, J.: Note on learning rate schedules for stochastic optimization. In: Advances in Neural Information Processing Systems, vol. 3 (1990)
- Darken, C., Chang, J., Moody, J., et al.: Learning rate schedules for faster stochastic gradient search. In: Neural Networks for Signal Processing, vol. 2, pp. 3–12. Citeseer (1992)
- Cabot, A., Engler, H., Gadta, S.: On the long time behavior of second order differential equations with asymptotically small dissipation. Trans. Am. Math. Soc. 361, 5983–6017 (2009) -- [10.1090/S0002-9947-09-04785-0](https://doi.org/10.1090/S0002-9947-09-04785-0)
- Chambolle, A., Dossal, C.: On the convergence of the iterates of the “fast iterative shrinkage/thresholding algorithm". J. Optim. Theory Appl. 166, 968–982 (2015). https://doi.org/10.1007/s10957-015-0746-4 -- [10.1007/s10957-015-0746-4](https://doi.org/10.1007/s10957-015-0746-4)
- Kingma, D.P., Ba, J.: Adam: a method for stochastic optimization. arXiv preprint arXiv:1412.6980 (2014)
- Bock, S., Weiß, M.: A proof of local convergence for the Adam optimizer. In: International Joint Conference on Neural Networks (IJCNN), pp. 1–8. IEEE (2019) -- [10.1109/IJCNN.2019.8852239](https://doi.org/10.1109/IJCNN.2019.8852239)
- Forrester, A., Sobester, A., Keane, A.: Engineering Design Via Surrogate Modelling: A Practical Guide. Wiley, Hoboken (2008) -- [10.1002/9780470770801](https://doi.org/10.1002/9780470770801)
- Paszke, A., et al.: PyTorch: an imperative style, high-performance deep learning library. In: Advances in Neural Information Processing Systems, vol. 32, pp. 8024–8035. Curran Associates Inc (2019). http://papers.neurips.cc/paper/9015- pytorch- an- imperative- style- high- performance- deeplearning- library.pdf
- He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 770–778 (2016) -- [10.1109/CVPR.2016.90](https://doi.org/10.1109/CVPR.2016.90)
- Vaswani, A., et al.: Attention is all you need. In: Advances in Neural Information Processing Systems, vol. 30 (2017)
- Islam, M.R., Matin, A.: Detection of COVID 19 from CT image by the novel LeNet-5 CNN architecture. In: 2020 23rd International Conference on Computer and Information Technology (ICCIT), IEEE, pp. 1–5 (2020) -- [10.1109/ICCIT51783.2020.9392723](https://doi.org/10.1109/ICCIT51783.2020.9392723)

