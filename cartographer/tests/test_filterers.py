from cartographer.filterers import KernelDensityFilterer

from sklearn.datasets.samples_generator import make_blobs
from sklearn.utils.testing import assert_true, assert_raises
import numpy as np


def test_kde_one_dimension():
    X, true_labels = make_blobs(n_samples=1000, n_features=1)
    kde_filterer = KernelDensityFilterer()
    kde_prob = kde_filterer.fit_transform(X)
    assert_true(kde_prob.shape[0] == X.shape[0])
    assert_true(kde_prob.shape[1] == 1)


def test_kde_two_dimension():
    X, true_labels = make_blobs(n_samples=1000, n_features=2)
    kde_filterer = KernelDensityFilterer()
    kde_prob = kde_filterer.fit_transform(X)
    assert_true(kde_prob.shape[0] == X.shape[0])
    assert_true(kde_prob.shape[1] == 1)
