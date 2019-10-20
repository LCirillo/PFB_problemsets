#!/usr/bin/env python3
import re

dna = '''ACTAGTACAGTGCAGTGAT'''
match = re.match(r"[ATCGNatgcn]+", str(dna)) #DO NOT USE RE.SEARCH
line = match.group(0)
linelenght = len(str(line))
print(dna)
print(line)
print(linelenght)

