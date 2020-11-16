#!/usr/bin/env python3 
#https://github.com/mor16fsu/bch5884
#Mitchell Roth 


import numpy as np
from matplotlib import pyplot  
from scipy.signal import find_peaks_cwt

#Read the file
f=open("superose6_50.asc",'r')
lines=f.readlines()
f.close()

#Make two lists for both time and absorbance 

time=[]
absorbance=[]
for i in lines[3:]:
    words=i.split()
    try:
        time.append(float(words[0]))
        absorbance.append(float(words[1]))
    except:
        print("parsed", i)            
        continue 

#Find the peaks

threshold=80
peaks=[]
centroid=[]
centroid_peaks=[]
for i in range((len(absorbance))-1):
    a=absorbance[i-1]
    b=absorbance[i]
    c=absorbance[i+1]
    if b>=a and b>=c and b>threshold:
        peaks.append(absorbance[i])
        centroid.append(time[i])
        centroid_peaks.append((time[i],absorbance[i]))
#print(peaks)
print("The peaks are at the following x,y values (time,absorbance):")
print(centroid_peaks)

#Find the slopes;(y2-y1/x2-x1) 

slopes=[]
for i in range((len(absorbance))-1):
    delta_x=time[i+1]-time[i]
    delta_y=absorbance[i+1]-absorbance[i]
    slopes.append(delta_y/delta_x)
#print(slopes)

#Find the increasing and decreasing x and y values using slopes list
threshold=5
increasing_x=[]
decreasing_x=[]
increasing_y=[]
decreasing_y=[]
combine_increasing=[]
combine_decreasing=[]


for i in range(len(slopes)):
    if slopes[i]>threshold:
        increasing_x.append(time[i])
        increasing_y.append(absorbance[i])
        combine_increasing.append((time[i],absorbance[i]))
for i in range(len(slopes)):
    if slopes[i]<threshold:
        decreasing_x.append(time[i])
        decreasing_y.append(absorbance[i])
        combine_decreasing.append((time[i],absorbance[i]))

#print(combine_increasing)

#Find the boundaries of where the peaks begin and end 
print("The boundaries of the peaks are at the following time values (minutes):")
print("The boundary for peak one ranges from:")
print((increasing_x[1]))
print("to") 
print((increasing_x[25]))
print("The boundary for peak two ranges from:")
print((increasing_x[25]))
print("to")
print((increasing_x[40]))
print("The boundary for peak three ranges from:")
print((increasing_x[40]))
print("to")
print((increasing_x[101]))
print("The boundary for peak four ranges from:")
print((increasing_x[101]))
print("to")
print((decreasing_x[460]))

#Define x coordinates and format the graph to make it look good
 
xcoords=[64.733,72.427,79.333,98.187,113.12]
colors=['r','k','b','g','y']
for xc,c in zip(xcoords,colors):
    pyplot.axvline(x=xc,label='line at x=[]'.format(xc),c=c)
pyplot.title('Size Exclusion Chromatogram (superose6_50.asc.)')
pyplot.xlabel('Time (min)')
pyplot.ylabel('Absorbance (mAu)')
pyplot.scatter
pyplot.scatter(centroid,peaks,color='red',marker='o')
pyplot.plot(time,absorbance)
pyplot.show()
