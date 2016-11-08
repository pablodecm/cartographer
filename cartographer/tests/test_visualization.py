from cartographer.mapper import Mapper
from cartographer.visualization import html_graph, json_graph
from sklearn.datasets.samples_generator import make_circles
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils.testing import assert_true
import numpy as np
import json


def test__graph_simple():
    data, labels = make_circles(n_samples=2000, noise=0.03, factor=0.3)
    params = {'coverer__intervals': 10,
              'coverer__overlap': 0.1,
              'clusterer__min_samples': 3,
              'clusterer__eps': 0.5}
    m = Mapper(params=params)
    scaled_data = MinMaxScaler().fit_transform(data)
    m.fit(data, scaled_data)

    json_graph_str = json_graph(m)
    # check if it can be loaded to validate html
    json_graph_dict = json.loads(json_graph_str)
    html_graph_str = html_graph(m)  # validate HTML?
