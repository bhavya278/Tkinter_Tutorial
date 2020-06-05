from tkinter import *
root=Tk()

def bhavya(event):
    print(f'clicked on {event.x},{event.y}')
root.title("events")
root.geometry('600x700')

widget=Button(root,text='click me plz')
widget.pack()

widget.bind('<Button-1>',bhavya)
widget.bind('<Double-1>',quit)
root.mainloop()