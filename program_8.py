from tkinter import *
root=Tk()
def getvals():
    print(f"the value of username is {uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")
root.geometry('400x867')

user=Label(root,text='username')
password=Label(root,text='password')
user.grid()
password.grid(row=1)

#Variable classes in tkinter
#BooleanVar,DoubleVar,IntVar,StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue,show='*')

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text='Submit',command=getvals).grid()

root.mainloop()

