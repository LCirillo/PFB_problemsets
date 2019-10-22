#!/usr/bin/env python3

from Bio import SeqIO

#Create a dict from a FASTA file
FastaDict = SeqIO.to_dict(SeqIO.parse("Biopython11.1.fa","fasta"))

GeneIDs = list(FastaDict.keys())
Id_Seq_dict = {}
for i in  GeneIDs: #iterate through dict and get the seq. Note that this is not a conventional dict, sequences must be retrieved with .seq command.
		Id_Seq_dict[i] = str(FastaDict[i].seq)	
SeqStr = ''
Sequences = (list(Id_Seq_dict.values()))

GC_content = [] #This is the relative GC
SeqLen = []

for seq in Sequences:
	seq = seq.lower()
	countG = seq.count('g')
	countC = seq.count('c')
	lenght = len(seq)
	GC_percentage = (countG + countC)/lenght
	SeqLen.append(lenght)	
	GC_content.append(GC_percentage)

N_sequence = len(Id_Seq_dict.keys())
AvgSeqLenght = sum(SeqLen)/len(SeqLen)
AvgGC = sum(GC_content)/len(SeqLen)

print ('4- there are',len(Id_Seq_dict.keys())  ,'sequences in the Fasta')
print('5-  The average sequence lenght is:', AvgSeqLenght, 'nt')
print('6- the shortest sequence is:', min(SeqLen), 'nt long')
print('7- the shortest sequence is:', max(SeqLen), 'nt long' )
print('8- the richest GC sequence has:', max(GC_content), '% GC' )
print('9- the poorest GC sequence has:', min(GC_content), '% GC' )


