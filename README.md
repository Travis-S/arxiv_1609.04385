This repository provides the paper source code and some data files for the paper

**Behavior of the Maximum Likelihood in Quantum State Tomography**

_Travis L Scholten_ and _Robin Blume-Kohout_<br>
Center for Computing Research (CCR), Sandia National Labs<br>
Center for Quantum Information and Control, University of New Mexico

The most recent arXiv version is available [here](????).

If you find our work useful to you, please consider citing

```
@article{scholten2016,
  title={Behavior of the Maximum Likelihood in Quantum State Tomography},
  author={Scholten, Travis and Blume-Kohout, Robin},
  archivePrefix = {arXiv},
    arxivId = {????},
  year={2016}
}
```
Abstract
-----------
Quantum state tomography on a d-dimensional system demands resources that grow rapidly with d. Model selection can be used to tailor the number of fit parameters to the data, but quantum tomography violates some common assumptions that underly canonical model selection techniques based on ratios of maximum likelihoods (loglikelihood ratio statistics), due to the nature of the state space boundaries. Here, we study the behavior of the maximum likelihood  in different Hilbert space dimensions, and derive an expression for a complexity penalty -- the expected value of the loglikelihood ratio statistic (roughly, the logarithm of the maximum likelihood) -- that can be used to make an appropriate choice for d.

Summary
----------
This paper investigates a problem in _quantum state tomography_, a statistical inference process used to estimate quantum states. The resources required to estimate  a quantum state can grow very quickly, which means we need to find ways of using fewer resources. Some techniques to do so go by the name of ``statistical model selection". In this paper, we investigated how the behavior of a particular model selection technique (based on loglikelihood ratio statistics) behaves in the context of state tomography. This technique relies on a result known as the _Wilks Theorem_. Surprisingly, the Wilks Theorem breaks down in state tomography, in part because the  state space has _boundaries_ which violate some of the assumptions of the Theorem. In turn, this means model selection techniques based on loglikelihood ratio statistics might not work very well.

To help remedy this, we constructed a new theory for loglikelihood ratio statistics and their behavior in state tomography. Numerical simulations verify our theory works reasonably well, and dramatically improves upon the Wilks Theorem. We applied our result to a particular kind of  state tomography (that of states of light), and found our result performs well in predicting some of the properties of loglikelihood ratio statistics. This work lays the foundation for developing a model selection technique based on loglikelihood ratio statistics which is accurate in state tomography.

Use of Code/Data
---------

**Paper Source**

If you'd like to download or modify the text of our paper, you may do so. If you find typos or other improvements,
feel free to [email me](mailto:travisscholten@gmail.com) or open an issue on this repository. As of now, I anticipate adding acknowledgments to each person who helps improve the paper.

**Data**

In the ``Data`` directory, you'll find several csv files which contain some of the data used to generate the figures in our paper. Below is a description of the data files, and the related figures. See ``Data/README_data.md`` for more information, such as descriptions of the data, what it is, as well as variable names.

The data files in that directory are sufficient to reproduce the Figures 1, 2, 3, 4, 7, 8, 9, 10, and 11.

**Figure Generation Code**

At this time, we are unable to provide code which would use the data to make the figures.

Updates
------------

This repository will be updated each time a new version is posted to the arXiv. I plan to use git tags to keep track of the appropriate versions here. (Thus tag `v1` corresponds to the first version on the arXiv, `v2` to the second, and so on.)

License
----------
