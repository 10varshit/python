from tkinter import *
ap=Tk()
def Click():
    svar.set("Processing")
    sbar.update()
    import time
    time.sleep(1)
    svar.set("Done!")
def Try():
    svar.set("Thinking")
    sbar.update()
    import time
    time.sleep(2)
    svar.set("ok fine")
ap.geometry("320x270")
svar=StringVar()
svar.set("Welcome")
sbar=Label(ap,textvariable=svar,anchor="w",bg="black",fg="white")
sbar.pack(side=BOTTOM,fill=X)
Button(ap,text="click me",command=Click).pack()
Button(sbar,text="try me",command=Try).pack()
ap.mainloop()