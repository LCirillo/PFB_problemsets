#!/usr/bin/env python3

#in the file the first column is the unique identifier of the gene
#I need to count that

GeneCount = {}
IDList = []
Name_Dict = {}
with open('bowtie2.sam','r') as Input:
	for line in Input:
		line = line.split()
		GeneName = line[2]
		GeneName = GeneName.split('^')
		GeneName = GeneName[0]
		ID  = line[0]
		Name_Dict[GeneName] = ID
print(Name_Dict)
	#for GeneName in Name_Dict:	
#		IDs = Name_Dict[GeneName]
#		print(IDs)
#		GeneCount[GeneName] = set(Name_Dict[GeneName])

#t_name_Dict = Name_Dict.items()
#for item in t_name_Dict:
	

#	for name in Name_Dict:
#		if Name_Dict[name] in Name_Dic :
#		#	ID_Dict[ID] = gene
#			GeneCount[name] += 1
#		else:
#			GeneCount[name] = 1
 
#print (GeneCount)
print(Name_Dict)



