from cartographer.coverers import HyperRectangleCoverer

from sklearn.datasets.samples_generator import make_blobs
from sklearn.utils.testing import assert_true, assert_raises
import numpy as np


def test_one_dimension_int_parameters():
    X, true_labels = make_blobs(n_samples=1000, n_features=1)
    n_intervals = 10
    hrc = HyperRectangleCoverer(n_intervals, 0.3)
    hrc.fit(X)
    assert_true(hrc.lowerbounds.shape[0] == n_intervals**X.shape[1])
    assert_true(hrc.upperbounds.shape[0] == n_intervals**X.shape[1])
    m_matrix = hrc.transform(X)
    assert_true(m_matrix.shape[1] == n_intervals**X.shape[1])
    # every sample is in at least one partition
    assert_true(np.sum(m_matrix.any(axis=1)) == X.shape[0])


def test_two_dimension_int_parameters():
    X, true_labels = make_blobs(n_samples=1000, n_features=2)
    hrc = HyperRectangleCoverer(10, 0.3)
    n_intervals = 10
    hrc.fit(X)
    assert_true(hrc.lowerbounds.shape[0] == n_intervals**X.shape[1])
    assert_true(hrc.upperbounds.shape[0] == n_intervals**X.shape[1])
    m_matrix = hrc.transform(X)
    assert_true(m_matrix.shape[1] == n_intervals**X.shape[1])


def test_three_dimension_int_wrong_cases():
    X, true_labels = make_blobs(n_samples=1000, n_features=3)
    intervals = [5, 10, 15]
    overlap = [0.1, 0.2, 0.3]
    hrc = HyperRectangleCoverer(intervals, overlap)  # right case
    hrc_wrong_intervals = HyperRectangleCoverer([10, 5], 0.3)
    hrc_wrong_overlap = HyperRectangleCoverer(10, [0.1, 0.2])
    assert_raises(ValueError, hrc_wrong_intervals.fit, X)
    assert_raises(ValueError, hrc_wrong_overlap.fit, X)
    hrc.fit(X)
    assert_true(hrc.lowerbounds.shape[0] == np.prod(intervals))
    assert_true(hrc.upperbounds.shape[0] == np.prod(intervals))
    m_matrix = hrc.transform(X)
    assert_true(m_matrix.shape[1] == np.prod(intervals))
    assert_raises(ValueError, hrc_wrong_overlap.fit, X, X)
    assert_raises(ValueError, hrc_wrong_overlap.transform, X, X)
