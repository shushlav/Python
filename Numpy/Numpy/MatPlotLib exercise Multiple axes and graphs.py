#    MatPlotLib exercise - Multiple graphs and axes
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# using the variable ax1 for single Axes
fig, ax1 = plt.subplots()    # create plot using ax1 instead of plt

time = [0, 1, 2, 3, 4, 5, 6]
co2_conc = [250, 265, 272, 260, 300, 320, 389]

ax1.set_ylabel('[CO2]', color='b')
ax1.plot(time, co2_conc, color='b')
ax2 = ax1.twinx()      ## instantiate a second axes that shares the same x-axis
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
ax2.set_ylabel('Temp (degC', color='r')
ax2.plot(time, temp, color='r')
plt.show()

#     3 graphs side by side
plt.subplot(1, 3, 1)        # 1 row, 3 columns=graphs, graph 1 is active
a = np.arange(0, 10, 1)
plt.plot(a)
plt.subplot(1, 3, 2)        #graph 2 is active
b = np.arange(10, 0, -1)
plt.plot(b)
plt.subplot(1, 3 , 3)       #graph 3 is active
c = [4] * 10
plt.plot(c)
plt.show()


#plt.show()
