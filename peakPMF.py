""" This script determines the peak PMF value from a set of PMF lists from simulations 
    different chain lengths. It then plots the PMF (normalized by inter-plate volume)
    vs total strain in a scatter plot, as well as peak PMF values vs chain length in a 
    bar chart."""

import matplotlib.pyplot as plt
import numpy as np

#########################################################################
########################### EDIT THESE VALUES ###########################

# !!!!!!!!!!!!!!!! 
#Be sure that these three lists are the same length and in the right order!

# Edit this list of paths for the PMF text files.

pmfPaths = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/rerun1/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_00005/PMF.txt"
    ]

# Edit this list of strain rates for the PMF text files.
# Units are in A/fs.

strainRateList = [
    float(0.00005),
    float(0.00005),
    float(0.00005),
    float(0.00005),
    float(0.00005),
    float(0.00005),
    float(0.00005),
    float(0.00005),
    float(0.00005)
]

# Edit this list of inter-plate volumes for the PMF text files.
# Units are in m^3.

volumeList = [
    float(1.73E-25),
    float(2.43E-25),
    float(3.14E-25),
    float(3.84E-25),
    float(4.56E-25),
    float(5.25E-25),
    float(5.96E-25),
    float(6.64E-25),
    float(7.37E-25)
    ]

############################## STOP EDITING #############################
#########################################################################


##################################################################################################
### This function takes in a PMF.txt file, a strain rate, and an interplate volume. It returns ###
### lists for the total strain, and PMF (values, normalized by peak PMF, and normalized        ###
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

##################################################################################################
### This function returns the index and value of the beginning of the PMF curve plateau given  ###
### a list of PMF values.                                                                      ###
##################################################################################################

def findPMFPeakIndex(pmfList):
    for index in range(3, len(pmfList)):
        if abs(pmfList[index] - pmfList[index-3]) < 20:
            pmfPeakIndex = index - 3
            pmfPeakValue = pmfList[index-3]
            break
    return pmfPeakIndex, pmfPeakValue

pmfPeakList = []

for count in range(0, len(pmfPaths)):
    
    # Create lists of relevant data

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[1]
    pmfNormVolList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[3]
    
    # Determine where PMF plateau begins
    pmfPeakStartIndex = findPMFPeakIndex(pmfList)[0]
    
    # Determine average peak PMF value and add to list
    summation = 0
    
    for item in range(pmfPeakStartIndex, len(pmfList)):
        summation += pmfList[item]
    
    avgPeakPMFValue = summation / (len(pmfList) - (pmfPeakStartIndex+1))
    pmfPeakList.append(avgPeakPMFValue)

    # Plot PMF (norm by volume) vs total strain across all chain lengths

    legendList = ["N=20", "N=30", "N=40", "N=50", "N=60", "N=70", "N=80", "N=90", "N=100"]

    plt.plot(totalStrainList, pmfNormVolList)
    plt.title("Normalized PMF (vol) vs Total Strain")
    plt.xlabel("Total Strain (A)")
    plt.ylabel("PMF (kCal/mol-m^3)")
    plt.legend(legendList)

plt.show()

# Plot average peak PMF value vs chain length in a bar chart

legendList = ["N=20", "N=30", "N=40", "N=50", "N=60", "N=70", "N=80", "N=90", "N=100"]
plt.bar(legendList, pmfPeakList)
plt.xlabel("Chain Length")
plt.ylabel("Peak PMF (kCal/mol)")
plt.title("Peak PMF vs Chain Length")
plt.show()