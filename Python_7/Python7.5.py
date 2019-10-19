#!/usr/bin/env python3
import re
#This is a fasta parser
seq = ''
genes = {}
with open ("Python7.3input.txt","r") as FastaFile:
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

print(genes)    
   


