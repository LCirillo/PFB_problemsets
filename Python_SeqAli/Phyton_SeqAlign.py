#!/usr/bin/env python3
#import re
#i = 0
#queries = []
#lines = {}
#with open('ss_rand5-200_v_qfo_BL50.txt.1','r') as BL50:
# for line in BL50:
#		i = 0
#		line = line.rstrip()
#		if '#' in line:
#			line.split()
#			print (line)
#			i += 1
#		if '#' not in line:	
#			[query, subject, identity, ali_length, mismatches, gap_opens, q_start, q_end, s_start, s_end, evalue, bit_score] = line.split()
#			i += 1
#			if i > 0:
#				break
#		else:
#			continue		
#print(mismatches)
#print(lines)

import sys
hit_files = []
field_str = "q_seqid s_seqid percid alen mism gaps q_start q_end s_start s_end evalue bits"
fields = field_str.split(' ')

hits_list = []

for hit_file in sys.argv[1:]:
	with open (hit_file, 'r') as fin:
		for line in fin:
			if line[0] == '#':
				continue
			hit_data =  dict(zip(fields,line.strip('\n').split('\t')))
			hit_data['file'] = hit_file
			hits_list.append(hit_data)
			break
for hit in hits_list:
	print ('\t'.join([hit[x] for x in ('file','percid','alen','evalue')]))


