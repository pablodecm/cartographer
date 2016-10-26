"""
Coverers of the filtrated space
"""
from sklearn.base import BaseEstimator


class HyperRectangleCoverer(BaseEstimator):
    """ Covers the space using overlapping hyperectangles

    Parameters
    ----------

    intervals: integer or list of integers
      number of intervals in each filtered space dimension, if an integer
      is specified the same number is used in all dimensions.

    overlap: float or list of floats
      fraction of overlap between hyperectangles in each space dimension,
      if a single float is specified the same overlap is used in all
      dimensions.


    Attributes
    ----------

    """

    def __init__(self, intervals, overlap):
        self.intervals = intervals
        self.overlap = overlap

    def fit(X, y=None):
        """ Creates the space covering for the input data

        It creates a hyperectangle covering of the multidimensional space of X.

        Parameters
        ----------
        X: array-like, shape=(n_samples, n_features)
          Data which will be covered.

        """

    return self
