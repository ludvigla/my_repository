
from simple_math import *
import numpy as np

def test_simple_add():
    assert simple_add(1, 1) == 2

def test_simple_sub():
    assert simple_sub(1, 1) == 0

def test_simple_mult():
    assert simple_mult(2, 2) == 4

def test_simple_div():
    assert simple_div(2, 2) == 1.0

def test_poly_first():
    assert all(poly_first(np.array([1, 2, 3]), 1, 1) == np.array([2, 3, 4]))

def test_poly_second():
    assert all(poly_second(np.array([1, 2, 3]), 1, 1, 1) == np.array([3, 7, 13]))
