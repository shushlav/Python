import pandas
import numpy


employee_file = pandas.DataFrame(columns = ["employee_id", "name", "phone", "age"])
employee_file.to_csv("employee_file.csv") # saves the file  

attendance_log = pandas.DataFrame(columns = ["employee_id", "name", "date", "time"])
attendance_log.to_csv("attendance_log.csv") 

print(employee_file)
print(employee_file.index)
print(attendance_log)