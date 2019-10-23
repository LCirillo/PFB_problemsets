#!/usr/bin/env python3
import re
import sys


i = 0
queries = []
results = []
for hit in sys.argv[1:]: #opens all the files
	with open(hit,'r') as InFile:
		for line in InFile:
			line = line.rstrip()
			if '#' in line and i==0:
				i += 1
				line = line.split()
				queries.append(line[5])
			elif '#' not in line:	
					[query, subject, identity, ali_length, mismatches, gap_opens, q_start, q_end, s_start, s_end, evalue, bit_score] = line.split()
					varList = [identity, ali_length, evalue]
					results.append(varList)
					i += 1
					if i > 1:
						i = 0
						break
			else:
				i += 1
				continue		

Dict_QR = dict(zip(queries, results))
FirstRow = ('Mat' + '\t' + 'id' + '\t' + 'alen' + '\t' + 'eval')
print(FirstRow)
for query in Dict_QR:
	Row= str(str(query) + '\t' + (str(Dict_QR[query][0])) + '\t' + (str(Dict_QR[query][1])) + '\t'  + (str(Dict_QR[query][2])))
	print(Row)

