from cartographer.coverers import HyperRectangleCoverer

from sklearn.datasets.samples_generator import make_blobs
from sklearn.utils.testing import assert_true
import numpy as np


def test_one_dimension_int_parameters():
    X, true_labels = make_blobs(n_samples=1000,n_features=1)
    n_intervals = 10
    hrc = HyperRectangleCoverer(n_intervals, 0.3)
    hrc.fit(X)
    assert_true(hrc.lowerbounds.shape[0] == n_intervals**X.shape[1]) 
    assert_true(hrc.upperbounds.shape[0] == n_intervals**X.shape[1]) 
    m_matrix = hrc.transform(X)
    assert_true(m_matrix.shape[1] == n_intervals**X.shape[1]) 
    # every sample is in at least one partition
    assert_true(np.sum(m_matrix.any(axis=1)) ==X.shape[0]) 
    
def test_two_dimension_int_parameters():
    X, true_labels = make_blobs(n_samples=1000,n_features=2)
    hrc = HyperRectangleCoverer(10, 0.3)
    n_intervals = 10
    hrc.fit(X)
    assert_true(hrc.lowerbounds.shape[0] == n_intervals**X.shape[1]) 
    assert_true(hrc.upperbounds.shape[0] == n_intervals**X.shape[1]) 
    m_matrix = hrc.transform(X)
    assert_true(m_matrix.shape[1] == n_intervals**X.shape[1]) 

    




