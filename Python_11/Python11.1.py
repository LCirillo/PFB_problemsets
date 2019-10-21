#!/usr/bin/env python3
 
class DNA_Record(object):
	def __init__ (self, sequence, name, organism):
		self.sequence = sequence
		self.name = name
		self.organism = organism

Obj1 = DNA_Record('ACTAGTACGGCAT','Plk1','Homo Sapiens')
for i in [Obj1]: #remember squares
	print('name:',i.name,'organism:',i.organism,'sequence',i.sequence, sep='\n')

