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
from scipy import stats

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

dataLabels = ['Data - L20', 'Data - L30', 'Data - L40', 'Data - L50', 'Data - L60', 'Data - L70', 'Data - L80', 'Data - L90', 'Data - L100']
fitLabels = ['Fit - L20', 'Fit - L30', 'Fit - L40', 'Fit - L50', 'Fit - L60', 'Fit - L70', 'Fit - L80', 'Fit - L90', 'Fit - L100']

LList = [20, 30, 40, 50, 60, 70, 80, 90, 100]
aList = []
bList = []

linearX = []
linearY = []

linearXList = []
linearYList = []

for count in range(0, len(yvalues)):
    
    x = xarray
    
    params, params_covariance = curve_fit(func, x, yvalues[count], p0=[3e28, 0.20], maxfev=10000)
    aList.append(params[0])
    bList.append(params[1])

    print("Parameters [a b] for", dataLabels[count], ':', params)

    plt.scatter(1+(x/1e-5)**bList[count], yvalues[count]/aList[count], label=dataLabels[count])

    linearX.append(1+(x/1e-5)**bList[count])
    linearY.append(yvalues[count]/aList[count])

for item in linearX:
    for subitem in item:
        linearXList.append(subitem)

for item in linearY:
    for subitem in item:
        linearYList.append(subitem)

slope, intercept, r_value, p_value, std_err = stats.linregress(linearXList, linearYList)
print("Slope:", slope)
print("Intercept:", intercept)
print("R-value:", r_value)
rSquared = round(r_value ** 2, 3)
print("R^2:", rSquared)
R2text = "$R^2 = $" + str(rSquared)

newxDummy = np.linspace(1.5, 4.5, 10)
newyDummy = []
for item in newxDummy:
    newyDummy.append(slope*item+intercept)

plt.plot(newxDummy, newyDummy, 'red', zorder=0)
plt.text(3.75, 3.5, R2text, fontsize=13)

#plt.xlim(10e-7,10e-2)
plt.legend(loc='best')
plt.ylabel('$\psi_{plateau}/a$')
plt.xlabel('$1+(SR/1e-5)^b$')
plt.title(r'$\psi_{plateau}=a[1+(\frac{SR}{c})^b]$, $c=1e^{-5}$')
plt.show()