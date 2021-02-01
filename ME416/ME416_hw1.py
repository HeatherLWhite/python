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
from random import seed
from random import random

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


""" Problem 1c,d """
"""
decimal.getcontext().prec = 7

kbT = decimal.Decimal('0') # Thermal energy
N = 1000000 # Number of integration steps
m = decimal.Decimal('1') # particle mass
gamma = decimal.Decimal('0.05') # damping constant
dt = decimal.Decimal('0.001') # timestep
x = [decimal.Decimal('0')]
v = [1]
KE = [decimal.Decimal('0.5')*m*v[0]**2]
leftwelltimelist = []
rightwelltimelist = []
welltime = 0
dist_from_eq_list = []
F_C_list = []
inner_springconst_list = []
outer_springconst_list = []


time = [decimal.Decimal('0')]
current_time = 0
for count in range(0, N):

    current_time += dt
    time.append(current_time)
    
    xi = decimal.Decimal(np.random.normal())
 
    # Force calculations
    F_R = decimal.Decimal(math.sqrt((2*m*kbT*gamma)/dt)) * xi
    F_C = decimal.Decimal(x[count] - x[count]**3)
 
    # Position calculation
    new_x = decimal.Decimal(x[count] + v[count]*dt) + decimal.Decimal('0.5')*((-gamma*v[count]) + (1/m)*(F_R+F_C))*(dt**2)
    x.append(new_x)

    # Velocity calculation
    new_v = decimal.Decimal(v[count] + (-gamma*v[count] + (1/m)*(F_R + F_C))*dt)
    v.append(new_v)

    # Kinetic energy calculation
    new_KE=(decimal.Decimal('0.5')*m*v[count]**2)
    KE.append(new_KE)

    # Spring constant calculations
    inner_springconst = 0
    outer_springconst = 0

    if new_x < 0:
        F_C_list.append(abs(F_C))
        x_well = decimal.Decimal('-1')
        deltax = abs(new_x - x_well)
        dist_from_eq_list.append(deltax)
        if deltax != 0 and F_C != 0:
            if abs(new_x) < 1:
                inner_springconst = abs(deltax)/abs(F_C)
                inner_springconst_list.append(inner_springconst)
            elif abs(new_x) > 1:
                outer_springconst = abs(deltax)/abs(F_C)
                outer_springconst_list.append(outer_springconst)

    elif new_x > 0:
        F_C_list.append(abs(F_C))
        x_well = decimal.Decimal('1')
        deltax = abs(new_x - x_well)
        dist_from_eq_list.append(deltax)
        if deltax != 0 and F_C != 0:
            if abs(new_x) < 1:
                inner_springconst = abs(deltax)/abs(F_C)
                inner_springconst_list.append(inner_springconst)
            elif abs(new_x) > 1:
                outer_springconst = abs(deltax)/abs(F_C)
                outer_springconst_list.append(outer_springconst)
            
    # Well time calculations
    if new_x * x[count] < 0:
        if x[count] < 0:
            leftwelltimelist.append(welltime)
        if x[count] > 0:
            rightwelltimelist.append(welltime)
        welltime = 0
    else:
        welltime += 1

    # Print select data to terminal
    if count%10000 == 0:
        print(count, inner_springconst, outer_springconst)

# More well time calculations
leftaveragewelltime = 0
rightaveragewelltime = 0

for item in leftwelltimelist:
    leftaveragewelltime += item
for item in rightwelltimelist:
    rightaveragewelltime += item

leftaveragewelltime = leftaveragewelltime / len(leftwelltimelist)
rightaveragewelltime = rightaveragewelltime / len(rightwelltimelist)

print("Average well time (left):", str(decimal.Decimal(leftaveragewelltime)*dt))
print("Average well time (right):", str(decimal.Decimal(rightaveragewelltime)*dt))

# More spring constant calculations
average_inner_springconst = 0
average_outer_springconst = 0

for item in inner_springconst_list:
    average_inner_springconst += item

for item in outer_springconst_list:
    average_outer_springconst += item

average_inner_springconst = average_inner_springconst / len(inner_springconst_list)
average_outer_springconst = average_outer_springconst / len(outer_springconst_list)

print("Spring constant (inner):", average_inner_springconst)
print("Spring constant (outer):", average_outer_springconst)

########## PLOTS ##########

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

smallx = []
smallv = []
for index in range(0,len(x)):
    if index % 100 == 0:
        smallx.append(x[index])
        smallv.append(v[index])

plt.scatter(smallx, smallv, s=2)
plt.title("Problem 1: Phase Portrait")
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.show()

hist_counts, hist_bins, hist_bars = plt.hist(x, bins = 70, label = "Position")
plt.title("Particle Position Frequency")
plt.show()

for item in hist_counts:
    print(item)

for item in hist_bins:
    print(item)

for item in hist_bars:
    print(item)

plt.scatter(dist_from_eq_list, F_C_list)
plt.title("Problem 1: Force vs Equilibrium")
plt.xlabel("Distance from Equilibrium")
plt.ylabel('$F_C$')
plt.show()
"""


