#!/usr/bin/env python
import re
i=0
with open("Python7.1input.txt","r") as Input_file:
 for line in Input_file:
  i+=1
  if re.search(r'Nobody', line):
   print('There is a Nobody in line', i)
  else:
   continue



