#!usr/bin/env python3 
#Mitchell Roth	
#https://github.com/mor16fsu/bch5884

import sys

#1 Read in the PDB file

f=open("2FA9noend.pdb", 'r')
lines=f.readlines()
f.close()

#2 Make a list of lists 

line=[]
for i in range(len(lines)):
	line.append(lines[i].split())


#Output Centered PDB file for either center of mass or geometric center 

f=open("new2FA9noend.pdb","w")
for line in lines:
    f.write("%-4s%7d %-5s%-4s%-3s%-6d%8.3f%8.3f%8.3f%6.2f%6.2f%12s \n" %(line[0:4],int(line[5:11]),line[12:16],line[17:20],line[21:22],int(line[23:26]),float(line[27:38]),float(line[39:46]),float(line[47:54]),float(line[55:60]),float(line[61:66]),line[67:78]))
f.close()
print("Done!")

