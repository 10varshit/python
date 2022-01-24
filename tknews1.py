from tkinter import *
from PIL import Image,ImageTk
#def every_50(text):
#    final_text=""
#    for i in range(0,len(text)):
#        final_text+=text[i]
#        if i%100==0 and i!=0:
#            final_text+="\n"
#        return final_text
ap=Tk()
ap.geometry("1000x900")
texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
       text=f.read()
    texts.append((text))
    image=Image.open(f"{i+1}.png")
    image=image.resize((350,200),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(ap,width=800,height=70)
Label(f0,text="News Buzz",font="lucida 25 bold").pack()
Label(f0,text="18-01-2022",font="lucida 10 bold").pack()
f0.pack()
f1=Frame(ap,width=900,height=200)
Label(f1,text=texts[0],pady=20,padx=10).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack(side="left")
f1.pack(anchor="w")
f2=Frame(ap,width=900,height=200,padx=15)
Label(f2,text=texts[1],pady=20,padx=10).pack(side="left")
Label(f2,image=photos[1],anchor="e").pack(side="left")
f2.pack(anchor="w")
f3=Frame(ap,width=900,height=200)
Label(f3,text=texts[2],pady=20,padx=10).pack(side="left")
Label(f3,image=photos[2],anchor="e").pack(side="left")
f3.pack(anchor="w")
ap.mainloop()