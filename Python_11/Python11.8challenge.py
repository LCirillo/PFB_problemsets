#!/usr/bin/env python3
 
class DNA_Record(object):
	def __init__ (self, sequence, name, organism):
		self.sequence = sequence.upper() #I put them upper because of the nt_composition
		self.name = name.upper()
		self.organism = organism.upper()
Obj1 = DNA_Record('ACTAGTACGGCAT','Plk1','Homo Sapiens')
Obj2 = DNA_Record('ATAGTACGGCAT','Plk1','Homo Sapiens')
#Obj3 = DNA_Record('ACTAGTACGGCAT','hBora','Homo Sapiens')

Obj1List = []
for i in [Obj1]:
	Obj1List.append(i.name)
	Obj1List.append(i.sequence)
	Obj1List.append(i.organism)
Obj2List = []
for i in [Obj2]:
	Obj2List.append(i.name)
	Obj2List.append(i.sequence)
	Obj2List.append(i.organism)

print(Obj1List)	
print(Obj2List)	
#if Obj1List == Obj2List:
print(Obj1List == Obj2List)

