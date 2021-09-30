#@@@@@@@@@@@@@@@   Matplotlib   @@@@@@@@@@@@@@@@@@@@@
#------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.plot([1,2,3],[5,7,4])    # x,y

plt.show()   #מציג את הגרף בחלון נפרד

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]   # population in billions

plt.plot(year, pop)    #x,y
plt.show()

plt.scatter(year, pop)    #scatter plot
plt.show()

#_________________________________________________________
# World population Data:
year = np.arange(1951,2020,1)
population  = np.array([2.583816786,2.630584384,2.677230358,2.724302468,2.772242535,2.821383444,2.871952278,
                        2.924081243,2.977824686,3.033212527,3.090305279,3.149244245,3.210271352,3.273670772,
                        3.339592688,3.408121405,3.479053821,3.5518807,3.625905514,3.70057765,3.7757909,
                        3.851545181,3.927538695,4.003448151,4.079087198,4.154287594,4.229201257,4.304377112,4.380585755,
                        4.458411534,4.537845777,4.618776168,4.701530843,4.786483862,4.873781796,4.963633228,
                        5.055636132,5.148556956,5.240735117,5.33094346,5.418758803,5.504401149,5.588094837,
                        5.670319703,5.751474416,5.83156502,5.910566295,5.988846103,6.066867391,6.145006989,
                        6.223412158,6.302149639,6.381408987,6.461370865,6.542159383,6.623847913,6.706418593,
                        6.789771253,6.873741054,6.958169159,7.043008586,7.128176935,7.213426452,7.298453033,
                        7.38300882,7.46696428,7.550262101,7.632819325,7.714576923])
print("last items:", year[-1], population[-1])    #last items: 2019 7.714576923
plt.plot(year, population)
plt.show()
plt.scatter(year, population)
plt.show()
#    Histogram - to explore the dataset - distribution of the values

#help(plt.hist)       # x= no of values, bins = how many parts 

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins = 3)
plt.show()

data = np.random.random(1000)    #1000 numbers between 0-1
plt.hist(data)    # bins=10 by default
plt.show()
plt.clf()    #cleans the display
plt.hist(data, bins=5)
plt.show()
plt.clf()
plt.hist(data, bins = 20)
plt.show()
plt.clf()

# Labels
# World population Data:
year = np.arange(1951, 2020, 1)
population  = np.array([2.583816786,2.630584384,2.677230358,2.724302468,2.772242535,2.821383444,2.871952278,
                        2.924081243,2.977824686,3.033212527,3.090305279,3.149244245,3.210271352,3.273670772,
                        3.339592688,3.408121405,3.479053821,3.5518807,3.625905514,3.70057765,3.7757909,
                        3.851545181,3.927538695,4.003448151,4.079087198,4.154287594,4.229201257,4.304377112,4.380585755,
                        4.458411534,4.537845777,4.618776168,4.701530843,4.786483862,4.873781796,4.963633228,
                        5.055636132,5.148556956,5.240735117,5.33094346,5.418758803,5.504401149,5.588094837,
                        5.670319703,5.751474416,5.83156502,5.910566295,5.988846103,6.066867391,6.145006989,
                        6.223412158,6.302149639,6.381408987,6.461370865,6.542159383,6.623847913,6.706418593,
                        6.789771253,6.873741054,6.958169159,7.043008586,7.128176935,7.213426452,7.298453033,
                        7.38300882,7.46696428,7.550262101,7.632819325,7.714576923])
# Make a line plot: year on the x-axis, population on the y-axis
plt.plot(year, population)
# Add axis labels using the plt.xlabel(), plt.ylabel() and plt.title() commands
xlab = 'Year'
plt.xlabel(xlab)
plt.ylabel('Population(billions)')
plt.title('World population')
plt.yticks([0,2,4,6,8,10])    # creating the y-scale as we want it to show
# Definition of tick_val and tick_lab
tick_val = [2, 3, 4, 5, 6, 7, 8]
tick_lab = ['2b', '3b','4b','5b','6b','7b','8b']
plt.yticks(tick_val, tick_lab)  # replacing the ticks with labels 

#    Add more data    TODO doesn't work
#year = [1800, 1850, 1900] + year
#population = [1.0, 1.262, 1.650] + population

