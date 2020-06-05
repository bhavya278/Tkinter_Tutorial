from tkinter import *
root=Tk()
root.geometry('444x222')
root.title("bhavya coding")

#important label options
#text-adds the text
#bd-background
#fg-foreground
#font-sets the font

#1.font=('comicsansms',25,'bold')
#2.(font='comicsansms,25,bold')

#padx- x padding
#pady- y padding
#relief- border styling-SUNKEN,RAISED,GROOVE,RIDGE
title_label=Label(text='bhavya is a smart boy',bg='red',fg='white',padx=50,pady=50,font='comicsansms,25,bold',borderwidth=3,relief=SUNKEN)

#IMPORTANT Pack OPTIONS
#anchor=nw/ne
#side=TOP,BOTTOM,LEFT,RIGHT
#use side=BOTTOM for use anchor=se/sw
#fill
#padx
#pady

#title_label.pack(side=BOTTOM,anchor='se',fill=X)
#----------------OR----------------
title_label.pack(side=LEFT,fill=Y,padx=54,pady=54)

root.mainloop()