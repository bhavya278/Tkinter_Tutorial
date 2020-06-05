from tkinter import *
root=Tk()
root.geometry('565x757')
root.title("listbox tutorial")
def add():
    global i
    lbx.insert(ACTIVE,f'{i}')
    i+=1

i=0
lbx=Listbox(root)
lbx.pack()

lbx.insert(END,'First item of a list box')
Button(root,text='add item',command=add).pack()


root.mainloop()