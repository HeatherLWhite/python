"""
Heather White
ME 416
Homework 1
Problem 2
Due 2-2-2020
"""
import matplotlib.pyplot as plt
import numpy as np
import math
import decimal
import decimal as d
from random import seed
from random import random

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
