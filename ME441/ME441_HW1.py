"""
Heather White
ME 441
Assignment 1, Problem 4
Due 1-21-21
"""

import math

# Given
W = 10000 # N
s = 2 # m
b1 = 5 # m
b2 = 2 # m
b3 = 90
sig_a = 250E6 # Pa
E = 210E9 # Pa
rho = 7850 # kg/m^3
FS = 2

# Design Variables
H = 5.0 # m
D = 0.1 # m
t = 0.01 # m

# Calculations
ratio = D/t
stress = W / (2*D*t*math.pi)
inertia = (math.pi/4)*((0.5*D + 0.5*t)**4 - (0.5*D - 0.5*t)**4)
area = 2 * D * t * math.pi
length = math.sqrt((s/2)**2 + H**2)
crit_buckling_load = (1/FS) * ((math.pi ** 2 * E * inertia) / ((0.7 * length)**2)) * area


print("\nConstraints:")

# Diameter constraint
if D >= 0.1 and D <= 2:
    print("Diameter =", D, "m. Constraint passed.")
else:
    print("Diameter =", D, "m. Constraint FAILED.")

# Thickness constraint
if t >= 0.01 and t <= 0.1:
    print("Thickness =", t, "m. Constraint passed.")
else:
    print("Thickness =", t, "m. Constraint FAILED.")

# Height constraint
if H >= b2 and H <= b1:
    print("Height =", H, "m. Constraint passed.")
else:
    print("Height =", H, "m. Constraint FAILED.")

# Ratio constraint
if ratio <= b3:
    print("Ratio =", ratio, "Constraint passed.")
else:
    print("Ratio =", ratio, "Constraint FAILED.")

# Allowable stress constraint
if stress <= sig_a:
    print("Stress =", stress, "N. Constraint passed.")
else:
    print("Stress =", stress, "N. Constraint FAILED.")

# Buckling stress constraint
if stress <= crit_buckling_load:
    print("Critical buckling load =", crit_buckling_load, "N. Constraint passed.")
else:
    print("Critical buckling load =", crit_buckling_load, "N. Constraint FAILED.")

print("\nObjective: Minimize Mass")

# Minimize mass
mass = area * length * rho * 2
print("Mass =", mass, "kg")
print("Compressive stress =", stress, "Pa")
print("Load = ", W, "N")
print("Critical buckling load =", crit_buckling_load, "N")