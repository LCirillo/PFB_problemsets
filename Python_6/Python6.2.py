#!/usr/bin/env python3

with open ("Python6.1input.txt","r") as file_IN, open("Python_06_uc.txt","w") as file_OUT:
 for line in file_IN:
  line = line.strip() 
  Upper = line.upper()
  file_OUT.write(Upper + "\n")


