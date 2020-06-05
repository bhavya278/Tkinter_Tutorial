from tkinter import *
root=Tk()
def getvals():
    print("submitting form")

    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("record.txt",'a') as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")

root.attributes('-fullscreen',True)

photo=PhotoImage(file='image_1.png')
l=Label(image=photo)
l.grid(row=100,column=100)


#heading
Label(root,text='welcome to bhavya lapi',font='comicsansms 13 bold',pady=15).grid(row=0,column=3)

photo=PhotoImage(file='image_1.png')
l=Label(image=photo)
l.grid(row=100,column=100)

#text for our form

name=Label(root,text='Name')
phone=Label(root,text='Phone')
gender=Label(root,text='Gender')
emergency=Label(root,text='Emergency Contact')
paymentmode=Label(root,text='Payment Mode')

#pack text for our form

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#tkinter variable for storing entries

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#entries for a form

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)

#packing the entries

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#check box and packing it

foodservice=Checkbutton(text="want to prebook your meals",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

#button and packing it and assigning it a command

Button(text='submit',command=getvals).grid(row=7,column=3)
root.mainloop()

