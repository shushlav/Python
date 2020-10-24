import pandas as pd
from pathlib import Path
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from pandastable import Table 
 


project_folder = Path("D:\\Python\\")
open_employee = project_folder / 'employees.csv'

def add_employee():
    
    def save_employee():
        # gather all the info from the screen
        anew_id = new_id.get()
        anew_name = new_name.get()
        anew_phone = new_phone.get()
        anew_age = new_age.get()

        #error checking:
        #blank entry
        if anew_id == '' or anew_name == '' or anew_phone =='' or anew_age == '':
            messagebox.showerror('Error', "Some of the information is not full")
    
        elif not anew_name.isalpha():
            messagebox.showerror("You must enter only letters")
        elif len(new_age) > 2:
            messagebox.showerror("You must enter only 2 numbers for age") 

        else:
            result = messagebox.askquestion("Save", "Do you want to same the data to the file?")
            
            if result == 'yes':
                # open the file
                employees = pd.read_csv(open_employee, index_col=False,
                                skipinitialspace=True, skip_blank_lines=True)
                # Pass the info to DataFrame’s constructor to create a dataframe object
                info_df=pd.DataFrame({'employee_id': [anew_id], 'name': [
                                    anew_name], 'phone': [anew_phone], 'age': [anew_age]})

                # appends the info_df to the employees file w new index
                employees = pd.concat([employees, info_df], ignore_index=True)
                employees = employees.drop_duplicates()  # deletes any duplicates in file
                print(employees)
                employees.to_csv(open_employee, index=False)
                messagebox.showinfo("New Employee", "New employee added!") 
                addEmployee.mainloop()
            else:
                new_id.set('')
                new_name.set('')
                new_phone.set('')
                new_age.set('')

    # Set up the frame
    addEmployee = tk.Toplevel(bg='light grey')
    

    # define all the variables for each gui component
    new_id = StringVar()
    new_name = StringVar()
    new_phone = StringVar()
    new_age = StringVar()

    # Row 0 - Headings
    lblHeading = tk.Label(addEmployee, text="New employee", font=('Arial',24, 'bold'))
    lblHeading.grid(row=0, column=0, columnspan = 2, padx=20, pady=10)
    
    # Row 1 - ID and entry
    lblID = tk.Label(addEmployee, text="ID number", font=('Arial', 14, 'bold'), width= 12, relief=tk.RIDGE)
    lblID.grid(row=1, column=0)
    entryID = tk.Entry(addEmployee, textvariable=new_id, width=10)
    entryID.grid(row=1, column=1)
    
    # Row 2 - Name and entry
    lblName = tk.Label(addEmployee, text="Name", font=('Arial', 14, 'bold'), justify=LEFT, width= 12, relief=tk.RIDGE)
    lblName.grid(row=2, column=0)
    entryName = tk.Entry(addEmployee, textvariable=new_name, width=10)
    entryName.grid(row=2, column=1)
    
    # Row 3 - Phone and entry
    lblPhone = tk.Label(addEmployee, text="Phone no.", font=('Arial', 14, 'bold'), justify=LEFT, width= 12, relief=tk.RIDGE)
    lblPhone.grid(row=3, column=0)
    entryPhone = tk.Entry(addEmployee, textvariable=new_phone, width=10)
    entryPhone.grid(row=3, column=1)

    # Row 4 - Age and entry
    lblAge = tk.Label(addEmployee, text="Age", font=('Arial', 14, 'bold'), width= 12, relief=tk.RIDGE)
    lblAge.grid(row=4, column=0)
    entryAge = tk.Entry(addEmployee, textvariable=new_age, width=10, relief=tk.SUNKEN)
    entryAge.grid(row=4, column=1)

    # Row 5 -buttons
    submit_button = tk.Button(addEmployee, text="Save", justify=LEFT)  #command=save_employee,
    submit_button.grid(row=5, column=0, sticky=E, padx=20, pady=10)
    cancel_button = tk.Button(addEmployee, text="Cancel")
    cancel_button.grid(row=5, column=1, sticky=E, padx=20, pady=10)

    addEmployee.mainloop()

    
'''
    new_id = simpledialog.askinteger("input", "Please enter ID")
    if new_id is None:
        messagebox.showerror("You must enter only ID number")
    if new_id in employees.employee_id.values:
        messagebox.showerror("ID error", "This ID already exists!")
    new_name = simpledialog.askstring("input name", "Please enter the Name")
    if new_name is None:
        messagebox.showerror("You must enter only letters")
        add_employee()
    if not new_name.isalpha():
        messagebox.showerror("You must enter only letters")
        add_employee()
    new_phone = simpledialog.askinteger("input phone", "Please enter Phone number")        
    if new_phone is None:
        messagebox.showerror("You must enter only numbers")        
    new_age = simpledialog.askinteger("input age", "Please enter the age")
    if new_age is None:
        messagebox.showerror("You must enter only numbers")
    if len(str(new_age)) > 2:
        messagebox.showerror("You must enter only 2 numbers for age") 
'''
    

# +++++++++++++++++ Add from file

def add_e_fromFile():
    new = filedialog.askopenfilename()
    '''
    employees = pd.read_csv(open_employee, index_col=False,
                            skipinitialspace=True, skip_blank_lines=True)
    # The file Must be w\o any blank lines!!
    add_file = pd.read_csv(new, index_col=False, skipinitialspace=True,
                           skip_blank_lines=True)  # reads the file to be added
    '''
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
    '''
    # display the data in new window
    buttonStart_Click={
    Import-Csv -Path C:\ps-test\SAPIENMVP2015.csv `
        -Header ID, Name, City, State, Country |
    Out-GridView –Title Get-CsvData
}
    '''
    print(emp)
    new_name = simpledialog.askstring("input", "Please enter the name to DELETE")
    if new_name is None:
        return
    elif not new_name.isalpha():
        messagebox.showerror("Error", "You must enter a name")
        return
    if new_name not in employees.name.values:
        messagebox.showerror("Name error", "This NAME doesn't exist!")
        return
    else:
        confirmtxt = "Are you sure you want to delete " + new_name +"?"
        if messagebox.askokcancel("Delete", confirmtxt, default="ok", icon="warning"):
             
            # takes up all the names except the input(new), thereby dropping the row with input name
            emp = emp[employees.name != new_name]
            print(emp)
            emp.to_csv(open_employee, index=False)
            # The working path HAVE to be the Final_Project Path or it won't write to the right file!!!
            messagebox.showinfo("Delete", "Employee Deleted")
        else:
            messagebox.showinfo("Delete", "Delete employee - CANCELED!")

# ------------------------Delete employee from file        
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

