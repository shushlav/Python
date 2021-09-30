# *************************   NumPy    ************************************
# --------------------------------------------------------------------------
import numpy as np
arr = np.arange(90)     # 1D array with 90 numbers
arr.reshape(9, 10)       # 9 Rows with 10 numbers in row
# 3D array: 9 arrays with 2 rows each and 5 numbers in each row
arr = arr.reshape(9, 2, 5)
print(arr)
print(arr[4][0][2])  # 42

a = np.array([[1,2,3],[4,5,6]])
a = np.resize(a, (2,2))
print(a)

np_2d = np.array([[1.70, 1.70, 1.56, 1.87, 1.78, 1.39],
                  [75, 76, 58, 100, 75, 32]])
# an 2D array of height and weight in my family (only one type = float)
print(np_2d.shape)  # (2, 6)   2 rows, 6 columns
print(np_2d[0])  # [1.7  1.7  1.56 1.87 1.78 1.39] = fist row
print(np_2d[0, 2])  # 1.56 = first row, column number 2
print(np_2d[:, 1:3])  # [[ 1.7   1.56]
#  [76.   58.  ]]    both rows, columns no 1+2
print(np_2d[1, :])    # [ 75.  76.  58. 100.  75.  32.] = all of row 1
print(np.mean(np_2d[0, :]))  # 1.6666666666666667 mean height
print(np.mean(np_2d[1]))     # 69.33333333333333 mean weight
print(np.std(np_2d[1]))      # STD of the weight
print(np.max(np_2d[1]))  # 100.0   max weight

# Generate a 2-D array with 3 rows, each row containing 5 random numbers
x = np.random.rand(3, 5)

print(x)
y = np.random.choice(x[0])
print(y)
# (mean, std, no of samples), round to 2 numbers after dot
z = np.round(np.random.normal(1.75, 0.2, 100), 2)

print(z)

c = np.round(np.random.normal(65.5, 0.5, 100), 1)
print(c)

# ++++++++++++++++++++++++++ array calculations +++++++++++++++++++++++++++++++

a = np.array((range(4), range(10, 14)))
print(a)
# [[ 0  1  2  3]
# [10 11 12 13]]
b = np.array((range(4), range(10, 14)))
print(b)
print(a * b)
# [[  0   1   4   9]
# [100 121 144 169]]

b1 = b * 100
print(b1)
# [[   0  100  200  300]
# [1000 1100 1200 1300]]
b2 = b * 100.0
print(b2)
# [[   0.  100.  200.  300.]
# [1000. 1100. 1200. 1300.]]
print(b1 == b2)
print(b1.dtype)  # int64
print(b2.dtype)  # float64

print(a.sum())  # 52
print(np.sum(a))  # 52
print(a.mean())  # 6.5
print(np.mean(a))
print(a.prod())

print(a.var())
print(np.std(a))
print(np.argmin(a))  # the index of the min number = 0
print(a.argmax())    # the index of the max number = 7

# _________________array comparisons_________________

arr = np.array(range(0, 10))
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
print(arr < 3)  # [ True  True  True False False False False False False False]
print(arr[arr < 4])  # [0 1 2 3] Only the True elements is returned
sel = a < 4  # the condition is stored in a variable
print(a[sel])        # [0 1 2 3]

# [ True  True  True False False False False False False  True]
print(np.logical_or(arr < 3, arr > 8))
# [0 1 2 9] Only the True elements is returned
print(arr[np.logical_or(arr < 3, arr > 8)])     # [0 1 2 9]
print(arr[np.logical_and(arr > 3, arr < 11)])   # [4 5 6 7 8 9]

# =========== Selecting using integer array (as an index=indices):
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)
print(a[b])         # b is the indexes you select from a: [2. 2. 4. 8. 6. 4.]
print(a.take(b))    # same: # [2. 2. 4. 8. 6. 4.]

# For multi-D send multiple 1D integers
a = np.array([[2, 4], [6, 8]], float)
c = np.array([1, 1, 0, 0, 1, 1], int)
d = np.array([0, 0, 1, 1, 0, 0], int)
print(a[c, d])  # [6. 6. 4. 4. 6. 6.]  TODO understand.....in 2D
print(a[d, c])  # [4. 4. 6. 6. 4. 4.]
# print("dot product: ", c @ d) TODO doesn't work

# **************    np.where(condition, do X if true, do Y if false)
arr1 = np.where(np.logical_or(arr < 3, arr > 8), arr * 5, arr * (-5))
print(arr1)  # [  0   5  10 -15 -20 -25 -30 -35 -40  45]
#   =============  SORT ==================
# sorted:  [-40 -35 -30 -25 -20 -15   0   5  10  45]
print("sorted: ", np.sort(arr1))

g = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])
print(np.where(g < 4, g, -1))  # -1 is broadcast
# array([[ 0,  1,  2],
#       [ 0,  2, -1],
#       [ 0,  3, -1]])

# ---------------Random array

z = np.random.randint(10, size=6)
print(z)                         # [8 5 6 6 7 9]

'''                                   PUT
Replaces specified elements of an array with given values
np.put(a, ind, v, mode='raise')[source]
a= Target array
ind = Target indices, interpreted as integers
v= Values to place in a at target indices. '''

b = np.arange(6)
print(b)  # [0 1 2 3 4 5]
np.put(b, 0, 6)
print(b)  # [6 1 2 3 4 5]
c = np.array(range(5))  # [0 1 2 3 4]
print(c)
b.put(0, c[-1])  # replace the first element of "b" with the last element of "c"
print(b)         # [4 1 2 3 4 5]

# ____________________Statistics & random sampling_______________________

# (a) Create a 2-D array of shape (2, 4) containing two lists (range(4), range(10, 14)) and assign it to the variable "a"
a = [np.arange(4), np.arange(10, 14)]  #([array([0, 1, 2, 3])], [array([10, 11, 12, 13])])
a1 = np.array((range(4), range(10,14)))  #[[ 0  1  2  3]
                                        #   [10 11 12 13]]
print(np.median(a1))    #6.5
print(np.corrcoef(a1))  # [[1. 1.]
                        #  [1. 1.]]                             

print(np.random.rand(2,4))    #between 0.0, 1.0
#[[0.77065897 0.82455098 0.84996689 0.11188479]
# [0.04153292 0.9488284  0.67824436 0.0979049 ]]
print(np.random.randint(2,10))   # selects random integer between 2 to 10

#    a random sample np.random.normal(Mean, STD, size))
b = np.random.normal(0, 1, 40)
print(b)   # [-0.26094183  0.37434045 -0.26444266  0.76178146......
b = np.round(np.random.normal(0, 1, 40), 2)  #עיגול המספר אחרי הנקודה ל 2
print(b)   #[-0.37  1.01  0.6  -0.2   0.21 -0.   -0.07  .....

# shuffle the random numbers: np.random.shuffle(b)
#This function only shuffles the array along the first axis of a multi-dimensional array. The order of sub-arrays is changed but their contents remains the same.

arr = np.arange(10)
np.random.shuffle(arr)
print(arr)
arr = np.arange(9).reshape((3, 3))
print(arr)                          #[[0 1 2] [3 4 5] [6 7 8]]
np.random.shuffle(arr)
print("shuffle: \n", arr)             #  [[3 4 5]  only this axis is shuffled
                                      #  [0 1 2]
                                      #  [6 7 8]]



l = list(range(10))   #range returns a lazy sequence object - it does NOT return a list. 
print("l:" , l)     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
np.random.shuffle(l)
print(l)            # [1, 7, 9, 4, 3, 0, 2, 5, 8, 6]