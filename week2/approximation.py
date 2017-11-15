import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
# %matplotlib inline

x = [1,15]
y = [0,1]
matrix = np.matrix('1 1; 1 15')

# for ix, line in enumerate(x):
#     for iy in enumerate(y):
#         x = line.count(word)
#         matrix[index,words[word]] = x


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

b = [f(i) for i in x]
print (b)
x = np.arange(1, 15, 0.1)
y = f(x)
plt.plot(x, y)
