import pandas as pd
from pathlib import Path
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk, filedialog, messagebox, simpledialog
#from pandastable import Table
#from tksheet import *


project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'
'''
# creating a class
class Employees():
    employee_type = "juniors" # every instance will get this type unless I change a specific instance

    def __init__(self):
        self.name = name 
        self.id = id
        self.age = age
        self.phone = ""
'''        

# creating a class for the window with the list of employees
class nWin():
    def __init__(self):
        # Set up the window
        self.delEmployee = tk.Toplevel(bg='green')
        self.delEmployee.geometry("1000x500")

        # Frame for TreeView (for csv file)
        self.frame1 = tk.LabelFrame(delEmployee, text="Employees File", bg="yellow")
        frame1.place(relx=0.1, relheight=0.6, relwidth=0.8)

        # Treeview Widget
        tv1 = ttk.Treeview(frame1)
        # set the height and width of the widget to 100% of its container (frame1).
        tv1.place(relheight=1, relwidth=1)
        # scrollbars
        # command means update the yaxis view of the widget
        treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
        # command means update the xaxis view of the widget
        treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
        # assign the scrollbars to the Treeview Widget
        tv1.configure(xscrollcommand=treescrollx.set,
                    yscrollcommand=treescrolly.set)
        # make the scrollbar fill the x axis of the Treeview widget
        treescrollx.pack(side="bottom", fill="x")
        # make the scrollbar fill the y axis of the Treeview widget
        treescrolly.pack(side="right", fill="y")

        tv1["column"] = list(emp.columns)  # writing columns headings
        tv1["show"] = "headings"   # Display the heading row
        for column in tv1["columns"]:
            # let the column heading = column name
            tv1.heading(column, text=column)

        df_rows = emp.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
            tv1.insert("", "end", values=row)

        # Frame for open file dialog
        file_frame1 = tk.LabelFrame(delEmployee, bg="pink")
        file_frame1.place(relx=0.1, rely=0.7, relheight=0.15, relwidth=0.8)

        # Set up delete label & entry
        delName = tk.Label(file_frame1, text="Select the name you want to delete and press delete", font=(
            'Arial', 14, 'bold'), bg='pink')  # (file_frame1, text="Name to delete: ", font=('Arial', 14, 'bold'), relief=RAISED)
        delName.place(relx=0.1, rely=0.3, relwidth=0.8)

        # Set up the buttons
        delete_button = tk.Button(delEmployee, text="Delete",
                                command=delete, relief=tk.RAISED)  # TODO: add command
        delete_button.place(relx=0.2, rely=0.9)
        cancel_button = tk.Button(
            delEmployee, text="Cancel", command=quit, relief=tk.RAISED)
        cancel_button.place(relx=0.7, rely=0.9)

        delEmployee.mainloop()



