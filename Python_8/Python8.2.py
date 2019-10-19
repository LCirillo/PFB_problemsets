#!/usr/bin/env python3
import re
#This is a fasta parser
seq = ''
genes = {}

with open ("Python8.1input.fa","r") as FastaFile:#, open("Python8.1outputTEST.txt","w"):
 for line in FastaFile:
  if re.search(r"^>\S+", str(line)):
   match = (re.match(r"(^>\S+)(.+)", str(line)))
   geneID = (match.group(1))
   geneID = geneID[1:]
   genes[geneID] = seq
  else:
   seqline = line.rstrip()
   seq = seq + seqline
   genes[geneID]= seq

GeneCodons = {}
for geneID in genes:
	codons = (re.findall(r"\S\S\S", str(seq)))	#this may be wrong
	codonstring=""
	print(geneID)
	for codon in codons:
			codonstring  = codonstring + str(codon) + " "
	GeneCodons[geneID] = codonstring

#print(GeneCodons)
#print(GeneCodons['gi|603555|emb|X83548.1|'])					
print(GeneCodons['c12_g1_i1'])	

