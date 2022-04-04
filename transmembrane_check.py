#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# hydrophilicity plot = degree of hydrophobicity of amino acids
# each letter is a protein 
hydro_score = {
'I': 4.5,
'V': 4.2,
'L': 3.8,
'F': 2.8,
'C': 2.5,
'M': 1.9,
'A': 1.8,
'G': -0.4,
'T': -0.7,
'S': -0.8,
'W': -0.9,
'Y': -1.3,
'P': -1.6,
'H': -3.2,
'E': -3.5,
'Q': -3.5,
'D': -3.5,
'N': -3.5,
'K': -3.9,
'R': -4.5
}


def find_name(line):
	return line[1:line.index('|')-1]

# determine if hydrophobic reigon 
def hydrophobic_region(seq):
	hydrophobic = False
	region = seq[30:]
	KD = 0
	
	# checks for proline, and the value for KD
	for i in range(len(region)-11):
		peptide = region[i:i+11]
		
		if 'P' in peptide:
			continue
		for aa in peptide: 
			KD += hydro_score[aa]
		if KD/11 > 2.0: 
			hydrophobic = True
			break
	return hydrophobic
	
# determine if it is a signal protein based on KD value 
def signal_peptide(seq):
	pep = seq[0:30]
	signal = False
	for i in range(30-8):
		KD = 0
		for j in range(8): KD += hydro_score[pep[i+j]]
		if KD/8 > 2.5: 
			signal = True
			break
	return signal
	
#main function 	
def main():
    # get file from user, first argument should be the file
    file = open(sys.argv[1])

	#generate list of transmembrane protein in the file 
    trans_mem = []

	# read lines in file 
    for line in file.readlines():
        if ('>' in line):
            seq = ''
            forward = ('FORWARD' in line)
            name = find_name(line)
        else:
            if '*' in line:
                seq += line
                seq = seq.replace('*','')
                seq = seq.replace('\n','')
                seq = seq.replace(' ','')
                #if forward is False: seq = seq[::-1]
                #print(name)
                #print(seq)
                
				# if it is a signal peptide and is hydrophobic, then it is a transmembrane protein
				#add protein to list 
                if signal_peptide(seq) and hydrophobic_region(seq):
                    trans_mem.append(name)
                else: seq += line

	 # print all proteins in trans membrane protien list                       
    for protein in trans_mem:
            print(protein)
			
	
		
		
	
