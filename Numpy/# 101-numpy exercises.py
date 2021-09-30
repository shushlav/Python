# 101-numpy exercises
#=============================

import numpy as np
from numpy.core.arrayprint import printoptions
#                           Import numpy as np and print the version number.
print(np.__version__)     # 1.20.1
#                           Create a 1D array of numbers from 0 to 9
arr = np.arange(0,10)
print(arr)      #[0 1 2 3 4 5 6 7 8 9]
#                           Create a 3×3 numpy array of all True’s
arr = np.full((3,3), True, dtype=bool)
print(arr)
                            #  Extract all odd numbers from arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr%2!=0])        #[1 3 5 7 9]   
                            #Replace all odd numbers in arr with -1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 !=0] = -1
print(arr)              #[ 0 -1  2 -1  4 -1  6 -1  8 -1]
                            # Replace all odd numbers in arr with -1 without changing arr                                           
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)     #(condition, return y, array)
print(arr)    #[0 1 2 3 4 5 6 7 8 9]
print(out)    #[ 0 -1  2 -1  4 -1  6 -1  8 -1]
                            #  Convert a 1D array to a 2D array with 2 rows
arr = np.arange(10)
arr = arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols
print(np.shape(arr))
print(arr) 
                           # Stack arrays a and b vertically  VSTACK   
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)                                                   
print(a)
print(b)
c =np.vstack((a,b))
print(c)
                            # Stack the arrays a and b horizontally HSTACK
d = np.hstack((a, b))
print(d)
        #[[0 1 2 3 4 1 1 1 1 1]
        # [5 6 7 8 9 1 1 1 1 1]]
                            #    Create the following pattern without hardcoding. 
a = np.array([1,2,3])
a1 = np.repeat(a, 3)    #[1 1 1 2 2 2 3 3 3]

a2 = np.tile(a, 3)      #[1 2 3 1 2 3 1 2 3]

b = np.r_[np.repeat(a, 3), np.tile(a, 3)]     # stack arrays vertically
print (b)   #[1 1 1 2 2 2 3 3 3 1 2 3 1 2 3 1 2 3]                         

                                #  Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
common = np.intersect1d(a,b)    #[2 4]
                               #      From array a remove all items present in array b
c = np.setdiff1d(a,b)   #[1 3 5 6]
                                #Get the positions where elements of a and b match
d = np.where(a == b)    #(array([1, 3, 5, 7], dtype=int64),)

                        #             Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
c = a[(a >= 5) & (a<=10)] #[ 6  9 10]

                                #Convert the function maxx that works on two scalars, to work on two arrays.                     
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

print(maxx(1, 5))

pair_max = np.vectorize(maxx, otypes=[float]) #Get the largest numbers in both arrays to ONE array
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a, b))       #[6. 7. 9. 8. 9. 7. 5.]

                                                #Swap columns 1 and 2 in the array arr
arr = np.arange(9).reshape(3,3)         #[[0 1 2][3 4 5][6 7 8]]
print(arr)    
print(arr[:, [1,0,2]])         # changes the order of the COLUMNS [[1 0 2][4 3 5][7 6 8]]
print("change rows",arr[[1,0,2], :])                #changes the order of the ROWS
arr[[0, 1]] =  arr[[1 , 0]]    # changes ROWS: [[3 4 5][0 1 2][6 7 8]]
print(arr)

print(np.swapaxes(arr, axis1=0, axis2=1))   #מחליף את כל השורות לעמודות
#[[3 0 6]
 #[4 1 7]
 #[5 2 8]]
                            
arr = np.arange(9).reshape(3,3)         #[[0 1 2][3 4 5][6 7 8]]
print("reverse rows",arr[::-1])         #Reverse the rows of a 2D array arr.                     
print("reverse columns",arr[:, ::-1])   #reverse columns [[2 1 0][5 4 3][8 7 6]]  

                                #Create a 2D array of shape 5x3 to contain RANDOM decimal numbers between 5 and 10.
rand_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
print(rand_arr)
#    option B:
rand_arr = np.random.uniform(5,10, size=(5,3))
print(rand_arr)  
                                # SET_PRINTOPTIONS
            #   Print or show only 3 decimal places of the numpy array rand_arr.
np.set_printoptions(precision=3)
print(rand_arr)  
            #   Pretty print rand_arr by suppressing the scientific notation (like 1e10)
