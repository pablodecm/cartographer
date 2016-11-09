from cartographer.mapper import Mapper
from sklearn.datasets.samples_generator import make_circles
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils.testing import assert_true
import numpy as np
import json


def test_mapper_filterer():
    data, labels = make_circles(n_samples=2000, noise=0.03, factor=0.3)
    params = {'coverer__intervals': 10,
              'coverer__overlap': 0.1,
              'clusterer__min_samples': 3,
              'clusterer__eps': 0.5}
    m_filter = Mapper(filterer=MinMaxScaler(), params=params)
    m_nofilter = Mapper(filterer=MinMaxScaler(), params=params)
    scaled_data = MinMaxScaler().fit_transform(data)
    m_filter.fit(data)
    m_nofilter.fit(data, scaled_data)
    assert_true(m_filter.links_ == m_nofilter.links_)
    assert_true(len(m_filter.nodes_) == len(m_nofilter.nodes_))
