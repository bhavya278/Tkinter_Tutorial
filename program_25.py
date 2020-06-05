from tkinter import *

class GUI(Tk):
    def __init__(self):       #self = root
        super().__init__()
        self.geometry('454x565')

    def status(self):
        self.var=StringVar()
        self.var.set('ready')
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor='w')
        self.statusbar.pack(side='bottom',fill=X)

    def click(self):
        print('button clicked')
    def createbutton(self,inptext):
        Button(text=inptext,command=self.click).pack()

if __name__ =='__main__':
    window=GUI()        #window=root
    window.status()
    window.createbutton('clickme')
    window.mainloop()