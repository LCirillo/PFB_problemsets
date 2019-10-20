#!/usr/bin/env python3

import re


def Lines_in_60char(InputFile):
		output = ''
		N_60mersList= []
		InputFile = str(InputFile)
		InputFile = InputFile.replace('\n','')
		match = re.match(r"[ATCGNatgcn]+", InputFile)
		line = match.group(0)			
		linelenght = len(str(line))
		N_60mers = int(linelenght/60)
		if linelenght%60 != 0:
				N_60mers += 1
		for i in range(N_60mers + 1):
				i = i*60
				string = line[i:i+60]
				output = output + string + '\n'
		return(output)		

InputFile = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''
#with open('Python10.2input.txt','r') as InputFile:
#	print(Lines_in_60char(InputFile))
print(Lines_in_60char(InputFile))
#it doesnt work if the file comes from a file, but that's life

