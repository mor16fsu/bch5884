#!/usr/bin/env python3 
#github.com/mor16fsu/bch5884

import math

x=float(input("Please enter a value in degrees Farenheit to convert to degrees Kelvin:"))

print (type (x))
x=float(x)

y=math.floor(x-32)*5/9+273.15

print (y)
print ("The calculation is complete: Degrees Kelvin") 



