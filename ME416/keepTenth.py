infile = open("/mnt/c/Users/heath/Documents/NU_Courses/ME416/HW2/tinyradio/COM.txt", 'r')
outfile = open("/mnt/c/Users/heath/Documents/NU_Courses/ME416/HW2/tinyradio/COM_short.txt", 'w')

line1 = infile.readline()
line2 = infile.readline()

timestepList = []
COMList = []

for line in infile:
    line = line.strip()
    line = line.split()
    timestepList.append(line[0])
    COMList.append(line[1])

timestepListLength = len(timestepList)
COMListLength = len(COMList)

newTimestepList = []
newCOMList = []

for count in range(0, timestepListLength):
    if count % 10 == 2:
        newTimestepList.append(timestepList[count])
        newCOMList.append(COMList[count])

for count in range(0, len(newTimestepList)):
    outfile.write(newTimestepList[count] + '\t' + newCOMList[count] + '\n')

infile.close()
outfile.close()