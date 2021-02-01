"""
Heather White
ME 416
Homework 1
Problem 3
Due 2-2-2020
"""
import matplotlib.pyplot as plt
import numpy as np
import math
import decimal
import decimal as d
from random import seed
from random import random

""" Problem 4 """
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
