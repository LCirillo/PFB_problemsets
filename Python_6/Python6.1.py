#!/usr/bin/env python3

with open ("Python6.1input.txt") as file_obj:
 for line in file_obj:
  line = line.strip() 
  Upper = line.upper()
  print(Upper)


