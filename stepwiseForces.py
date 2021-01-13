"""
For analysis of the smdforces output from stepwise PGN plate simulations. 
From a set of files, compiles the first entry from each into a single file.
"""

import matplotlib.pyplot as plt
import numpy as np

#return totalStrainList, pmfList
def extractPMFData(FCTpath, FCTstrainRate):

    infile = open(FCTpath, 'r')
    infile.readline()
    infile.readline()

    timestepList = []
    pmfList = []

    for line in infile:
        line = line.strip()
        line = line.split(" ")
        
        timestep = int(line[0])
        pmf = float(line[1])

        timestepList.append(timestep)
        pmfList.append(pmf)

    infile.close()

    numTimesteps = len(timestepList)
    totalStrainList = []

    for item in timestepList:
        adjustedTimestep = item - timestepList[0]

        totalStrain = float(adjustedTimestep) * FCTstrainRate
        totalStrain = round(totalStrain, 3)
        totalStrainList.append(totalStrain)

    return totalStrainList, pmfList

path = "/mnt/c/Users/heath/Ubuntu/CL50GD0_05_Test13/smdforces"
OGpath = "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_00005/PMF.txt"

#Number of PMF files in simulationb
numFiles = 40

#Strain rate being used
OGstrainRate = 0.00005 # A/fs
SWstrainRate = 0.00005

#equilibriumVolume = 3.8401E-25 # m^3

# Number of timesteps per pmf output
outputIncrement = 1000
currentIncrement = 0

# Number of timesteps in 1 round smd
currentsmdTimestep = 1200000/40
smdTimesteps = 1200000/40

#Combined Force list
allYForces = [] #Kcal/mole-Angstrom

#Combined timestep list
allTimestep = []

#Total displacement list
totalDisp = [] #Angstrom

#PMF list
pmfList = [] #Kcal/mole


for count in range(1,numFiles+1):
    
    disp = currentsmdTimestep*SWstrainRate
    totalDisp.append(disp)
    currentsmdTimestep += smdTimesteps
    
    infilePath = path + "/smdforces" + str(count) + ".txt"
    infile = open(infilePath, 'r')

    for count3 in range(0,32):
        infile.readline()

    myline = infile.readline()
    print(myline)
    infile.close

    myline = myline.strip()
    myline = myline.split(" ")
    Yforce = float(myline[2])
    allYForces.append(Yforce)
    
    pmf = Yforce * disp
    pmfList.append(pmf)

revised_pmfList = []
for item in pmfList:
    revised_pmfList.append(item)

for count2 in range(0,len(pmfList)):
    if count2 == 0:
        revised_pmfList[count2] = revised_pmfList[count2]
    else:
        revised_pmfList[count2] += revised_pmfList[count2-1]

OGtotalDispList = extractPMFData(OGpath, OGstrainRate)[0]
OGpmfList = extractPMFData(OGpath, OGstrainRate)[1]

# Plot PMF vs total strain
plt.scatter(totalDisp, revised_pmfList, c = "C3", label = "stepwise (cumulative)")
plt.scatter(OGtotalDispList, OGpmfList, c = "C1", label = "continuous")
plt.scatter(totalDisp, pmfList, c = "C0", label = "stepwise (noncumulative)")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.title("CL = 50, GD = 0.05" + "\n" + "Strain Rate = 0.00005 A/fs")
plt.legend()
plt.xlabel("Total Displacement (A)")
plt.ylabel("\u03A8 (kcal/mol)")
plt.show()