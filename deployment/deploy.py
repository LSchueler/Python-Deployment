# -*- coding: utf-8 -*-
"""
A deployment test script.

.. currentmodule:: deployment.deploy

The following classes are provided

.. autosummary::
   
"""
import numpy as np


def mat_mul_np(a, b):
    """
    Matrix multiplication (vectorized)

    Parameters
    ----------
    a, b : :class:`np.ndarray`
        Input arrays, scalars not allowed.

    Returns
    -------
    c : :class:`np.ndarray`
        The matrix product of the inputs.
    """
    return np.matmul(a, b)

if __name__ == '__main__':
    pass
