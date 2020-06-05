
from tkinter import *
root=Tk()

root.geometry('222x444')
root.title('entry form')
def getvals():
    print(f'value of name is {student_value.get()}')
    print(f'value of age is {age_value.get()}')
    print(f'value of gender is {gender_value.get()}')
    print(f'value of password is {password_value.get()}')

student_name=Label(root,text="enter student name")
student_name.grid(row=0,column=0)
age=Label(root,text="enter student age")
age.grid(row=1,column=0)
gender=Label(root,text="enter student gender")
gender.grid(row=2,column=0)
password=Label(root,text="enter student password")
password.grid(row=3,column=0)

student_value=StringVar()
age_value=StringVar()
gender_value=StringVar()
password_value=StringVar()

student_entry=Entry(root,textvariable=student_value).grid(row=0,column=1)
age_entry=Entry(root,textvariable=age_value).grid(row=1,column=1)
gender_entry=Entry(root,textvariable=gender_value).grid(row=2,column=1)
password_entry=Entry(root,textvariable=password_value,show='*').grid(row=3,column=1)

Button(text='Submit',command=getvals).grid()

root.mainloop()