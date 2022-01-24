from tkinter import *
ap=Tk()
def Try():
    statusvar.set("Busy")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("ready now")
ap.geometry("450x310")
statusvar=StringVar()
statusvar.set("ready")
sbar=Label(ap,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(ap,text="try",command=Try).pack()
ap.mainloop()