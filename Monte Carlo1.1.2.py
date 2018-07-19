import numpy as np
import matplotlib.pyplot as plt
import math

N = 100
def uniformSample(N):
    s = []
    for i in range(N):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        s.append([x, y])
    return s
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
# print(y)
plt.hist(y, bins=np.arange(2.8, 3.5, 0.1), histtype='bar', edgecolor='r')
plt.title('The histogram of the k=50 pi estimates')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()