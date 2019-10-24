#!/usr/bin/env python3
row = ''
contigs = {}
count =0
with open('ecoli_0.25.contigs.fasta','r') as InFile : 
	for line in InFile:
		if ">" in line:
			row = ''
			line = line.strip()
			line = line.replace('>','')
			line = line.split()
			ID = (line [0])
			
			count +=1
			contigs[ID] = '' 
		else:
			line = line.strip()
			row = row + line 
			contigs[ID] = row

# 1. how many contigs are there?
print('There are', count, 'contigs in the file')
# 2,3. What is the shortest and longest contig?
Ordered_contigs = list(reversed(sorted((len(value), key) for (key,value) in contigs.items())))
#Ordered_contigs_reverse  = list(reversed(sorted((len(value), key) for (key,value) in contigs.items()))
shortest = str(Ordered_contigs[-1][1])
longest = str(Ordered_contigs[0][1])
count_GenSize = 0

print('The shortest contig is', shortest,':', len(contigs[shortest]), 'nt long')
print('The longest contig is', longest,':', len(contigs[longest]), 'nt long')

# 4. calculate N50 and L50
count_GenSize = 0
for ID in contigs:
	lenght = len(contigs[ID])
	count_GenSize = count_GenSize + lenght
Half_GenSize = count_GenSize // 2
count = 0
iterations = 0
for contig in Ordered_contigs:
	contig_size = int(contig[0])
	contig_ID = str(contig[1])
	#size = len(contigs[contig_ID])
	count = count + contig_size
#	print(contig)
	iterations += 1
	if count <  Half_GenSize:
		continue
	else:
		print('the contig at 50% of the genome is', contig_ID,':', contig_size, 'nt long')
		print('The N50 value (smallest number of contig to assemble 50% of the genome) is:', iterations)
		print('The L50 value (lenght of the contig spanning through the genome halfpoint) is:', contig_size)
		break

#N50 = str(Ordered_contigs[Half_GenSize][1])

#print(len(N50))


