"""
For analysis of the group/group output from stepwise PGN plate simulations. 
"""

import matplotlib.pyplot as plt
import numpy as np

######### VARIABLES ###############

# Number of timesteps per round of SMD
timesteps_per_SMDround = 1200000/40

# Strain rate being used
strainRate = 0.00005 # A/fs

# Number of PMF files in simulation
numFiles = 40

#equilibriumVolume = 3.8401E-25 # m^3

# File paths
path_nocycle = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/nocycle_noeq_run2/PMF.txt"
path_cycle_noeq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_noeq/Poly2Poly1/"
path_cycle_5keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_5keq/Poly2Poly1/"
path_cycle_50keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_50keq/Poly2Poly1/"
########## FUNCTIONS ###############

#return totalStrainList, pmfList for simulation with PMF output from SMD
def extractDataNoCycle(FCTpath, FCTstrainRate):

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
        fs_per_timestep = 4
        adjustedTimestep = item - timestepList[0]

        totalStrain = float(adjustedTimestep) * FCTstrainRate * fs_per_timestep
        totalStrain = round(totalStrain, 3)
        totalStrainList.append(totalStrain)

    return totalStrainList, pmfList

#return totalStrainList, pmfList for simulation with yforces
def extractDataCycle(FCTpath, FCTnumFiles, FCTstrainRate, FCTtimesteps_per_SMDround):

    currentSMDtimestep = 0
    timestepList = []
    yforceList = []

    for count1 in range(0, FCTnumFiles):

        fileName =  "GG_Poly2Poly1_Loop" + str(count1+1) + ".txt"
        filePath = FCTpath + fileName

        infile = open(filePath, 'r')
        infile.readline()
        infile.readline()
        line = infile.readline()
        line = line.strip()
        line = line.split(" ")
        yforce = float(line[2])
        infile.close()
        
        yforceList.append(-yforce)
        timestepList.append(currentSMDtimestep)
        currentSMDtimestep += FCTtimesteps_per_SMDround    
        
    fs_per_timestep = 4    
    totalStrainList = []

    for item in timestepList:
        totalStrain = item * FCTstrainRate * fs_per_timestep
        totalStrain = round(totalStrain, 3)
        totalStrainList.append(totalStrain)

    # Integration to get PMF from forces
    pmfList = [0] # Add zero at beginning so list has right number of elements

    for count2 in range(1, len(yforceList)):
        width = abs(totalStrainList[count2] - totalStrainList[count2-1])
        height = 0.5 * (yforceList[count2] + yforceList[count2-1])
        additionalPMF  = width * height
        runningPMF = pmfList[count2-1] + additionalPMF
        runningPMF = round(runningPMF, 3)
        pmfList.append(runningPMF)
    
    return totalStrainList, yforceList, pmfList

totalStrain_nocycle = extractDataNoCycle(path_nocycle, strainRate)[0]
PMF_nocycle = extractDataNoCycle(path_nocycle, strainRate)[1]

totalStrain_cycle_noeq = extractDataCycle(path_cycle_noeq, numFiles, strainRate, timesteps_per_SMDround)[0]
yforceList_cycle_noeq = extractDataCycle(path_cycle_noeq, numFiles, strainRate, timesteps_per_SMDround)[1]
PMF_cycle_noeq = extractDataCycle(path_cycle_noeq, numFiles, strainRate, timesteps_per_SMDround)[2]

totalStrain_cycle_5keq = extractDataCycle(path_cycle_5keq, numFiles, strainRate, timesteps_per_SMDround)[0]
yforceList_cycle_5keq = extractDataCycle(path_cycle_5keq, numFiles, strainRate, timesteps_per_SMDround)[1]
PMF_cycle_5keq = extractDataCycle(path_cycle_5keq, numFiles, strainRate, timesteps_per_SMDround)[2]

totalStrain_cycle_50keq = extractDataCycle(path_cycle_50keq, numFiles, strainRate, timesteps_per_SMDround)[0]
yforceList_cycle_50keq = extractDataCycle(path_cycle_50keq, numFiles, strainRate, timesteps_per_SMDround)[1]
PMF_cycle_50keq = extractDataCycle(path_cycle_50keq, numFiles, strainRate, timesteps_per_SMDround)[2]

############ PLOTS #######################

legendList = [
    "SMD PMF Output (no cycle)",
    "Calc. PMF (cycle, no eq)",
    "Calc. PMF (cycle, 5k ts eq)",
    "Calc. PMF (cycle, 50k ts eq)"
    ]

plt.scatter(totalStrain_nocycle, PMF_nocycle, s = 8)
plt.scatter(totalStrain_cycle_noeq, PMF_cycle_noeq, s = 8)
plt.scatter(totalStrain_cycle_5keq, PMF_cycle_5keq, s = 8)
plt.scatter(totalStrain_cycle_50keq, PMF_cycle_50keq, s = 8)

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.title("PMF Calculations for N=50, \u03C3=0.05 chains/$nm^2$", fontsize = 14)
plt.xlabel("Total Displacement ($\AA$)", fontsize = 14)
plt.xticks(fontsize = 14)
plt.ylabel(r"$\psi$ (kcal/mol)", fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(legendList, scatterpoints=4, fontsize = 10)
plt.show()