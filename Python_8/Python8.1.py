#!/usr/bin/env python3
import re
#This is a fasta parser
seq = ''
genes = {}

with open ("Python8.1input.fa","r") as FastaFile:
 for line in FastaFile:
  if re.search(r"^>\S+", str(line)):
   match = (re.match(r"(^>\S+)(.+)", str(line)))
   geneID = (match.group(1))
   geneID = geneID[1:]
   genes[geneID] = seq
  else:
   seqline = line.rstrip()
   seq = seq + seqline
   genes[geneID]= {'sequence': seq}


for geneID in genes:
	sequence  = genes[geneID]['sequence'] # returns the sequence of the gene
	Acount = sequence.count('A')
	Tcount = sequence.count('T')
	Gcount = sequence.count('G')
	Ccount = sequence.count('C')
	genes[geneID]['A'] = Acount
	genes[geneID]['T'] = Tcount
	genes[geneID]['C'] = Ccount
	genes[geneID]['G'] = Gcount
 # genes[geneID]= {'A': Acount} #for some reason this generates an error
 # genes[geneID]= {'T': Tcount}
 # genes[geneID]= {'G': Gcount}
 # genes[geneID]= {'C': Ccount}
	#print(geneID)

print(genes['c256_g1_i1']['A'])

#print(genes)
#print(genes['gi|170746|gb|M12277.1|WHTH4091']['A'])
