#!/usr/bin/env python3
#github.com/mor16fsu/bch5884

import math 

x1=input ("Please enter a value for x1 for point A on the triangle:")
print (type (x1))
x1=int(x1)

y1=input ("Please enter a value for y1 for point A on the triangle:")
print (type (y1))
y1=int(y1)

x2=input("Please enter a value for x2 for point B on the triangle:")
print (type (x2))
x2=int(x2)

y2=input ("Please enter a value for y2 for point B on the triangle:")
print (type (y2))
y2=int(y2)

x3=input ("Please enter a value for x3 for point C on the triangle:")
print (type (x3))
x3=int(x3)

y3=input ("Please enter a value for y3 for point C on the triangle:")
print (type(y3))
y3=int(y3)

da=x2-x1
db=y2-y1
dc=x3-x2
dd=y3-y2
de=x3-x1
df=y3-y1

AB=math.sqrt(da**2+db**2)
BC=math.sqrt(dc**2+dd**2)
CA=math.sqrt(de**2+df**2)
 

CAsquared=(CA**2)
BCsquared=(BC**2)
ABsquared=(AB**2)

subtract=(CAsquared-BCsquared-ABsquared)

multiply=(-2*BC*AB)

beta=(subtract/multiply)

betaangle=math.acos(beta)*180/math.pi


convert=(math.sin(math.radians(betaangle)))

sinalpha=((BC*convert)/(CA))

alphaangle=math.asin(sinalpha)*180/math.pi

gammaangle=180-alphaangle-betaangle

print (alphaangle, betaangle, gammaangle)

print ("Alpha,Beta,Gamma")

print ("Done!")


