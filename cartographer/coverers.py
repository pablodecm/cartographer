"""
Coverers of the filtrated space
"""

from __future__ import print_function

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import sys




class HyperRectangleCoverer(BaseEstimator,TransformerMixin):
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

    def __init__(self, intervals=10, overlap=0.5):
        self.intervals = intervals
        self.overlap = overlap

    def fit(self, X, y=None):
        """ Creates the space covering for the input data

        It creates a hyperectangle covering of the multidimensional space of X.

        Parameters
        ----------
        X: array-like, shape=(n_samples, n_features)
          Data which will be covered.

        """

        if np.iterable(self.intervals):
          if len(self.intervals) != X.shape[1]:
            raise ValueError("length of intervals not matches X dimension")
          else:
            intervals = np.array(self.intervals, dtype=int)
        else:
          intervals = np.full((X.shape[1]),self.intervals, dtype=int)

        if np.iterable(self.overlap):
          if len(self.overlap) != X.shape[1]:
            raise ValueError("length of overlap not matches X dimension")
          else:
            overlap = np.array(self.overlap, dtype=float)
        else:
          overlap = np.full((X.shape[1]),self.overlap, dtype=float)

        # partition each dimension, incluiding last point
        bbs, ws = zip(*[np.linspace(*min_max_num, endpoint=True, retstep=True) \
            for min_max_num in \
            zip(np.min(X, axis=0),np.max(X, axis=0), intervals+1)]) 

        # get cover lower and upper bounds
        self.lowerbounds = np.array(np.meshgrid(*[bb[:-1] - shift for \
            bb, shift in zip(bbs, ws*overlap)])).T.reshape(-1,X.shape[1]) 
        self.upperbounds = np.array(np.meshgrid(*[bb[1:] + shift for \
            bb, shift in zip(bbs, ws*overlap)])).T.reshape(-1,X.shape[1])

        return self

    def transform(self, X, y=None):
        """ Returns boolean array of space partition membership

        Returns a (n_samples, n_partitions) boolean array whose elements
        are true when the sample (row) is a member of each space partition
        (column). This will be used to filter in the clustering space.

        Parameters
        ----------
        X: array-like, shape=(n_samples, n_features)
          Data which will be partition in hyperectangles.
        
        Returns
        -------
        m_matrix: boolean array, shape=(n_samples, n_partitions)
          Boolean matrix of sample membership to each partition

        """
        return np.logical_and( 
                  np.all(X[:,:,np.newaxis] > self.lowerbounds.T,axis=1),
                  np.all(X[:,:,np.newaxis] < self.upperbounds.T,axis=1))

    def overlap_matrix(self):
        """ Returns a boolean array with the overlaps between space partitions 

        Returns a (n_partitions, n_partitions) boolean array whose elements
        are true when there is overlap between the i and j partitions, only
        upper triangle is filled (rest is False).

        Returns
        -------
        overlap_matrix: boolean array, shape=(n_partitions, n_partitions)
          Boolean matrix of overlaping between partitions, only the upper
          triangle is filled and the rest is False.

        """
        overlap_matrix = None
        i_min_leq_j_min = self.lowerbounds[:,:,np.newaxis] <= self.lowerbounds.T
        i_max_geq_j_min = self.upperbounds[:,:,np.newaxis] >= self.lowerbounds.T
        overlap_matrix = np.all((i_min_leq_j_min,i_max_geq_j_min), axis  = 0)
        overlap_matrix = np.any((overlap_matrix, overlap_matrix.T), axis = 0)
        overlap_matrix = np.all(overlap_matrix, axis = 1)

        # only upper triagular filled
        np.fill_diagonal(overlap_matrix, False)
        return np.triu(overlap_matrix) 
