#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is the unittest of the matrix multiplication methods.
"""
from __future__ import division, absolute_import, print_function

import unittest
import numpy as np
from deployment import mat_mul_np, mat_mul_cy


class TestMatMul(unittest.TestCase):
    def setUp(self):
        self.A = np.array(((1, 2, 3), (3, 4, 5)), dtype=np.double)
        self.B = np.array(((9, 8), (7, 6), (5, 4)), dtype=np.double)

    def test_matmul(self):
        C_py = mat_mul_np(self.A, self.B) 
        C_cy = mat_mul_cy(self.A, self.B)
        self.assertAlmostEqual(C_py.tolist(), C_cy.tolist())
