"""
For analysis of the group/group output from stepwise PGN plate simulations. 
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats.distributions import t

######### VARIABLES ###############

# Number of timesteps per round of SMD
timesteps_per_SMDround = 1200000/40

timesteps_between_EQrounds = 30000
timesteps_per_EQoutput = 1000

# Strain rate being used
strainRate = 0.00005 # A/fs

# Number of PMF files in simulation
numFiles = 40

equilibriumVolume = 3.8401E-25 # m^3

# File paths
path_nocycle = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/nocycle_noeq_run2/PMF.txt"
path_cycle_noeq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_noeq/Poly2Poly1/"
path_cycle_5keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_5keq_run3/smdGG/Poly2Poly1/"
path_cycle_50keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_50keq_run2/Poly2Poly1/"
path_cycle_50keq_100Loop = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_50keq_100Loop/Poly2Poly1/"
path_cycle_75keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_75keq/smdGG/Poly2Poly1/"
path_cycle_200keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_200keq/smdGG/Poly2Poly1/"
path_cycle_500keq = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_500keq/smdGG/Poly2Poly1/"

path_cycle_5keq_equildata = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_5keq_run3/equilGG/Poly2Poly1/"
path_cycle_50keq_equildata = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_50keq_run2/equilGG/Poly2Poly1/"
path_cycle_50keq_equildata_100Loop = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_50keq_100Loop/equilGG/Poly2Poly1/"
path_cycle_75keq_equildata = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_75keq/equilGG/Poly2Poly1/"
path_cycle_200keq_equildata = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_200keq/equilGG/Poly2Poly1/"
path_cycle_500keq_equildata = "/mnt/c/Users/heath/Ubuntu/PGN_Revisions/cycle_500keq/equilGG/Poly2Poly1/"


########## FUNCTIONS ###############

#return totalStrainList, pmfList, convertedPMFList 
#for simulation with PMF output from SMD
def extractDataNoCycle(FCTpath, FCTstrainRate, FCTvolume):

    infile = open(FCTpath, 'r')
    infile.readline()
    infile.readline()

    timestepList = []
    pmfList = []

    for line in infile:
        line = line.strip()
        line = line.split(" ")
        
        timestep = int(line[0])
        pmf = float(line[1])
        timestepList.append(timestep)
        pmfList.append(pmf)

    infile.close()

    # Convert PMF to kcal/m^3
    
    mysteryParam = 1000
    avogadro = 6.022 * 10**23 * mysteryParam
    convertedPMFList = []

    for item in pmfList:
        convertedPMF = item / avogadro
        convertedPMF = convertedPMF / FCTvolume
        convertedPMFList.append(convertedPMF)

    # Convert timesteps to total strain (displacement)

    numTimesteps = len(timestepList)
    totalStrainList = []

    for item in timestepList:
        fs_per_timestep = 4
        adjustedTimestep = item - timestepList[0]

        totalStrain = float(adjustedTimestep) * FCTstrainRate * fs_per_timestep
        totalStrain = round(totalStrain, 3)
        totalStrainList.append(totalStrain)

    return totalStrainList, pmfList, convertedPMFList

#return totalStrainList, yforceList, pmfList, convertedPMFList 
# for stepwise simulation with yforces and no equilbration
def extractDataCycleNoEq(FCTpath, FCTnumFiles, FCTstrainRate, FCTtimesteps_per_SMDround , FCTvolume):

    currentSMDtimestep = 0
    timestepList = []
    yforceList = []

    for count1 in range(0, FCTnumFiles):

        fileName =  "GG_Poly2Poly1_Loop" + str(count1+1) + ".txt"
        filePath = FCTpath + fileName

        infile = open(filePath, 'r')
        infile.readline()
        infile.readline()
        line = infile.readline()
        line = line.strip()
        line = line.split(" ")

        yforce = float(line[2])
        yforceList.append(-yforce)

        timestepList.append(currentSMDtimestep)
        currentSMDtimestep += FCTtimesteps_per_SMDround    

    infile.close()

    fs_per_timestep = 4    
    totalStrainList = []

    for item in timestepList:
        totalStrain = item * FCTstrainRate * fs_per_timestep
        totalStrain = round(totalStrain, 3)
        totalStrainList.append(totalStrain)

    # Integration to get PMF from forces
    pmfList = [0] # Add zero at beginning so list has right number of elements

    for count2 in range(1, len(yforceList)):
        width = abs(totalStrainList[count2] - totalStrainList[count2-1])
        height = 0.5 * (yforceList[count2] + yforceList[count2-1])
        additionalPMF  = width * height
        runningPMF = pmfList[count2-1] + additionalPMF
        runningPMF = round(runningPMF, 3)
        pmfList.append(runningPMF)

    # Convert PMF to kcal/m^3
    
    mysteryParam = 1000
    avogadro = 6.022 * 10**23 * mysteryParam
    convertedPMFList = []

    for item in pmfList:
        convertedPMF = item / avogadro
        convertedPMF = convertedPMF / FCTvolume
        convertedPMFList.append(convertedPMF)
    print("Max PMF:", convertedPMF)

    #print("\n Max PMF for " + FCTpath + ":\n" + str(convertedPMFList[len(convertedPMFList)-1]))

    return totalStrainList, yforceList, pmfList, convertedPMFList

#return totalStrainList, yforceList, pmfList, convertedPMFList
# for stepwise simulation with yforces and equilbration
def extractDataCycle(FCTpath, FCTnumFiles, FCTstrainRate, FCTtimesteps_per_SMDround , FCTvolume):

    currentSMDtimestep = 0
    timestepList = []
    yforceList = []

    for count1 in range(0, FCTnumFiles):

        fileName =  "GG_Poly2Poly1_Loop" + str(count1+1) + ".txt"
        filePath = FCTpath + fileName

        infile = open(filePath, 'r')
        infile.readline()
        infile.readline()

        lineCount = 0
        average_yforce = 0

        for line in infile:
            lineCount += 1
            line = line.strip()
            line = line.split(" ")
            yforce = float(line[2])
            average_yforce += -yforce

        infile.close() 

        average_yforce = average_yforce / (lineCount-1)
        yforceList.append(average_yforce)

        timestepList.append(currentSMDtimestep)
        currentSMDtimestep += FCTtimesteps_per_SMDround
        
    fs_per_timestep = 4    
    totalStrainList = []

    for item in timestepList:
        totalStrain = item * FCTstrainRate * fs_per_timestep
        totalStrain = round(totalStrain, 3)
        totalStrainList.append(totalStrain)

    # Integration to get PMF from forces
    pmfList = [0] # Add zero at beginning so list has right number of elements

    for count2 in range(1, len(yforceList)):
        width = abs(totalStrainList[count2] - totalStrainList[count2-1])
        height = 0.5 * (yforceList[count2] + yforceList[count2-1])
        additionalPMF  = width * height
        runningPMF = pmfList[count2-1] + additionalPMF
        runningPMF = round(runningPMF, 3)
        pmfList.append(runningPMF)  

    # Convert PMF to kcal/m^3
    
    mysteryParam = 1000
    avogadro = 6.022 * 10**23 * mysteryParam
    convertedPMFList = []

    for item in pmfList:
        convertedPMF = item / avogadro
        convertedPMF = convertedPMF / FCTvolume
        convertedPMFList.append(convertedPMF)

    #print("\nMax PMF for " + FCTpath + ":\n" + str(convertedPMFList[len(convertedPMFList)-1]))

    return totalStrainList, yforceList, pmfList, convertedPMFList

#return timestepList, yforceList
#for examination of equilibration in stepwise simulation
def extractEquilDataCycle(FCTpath, FCTnumFiles, FCTstrainRate, FCTtimesteps_per_EQoutput, FCTtimesteps_between_EQrounds):
    
    currentEQtimestep = 10000
    timestepList = []
    yforceList = []

    for count1 in range(0, FCTnumFiles):
        fileName =  "GG_Poly2Poly1_Loop" + str(count1+1) + ".txt"
        filePath = FCTpath + fileName

        infile = open(filePath, 'r')
        infile.readline()
        infile.readline()

        for line in infile:
            line = line.strip()
            line = line.split(" ")
            yforce = float(line[2])
            yforceList.append(-yforce)
            timestepList.append(currentEQtimestep)
            currentEQtimestep += FCTtimesteps_per_EQoutput 
            
        currentEQtimestep += FCTtimesteps_between_EQrounds - FCTtimesteps_per_EQoutput 
        infile.close()   

    return timestepList, yforceList
    
###### Fomat data using functions ######

totalStrain_nocycle = extractDataNoCycle(path_nocycle, strainRate, equilibriumVolume)[0]
PMF_nocycle = extractDataNoCycle(path_nocycle, strainRate, equilibriumVolume)[2]

totalStrain_cycle_noeq = extractDataCycleNoEq(path_cycle_noeq, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[0]
yforceList_cycle_noeq = extractDataCycleNoEq(path_cycle_noeq, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[1]
PMF_cycle_noeq = extractDataCycleNoEq(path_cycle_noeq, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[3]

totalStrain_cycle_5keq = extractDataCycle(path_cycle_5keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[0]
yforceList_cycle_5keq = extractDataCycle(path_cycle_5keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[1]
PMF_cycle_5keq = extractDataCycle(path_cycle_5keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[3]

totalStrain_cycle_50keq = extractDataCycle(path_cycle_50keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[0]
yforceList_cycle_50keq = extractDataCycle(path_cycle_50keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[1]
PMF_cycle_50keq = extractDataCycle(path_cycle_50keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[3]

totalStrain_cycle_50keq_100Loop = extractDataCycle(path_cycle_50keq_equildata_100Loop, 100, strainRate, 12000, equilibriumVolume)[0]
yforceList_cycle_50keq_100Loop = extractDataCycle(path_cycle_50keq_equildata_100Loop, 100, strainRate, 12000, equilibriumVolume)[1]
PMF_cycle_50keq_100Loop = extractDataCycle(path_cycle_50keq_equildata_100Loop, 100, strainRate, 12000, equilibriumVolume)[3]

totalStrain_cycle_75keq = extractDataCycle(path_cycle_75keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[0]
yforceList_cycle_75keq = extractDataCycle(path_cycle_75keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[1]
PMF_cycle_75keq = extractDataCycle(path_cycle_75keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[3]

totalStrain_cycle_200keq = extractDataCycle(path_cycle_200keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[0]
yforceList_cycle_200keq = extractDataCycle(path_cycle_200keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[1]
PMF_cycle_200keq = extractDataCycle(path_cycle_200keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[3]

totalStrain_cycle_500keq = extractDataCycle(path_cycle_500keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[0]
yforceList_cycle_500keq = extractDataCycle(path_cycle_500keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[1]
PMF_cycle_500keq = extractDataCycle(path_cycle_500keq_equildata, numFiles, strainRate, timesteps_per_SMDround, equilibriumVolume)[3]

#######

eq_timesteps_cycle_5keq = extractEquilDataCycle(path_cycle_5keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[0]
eq_yforce_cycle_5keq = extractEquilDataCycle(path_cycle_5keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[1]

eq_timesteps_cycle_50keq = extractEquilDataCycle(path_cycle_50keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[0]
eq_yforce_cycle_50keq = extractEquilDataCycle(path_cycle_50keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[1]

eq_timesteps_cycle_75keq = extractEquilDataCycle(path_cycle_75keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[0]
eq_yforce_cycle_75keq = extractEquilDataCycle(path_cycle_75keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[1]

eq_timesteps_cycle_500keq = extractEquilDataCycle(path_cycle_500keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[0]
eq_yforce_cycle_500keq = extractEquilDataCycle(path_cycle_500keq_equildata, numFiles, strainRate, timesteps_per_EQoutput, timesteps_between_EQrounds)[1]

############ PLOTS #######################


# SMD data
legendList1 = [
    "Predicted zero-shear PMF",
    "SMD PMF Output (no cycle)",
    "Calc. PMF (cycle, no eq)",
    "Calc. PMF (cycle, 5k ts eq)",
    "Calc. PMF (cycle, 50k ts eq)",
    "Calc. PMF (cycle, 75k ts eq)",
    "Calc. PMF (cycle, 200k ts eq)",
    "Calc. PMF (cycle, 500k ts eq)"
    ]

plt.scatter(totalStrain_nocycle, PMF_nocycle, s = 8)
plt.scatter(totalStrain_cycle_noeq, PMF_cycle_noeq, s = 8)
plt.scatter(totalStrain_cycle_5keq, PMF_cycle_5keq, s = 8)
plt.scatter(totalStrain_cycle_50keq, PMF_cycle_50keq, s = 8)
plt.scatter(totalStrain_cycle_75keq, PMF_cycle_75keq, s = 8)
plt.scatter(totalStrain_cycle_200keq, PMF_cycle_200keq, s = 8)
plt.scatter(totalStrain_cycle_500keq, PMF_cycle_500keq, s = 8)
plt.plot((0, 250), (48.83, 48.83), c = 'red')

#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.title("PMF Calculations for N=50, \u03C3=0.05 chains/$nm^2$", fontsize = 14)
plt.xlabel("Total Displacement ($\AA$)", fontsize = 14)
plt.xticks(fontsize = 14)
plt.ylabel(r"$\psi$ (kcal/$m^3$)", fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(legendList1, scatterpoints=4, fontsize = 10)
plt.show()



# SMD data - compare # loops for 50k
legendList1 = [
    "Predicted zero-shear PMF",
    "Calc. PMF (40 loops, 50k ts eq)",
    "Calc. PMF (100 loops, 50k ts eq)"
    ]

plt.scatter(totalStrain_cycle_50keq, PMF_cycle_50keq, s = 8)
plt.scatter(totalStrain_cycle_50keq_100Loop, PMF_cycle_50keq_100Loop, s = 8)
plt.plot((0, 250), (48.83, 48.83), c = 'red')

plt.title("PMF Calculations for N=50, \u03C3=0.05 chains/$nm^2$", fontsize = 14)
plt.xlabel("Total Displacement ($\AA$)", fontsize = 14)
plt.xticks(fontsize = 14)
plt.ylabel(r"$\psi$ (kcal/$m^3$)", fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(legendList1, scatterpoints=4, fontsize = 10)
plt.show()



###Plot peak values

mysteryParam = 1000
avogadro = 6.022 * 10**23 * mysteryParam

# Non-stepwise data
yL50 = np.array([
    5.421E+28 / avogadro,
    6.062E+28 / avogadro,
    7.057E+28 / avogadro,
    7.482E+28 / avogadro,
    8.980E+28 / avogadro,
    1.048E+29 / avogadro
    ])

xL50 = [5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3]

xdummy1 = np.linspace(1E-6, 1E-4, 500)

# Stepwise data
effectiveSRvalues = [5e-5, 4.29E-5, 1.88E-5, 1.43E-5, 6.52E-6, 2.83E-6]
peakPMFvalues = [109.77, 118.26, 99.88, 91.36, 81.26, 80.17]

x = effectiveSRvalues
y = peakPMFvalues

xdummy2 = np.linspace(1E-6, 1.1E-2, 500)

aList = []
bList = []

def func(x, a, b):
    return a * (1 + (x/(1e-5))**b)

# Stepwise data
params, params_covariance = curve_fit(func, x, y, p0=[75, 0.06], maxfev=10000)
aList.append(params[0])
bList.append(params[1])

# CI calculation from http://kitchingroup.cheme.cmu.edu/blog/2013/02/12/Nonlinear-curve-fitting-with-parameter-confidence-intervals/
alpha = 0.05 # 95% confidence interval
n = len(y) # number of data points
p = len(params) # number of parameters
dof = max(0, n-p) # number of degrees of freedom
tval = t.ppf(1.0-alpha/2., dof)
paramNames = ['a','b']
for i, p, var in zip(range(n), params, np.diag(params_covariance)):
    sigma = var**0.5
    print('CI for stepwise fit', paramNames[i], ': {1} [{2}  {3}] {4}'.format(i, p, p - sigma*tval, p + sigma*tval, sigma*tval))

plt.scatter(x, y, s=70)
plt.plot(xdummy1, func(xdummy1, params[0], params[1]), linewidth = 2)

# Original data
params, params_covariance = curve_fit(func, xL50, yL50, p0=[75, 0.06], maxfev=10000)
aList.append(params[0])
bList.append(params[1])

# CI calculation from http://kitchingroup.cheme.cmu.edu/blog/2013/02/12/Nonlinear-curve-fitting-with-parameter-confidence-intervals/
alpha = 0.05 # 95% confidence interval
n = len(yL50) # number of data points
p = len(params) # number of parameters
dof = max(0, n-p) # number of degrees of freedom
tval = t.ppf(1.0-alpha/2., dof)
paramNames = ['a','b']
for i, p, var in zip(range(n), params, np.diag(params_covariance)):
    sigma = var**0.5
    print('CI for original fit', paramNames[i], ': {1} [{2}  {3}] {4}'.format(i, p, p - sigma*tval, p + sigma*tval, sigma*tval))


plt.scatter(xL50, yL50, s=70)
plt.plot(xdummy2, func(xdummy2, params[0], params[1]), linewidth = 2)

legendList = ("Stepwise", "Original")
plt.legend(legendList)
plt.title("PMF Calculations for N=50, \u03C3=0.5 chains/$nm^2$", fontsize = 14)
plt.xscale('log')
#plt.xlim(10E3, 10E5)
plt.xlabel("Effective PullVel (A/fs)", fontsize = 14)
plt.xticks(fontsize = 14)
plt.ylabel("Peak $\psi$ (kcal/$m^3$)", fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()


"""
#Plot equilibrium force values

legendList2 = [
    "Equilibration PMF (500k ts eq)"
    ]

plt.scatter(eq_timesteps_cycle_500keq, eq_yforce_cycle_500keq, s = 8)

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.title("y Force Calculations for N=50, \u03C3=0.5 chains/$nm^2$", fontsize = 14)
plt.xlabel("Timesteps", fontsize = 14)
plt.xticks(fontsize = 14)
plt.ylabel("y Force", fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(legendList2, scatterpoints=4, fontsize = 10)
plt.show()
"""