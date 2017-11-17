import numpy as np
import math
from scipy import optimize


def func(x):
    return math.sin(x / 5.0) * math.exp(x / 10.0) + 5.0 * math.exp(-x / 2.0)

def h(x):
    return int(func(x))


# r1 = optimize.minimize(func, 2, method='Powell')
# print (r1)
# print("*********************************************")
#
# r2 = optimize.minimize(func, 30, method='BFGS')
# print (r2)
# print("*********************************************")
# r3 = optimize.differential_evolution(func, [(1,30)])
# print(r3)

# t1 = optimize.minimize(h, 30, method='BFGS')
# print(t1)

t2 = optimize.differential_evolution(h, [(1,30)])
print(t2)