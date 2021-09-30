import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
x = np.linspace(0, 2 * np.pi, 101)
s = np.sin(x)
c = np.cos(x)

img = plt.imread('D:\Python\MATPLOTLIBexcercises\dc_metro.JPG')
# creating the size og the layout to 2x2, 3 slots occupied
fig, axes = plt.subplots(2,2)    # nrows=2, ncols=2

# 1st
#---------------------------------
axes[0,0].plot(x, s, 'b-')
axes[0,0].plot(x, c, 'r+' )
axes[0,1].axis('tight')    # the extents fit the plot exactly TODO
# האפס לא מתחיל מהקצה.... למה?


#  2nd
#----------------------------------
axes[0,1].plot(x, s, 'b-')
axes[0,1].grid(which='major')
axes[0,1].set_xlabel('radians')
axes[0,1].set_ylabel('amplitude')
axes[0,1].set_title('sin(x)')
axes[0,1].axis('tight')

#  3rd image show!!! imshow
#----------------------------------
axes[1,0].imshow(img)
plt.tight_layout()    #מסדר מרווחים בין הגרפים ומונע דריסה של שמות הצירים 
plt.show()

# Save the plot to a file
fig.savefig('D:\Python\MATPLOTLIBexcercises\excercise results.png')


#       שיטה נוספת
# Same as before:
x = np.linspace(0, 2 * np.pi, 101)
s = np.sin(x)
c = np.cos(x)

img = plt.imread('D:\Python\MATPLOTLIBexcercises\dc_metro.JPG')

# The changes:
plt.subplot(2, 2, 1)        # 2 row, 2 columns=graphs, graph 1 is active
plt.plot(x, s, 'b-', x, c, 'r+')

#plt.xlim(0, 6)
plt.axis('tight')
# 2 row, 2 columns=graphs, graph 2 is active
plt.subplot(2, 2, 2)
plt.plot(x, s, "b-")
plt.xlabel('radians')
plt.ylabel('amplitude')
plt.title('sin(x)')
plt.grid()
plt.xlim(0, 6)
# 2 row, 2 columns=graphs, graph 3 is active
plt.subplot(2, 2, 3)
plt.imshow(img, extent=[-10, 10, -10, 10])


plt.tight_layout()
plt.show()

# Save the plot to a file
fig.savefig('D:\Python\MATPLOTLIBexcercises\excercise results.png')