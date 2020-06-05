from tkinter import *
def update():
    root.geometry(f'{width.get()}x{height.get()}')

root=Tk()
root.geometry('545x471')


width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text='apply',command=update).pack()
root.mainloop()