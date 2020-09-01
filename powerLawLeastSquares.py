"""
Least squares curve fitting for the power law, y=ax^b
"""
import math
import numpy as np

xList = [
    5.301, 
    5.000, 
    4.301, 
    4.000, 
    3.301, 
    3.000]


yList = [
    68564,
    70375,
    82096,
    91010,
    107857,
    157352
    ]

n = len(xList)

x_pList = []
y_pList = []

# Make lists of the natural logarithms of the x and y values
for count in range (0, n):
    xLN = np.log(xList[count])
    x_pList.append(xLN)
    yLN = np.log(yList[count])
    y_pList.append(yLN)

# Calculate relevant terms
sumx_pTimesy_p = 0
sumx_p = 0
sumy_p = 0
sumx_pSquared = 0

for count in range (0, n):
    sumx_pTimesy_p += (x_pList[count]*y_pList[count])
    sumx_p += (x_pList[count])
    sumy_p += (y_pList[count])
    sumx_pSquared += (x_pList[count]**2)
   
squaredSumx_p = (sumx_p)**2

# Calculate value of b

bTop = (n * sumx_pTimesy_p) - (sumx_p * sumy_p)
bBottom = (n * sumx_pSquared) - squaredSumx_p
b = bTop/bBottom

# Calculate value of a

aTop = sumy_p - (b * sumx_p)
a = math.exp(aTop/n)

print("Equation: y=ax^b")
print("a = " + str(a))
print("b = " + str(b))