import pandas as pd
from pathlib import Path
import functions_emp
import Attendance_report_function
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

'''
Error
_tkinter.TclError: image "pyimage1" doesn't exist
creating more than once instance of Tk. 
Tkinter is designed such that there should only ever be exactly once instance of Tk
the rest need to be instances of Toplevel
'''
HEIGHT = 700  # size of canvas
WIDTH = 1500
root = tk.Tk()   # creates the root window
root.title("Employee Manager")   # The label of the window

# The size of the app (the canvas)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# pack- This geometry manager organizes widgets in blocks before placing them in the parent widget.


# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
path = "D:\\Python\\Reka55.gif"
img = ImageTk.PhotoImage(Image.open(path))
background_label = tk.Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

# Main Label
main_label = tk.Label(root, text="Hi! What would you like to do today?", font="bold", anchor='n', bg="#CFF8F9", padx=10, pady=10)
main_label.place(relx=0.2, rely=0.05, relwidth=0.5, relheight=0.1)
## Add\Delete employee 
HR_files = tk.LabelFrame(root, text="HR Employee Files", padx=5, pady=5, bg="#09C7F9")
HR_files.place(relx=0.6, rely=0.3, relwidth=0.4, relheight=0.5)

add_button1 = tk.Button(HR_files, text='Add employee manually',
                        command=functions_emp.add_employee, bg='#A6E7F8')
add_button2 = tk.Button(HR_files, text='Add employee from file',
                        command=functions_emp.add_e_fromFile, bg='#A6E7F8')
del_button3 = tk.Button(HR_files, text='Delete employee manually',
                        command=functions_emp.delete_employee, bg='#A6E7F8')
del_button4 = tk.Button(HR_files, text='Delete employees from file',
                        command=functions_emp.delete_fromFile, bg='#A6E7F8')
#hrReports_button = tk.Button(
#    root, text="HR reports", command=Attendance_report_function.attendance, bg="#F66EF0")
mark_button = tk.Button(root, text="Mark Attendance",
                        command=Attendance_report_function.mark_attendance, bg="#F66EF0")
exit_button = tk.Button(root, text='Exit', command=exit,
                        font="Arial 18", bg='#C233FF')


# Add\Delete employee
HR_files.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.5)

add_button1.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.2)
add_button2.place(relx=0.01, rely=0.3, relwidth=0.98, relheight=0.2)
del_button3.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.2)
del_button4.place(relx=0.01, rely=0.7, relwidth=0.98, relheight=0.2)

mark_button.place(relx=0.10, rely=0.85, relwidth=0.2, relheight=0.1)
exit_button.place(relx=0.66, rely=0.85, relwidth=0.2, relheight=0.1)
#entry_place.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)

# Frame for HR REPORTS

HR_reports = tk.LabelFrame(root, text="HR REPORTS", padx=10, pady=10, bg="#269003")
HR_reports.place(relx=0.05, rely=0.3, relwidth=0.3, relheight=0.5)
# Labels for reports
by_id = tk.Button(HR_reports, text="report by employee's ID",
                         bg='#A5FA89')
report_by_month = tk.Button(HR_reports, text='report by month',
                        bg='#A5FA89')
late_employee = tk.Button(HR_reports, text='report of late employee',
                        bg='#A5FA89')
date_range = tk.Button(HR_reports, text='report of given date range',
                        bg='#A5FA89')

by_id.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.2)
report_by_month.place(relx=0.01, rely=0.3, relwidth=0.98, relheight=0.2)
late_employee.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.2)
date_range.place(relx=0.01, rely=0.7, relwidth=0.98, relheight=0.2)





def exit():
    print("Good Bye!")
    #stop == True



root.mainloop()
