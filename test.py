import math
import numpy as np

# def f2(x ,y):
#     z = math.exp(-(x**4 + y**4))
#     return z
#
# x1 = np.linspace(-math.pi, math.pi)
# y1 = np.linspace(-math.pi, math.pi)
# print(x1)
# print(y1)
X = np.arange(-math.pi, math.pi, 0.25)
Y = np.arange(-math.pi, math.pi, 0.25)
X, Y = np.meshgrid(X, Y)
R = math.exp(X**2 + Y**2)
Z = np.sin(R)
print(Z)