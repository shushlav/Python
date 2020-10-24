from tkinter import *
import tkinter as tk


addEmployee = Toplevel()
# define all the variables for each gui component


# Row 0 - Headings
lblHeading = tk.Label(addEmployee, text="New employee",
                      font=('Arial', 24, 'bold'))
lblHeading.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

# Row 1 - ID and entry
lblID = tk.Label(addEmployee, text="ID number", font=('Arial', 14, 'bold'))
lblID.grid(row=1, column=0)

# Row 2 - Name and entry
lblName = tk.Label(addEmployee, text="Name", font=('Arial', 14, 'bold'))
lblName.grid(row=2, column=0)


# Row 3 - Phone and entry
lblPhone = tk.Label(addEmployee, text="Phone no.",
                    font=('Arial', 14, 'bold'))
lblPhone.grid(row=3, column=0)

# Row 4 - Age and entry
lblAge = tk.Label(addEmployee, text="Age", font=('Arial', 14, 'bold'))
lblAge.grid(row=4, column=0)


# Row 5 -buttons
submit_button = tk.Button(addEmployee, text="Save")
submit_button.grid(row=5, column=0, sticky=E, padx=20, pady=10)

addEmployee.mainloop()
