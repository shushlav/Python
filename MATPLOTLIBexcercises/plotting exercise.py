# plotting exercise

import matplotlib.pyplot as plt
import pandas as pd

#    Matplotlib Barchart
p_language = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C**']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['r', 'k', 'g', 'b', 'gold', 'c']     # for bar colors
# you can create ****horizontal***** bar with plt.barh
plt.barh(p_language, popularity, color=colors, edgecolor='k')   # change the colors 

#  The edgecolor argument allows you to color the borders of barplots.
#  plt.barh(p_language, popularity, color='r')    #אם רוצים שכולם יהיו באותו הצבע
plt.title('Popularity of programming language worldwide')
plt.xlabel('Languages')
plt.ylabel('Popularity')
# add the major grid
plt.grid(which='major', color='red', linestyle='-', linewidth=0.3)

# Turn on the minor TICKS, which are required for the minor GRID
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

#   Attach a text label above each bar displaying its height
#
for index, value in enumerate(popularity):
    plt.text(value, index, float(value))

plt.show()

# More changes to the original:
#**************************************

p_language = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C**']

popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['r', 'k', 'g', 'b', 'gold', 'c']     # for bar colors

plt.title('Popularity of programming language worldwide')
plt.xlabel('Languages')
plt.ylabel('Popularity')
# # Select the position of each barplots on the x-axis (space=1,3,3,2,1)
y_pos = [0,1,4,7,9,10]
#Select the width of each bar and their positions
bar_width = [0.1, 0.2, 0.6, 1.1, 0.2, 0.3]   # different widths for each bar!
# create the ticks as the languages5
plt.xticks(y_pos, p_language)
plt.bar(y_pos, popularity, color='y', edgecolor='k', width=bar_width, linewidth=2, align='edge', bottom=50)  
# Custom the subplot layout
plt.subplots_adjust(bottom=0.4, top=.8)   # המרחק של הגרף מהרצפה
# add the major grid
plt.grid(which='major', color='red', linestyle='-', linewidth=0.3)

# Turn on the minor TICKS, which are required for the minor GRID
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

#Write a Python program to create bar plot of scores by group and gender. 
# Use multiple X values on the same chart for men and women.
'''
x = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)
#Define an axis in a figure
fig, ax = plt.subplots()
men = plt.bar(x, men_means, 'g', label='Men')    # first bar 
women = plt.bar(x, women_means, 'r', label='Women')    #second bar with same axis
plt.title('Scores by person')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.legend()
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, men_means, bar_width,
alpha=opacity,
color='g',
label='Men')

rects2 = plt.bar(index + bar_width, women_means, bar_width,
alpha=opacity,
color='r',
label='Women')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()

# Write a Python program to create bar plot from a DataFrame

df = pd.DataFrame(
    {'a': [2, 4, 6, 8, 10],
    'b': [4, 2, 4, 2, 2],
    'c': [8, 3, 7, 6, 4],
    'd': [7, 2, 7, 8, 3],
    'e': [6, 6, 8, 6, 2]}, index=[2,4,6,8,10])   # index - לפי הדרישה
df.plot(kind='bar')
                        # grid ticks
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.5, color='g')
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='k')

plt.show()

#  Write a Python program to create bar plots with error bars on the same figure
x = np.arange (4) # לפי מספר האיברים בוויי
mean_velocity = (0.2474, 0.1235, 0.1737, 0.1824)
sd_velocity = [0.3314, 0.2278, 0.2836, 0.2645]
# the width of the bars
width = 0.35
plt.bar(x, mean_velocity, width, color='r', align='edge', yerr=sd_velocity, ecolor='k', capsize=3)

# add some text for labels, title and axes ticks
plt.title('Scores by Velocity')
plt.xlabel('Velocity')
plt.ylabel('Scores')
# show the current axis limits values
print(plt.axis())    #     (-0.2175, 4.5675, 0.0, 74.9385)
plt.axis([0.0, 3.5, -0.2 , 0.65])    ## set new axes limits [xmin, xmax, ymin, ymax] 
#   Attach a text label above each bar displaying its error
for index, value in enumerate(sd_velocity):    #TODO - doesn't work!
    plt.text(value, index, float(value))
   
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.5, color='g')
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='k')
plt.show()
