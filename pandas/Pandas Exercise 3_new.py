# Pandas Exercise 3_new
import pandas as pd 


# Read all csv files:
microsoft_workers = pd.read_csv(r'D:\\Python\pandas\microsoft_workers.csv', index_col=0)  #  index is not treated as a column!
users_office = pd.read_csv(r'D:\\Python\pandas\users_office.csv', index_col=0)
department_location = pd.read_csv(r'D:\\Python\pandas\department_location.csv')

# another way to set the index after reading: microsoft_workers.set_index('User Name', inplace=True)

print('microsoft_workers:\n',microsoft_workers.head(3))
'''microsoft_workers:
                      Display Name   Job Title
User Name
chris@contoso.com     Chris Green  IT Manager
ben@contoso.com       Ben Andrews  IT Manager
david@contoso.com  David Longmuir  IT Manager'''

print('users_office:\n', users_office.head(3))
print('department_location:\n',department_location.head())

#Create a new DataFrame, “joined”, by joining the first and second tables
workers = pd.merge(microsoft_workers, users_office, on='User Name')
print('workers:\n', workers.head(3))
      #  reset the index
workers = workers.reset_index()
print('workers:\n', workers.head(3))
'''
workers:
                      Display Name   Job Title              Department  ...  Office Phone  Mobile Phone           Fax
User Name                                                              ...
chris@contoso.com     Chris Green  IT Manager  Information Technology  ...  123-555-1211  123-555-6641  123-555-9821        
ben@contoso.com       Ben Andrews  IT Manager  Information Technology  ...  123-555-1212  123-555-6642  123-555-9822        
david@contoso.com  David Longmuir  IT Manager  Information Technology  ...  123-555-1213  123-555-6643  123-555-9823
'''

#    Set the index of the joined table and the third table as “Department” and join between them
workers = workers.set_index('Department')
print('workers:\n', workers.head())
'''
workers:
            User Name    Display Name   Job Title  ...  Office Phone  Mobile Phone           Fax
0  chris@contoso.com     Chris Green  IT Manager  ...  123-555-1211  123-555-6641  123-555-9821
1    ben@contoso.com     Ben Andrews  IT Manager  ...  123-555-1212  123-555-6642  123-555-9822
2  david@contoso.com  David Longmuir  IT Manager  ...  123-555-1213  123-555-6643  123-555-9823
'''
department_location = department_location.set_index('Department')
print(department_location)
all_info = pd.merge(workers, department_location, on='Department' )
print(all_info.head(6))
'''                                User Name Display Name   Job Title  ...  State        Country Postal Code
Department                                                          ...
Information Technology  chris@contoso.com  Chris Green  IT Manager  ...     Wa  United States       98052
Information Technology  chris@contoso.com  Chris Green  IT Manager  ...     Wa  United States       98052
Information Technology  chris@contoso.com  Chris Green  IT Manager  ...     Wa  United States       98052
Information Technology  chris@contoso.com  Chris Green  IT Manager  ...     Wa  United States       98052
Information Technology  chris@contoso.com  Chris Green  IT Manager  ...     Wa  United States       98052
Information Technology    ben@contoso.com  Ben Andrews  IT Manager  ...     Wa  United States       98052
'''

#     Save the table with MY_DF.to_pickle('FILENAME.dat')
all_info.to_pickle('exercise3.pkl')

#Append this table and add another worker. Use any values you want.
all_info = all_info.append({'User Name': 'yael@contoso.com', 'Job Title': 'Veterinarian'}, ignore_index=True  )
print(all_info.tail())
'''
            User Name Display Name     Job Title  Office Number  ...     City State Country Postal Code
115    sam@contoso.il    Sam Boreg  House keeper       111005.0  ...  Rehovot    IL  Isreal     79801.0
116    sam@contoso.il    Sam Boreg  House keeper       111005.0  ...  Rehovot    IL  Isreal     79801.0
117    sam@contoso.il    Sam Boreg  House keeper       111005.0  ...  Rehovot    IL  Isreal     79801.0
118    sam@contoso.il    Sam Boreg  House keeper       111005.0  ...  Rehovot    IL  Isreal     79801.0
119  yael@contoso.com          NaN           NaN            NaN  ...      NaN   NaN     NaN         NaN
'''