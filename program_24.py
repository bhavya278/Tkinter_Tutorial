from tkinter import *
root=Tk()
root.geometry('500x500')
root.title('status bar'

def upload():
    statusvar.set('busy...')
    sbar.update())
    import time
    time.sleep(2)
    statusvar.set('ready now')
statusvar=StringVar()
statusvar.set("ready")

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM,fill=X)

Button(root,text='upload',command=upload).pack()

root.mainloop()