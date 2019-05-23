# -*- coding: utf-8 -*-
"""
Purpose
=======

This is a very simple Python script with which different deployment steps can
be tested.

Subpackages
===========

.. autosummary::
    deploy

Functions
=========

.. currentmodule:: deployment.deploy

.. autosummary::
    mat_mul_np
    mat_mul_cy

"""


from deployment import deploy
from deployment.deploy import mat_mul_np
from deployment.matmul import mat_mul_cy

__all__ = ['mat_mul_np', 'mat_mul_cy']
