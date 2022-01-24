from tkinter import *
from PIL import Image,ImageTk
ap=Tk()
ap.geometry("456x350")
image=Image.open("2.png")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
button=Button(ap,text="BUTTON",bg="sky blue",command=ap.destroy)
lab=Label(text="THIS IS A SAMPLE")
lab.pack()
label.pack()
button.pack()
ap.mainloop()
