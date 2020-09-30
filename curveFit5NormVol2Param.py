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
"""
xL100 = np.array([
    5.00E-06,
    1.00E-05,
    5.00E-05,
    0.0001,
    0.0005
    #0.001
    ])
"""
yL20 = np.array([
    2.114E+28,
    2.229E+28,
    2.763E+28,
    3.119E+28,
    3.729E+28,
    4.966E+28
    ])

yL30 = np.array([
    3.623E+28,
    4.008E+28,
    4.524E+28,
    5.127E+28,
    6.173E+28,
    7.228E+28
    ])

yL40 = np.array([
    4.350E+28,
    4.593E+28,
    5.706E+28,
    5.887E+28,
    7.264E+28,
    8.524E+28
    ])

yL50 = np.array([
    5.421E+28,
    6.062E+28,
    7.057E+28,
    7.482E+28,
    8.980E+28,
    1.048E+29
    ])

yL60 = np.array([
    6.03656E+28,
    6.52949E+28,
    7.54163E+28,
    8.5306E+28,
    1.0154E+29,
    1.14761E+29
    ])

yL70 = np.array([
    7.734E+28,
    8.421E+28,
    9.719E+28,
    1.022E+29,
    1.271E+29,
    1.388E+29,
    ])

yL80 = np.array([
    7.437E+28,
    7.913E+28,
    8.962E+28,
    9.662E+28,
    1.160E+29,
    1.279E+29
    ])

yL90 = np.array([
    8.224E+28,
    8.671E+28,
    1.009E+29,
    1.079E+29,
    1.299E+29,
    1.463E+29
    ])

yL100 = np.array([
    9.303E+28,
    9.549E+28,
    1.114E+29,
    1.235E+29,
    1.463E+29,
    1.616E+29
    ])

yvalues = [yL20, yL30, yL40, yL50, yL60, yL70, yL80, yL90, yL100]

xdummy = np.linspace(0.0000001, 0.001, 500)

def func(x, a, b):
    return a * (1 + (x/(1e-5))**b)

dataLabels = ['N=20', 'N=30', 'N=40', 'N=50', 'N=60', 'N=70', 'N=80', 'N=90', 'N=100']
fitLabels = ['Fit - L20', 'Fit - L30', 'Fit - L40', 'Fit - L50', 'Fit - L60', 'Fit - L70', 'Fit - L80', 'Fit - L90', 'Fit - L100']

LList = [20, 30, 40, 50, 60, 70, 80, 90, 100]
aList = []
bList = []

colorlist = ['firebrick', 'chocolate', 'goldenrod', 'forestgreen', 'seagreen', 'teal', 'cornflowerblue', 'mediumorchid', 'palevioletred']

for count in range(0, len(yvalues)):

    x = xarray
    """
    if yvalues[count].all == yL100.all:
        x = xL100
    else:
        x = xarray
    """
    params, params_covariance = curve_fit(func, x, yvalues[count], p0=[6e28, 0.1], maxfev=10000)
    aList.append(params[0])
    bList.append(params[1])
    print("Parameters [a b] for", dataLabels[count], ':', params)
    #print("Covariance for [a b c] for", dataLabels[count], ':', params_covariance)

    plt.scatter(x, yvalues[count], c=colorlist[count], label=dataLabels[count])
    plt.plot(xdummy, func(xdummy, params[0], params[1]), c=colorlist[count])

plt.xlim(10e-8,5e-3)
plt.ylim(-0.15e29, 1.8e29)
plt.legend(loc='lower left', fontsize='small', ncol=5)
plt.ylabel('Plateau \u03A8 (kCal/$m^3$)')
plt.xscale('log')
plt.xlabel('Strain Rate ($\AA$/fs)')
plt.title(r'$\psi_{plateau}=a[1+(\frac{SR}{c})^b]$, $c=1e^{-5}$')
plt.text(5e-5, 0.12e29, '\u03C3=0.05 chains/$nm^2$', fontsize=12)
plt.show()

plt.scatter(LList, aList)
plt.xlabel('Chain Length, N')
plt.ylabel('a')
plt.title("Value of Parameter 'a'")
plt.show()

plt.scatter(LList, bList)
plt.xlabel('Chain Length, N')
plt.ylabel('b')
plt.title('Value of "b" in $PMF=a[1+(SR/1e^-5)^b]$')
plt.show()