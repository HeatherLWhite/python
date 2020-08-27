#!/usr/bin/env python.

import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange

###################
### User Inputs ###
###################

# Grafting density
sigma = 0.5
# Chain length
N = 50
# Radius of NP (20-50 A)
r = 20
# Number of grafts/nm^2
f = 33
# Number identity of polymer to use
# PMMA=0, PS=1, PC=2, PB=3
polynum = 0
# Number of points in potential table
xlen = 500000
# Reduced sigma
red_sigma = 0.028246

###################################
### Polymer-Specific Geometries ###
###################################

# Monomer length, A
l_m = [2.71, 2.57, 12.92, 4.48]
# Monomer weight
unitweight = [100.12, 104.1, 254.3, 172.18];
# Surface area of NP
a = 4 * math.pi * r**2
# Volume of NP
v = 4/3 * math.pi * r**3

#####################################
### Polymer-Specific Coefficients ###
#####################################

# Constants, aa
k_1aa = [2.5e-3, 6.5e-5, 2.3e-3, 1e-4]
k_2aa = [-1.7e1, -5.3, -6.6e-2, -1.5]
k_3aa = [1.2, 1.4e-1, 1.2e-1, 3.4e-1]
k_4aa = [-1.5e-2, 2.5e-2, -1.7e-2, 0]

# Constants, ca
k_1ca = [1.8, 2, 1.9e-1, 1.5]
k_2ca = [8.9, 2.8e-1, 6.5e-3, 7.9e-1]
k_3ca = [-4.5e-1, 7.2e-1, -9.6e-3, -1.6e-1]
k_4ca = [1.5e-2, 8.8e-3, 9e-3, 8.5e-3]

# Constants, ar
k_1ar = [-0.019, -0.005, -0.001, -0.043]
k_2ar = [137.09, 104.36, 64.357, 34.891]
k_3ar = [1.755, 5.498, -1.745, 2.146]

# Constants, br
k_1br = [11.135, 10.440, 0.822, 2.394]
k_2br = [0.003, 0.003, 0.028, 0.016]
k_3br = [-0.079, 0.176, 0.002, -0.096]

##############################
### Calculate Coefficients ###
##############################

print("Calculating coefficients...")

a_r = 10 ** (k_1ar[polynum]*N + k_2ar[polynum]*red_sigma + k_3ar[polynum])
b_r = (k_1br[polynum]/N) + (k_2br[polynum]/red_sigma) + k_3br[polynum]
c_a = (k_1ca[polynum]/N) + (k_2ca[polynum]*(red_sigma**2)) + (k_3ca[polynum]*red_sigma) + k_4ca[polynum]

a_aDIVb_a = (k_1aa[polynum]*N) + (k_2aa[polynum]*red_sigma**2) + (k_3aa[polynum]*red_sigma) + k_4aa[polynum]
b_a = 0.1
a_a = a_aDIVb_a * b_a

######################################
### Find x_0 (location of min PMF) ###
######################################

checkRange = [0, 1000]

print("Finding x_0... Using lower x boundary", checkRange[0], "and upper x boundary", checkRange[1])

for x_var in arange(checkRange[0], checkRange[1], 0.00001*checkRange[1]):
    forceEq = -b_r * a_r  * math.exp(-b_r*x_var) + (a_a*c_a*math.exp(-c_a*x_var))/((b_a+math.exp(-c_a*x_var))**2)
    if forceEq >=0:
        x_0 = x_var
        break

print("x_0 is", x_0)

######################################
### Find x location of pmf plateau ###
######################################

print("Calculating location of PMF plateau...")

pmf_array = []

interval = 0.1
for count in arange(0, 1, interval):
    pmf_array.append(a_r*math.exp(-b_r*count) + a_a/(b_a + math.exp(-c_a*count)) - a_a/(b_a+math.exp(-c_a*x_0)))

while abs(pmf_array[len(pmf_array)-1] - pmf_array[len(pmf_array)-9]) > 0.000001:
    pmfEq = (a_r*math.exp(-b_r*interval) + a_a/(b_a + math.exp(-c_a*interval)) - a_a/(b_a+math.exp(-c_a*x_0)))
    pmf_array.append(pmfEq)
    interval += 0.1

x_plateau = interval

print("The pmf plateau x value is: ", x_plateau)

#########################
### Calculate epsilon ###
#########################

# Convertion factor from original kCal/mol to MJ/m^3
kCal2mJ= (x_0**3 * 1e-30 * 6.022e23 * 1000) / 4.184

pmf_min = kCal2mJ * (a_r*math.exp(-b_r*x_0) + a_a/(b_a + math.exp(-c_a*x_0)) - a_a/(b_a+math.exp(-c_a*x_0)))
print("The minimum PMF (mJ/m^3) is", pmf_min)
pmf_plateau = kCal2mJ * (a_r*math.exp(-b_r*x_plateau) + a_a/(b_a + math.exp(-c_a*x_plateau)) - a_a/(b_a+math.exp(-c_a*x_0)))
print("The plateau PMF (mJ/m^3) is", pmf_plateau)
epsilon = pmf_plateau - pmf_min
print("The value of epsilon is", epsilon)

###########################################################################
### Calculate PMF as a function of x and place into arrays for plotting ###
###########################################################################

x_array =  []
pmf_array = []
for x in arange(0, round(x_plateau), 0.001):
    x_array.append(x)
    pmfEq = kCal2mJ * (a_r*math.exp(-b_r*x) + a_a/(b_a + math.exp(-c_a*x)) - a_a/(b_a+math.exp(-c_a*x_0)));
    pmf_array.append(pmfEq)

##########################################
### Plot PMF as a function of distance ###
##########################################

plt.plot(x_array, pmf_array)
plt.xlabel("x (m)")
plt.ylabel("PMF(mJ/m^3)")
plt.ylim(0, 5)
plt.text(100, 1, "epsilon = " + str(round(epsilon,4)))
plt.show()