np.random.seed(100)       # Create the random array
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)   #[[5.434e-04 2.784e-04 4.245e-04].....
np.set_printoptions(suppress=True, precision=6)  # precision is optional
print(rand_arr)   #[[0.000543 0.000278 0.000425].......

#               Limit the number of items printed in python numpy array a to a maximum of 6 elements.
a = np.arange(1500)
np.set_printoptions(threshold=6)        #[ 0  1  2 ... 12 13 14]
print(a)
np.set_printoptions(edgeitems=2)        # [ 0  1 ... 13 14]
print(a)
b = np.arange(10)
np.set_printoptions(threshold=np.inf, linewidth=np.nan)
print(b)                            #[0 1 2 3 4 5 6 7 8 9]  

            #Import the iris dataset keeping the text intact.   dtype='object'
iris = np.loadtxt('D:\Python\Structured_array DS\iris.data', delimiter=',', dtype='object')     
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris) 
# Print the first 3 rows
print(iris[0:3])         
                            # Extract the text column species from the 1D iris
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
species = np.array([row[4] for row in iris_1d])
print(species)                            

            #Convert the 1D iris to 2D array iris_2d by omitting(להשמיט) the species text field
iris = np.loadtxt('D:\Python\Structured_array DS\iris.data', delimiter=',', usecols=(0,1,2,3), dtype='float')
print(iris[:4])
                #28. Find the mean, median, standard deviation of iris's sepallength (1st column)
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu, med, sd)  #5.843333333333334 5.8 0.8253012917851409

                    #Create a normalized form of iris's sepallength (ABOVE) whose values range exactly between 0 and 1 
                    # so that the minimum has value 0 and maximum has value 1.
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/(Smax - Smin)
#or
# S = (sepallength - Smin) / sepallength.ptp()  # ptp=Range of values (maximum - minimum) along an axis.
np.set_printoptions(precision=3)  # 3 אחרי הנקודה
print("S: ", S)                    

                #Compute the softmax score of sepallength 
'''The softmax function transforms each element of a collection by computing the exponential of each element 
divided by the sum of the exponentials of all the elements.'''
#from scipy.special import softmax
#print(scipy.special.softmax(sepallength))     #TODO - install

                        # Find the 5th and 95th percentile of iris's sepallength
print(np.percentile(sepallength, q=[5, 95]))    # [4.6   7.255]

                        # How to insert values at random positions in an array?
                        # Insert np.nan values at 20 random positions in iris_2d dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
print(iris_2d.shape)    # (150, 5)
#np.random.seed(100)                       
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
print(iris_2d)
                        # Find the number and position of missing values in iris_2d's sepallength (1st column)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
print("Number of missing values: \n", np.isnan(iris_2d[:, 0]).sum())        #5
print("Position of missing values: \n", np.where(np.isnan(iris_2d[:, 0])))  #(array([13, 17, 47, 53, 91], dtype=int64),)

                        #Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
filtered = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
print(iris_2d[filtered])                       
                        # Select the rows of iris_2d that does not have any nan value.
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
print(iris_2d[~np.isnan(iris_2d).any(axis=1)])                                  # ~ inverts True/False                  
                        # 38. Replace all ccurrences of nan with 0 in numpy array
iris_2d = np.nan_to_num(iris_2d, nan=0)   # also iris_2d[np.isnan(iris_2d)] = 0
print("Replace nan w 0:\n", iris_2d[:5])                        
                            
                            # Find the correlation between SepalLength(1st column) and PetalLength(3rd column) in iris_2d
                            # # Correlation coef indicates the degree of linear relationship between two numeric variables.
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
R = np.corrcoef(iris_2d[:,0], iris_2d[:,2])     #0.872
print(R)

#Find out if iris_2d has any missing values
# any - Test whether any array element along a given axis evaluates to True.
# Returns single boolean unless axis is not None
print(np.isnan(iris_2d).any())  #False

                            # Find the unique values and the count of unique values in iris's species
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')  # # Import iris keeping the text column intact
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# Extract the species column as an array
species = np.array([row.tolist()[4] for row in iris])
# Get the unique values and the counts
u = np.unique(species, return_counts=True)  # return_counts = return the number of times each unique item appears
print("unique:", u)



