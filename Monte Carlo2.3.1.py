import numpy as np
import matplotlib.pyplot as plt
import math
import random
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

# generate 1000 samples uniformly in x axis on the first function
def Xsamples(N):
    s = []
    for i in range(N):
        x = np.random.uniform(0.8, 3)
        s.append(x)
    return s

# generate 1000 samples uniformly in x axis and y axis on the second function
def XYsamples(N):
    s = []
    for i in range(N):
        x = np.random.uniform(-math.pi, math.pi)
        y = np.random.uniform(-math.pi, math.pi)
        s.append([x, y])
    return s

# first function
def fa(x):
    y = 1/(1 + np.sinh(2*x) * np.log(x))
    return y

# second function
def fb(x, y):
    z = np.exp(-(x**4 + y**4))
    return z

# plot function a
plt.figure(1)
plt.title('The plot of the first function')
plt.xlabel('X')
plt.ylabel('Y')
x = np.linspace(0.8, 3)
# replacement function Normal
def NormalPdf(x, mu, sigma):
    return ((1/math.sqrt(2*math.pi*sigma))*np.exp(-(x-mu)**2/(2*sigma)))
plt.plot(x, fa(x))
plt.text(0.9, fa(0.9), 'function a')
plt.plot(x, NormalPdf(x, 0, 1))
plt.text(0.8, NormalPdf(0.8, 0, 1), 'Normal Distribution')

# plot function b
fig = plt.figure(2)
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

# integral estimate of function a
def InteOa(f):
    integral = 0
    for i in range(N):
        integral += fa(f[i])*(3 - 0.8)
    integral = integral/N
    return integral

# calculate the original variance of function a
data_inteOa = []
for i in range(K):
    data_inteOa.append(InteOa(Xsamples(N)))
aver_Oa = Get_Average(data_inteOa)
var_Oa = Get_Variance(data_inteOa)
print('The original average integral estimation of function a is:', aver_Oa)
print('The original variance of function a is:', var_Oa)

# stratification to a
# calculate integral
def InteSa(f):
    inte1 = 0
    inte2 = 0
    for i in range(900):
        inte1 += fa(f[i])*(2 - 0.8)
    inte1 = inte1/900
    for i in range(900, 999):
        inte2 += fa(f[i])* (3 - 2)
    inte2 = inte2/100
    return (inte1 +inte2)
# New sampling using stratification for function a
def StrSampA(N):
    s = []
    for i in range(int(0.9*N)):
        y = random.uniform(0.8, 2)
        s.append(y)
    for i in range(int(0.1*N)):
        y = random.uniform(2, 3)
        s.append(y)
    return s
# calculate variance after stratification
data_inteSa = []
for i in range(K):
    data_inteSa.append(InteSa(StrSampA(N)))
aver_Sa = Get_Average(data_inteSa)
var_Sa = Get_Variance(data_inteSa)
print('The average integral estimation of function a after using stratification is:', aver_Sa)
print('The variance of function a after using stratification:', var_Sa)

# apply importance sampling for function a
# sample from normal distribution
# def sampleExp(Lambda):
#     Xi = []
#     # for i in range(N):
#     #     u = np.random.random()
#     #     y = -np.log(1-u)/Lambda
#     #     if y >= 0.8 and y <= 3:
#     #         Xi.append(y)
#     # return Xi
#     for i in range(N):
#         x = np.random.exponential(1/Lambda)
#         if x >= 0.8 and x <= 3:
#             Xi.append(x)
#     return Xi
def sampleFromNormal(mu, sigma):
    Xi = []
    for i in range(N):
        x = np.random.normal(mu, sigma)
        if x >= 0.8 and x <= 3:
            Xi.append(x)
    return Xi
# plot the sampling of Normal
plt.figure(3)
plt.title('histogram of sampling from normal distribution pdf')
plt.xlabel('X')
plt.ylabel('Y')
plt.hist(sampleFromNormal(0, 1), histtype='bar', edgecolor='r')
# IS calculate integral of function a
def InteAbyIS(f, mu, sigma):
    inte = 0
    for i in range(len(f)):
        inte = inte + (fa(f[i]))/(NormalPdf(f[i], 0, 1))
    inte = (inte) / (len(f))
    return inte
data_inteISa = []
for i in range(K):
    data_inteISa.append(InteAbyIS(sampleFromNormal(0, 1), 0, 1))
aver_ISa = Get_Average(data_inteISa)
var_ISa = Get_Variance(data_inteISa)
print('The average integral estimation of function a after using Importance Sampling is:', aver_ISa)
print('The variance of function a after using Importance Sampling:', var_ISa)
plt.show()