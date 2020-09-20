""" This script is used to perform calculations on data from 
LAMMPS PMF.txt files that are then plotted. """

import matplotlib.pyplot as plt
import numpy as np

#########################################################################
########################### EDIT THESE VALUES ###########################

# !!!!!!!!!!!!!!!! 
#Be sure that these three lists are the same length and in the right order!

# Edit this list of paths for the PMF text files.

pmfPaths = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/graft_density_variation/gd0-10_L50/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/graft_density_variation/gd0-10_L50/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/graft_density_variation/gd0-10_L50/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/graft_density_variation/gd0-10_L50/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/graft_density_variation/gd0-10_L50/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/graft_density_variation/gd0-10_L50/sr0_001/PMF.txt"
    ]

# Edit this list of strain rates for the PMF text files.
# Units are in A/fs.

strainRateList = [
    float(0.000005),
    float(0.00001),
    float(0.00005),
    float(0.0001),
    float(0.0005),
    float(0.001)
    ]

# Edit this list of inter-plate volumes for the PMF text files.
# Units are in m^3.

volumeList = [
    float(7.35E-25),
    float(7.35E-25),
    float(7.35E-25),
    float(7.35E-25),
    float(7.35E-25),
    float(7.35E-25)
    ]

############################## STOP EDITING #############################
#########################################################################

##################################################################################################
### This function takes in a PMF.txt file, a strain rate, and an interplate volume. It returns ###
### lists for the time, total strain, and PMF (values, normalized by peak PMF, and normalized  ###
### by inter-plate volume).                                                                    ###
##################################################################################################

def extractData(strainRate, volume, path):

    ##########################################
    ### This section is for file handling. ###
    ##########################################

    infile = open(path, 'r')
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

        totalStrain = float(adjustedTimestep) * strainRate
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
        pmfNormVol = item / volume
        pmfNormPeak = round(pmfNormPeak, 3)
        pmfNormVol = round(pmfNormVol, 3)
        pmfNormPeakList.append(pmfNormPeak)
        pmfNormVolList.append(pmfNormVol)

    return totalStrainList, pmfList, pmfNormPeakList, pmfNormVolList

################################################
### This section plots PMF-strain rate data. ###
################################################

numPlots = len(pmfPaths)

# Plot PMF vs total strain

legendList = []

for count in range(0,numPlots):
    
    legendList.append("SR = " + str(strainRateList[count]) + " A/fs")

    extractData(strainRateList[count], volumeList[count], pmfPaths[count])

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[1]
    plt.plot(totalStrainList, pmfList)

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.title("PMF vs Total Strain")
plt.xlabel("Total Strain (A)")
plt.ylabel("PMF (kCal/mol)")
plt.legend(legendList)
plt.show()

# Plot PMF normalized by the plateu value vs total strain

legendList = []

for count in range(0,numPlots):

    legendList.append("SR = " + str(strainRateList[count]) + " A/fs")

    extractData(strainRateList[count], volumeList[count], pmfPaths[count])

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfNormPeakList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[2]
    plt.plot(totalStrainList, pmfNormPeakList)

plt.title("Normalized PMF (plateau) vs Total Strain")
plt.xlabel("Total Strain (A)")
plt.ylabel("PMF")
plt.legend(legendList)
plt.show()

# Plot PMF normalized by inter-plate volume vs total strain

legendList = []

for count in range(0,numPlots):

    legendList.append("SR = " + str(strainRateList[count]) + " A/fs")

    extractData(strainRateList[count], volumeList[count], pmfPaths[count])

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfNormVolList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[3]
    plt.plot(totalStrainList, pmfNormVolList)

plt.title("Normalized PMF (vol) vs Total Strain")
plt.xlabel("Total Strain (A)")
plt.ylabel("PMF (kCal/mol-m^3)")
plt.legend(legendList)
plt.show()