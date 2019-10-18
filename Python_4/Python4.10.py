#!/usr/bin/env python3
import sys

#Get the first and last argument from command line
first = sys.argv[1]
last = sys.argv[-1]

print(first)
print(last)

if int(first)%2!=0:
 print('first is odd')
else:
 print('first is even')
