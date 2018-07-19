import numpy as np
import matplotlib.pyplot as plt
import random
import math
from mpl_toolkits.mplot3d import Axes3D

N = 1000

# first function
def f1(x):
    y1 = 1 / (1 + np.sinh(2 * x) * np.log(x))
    return y1

# second function
def f2(x ,y):
    z = np.exp(-(x**4 + y**4))
    return z

# samples generation function 1
def SamplesA(N):
    s = []
    for i in range(N):
        x = random.uniform(0.8, 3)
        s.append(x)
    return s

# samples generation function 2
def SamplesB(N):
    s = []
    for i in range(N):
        x = random.uniform(-math.pi, math.pi)
        y = random.uniform(-math.pi, math.pi)
        s.append([x,y])
    return s

# estimate the integral of the first function
s1 = SamplesA(N)
y = []
for i in range(len(s1)):
    y.append(f1(s1[i]))
integral_a = 0
for i in range(len(s1)):
    integral_a += y[i]*(3 - 0.8)
integral_a = integral_a/N
print('The Monte Carlo integral estimate for function a is:', integral_a)
# estimate the integral of the second function
s_b = SamplesB(N)
s2 = np.array(s_b)
Z = []
for i in range(len(s2)):
    Z.append(f2(s2[i, 0], s2[i, 1]))
integral_b = 0
for i in range(len(s2)):
    integral_b += Z[i]*((2*math.pi)**2)
integral_b = integral_b/N
print('The Monte Carlo integral estimate for function b is:', integral_b)