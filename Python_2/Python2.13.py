#!/usr/bin/env python3
import sys
var = sys.argv[1]
var = float(var)

if var>0:
 print(var, 'is positive')
 if var>50:
  print(var, 'is greater than 50')
  if var%3==0:
   print(var, 'is divisible by 3')
  else:
   print(var, 'is not Divisible by 3')

 elif var==50:
  print(var,'is equal to 50, not divisible by 3')
 
 else:
  print(var, 'is smaller than 50')
  if var % 3 ==0:
   print(var, 'is divisible by 3')
  else:
   print(var, 'is not Divisible by 3')
  
elif var == 0:
 print(var, "is equal to 0")

else:
 print(var, 'is negative')
 if var>-50:
  print(var, 'is greater than -50')
  if var % 3 ==0:
   print(var, 'is divisible by 3')
  else:
   print(var, 'is not Divisible by 3')
  
 elif var==-50:
  print(var,'is equal to -50, not divisible by 3')
 
 else:
  print(var, 'is smaller than -50')
  if var % 3==0:
   print(var, 'is divisible by 3')
  else:
   print(var, 'is not divisible by 3')