# ---------------------Add employee manually--------------WORKING!!
def add_employee():

    def save_employee():
        # gather all the info from the screen
        anew_id = new_id.get()
        anew_name = new_name.get()
        anew_phone = new_phone.get()
        anew_age = new_age.get()
        errors = 0
        
            
    # error checking: TODO: add more errors for phone and age and don't close the window
    # blank entry
            
        if anew_id == '' or anew_name == '' or anew_phone == '' or anew_age == '':
            messagebox.showerror(
                'Error', "Some of the information is not full", parent=addEmployee)  # parent= keeps the frame open!
            
        if not anew_name.isalpha():
            messagebox.showerror(
                'Name Error', "You must enter only letters in 'Name'", parent=addEmployee)

        if len(anew_age) != 2:  # TODO - stop and return to age entry
            messagebox.showerror(
                'Age Error', "You must enter only 2 numbers for age", parent=addEmployee)
        
        else:
            result = messagebox.askquestion(
                "Save", "Do you want to save the data to the file?", parent=addEmployee)

            if result == 'yes':
                
                addEmployee.destroy()    # destroys the window
                # open the file 
                employees = pd.read_csv(open_employee, index_col=False,
                                        skipinitialspace=True, skip_blank_lines=True)
                # Pass the info to DataFrame’s constructor to create a dataframe object
                info_df = pd.DataFrame({'employee_id': [anew_id], 'name': [
                    anew_name], 'phone': [anew_phone], 'age': [anew_age]})

                # appends the info_df to the employees file w\o new index
                employees = pd.concat([employees, info_df], ignore_index=True)
                employees = employees.drop_duplicates()  # deletes any duplicates in file
                print(employees)
                employees.to_csv(open_employee, index=False)
                messagebox.showinfo("New Employee", "New employee added!")
                
                # show the employees list in GUI:
                employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
                emp = employees.drop_duplicates()  # deletes any duplicates in file
                selected = tv1.selection()
                # Create a list of the selected row! WORKS!!
                # creates a nested list TODO: why nested?
                name_List = [tv1.item(x)['values'] for x in selected]
                print(name_List)


    
                # addEmployee.mainloop()
            else:
                new_id.set('')
                new_name.set('')
                new_phone.set('')
                new_age.set('')

    # Set up the frame
    addEmployee = tk.Toplevel(bg='light grey')

    # define all the variables for each gui component
    new_id = tk.StringVar()
    new_name = tk.StringVar()
    new_phone = tk.StringVar()
    new_age = tk.StringVar()

    # Row 0 - Headings
    lblHeading = tk.Label(addEmployee, text="New employee",
                          font=('Arial', 24, 'bold'))
    lblHeading.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    # Row 1 - ID and entry
    lblID = tk.Label(addEmployee, text="ID number", font=(
        'Arial', 14, 'bold'), width=12, relief=tk.RIDGE)
    lblID.grid(row=1, column=0, padx=20)
    entryID = tk.Entry(addEmployee, textvariable=new_id, width=12)
    entryID.grid(row=1, column=1, padx=20)

    # Row 2 - Name and entry
    lblName = tk.Label(addEmployee, text="Name", font=(
        'Arial', 14, 'bold'), width=12, relief=tk.RIDGE)
    lblName.grid(row=2, column=0)
    entryName = tk.Entry(addEmployee, textvariable=new_name, width=12)
    entryName.grid(row=2, column=1)

    # Row 3 - Phone and entry
    lblPhone = tk.Label(addEmployee, text="Phone no.", font=(
        'Arial', 14, 'bold'), width=12, relief=tk.RIDGE)
    lblPhone.grid(row=3, column=0, padx=20)
    entryPhone = tk.Entry(addEmployee, textvariable=new_phone, width=12,)
    entryPhone.grid(row=3, column=1)

    # Row 4 - Age and entry
    lblAge = tk.Label(addEmployee, text="Age", font=(
        'Arial', 14, 'bold'), width=12, relief=tk.RIDGE)
    lblAge.grid(row=4, column=0, padx=20, sticky=tk.W)
    entryAge = tk.Entry(addEmployee, textvariable=new_age,
                        width=12, relief=tk.SUNKEN)
    entryAge.grid(row=4, column=1)

    # Row 5 -buttons
    # command=save_employee,
    submit_button = tk.Button(addEmployee, text="Save",
                              command=save_employee, width=10)
    submit_button.grid(row=5, column=0, padx=10, pady=10)
    cancel_button = tk.Button(addEmployee, text="Cancel",
                              command=addEmployee.destroy, width=10)  # destroys the window
    cancel_button.grid(row=5, column=1, sticky='E', padx=20, pady=10)

    addEmployee.mainloop()


# ++++++++++++++++++++++++++ Add from file +++++++++++++++++++++

def add_e_fromFile():
    new = filedialog.askopenfilename()
    #open the original file
    employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    # The file Must be w\o any blank lines!!
    # open the file to be added:
    add_file = pd.read_csv(new, index_col=False, skipinitialspace=True,
                           skip_blank_lines=True)  # reads the file to be added
    
    # Check if all the data of all employees is supplied
    # It returns True if all elements within a series or along a Dataframe axis are non-zero, not-empty or not-False.טע==
    print(add_file.isna().any().any())
    if add_file.isna().any().any() == True:
        print('The data in the file is not full. please fill the data and try again')
        #  delete_fromFile()  ?????
    else:
        print('All data is filled')

    # Check for duplicates between files:
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
    messagebox.showinfo(
                "Add File", "The new file was added to the employees file")

