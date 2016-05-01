# Sebastian Raschka 2014-2016
# mlxtend Machine Learning Library Extensions
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

from mlxtend._base import _BaseMultiClass
import numpy as np
from mlxtend.utils import assert_raises


def test_default():
    y = np.array([0, 1, 2, 3, 4, 2])
    mc = _BaseMultiClass()
    expect = np.array([[1., 0., 0., 0., 0.],
                       [0., 1., 0., 0., 0.],
                       [0., 0., 1., 0., 0.],
                       [0., 0., 0., 1., 0.],
                       [0., 0., 0., 0., 1.],
                       [0., 0., 1., 0., 0.]], dtype='float')
    out = mc._one_hot(y=y, n_labels=5, dtype='float')
    np.testing.assert_array_equal(expect, out)


def test_oneclass():
    y = np.array([0, 0, 0])
    mc = _BaseMultiClass()
    out = mc._one_hot(y=y, n_labels=1, dtype='float')
    expect = np.array([[1.], [1.], [1.]])
    np.testing.assert_array_equal(expect, out)


def test_morelabels():
    y = np.array([0, 0, 1])
    mc = _BaseMultiClass()
    out = mc._one_hot(y=y, n_labels=4, dtype='float')
    expect = np.array([[1., 0., 0., 0.],
                       [1., 0., 0., 0.],
                       [0., 1., 0., 0.]])
    np.testing.assert_array_equal(expect, out)

"""
def test_list_morelabels():
    y = [0, 1]
    expect = np.array([[1., 0., 0.],
                       [0., 1., 0.]], dtype='float')
    out = one_hot(y, num_labels=3)
    np.testing.assert_array_equal(expect, out)
"""
