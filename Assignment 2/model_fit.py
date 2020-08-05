import numpy as np

np.random.seed(0)

x_data = [0, 1, 2, 3]
y_data = [95.57142857, 64.14285714, 47, 45.71428571]

import matplotlib.pyplot as plt

from scipy import optimize

def test_func(x, a, b, c):
    return (a-c)*(x+1)**(-b)+c
params, params_covariance = optimize.curve_fit(test_func, x_data, y_data,
                                               p0=[1, 1, 1])
print(params)

