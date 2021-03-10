"""
Heather White
ME 416
Homework 1
Problem 4
Due 2-2-2020
"""
import matplotlib.pyplot as plt
import numpy as np
import math

materialno = "4"

if materialno == "1":
    dr = 0.01
elif materialno == "2":
    dr = 0.1
elif materialno == "3":
    dr = 0.01
elif materialno == "4":
    dr = 0.01
elif materialno == "5":
    dr = 0.01

distlist = []

path = "/home/hwhite/git/python/ME416/HW1structures/" + materialno + ".xyz"
infile = open(path, 'r')
numatoms = int(infile.readline())
infile.readline()

xlist = []
ylist = []
zlist = []

if materialno == "1":
    xref = 0.0
    yref = 0.0
    zref = 0.0
elif materialno == "2":
    xref = 50.12009
    yref = -33.2245
    zref = 14.11152
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

for line in infile:
    line = line.strip()

    if materialno == "3":
        line = line.split('  ')
    else:
        line = line.split('      ')

    xlist.append(float(line[1]))
    ylist.append(float(line[2]))
    zlist.append(float(line[3]))

for count in range(0, len(xlist)):
    dist = math.sqrt((xlist[count] - xref)**2 + (ylist[count] - yref)**2 + (zlist[count] - zref)**2)
    distlist.append(dist)

longest_dist = max(distlist)
shortest_dist = min(distlist)
print("Longest distance: ", longest_dist)
print("Shortest distance: ", shortest_dist)

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
    
    shell_num_list.append(num_in_shell/(currentr**3))
    shell_list.append(currentr)
    currentr += (dr)

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
    print("1st nn:", round(adjustedpeaklist[0], 4))
    print("2nd nn:", round(adjustedpeaklist[1], 4))
    print("3rd nn:", round(adjustedpeaklist[2], 4))
    print("4th nn:", round(adjustedpeaklist[3], 4))
    print("5th nn:", round(adjustedpeaklist[4], 4))
    print("6th nn:", round(adjustedpeaklist[5], 4))
    print("7th nn:", round(adjustedpeaklist[6], 4))
    print("8th nn:", round(adjustedpeaklist[7], 4))
    print("9th nn:", round(adjustedpeaklist[8], 4))
    print("10th nn:", round(adjustedpeaklist[9], 4))

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
plt.xlim(shortest_dist, longest_dist)
plt.ylabel("N/$r^3$")
plt.show()
