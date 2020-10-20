import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

# documentation: https://www.tutorialspoint.com/python/python_gui_programming.htm

HEIGHT = 700
WIDTH = 800
root = tk.Tk()   # creates the root window

# The size of the app (the canvas)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# pack- This geometry manager organizes widgets in blocks before placing them in the parent widget.
'''
#set background from the same directory
This DIDN"T work!!!
background_image = tk.PhotoImage(file='wallpaper.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
'''
path = "D:\\Python\\Reka55.gif"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
background_label = tk.Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

# Creating a frame widget
frame =tk.Frame(root, bg='gray', bd=5) # bd=border margins
# PLACE-This geometry manager organizes widgets by placing them in a specific position in the parent widget.
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')  
# relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.
# Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

# Creating Widgets: Entry = a place to write-in
entry = tk.Entry(frame, bg='green')
entry.place(relwidth=0.65, relheight=1)

# Creating Widgets: button
button = tk.Button(frame, text='Test button', font=40)
# button.pack(side='left', fill='x')  #fill =fills extra space horizontally or vertically or both
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Creating Widgets: label
label = tk.Label(lower_frame, text='This is a label', bg='yellow')
label.place(relwidth=1, relheight=1)   #fills the lower frame (with borders)


root.mainloop()    # To run the app
