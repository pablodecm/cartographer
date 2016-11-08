"""
Mapper algorithm implementation
"""
from sklearn.base import BaseEstimator, ClusterMixin
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import numpy as np
from .coverers import HyperRectangleCoverer
import itertools


class Mapper(BaseEstimator, ClusterMixin):

    """ Mapper algorithm implementation

    Parameters
    ----------

    filterer : scikit-learn transformer, default=PCA(n_components=2)
      If y is not specified in the fit method the lense/filter values used will
      be the result of the application of this transform Pipeline to the
      input data will be considered.

    coverer: instance of Coverer object, default=HyperRectangleCoverer()

    clusterer: scikit-learn-like cluster estimator, default=DBSCAN()

    params: dict of params for filterer, coverer and clusterer, default={}
      Parameters to be passed to the filter, coverer and cluster objects

    Attributes
    ----------

    Notes
    -----

    References
    ----------


    """

    def __init__(self, filterer=PCA(n_components=2),
                 coverer=HyperRectangleCoverer(),
                 clusterer=DBSCAN(),
                 params={}):
        self.filterer = filterer
        self.coverer = coverer
        self.clusterer = clusterer
        self.set_params(**params)

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

        # if y no specified, use filterer object to obtain filter map
        if y is None:
            y = self.filterer.fit_transform(X)

        # obtain matrix of partition membership
        m_matrix = self.coverer.fit_transform(y)
        # overlap between partitions
        o_matrix = self.coverer.overlap_matrix()

        def clusterize_samples(X, mask):
            ids = np.where(mask)[0]
            if len(ids) == 0:
                return []
            s_labels = self.clusterer.fit_predict(X[ids])
            # get distinct labels (remove noise -1)
            u_labels = s_labels[np.where(np.unique(s_labels) > -1)[0]]
            # if no clusters return empty list or list of np.array otherwise
            if len(u_labels) == 0:
                return []
            else:
                return [ids[s_labels == label] for label in u_labels]

        # clustering per partition
        # this can be parallelized (e.g. joblib)
        self.nodes_ = [clusterize_samples(X, mask) for mask in m_matrix.T]

        # obtain links checking cluster intersections
        # in the future could also save the size of intersection
        self.links_ = []
        self.nodes_to_int_ = {}
        counter = 0
        for p_idx, o_ids in enumerate(o_matrix):
            nc_p_idx = len(self.nodes_[p_idx])
            # map to go from (p, c) node notation to a single int
            for c_p_idx in range(nc_p_idx):
                self.nodes_to_int_[(p_idx, c_p_idx)] = counter
                counter += 1
            # only check overlapping partitions for intersection
            for o_idx in np.where(o_ids)[0]:
                nc_o_idx = len(self.nodes_[o_idx])
                for c_p_idx, c_o_idx in \
                        itertools.product(range(nc_p_idx), range(nc_o_idx)):
                    intersect = np.intersect1d(self.nodes_[p_idx][c_p_idx],
                                               self.nodes_[o_idx][c_o_idx],
                                               assume_unique=True)
                    if intersect.shape[0] != 0:
                        self.links_.append(((p_idx, c_p_idx),
                                            (o_idx, c_o_idx),
                                            intersect.shape[0]))

        return self
