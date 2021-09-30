# Pandas ex 4 - https://shecodesconnect.com/DataAnalysis/Pandas_Ex4.html
import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df)
print(df.info())    #summary of the basic information = also:  df.describe()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, a to j
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   animal    10 non-null     object
 1   age       8 non-null      float64
 2   visits    10 non-null     int64
 3   priority  10 non-null     object
dtypes: float64(1), int64(1), object(2)
memory usage: 400.0+ bytes
'''
print(df.head(3))   # Return the first 3 rows of the DataFrame = df.iloc[:3]
'''
  animal  age  visits priority
a    cat  2.5       1      yes
b    cat  3.0       3      yes
c  snake  0.5       2       no'''

print(df[['animal','age']])    # Select just the 'animal' and 'age' columns = df.loc[:, ['animal', 'age']]
print("Select specific rows:\n", df.iloc[[3,4,8]])        # Prints only specified rows
'''
Select specific rows:
   animal  age  visits priority
d    dog  NaN       3      yes
e    dog  5.0       2       no
i    dog  7.0       2       no
'''
#  slice only the rows & columns that u want
print(df.loc[df.index[[3,4,8]], ['animal', 'age']])    # Combining positional and label-based indexing
print(' number of visits is greater than 3\n')
print(df[df['visits'] > 3])  #Select the rows where the number of visits is greater than 3 = Index: []
                                
print(df[df['age'].isnull()]) # # Select the rows where the age is missing, i.e. is NaN.
'''
  animal  age  visits priority
d    dog  NaN       3      yes
h    cat  NaN       1      yes'''
# Select the rows where the animal is a cat and the age is less than 3                               

print("Only cats less than 3:\n", df[(df['animal'] == 'cat') & (df['age'] < 3)]) 
'''
   age animal priority  visits
a  2.5    cat      yes       1
f  2.0    cat       no       3'''

#       ***Select the rows the age is between 2 and 4 (inclusive):
print(df['age'].between(2, 4, inclusive=True))     # Series.between(left, right, inclusive=True)
'''
   age animal priority  visits
a  2.5    cat      yes       1
b  3.0    cat      yes       3
f  2.0    cat       no       3
j  3.0    dog       no       1'''
                # Change the age in row 'f' to 1.5. Hint: you can use .loc(row,col)

df.loc['f', 'age'] = 1.5
                                # Calculate the sum of all visits.
df_sum = df['visits'].sum()
print('Sum = ', df_sum)         # Sum =  19