# ------------------------Delete employee manually - WORKING!
def delete_employee():
    employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    emp = employees.drop_duplicates()  # deletes any duplicates in file
    

    def delete():
        selected = tv1.selection()
        # Create a list of the selected row! WORKS!!
        # creates a nested list TODO: why nested?
        name_List = [tv1.item(x)['values'] for x in selected]
        print(name_List)
        delName = name_List[0][1]  # stores the name of the emp
        confirmtxt = "Are you sure you want to delete the marked employee?"
        if messagebox.askokcancel("Delete", confirmtxt, default="ok", icon="warning", parent=delEmployee):
            print(delName)
            # delete name from treeview:
            d = tv1.selection()[0]  # use the raw selected
            tv1.delete(d)

            # takes up all the names except the input(new), thereby dropping the row with input name
            emp1 = employees[employees.name != delName]
            print(emp1)
            emp1.to_csv(open_employee, index=False)
            # The working path HAVE to be the Final_Project Path or it won't write to the right file!!!
            messagebox.showinfo(
                "Delete", "Employee Deleted", parent=delEmployee)
    def quit():
        delEmployee.destroy()

    # Set up the window     TODO: make it a function or a class to show the list
    delEmployee = tk.Toplevel(bg='green')
    delEmployee.geometry("1000x500")

    # Frame for TreeView (for csv file)
    frame1 = tk.LabelFrame(delEmployee, text="Employees File", bg="yellow")
    frame1.place(relx=0.1, relheight=0.6, relwidth=0.8)

    # Treeview Widget
    tv1 = ttk.Treeview(frame1)
    # set the height and width of the widget to 100% of its container (frame1).
    tv1.place(relheight=1, relwidth=1)
    # scrollbars
    # command means update the yaxis view of the widget
    treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
    # command means update the xaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
    # assign the scrollbars to the Treeview Widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)
    # make the scrollbar fill the x axis of the Treeview widget
    treescrollx.pack(side="bottom", fill="x")
    # make the scrollbar fill the y axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")

    tv1["column"] = list(emp.columns)  # writing columns headings
    tv1["show"] = "headings"   # Display the heading row
    for column in tv1["columns"]:
        # let the column heading = column name
        tv1.heading(column, text=column)

    df_rows = emp.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        tv1.insert("", "end", values=row)

    # Frame for open file dialog
    file_frame1 = tk.LabelFrame(delEmployee, bg="pink")
    file_frame1.place(relx=0.1, rely=0.7, relheight=0.15, relwidth=0.8)

    # Set up delete label & entry
    delName = tk.Label(file_frame1, text="Select the name you want to delete and press delete", font=(
        'Arial', 14, 'bold'), bg='pink')  # (file_frame1, text="Name to delete: ", font=('Arial', 14, 'bold'), relief=RAISED)
    delName.place(relx=0.1, rely=0.3, relwidth=0.8)

    # Set up the buttons
    delete_button = tk.Button(delEmployee, text="Delete",
                              command=delete, relief=tk.RAISED)  # TODO: add command
    delete_button.place(relx=0.2, rely=0.9)
    cancel_button = tk.Button(
        delEmployee, text="Cancel", command=quit, relief=tk.RAISED)
    cancel_button.place(relx=0.7, rely=0.9)

    delEmployee.mainloop()


# ------------------------Delete employee from file

def delete_fromFile():
    # open GUI to open file path
    new = filedialog.askopenfilename()
    # open th eemployee file
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
    messagebox.showinfo('Delete from File', "Employees from file were deleted!")


    # *********************** function to open a file ************************
    
    def read_Employee():
        employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
        emp = employees.drop_duplicates()  # deletes any duplicates in file 