"""
Some filterers implemented as transformers for convenience
"""

from __future__ import print_function

from sklearn.base import TransformerMixin
from sklearn.neighbors import KernelDensity
import numpy as np


class KernelDensityFilterer(KernelDensity, TransformerMixin):
    """ Minimal wrapper of scikit-learn KernelDensity
    estimator to use it as a coverer (i.e. Transformer API)

    """

    def transform(self, X, y=None):
        """ Returns probability density estimation for each sample

        Parameters
        ----------
        X: array-like, shape=(n_samples, n_features)
          Data for KDE.

        Returns
        -------
        kde: array-like, shape=(n_samples, 1)
          Array with KDE probabilities for each sample

        """

        return np.exp(self.score_samples(X)[:, np.newaxis])
