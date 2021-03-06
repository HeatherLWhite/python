"""USED IN FIGURES"""

""" This script is used to perform calculations on data from 
LAMMPS PMF.txt files that are then plotted. """

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

#########################################################################
########################### EDIT THESE VALUES ###########################

# !!!!!!!!!!!!!!!! 
#Be sure that these three lists are the same length and in the right order!

# Edit this list of paths for the PMF text files.

pmfPaths = [
    "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/PGN/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50/sr0_001/PMF.txt"
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
    float(3.83E-25),
    float(3.83E-25),
    float(3.83E-25),
    float(3.83E-25),
    float(3.83E-25),
    float(3.83E-25)
    ]

############################## STOP EDITING #############################
#########################################################################

##################################################################################################
### This function takes in a PMF.txt file, a strain rate, and an interplate volume. It returns ###
### lists for the time, total strain, and PMF (values, normalized by peak PMF, and normalized  ###
### by inter-plate volume).                                                                    ###
##################################################################################################

#return totalStrainList, pmfList, pmfNormPeakList, pmfNormVolList
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
    totalStrainList = []

    for item in timestepList:
        totalStrain = float(item) * strainRate * 4
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

########################################################
### This function divides lists by Avogadro's Number ###
########################################################

def divideAvogadro(inlist):
    avogadroNum = 6.022 * (10**23) * 1000
    outlist = []
    for index in range(0,len(inlist)):
        outlist.append(inlist[index] / avogadroNum)
    return(outlist)

################################################
### This section plots PMF-strain rate data. ###
################################################

numPlots = len(pmfPaths)

# Plot PMF vs total strain

legendList = []
colorlist = ['red', 'orange', 'green', 'blue', 'mediumvioletred', 'darkviolet']

for count in range(0,numPlots):
    
    legendList.append(str(strainRateList[count]))

    extractData(strainRateList[count], volumeList[count], pmfPaths[count])

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfNormVolList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[3]
    
    pmfNormVolList = divideAvogadro(pmfNormVolList)

    plt.plot(totalStrainList, pmfNormVolList)
    #plt.plot(totalStrainList, pmfList, c=colorlist[count])

#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.title("Strain Rates for N=50, \u03C3=0.05 chains/$nm^2$")
plt.xlabel("Total Displacement ($\AA$)")
plt.ylabel(r"$\psi$ (kCal/$m^3$)")
plt.text(-38, 320, "Strain Rate ($\AA$/fs)")
plt.text(30, 1e4, "N = 50 monomers")
plt.text(30, 0.5e4, "\u03C3 = 0.05 chains/$nm^2$")
plt.legend(legendList, bbox_to_anchor=(0.25, 0.8), bbox_transform=plt.gcf().transFigure)
plt.show()

# Plot PMF normalized by the plateu value vs total strain

legendList = []

for count in range(0,numPlots):

    legendList.append(str(strainRateList[count]) + " $\AA$/fs")

    extractData(strainRateList[count], volumeList[count], pmfPaths[count])

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfNormPeakList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[2]
    plt.plot(totalStrainList, pmfNormPeakList, linewidth = 2)
    #plt.plot(totalStrainList, pmfNormPeakList, c=colorlist[count])

#plt.title("Strain Rates for N=50, \u03C3=0.05 chains/$nm^2$")
plt.xticks(fontsize = 40, weight = "bold")
plt.xlabel("Total Displacement ($\AA$)", fontsize=40, weight = "bold")
plt.yticks(fontsize =40, weight = "bold")
plt.ylabel(r"$\psi$ / $\psi_{max}$", fontsize=40, weight = "bold")
#plt.legend(legendList)
plt.figure(figsize=(5,5))
plt.show()

# Plot PMF normalized by inter-plate volume vs total strain

legendList = []

for count in range(0,numPlots):

    legendList.append(str(strainRateList[count]))

    extractData(strainRateList[count], volumeList[count], pmfPaths[count])

    totalStrainList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[0]
    pmfNormVolList = extractData(strainRateList[count], volumeList[count], pmfPaths[count])[3]
    pmfNormVolListDivAvo = divideAvogadro(pmfNormVolList)

    plt.plot(totalStrainList, pmfNormVolListDivAvo, linewidth = 3)
    #plt.plot(totalStrainList, pmfNormVolListDivAvo, c=colorlist[count])


#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.title("Strain Rates for N=50, \u03C3=0.05 chains/$nm^2$")
plt.xlabel("Total Displacement ($\AA$)", fontsize = 25)
plt.xticks(fontsize = 20)
plt.ylabel(r"$\psi$ (kCal/$m^3$)", fontsize = 25)
plt.yticks(fontsize = 20)
plt.text(-45, 3.3e2, "Pulling Velocity ($\AA$/fs)", fontsize = 20)
#plt.text(30, 3e1, "N = 50 monomers")
#plt.text(30, 0, "\u03C3* = 0.05 chains/$nm^2$")
plt.legend(legendList, fontsize = 20, bbox_to_anchor=(0.25, 0.82), bbox_transform=plt.gcf().transFigure)
plt.show()
