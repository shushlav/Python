import pandas as pd
import datetime
from pathlib import Path



project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'

# attendance_log = pd.read_csv('Attendance_log.csv')

# The file Must be w\o any blank lines!!
check_emp = pd.read_csv(open_employee, index_col='employee_id')
print(check_emp)

def late_employee():
    # open attendance file
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True)
    attendance_file = attendance_file.drop_duplicates()  # delete duplicates
    attendance_file.time = pd.to_datetime(attendance_file.time).dt.time # change object to time type
    # finds time>9:30
    late = attendance_file[attendance_file.time > datetime.time(9,30,0)]
    if late.empty:
        print('No employees in this search')
    print(late)



def mark_attendance():
    # open the main employee file
    employees_main = pd.read_csv(open_employee, index_col=False,
                                 skipinitialspace=True, skip_blank_lines=True)

    emp = employees_main.drop_duplicates()  # deletes any duplicates in file
    print(emp)
    # open attendance file
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True)
    attendance_file = attendance_file.drop_duplicates()
    try:
        new = int(input("Please enter the ID of the employee for attendance log:\n"))
    # checking for errors:
    except ValueError:
        print("You must enter only ID number")
    if new not in attendance_file['employee_id'].values:
        if new not in emp['employee_id'].values:
            print('No such employee in the employee main file')


    # finds all the rows that contains the ID given (new)
        else:
            now_time = datetime.datetime.now()
            entering_time = now_time.replace(microsecond=0)    # deleting the microseconds
            print('Entering time is: ', entering_time)
            # create a new dataframe
            new_record = pd.DataFrame({'employee_id': new, 'name': emp[emp.employee_id == new].name,
                                    'date': entering_time.date(), 'time': entering_time.time() })
            new_record = new_record.drop_duplicates()     # erase duplicates
            # Merge the files to a new DF
            emp_df = pd.merge(attendance_file, new_record, how='outer')
            emp_df.to_csv('D:\\Python\\attendance_log.csv', index=False, date_format='%Y-%m-%d')

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
        late_employee()
    if chosen == '4':
        mark_attendance()
    if chosen == '5':
        pass   
    
def emp_attendance_log():    
    # open the main employee file
    employees_main = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    
    emp = employees_main.drop_duplicates()  # deletes any duplicates in file
    print(emp)
    # open attendance file
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    try:
        new = int(input("Please enter the ID of the employee for attendance log:\n"))
    # checking for errors:
    except ValueError:
        print("You must enter only ID number")
    if new not in emp['employee_id'].values:              # it doesn't work!!! read how to
        print('No such employee in the employee main file')
    if new not in attendance_file['employee_id'].values:
        print('No such employee in the attendance log file')
    # finds all the rows that contains the ID given (new)
    else:
        per_name = attendance_file[attendance_file.employee_id == new]
        print(per_name)


def month_log():    
    
    # open attendance file
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    try:
        new = int(input("Please enter the month (a number) for attendance log:\n"))
    # checking for errors:
    except ValueError:
        print("You must enter only the number of the month")
    # convert the time column to datetime:
    attendance_file['date'] = pd.to_datetime(attendance_file['date'], format="%d/%m/%Y")
    print(attendance_file.date.dt.month)
    # Check that the month has information
    if new not in attendance_file.date.dt.month:
        print('The month has no log')
    
    # finds all the rows that contains the name given (new)
    per_month = attendance_file[attendance_file.date.dt.month == new]
    print(per_month)
    
    
    
    
    # The working path HAVE to be the Final_Project Path or it won't write to the right file!!!
