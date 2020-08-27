""" This script is used to perform calculations on data from LAMMPS 
PMF.txt files that is then output into a csv file that can be pasted into
Excel. In addition to combining the data, the script calculates the
time, total strain, and normalized PMF (by peak and volume) given a strain 
rate and a plate-plate volume. """

import csv

##########################################
### This section is for file handling. ###
##########################################

#########################
### EDIT THESE VALUES ###
STRAINRATE = float(0.000005)
VOLUME = float(5.25E-25)
infile = open("/mnt/c/Users/heath/Ubuntu/PMF.txt", 'r')
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

##############################################################
### This section combines the small lists into a big list. ###
##############################################################

totalList = []

totalList.append("SR (A/fs)" + "\t" + str(STRAINRATE) + "\t" + "Plateau PMF" + 
    "\t" + str(pmfMean) + "\t" + "Plate-plate vol (m^3)" + "\t" + str(VOLUME))

totalList.append("TimeStep" + "\t" + "Time (fs)" + "\t" + "Total strain (A)" + 
    "\t" + "PMF (kCal/mol)" + "\t" + "PMF norm (vol)" + "\t" + "PMF norm (peak)")

for item in range (numTimesteps):
    totalList.append(str(timestepList[item]) + '\t' + str(timeList[item]) + '\t' 
        + str(totalStrainList[item]) + '\t' + str(pmfList[item]) + '\t' 
        + str(pmfNormVolList[item]) + "\t" + str(pmfNormPeakList[item]))

####################################################
### This section writes data to the output file. ###
####################################################

with open('output_' + str(STRAINRATE) + '.csv', mode = 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in totalList:
        writer.writerow([item])

# Close the output file after writing is finished.
csvfile.close()