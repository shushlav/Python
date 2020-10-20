import pandas as pd
import datetime
from pathlib import Path
import tkinter as tk



project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'

# attendance_log = pd.read_csv('Attendance_log.csv')
'''
# The file Must be w\o any blank lines!!
check_emp = pd.read_csv(open_employee, index_col='employee_id')
print(check_emp)
'''

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
    # print sorted by name
    print(late.sort_values(by=['name'], ascending=False))



def mark_attendance():
    # Creating a frame widget
    '''
    frame = tk.Frame(root, bg='gray', bd=5) # bd=border margins
    frame.place(relx=0.42, rely=0.95, width=0.75, height=0.5)
    id_label = tk.Label(frame, text="Please enter your ID", bd=10)
    id_label.place(relx=0.52, rely=0.95)
    idEntry = tk.Entry(frame, bg='grey')
    idEntry.place(relx=0.72, rely=0.95)
    '''
    new = simpledialog.askinteger("input", "Please enter your ID", parent = root)
    # open the main employee file
    employees_main = pd.read_csv(open_employee, index_col=False,
                                 skipinitialspace=True, skip_blank_lines=True)

    emp = employees_main.drop_duplicates()  # deletes any duplicates in file
    
    # open attendance file
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True)
    attendance_file = attendance_file.drop_duplicates()
    '''
    try:
        new = answer    
    # checking for errors:
    except ValueError:
        print("You must enter only ID number")
    '''
    if new not in attendance_file['employee_id'].values:
        if new not in emp['employee_id'].values:
            print('No such employee in the employee main file')

    else:
        now_time = datetime.datetime.now()
        entering_time = now_time.replace(microsecond=0)    # deleting the microseconds
        # print in the format I want
        print('Entering time is: ', entering_time.strftime("%d/%m/%Y %H:%M"))
        # create a new dataframe
        new_record = pd.DataFrame({'employee_id': new, 'name': emp[emp.employee_id == new].name,
                                'date': entering_time.date().strftime("%d/%m/%Y"), 'time': entering_time.time() })
        # emp[emp.employee_id == new].name  finds the row that contains the ID given (new)
        # strftime("%d/%m/%Y") = format the date to dd/mm/yyyy
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
                    (5) report of given date range\n \
                    (6) Exit \n \
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
        date_range()   
    if chosen == '6':
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
    global new
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True)
    try:
        new = int(input("Please enter the month (a number) for attendance log:\n"))
    # checking for errors:
    except ValueError:
        print("You must enter only the number of the month")
    print(attendance_file['date'].dtype)
    # convert the date column to datetime:
    attendance_file['date'] = pd.to_datetime(attendance_file['date'], format='%d/%m/%Y')
    # Check that the month has information
    if new not in attendance_file['date'].dt.month:
        print('The month has no log')
    else:
        # finds all the rows that contains the name given (new)
        per_month = attendance_file[attendance_file.date.dt.month == new]
        print(per_month)
    
def date_range():
    # indicate which columns are dates:
    dateparse = lambda x: datetime.datetime.strptime(x, '%d/%m/%Y') # changes all dates to the same format!!!
    dateCol = ['date']
    attendance_file = pd.read_csv('attendance_log.csv', index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True, parse_dates=dateCol, date_parser=dateparse)
    
    try:
        starting_date = input("Please enter the starting date (dd/mm/yyyy) for attendance log:\n")
        starting_datetime = datetime.datetime.strptime(starting_date, "%d/%m/%Y") # parsing string as time
        ending_date = input("Please enter the ending date (dd/mm/yyyy) for attendance log:\n")
        ending_datetime = datetime.datetime.strptime(ending_date, "%d/%m/%Y")
    # checking for errors:
    except ValueError:
        print("The value entered does not match format '%d/%m/%Y")
        date_range() 
    
    
    # convert the date column to datetime with DAY FIRST: 
    attendance_file['date'] = pd.to_datetime(attendance_file['date'], dayfirst=True, format='%d/%m/%Y')
    
    # select rows based on loc
    result = attendance_file.loc[(attendance_file['date'] >= starting_datetime) & (attendance_file['date'] <= ending_datetime)]
    print(result.sort_values(by=['date'], ascending=False))


    # The working path HAVE to be the Final_Project Path or it won't write to the right file!!!