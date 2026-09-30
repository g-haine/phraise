---
title: "Who Breaks Early, Looses: Goal Oriented Training of Deep Neural Networks Based on Port Hamiltonian Dynamics"
date: 2023-09-21 00:00:00 +0100
permalink: who-breaks-early-looses-goal-oriented-training-of-deep-neural-networks-based-on-port-hamiltonian-dynamics
year: 2023
authors: Julian Burghoff, Marc Heinrich Monells, Hanno Gottschalk
category: proceedings
tags:
  - neural nets
  - momentum
  - goal oriented search
  - port Hamilton systems
---
 
## Authors
[Julian Burghoff](authors/julian-burghoff), [Marc Heinrich Monells](authors/marc-heinrich-monells), [Hanno Gottschalk](authors/hanno-gottschalk)
 
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
 
[Download the bib file]({{ site.baseurl }}/assets/bib/who-breaks-early-looses-goal-oriented-training-of-deep-neural-networks-based-on-port-hamiltonian-dynamics.bib)
 
## References
- Lecun Y, Bottou L, Bengio Y, Haffner P (1998) Gradient-based learning applied to document recognition. Proc IEEE 86(11):2278–2324. https://doi.org/10.1109/5.726791 -- [10.1109/5.726791](https://doi.org/10.1109/5.726791)
- Krizhevsky, A., Hinton, G.: Learning multiple layers of features from tiny images (2009)
- Xiao, H., Rasul, K., Vollgraf, R.: Fashion-MNIST: a novel image dataset for benchmarking machine learning algorithms. CoRR, vol. abs/1708.07747 (2017). arXiv: 1708.07747
- Werbos PJ (2005) Applications of advances in nonlinear sensitivity analysis. In: Lecture Notes in Control and Information Sciences. Springer-Verlag, Berlin/Heidelberg, pp 762–770 -- [10.1007/bfb0006203](https://doi.org/10.1007/bfb0006203)
- Goodfellow, I., Bengio, Y., Courville, A.: Deep Learning. MIT Press, Cambridge (2016)
- Bazaraa MS, Sherali HD, Shetty CM (2005) Nonlinear Programming. Wiley -- [10.1002/0471787779](https://doi.org/10.1002/0471787779)
- Nocedal J, Wright SJ (eds) (1999) Numerical Optimization. Springer-Verlag, New York -- [10.1007/b98874](https://doi.org/10.1007/b98874)
- Li M, Zhang T, Chen Y, Smola AJ (2014) Efficient mini-batch training for stochastic optimization. In: Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, New York, NY, USA, pp 661–670 -- [10.1145/2623330.2623612](https://doi.org/10.1145/2623330.2623612)
- Saad, D.: Online algorithms and stochastic approximations. Online Learn. 5(3), 6 (1998)
- Shalev-Shwartz S, Ben-David S (2014) Understanding Machine Learning. Cambridge University Press -- [10.1017/cbo9781107298019](https://doi.org/10.1017/cbo9781107298019)
- Becker S, Zhang Y, Lee AA (2020) Geometry of Energy Landscapes and the Optimizability of Deep Neural Networks. Phys Rev Lett 124(10):108301. https://doi.org/10.1103/physrevlett.124.108301 -- [10.1103/physrevlett.124.108301](https://doi.org/10.1103/physrevlett.124.108301)
- Nesterov, Y.: A method for unconstrained convex minimization problem with the rate of convergence o (1/$$\hat{\text{k}}$$2). In: Doklady an USSR, vol. 269, pp. 543–547 (1983)
- Goh G (2017) Why Momentum Really Works. Distill 2(4). https://doi.org/10.23915/distill.00006 -- [10.23915/distill.00006](https://doi.org/10.23915/distill.00006)
- Qian N (1999) On the momentum term in gradient descent learning algorithms. Neural Networks 12(1):145–151. https://doi.org/10.1016/s0893-6080(98)00116-6 -- [10.1016/s0893-6080(98)00116-6](https://doi.org/10.1016/s0893-6080(98)00116-6)
- Antipin, A.: Second order proximal differential systems with feedback control. Differ. Equ. 29, 1597–1607 (1993)
- Attouch H, Chbani Z, Peypouquet J, Redont P (2016) Fast convergence of inertial dynamics and algorithms with asymptotic vanishing viscosity. Math Program 168(1-2):123–175. https://doi.org/10.1007/s10107-016-0992-8 -- [10.1007/s10107-016-0992-8](https://doi.org/10.1007/s10107-016-0992-8)
- Polyack, B.: Some methods of speeding up the convergence of iterative methods. Z. Vylist Math. Fiz. 4, 1–17 (1964)
- Ochs P, Chen Y, Brox T, Pock T (2014) iPiano: Inertial Proximal Algorithm for Nonconvex Optimization. SIAM J Imaging Sci 7(2):1388–1419. https://doi.org/10.1137/130942954 -- [10.1137/130942954](https://doi.org/10.1137/130942954)
- Ochs P (2018) Local Convergence of the Heavy-Ball Method and iPiano for Non-convex Optimization. J Optim Theory Appl 177(1):153–180. https://doi.org/10.1007/s10957-018-1272-y -- [10.1007/s10957-018-1272-y](https://doi.org/10.1007/s10957-018-1272-y)
- Ochs P, Pock T (2019) Adaptive FISTA for Nonconvex Optimization. SIAM J Optim 29(4):2482–2503. https://doi.org/10.1137/17m1156678 -- [10.1137/17m1156678](https://doi.org/10.1137/17m1156678)
- [Massaroli S, Poli M, Califano F, Faragasso A, Park J, Yamashita A, Asama H (2019) Port–Hamiltonian Approach to Neural Network Training. In: 2019 IEEE 58th Conference on Decision and Control (CDC). IEEE, pp 6799–6806](port-hamiltonian-approach-to-neural-network-training) -- [10.1109/cdc40024.2019.9030017](https://doi.org/10.1109/cdc40024.2019.9030017)
- Poli, M., Massaroli, S., Yamashita, A., Asama, H., Park, J.: Port-Hamiltonian gradient flows. In: ICLR 2020 Workshop on Integration of Deep Neural Models and Differential Equations (2020)
- Kovachki, N.B., Stuart, A.M.: Continuous time analysis of momentum methods. J. Mach. Learn. Res. 22, 1–40 (2021)
- [van der Schaft A, Jeltsema D (2014) Port-Hamiltonian Systems Theory: An Introductory Overview. Foundations and Trends® in Systems and Control 1(2-3):173–378. https://doi.org/10.1561/2600000002](port-hamiltonian-systems-theory-an-introductory-overview) -- [10.1561/2600000002](https://doi.org/10.1561/2600000002)
- Bengio Y (2012) Practical Recommendations for Gradient-Based Training of Deep Architectures. In: Lecture Notes in Computer Science. Springer Berlin Heidelberg, Berlin, Heidelberg, pp 437–478 -- [10.1007/978-3-642-35289-8_26](https://doi.org/10.1007/978-3-642-35289-8_26)
- Darken, C., Moody, J.: Note on learning rate schedules for stochastic optimization. In: Advances in Neural Information Processing Systems, vol. 3 (1990)
- Darken, C., Chang, J., Moody, J., et al.: Learning rate schedules for faster stochastic gradient search. In: Neural Networks for Signal Processing, vol. 2, pp. 3–12. Citeseer (1992)
- Cabot A, Engler H, Gadat S (2009) On the long time behavior of second order differential equations with asymptotically small dissipation. Trans Amer Math Soc 361(11):5983–6017. https://doi.org/10.1090/s0002-9947-09-04785-0 -- [10.1090/s0002-9947-09-04785-0](https://doi.org/10.1090/s0002-9947-09-04785-0)
- Chambolle A, Dossal C (2015) On the Convergence of the Iterates of the “Fast Iterative Shrinkage/Thresholding Algorithm”. J Optim Theory Appl 166(3):968–982. https://doi.org/10.1007/s10957-015-0746-4 -- [10.1007/s10957-015-0746-4](https://doi.org/10.1007/s10957-015-0746-4)
- Kingma, D.P., Ba, J.: Adam: a method for stochastic optimization. arXiv preprint arXiv:1412.6980 (2014)
- Bock S, Weis M (2019) A Proof of Local Convergence for the Adam Optimizer. In: 2019 International Joint Conference on Neural Networks (IJCNN). IEEE, pp 1–8 -- [10.1109/ijcnn.2019.8852239](https://doi.org/10.1109/ijcnn.2019.8852239)
- Forrester AIJ, Sóbester A, Keane AJ (2008) Engineering Design via Surrogate Modelling. Wiley -- [10.1002/9780470770801](https://doi.org/10.1002/9780470770801)
- Paszke, A., et al.: PyTorch: an imperative style, high-performance deep learning library. In: Advances in Neural Information Processing Systems, vol. 32, pp. 8024–8035. Curran Associates Inc (2019). http://papers.neurips.cc/paper/9015- pytorch- an- imperative- style- high- performance- deeplearning- library.pdf
- He K, Zhang X, Ren S, Sun J (2016) Deep Residual Learning for Image Recognition. In: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, pp 770–778 -- [10.1109/cvpr.2016.90](https://doi.org/10.1109/cvpr.2016.90)
- Vaswani, A., et al.: Attention is all you need. In: Advances in Neural Information Processing Systems, vol. 30 (2017)
- Islam MR, Matin A (2020) Detection of COVID 19 from CT Image by The Novel LeNet-5 CNN Architecture. In: 2020 23rd International Conference on Computer and Information Technology (ICCIT). IEEE, pp 1–5 -- [10.1109/iccit51783.2020.9392723](https://doi.org/10.1109/iccit51783.2020.9392723)

