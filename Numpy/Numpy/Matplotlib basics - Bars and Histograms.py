#@@@@@@@@@@@@@@@   Matplotlib   @@@@@@@@@@@@@@@@@@@@@
#------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#                    Bars
# Define a figure with 2 columns and 2 rows.
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(4, 4), dpi=100)

#Create an array for each bar
np.random.seed(1)
java = np.random.random_integers(40, size=(100,))
matlab = np.random.random_integers(60, size=(100,))
python = np.random.random_integers(100, size=(100,))
#We plot the mean of Y arrays
values = [np.mean(java), np.mean(matlab), np.mean(python)]  
xlabels = ['Java', 'MATLAB', 'Python']   #x ticks
#Set a width to each bar
width=0.8 
#--------------------------------------------
# For the example I'll use the same data and just change the colors.

# The top left axis
axes[0,0].bar(range(len(xlabels)), values, width=width, color='b', alpha=0.4) #bar plot on the top left axis
axes[0,0].set_ylim([0, 60]) #add some space on the x axis
axes[0,0].set_xlim([-0.3, 3.1]) #add some space on the y axis

# NOTE: Here I'm copy-paste the lines above, and just change the axis location, colors and title

# The top right axis
axes[0,1].bar(range(len(xlabels)), values, width=width, color='r', alpha=0.4) #bar plot on the top left axis
axes[0,1].set_ylim([0, 60]) #add some space on the x axis
axes[0,1].set_xlim([-0.3, 3.1]) #add some space on the y axis

# The bottom left axis
axes[1,0].bar(range(len(xlabels)), values, width=width, color='g', alpha=0.4) #bar plot on the top left axis
axes[1,0].set_ylim([0, 60]) #add some space on the x axis
axes[1,0].set_xlim([-0.3, 3.1]) #add some space on the y axis

# The bottom right axis
axes[1,1].bar(range(len(xlabels)), values, width=width, color='k', alpha=0.4) #bar plot on the top left axis
axes[1,1].set_ylim([0, 60]) #add some space on the x axis
axes[1,1].set_xlim([-0.3, 3.1]) #add some space on the y axis

# Add a title for the whole figure
fig.suptitle('2x2 Axes', fontsize=12)

plt.show()
#             Can use a loop for the axes
#-------------------------------------------------------
# Define a figure with 3 columns and 3 rows.
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(6, 6), dpi=100)

#Create an array for each bar
np.random.seed(1)
java = np.random.random_integers(40, size=(100,))
matlab = np.random.random_integers(60, size=(100,))
python = np.random.random_integers(100, size=(100,))
#We plot the mean of Y arrays
values = [np.mean(java), np.mean(matlab), np.mean(python)]  
#Set a width to each bar
width=0.8 

# I'm too lazy to write all those lines as I've done before, so I'm going to write a for-loop.
axis_all = [axes[0,0], axes[0,1], axes[0,2], 
            axes[1,0], axes[1,1], axes[1,2],
            axes[2,0], axes[2,1], axes[2,2]] # locations available
colors = ['b', 'r', 'g', 'k', 'y', '#00ffff', '#808080', '#996633', '#df80ff'] # colors list

for c,ax in enumerate(axis_all):
    ax.bar(range(len(xlabels)), values, width=width, color=colors[c])
    ax.set_ylim([0, 60]) #add some space on the x axis
    ax.set_xlim([-0.3, 3.1]) #add some space on the y axis

fig.suptitle('3x3 Axes', fontsize=12)

plt.show()
#--------------------------------------------
#                        Customizing Location of Subplot    using grid
#                  ----------------------------------------------------------
fig = plt.figure(figsize=(5, 6))

ax1 = plt.subplot2grid((3,2), (0,0), colspan=2)
ax2 = plt.subplot2grid((3,2), (1,0))
ax3 = plt.subplot2grid((3,2), (1,1))
ax4 = plt.subplot2grid((3,2), (2,0))
ax5 = plt.subplot2grid((3,2), (2,1))

axis_all = [ax1, ax2, ax3, ax4, ax5]

for c,ax in enumerate(axis_all):
    ax.bar(range(len(xlabels)), values, width=width, color=colors[c])
    ax.set_ylim([0, 60]) #add some space on the x axis
    ax.set_xlim([-0.3, 3.1]) #add some space on the y axis

fig.suptitle('Customizing Location of Subplot using grid', fontsize=12)
plt.show()

