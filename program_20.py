from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.geometry('656x656')
def order():
    tsmg.showinfo('order recieved',f'we have recieved your order that is {var.get()},thanks for ordering')


#var=IntVar()
var=StringVar()
var.set("radio")
Label(root,text='what you want to eat',font='lucida 19 bold',justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text='Dosa',padx=14,variable=var,value='dosa').pack(anchor='w')
radio=Radiobutton(root,text='Idly',padx=14,variable=var,value='idly').pack(anchor='w')
radio=Radiobutton(root,text='Paratha',padx=14,variable=var,value='paratha').pack(anchor='w')
radio=Radiobutton(root,text='samosa',padx=14,variable=var,value='samosa').pack(anchor='w')
Button(text='order now',command=order).pack()

root.mainloop()