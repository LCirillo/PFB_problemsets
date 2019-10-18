#!/usr/bin/env python3

DNA = 'ATGCAGGGGAAACATGATTCAGGAC'

repA = DNA.replace('A','t')
repT = repA.replace('T','a')
repC = repT.replace('C','g')
repG = repC.replace('G','c')

Comp = repG.upper()
RevComp = Comp[::-1]

print(Comp)
print(RevComp)
