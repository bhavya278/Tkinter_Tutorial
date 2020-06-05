from tkinter import *
root=Tk()
root.geometry('600x450')
def hello():
    print("hlo")
def hii():
    print("hii")
def darling():
    print("darling")
def dear():
    print("dear")
frame=Frame(root,borderwidth=6,bg='grey',relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1=Button(frame,fg='red',text='hello',command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(frame,fg='red',text='hii',command=hii)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg='red',text='darling',command=darling)
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg='red',text='dear',command=dear)
b4.pack(side=LEFT,padx=23)

root.mainloop()