# working_with_excel_files
#https://www.datacamp.com/community/tutorials/python-excel-tutorial

# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'D:\Python\pandas\student_data2.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)       #['student_data2', 'new', 'numbers']
data = xl.sheet_names

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('new', index_col=0)
print(df1)

# Convert Sheet to DataFrame
#df2 = pd.DataFrame(xl.new)
#print(df2)