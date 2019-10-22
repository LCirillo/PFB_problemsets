#!/usr/bin/env python3

from Bio import SeqIO

for seq_record in SeqIO.parse("Biopython11.1.fa","fasta"):
	print('ID:', seq_record.id)
	print('Sequence:',seq_record.seq)
	print('Lenght:',len(seq_record))




