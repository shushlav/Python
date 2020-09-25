import pandas as pd
from pathlib import Path


project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'

# attendance_log = pd.read_csv('Attendance_log.csv')

# The file Must be w\o any blank lines!!
check_emp = pd.read_csv(open_employee, index_col='employee_id')
print(check_emp)
# Index(['employee_id', 'name', 'phone', 'age'], dtype='object')
print(check_emp.columns)

def check_info(info):
    if len(info) != 4:
        print ('Please write all the information as requested')
        add_employee()
    if not info[0].isnumeric():
        print ('id number must contains only numbers')
        add_employee()
    if not info[1].strip().isalpha():
        print ('Name  must contains only letters')
        add_employee()
    if not info[2].strip().isnumeric():
        print ('Phone-number must contains only numbers')
        add_employee()
    if not info[3].strip().isnumeric():
        print ('age must be numbers only')
        add_employee()
    if len(info[3].strip())!= 2:
        print ('age must contains 2 numbers only')
        add_employee()


def add_employee():
    # open the file
    employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)

    try:
        new = input(
            "Please write: Employee_ID, Name, Phone, Age (using commas as separators):\n")
    # checking for errors:
    except ValueError:
        print("You must enter all the data mentioned with commas")
        # Separate on comma.
    info = new.split(",")  # separate every string between ","
    #check if the info is correct:
    check_info(info)
    # Pass this list to DataFrame’s constructor to create a dataframe object
    info_df = pd.DataFrame(
        [info], columns=['employee_id', 'name', 'phone', 'age'])
    print(info_df)
    # check if the name already exists:
    if info_df.values in employees.values:
        print('***************This employee already exists ************************\n')
    # appends the add_file to the employees file w new index
    employees = pd.concat([employees, info_df], ignore_index=True)
    employees = employees.drop_duplicates()  # deletes any duplicates in file
    print(employees)
    employees.to_csv(open_employee, index=False)

# +++++++++++++++++ Add from file


def add_e_fromFile():
    try:
        new = input("Please enter the full path of the file:\n")
    # checking for errors:
    except ValueError:
        print("You must enter the FULL path")
    employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    # The file Must be w\o any blank lines!!
    add_file = pd.read_csv(new, index_col=False, skipinitialspace=True,
                           skip_blank_lines=True)  # reads the file to be added
    # Check if all the data of all employees is supplied
    # It returns True if all elements within a series or along a Dataframe axis are non-zero, not-empty or not-False.טע==
    print(add_file.isna().any().any())
    if add_file.isna().any().any() == True:  
        print('The data in the file is not full. please fill the data and try again')
        delete_fromFile()
    else:
        print('All data is filled')
     
    # Check for duplicates:
    duplicates = employees[employees.name.isin(
        add_file.name)]  # checks for common names
    if len(duplicates) != 0:
        print('******The duplicates names (in both files) are:\n')
        print(duplicates)
        print('Duplicates will not be merged')

    # Merge the files to a new DF
    emp_df = pd.merge(employees, add_file, how='outer')
    # delete duplicates
    emp_df = emp_df.drop_duplicates()  # deletes any duplicates in file
    print(emp_df)
    # write to csv:
    emp_df.to_csv(open_employee, index=False)
    emp_df.to_csv('D:\\Python\\employeesTest1.csv', index=False)
    
    
# ------------------------Delete employee manually
def delete_employee():
    employees = pd.read_csv(open_employee, index_col=False, skipinitialspace=True, skip_blank_lines=True)

    emp = employees.drop_duplicates()  # deletes any duplicates in file
    print(emp)
    
    try:
        new = input("Please enter the name of the employee to delete:\n")
    # checking for errors:
    except ValueError:
        print("You must enter only a name")
    if new not in emp['name']:
        print('No such employee in our file')
        # takes up all the names except the input(new), thereby dropping the row with input name
    emp = emp[employees.name != new]
    print(emp)
    emp.to_csv(open_employee, index=False)
    # The working path HAVE to be the Final_Project Path or it won't write to the right file!!!

# Delete employees from a file
def delete_fromFile():
    try:
        new = input("Please enter the full path of the file:\n")
    # checking for errors:
    except ValueError:
        print("You must enter the FULL path")
    # The file Must be w\o any blank lines!!
    employees = pd.read_csv(open_employee, index_col=False)
    print(employees)
    # reads the file to delete without the legends row
    del_file = pd.read_csv(new, index_col=False)
    print(del_file)

    # Check if all the data of all employees is supplied
    # It returns True if all elements within a series or along a Dataframe axis are non-zero, not-empty or not-False.טע==
    print(del_file.isna().any().any())
    if del_file.isna().any().any() == True:  
        print('The data in the file is not full. please fill the data and try again')
        delete_fromFile()
    else:
        print('All data is filled')
        
    # include rows present in First DataFrame and Not in Second DataFrame
    new_emp = employees[~employees.name.isin(del_file.name)]
    print(new_emp)

    new_emp.to_csv('D:\\Python\\employeesTest1.csv', index=False)
    new_emp.to_csv(open_employee, index=False)