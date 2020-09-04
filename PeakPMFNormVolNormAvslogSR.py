import matplotlib.pyplot as plt
import numpy as np

#########################################################################
########################### EDIT THESE VALUES ###########################

# Edit this list of paths for the PMF text files.

pmfPathsL20 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L20/sr0_001/PMF.txt"
    ]

pmfPathsL30 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L30/sr0_001/PMF.txt"
    ]

pmfPathsL40 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L40/sr0_001/PMF.txt"
    ]

pmfPathsL50 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L50/sr0_001/PMF.txt"
    ]

pmfPathsL60 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L60/sr0_001/PMF.txt"
    ]

pmfPathsL70 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/sr0_000005_rerun3/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/rerun1/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/rerun1/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/rerun1/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/rerun1/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/sr0_001_rerun3/PMF.txt"
    ]

pmfPathsL80 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L80/rerun1/sr0_001/PMF.txt"
    ]

pmfPathsL90 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_00001-rerun/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L90/sr0_001/PMF.txt"
    ]

pmfPathsL100 = [
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L100/sr0_001/PMF.txt"
    ]

pmfPathsList = [
    pmfPathsL20,
    pmfPathsL30,
    pmfPathsL40,
    pmfPathsL50,
    pmfPathsL60,
    pmfPathsL70,
    pmfPathsL80,
    pmfPathsL90,
    pmfPathsL100
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

paramAList = [
    1.94290782e+28,
    3.55543153e+28,
    4.24569737e+28,
    5.46194143e+28,
    5.56408111e+28,
    7.73819166e+28,
    7.35449061e+28,
    8.08363391e+28,
    8.90252852e+28
    ]

############################## STOP EDITING #############################
#########################################################################

##################################################################################################
### This function takes in a PMF.txt file, a strain rate, and an interplate volume. It returns ###
### lists for the total strain, and PMF (values, normalized by peak PMF, and normalized        ###
### by inter-plate volume).                                                                    ###
### return totalStrainList, pmfList, pmfNormPeakList, pmfNormVolList                           ###
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
    for index in range(10, len(pmfList)):
        if abs(pmfList[index] - pmfList[index-10]) < 20:
            pmfPeakIndex = index - 3
            pmfPeakValue = pmfList[index-3]
            break
        else:
            pmfPeakIndex = None
            pmfPeakValue = None
    return pmfPeakIndex, pmfPeakValue

"""
pmfPeakListSR0_000005 = []
pmfPeakListSR0_00001 = []
pmfPeakListSR0_00005 = []
pmfPeakListSR0_0001 = []
pmfPeakListSR0_0005 = []
pmfPeakListSR0_001 = []

peakListNamesSR = [
    pmfPeakListSR0_000005,
    pmfPeakListSR0_00001,
    pmfPeakListSR0_00005,
    pmfPeakListSR0_0001,
    pmfPeakListSR0_0005,
    pmfPeakListSR0_001
    ]   
"""

pmfPeakListL20 = []   
pmfPeakListL30 = []
pmfPeakListL40 = []
pmfPeakListL50 = []
pmfPeakListL60 = []
pmfPeakListL70 = []
pmfPeakListL80 = []
pmfPeakListL90 = []
pmfPeakListL100 = []

peakListNamesCL = [
    pmfPeakListL20,
    pmfPeakListL30,
    pmfPeakListL40,
    pmfPeakListL50,
    pmfPeakListL60,
    pmfPeakListL70,
    pmfPeakListL80,
    pmfPeakListL90,
    pmfPeakListL100
    ]

count1 = 0

"""
# Open file
fileName = "/mnt/c/Users/heath/Ubuntu/PeakPMFNormVolAllCL_PMFvsSR_RawData.txt"
outFile = open(fileName, "w")
outFile.write("Strain Rate (A/fs)" + '\t' + "Peak PMF L=20" + '\t' + "Peak PMF L=30" + '\t' 
    + "Peak PMF L=40" + '\t' + "Peak PMF L=50" + '\t' + "Peak PMF L=60" + '\t' + "Peak PMF L=70" 
    + '\t' + "Peak PMF L=80" + '\t' + "Peak PMF L=90" + '\t' + "Peak PMF L=100" + "\n")
"""

# Extract and sort all needed data

for pathSet in pmfPathsList:
    count2 = 0

    for path in pathSet:
        # Create lists of relevant data
        pmfList = extractData(strainRateList[count2], volumeList[count1], pathSet[count2])[1]
        pmfNormVolList = extractData(strainRateList[count2], volumeList[count1], pathSet[count2])[3]
    
        # Determine where PMF plateau begins
        pmfPeakStartIndex = findPMFPeakIndex(pmfList)[0]

        # Determine average peak PMF value and add to list
        summation = 0
        
        for item in range(pmfPeakStartIndex, len(pmfList)):
            summation += pmfNormVolList[item]
        
        avgPeakPMFValue = summation / (len(pmfList) - (pmfPeakStartIndex+1))

        #peakListNamesSR[count2].append(avgPeakPMFValue)

        peakListNamesCL[count1].append((avgPeakPMFValue)-(paramAList[count1]))

        count2 += 1

    plt.scatter(strainRateList, peakListNamesCL[count1])
    
    count1 += 1

"""
for count in range (0,6):
    strainRateList[count] = str(strainRateList[count])
    pmfPeakListL20[count] = str(pmfPeakListL20[count])
    pmfPeakListL30[count] = str(pmfPeakListL30[count])
    pmfPeakListL40[count] = str(pmfPeakListL40[count])
    pmfPeakListL50[count] = str(pmfPeakListL50[count])
    pmfPeakListL60[count] = str(pmfPeakListL60[count])
    pmfPeakListL70[count] = str(pmfPeakListL70[count])
    pmfPeakListL80[count] = str(pmfPeakListL80[count])
    pmfPeakListL90[count] = str(pmfPeakListL90[count])
    pmfPeakListL100[count] = str(pmfPeakListL100[count])

    outFile.write(strainRateList[count] + '\t' + pmfPeakListL20[count] + '\t' + pmfPeakListL30[count] + '\t' + pmfPeakListL40[count]
        + '\t' + pmfPeakListL50[count] + '\t' + pmfPeakListL60[count] + '\t' + pmfPeakListL70[count] + '\t' + pmfPeakListL80[count]
        + '\t' + pmfPeakListL90[count] + '\t' + pmfPeakListL100[count] + '\n')

outFile.close()
"""

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.title("Peak PMF vs Strain Rate")
plt.xlabel("Strain Rate (A/fs)")
plt.xscale("log")
plt.xlim(xmin = 10e-7, xmax=0.002)
plt.ylabel("Peak PMF, normalized by volume (m^2) minus parameter 'a'")
legendList = ["N=20", "N=30", "N=40", "N=50", "N=60", "N=70", "N=80", "N=90", "N=100"]
plt.legend(legendList)
plt.show()