fig = plt.figure(figsize=(6, 6))

ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2, 0))
ax5 = plt.subplot2grid((3,3), (2, 1))

axis_all = [ax1, ax2, ax3, ax4, ax5]

for c,ax in enumerate(axis_all):
    ax.bar(range(len(xlabels)), values, width=width, color=colors[c])
    ax.set_ylim([0, 60]) #add some space on the x axis
    ax.set_xlim([-0.3, 3.1]) #add some space on the y axis

plt.show()

#------------------------------------------------------------------
values = [20,30,70]    #y values
width=0.8    #width of each column (you can change it)
plt.bar(range(len(values)), values, width=width)   #plt.bar(number of bars, values, width)
#Change the ticks on the X axis
xlabels = ['Java', 'MATLAB', 'Python']   #x ticks
plt.xticks(np.arange(len(xlabels)) + width/2, xlabels)   #plt.xticks(location, new_ticks)
plt.show()

#  When Ys are arrays: Plot the mean of Y arrays
#Create an array for each bar
np.random.seed(1)
java = np.random.random_integers(40, size=(100,))
matlab = np.random.random_integers(60, size=(100,))
python = np.random.random_integers(100, size=(100,))
#We plot the mean of Y arrays
values = [np.mean(java), np.mean(matlab), np.mean(python)]
#Set a width to each bar
width=0.8


#     Calculates the standard error of the mean of each array.
sem = [stats.sem(prog_language) for prog_language in [java, matlab, python]]

#    Add the error to each bar, and make the bars lighter so you could see the error
#    plt.bar(range(len(xlabels)), values, width=width, alpha=0.3, yerr=sem)   #yerr = y error
#                 Annotate the SEM for each bar = sem מציג את המספרים של 
#Set variable my_b = plt.bar()
my_b = plt.bar(range(len(xlabels)), values, width=width, alpha=0.3, yerr=sem)
rects = my_b.patches

#Attach SEM to each bar 
for i,prog_lang in enumerate([java, matlab, python]):
    plt.text(rects[i].get_x() + rects[i].get_width()/2., 1.06*values[i],
            '%0.2f' % sem[i],
            ha = 'center', va = 'bottom', fontsize=12)
    
#         Add the SEM values to each bar
plt.bar(range(len(values)), values, width=width)   #plt.bar(number of bars, values, width)
#        Change the ticks on the X axis
#xlabels = ['Java', 'MATLAB', 'Python']   #x ticks
#plt.xticks((np.arange(len(xlabels)) + width/2), xlabels)   #plt.xticks(location, new_ticks)

#    Rotate the x ticks
#Change the ticks on the X axis
xlabels = ['Java programming', 'MATLAB programming', 'Python programming'] # make long ticks
plt.xticks(np.arange(len(values)), xlabels, rotation=30)     # HERE: add rotation to plt.xticks() (I set to 30 degree)
# Add some space in X and Y axes
#Add some space on X&Y axis by set a fixed lim
plt.ylim([0, 60])
plt.xlim([-0.3, 3.1])
plt.show()

#--------------------------------------------------------------------

#The mean grade of women and men in each course
YF_mean = [84, 86, 93]    # mean grades of women in each course [Java, MATLAB and Python].
YM_mean = [63, 79, 87]    # mean grades of Men  in each course [Java, MATLAB and Python].

width=0.3          # the width of the bars
courses = 3        # number of courses avilable
ind = np.arange(courses) # the x locations for the courses

#Define an axis in a figure
fig, ax = plt.subplots()
#In this way W and M will show on the same axis
W = ax.bar(ind + width, YF_mean, width, color='b', alpha=0.4) # women bars on the right
M = ax.bar(ind, YM_mean, width, color='g', alpha=0.4)         # men bars on the left

#Add some space on X&Y axis by set a fixed lim
ax.set_ylim([0, 130])
ax.set_xlim([-0.3, 3.1])

#Add some text for labels, title and axes ticks
ax.set_ylabel('Grade', fontsize=12)
ax.set_title('Grades by programming course and gender', fontsize=14)
ax.set_xticks(ind + width)
ax.set_xticklabels(('Java', 'MATLAB', 'Python'), fontsize=12)
ax.set_yticklabels(np.arange(0,110,20), fontsize=12) #We must change Y labels because the maximal grade is 100

#Add a legend
ax.legend((M[0], W[0]), ('Men', 'Woman'), ncol=2, mode="expand")

