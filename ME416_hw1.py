"""
Heather White
ME 416
Homework 1
Due 1-26-2020
"""
import matplotlib.pyplot as plt
import numpy as np
import math
import decimal
import decimal as d

""" Problem 1a """
"""
xvalues = np.linspace(-2, 2, 100)
yvalues = (-0.5 * xvalues**2) + (0.25 * xvalues**4)

plt.scatter(xvalues, yvalues)
plt.title("Problem 1: Double-Well Potential")
plt.xlabel('x')
plt.ylabel('V(x)')
#plt.show()
"""
""" Problem 1c """

"""
d = decimal.Decimal('0.123456')
for i in range(1,5):
    decimal.getcontext().prec = i
    print(i, ':', d, d*1)
"""
decimal.getcontext().prec = 6

kbT = decimal.Decimal('0.5') # Thermal energy
N = 1000000 # Number of integration steps
m = decimal.Decimal('1') # particle mass
gamma = decimal.Decimal('1') # damping constant
dt = decimal.Decimal('0.001') # timestep
x = [decimal.Decimal('0')]
v = [kbT]
KE = [decimal.Decimal('0.5')*m*v[0]**2]

print("Round" + '\t' + "Time" + '\t' + "x" + '\t' + "F_C" + '\t' + '\t' + "F_R")
time = [0]
current_time = 0
for count in range(0, N):

    current_time += dt
    time.append(current_time)
    
    xi = decimal.Decimal(np.random.normal())
 
    F_R = decimal.Decimal(math.sqrt((2*m*kbT*gamma)/dt)) * xi
    F_C = decimal.Decimal(x[count] - x[count]**3)
 
    new_x = decimal.Decimal(x[count] + v[count]*dt) + decimal.Decimal('0.5')*((-gamma*v[count]) + (1/m)*(F_R+F_C))*(dt**2)
    x.append(new_x)

    new_v = decimal.Decimal(v[count] + (-gamma*v[count] + (1/m)*(F_R + F_C))*dt)
    v.append(new_v)

    new_KE=(decimal.Decimal('0.5')*m*v[count]**2)
    KE.append(new_KE)

    if count%10000 == 0:
        print(count, current_time, x[count], F_C, F_R)

"""
plt.scatter(time, x, s = 2)
plt.hlines(1, 0, 1000, color='r')
plt.hlines(-1, 0, 1000, color='r')
plt.title("Problem 1: Position vs Time")
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()

plt.scatter(time, KE, s = 2)
plt.title("Problem 1: Kinetic Energy vs Time")
plt.xlabel('Time')
plt.ylabel('Kinetic Energy')
plt.show()
"""

plt.scatter(x, v, s=2)
plt.title("Problem 1: Phase Portrait")
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.show()