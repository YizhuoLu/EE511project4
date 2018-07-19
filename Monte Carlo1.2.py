import numpy as np
import matplotlib.pyplot as plt
import math

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

# samples generation function
def uniformSample(N):
    s = []
    for i in range(N):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        s.append([x, y])
    return s

# samples change from 100 to 1000
var = []
for N in np.arange(100, 1100, 100):
    K = 50
    y = []
    for i in range(K):
        z = np.array(uniformSample(N))
        count = 0
        for i in range(len(z)):
            if math.sqrt(1 - z[i, 0] ** 2) >= z[i, 1]:
                count = count + 1
        area = count / N
        pi = 4 * area
        y.append(pi)
    var.append([N, Get_Variance(y)])

# plot between variances and N
v = np.array(var)
nrx = np.linspace(100, 1000, 10)
plt.xticks(nrx)
nry = np.linspace(min(v[:, 1]), max(v[:, 1]), len(v))
plt.yticks(nry)
plt.plot(v[:, 0], v[:, 1])
plt.title('Sample variance of the pi-estimates for different n')
plt.xlabel('n')
plt.ylabel('Variance')
plt.show()