plt.show()

#---------------------------------------
#Create arrays shape 3x30 represent the grades of 30 women and 30 men in three courses
YF = np.array([[89, 92, 83, 88, 88, 92, 99, 100, 78, 66, 95, 94, 80,
                97, 52, 55, 86, 84, 93, 92, 98, 81, 100, 93, 63, 100,
                82, 85, 71, 54],
               [89, 91, 83, 88, 88, 92, 99, 90, 78, 66, 95, 94, 80,
                97, 92, 55, 86, 84, 93, 92, 98, 81, 100, 93, 63, 100,
                82, 85, 71, 87],
               [89, 90, 91, 92, 93, 94, 95, 96, 97,  98,  99,  100,  99,
                98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 90, 91, 92,
                93, 94, 95, 96]])
YM = np.array([[30, 40, 50, 60, 70, 80, 90, 85, 75, 65, 55, 45, 35,
                37, 47, 57, 67, 77, 87, 97, 98, 88, 78, 68, 58, 48,
                38, 50, 55, 60],
               [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 88, 89,
                90, 97, 98, 86, 84, 93, 92, 55, 46, 80, 68, 78, 91,
                82, 85, 71, 87],
               [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 83,
                94, 95, 96, 97, 98, 99, 100, 81, 82, 83, 84, 85, 86,
                80, 79, 77, 76]])

width=0.3          # the width of the bars
courses = 3        # number of courses avilable
ind = np.arange(courses) # the x locations for the courses

#We plot the mean of Y arrays
YF_mean = np.array([int(np.mean(prog_course)) for prog_course in YF])
YM_mean = np.array([int(np.mean(prog_course)) for prog_course in YM])

#Calculate the SEM (just because we want to)
YF_sem = [stats.sem(grades) for grades in YF]
YM_sem = [stats.sem(grades) for grades in YM]

#Define an axis in a figure
fig, ax = plt.subplots()
#In this way W and M will show on the same axis
W = ax.bar(ind + width, YF_mean, width, color='b', yerr=YF_sem, alpha=0.4) # women bars on the right
M = ax.bar(ind, YM_mean, width, color='g', yerr=YM_sem, alpha=0.4)         # men bars on the left

#Add some space on X&Y axis by set a fixed lim
ax.set_ylim([0, 130])
ax.set_xlim([-0.3, 3.1])

#Add some text for labels, title and axes ticks
ax.set_ylabel('Grade', fontsize=12)
ax.set_title('Grades by programming course and gender', fontsize=14)
ax.set_xticks(ind + width)
ax.set_xticklabels(('Java', 'MATLAB', 'Python'), fontsize=12)
ax.set_yticklabels(np.arange(0,110,20), fontsize=12) #We must change Y labels because the maximal grade is 100

#Add a legend
ax.legend((M[0], W[0]), ('Men', 'Woman'), ncol=2, mode="expand")

#Attach SEM to each bar 
def autolabel(gender_plot, gender_sem):
    for i,g in enumerate(gender_plot):
        ax.text(g.get_x() + g.get_width()/2., 1.06*g.get_height(),
                '%0.2f' % gender_sem[i],
                ha='center', va='bottom', fontsize=12)

autolabel(W, YF_sem)
autolabel(M, YM_sem)

plt.show()

#                             HISTOGRAM
#============================================================
#https://shecodesconnect.com/DataAnalysis/Histograms.html

# Make some random values
x = np.random.randn(500)

n, bins, patches = plt.hist(x, 50, facecolor='b', alpha=0.3)
plt.show()
'''
n: is the number of counts in each bin of the histogram
bins: is the left hand edge of each bin = how many rectangles (default=10) לכמה חלקים לחלק את הנתונים
patchesis the individual patches used to create the histogram, e.g a collection of rectangles
'''
x = np.random.normal(size=100)
n, bins, patches = plt.hist(x)   # bins = default=10

plt.setp(patches[0], 'facecolor', 'g')  # colors the first bar in green
plt.show()

# Practice:
# https://software-carpentry.org/blog/2012/05/an-exercise-with-matplotlib-and-numpy.html
# https://www.google.com/url?q=https://drive.google.com/open?id%3D0B9crmgoWupXkUHdEd243YllpYWs&sa=D&ust=1612290261041000&usg=AOvVaw1auomi7wqeRLUuvapIw5v6