""" Problem 2 """
"""
kb = 0.00198
T = 300
N = 10000000
F = 1
L = 1
dx_mean = 0
dx_stdev = 1.0
stdev_list = []
finalx_list = []

for count in range(0,5):
    V = [1]
    x = [0]
    timelist = [0]
    time = 0

    for index in range(0, N):

        if index%(N/10) == 0:
            progress = round((index/N*100), 0)
            print(str(progress) + "%")

        Vold = V[len(V)-1]
        dx = np.random.normal(dx_mean, dx_stdev)
        xnew = x[len(x)-1] + dx
        #Vnew = -V[0]*math.sin(2*math.pi*(xnew/L))
        #Vnew = -V[0]*math.sin(2*math.pi*(xnew/L)) - F*xnew
        Vnew = -V[0]*math.sin(2*math.pi*(xnew/L)) + 0.25*math.sin(4*math.pi*(xnew/L)) - F*xnew

        if Vnew < Vold:
            x.append(xnew)
            V.append(Vnew)
            time += 1
            timelist.append(time)
        else:
            randnum = random()
            probability = math.exp(-(Vnew - Vold)/(kb*T))
            if randnum < probability:
                x.append(xnew)
                V.append(Vnew)
                time += 1
                timelist.append(time)

    stdev = np.std(x)
    print("Round", count+1, "Done:", x[len(x)-1], "\n")
    stdev_list.append(stdev)     

    finalx_list.append(x[len(x)-1])

    plt.plot(timelist, x)
    plt.xlabel("time")
    plt.ylabel("x position")
    #plt.show()

print("x value st. dev.:")
for item in stdev_list:
    print(item)

print("final x:")
for item in finalx_list:
    print(item)

F = 1
L = 1
V = [1]

xlist = np.linspace(-1, 1, 100)
V1list = []
V2list = []
V3list = []
V4list = []

for item in xlist:
    V1 = -V[0]*math.sin(2*math.pi*(item/L))
    V2 = -V[0]*math.sin(2*math.pi*(item/L)) + 0.25*math.sin(4*math.pi*(item/L))
    V3 = -V[0]*math.sin(2*math.pi*(item/L)) - F*item
    V4 = -V[0]*math.sin(2*math.pi*(item/L)) + 0.25*math.sin(4*math.pi*(item/L)) - F*item
    V1list.append(V1)
    V2list.append(V2)
    V3list.append(V3)
    V4list.append(V4)

legend = ("single sine", "double sine", "single sine - tilted", "double sine - tilted")
plt.plot(xlist, V1list, label = "single sine")
plt.plot(xlist, V2list, label = "double sine")
plt.plot(xlist, V3list, label = "single sine - tilted")
plt.plot(xlist, V4list, label = "double sine - tilted")
plt.hlines(0, -1, 1, 'black')
plt.xlabel("Position")
plt.ylabel("Potential")
plt.legend(legend)
plt.show()
"""

