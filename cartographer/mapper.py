"""
Mapper algorithm implementation
"""
from sklearn.base import BaseEstimator, ClusterMixin
from sklearn import cluster


class Mapper(BaseEstimator, ClusterMixin):

    """ Mapper algorithm implementation

    Parameters
    ----------

    filterer : f(X) which returns 2D array, array of f(X) which return 1D
    arrays or scikit-learn transformer, default=np.mean
      If y is not specified in the fit method the lense/filter values used will
      be the result of the application of this function array or transform
      Pipeline to the input data.

    filterer_params : dict of params of filterer, default={}
      Parameters to be passed to the filterer object/function

    coverer: instance of Coverer object

    coverer_params: dict of params of coverer, default={}
      Parameters to be passed to the coverer object/function

    clusterer: scikit-learn-like cluster estimator,
    default=DBSCAN(eps=0.5,min_samples=3)

    clusterer_params: dict of params of coverer, default={}
      Parameters to be passed to the clusterer object/function

    Attributes
    ----------

    Notes
    -----

    References
    ----------


    """

    def __init__(self, filterer=, filterer_params={},
                 coverer=, coverer_params={},
                 clusterer=cluster.DBSCAN(eps=0.5, min_samples=3),
                 clusterer_params={}):
        self.filterer = filterer
        self.filterer_params = filterer_params
        self.coverer = coverer
        self.coverer_params = coverer_params
        self.clusterer = clusterer
        self.clusterer_params = clusterer_params

    def fit(self, X, y=None):
        """ Creates a Mapper graph for the input data

        If y is not None but a bidimensional array-like, its columns are used
        as lens/filter. If is None, the filters attribute is used.

        Parameters
        ----------

        X : array-like, shape=(n_samples, n_features)
          Data on which the mapper algorithm will be applied.

        y : array-like, shape=(n_samples, n_filters), optional
          Lense/filter values for each samples, if not specified the class
          attribute filters will be used.

        """

    return self
