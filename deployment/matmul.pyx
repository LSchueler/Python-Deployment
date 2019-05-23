#!python
#cython: language_level=2
# -*- coding: utf-8 -*-
"""
This is the cython implementation of the matrix multiplication.
"""
from __future__ import division, absolute_import, print_function

import numpy as np

cimport cython
cimport numpy as np


DTYPE = np.double
ctypedef np.double_t DTYPE_t


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def mat_mul_cy(double[:,:] A, double[:,:] B):
    cdef int i, j, k
    cdef int max_i = A.shape[0]
    cdef int max_j = B.shape[1]
    cdef int max_k = A.shape[1]

    cdef double[:,:] C = np.zeros((max_i, max_j), dtype=DTYPE)

    for i in range(max_i):
        for j in range(max_j):
            for k in range(max_k):
                C[i,j] += A[i,k] * B[k,j]

    return np.asarray(C)
