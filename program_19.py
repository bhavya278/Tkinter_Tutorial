from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry('500x500')
root.title("bhavya")
def getdollar():
    print(f"we have credited{myslider2.get()} dollars to yur bank account")
    tmsg.showinfo('amount credited',f"we have credited{myslider2.get()} dollars to yur bank account")
#myslider=Scale(root,from_=0,to=100)
#myslider.pack()

Label(root,text='how many dollars you want').pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
#myslider2.set(34)
myslider2.pack()
Button(root,text='get dollars',pady=10,padx=10,command=getdollar).pack()

root.mainloop()