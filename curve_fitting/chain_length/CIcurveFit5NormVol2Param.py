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
    6.38E+28,
    7.03E+28,
    7.96E+28,
    8.84E+28,
    9.99E+28,
    1.26E+29
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

yL20 = divideAvogadro(yL20)
yL30 = divideAvogadro(yL30)
yL40 = divideAvogadro(yL40)
yL50 = divideAvogadro(yL50)
yL60 = divideAvogadro(yL60)
yL70 = divideAvogadro(yL70)
yL80 = divideAvogadro(yL80)
yL90 = divideAvogadro(yL90)
yL100 = divideAvogadro(yL100)

#####################################################

yvalues = [yL20, yL30, yL40, yL50, yL60, yL70, yL80, yL90, yL100]

xdummy = np.linspace(0.0000001, 0.001, 500)

def func(x, a, b):
    return a * (1 + (x/(1e-5))**b)

dataLabels = ['N=20', 'N=30', 'N=40', 'N=50', 'N=60', 'N=70', 'N=80', 'N=90', 'N=100']
fitLabels = ['Fit - L20', 'Fit - L30', 'Fit - L40', 'Fit - L50', 'Fit - L60', 'Fit - L70', 'Fit - L80', 'Fit - L90', 'Fit - L100']

LList = [20, 30, 40, 50, 60, 70, 80, 90, 100]
aList = []
bList = []

#colorlist = ['firebrick', 'chocolate', 'goldenrod', 'forestgreen', 'seagreen', 'teal', 'cornflowerblue', 'mediumorchid', 'palevioletred']

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

# Extra point [x = 0.0000005, y = 4.747E+28 / (6.022 * (10**23) * 1000)]
plt.scatter(0.0000005, 4.747E+28 / (6.022 * (10**23) * 1000), c = '#660066', s=70)
plt.xscale('log') 
plt.xlim(10e-8,2e-3)
plt.xticks(fontsize = 14)
plt.xlabel('Pulling Velocity ($\AA$/fs)', fontsize = 14)
plt.ylim(-25, 350)
plt.ylabel('$\u03A8_{max}$ (kCal/$m^3$)', fontsize = 14)
plt.legend(loc='lower left', fontsize='medium', ncol=5)
#plt.title(r'$\psi_{plateau}=a[1+(\frac{SR}{c})^b]$, $c=1e^{-5}$')
plt.text(5e-5, 300, '\u03C3=0.5 chains/$nm^2$', fontsize=12)
plt.text(2.5e-8, 370, '(a)', fontsize=20, weight = 'bold')
plt.show()

for index in range(0,len(colorHex)):
    plt.scatter(LList[index], aList[index], color = colorHex[index], s = 200) #s=500

plt.xticks(fontsize = 30, weight = 'bold')
plt.xlabel('Chain Length (N)', fontsize=30, weight = 'bold')
plt.tick_params(axis = 'y', right = True, left = False, labelright = True, labelleft = False)
plt.yticks(fontsize = 30, weight = 'bold')
"""
CIstring1 = ('95' + '% ' +  'Confidence Interval')
CIstring2 = ('        N              CI ')
CIstring3 = (
    '        20           $\pm$2.98' + '\n' + 
    '        30           $\pm$2.04' + '\n' + 
    '        40           $\pm$2.54' + '\n' +
    '        50           $\pm$3.00' + '\n' +
    '        60           $\pm$1.96' + '\n' +
    '        70           $\pm$7.08' + '\n' +
    '        80           $\pm$1.57' + '\n' +
    '        90           $\pm$2.26' + '\n' +
    '       100          $\pm$2.35' + '\n')
plt.text(20, 80, CIstring1, fontsize=18, weight = 'bold')
plt.text(20, 77, CIstring2, fontsize=18, weight = 'bold')
plt.text(20, 50, CIstring3, fontsize=18)
"""

yerrorList = [2.98, 2.04, 2.54, 3.00, 1.96, 7.08, 1.57, 2.26, 2.35]
for datapoint in range (0, len(aList)):
    xvalue = LList[datapoint]
    yvalue = aList[datapoint]
    yerror = yerrorList[datapoint]
    color = colorHex[datapoint]
    plt.errorbar(xvalue, yvalue, yerr=yerror, ecolor = color, elinewidth = 3, barsabove=True)

#plt.title("Projected Zero-Rate PMF", fontsize = 30, weight = 'bold')
plt.show()

plt.scatter(LList, bList)
plt.xlabel('Chain Length, N')
plt.ylabel('b')
plt.title('Value of "b" in $PMF=a[1+(SR/1e^-5)^b]$')
#plt.show()