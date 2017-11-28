This repository provides the paper source code and some data files for the paper

**Behavior of the Maximum Likelihood in Quantum State Tomography**

_Travis L Scholten_ and _Robin Blume-Kohout_<br>
Center for Computing Research (CCR), Sandia National Labs<br>
Center for Quantum Information and Control, University of New Mexico

This paper is available on the arXiv, at ID [1609.04385](http://arxiv.org/abs/1609.04385).

If you find this work useful to you, please consider citing

```
@article{[citation key],
  title={Behavior of the Maximum Likelihood in Quantum State Tomography},
  author={Scholten, Travis and Blume-Kohout, Robin},
  arxivId = {1609.04385},
  year={2016}
}
```

NOTE: The current version of the files in this repository is behind the version on the arXiv. I am working to update these files as soon as possible.

Abstract
-----------
Quantum state tomography on a $d$-dimensional system demands resources that grow rapidly with $d$. They may be reduced by using model selection to tailor the number of parameters in the model (i.e., the size of the density matrix).  Most model selection methods typically rely on a test statistic and a null theory that describes its behavior when two models are equally good. Here, we consider the loglikelihood ratio.  Because of the positivity constraint $\rho \geq 0$, quantum state space does not generally satisfy local asymptotic normality, meaning the classical null theory for the loglikelihood ratio (the Wilks theorem) should not be used.  Thus, understanding and quantifying how positivity affects the null behavior of this test statistic is necessary for its use in model selection for state tomography.  We define a new generalization of local asymptotic normality, metric-projected local asymptotic normality, show that quantum state space satisfies it, and derive a replacement for the Wilks theorem. In addition to enabling reliable model selection, our results shed more light on the qualitative effects of the positivity constraint on state tomography.

Summary
----------
This paper investigates a problem in _quantum state tomography_, which is the task of inferring an unknown quantum state. The resources required to estimate  a quantum state can grow very quickly, which means we need to find ways of using fewer resources. Some techniques to do so go by the name of ``statistical model selection". In this paper, we investigated how the behavior of a particular model selection technique (based on the loglikelihood ratio statistic) behaves in the context of state tomography. This technique relies on a result known as the _Wilks Theorem_. Surprisingly, the Wilks Theorem breaks down in state tomography, because state space has _boundaries_ which violate some of the assumptions of the theorem. In turn, this means model selection techniques based on the loglikelihood ratio statistic might not work very well.

To help remedy this, we (a) constructed a new framework for reasoning about the asymptotic properties of models, by generalizing [Local Asymptotic Normality](https://en.wikipedia.org/wiki/Local_asymptotic_normality) to the case of models with convex constraints, which we call "Metric-Projected Local Asymptotic Normality" (MP-LAN), and (b) used the new framework to develop a new theory for the loglikelihood ratio statistic and its behavior in state tomography. Numerical simulations verify our theory works reasonably well, and dramatically improves upon the Wilks Theorem. We applied our result to a particular kind of  state tomography (that of states of light), and found our result performs well in predicting some of the properties of the loglikelihood ratio statistic. This work lays the foundation for developing a model selection technique based on the loglikelihood ratio statistic which is accurate in state tomography.

![Our main result - a replacement for the Wilks Theorem](arxiv_1609.04385/Images/Figure_3.pdf)

Use of Code/Data
---------

**Paper Source**

If you'd like to download and use the text of our paper, you may do so. If you find typos or other improvements,
feel free to [email me](mailto:travisscholten@protonmail.com) or open an issue on this repository. As of now, I anticipate adding acknowledgments to each person who helps improve the paper.

**Data**

In the ``Data`` directory, you'll find several csv files which contain some of the data used to generate the figures in our paper. See ``Data/README.md`` for more information, such as descriptions of the data, what it is, as well as variable names.

The data files in that directory are sufficient to reproduce Figures 1 through 13.

**Figure Generation Code**

The Jupyter notebook ``Supplemental_NB-I.ipynb`` contains code necessary to reproduce Figures 1 through 13.

**Images**

Within the ``Images`` directory you will find PDF files for each image in the paper. If you find them useful, please let me know.

**Making the Paper**

Included in this repository is a Makefile which automates compiling the paper. Typing ``make`` in your command line should trigger the compilation process.

Updates
------------

This repository will be updated each time a new version is posted to the arXiv. I plan to use tags to keep track of the appropriate versions here. (Thus tag `v1` corresponds to the first version on the arXiv, `v2` to the second, and so on.)
