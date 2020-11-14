import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def divideAvogadro(inlist):
    avogadroNum = 6.022 * (10**23) * 1000
    outlist = []
    for index in range(0,len(inlist)):
        outlist.append(inlist[index] / avogadroNum)
    return(outlist)

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
        totalStrain = float(item) * strainRate
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
# return totalStrainList, pmfList, pmfNormPeakList, pmfNormVolList
# Cannot trust pmfNormPeakList here - peak pmf is not in shortened data file

def func(x, k):
    return 0.5 * k * x**2

for choice in range(0,6):

    pathList = ["sr0_000005", "sr0_00001", "sr0_00005", "sr0_0001", "sr0_0005", "sr0_001"]
    pmfPath = "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50-TotalDisp2A/"+pathList[choice]+"/PMF.txt"
    SRList = [0.000005, 0.00001, 0.00005, 0.0001, 0.0005, 0.001]
    peakList = [5.42E28, 6.06E28, 7.06E28, 7.48E28, 8.98E28, 1.04E29]
    volume = 3.8401E-25 #N = 50, norm by volume
    #peakList = divideAvogadro(peakList)
    strainRate = SRList[choice]
    peakPMF = peakList[choice]
    

    xlist = []  # Total displacement
    ylist = []  # PMF norm peak value

    for item in extractData(strainRate, volume, pmfPath)[0]: # Returns totalStrainList
        xlist.append(item)

    for item in extractData(strainRate, volume, pmfPath)[3]: # Returns pmfList norm vol
        ylist.append(item)

    # Normalize pmfList by peakPMF
    for index in range(0, len(ylist)):
        ylist[index] = ylist[index] / peakPMF
    
    params, params_covariance = curve_fit(func, xlist, ylist, p0=None, maxfev=10000)

    print("Strain Rate: " + str(strainRate))
    print("Inter-Plate Volume: " + str(volume))
    print("Peak PMF value: " + str(peakPMF))
    print("k value: " + str(params) + "\n")
    
    xdummy = np.linspace(-2, 2, 1000)
    ydummy = []
    k = params

    for item in xdummy:
        ydummy.append(0.5 * k * item**2)

    legendList1 = [
        "0.000005   5.636e-3   1.000", 
        "0.00001     5.567e-3   0.988", 
        "0.00005     5.851e-3   1.038", 
        "0.0001       6.278e-3   1.114", 
        "0.0005       7.141e-3   1.267", 
        "0.001         7.977e-3   1.415"
        ]
 
    plt.plot(xdummy,ydummy, linewidth = 3)
    
    plt.xlabel("Total Displacement ($\AA$)")
    plt.ylabel(r"$\psi$ / $\psi_{max}$")
    #plt.ylim(-10E-27, 1.75E-25)
    plt.legend(legendList1, loc = "upper center", bbox_to_anchor=(0.50, 0.92))
        
plt.show()

######################################3
    

pmfPath = "/mnt/c/Users/heath/Ubuntu/SimulationResults/heather_sim/tension_and_compression/chain_length_variation/gd0-05_L50-TotalDisp2A/sr0_00005/PMF.txt"
strainRate = 0.00005
peakPMF = peakList[2]
volume = 3.8401E-25 #N = 50

xlist = []  # Total displacement
ylist = []  # PMF norm peak value

for item in extractData(strainRate, volume, pmfPath)[0]: # Returns totalStrainList
    xlist.append(item)

for item in extractData(strainRate, volume, pmfPath)[3]: # Returns pmfList norm vol
    ylist.append(item)

# Normalize pmfList by peakPMF
for index in range(0, len(ylist)):
    ylist[index] = ylist[index] / peakPMF 

params, params_covariance = curve_fit(func, xlist, ylist, p0=None, maxfev=10000) 

xdummy = np.linspace(-2, 2, 1000)
ydummy = []
k = params

for item in xdummy:
    ydummy.append(0.5 * k * item**2)

legendList2 = ["Fit", "Data"]

plt.plot(xdummy,ydummy, linewidth = 4)
plt.plot(xlist, ylist, linewidth = 4)
plt.xlabel("Total Displacement ($\AA$)", fontsize=12)
plt.xticks(fontsize = 12)
plt.ylabel(r"$\psi$ / $\psi_{max}$", fontsize=12)
plt.yticks(fontsize = 12)
#plt.ylim(-20E-27, 1.5E-25)
#plt.text(-10, -0.1E-25, "Strain Rate: " + str(strainRate) + " $\AA$/fs", fontsize=12)
plt.legend(legendList2, fontsize = 12, loc = 'lower right')
plt.show()