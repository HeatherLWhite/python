
""" This script is used to perform calculations on data from 
LAMMPS PMF.txt files that are then plotted. """

import matplotlib.pyplot as plt
import numpy as np

##########################################
### This section is for file handling. ###
##########################################

#########################
### EDIT THESE VALUES ###
STRAINRATE = float(0.000005)
VOLUME = float(5.96E-25)
infile = open("/mnt/c/Users/heath/Ubuntu/gd0-05_L80/rerun1/sr0_000005/PMF.txt", 'r')
#########################

infile.readline()
infile.readline()

#################################################################################################
### This section reads in each line from the PMF.txt file creates lists for timestep and PMF. ###
#################################################################################################

timestepList = []
pmfList = []

for line in infile:
    line = line.strip()
    line = line.split(" ")
    
    timestep = int(line[0])
    pmf = float(line[1])

    timestepList.append(timestep)
    pmfList.append(pmf)

# Close the input file
infile.close()

####################################################################################################
### This section calculates the elapsed time (in fs) from the timesteps, as well as total strain ###
####################################################################################################

numTimesteps = len(timestepList)
timeList = []
totalStrainList = []

for item in timestepList:
    adjustedTimestep = item - timestepList[0]
    timeList.append(adjustedTimestep)

    totalStrain = float(adjustedTimestep) * STRAINRATE
    totalStrain = round(totalStrain, 3)
    totalStrainList.append(totalStrain)


#####################################################################################################
### This section calculates the mean PMF from the last 100 data entries to be the peak PMF value. ###
#####################################################################################################

pmfSum = 0

for item in range(numTimesteps-51, numTimesteps-1):
    pmfSum += pmfList[item]

pmfMean = pmfSum/50
pmfMean = round(pmfMean, 3)

##############################################################################
### This section calculates the normalized PMF by dividing each PMF entry ###
### by the peak PMF value and by the plate-plate volume.                  ### 
#############################################################################

pmfNormPeakList = []
pmfNormVolList = []

for item in pmfList:
    pmfNormPeak = item / pmfMean
    pmfNormVol = item / VOLUME
    pmfNormPeak = round(pmfNormPeak, 3)
    pmfNormVol = round(pmfNormVol, 3)
    pmfNormPeakList.append(pmfNormPeak)
    pmfNormVolList.append(pmfNormVol)

#################################################
### This section creates plots from the data. ###
#################################################

plt.plot(timeList, pmfList)
plt.title('PMF vs Time')
plt.xlabel('Time (fs)')
plt.ylabel('PMF (kcal/mol)')
plt.show()

plt.plot(timeList, pmfNormPeakList)
plt.title('PMF (norm by peak) vs Time')
plt.xlabel('Time (fs)')
plt.ylabel('PMF')
plt.show()

plt.plot(timeList, pmfNormVolList)
plt.title('PMF (norm by vol) vs Time')
plt.xlabel('Time (fs)')
plt.ylabel('PMF (kcal/mol-m^3)')
plt.show()