import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

N = 1000
K = 50

# get average
def Get_Average(list):
    sum = 0
    for item in list:
        sum += item
    return sum/len(list)

# get variance
def Get_Variance(list):
    sum = 0
    average = Get_Average(list)
    for item in list:
        sum += (item - average)**2
    return sum/len(list)

# second function
def fb(x, y):
    z = np.exp(-(x**4 + y**4))
    return z

# plot function b
fig = plt.figure(1)
ax = Axes3D(fig)
X = np.linspace(-math.pi, math.pi)
Y = np.linspace(-math.pi, math.pi)
X, Y = np.meshgrid(X, Y)
Z = fb(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
plt.title('The plot of the second function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# calculate original integral of function b
# random points generation
def XYsamples(N):
    s = []
    for i in range(N):
        x = np.random.uniform(-math.pi, math.pi)
        y = np.random.uniform(-math.pi, math.pi)
        z = np.random.uniform(0, fb(0, 0))
        s.append([x, y, z])
    return s
# calculate integral
def InteOB():
    s = XYsamples(N)
    s1 = np.array(s)
    count = 0
    for i in range(len(s1)):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / N
    integral = rate * 2 * math.pi * 2 * math.pi * fb(0, 0)
    return integral
# calculate average integral and variance
inte_OB = []
for i in range(K):
    inte_OB.append(InteOB())
aver_Ob = Get_Average(inte_OB)
var_Ob = Get_Variance(inte_OB)
print('The original average integral estimation of function b is:', aver_Ob)
print('The original variance of function b is:', var_Ob)

# Using stratification
def StraSampB():
    s = []
    for i in range(968):
        x = np.random.uniform(-1.2, 1.2)
        y = np.random.uniform(-1.2, 1.2)
        z = np.random.uniform(0, fb(0, 0))
        s.append([x, y, z])
    # first zone
    for i in range(4):
        x = np.random.uniform(-math.pi, -1.2)
        y = np.random.uniform(-math.pi, -1.2)
        z = np.random.uniform(0, fb(-1.2, -1.2))
        s.append([x, y, z])
    # second zone
    for i in range(4):
        x = np.random.uniform(-math.pi, -1.2)
        y = np.random.uniform(-1.2, 1.2)
        z = np.random.uniform(0, fb(-1.2, 0))
        s.append([x, y, z])
    # third zone
    for i in range(4):
        x = np.random.uniform(-math.pi, -1.2)
        y = np.random.uniform(1.2, math.pi)
        z = np.random.uniform(0, fb(-1.2, 1.2))
        s.append([x, y, z])
    # fourth zone
    for i in range(4):
        x = np.random.uniform(-1.2, 1.2)
        y = np.random.uniform(-math.pi, -1.2)
        z = np.random.uniform(0, fb(0, -1.2))
        s.append([x, y, z])
    # fifth zone
    for i in range(4):
        x = np.random.uniform(-1.2, 1.2)
        y = np.random.uniform(1.2, math.pi)
        z = np.random.uniform(0, fb(0, 1.2))
        s.append([x, y, z])
    # sixth zone
    for i in range(4):
        x = np.random.uniform(1.2, math.pi)
        y = np.random.uniform(-math.pi, -1.2)
        z = np.random.uniform(0, fb(1.2, -1.2))
        s.append([x, y, z])
    # seventh zone
    for i in range(4):
        x = np.random.uniform(1.2, math.pi)
        y = np.random.uniform(-1.2, 1.2)
        z = np.random.uniform(0, fb(1.2, 0))
        s.append([x, y, z])
    # eighth zone
    for i in range(4):
        x = np.random.uniform(1.2, math.pi)
        y = np.random.uniform(1.2, math.pi)
        z = np.random.uniform(0, fb(1.2, 1.2))
        s.append([x, y, z])
    return s
# calculate average integral and variance using stratification
def InteStra():
    s = StraSampB()
    s1 = np.array(s)
    count = 0
    for i in range(968):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 968
    integral = rate * 2.4 * 2.4 * fb(0, 0)
    # first zone
    count = 0
    rate = 0
    for i in range(968, 971):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
             count += 1
    rate = count / 4
    integral += rate * (math.pi - 1.2) * (math.pi - 1.2) * fb(-1.2, -1.2)
    # second zone
    count = 0
    rate = 0
    for i in range(972, 975):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * 2.4 * (math.pi - 1.2) * fb(-1.2, 0)
    # third zone
    count = 0
    rate = 0
    for i in range(976, 979):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * (math.pi - 1.2) * (math.pi - 1.2) * fb(-1.2, 1.2)
    # fourth zone
    count = 0
    rate = 0
    for i in range(980, 983):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * 2.4 * (math.pi - 1.2) * fb(0, -1.2)
    # fifth zone
    count = 0
    rate = 0
    for i in range(984, 987):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * 2.4 * (math.pi - 1.2) * fb(0, 1.2)
    # sixth zone
    count = 0
    rate = 0
    for i in range(988, 991):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * (math.pi - 1.2) * (math.pi - 1.2) * fb(1.2, -1.2)
    # seventh zone
    count = 0
    rate = 0
    for i in range(992, 995):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * 2.4 * (math.pi - 1.2) * fb(1.2, 0)
    # eighth zone
    count = 0
    rate = 0
    for i in range(996, 999):
        if s1[i, 2] <= fb(s1[i, 0], s1[i, 1]):
            count += 1
    rate = count / 4
    integral += rate * (math.pi - 1.2) * (math.pi - 1.2) * fb(1.2, 1.2)
    return integral
inte_OB1 = []
for i in range(K):
    inte_OB1.append(InteStra())
aver_Ob1 = Get_Average(inte_OB1)
var_Ob1 = Get_Variance(inte_OB1)
print('The average integral estimation of function b after using stratification is:', aver_Ob1)
print('The variance of function b after using stratification is:', var_Ob1)

# Importance sampling
# projection on X-Z
fig1 = plt.figure(2)
ax1 = Axes3D(fig1)
X1 = np.linspace(-math.pi, math.pi)
Y1 = np.linspace(-math.pi, math.pi)
X1, Y1 = np.meshgrid(X1,Y1)
Z1 = fb(X1,Y1)
#, cmap=plt.get_cmap('rainbow')
ax1.contourf(X1, Y1, Z1, zdir='x', offset=0)
plt.title(' projection on X-Z plane')
ax1.set_xlabel('X')
ax1.set_zlabel('Z')
ax1.set_ylabel('Y')
# replacement function Normal
def NormalPdf(x, mu, sigma):
    return ((1/math.sqrt(2*math.pi*sigma))*np.exp(-(x-mu)**2/(2*sigma)))
# apply importance sampling in X-Z and Y-Z plain
def ISXorY():
    s = []
    count = 0
    for i in range(N):
        x = np.random.normal(0, 1)
        if x >= -math.pi and x <= math.pi:
            s.append(x)
            count += 1
    return (count, s)
# process two IS sample array to make their counts equal
def ProIS():
    (c1, s1) = ISXorY()
    (c2, s2) =ISXorY()
    if c1 == c2:
        return (s1, s2)
    elif c1 > c2:
        while(len(s1)>len(s2)):
            s1.pop(len(s1)-1)
        return (s1, s2)
    else:
        while (len(s2) > len(s1)):
            s2.pop(len(s2)-1)
        return (s1, s2)
# create z(.) and h(.) and calculate integral
def InteCreZandH():
    (x1, x2) = ProIS()
    z = []
    for i in range(len(x1)):
        z.append(np.exp(-x1[i]**4) * np.exp(-x2[i]**4))
    h = []
    for i in range(len(x1)):
        h.append(NormalPdf(x1[i], 0, 1) * NormalPdf(x2[i], 0, 1))
    integral = 0
    for i in range(len(z)):
        integral += z[i] / h[i]
    integral = integral / len(z)
    return integral
# loop for 50 times and calculate average integral and variance
data_IS = []
for i in range(K):
    data_IS.append(InteCreZandH())
aver_IS = Get_Average(data_IS)
var_IS = Get_Variance(data_IS)
print('The average integral estimation of fucntion b after using Importance Sampling is:', aver_IS)
print('The variance of function b after using Importance Sampling is:', var_IS)
plt.show()