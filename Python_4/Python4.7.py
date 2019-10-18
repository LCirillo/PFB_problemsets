#!/usr/bin/env python3

loop = [101,2,15,22,95,33,2,27,72,15,52]
sort_loop = sorted(loop)
even = []
odd = []
for i in sort_loop:
 print(i)
 if i%2==0:
  even.append(i)
 else:
  odd.append(i)

print(even)
print(odd)
print(sum(even))
print(sum(odd))

