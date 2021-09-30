# Fancy slicing\indexing
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, pi, sin, cos

a = np.linspace(0, 2*pi, 21)  # linspace=Return evenly spaced numbers over a specified interval.
print(a)

b = sin(a)
plt.plot(a,b)


# find all the dots above x=0
mask = b >=0     # a boolean
print(mask)

plt.plot(a[mask], b[mask], 'ro')   # only the places where the mask=True


# we can seek also a complex operation: 
mask2 = (b >= 0) & (a<=pi/4)
plt.plot(a[mask2], b[mask2], 'b*')

plt.show()

#============================================
#a = np.array([0,1,2,3,4,5][10,11,12,13,14,15][20,21,22,23,24,25][30,31,32,33,34,35])
a = np.arange(0,25)
a.shape = 5,5
#  בחיפוש אלכסוני של נתונים
print(a)
print(a.diagonal())    #[ 0  6 12 18 24]   Only reads the values. not writing
print(a.diagonal(1))   #[ 1  7 13 19]