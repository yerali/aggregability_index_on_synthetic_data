import numpy as np
import sys

mini=float(sys.argv[1])
maxi=float(sys.argv[2])
delt=float(sys.argv[3])

def drange(start, stop, step):
     r = start
     while r < stop:
         yield r
         r += step
         
i0=drange(mini,maxi,delt)

for x in i0:
   d=[]
#   print x
   with open('stat.dat') as s:
      for line in s:
         data = line.split()
         deci = float(data[0])
#         print deci,x
         if ( abs(deci-x)<0.001):
           d.append(float(data[1]))
   #print d
   print x,np.mean(d)
           
