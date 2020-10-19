#!usr/bin/env python3 
#Mitchell Roth	
#

import sys

#1 Read in the PDB file

f=open("2FA9noend.pdb", 'r')
lines=f.readlines()
f.close()

#2 Make a list of lists 

line=[]
for i in range(len(lines)):
	line.append(lines[i].split())

#print(lines)

#3 Center the PDB based on the users choice of geometric center or the center of mass and output the centered PDB file.


#4 Define the mass of each element (amu) 

def amu(element): 
	if element=="C": 
		return 12.01
	if element=="N": 
		return 14.01
	if element=="O":
		return 16.00
	if element=="P": 
		return 31.00
	if element=="S": 
		return 32.07



#5 Calculate the center of mass
mi=0
xorigin=0
yorigin=0
zorigin=0
for i in range(len(lines)):
	x=float(line[i][6])
	y=float(line[i][7])
	z=float(line[i][8])
	mi=mi+amu(line[i][11])
	xorigin=xorigin+amu(line[i][11])*x
	yorigin=yorigin+amu(line[i][11])*y
	zorigin=zorigin+amu(line[i][11])*z
	centerx=xorigin/mi
	centery=yorigin/mi	
	centerz=zorigin/mi

print('The center of mass is ({:0.3f},{:0.3f},{:0.3f}).'.format(centerx,centery,centerz))


#6 Calculate the geometric center
xgcenter=0
ygcenter=0
zgcenter=0
atoms=1337
for i in range(len(lines)):
	x=float(line[i][6])
	y=float(line[i][7])
	z=float(line[i][8])
	xgcenter=xgcenter+x
	ygcenter=ygcenter+y
	zgcenter=zgcenter+z
	xgc=xgcenter/atoms
	ygc=ygcenter/atoms
	zgc=zgcenter/atoms

print('The geometric center of mass is ({:0.3f},{:0.3f},{:0.3f}).'.format(xgc,ygc,zgc))


ch=input("If you want to center the PDB file by mass input uppercase M, if you want to center the PDB file by geometric center input uppercase G: ")

#New PDB coordinates for center of Mass
if ch=="M":
    for i in range(len(lines)):
        line[i][6]=float(line[i][6])-centerx
        line[i][7]=float(line[i][7])-centery
        line[i][8]=float(line[i][8])-centerz

#New PDB coordinates for geometric center
else:
    for i in range(len(lines)):
        line[i][6]=float(line[i][6])-xgcenter
        line[i][7]=float(line[i][7])-ygcenter
        line[i][8]=float(line[i][8])-xgcenter


#Output Centered PDB file for either center of mass or geometric center 

f=open("new2FA9noend.pdb","w")
for line in lines:
    f.write("%-4s%7d %-5s%-4s%-3s%-6d%8.3f%8.3f%8.3f%6.2f%6.2f%12s \n" %(line[0:4],int(line[5:11]),line[12:16],line[17:20],line[21:22],int(line[23:26]),float(line[27:38]),float(line[39:46]),float(line[47:54]),float(line[55:60]),float(line[61:66]),line[67:78]))
f.close()
print("Done!")
