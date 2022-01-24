'''padx
pady
relief
fill
side
anchor'''
from tkinter import *
ap=Tk()
ap.title("VARSHIT")
ap.geometry("500x400")
f1=Frame(ap,bg="black",borderwidth=10,relief=SUNKEN)
l=Label(f1,text="project-sample")
l.pack(pady=142)
f1.pack(side=LEFT,fill=Y,pady=20)
f2=Frame(ap,bg="green",borderwidth=15,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l1=Label(f2,text="WELCOME",foreground="blue",font="Helvetica 10 italic")
l1.pack()
ap.mainloop()