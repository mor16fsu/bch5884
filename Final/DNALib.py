#!/usr/bin/env python3 
#https://github.com/mor16fsu/bch5884
#Mitchell Roth

#List of DNA Nucleotides
#Dictionary for reverse complement
#Dictionary for amino acids 
#Dictionary for human codon optimization

from matplotlib import pyplot as plt 

Nucleotides=["A","C","G","T"]
reversedict={'A':'T','C':'G','G':'C','T':'A',}
aminodict={
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','CAT':'H','CAC':'H',
    'CAA':'Q','CAG':'Q','AAT':'N','AAC':'N',
    'AAA':'K','AAG':'K','GAT':'D','GAC':'D',
    'GAA':'E','GAG':'E','TGT':'C','TGC':'C',
    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGT':'G','GGC':'G','GGA':'G','GGG':'G',
    'TGG':'W','TAA':'*','TAG':'*','TGA':'*',}

humandict={
    'TTT':'TTC','TTC':'TTC','TTA':'CTG','TTG':'CTG',
    'CTT':'CTG','CTC':'CTG','CTA':'CTG','CTG':'CTG',
    'TAT':'TAC','TAC':'TAC','CAT':'CAC','CAC':'CAC',
    'CAA':'CAG','CAG':'CAG','ATT':'ATC','ATC':'ATC',
    'ATA':'ATC','ATG':'ATG','AAT':'AAC','AAC':'AAC',
    'AAA':'AAG','AAG':'AAG','GTT':'GTG','GTC':'GTG',
    'GTA':'GTG','GTG':'GTG','GAT':'GAC','GAC':'GAC',
    'GAA':'GAG','GAG':'GAG','TCT':'AGC','TCC':'AGC',
    'TCA':'AGC','TCG':'AGC','AGT':'AGC','AGC':'AGC',
    'TGT':'TGC','TGC':'TGC','TGG':'TGG','CCT':'CCC',
    'CCC':'CCC','CCA':'CCC','CCG':'CCC','CGT':'CGG',
    'CGC':'CGG','CGA':'CGG','AGA':'CGG','AGG':'CGG',
    'ACT':'ACC','ACC':'ACC','ACA':'ACC','ACG':'ACC',
    'GCT':'GCC','GCC':'GCC','GCA':'GCC','GCG':'GCC',
    'GGT':'GGC','GGC':'GGC','GGA':'GGC','GGG':'GGC',
    'TAA':'TGA','TAG':'TGA','TGA':'TGA','CGG':'CGG',}


#Check for the sequence to make sure it is correct 

def checkseq(seq):
    seq=seq.upper()
    for nuc in seq:
        if nuc not in Nucleotides: 
            return False
         

#Count each of the nucleotides in the sequence provided 

def countnuc(seq):
    countnucDict={"A":0, "C":0, "G":0, "T":0}
    for i in seq: 
        countnucDict[i]+=1
    return countnucDict        

#Transcribe the sequence

def transcribe(seq):
    return seq.replace("T","U")


#Reverse Complement

def reverse_complement(seq):
    reverse=''
    for i in range(len(seq)):
        complement=seq[i]
        reverse+=reversedict[complement]
    return reverse[::-1]


#Translation

def translate(seq,code):
    protein=''
    for i in range(0,len(seq),3):
        codon=seq[i:i+3]
        protein+=aminodict[codon]
    return protein    

#Calculate GC Content 

def GC(seq):
    return ((seq.count('G')+seq.count('C'))/len(seq)*100)


#Human codon optimization

def human_optimize(seq,code):
    optimization=''
    for i in range(0,len(seq),3):
        codonseq=seq[i:i+3]
        optimization+=humandict[codonseq]
    return optimization


#Calculate Tm
 
def tm(seq):
    return ((seq.count('A')+seq.count('T'))*2+(seq.count('G')+seq.count('C'))*4)-1.5
    

#Plot Nucleotide Frequency in bar graph 

def plot(seq):
    countnucDict={"A":0, "C":0, "G":0, "T":0}
    for i in seq:
        countnucDict[i]+=1    
    plt.bar(*zip(*countnucDict.items()))
    plt.title('Nucleotide Frequency')
    plt.xlabel('Nucleotides')
    plt.ylabel('Frequency')
    plt.show()
    return plot

###HTML functions###
 
