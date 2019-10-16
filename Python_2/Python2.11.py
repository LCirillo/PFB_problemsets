#!/usr/bin/env python3
import sys
var = sys.argv[1]
var = float(var)

if var>0:
 print('Positive')
 if var>50:
  print('greater than 50')
  if var%3==0:
   print('Divisible by 3')
  else:
   print('Not Divisible by 3')
 elif var==50:
  print('equal to 50')
 else:
  print('smaller than 50')
  if var%2 == 0:
   print('number is even')
  else:
   print('number is odd')
elif var==0:
 print('Value equal to 0')
else:
 print('Negative')
