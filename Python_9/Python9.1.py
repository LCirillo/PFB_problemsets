#!/usr/bin/env python3
import re
import sys
#This is a fasta parser
seq = ''
genes = {}
InFile = ' '
try: # will open the file OR raise an error
 InFile = sys.argv[1]
 if not InFile.endswith('.fa'):
  raise ValueError ("This is not a FASTA")
 with open (InFile,"r") as FastaFile:
  for line in FastaFile:
   if re.search(r"^>\S+", str(line)):
    match = (re.match(r"(^>\S+)(.+)", str(line)))
    geneID = (match.group(0))
    geneID = geneID[1:]
    genes[geneID] = seq
   else:
    seqline = line.rstrip()
    seq = seq + seqline
    genes[geneID]= seq
#search for any character but A T C G N a t g c n, if a different character is present raise an error
    if re.search(r"[^ATCGNatgcn]", str(seq)):
     raise ValueError ("The sequence contains special characters")

 GeneCodons = {}
 for geneID in genes:
		codons = (re.findall(r"\S\S\S", str(seq)))	#this may be wrong
		codonstring=""
		print(geneID)
		for codon in codons:
				codonstring  = codonstring + str(codon) + " "
		GeneCodons[geneID] = codonstring
 print(GeneCodons)
except IndexError:
	print("no file provided")
except IOError as ex:
	print("Can't find", InFile, ':', ex.strerror)
#print(GeneCodons['gi|603555|emb|X83548.1|'])					
#print(GeneCodons['GeneA'])	

