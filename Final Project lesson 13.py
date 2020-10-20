import pandas as pd
from pathlib import Path
import functions_emp
import Attendance_report_function
import tkinter as tk
from PIL import ImageTk, Image


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

'''
# Creating a frame widget
frame =tk.Frame(root, bg='green', bd=5) # bd=border margins
# PLACE-This geometry manager organizes widgets by placing them in a specific position in the parent widget.
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=1, anchor='n')  
# relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.
# Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.
'''
main_label = tk.Label(root, text="Hi! What would you like to do today?", anchor='n', bg="yellow", padx=10, pady=10)
main_label.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)
add_button1 = tk.Button(root, text='Add employee manually',
                        command=functions_emp.add_employee, bg='pink')
add_button2 = tk.Button(root, text='Add employee from file',
                        command=functions_emp.add_e_fromFile, bg='pink')
del_button3 = tk.Button(root, text='Delete employee manually',
                        command=functions_emp.delete_employee, bg='pink')
del_button4 = tk.Button(root, text='Delete employees from file',
                        command=functions_emp.delete_fromFile, bg='pink')
hrReports_button = tk.Button(
    root, text="HR reports", command=Attendance_report_function.attendance, bg="#F66EF0")
mark_button = tk.Button(root, text="Mark Attendance",
                        command=Attendance_report_function.mark_attendance, bg="#F66EF0")
exit_button = tk.Button(root, text='Exit', command=exit,
                        font="Arial 18", bg='#C233FF')

#entry_place = tk.Entry(root, width=50)


add_button1.place(relx=0.04, rely=0.5, relwidth=0.2, relheight=0.1)
add_button2.place(relx=0.28, rely=0.5, relwidth=0.2, relheight=0.1)
del_button3.place(relx=0.52, rely=0.5, relwidth=0.2, relheight=0.1)
del_button4.place(relx=0.76, rely=0.5, relwidth=0.2, relheight=0.1)
hrReports_button.place(relx=0.10, rely=0.7, relwidth=0.2, relheight=0.1)
mark_button.place(relx=0.40, rely=0.7, relwidth=0.2, relheight=0.1)
exit_button.place(relx=0.76, rely=0.7, relwidth=0.2, relheight=0.1)
#entry_place.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)


def exit():
    print("Good Bye!")
    #stop == True


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
'''
root.mainloop()
