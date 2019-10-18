#!/usr/bin/env python3

#This is a fasta parser
seq = ''
genes = {}
with open ("Python6.5input.fasta","r") as FastaFile:
 for line in FastaFile:
  FirstChar=line[0]  #startswith would work as well
  if FirstChar == '>':
   seq = ''
   geneID = line[1:]
   geneID = geneID.rstrip()
   genes[geneID]=seq  
  else:
   seqline = line.rstrip()
   seq = seq + seqline
   genes[geneID]= seq

print(genes)    
   


