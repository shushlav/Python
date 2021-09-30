"""Trying Michael Hansen's temperature trend example using Pandas
The original example, without Pandas, is available at:
http://software-carpentry.org/2012/05/an-exercise-with-matplotlib-and-numpy/
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from scipy import stats
from datetime import datetime



def read_weather(file_name):
    #Importing the file with the headers on row 0
    data = pd.read_csv(file_name, index_col=0, header=[0], parse_dates=True)
    return data
    
def temp_plot(mean_temps, min_temps=None, max_temps=None):
    
    year_start = datetime(2016, 1, 1)
    days = np.array([(d - year_start).days + 1 for d in mean_temps.index])    

    fig = pyplot.figure()
    pyplot.title('Temperatures in Bloomington 2016')
    pyplot.ylabel('Mean Temperature (C)')
    pyplot.xlabel('Day of Year')
    
    if (max_temps is None or min_temps is None):
        pyplot.plot(days, mean_temps, marker='o')
    else:
        temp_err = np.vstack((mean_temps - min_temps,
                              max_temps - mean_temps))

        pyplot.errorbar(days, mean_temps, marker='o', yerr=temp_err)
        pyplot.title('Temperatures in Bloomington 2016 (max/min)')    
    
    #Use Scipy for statistical functions
    slope, intercept, rval, pval, stderr = stats.linregress(days, mean_temps)
    ideal_temps = intercept + (slope * days)
    fit_label = 'Linear fit ({0:.3f})'.format(slope)    # 3 numbers after the dot
    pyplot.plot(days, ideal_temps, color='red', linestyle='--', label=fit_label)
    pyplot.annotate('r^2 = {0:.3f}'.format(rval ** 2), (0.05, 0.9), xycoords='axes fraction')
    pyplot.legend(loc='lower right')
    
    pyplot.show()
    return fig

#-------------------------------------------------- 

# Read data and extract dates, temperatures, and events
data = read_weather('weather.csv')
min_temps = data['Min TemperatureC']
mean_temps = data['Mean TemperatureC']
max_temps = data['Max TemperatureC']
events = data[' Events']

if not os.path.exists('plots'):             # if there is no directory named "plots" - make one
    os.mkdir('plots')

# Plot without error bars
#In Pandas the temperatures are automatically associated with the dates, so
#we can just pass the mean_temps Series object to temp_plot
fig = temp_plot(mean_temps)
fig.savefig('plots/day_vs_temp.png')          # Save the figure

# Plot with error bars
fig = temp_plot(mean_temps, min_temps, max_temps)
fig.savefig('plots/day_vs_temp-all.png')       # Save the figure