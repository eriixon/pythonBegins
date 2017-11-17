import numpy as np
import math
from scipy import optimize


def f(x):
    return math.sin(x / 5.0) * math.exp(x / 10.0) + 5.0 * math.exp(-x / 2.0)


m = np.matrix([[1, 1], [1, 30]])
# v = np.array([f(1), f(30)])
r = optimize.minimize(f, 1)
print (r)