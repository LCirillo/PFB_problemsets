#!/usr/bin/env python3
import re
#This is a fasta parser
seq = ''
genes = {}

with open ("Python7.3input.txt","r") as FastaFile:#, open("Python8.1outputTEST.txt","w"):
 for line in FastaFile:
  if re.search(r"^>\S+", str(line)):
   match = (re.match(r"(^>\S+)(.+)", str(line)))
   geneID = (match.group(1))
   geneID = geneID[1:]
   genes[geneID] =  seq
  else:
   seqline = line.rstrip()
   seq = seq + seqline
   genes[geneID] = {'sequence': seq}

GeneCodons = {}
for geneID in genes:
	seq = genes[geneID]['sequence']
	Codons1 = (re.findall(r"\S\S\S", str(seq)))	#this may be wrong
	Codons2 = (re.findall(r"\S\S\S", str(seq[1:])))	#this may be wrong
	Codons3 = (re.findall(r"\S\S\S", str(seq[2:])))	#this may be wrong
	Frame1 = ""
	Frame2 = ""
	Frame3 = ""
	#print(geneID)
	for codon in Codons1:
			Frame1  = Frame1 + str(codon) + " "
	for codon in Codons2:
			Frame2 = Frame2 + str(codon) + " "
	for codon in Codons3:
			Frame3 = Frame3 + str(codon) + " "

#it seems that a dictionary of dictionaries has to be inizialized as follows
	GeneCodons[geneID]= {'Frame1': Frame1}
	GeneCodons[geneID]['Frame2'] = Frame2
	GeneCodons[geneID]['Frame3'] = Frame3

#this attach the frames to the original dict (genes), this dict was already initialized in line 17
	genes[geneID]['Frame1'] = Frame1
	genes[geneID]['Frame2'] = Frame2
	genes[geneID]['Frame3'] = Frame3

print(genes)
#print(GeneCodons)
#print(genes['gi|603555|emb|X83548.1|'])					
#print(GeneCodons['c12_g1_i1'])	

