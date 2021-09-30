#    MatPlotLib exercise
import matplotlib.pyplot as plt
x = range(10)
plt.plot(x)
plt.show()

#   2
time = [0, 1, 2, 3, 4, 5, 6]
co2_conc = [250, 265, 272, 260, 300, 320, 389]

plt.plot(time, co2_conc, 'b--', label= 'Co2 concentration')  # blue dashed line
xlab = 'Time (decade)'
ylab = 'Co2 concentration'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title('Co2 and Temp vs time')
#           Plots with different scales
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.plot(time, temp, 'y-^', time, co2_conc, 'r*-', label='Temp(C)')

plt.show()
#       Save figure to PDF file
plt.savefig('co2 and temp vs time.pdf')  