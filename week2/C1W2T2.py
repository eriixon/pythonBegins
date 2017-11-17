
# coding: utf-8
# In[25]:


import matplotlib.pyplot as plt
# get_ipython().magic(u'matplotlib inline')
import numpy as np



# In[44]:


def f(x):
    return np.sin(x/5.0)*np.exp(x/10.0) + 5.0*np.exp(-x/2.0)
x = np.arange(1., 15., 0.5)
y = f(x)
# plt.plot(x, y)


# In[6]:


from scipy.linalg import solve


# In[15]:


A1 = np.matrix('1 1; 1 15')
B1 = np.array([f(1), f(15)])
w_1 = np.polynomial.polynomial.Polynomial(solve(A1, B1))
print (w_1)


# In[39]:


A2 = np.matrix('1 1 1; 1 8 64; 1 15 255')
B2 = np.array([f(1), f(8), f(15)])
w_2 = np.polynomial.polynomial.Polynomial(solve(A2, B2))
print (w_2)


# In[47]:


A3 = np.matrix([[1,1,1,1],[1,4,16,64],[1,10,100,1000],[1,15,255,3375]])
#A3 = np.array([[1,1,1,1],[1,4,4**2,4**3],[1,10,10**2,10**3],[1,15,15**2,15**3]])
B3 = np.array([f(1), f(4), f(10), f(15)])
w_3 = solve(A3,B3)
#w_3 = np.polynomial.polynomial.Polynomial(solve(A3, B3))
print (w_3)


# In[50]:


a=np.array([[1,1,1,1],[1,4,4**2,4**3],[1,10,10**2,10**3],[1,15,15**2,15**3]])
b=np.array([f(1),f(4),f(10),f(15)])
coef_3 = solve(a,b)
print (coef_3)

