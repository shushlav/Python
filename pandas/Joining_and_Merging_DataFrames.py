#https://www.w3resource.com/python-exercises/pandas/joining-and-merging/index.php

import pandas as pd
from pandas.core.indexes.base import Index 
'''
Prepare the files:
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})
student_data1.to_csv('D:\Python\pandas\student_data1.csv')
student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})
student_data2.to_csv('D:\Python\pandas\student_data2.csv')
'''
stu1 = pd.read_csv('D:\Python\pandas\student_data1.csv', delimiter=',', header=0, skipinitialspace = True)
stu2 = pd.read_csv('D:\Python\pandas\student_data2.csv', delimiter=',',header=0, skipinitialspace = True)
print(stu1.columns.values)     # to see an array of your column names ['student_id,name,marks']

print(stu1['name'])
print(stu2)
                    #  join the two given dataframes along ROWS and assign all data
conc_students = pd.concat([stu1, stu2], axis=0)    # axis=0 : rows under rows
print("*******************concatenate:\n", conc_students)

all_students = pd.merge(stu1, stu2, how='outer')   #how=outer: use union of keys from both frames
print("*****************merge:\n",   all_students)

                    #    join the two given dataframes along COLUMNS and assign all data
conc_students2 = pd.concat([stu1, stu2], axis=1)    # axis=1 : columns
print("*******************concatenate columns:\n", conc_students2)

                    #       append rows to an existing DataFrame and display the combined data
student_append_rows = stu1.append(stu2, ignore_index = True)
print('****************student_append_rows:\n',student_append_rows)  

                    # 4      append a list of dictioneries or series to a existing DataFrame and display the combined data
dict_1 = [{'student_id': 's6', 'name': 'Scarlette Fisher', 'marks': 203},
          {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]
appstudic = stu1.append(dict_1, ignore_index = True)
print(appstudic)

                    # 5      join the two given dataframes along rows and merge with another dataframe along the common column id
conc_students = pd.concat([stu1, stu2], axis=0) #concatenate along rows
exam = pd.read_csv('D:\Python\pandas\exam_data.csv', delimiter=',', header=0, skipinitialspace = True)
print(exam.columns.values)
studentsWExam = pd.merge(conc_students, exam, on='student_id', left_index=False)  # merge only student_id that exist on conc_students!!
print(studentsWExam)
                    #  6  join the two dataframes with matching records from both sides where available
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

new_data = pd.merge(student_data1, student_data2, how='outer')
print("join based on matching records:\n", new_data)
                          # inner: form intersection of calling frame’s index (or column if on is specified) with other’s index, preserving the order of the calling’s one.
merged_data = pd.merge(student_data1, student_data2, on='student_id', how='inner')   # only S4 S5 ovrlap
print("Merged data (inner join):")
print(merged_data)

                           # 8 + 9 +10  join (left join) the two dataframes using keys from left dataframe only.
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
merged_datas = pd.merge(data1, data2, how='left')         #keys from left dataframe only
print('merge by keys from data1(left):\n', merged_datas)
'''
merge by keys from data1(left):
   key1 key2   P   Q    R    S
0   K0   K0  P0  Q0   R0   S0
1   K0   K1  P1  Q1  NaN  NaN
2   K1   K0  P2  Q2   R1   S1
3   K1   K0  P2  Q2   R2   S2
4   K2   K1  P3  Q3  NaN  NaN
'''
merged_datas1 = pd.merge(data1, data2, how='right')       #keys from right dataframe only
print('merge by keys from data2(right):\n', merged_datas1) 
'''
merge by keys from data2(right):
   key1 key2    P    Q   R   S
0   K0   K0   P0   Q0  R0  S0
1   K1   K0   P2   Q2  R1  S1
2   K1   K0   P2   Q2  R2  S2
3   K2   K0  NaN  NaN  R3  S3
'''
merged_datas2 = pd.merge(data1, data2, how='outer') 
print('merge by multiple join keys:\n', merged_datas2)     # multiple join keys
'''
merge by multiple join keys:
   key1 key2    P    Q    R    S
0   K0   K0   P0   Q0   R0   S0
1   K0   K1   P1   Q1  NaN  NaN
2   K1   K0   P2   Q2   R1   S1
3   K1   K0   P2   Q2   R2   S2
4   K2   K1   P3   Q3  NaN  NaN
5   K2   K0  NaN  NaN   R3   S3
'''
merged_datas3 = pd.merge(data1, data2, how='inner') 
print('merge by intersection:\n', merged_datas3)           # intersection  = inner
'''
merge by intersection:
   key1 key2   P   Q   R   S
0   K0   K0  P0  Q0  R0  S0
1   K1   K0  P2  Q2  R1  S1
2   K1   K0  P2  Q2  R2  S2
'''

                                # create a new DataFrame based on existing series, using specified argument and override the existing columns names

s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
#df = pd.concat([s1, s2, s3], ignore_index=True, axis=1, names=['column1', 'column2', 'column3'])
df = pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3'])
print(df)
'''
   column1  column2  column3
0        0        0        0
1        1        1        1
2        2        2        4
3        3        3        5
'''
                                #create a combination from two dataframes where a column id combination appears more than once in both dataframes
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
new = pd.merge(data1, data2, on='key1')    # many-to-many join case
print(new)                      
'''
  key1 key2   P   Q   R   S
0   K0   K0  P0  Q0  R0  S0
1   K1   K0  P2  Q2  R1  S1
2   K1   K0  P2  Q2  R2  S2
'''
