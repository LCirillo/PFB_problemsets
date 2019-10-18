#!/usr/bin/env python3

lines_Len = []
with open ("Python6.4input.fastq","r") as file_IN:
 for line in file_IN:
  line_len = len(line)
  lines_Len.append(line_len)
  
totLines = len(lines_Len)
totChar = sum(lines_Len)
AvgLenght = totChar/totLines 

print('There are', totLines,'lines')
print('There are', totChar,'characters')
print('on average, there are', AvgLenght,'characters per line')

