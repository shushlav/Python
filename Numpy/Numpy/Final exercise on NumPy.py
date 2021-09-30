#      NumPy Final exercise  
# @https://docs.google.com/document/d/1MDkF7O4BNn5LlGazanSJ9Y0PyShDQoXe-1lVtSLg2B8/edit#heading=h.39ryy8kacaej

# =================================
import numpy as np
#print(help())

a = np.array([1, 2, 3])      
b = a.astype(float)     # change type to float
print(b)                # [1. 2. 3.]
a = np.arange(11, dtype=int)            #[ 0  1  2  3  4  5  6  7  8  9 10]
a = np.linspace(0, 23, 7)
print(a)        #[ 0.          3.83333333  7.66666667 11.5        15.33333333 19.16666667 23.        ]
a = np.ones(100)*5
a = a.reshape(2, 5, 1, 2, 5, 1)
b = np.ones((2,5,1,5,2,1)) * 5.0    # shorter way....
                

#           Remove dimensions of size 1 from ndarray = np.squeeze
a  = np.squeeze(a)
print("squeeze: \n", a)
                   
print(a.shape)      #(2, 5, 2, 5)
#   #7
c = a.reshape(2, -1)   # reshape to only 2d(-1 if you want python to calculate the columns)
# The answer is c = a.reshape((10,10))
print("c: \n", c)
print(c.shape)  #(2, 50)
# -----------another example:
b = np.arange(6).reshape(1, 2, 1, 3, 1)
print(b)
'''
[[[[[0]
    [1]
    [2]]]


  [[[3]
    [4]
    [5]]]]]
    '''
print(b.shape)          #(1, 2, 1, 3, 1)
b =b.squeeze()
print(b)
# [[0 1 2]
#  [3 4 5]]
print(b.shape)  #(2, 3)
b = b.reshape(3, -1)
print(b.shape)  # (3, 2)
#-----------#8----------------------------------------------------
a = np.arange(10)
b = np.arange(5)
# change a to create the array [0,1,2,3,4,4,3,2,1,0]
a[5:] = a[b[::-1]]
print(a)                    # [0 1 2 3 4 4 3 2 1 0]         
#--------------9-16-----------------------------------------------------
a = np.random.normal(21.0, 4.5, 324)  # or (21.0, 4.5, size=(3,3,12,3))
a = a.reshape(3, 3, 12, 3)
print(a)
print(a.shape)          # (3, 3, 12, 3)
print(a.dtype)          # float64
#   #10
print("mean = ", a.mean())
print("std = ", a.std())
print("var =", a.var())
print("min = ", a.min())
print("dimensions = ",len(a.shape))
#11 get: only 2nd dimension
print("mean of 2D = ", a.mean(axis=1))   #my answer
print("*************a.mean: ", a.mean(1))  # their answer - the same!
#12
a = a.reshape(1,-1)  # -1 אם לא יודעים כמה עמודות המחשב יחשב לבד
print(a.shape)        #(1, 324)
b = a.flatten()       #(324,)     Their answer
print(b.shape)
print("*********************flatten", b)
#13
b = a[np.logical_and(a>15, a<26)]    # Their answer: b = a[(a>15)&(a<26)]

#14 -----------------------------------clip as NaN
b = np.clip(a, 15, 26, out=None)    #Syntax : np.clip(a, a_min, a_max, out=None)
b[b==15] = np.NaN                    # put Nan instead of low
b[b==26] = np.NaN
print(b)
#15   np.nansum = Return the sum of array elements over a given axis treating (NaNs) as zero.
print('sum = ', np.sum(b))    #nan
print('sum=', np.nansum(b))   #4972.203496542883
#16
print('mean = ', b.mean())  #nan
# ------------------------------NaN-----------------
impressions = np.array([0,11000, 23000, 55000, 37000, 33000, 44500]) #num of ad displayed per day
clicks = np.array([0, 100,600,1000,2000,10000,15000])
ctr = clicks/impressions
print('ctr =', ctr)   # [nan 0.00909091 0.02608696 0.01818182 0.05405405 0.3030303 0.33707865]
print(np.mean(ctr))   #nan
print(np.argwhere(np.isnan(ctr)))     #[[0]]
#   17   -----------------------------------convert nan to 0 (np.nan_to_num)
c = np.nan_to_num(ctr, nan=0.0)
print(c)    #[0.0.00909091 0.02608696 0.01818182 0.05405405 0.3030303  0.33707865]
#                        -------save c and load again (np.savetxt, np.loadtxt)
np.savetxt("c", c, delimiter=',')
c_loaded = np.loadtxt("c")