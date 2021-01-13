"""
For analysis of the PMF output from stepwise PGN plate simulations. 
"""

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

#Simulation-specific constants
#currentStrainRate = 0.00005 # A/fs
#equilibriumVolume = 3.8401E-25 # m^3
path = "/mnt/c/Users/heath/Ubuntu/CL50GD0_05_Test10/PMF"

#Number of PMF files in simulationb
numFiles = 40

# Number of timesteps per pmf output
pmfOutputIncrement = 1000

#Combined PMF list
allPMF = []
#Combined timestep list
allTimestep = []

def combineFiles(fctNumFiles, fctPath, fctpmfOutputIncrement):

    #Timestep increment info for PMF output
    pmfCurrentOutputTimestep = 0

    for count in range(1,numFiles+1):
        infilePath = fctPath + "/PMF" + str(count) + ".txt"
        infile = open(infilePath, 'r')

        if count == 1:
            line1 = infile.readline()
            line2 = infile.readline()
        else:
            infile.readline()
            infile.readline()

        for line in infile:
            line = line.strip()
            line = line.split(" ")
            #timestep = int(line[0])
            pmf = float(line[1])
            #allTimestep.append(timestep)
            allPMF.append(pmf)
            allTimestep.append(pmfCurrentOutputTimestep)
            pmfCurrentOutputTimestep += fctpmfOutputIncrement

    outfileName = "AllPMF.txt"
    outfile = open(fctPath+"/"+outfileName, 'w')
    outfile.write(line1+line2)
    
    for index in range(0,len(allPMF)):
        outfile.write(str(allTimestep[index]) + "\t" + str(allPMF[index]) + "\n")

    infile.close()
    outfile.close()

combineFiles(numFiles, path, pmfOutputIncrement)