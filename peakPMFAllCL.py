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
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/rerun1_gd0-05_L60/sr0_000005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/rerun1_gd0-05_L60/sr0_00001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/rerun1_gd0-05_L60/sr0_00005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/rerun1_gd0-05_L60/sr0_0001/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/rerun1_gd0-05_L60/sr0_0005/PMF.txt",
    "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/rerun1_gd0-05_L60/sr0_001/PMF.txt"
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

pmfPeakListSR0_000005 = []
pmfPeakListSR0_00001 = []
pmfPeakListSR0_00005 = []
pmfPeakListSR0_0001 = []
pmfPeakListSR0_0005 = []
pmfPeakListSR0_001 = []

peakListNames = [
    pmfPeakListSR0_000005,
    pmfPeakListSR0_00001,
    pmfPeakListSR0_00005,
    pmfPeakListSR0_0001,
    pmfPeakListSR0_0005,
    pmfPeakListSR0_001
    ]   

count1 = 0

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
            summation += pmfList[item]
        
        avgPeakPMFValue = summation / (len(pmfList) - (pmfPeakStartIndex+1))
        peakListNames[count2].append(avgPeakPMFValue)
        
        count2 += 1

    count1 += 1

# Plot average peak PMF value vs chain length in a bar chart
xMarkerList = ["N=20", "N=30", "N=40", "N=50", "N=60", "N=70", "N=80", "N=90", "N=100"]
legendList = ["SR=0.000005 A/fs", "SR=0.00001 A/fs", "SR=0.00005 A/fs", "SR=0.0001 A/fs", "SR=0.0005 A/fs", "SR=0.001 A/fs"]
N = 9
ind = np.arange(N)
width = 0.14

plt.bar(ind+0*width, pmfPeakListSR0_000005, width, label = "SR=0.000005 A/fs")
plt.bar(ind+1*width, pmfPeakListSR0_00001, width, label = "SR=0.00001 A/fs")
plt.bar(ind+2*width, pmfPeakListSR0_00005, width, label = "SR=0.00005 A/fs")
plt.bar(ind+3*width, pmfPeakListSR0_0001, width, label = "SR=0.0001 A/fs")
plt.bar(ind+4*width, pmfPeakListSR0_0005, width, label = "SR=0.0005 A/fs")
plt.bar(ind+5*width, pmfPeakListSR0_001, width, label = "SR=0.001 A/fs")

print(pmfPeakListSR0_000005)
print(pmfPeakListSR0_00001)
print(pmfPeakListSR0_00005)
print(pmfPeakListSR0_0001)
print(pmfPeakListSR0_0005)
print(pmfPeakListSR0_001)

plt.xlabel("Chain Length")
plt.xticks(ind+0.4, xMarkerList)
plt.ylabel("Peak PMF (kCal/mol)")
plt.title("Peak PMF vs Chain Length")
plt.legend(legendList, facecolor = "white", framealpha = 1)
plt.grid(b=None, which='major', axis='y')

plt.show()