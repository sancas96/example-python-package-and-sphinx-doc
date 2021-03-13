import numpy as np
from scipy.integrate import quad

def Rcf(f,a,b,n):
    """
    Compute numerical approximation using rectangle or mid-point
    method in an interval.
    Nodes are generated via formula: x_i = a+(i+1/2)h_hat for
    i=0,1,...,n-1 and h_hat=(b-a)/n

    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral
        of f in the interval a,b
    """
    h_hat=(b-a)/n
    nodes=[a+(i+1/2)*h_hat for i in range(0,n)]
    sum_res=0
    for node in nodes:
        sum_res=sum_res+f(node)
    return h_hat*sum_res
def Rcf2(f,a,b,n):
    """
    Similar function to Rcf just to show how two different docstrings
    in Python can be used with Sphinx (see source to compare).
    
    :param f: function expression of integrand
    :param a: left point of interval
    :param b: right point of interval
    :param n: float
    :type f: function
    :type a: float
    :type b: float
    :type n: float
    :returns: numerical approximation to integral of f in
              the interval a,b
    :rtype: float
    """
    h_hat=(b-a)/n
    nodes=[a+(i+1/2)*h_hat for i in range(0,n)]
    sum_res=0
    for node in nodes:
        sum_res=sum_res+f(node)
    return h_hat*sum_res
