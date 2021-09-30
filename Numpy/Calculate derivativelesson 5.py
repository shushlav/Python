# Calculate derivative (שיפוע)
# lesson 5 - visualization of NumPy array
#================================================
## calculate the sin() function on evenly spaced data.
import numpy as np
from numpy import linspace, nanmin, pi, sin, cos, cumsum 
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 101)
y = sin(x)
c = np.cos(x)

dy = y[1:] - y[:-1]   #הפרשים בין 2 נקודות של וויי
dx = x[1:] - x[:-1]
x_c = (x[1:] + x[:-1])/2    # the center of each slope = average
s = dy/dx   # the slope
plt.plot(x, y, 'b-', x_c, s, 'r-*', x, c, 'y--')
plt.show()


# Using Riemann sums   = AUC
def f(x):
    return sin(pi*x**2)
#גבולות החישוב בין 0-5
a = 0
b = 5
# מספר החלוקות של הגרף = 100
n = 100
dx = (b-a)/n  #גודל כל מלבן שמתחת לעקומה
xi = 0.0
sum = 0.0
for i in range(n):
    xi = xi + dx
    sum += f(xi)
print(sum*dx)     # calculate AUC