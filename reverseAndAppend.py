"""
This script is used to combine tensile and compressive LAMMPS PMF text files.
In order to do this, the compressive file must be reversed so that it flows into the tensile file.
"""

import matplotlib.pyplot as plt
import numpy as np

##########################################
### This section is for file handling. ###
##########################################

# Tensile file
pathTensile = "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tensile/chain_length_variation/gd0-05_L70/sr0_001_rerun3/PMF.txt"

# Compressive file
pathCompress = "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/compression/chain_length_variation/gd0-05_L70/sr0_001/PMF.txt"

# Combined file
pathCombined = "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L70/sr0_001/PMF.txt"

infileTensile = open(pathTensile, 'r')
line1 = infileTensile.readline()
line2 = infileTensile.readline()

infileCompress = open(pathCompress, 'r')
infileCompress.readline()
infileCompress.readline()

outfile = open(pathCombined, 'w')

#################################################################################################
### This section reads in each line from the PMF.txt file creates lists for timestep and PMF. ###
#################################################################################################

# Tension
timestepListTensile = []
pmfListTensile = []

for line in infileTensile:
    line = line.strip()
    line = line.split(" ")
    
    timestep = int(line[0])
    pmf = float(line[1])

    timestepListTensile.append(timestep)
    pmfListTensile.append(pmf)

infileTensile.close()

# Compression
timestepListCompress = []
pmfListCompress = []

for line in infileCompress:
    line = line.strip()
    line = line.split(" ")
    
    timestep = int(line[0])
    pmf = float(line[1])

    timestepListCompress.append(timestep)
    pmfListCompress.append(pmf)

infileCompress.close()    

########################################################################
### This section ajusts the compressive lists to a reasonable range. ###
########################################################################

peakPMFEstimate = pmfListTensile[len(pmfListTensile) - 1]

for item in pmfListCompress:
    if item > (2*peakPMFEstimate):
        stopIndex = pmfListCompress.index(item)
        break

pmfListCompressShort = []
timestepListCompressShort = []

for item in range(0,stopIndex):
    pmfListCompressShort.append(pmfListCompress[item])
    timestepListCompressShort.append(timestepListCompress[item])

# for index in range(0,stopIndex):
#     print(timestepListCompressShort[index], pmfListCompressShort[index])

########################################################################
### This section adjusts the timesteps in the files for consistency. ###
########################################################################

# Compressive values

adjustmentCompress = timestepListCompressShort[0]

pmfListCompressShort.reverse()
timestepListCompressShort.reverse()

for count in range(0, len(timestepListCompressShort)):
    timestepListCompressShort[count] = timestepListCompressShort[count] * -1 + adjustmentCompress

# Tensile values

adjustmentTensile = timestepListTensile[0]

for count in range(0, len(timestepListTensile)):
    timestepListTensile[count] = timestepListTensile[count] - adjustmentTensile

###############################################################
### This section combines the tensile and compressive data. ###
###############################################################

pmfListCombined = []
for item in pmfListCompressShort:
    pmfListCombined.append(item)

for item in pmfListTensile:
    pmfListCombined.append(item)

timestepListCombined = []
for item in timestepListCompressShort:
    timestepListCombined.append(item)

for item in timestepListTensile:
    timestepListCombined.append(item)

# plt.plot(timestepListCombined, pmfListCombined)
# plt.show()

######################################
### Print data to a new text file. ###
######################################

outfile.write(line1 + line2)
for count in range(0, len(timestepListCombined)):
    outfile.write(str(timestepListCombined[count]) + ' ' + str(pmfListCombined[count]) + '\n')

outfile.close()