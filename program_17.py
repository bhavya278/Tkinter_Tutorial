from tkinter import *
root=Tk()
root.geometry('900x900')
root.title("pycharm")
def myfunc():
    print("dsf bf h ")

#use these to create a non dropdown menu
'''mymenu=Menu(root)
mymenu.add_command(label='File',command=myfunc)
mymenu.add_command(label='Exit',command=quit)
root.config(menu=mymenu)'''

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='File',menu=m1)


m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit',menu=m2)

root.mainloop()