#!/usr/bin/env python3

with open('Python10.1input.txt') as InputFile:
	output = ''
	N_60mersList= []
	for line in InputFile:
		line = line.rstrip()
		linelenght = len(line)
		N_60mers = int(linelenght/60)
		if linelenght%60 != 0:
			N_60mers += 1
		for i in range(N_60mers + 1):
			i = i*60
			string = line[i:i+60]
			output = output + string + '\n'

#print(InputFile)
print(output)		