plt.show()

#             Sizes

x_data = np.arange(0,10)
y_data = np.array([2, 2.5, 3, 2.2 ,4 ,6, 5.5, 8, 7.7, 10])
# Make a scatter plot:
plt.scatter(x_data, y_data)
plt.show()
#  the size of the dots corresponds to the population
s = np.array([20, 100, 200, 400, 70, 500, 800, 1500, 300, 900])
plt.scatter(x_data, y_data, s)   # s is the size of each dot
plt.show()

# color each marker
cols = ['red','green','blue','yellow','pink','red','green','blue','yellow','pink']
plt.scatter(x_data, y_data, 4*s, c=cols, alpha=0.8) # alpha defines transparency
plt.show()

#------------------------
x = np.linspace(0, 8, 50)   # start, stop, num
plt.plot(x, np.sin(x), 'r-^')    # red, dotted, with ^
plt.show()
plt.plot(x, np.sin(x), 'ro')    # red,  circle, no line. like scatter   TODO see help plot?
plt.show()
# 
# Using legends (מקרא)
plt.plot(x, np.sin(x), 'b-o', 
    x, np.sin(2*x), 'r-^')
plt.show()

plt.plot(x, np.sin(x), label='sin')  
plt.plot(x, np.sin(2*x), label='sin*2')
plt.legend()       # legends as writen by label on plot
plt.show()
# -----------------Scatter with colorbar
x = np.random.rand(200)
y = np.random.rand(200)
size = np.random.rand(200)*30
color = np.random.rand(200)

plt.scatter(x,y, size, color)
plt.colorbar()     # shows a colorbar on the side
plt.show()

#--------------------Create two scatter plots in the same axis
#makes the random numbers predictable so the same numbers will appear in every random array.
np.random.seed(5) 
# Create Xs and Ys
x = np.arange(1, 101) #same X
y = 20 + 3 * x + np.random.normal(0, 60, 100) #same Y (mean,std, n)
y2 = 10 + 2 * x + np.random.normal(0, 60, 100) #another Y
# Plot all in the same graph. Use alpha(transparency) to see the overlap between the points
plt.plot(x, y, "o", color='b', alpha=0.5)
plt.plot(x, y2, "o", color='r', alpha=0.5)
plt.show()

# -------------  When different Xs and Ys are being used
np.random.seed(5) 
# Create Xs and Ys
x = np.arange(1, 101)
x2 = (np.arange(1, 101))*-1
y = 20 + 3 * x + np.random.normal(0, 60, 100)
y2 = 10 + 2 * x + np.random.normal(0, 60, 100)

# Plot all in the same graph. Use alpha to see the overlap between the points
# with legends
plt.plot(x, y, "o", color='b', alpha=0.5, label='Label x,y')
plt.plot(x2, y2, "o", color='r', alpha=0.5, label = 'Label x2,y2')
#    !!!!!    Note: without plt.legend labels won't be shown!
plt.legend(loc=9) # loc='upper center' (see documentation for legends codes)
plt.show()
#     OR Set legend location with x and y coordinates in the range
plt.plot(x, y, "o", color='b', alpha=0.5, label='Label x,y')
plt.plot(x2, y2, "o", color='r', alpha=0.5, label = 'Label x2,y2')
plt.legend(loc=(0.64,0.03)) # the same as plt.legend(loc=4) coordinates x,y 
plt.show()
#         Set legend location outside the plot
plt.plot(x, y, "o", color='b', alpha=0.5, label='Label x,y')
plt.plot(x2, y2, "o", color='r', alpha=0.5, label = 'Label x2,y2')
plt.legend(loc=(0.35,1)) # outside of Y 
plt.show()
#             With keywords and bbox_to_anchore(x,y)
plt.plot(x, y, "o", color='b', alpha=0.5, label='Label x,y')
plt.plot(x2, y2, "o", color='r', alpha=0.5, label = 'Label x2,y2')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25))
plt.show()

#               Create a scatter plot with the best fit line
np.random.seed(5)

# Create Xs and Ys
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
# Set the same color as these 2 plots represents the same values
# Don't forget to use alpha to see the overlap between the line and the points
plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(x), color='b') # create the fit line!
plt.plot(x, y, "o", color = 'b', alpha=0.5)

