import numpy as np
import matplotlib.pyplot as plt
import math

s = []
N = 100
def uniformSample(N):
    for i in range(N):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        s.append([x, y])
    return s
z = np.array(uniformSample(N))
count = 0
for i in range(len(z)):
    if math.sqrt(1-z[i,0]**2) >= z[i,1]:
        count = count + 1
# print('The number of samples that fall within the quarter unit-circle is:', count)
area = count / N
print("The estimated area of the inscribed quarter circle is:", area)
pi = 4 * area
print('The estimated value of pi is:', pi)
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
circ = plt.Circle((0, 0), radius=1, edgecolor='r', facecolor='white')
sca = plt.scatter(z[:, 0], z[:, 1], s=7, c='b')
ax.add_artist(circ)
ax.add_artist(sca)
plt.title('scatter plot of 100 uniform distributed samples')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()