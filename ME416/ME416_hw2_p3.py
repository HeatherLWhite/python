import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

path = '/mnt/c/Users/heath/Documents/NU_Courses/ME416/HW2/catchBonds/Q3/'
forces = ['1.4', '1.6', '1.8', '2.0', '2.2', '2.4', '2.6']

force_list = [1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6]
force_list_pN = []
for item in force_list:
    force_list_pN.append(item/64.479)

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
    average = average/1000 #fs to ps
    avg_offrate_list.append(1/average)

    infile.close()

kb = 1.380649*10**-23 * 10**12 * 10**12 # pN-pm/K
T = 50 # K

def func(x, X0, xb):
    return X0 * np.exp((x*xb) / (kb * T))

xdata = force_list_pN
ydata = avg_offrate_list
params, cv = curve_fit(func, xdata, ydata, p0 = (1e-6, 150), maxfev=1000000)

xdata = force_list_pN
ydata = avg_offrate_list
xdummy = np.linspace(0.021712496, 0.040323206, 100)
ydummy = params[0] * np.exp((xdummy*params[1]) / (kb * T))

plt.scatter(force_list_pN, avg_offrate_list)
plt.plot(xdummy, ydummy)
plt.title('Figure 12: Curve-Fitting of Catch Bond Data')
plt.xlabel('Force (pN)')
plt.ylabel('Off-Rate (1/ps)')
formatted_param1 = '{:.3e}'.format(params[0])
formatted_param2 = '{:.3e}'.format(params[1])
plt.legend(['Fit: ${\chi}_0$ = ' + str(formatted_param1) + ' $ps^{-1}$' + ', $x_b$ = ' + str(formatted_param2) + ' pm', 'Data'])
plt.show()