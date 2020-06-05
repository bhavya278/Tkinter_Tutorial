from tkinter import *

root=Tk()
root.geometry('655x944')
root.title('Bhavya Calculator')

scvalue=StringVar()
scvalue.set('')
screen=Entry(root,textvar=scvalue,font='lucida 44 bold',bg='red',relief=SUNKEN)
screen.pack(fill=Y,ipadx=8,padx=10,pady=10)

root.mainloop()