"""
PMF = a+[log(SR/c)^b]
a: zero-shear limit
b: concavity
c: target low shear rate at which there is no variation anymore
log(SR/c)>1
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy as sym

xarray = np.array([
    5.00E-06,
    1.00E-05,
    5.00E-05,
    0.0001,
    0.0005,
    0.001
    ])

yGD01= np.array([
    1.54E+28,
    1.69E+28,
    2.13E+28,
    2.24E+28,
    2.57E+28,
    3.37E+28
    ])

yGD02 = np.array([
    5.07E+28,
    4.63E+28,
    5.80E+28,
    4.76E+28,
    6.81E+28,
    8.26E+28
    ])

yGD03 = np.array([
    6.03E+28,
    6.12E+28,
    7.55E+28,
    8.39E+28,
    1.03E+29,
    1.16E+29
    ])

yGD04 = np.array([
    6.54E+28,
    6.76E+28,
    8.80E+28,
    9.28E+28,
    1.17E+29,
    1.29E+29
    ])

yGD05 = np.array([
    5.21E+28,
    5.58E+28,
    6.96E+28,
    7.03E+28,
    8.92E+28,
    1.02E+29
    ])

yGD07 = np.array([
    3.38E+28,
    3.69E+28,
    4.33E+28,
    4.39E+28,
    5.34E+28,
    6.21E+28
    ])

yGD08 = np.array([
    3.37E+28,
    3.57E+28,
    4.41E+28,
    4.69E+28,
    5.56E+28,
    6.48E+28
    ])

yGD10 = np.array([
    1.51E+28,
    1.37E+28,
    1.69E+28,
    1.53E+28,
    1.66E+28,
    2.02E+28
    ])

yGD12 = np.array([
    1.51E+28,
    1.37E+28,
    1.69E+28,
    1.53E+28,
    1.66E+28,
    2.02E+28
    ])

yvalues = [yGD01, yGD02, yGD03, yGD04, yGD05, yGD07, yGD08, yGD10, yGD12]

xdummy = np.linspace(0.0000001, 0.001, 500)

def func(x, a):
    return a * (1 + (x/(1e-5))**0.2)

dataLabels = ['GD = 0.01', 'GD = 0.02', 'GD = 0.03', 'GD = 0.04', 'GD = 0.05', 'GD = 0.07', 'GD = 0.08', 'GD = 0.10', 'GD = 0.12']
fitLabels = ['Fit - GD = 0.01', 'Fit - GD = 0.02', 'Fit - GD = 0.03', 'Fit - GD = 0.04', 'Fit - GD = 0.05', 'Fit - GD = 0.07', 'Fit - GD = 0.08', 'Fit - GD = 0.10', 'Fit - GD = 0.12']    

GDList = [0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.08, 0.10, 0.12]
aList = []
bList = []
#cList = []

colorlist = ['firebrick', 'chocolate', 'goldenrod', 'forestgreen', 'seagreen', 'teal', 'cornflowerblue', 'mediumorchid', 'palevioletred']

for count in range(0, len(yvalues)):

    x = xarray

    params, params_covariance = curve_fit(func, x, yvalues[count], p0=[6e28], maxfev=10000)
    aList.append(params[0])
    #bList.append(params[1])
    #cList.append(params[2])
    print("Parameters [a b] for", dataLabels[count], ':', params)
    #print("Covariance for [a b] for", dataLabels[count], ':', params_covariance)

    plt.scatter(x, yvalues[count], label=dataLabels[count])
    plt.plot(xdummy, func(xdummy, params[0]), label=fitLabels[count])

plt.xlim(10e-8,10e-1)
plt.legend(loc='best')
plt.ylabel('Peak PMF (kCal/mol-m^3)')
plt.xscale('log')
plt.xlabel('Strain Rate (A/fs)')
plt.title('Curve fits: PMF=a*[1+(SR/c)]^b')
plt.show()

plt.scatter(GDList, aList)
plt.xlabel('Chain Length')
plt.ylabel('a')
plt.title('Value of "a" in PMF=a*[1+(SR/c)]^b')
plt.show()

"""
plt.scatter(GDList, bList)
plt.xlabel('Chain Length')
plt.ylabel('b')
plt.title('Value of "b" in PMF=a*[1+(SR/c)]^b')
plt.show()

plt.scatter(GDList, cList)
plt.ylim(-0.0005, 0.003)
plt.xlabel('Chain Length')
plt.ylabel('c')
plt.title('Value of "c" in PMF=a*[1+(SR/c)]^b')
plt.show()
"""