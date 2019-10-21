#!/usr/bin/env python3
 
class DNA_Record(object):
	def __init__ (self, sequence, name, organism):
		self.sequence = sequence.upper() #I put them upper because of the nt_composition
		self.name = name.upper()
		self.organism = organism.upper()
	
	def count_nt(self) :
		lenght = len(self.sequence)
		return lenght #remember to define a return, otherwise the var will not be stored
	def nt_composition (self):
		A_count = self.sequence.count('A')
		T_count = self.sequence.count('T')
		G_count = self.sequence.count('G')
		C_count = self.sequence.count('C')
		AT_percentage = (A_count + T_count)/self.count_nt()
		return AT_percentage




	
Obj1 = DNA_Record('ACTAGTACGGCAT','Plk1','Homo Sapiens')
for i in [Obj1]: #remember squares
	print('name:',i.name,'organism:',i.organism,'sequence',i.sequence, 'lenght:', Obj1.count_nt(), "% AT", Obj1.nt_composition(),sep='\n')
	print(type(i.sequence))
