#USE FOR DISPLAY JPG IMAGES
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.attributes('-fullscreen',True)  #use for full screen resolution

image=Image.open("image_2.jpg")
photo=ImageTk.PhotoImage(image)

l=Label(image=photo)
l.pack()

root.mainloop()