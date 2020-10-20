import pandas as pd
from pathlib import Path


project_folder = Path("D:\\Python\\")


employee = project_folder / 'employees.csv'
student = project_folder / 'students.csv'
student2 = project_folder / 'students2.csv'
emp = pd.read_csv(employee)
stu = pd.read_csv(student)
stu2 = pd.read_csv(student2)
print(emp)
print(stu)
print(stu2)

#  Filter DataFrame by multiple OR conditions:
print("filter: ", stu2[(stu2.name == 'Yam') | (stu2.name == 'Gal') | (stu2.name == 'Chai')])

# Shorter way:
print("filter: ", stu2[stu2.name.isin(['Yam', 'Gal', 'Chai'])])
# Invert the filter:
print("filter invert: ", stu2[~stu2.name.isin(['Yam', 'Gal', 'Chai'])])

#new = stu1.merge(stu2,on=['Team','Year'],how='left')
adding_all = pd.merge(emp, stu2, how='outer')    # how='outer' joins all values and all rows (without duplicates!)
print('--------------how = outer: Join Data. retains all values, all rows!! without duplicates!\n')
print(adding_all)

new = adding_all.merge(stu, how='left')  # joins all values and all rows (without duplicates!)
new1 = adding_all.merge(stu, how='right')  # how = right: Only matching rows from both sets
print('--------------how = left:\n')
print(new)
print('----------------how = right: Only  rows that are unique to one of the sets:\n')
print(new1)

new2 = adding_all[~adding_all.name.isin(stu2.name)]
print('~.isin: All rows in adding_all that DONOT have a match in stu2:\n')
print(new2)
new3 = adding_all[~adding_all.name.isin(stu.name)]
print('new3')
print(new3)
new4 = stu[stu.name.isin(stu2.name)]
print('All rows in stu that have a match in stu2')
print(new4)

