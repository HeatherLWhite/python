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
from scipy.stats.distributions import t

colorHex = [
    # Blue
    '#0000FF',
    '#0000CC',
    '#4C0099',
    '#660066',
    '#660033',
    '#99004C',
    '#990000',
    '#CC0000',
    '#FF0000',
    # Red
    ]

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
    6.39E+27,
    6.48E+27,
    6.43E+27,
    6.84E+27,
    8.72E+27,
    1.13E+28
    ])

########################################################
### This function divides lists by Avogadro's Number ###
########################################################

def divideAvogadro(inlist):
    avogadroNum = 6.022 * (10**23) * 1000
    outlist = []
    for index in range(0,len(inlist)):
        outlist.append(inlist[index] / avogadroNum)
    return(outlist)

#####################################################
### Divide PMF values by Avogadro's Number * 1000 ###
#####################################################

yGD01 = divideAvogadro(yGD01)
yGD02 = divideAvogadro(yGD02)
yGD03 = divideAvogadro(yGD03)
yGD04 = divideAvogadro(yGD04)
yGD05 = divideAvogadro(yGD05)
yGD07 = divideAvogadro(yGD07)
yGD08 = divideAvogadro(yGD08)
yGD10 = divideAvogadro(yGD10)
yGD12 = divideAvogadro(yGD12)

#####################################################

yvalues = [yGD01, yGD02, yGD03, yGD04, yGD05, yGD07, yGD08, yGD10, yGD12]

xdummy = np.linspace(0.0000001, 0.001, 500)

def func(x, a, b):
    return a * (1 + (x/(1e-5))**b)

dataLabels = ['\u03C3=0.08', '\u03C3=0.18', '\u03C3=0.28', '\u03C3=0.40', '\u03C3=0.50', '\u03C3=0.66', '\u03C3=0.76', '\u03C3=0.96', '\u03C3=1.14']
#fitLabels = ['Fit - GD = 0.01', 'Fit - GD = 0.02', 'Fit - GD = 0.03', 'Fit - GD = 0.04', 'Fit - GD = 0.05', 'Fit - GD = 0.07', 'Fit - GD = 0.08', 'Fit - GD = 0.10', 'Fit - GD = 0.12']    

GDList = [0.08, 0.18, 0.28, 0.40, 0.50, 0.66, 0.76, 0.96, 1.14]
aList = []
bList = []
#cList = []

#colorlist = ['firebrick', 'chocolate', 'goldenrod', 'forestgreen', 'seagreen', 'teal', 'cornflowerblue', 'mediumorchid', 'palevioletred']
#colorlist = ['goldenrod', 'cornflowerblue', 'mediumorchid', 'palevioletred', 'teal', 'forestgreen', 'seagreen', 'chocolate', 'firebrick']

for count in range(0, len(yvalues)):
    
    x = xarray
    
    params, params_covariance = curve_fit(func, x, yvalues[count], p0=[6e28, 0.1], maxfev=10000)

    # CI calculation from http://kitchingroup.cheme.cmu.edu/blog/2013/02/12/Nonlinear-curve-fitting-with-parameter-confidence-intervals/
    alpha = 0.05 # 95% confidence interval
    n = len(yvalues[count]) # number of data points
    p = len(params) # number of parameters
    dof = max(0, n-p) # number of degrees of freedom
    tval = t.ppf(1.0-alpha/2., dof)
    paramNames = ['a','b']
    for i, p, var in zip(range(n), params, np.diag(params_covariance)):
        sigma = var**0.5
        print('CI for', dataLabels[count], paramNames[i], ': {1} [{2}  {3}] {4}'.format(i, p, p - sigma*tval, p + sigma*tval, sigma*tval))

    aList.append(params[0])
    bList.append(params[1])
    print("Parameters [a b] for", dataLabels[count], ':', params)
    print("Covariance for [a b] for", str(dataLabels[count]), ':')
    print(params_covariance, '\n')

    plt.scatter(x, yvalues[count], c=colorHex[count], label=dataLabels[count], s=70)
    plt.plot(xdummy, func(xdummy, params[0], params[1]), color = colorHex[count], linewidth = 2)

plt.xlim(10e-8,2e-3)
plt.xticks(fontsize = 14)
plt.ylim(-50, 300)
plt.legend(loc='lower left', fontsize='medium', ncol=5)
plt.ylabel('$\u03A8_{max}$ (kCal/$m^3$)', fontsize = 14)
plt.xscale('log')
plt.xlabel('Pulling Velocity ($\AA$/fs)', fontsize = 14)
#plt.title('Curve fits: PMF=a*[1+(SR/c)]^b')
plt.text(5e-5, 260, 'N=50 monomers', fontsize=12)
plt.text(2.5e-8, 315, '(b)', fontsize=20, weight = 'bold')
plt.show()

for index in range(0,len(colorHex)):
    plt.scatter(GDList[index], aList[index], color = colorHex[index], s = 200)

plt.xticks(fontsize = 30, weight = 'bold')
plt.xlabel('Grafting Density (\u03C3)', fontsize=30, weight = 'bold')
plt.tick_params(axis = 'y', right = True, left = False, labelright = True, labelleft = False)
plt.yticks(fontsize = 30, weight = 'bold')
#plt.ylabel('$\u03A8_0$', fontsize=30)
#plt.title('Value of "a" in PMF=a*[1+(SR/c)]^b')

yerrorList = [2.20, 9.58, 1.82, 2.71, 2.78, 2.16, 1.72, 1.91, 1.18]
for datapoint in range (0, len(aList)):
    xvalue = GDList[datapoint]
    yvalue = aList[datapoint]
    yerror = yerrorList[datapoint]
    color = colorHex[datapoint]
    plt.errorbar(xvalue, yvalue, yerr=yerror, ecolor = color, elinewidth = 3, barsabove=True)

plt.show()

plt.scatter(GDList, bList)
plt.xlabel('Chain Length')
plt.ylabel('b')
plt.title('Value of "b" in PMF=a*[1+(SR/c)]^b')
#plt.show()
