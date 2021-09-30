
# Plotting exercises from easy to hard
# https://www.w3resource.com/graphics/matplotlib/basic/index.php#EDITOR

'''
Write a Python program to draw a line using given axis values taken from a text file, 
with suitable label in the x axis, y axis and a title.
Test Data:
test.txt
1 2
2 4
3 1
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# open text file to read data:
with open('D:\Python\MATPLOTLIBexcercises\test.txt') as f:
    data = f.read()    # read the file to variable
data = data.split('\n')    # Return a list of the words in the string, using sep as the delimiter string
x = [float(row.split(' ')[0]) for row in data] # מכניס  כל מספר שנמצא במקום 0 בכל שורה לאיקס
y = [float(row.split(' ')[1]) for row in data]
plt.plot(x,y)
plt.xlabel('x-axis')    # Set the x axis label of the current axis.
plt.ylabel('y-axis')    # Set the y axis label of the current axis.
plt.title('Sample graph!')
plt.show()              # Display a figure.

#------------------------------------------------------
#Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016. Go to the editor
#Sample Financial data (fdata.csv)

# open the file with pandas and deliver with dates
data = pd.read_csv('fdata.csv', sep=',', index_col=0, parse_dates=True)
                          
# finds all the rows that contains the the dates we want
# specific_dates = data[(data.date>= 10/3/16) & (data.date <= 10/7/16)] TODO doesn't work
data.plot()
plt.show()

#----------------------------------------------------
#Write a Python program to plot two or more lines on same plot with suitable legends of each line, 
# different colors, width and styles

# using the variable ax1 for single axes


x = [10, 20, 30]
yA = [20, 40, 10]

yB = [40, 10, 30]    # the y numbers




plt.plot(x,yA, 'b--',  x,yB, 'c' )    # Set a title of the current axes.
plt.legend(['line-1-width-1', 'line-2-width-5'])                                 # show a legend on the plot
plt.show()                                  # Display a figure.

# ---------------------------------------------------------------------------
#Write a Python program to display the current axis limits values and set new axis values

x = range(1, 50)
y = [num * 2.5 for num in x]
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
# shows the current axis limits values
print(plt.axis())
# set new axes limits
# Limit of x axis 0 to 100
# Limit of y axis 0 to 200
plt.axis([0, 100, 0, 200])
plt.show()

# ----------------------------------------------
#Write a Python program to plot quantities which have an x and y position.

x1 = [2, 3, 5, 6, 8]
y1 = [1, 5, 10, 18, 20]

x2 = [3, 4, 6, 7, 9]
y2 = [2, 5, 11, 20, 22]

plt.plot(x1, y1, 'b*', x2, y2, 'ro') # only color and marker
plt.show()

#------------------------------------------------------
#Write a Python program to plot several lines with different format styles in one command using arrays

x = np.arange(0., 5., 0.2)

# Turn on the minor TICKS, which are required for the minor GRID
plt.minorticks_on()
# add the major grid
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.plot(x,x, 'g--', x, x**2, 'bs', x, x**3, 'r^')    # Three lines!!!
plt.show()

#  Creating multiple subplots using plt.subplots
# ==========================================================

#pyplot.subplots creates a figure and a grid of subplots with a single call, while providing reasonable control over how the individual plots are created. 
#For more advanced use cases you can use GridSpec for a more general subplot layout 
#or Figure.add_subplot for adding subplots at arbitrary locations within the figure.

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
# subplots() without arguments returns a Figure and a single Axes.
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')
ax.show()

#                  Customizing Location of Subplot    using grid
#                  ----------------------------------------------------------
#     subplot2grid(shape, loc, rowspan=1, colspan=1, fig=None, **kwargs)
#       shape = Number of rows and of columns of the grid in which to place axis.
fig = plt.figure(figsize=(2, 3))   # can write only plt.figure()

ax1 = plt.subplot2grid((2,3), (0,0), colspan=3)
plt.xticks(()), plt.yticks(())          # Not showing any ticks for ax1

ax2 = plt.subplot2grid((2,3), (1,0))
plt.xticks(()), plt.yticks(())

ax3 = plt.subplot2grid((2,3), (1,1))
plt.xticks(()), plt.yticks(())

ax4 = plt.subplot2grid((2,3), (1,2))
plt.xticks(()), plt.yticks(())

# axis_all = [ax1, ax2, ax3, ax4]

plt.show()