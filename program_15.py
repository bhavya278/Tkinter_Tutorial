from tkinter import *
from PIL import Image,ImageTk
def every_100(text):
    final_text=''
    for i in range(0,len(text)):
        final_text=final_text+text[i]
        if i%100==0 and i!=0:
            final_text+='\n'
    return final_text
root=Tk()
root.title('Bhavya Publication')
root.attributes('-fullscreen',True)
texts=[]
photos=[]
for i in range(3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))
    image=Image.open(f'image_{i+2}.jpg')

    #TODO: resize the image

    image=image.resize((225,265),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0=Frame(root,width=800,height=70)
Label(f0,text='code with bhavya news',font='lucida 33 bold').pack()
Label(f0,text='27 march 2020',font='lucida 13 bold').pack()
f0.pack()

f1=Frame(root,width=900,height=200,pady=30)
Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
Label(f1,image=photos[0],anchor='e').pack()
f1.pack(anchor='w')

f2=Frame(root,width=900,height=200,pady=30,padx=22)
Label(f2,text=texts[1],padx=22,pady=22).pack(side=RIGHT)
Label(f2,image=photos[1],anchor='e',padx=22).pack()
f2.pack(anchor='w')

f3=Frame(root,width=900,height=200,pady=30)
Label(f3,text=texts[2],padx=22,pady=22).pack(side=LEFT)
Label(f3,image=photos[2],anchor='e').pack()
f3.pack(anchor='w')
root.mainloop()