""" Problem 3 """
materialno = "1"
dr = 0.01
distlist = []

path = "/home/hwhite/git/python/ME416/HW1structures/" + materialno + ".xyz"
infile = open(path, 'r')
numatoms = int(infile.readline())
infile.readline()

complist = []
xlist = []
ylist = []
zlist = []

for line in infile:
    line = line.strip()

    if materialno == "3":
        line = line.split('  ')
    else:
        line = line.split('      ')

    complist.append(line[0])
    xlist.append(float(line[1]))
    ylist.append(float(line[2]))
    zlist.append(float(line[3]))

values, counts = np.unique(complist, return_counts = True)
print("Number of Components: ", len(values))

if materialno == "1":
    xref = 0.0
    yref = 0.0
    zref = 0.0
elif materialno == "2":
    xref = 0.0
    yref = 0.0
    zref = 0.0
elif materialno == "3":
    xref = 20.062
    yref = 28.66
    zref = 37.258
elif materialno == "4":
    xref = 26.866
    yref = 6.488
    zref = -0.001
elif materialno == "5":
    xref = 33.801441
    yref = 30.418772
    zref = 9.688134       

for count in range(0, len(xlist)):
    dist = math.sqrt((xlist[count] - xref)**2 + (ylist[count] - yref)**2 + (zlist[count] - zref)**2)
    distlist.append(dist)

x_range = max(xlist) - min(xlist)
y_range = max(ylist) - min(ylist)
z_range = max(zlist) - min(zlist)

longest_dist = 0
for item in distlist:
    if item > longest_dist:
        longest_dist = item

num_100shells = 0

numshells = math.ceil(longest_dist / (dr))
currentr = dr/2
shell_list = []
shell_num_list = []

for count in range(0, numshells):
    num_in_shell = 0
    
    inner_r = currentr - (dr/2)
    outer_r = currentr + (dr/2)

    for item in distlist:
        if item >= inner_r and item < outer_r:
            num_in_shell += 1
            if count < 100:
                num_100shells += 1
    
    shell_num_list.append(num_in_shell/(currentr**3))
    shell_list.append(currentr)
    currentr += (dr)

#systemvol = (4/3)*math.pi*longest_dist**3
#systemvol = x_range * y_range * z_range
#system_density = (numatoms/systemvol) * 10**24
print("System density: ", system_density, "atoms/cm^3")

peaklist = []
for count in range(0, len(shell_num_list)-1):
    current_gr = shell_num_list[count]
    next_gr = shell_num_list[count+1]
    if next_gr < current_gr:
        peaklist.append(shell_list[count])

adjustedpeaklist = []
for count in range(1, len(peaklist)):
    adjustedpeaklist.append(peaklist[count] - peaklist[0])

print("Material " + materialno)

try:
    print("1st nn:", round(adjustedpeaklist[0], 3))
    print("2nd nn:", round(adjustedpeaklist[1], 3))
    print("3rd nn:", round(adjustedpeaklist[2], 3))
    print("4th nn:", round(adjustedpeaklist[3], 3))
    print("5th nn:", round(adjustedpeaklist[4], 3))
    print("6th nn:", round(adjustedpeaklist[5], 3))
    print("7th nn:", round(adjustedpeaklist[6], 3))
    print("8th nn:", round(adjustedpeaklist[7], 3))
    print("9th nn:", round(adjustedpeaklist[8], 3))
    print("10th nn:", round(adjustedpeaklist[9], 3))

except:
    print("End of nn")

short_shell_list = []
short_shell_num_list = []
for count in range(5, len(shell_list)):
    short_shell_list.append(shell_list[count])
    short_shell_num_list.append(shell_num_list[count])

plt.plot(short_shell_list, short_shell_num_list)
plt.title("Material " + materialno)
plt.xlabel("r (A)")
plt.ylabel("g(r)")
plt.show()
