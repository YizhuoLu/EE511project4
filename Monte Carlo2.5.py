import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

N = 1000
K = 50

# function
def f(x, y):
    z = 20 + x**2 + y**2 - 10 * (np.cos(2*math.pi*x)+np.cos(2*math.pi*y))
    return z

# get average
def Get_Average(list):
    sum = 0
    for item in list:
        sum += item
    return sum/len(list)

# plot function
fig = plt.figure(1)
ax = Axes3D(fig)
X = np.linspace(-5, 5)
Y = np.linspace(-5, 5)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
plt.title('graph of the function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# calculate integral
def sampleXY(N):
    s = []
    for i in range(N):
        x = np.random.uniform(-5, 5)
        y = np.random.uniform(-5, 5)
        z = np.random.uniform(0, 80)
        s.append([x, y, z])
    return s
def Integ(N):
    count = 0
    ratio = 0
    s = sampleXY(N)
    s1 = np.array(s)
    for i in range(N):
        if s1[i, 2] <= f(s1[i, 0], s1[i, 1]):
            count += 1
    ratio = count / N
    integral = ratio * 80 * 10 * 10
    return integral
# loop for 50 times to obtain average
data_inte = []
for i in range(K):
    data_inte.append(Integ(N))
aver_integ = Get_Average(data_inte)
print('The integral estimation of the function is:', aver_integ)
plt.show()