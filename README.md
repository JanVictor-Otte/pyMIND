# PyMIND

This implements *MultIscale Nemirowski-Dantzig (MIND)* estimator in nonparametric regression (or denoising). It is a translation of the Matlab package provided by [H. Li](https://github.com/housenli/MIND). 
MIND minimizes a general regularization term under certain multiscale constraints in terms of dictionaries. It is a collection of methods, includes 
-  Haltmeier, M., Li, H., & Munk, A. (2021+). A variational view on statistical multiscale estimation. Annual Review of Statistics and Its Application, to appear (arXiv preprint [arXiv:2106.05828](https://arxiv.org/abs/2106.05828))
-  del Alamo, M., Li, H., & Munk, A. (2021). Frame-constrained total variation regularization for white noise regression. The Annals of Statistics, to appear (arXiv preprint [arXiv:1807.02038](https://arxiv.org/abs/1807.02038)).
-  Grasmair, M., Li, H., & Munk, A. (2018). Variational multiscale nonparametric regression: Smooth functions. In Annales de l'Institut Henri Poincaré, Probabilités et Statistiques ([Vol. 54, No. 2, pp. 1058-1097](https://projecteuclid.org/euclid.aihp/1524643240)). Institut Henri Poincaré.
- Frick, K., Marnitz, P., & Munk, A. (2013). Statistical multiresolution estimation for variational imaging: with an application in Poisson-biophotonics. Journal of Mathematical Imaging and Vision, [46(3), 370-387](https://link.springer.com/article/10.1007/s10851-012-0368-5).
- Frick, K., Marnitz, P., & Munk, A. (2012). Statistical multiresolution Dantzig estimation in imaging: Fundamental concepts and algorithmic framework. Electronic Journal of Statistics, [6, 231-268](https://projecteuclid.org/euclid.aihp/1524643240).

The implementation works exclusively for 2D grayscale images, and utilizes the [Chambolle-Pock algorithm](https://link.springer.com/article/10.1007/s10851-010-0251-1). For more details, please see 

\[1\] del Alamo, M., Li, H., Munk, A., & Werner, F. (2020). Variational multiscale nonparametric regression: Algorithms and implementation. Algorithms, [13(11), 296](https://doi.org/10.3390/a13110296).

## Installation
The codes require the following package not available on PyPI:
- **pyShearlab** from https://github.com/stefanloock/pyshearlab

It can be installed via:

    pip install https://github.com/stefanloock/pyshearlab/archive/master.zip

To install this package change into its folder and run:

    pip install -r requirements.txt
    python setup.py install

Don't forget to add the root folder to your PYTHONPATH.

## Example

Examples, as well as experiments in the paper \[1\], can be run with the file [example.py](https://gitlab.gwdg.de/hli1/pymind/-/blob/master/example.py). 

## Acknowledgement

The codes for proximity operator of total variation seminorm are built from those by [Markus Grasmair](https://www.ntnu.edu/employees/markus.grasmair) (NTNU).
The encapsule of Wavelet class is from [Michael Lustig](https://www2.eecs.berkeley.edu/Faculty/Homepages/mlustig.html) (UC Berkeley). The codes for one approach of noise level estimation is from [Masayuki Tanaka](http://www.ok.sc.e.titech.ac.jp/~mtanaka/) (Tokyo Institute of Technology).
