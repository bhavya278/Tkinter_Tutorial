from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry('500x500')
root.title("pycharm")
def myfunc():
    print("dsf bf h ")
def help():
    print('hii')
    tmsg.showinfo('help','bhavya always for you')  #it return ok
def rate():
    print('rate us')
    value=tmsg.askquestion(" was yr experience good",'how was your experience')
    if value=='yes':
        msg='good. rate us on appstore'
    else:
        msg='tell us what ur problem'
    tmsg.showinfo('Experience',msg)
def divya():
    ans=tmsg.askretrycancel('divya se dosti kr lo','sry divya nhi bnegi apki dost')
    if ans:
        print('retry krne pr bhi kuch nhi hoga')
    else:
        print("bhaut bdiya cancel kr diya")
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


m3=Menu(mainmenu,tearoff=0)
m3.add_command(label='help',command=help)
m3.add_command(label='rate',command=rate)
m3.add_command(label='befriend divya',command=divya)
mainmenu.add_cascade(label='help',menu=m3)
root.config(menu=mainmenu)
root.mainloop()


