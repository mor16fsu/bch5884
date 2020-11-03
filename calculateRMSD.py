#!/usr/bin/env python3 
#Mitchell Roth 
#https://github.com/mor16fsu/bch5884

#Create a function to read the PDB file (use script from previous PDBproject) 

def readthePDB(file):
  f=open(file)
  lines=f.readlines()
  f.close

#Return a list of atoms (use script from previous PDBproject)

  line=[]
  for i in range(len(lines)):
    line.append(lines[i].split())
  return line 

#Create a function which takes two lists of atoms and calculates the RMSD between the two 

def RMSD_calculation(): 
  list1=readthePDB("2FA9noend.pdb")
  list2=readthePDB("2FA9noend2mov.pdb")
  fullist=len(list1)

#Do a loop over the two PDB files for summation   
  
  for i in range(fullist):
    vix_wix=(float(list2[i][6])-float(list1[i][6]))**2
    viy_wiy=(float(list2[i][7])-float(list1[i][7]))**2
    viz_wiz=(float(list2[i][8])-float(list1[i][8]))**2
    sum=((vix_wix)+(viy_wiy)+(viz_wiz))
    finalrmsdvalue=(1/sum)**0.5
  return finalrmsdvalue

print("The value of the root mean squared deviation between the two PDB structures is:")
print(RMSD_calculation())


