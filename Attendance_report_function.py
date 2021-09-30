import pandas as pd
import datetime
from pathlib import Path
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk, filedialog, messagebox, simpledialog


project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'
Attendance_log = project_folder / 'attendance_log.csv'

# create a class for window with treeview
class Make_window():

    def __init__(self):
# Set up the window
        self.new_win = tk.Toplevel(bg='gray')
        self.new_win.geometry("1000x500")
        
    # Frame for TreeView (for csv file)
        self.frame1 = tk.LabelFrame(self.new_win, text="File", bg="purple")
        self.frame1.place(relx=0.1, relheight=0.6, relwidth=0.8)

        # Treeview Widget
        self.tv1 = ttk.Treeview(self.frame1)
        # set the height and width of the widget to 100% of its container (frame1).
        self.tv1.place(relheight=1, relwidth=1)
        # scrollbars
        # command means update the yaxis view of the widget
        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tv1.yview)
        # command means update the xaxis view of the widget
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal", command=self.tv1.xview)
        # assign the scrollbars to the Treeview Widget
        self.tv1.configure(xscrollcommand=self.treescrollx.set,
                    yscrollcommand=self.treescrolly.set)
        # make the scrollbar fill the x axis of the Treeview widget
        self.treescrollx.pack(side="bottom", fill="x")
        # make the scrollbar fill the y axis of the Treeview widget
        self.treescrolly.pack(side="right", fill="y")
    
    def file_to_treeview(self, my_file):
    #TODO: how to insert the file you want for each function
        self.my_file = my_file
        self.tv1["column"] = list(self.my_file.columns)  # writing columns headings
        self.tv1["show"] = "headings"   # Display the heading row
        for column in self.tv1["columns"]:
            # let the column heading = column name
            self.tv1.heading(column, text=column)

        self.df_rows = self.my_file.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in self.df_rows:
            # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
            self.tv1.insert("", "end", values=row)

#----------------------------Late Employee (over 9:30)
def late_employee():
    # open attendance file
    attendance_file = pd.read_csv(Attendance_log, index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True)
    attendance_file = attendance_file.drop_duplicates()  # delete duplicates
    print(attendance_file.head())
    print(attendance_file.columns)
    
    attendance_file = attendance_file.employee_id.astype(int)         # change ID to be integers
    attendance_file.astype({'time': 'datetime'})           # TODO: Fix the error
    #attendance_file.time.astype(datetime)                               # # change column type to time type            
    #attendance_file.time = pd.to_datetime(attendance_file.time).dt.time # change object to time type
    # finds time>9:30
    late = attendance_file[attendance_file.time > datetime.time(9,30,0)]
    if late.empty:
        print('No employees in this search')
    # TODO: show sorted by name in Treeview
    late_file = late.sort_values(by=['name'], ascending=False)
    Make_window()   # call the class ! -> Creates the new window nicely!
    Make_window.file_to_treeview(late_file)
    

    



def mark_attendance():
    # Creating a frame widget
    
    new = simpledialog.askinteger("input", "Please enter your ID")
    if new is None:
        messagebox.showerror("You must enter only ID number")
    # open the main employee file
    employees_main = pd.read_csv(open_employee, index_col=False,
                                 skipinitialspace=True, skip_blank_lines=True)

    emp = employees_main.drop_duplicates()  # deletes any duplicates in file
    
    # open attendance file
    attendance_file = pd.read_csv(Attendance_log, index_col=False,
                                  skipinitialspace=True, skip_blank_lines=True)
    attendance_file = attendance_file.drop_duplicates()    # deletes any duplicates in file
    
    if new not in attendance_file['employee_id'].values:
        if new not in emp['employee_id'].values:
            messagebox.showwarning("ERROR!", "No such employee in the employee main file")
            

    else:
        now_time = datetime.datetime.now()
        entering_time = now_time.replace(microsecond=0)    # deleting the microseconds
        # print in the format I want
        mark_time= 'Entering time is: ' + entering_time.strftime("%d/%m/%Y %H:%M")
        #messagebox.showinfo('Mark attendance', mark_time)
        print('Mark attendance', mark_time)
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
    attendance_file = pd.read_csv(Attendance_log, index_col=False,
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