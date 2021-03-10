"""
This program takes in a lammps data file for GO and 
returns the box boundaries needed for the simulation.
"""

#path = "/mnt/c/Users/heath/Ubuntu/GO/stack2_10a_10e_250y.data"
#path = "/mnt/c/Users/heath/Ubuntu/GO/ForAndrea/stack2_10a_10e_1500Ax_200Ay.data"
path = "/mnt/c/Users/heath/stack10_0a_0e_30ny_40nx_infX.data"
buffer = 3.5
xbuffer = 2.4768

infile = open(path, 'r')

xcoords = []
ycoords = []
zcoords = []

for line in infile:
    line = line.strip()
    if "Atoms" in line:
        infile.readline()
        break

for line in infile:
    line = line.strip()
    if line == '':
        break
    else:
        line = line.split(' ')
        numatoms = line[0]
        zcoords.append(float(line[6]))
        if line[1] == '1':
            xcoords.append(float(line[4]))
            ycoords.append(float(line[5]))
        
        
infile.close()

xmin = round((min(xcoords) - 0), 4)
xmax = round((max(xcoords) + xbuffer), 4)
rangex = xmax - xmin
ymin = round((min(ycoords) - 0), 4)
ymax = round((max(ycoords) + buffer), 4)
rangey = ymax - ymin
zmin = round((min(zcoords) - 0), 4)
zmax = round((max(zcoords) + buffer), 4)
rangez = zmax - zmin

print("atoms:", numatoms)
print("VMD index:", int(numatoms)/2-1)
print("x length", max(xcoords)-min(xcoords))
print("half x length", (max(xcoords)-min(xcoords))/2)
print('')
print(xmin, xmax, 'xlo xhi')
print(ymin, ymax, 'ylo yhi')
print(zmin, zmax, 'zlo zhi')