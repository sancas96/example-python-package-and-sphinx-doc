from scipy.integrate import quad
import numpy as np
from pytest import approx

from opt2.integration.compute_integral import Rcf

a = 0
b = 1
n = 2
f = lambda t: np.exp(-t**2/2)

approx_Rcf = Rcf(f, a, b, n)

obj, err = quad(f, a, b)

def test_Rcf():
    assert approx_Rcf == approx(obj, rel=1e-2)