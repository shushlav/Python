# pandas

import pandas as pd

# Pandas DataFrame is nothing but an in-memory representation of an excel sheet via Python programming language
# So, Pandas DataFrame is similar to excel sheet 

# As depicted in excel sheet above, if we consider column names as “Keys” and list of items under that column as “Values”, 
# we can easily use a python dictionary to represent the same as:
my_dict = { 
     'name' : ["a", "b", "c", "d", "e","f", "g"],
     'age' : [20,27, 35, 55, 18, 21, 35],
     'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
     
df = pd.DataFrame(my_dict)
df.set_index('name')  # the first column
print("index:", df.index)   # For Row Indexes: index: RangeIndex(start=0, stop=7, step=1)
print(df.head())   # Displays 1st Five Rows 
print(df.tail())    # Displays last Five Rows
print(df.head(2))   # Displays 1st two Rows  
print("columns:", df.columns)   # For Columns:  columns: Index(['name', 'age', 'designation'], dtype='object')
'''
# Deleting Rows and Columns from DataFrame

# Using Dictionary Syntax → To remove a Column, we’ll use del as
del df['designation']
print()
print(df)

#using drop
# The second argument “1” in function drop(...) denotes deletion of the “Column”, 
# whereas “0” means deletion of the “Row
# Delete Column "age"

#df.drop('age',1)

df.drop([2,3,4],0) #  Delete Rows with index "2","3", & "4" ( index , row)
print("Delete the Row with Index 3")
print(df)
'''
df.loc[-1] = [2, 3, 4]  # adding a row as the first raw of values
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index
print("after index shifting:")
print(df)