#!/usr/bin/env python3

DNAs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for sequence in DNAs:
	print(sequence)
for sequence in DNAs:
	print(len(sequence),DNAs.index(sequence),sequence,sep='\t')


