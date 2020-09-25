import pandas as pd
import datetime
from pathlib import Path
 


project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'

# attendance_log = pd.read_csv('Attendance_log.csv')

# The file Must be w\o any blank lines!!
check_emp = pd.read_csv(open_employee, index_col='employee_id')
print(check_emp)




def attendance():
    chosen = input ("What kind of report?\n \
                    (1) report by employee's ID\n \
                    (2) report by month \n \
                    (3) report of late employee (according to the time)\n \
                    (4) Mark attendance \n \
                    (5) Exit \n \
                    ")

    if chosen == '1':
        emp_attendance_log()
    if chosen == '2':
        month_log()
    if chosen == '3':
        pass
    if chosen == '4':
        pass
    if chosen == '5':
        pass   
    
def emp_attendance_log():    
    # open the main employee file
    employees_main = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    
    emp = employees_main.drop_duplicates()  # deletes any duplicates in file
    print(emp)
    # open attendance file
    Attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    try:
        new = int(input("Please enter the ID of the employee for attendance log:\n"))
    # checking for errors:
    except ValueError:
        print("You must enter only ID number")
    if new not in emp['employee_id']:
        print('No such employee in the employee main file')
    if new not in Attendance_file['employee_id']:
        print('No such employee in the attendance log file')
    # finds all the rows that contains the ID given (new)
    per_name = Attendance_file[Attendance_file.employee_id == new]
    print(per_name)


def month_log():    
    
    # open attendance file
    Attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    try:
        new = input("Please enter the month (a number) for attendance log:\n")
    # checking for errors:
    except ValueError:
        print("You must enter only the number of the month")
    # convert the time column to datetime:
    Attendance_file['date'] = pd.to_datetime(Attendance_file['date'], format="%d/%m/%Y")
    print(Attendance_file['date'].type)
# Check that the month has information
    if new not in Attendance_file['date'].dt.month:
        print('The month has no log')
    
    # finds all the rows that contains the name given (new)
    per_month = Attendance_file[Attendance_file['date'].dt.month == new]
    print(per_month)
    
    
    
    
    # The working path HAVE to be the Final_Project Path or it won't write to the right file!!!
