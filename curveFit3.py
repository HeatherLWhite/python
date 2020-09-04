"""
PMF = a+[log(SR/c)]^b
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

xL100 = np.array([
    5.00E-06,
    1.00E-05,
    5.00E-05,
    0.0001,
    0.0005
    #0.001
    ])

yL20 = np.array([
    3657,
    3857,
    4780,
    5396,
    6451,
    8591
    ])

yL30 = np.array([
    8805,
    9739,
    10992,
    12459,
    15001,
    17565
    ])

yL40 = np.array([
    13659,
    14423,
    17918,
    18484,
    22810,
    26766
    ])

yL50 = np.array([
    20815,
    23280,
    27098,
    28729,
    34485,
    40248
    ])

yL60 = np.array([
    27793,
    30203,
    34969,
    39855,
    53876,
    65101
    ])

yL70 = np.array([
    40603,
    44209,
    51026,
    53630,
    66727,
    72895
    ])

yL80 = np.array([
    44324,
    47159,
    53414,
    57588,
    69119,
    76237
    ])

yL90 = np.array([
    54609,
    57575,
    67012,
    71677,
    86271,
    97156
    ])

yL100 = np.array([
    68564,
    70375,
    82096,
    91010,
    107857
    #157352
    ])

yvalues = [yL20, yL30, yL40, yL50, yL60, yL70, yL80, yL90, yL100]

xdummy = np.linspace(0.0000001, 0.001, 500)

def func(x, a, b):
    return a + (np.log10(x/(10e-15)))**b

dataLabels = ['Data - L20', 'Data - L30', 'Data - L40', 'Data - L50', 'Data - L60', 'Data - L70', 'Data - L80', 'Data - L90', 'Data - L100']
fitLabels = ['Fit - L20', 'Fit - L30', 'Fit - L40', 'Fit - L50', 'Fit - L60', 'Fit - L70', 'Fit - L80', 'Fit - L90', 'Fit - L100']

for count in range(0, len(yvalues)):

    if yvalues[count].all == yL100.all:
        x = xL100
    else:
        x = xarray

    params, params_covariance = curve_fit(func, x, yvalues[count], p0=[20000, 9])
    print("Parameters [a b] for", dataLabels[count], ':', params)
    #print("Covariance for [a b c] for", dataLabels[count], ':', params_covariance)

    plt.scatter(x, yvalues[count], label=dataLabels[count])
    plt.plot(xdummy, func(xdummy, params[0], params[1]), label=fitLabels[count])

#plt.xlim(10e-8,10e-1)
plt.legend(loc='best')
plt.ylabel('Peak PMF (kCal/mol)')
plt.xscale('log')
plt.xlabel('log (Strain Rate (A/fs))')
plt.title('Curve fits: PMF=a+[log(SR/c)]^b')
plt.show()
                