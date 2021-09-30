# import Numpy, Pandas, and Matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the data file
url='http://apmonitor.com/che263/uploads/Main/data_with_headers.txt'
data_file = pd.read_csv(url)
print(data_file[0:6])
# create time vector from imported data
time = data_file['time']
# parse good sensor data from imported data
sensors = data_file.loc[:, 's1':'s4']

# calculate the correlation of the sensor readings
sensors_corr = sensors.corr()
print(sensors_corr)
print(sensors_corr.describe())
'''
             s1        s2        s3        s4
count  4.000000  4.000000  4.000000  4.000000
mean   0.836244  0.714356  0.822896  0.851040
std    0.154554  0.191086  0.165729  0.169522
min    0.641529  0.607442  0.608453  0.607442
25%    0.756579  0.608201  0.748310  0.818011
50%    0.851724  0.624991  0.841565  0.898360
75%    0.931389  0.731147  0.916150  0.931389
max    1.000000  1.000000  1.000000  1.000000'''
# display the first 6 sensor rows
print(sensors.head(6))     # as same as print(sensors[0:6])

# adjust time to start at zero by subtracting the
#  first element in the time vector (index = 0)
time = time - time[0]

# calculate the average of the sensor readings
avg = np.mean(sensors,1) # over the 2nd dimension


# export data
my_data = [time, sensors, avg]
result = pd.concat(my_data,axis=1)   # avg rows. if we want avg of columns then axis=0
result.columns.values[-1] = 'avg'    # naming the LAST column
print(result.head(10))
                      #export the results
result.to_csv('result.csv')
#result.to_excel('result.xlsx')
#result.to_html('result.htm')
#result.to_clipboard()

# generate a figure
plt.figure(1)
plt.plot(time,sensors['s1'],'r-')
plt.plot(time,avg,'b.')
# add text labels to the plot
plt.legend(['Sensor 1','Average'])
plt.xlabel('Time (sec)')
plt.ylabel('Sensor Values')
# save the figure as a PNG file
plt.savefig('my_Python_plot.png')
# show the figure on the screen
plt.show()
#[$[Get Code]]

