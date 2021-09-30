#lesson #6
import matplotlib.pyplot as plt

import numpy as np


array2 = np.loadtxt (r'D:\Documents\יעל\Python\Numpy\float_data.txt')
print(array2)       #[[1. 2. 3. 4.][5. 6. 7. 8.]]
#change the type to int32:
array2 = np.loadtxt (r'D:\Documents\יעל\Python\Numpy\float_data.txt', dtype=np.int32)
print(array2)       #[[1 2 3 4][5 6 7 8]]

#load a file and skip the first row:
array3 = np.loadtxt(r'D:\Documents\יעל\Python\Numpy\float_data_with_header.txt', skiprows=1)
print(array3)   #[[10. 20.  0. 40.][ 5.  6.  7.  8.]]
#load a file, skip the first row, skip comments, use only specific columns:
array1 = np.loadtxt(r"D:\Documents\יעל\Python\Numpy\complex_data_file.txt", delimiter=',', dtype = np.int32, skiprows = 1, usecols = (0,1,2,4),comments='%',unpack=True)
print(array1)

np.savetxt( "new_array.txt", array1)


