#USE FOR DISPLAY PNG IMAGES
from tkinter import *
root=Tk()
root.attributes('-fullscreen',True)
photo=PhotoImage(file='image_1.png')
l=Label(image=photo)
l.pack()
root.mainloop()