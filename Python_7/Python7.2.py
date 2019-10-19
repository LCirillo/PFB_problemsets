#!/usr/bin/env python
import re
#i=0
with open("Python7.1input.txt","r") as Input_file, open("Python7.2output.txt","w") as Output_file:
 for line in Input_file:
 # re.sub(r"Nobody","Michael",line)
 # print(line)
 # i+=1
 # if re.search(r'Nobody', line):
  line = line.rstrip()
  line = line.replace('Nobody','Michael')
  Output_file.write(line + "\n")  


