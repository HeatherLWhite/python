import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import random
from sklearn.utils import resample
import pandas as pd


path = '/mnt/c/Users/heath/Documents/NU_Courses/ME416/HW2/catchBonds/Q3/'
forces = ['1.4', '1.6', '1.8', '2.0', '2.2', '2.4', '2.6']

force_list = [1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6]

avg_offrate_list = []

for force in range(0, len(forces)):
    
    infile = open(path+forces[force]+'/LT.txt', 'r')
    length = 0
    average = 0
    
    for line in infile:
        line = line.strip()
        length += 1
        average += float(line)

    average = average/length
    avg_offrate_list.append(1/average)

    infile.close()

meanlist = []

for count in range(0, 10000):
    boot = resample(avg_offrate_list, replace = True, n_samples = 5)
    meanlist.append(sum(boot)/len(boot))    

#print(meanlist)

numbins = 40
#plt.hist(meanlist, bins=np.linspace(min(meanlist), max(meanlist), numbins))
#plt.show()

confidence_interval = pd.Series(meanlist).quantile([0.025, 0.975])
print(confidence_interval)

"""
def func(x, X0, xb):
    kb = scipy.constants.Boltzmann / 4184 # kcal/K
    # print(kb)
    T = 50 # K
    return X0 * np.exp((x*xb) / (kb * T))

xdata = force_list
ydata = avg_offrate_list
params, cv = curve_fit(func, xdata, ydata, p0 = (1e-10, 1E-23), maxfev=1000000)
print(params)

plt.scatter(force_list, avg_offrate_list)
#plt.plot(xdata, func(xdata, params[0], params[1]))
plt.xlabel('Force (kcal/mol-A')
plt.ylabel('Lifetime (fs)')
#plt.show()
"""