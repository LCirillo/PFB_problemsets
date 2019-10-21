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
		AT_percentage = ((A_count + T_count)/self.count_nt())*100
		GC_percentage = 100- AT_percentage
		return AT_percentage, GC_percentage


FastaDict= {}	
Obj1 = DNA_Record('ACTAGTACGGCAT','Plk1','Homo Sapiens')
for i in [Obj1]: #remember squares
	AT_percentage,GC_percentage = Obj1.nt_composition() #for a function with two returns ypu need to assign two variables to catch the two returns
	print('name:',i.name,'organism:',i.organism,'sequence',i.sequence, 'lenght:', Obj1.count_nt(), "% AT", AT_percentage, "%GC", GC_percentage,sep='\n')
	geneID = '>' + i.name
	FastaDict[geneID] = i.sequence	
	print(geneID + '\n' + i.sequence)
	print(FastaDict)


#	print(type(i.sequence))
