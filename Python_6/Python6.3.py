#!/usr/bin/env python3

genes = {}
with open ("Python6.3input.txt","r") as file_IN:
 for line in file_IN:
  line = line.strip()
  Elements = line.split()
  count = len(Elements)
  if count == 2:
   gene_ID,seq = line.split()
   CompT = seq.replace('T','a')
   CompA = CompT.replace('A','t')
   CompC = CompA.replace('C','g')
   seq  = CompC.replace('G','c')
   RevSeq = seq[::-1]
   RevSeq = RevSeq.upper()
   genes[gene_ID] = RevSeq
   print('>',gene_ID,'\n',RevSeq, sep="")
  else:
   continue

# the if statement is required because some lines do not contain
# two elements, in particular there is a space at the bottom of the file

