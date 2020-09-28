import pandas as pd
from pathlib import Path
import functions_emp
import Attendance_report_function
'''
project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'

# attendance_log = pd.read_csv('Attendance_log.csv')

# The file Must be w\o any blank lines!!
check_emp = pd.read_csv(open_employee, index_col=False)
print(check_emp)
# Index(['employee_id', 'name', 'phone', 'age'], dtype='object')
print(check_emp.columns)
'''
# Users' input
stop = False
while not stop:
    # def user_choice():
    choice = input("Hi! What would you like to do today:\n \
            (1) Add employee manually; \n \
            (2) add employee from file;\n \
            (3) Delete employee manually;\n \
            (4) Delete employees from file\n \
            (5) Create attendance report\n \
            (6) Exit\n")
    if choice == "1":
        functions_emp.add_employee()
    elif choice == "2":
        functions_emp.add_e_fromFile()
    elif choice == "3":
        functions_emp.delete_employee()
    elif choice == "4":
        functions_emp.delete_fromFile()
    elif choice == "5":
        Attendance_report_function.attendance()
    elif choice == "6":
        print("Good Bye!")
        stop == True
        break
    else:
        print("I can't understand your choice. Try again!")

