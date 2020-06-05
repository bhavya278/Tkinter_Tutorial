from tkinter import *
root=Tk()
def getvals():
    print(f'value of name is {userentry.get()}')
    print(f'value of age is {passwordentry.get()}')
root.geometry('656x500')
Label(root,text="welcome to bhavya's land",font='comicsansms 13 bold',pady=15).grid(row=0,column=13)

username=Label(root,text='Username')
password=Label(root,text='Password')

username.grid(row=1,column=3)
password.grid(row=2,column=3)

uservalue=StringVar()
passwordvalue=StringVar()
ready=IntVar()

userentry=Entry(root,textvariable=uservalue)
passwordentry=Entry(root,textvariable=passwordvalue,show='*')

userentry.grid(row=1,column=4)
passwordentry.grid(row=2,column=4)

ready_value=Checkbutton(text="want to prebook your meals",variable=ready)
ready_value.grid(row=6,column=3)

Button(text='submit',command=getvals).grid(row=7,column=3)

root.mainloop()