plt.show()

#          Use ScyPy to generate line formula,  R2  etc.
#========================================================================
np.random.seed(5)
# Create Xs and Ys
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)

# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
line = slope*x+intercept
# Set the same color as these 2 plots represents the same values
# Don't forget to use alpha to see the overlap between the line and the points
plt.plot(x,line, color='b') #Note: use line instead of y
plt.plot(x, y, "o", color = 'b', alpha=0.5)

plt.show()

#               Create two plots on the same axis
#=============================================================
np.random.seed(5)
# Create Xs and Ys
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
# Set the same color as these 2 plots represents the same values
plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(x), color='b')
plt.plot(x, y, "o", color = 'b', alpha=0.5)

# This part is changed:
#--------------------------------------------
y2 = 10 + 2 * x + np.random.normal(0, 60, 100) # a second scattered numbers
# Scatter and line plots with the same color
plt.plot(x, np.poly1d(np.polyfit(x, y2, 1))(x), color='r')  # Line plot w SciPy
plt.plot(x, y2, "o", color = 'r', alpha=0.5)
plt.show()

#              Add the mean, r-squared and a formula
np.random.seed(5)
# Create Xs and Ys
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
line = slope*x+intercept
plt.plot(x,line, color='b') # Line plot of (x,line)
plt.plot(x, y, "o", color = 'b', alpha=0.5) # Scatter plot of (x,y)

#calculate whatever you want
r_squared = np.round(r_value**2, decimals=2)
mu = np.round(np.mean(y), decimals=2)

#plt.text(x,y,string). Use x,y to set the location of the text
plt.text(5, 300, '$\mu={0}$ \n$R^2={1}$'.format(mu, r_squared), fontsize=14)
if intercept>=0:
    plt.text(5,250, '$y={0}*x+{1}$'.format(np.round(slope, decimals=2),np.round(intercept, decimals=2)), fontsize=14)
else:
    plt.text(5,250, '$y={0}*x{1}$'.format(np.round(slope, decimals=2), np.round(intercept, decimals=2)), fontsize=14)

plt.show()

#             figure() פותח חלון חדש לגרף חדש
t = np.linspace(0,2*3.14,50)    #Generate 50 linearly spaced vector in the interval writen
x = np.sin(t)
y = np.cos(t)
plt.figure(1)
plt.plot(x, label='sin')
plt.plot(y, label='cos')       # שם את הגרפים באותו חלון אחד על השני
plt.legend()          # יציג את המקרא בגרף
plt.show()
 

plt.figure(2)     # create a new figure
plt.plot(t, y)
plt.show()

#        subplot    (row(מספר גרפים), columns, active plot) מציג מס' גרפים בחלון אחד
#       -----------------------------------------------------------------------------
#
#    ממלא קודם את השורה הראשונה ויורד לפי כמות הגרפים
#        axes - figure מאפשר מיקום מדוייק של כל גרף בתוך 
plt.figure(3)           # create a new figure
plt.plot(t, y)
plt.subplot(2, 1, 1)   # plot #1 is active
plt.plot(t,y)          # מכין את הגרף הראשון
plt.subplot(2, 1, 2)   # plot #2 is active
plt.plot(t,x)          # מכין את הגרף השני
plt.show()             # מציג את שני הגרפים באותו החלון

plt.figure(4)
plt.subplot(2, 2, 1)   # plot #1 is active
plt.plot(t,y)          # מכין את הגרף הראשון
plt.subplot(2, 2, 2)   # plot #2 is active
plt.plot(t,x)          # מכין את הגרף השני
plt.show()             #יציג גרפים אחד ליד השני ושורה מתחת מקום לגרפים בלי גרפים

plt.close()      #סוגר לגמרי את החלונות לפי חלון ספציפי או הכל      
plt.clf()        # Clear the current figure leaves the window.
#               axes([left, bottom, width, height], axisbg='w') axisbg is the background color for the axis, default white.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
plt.figure(5, figsize=(8,6), dpi=80, facecolor='r', edgecolor='b')
plt.plot(t,x)
a = plt.axes([0.5, 0.6, 0.3, 0.1])     # המיקום של הגרף הבא בתוך הגרף
plt.plot(t,y)
plt.show()

