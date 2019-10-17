#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'
print("taxa as a string:", taxa)
print(taxa[1])
print(type(taxa), ": taxa should be a string")

species = taxa.split(', ')
print(species)
print(species[1])
print(type(species), ": species should be a list")

print(sorted(species), "this should be sorted alphabetically")
print(sorted(species, key=len), "this should be sorted by the lenght")
print(sorted(species, key=len, reverse=True), "this should be sorted by the lenght (from the longest)")

