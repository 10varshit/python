from tkinter import *
def Event():
    a=Label(ap,text="you clicked the button")
    a.pack()
ap=Tk()
ap.geometry("644x350")
but=Button(ap,text="click",command=Event)
but.pack()
#but.bind('<Button-1>',Event)
#but.bind('<Double-1>',quit)
ap.mainloop()