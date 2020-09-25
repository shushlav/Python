import csv
from pathlib import Path

project_folder = Path("D:\\Documents\\יעל\\Python\\Final_project\\")
open_employee = project_folder/'employees.csv' 

#     attendance_log = pandas.read_csv('Attendance_log.csv')

def add_employee():

    try:
        new = input("Please write: Employee_ID, Name, Phone, Age (using commas as separators):\n")
    #checking for errors:
    except ValueError:
        print("You must enter all the data mentioned with commas")    
    #Separate on comma.
    info = new.split(",") # separate every string between ","
    print("info:", info)    
              
    # Open file in append mode
    with open(open_employee, 'a') as csv_file:
        # Create a writer object from csv module
        csv_writer = csv.writer(csv_file)
        # Add contents of list as last row in the csv file       
        csv_writer.writerow(info)
        
def delete_employee():
    emp_name = input("Please enter the employee's name to delete:\n")
    with open(open_employee, 'r') as csv_file:
        reader = csv.reader(csv_file, skipinitialspace=True)  # inserts the file in a data list
        # skipinitialspace = When True, whitespace immediately following the delimiter is ignored. The default is False.
        reader = list(reader)  # Transforms to list
        for row in reader:
            if emp_name == row[1]:
                print(row[1], "was deleted from file")
                reader.remove(row)
                break
        
    with open(open_employee, 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator = '\n')
        writer.writerows(reader)

# Add employees from a file
def add_e_fromFile():
    pass
    
# Delete employees from a file

def delete_fromFile():
    try:
        new_file = input("Please enter the the file FULL path and name:\n")
    #checking for errors:
    except ValueError:
        print("You must enter full path and file name")
    with open(new_file, 'r') as delete_file, \
         open(open_employee, 'r') as csv_file:
        # nf_reader = csv.reader(copy_file, skipinitialspace=True) #csv.reader is the object which iterates over the lines of the CSV file
        # mainFile = csv.DictReader(csv_file, skipinitialspace=True) # removes initial spaces 
        # mainFile = list(mainFile)   # inserts the file in a data list
        nf_reader = delete_file.readlines()
        print(nf_reader)
        #next(nf_reader)   # will retrieve the first row of the iterator then discard it

        mainFile = csv_file.readlines()
        final_list = [['Employee_ID', 'Name', 'Phone', 'Age']]
        #csv_writer = csv.writer(csv_file, lineterminator = '\n')
        
        
        for row in nf_reader: #the line from source is stored in ‘row’ variable, which is a list
            if row not in mainFile:
                final_list.append(row)    
                    
        for line in mainFile:
            if line not in nf_reader:        
                final_list.append(line)
        
        print("final list:", final_list)
            # what if a name in the delete list doesn't exist in the employee?    
                    
            
    # writing the editted list to the main file
    with open(open_employee, 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator = '\n')
        writer.writerows(final_list)    
        print("The employees from the file were deleted")
    

# Users' input
# def user_choice():
choice = input("Hi! What would you like to do today:\n \
        (1) Add employee manually \n\
        (2) add employee from file;\n \
        (3) Delete employee manually;\n \
        (4) Delete employees from file\n \
        (5) Exit\n")
if choice == "1":
    add_employee()
elif choice == "2":
    add_e_fromFile()
elif choice == "3":
    delete_employee()
elif choice == "4":
    delete_fromFile()
elif choice == "5":
    print("Good Bye!")
else:
    print("I can't understand your choice. Good bye!")