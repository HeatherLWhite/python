import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants

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

print(avg_offrate_list)

kb = scipy.constants.Boltzmann / 4184 # kcal/K
T = 50 # K

X0 = 4.00E-09
xb = 3.6247E-25
xdummy = np.linspace(1.4, 2.6, 100)
ydummy = X0 * np.exp((xdummy*xb) / (kb * T))

xdata = force_list
ydata = avg_offrate_list

plt.scatter(force_list, avg_offrate_list)
plt.plot(xdummy, ydummy)
plt.title('Figure 12: Curve-Fitting of Catch Bond Data')
plt.xlabel('Force (kcal/mol-A')
plt.ylabel('Lifetime (fs)')
plt.legend(['Fit: ${\chi}_0$ = 4e-9, $x_b$ = 3.62e-25', 'Data'])
plt.show()