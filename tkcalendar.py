import calendar
from tkinter import *
ap=Tk()
ap.geometry("500x450")
ap.configure(bg="light pink")
def show():
    app=Tk()
    app.geometry("600x550")
    app.configure(bg="light yellow")
    yy=int(e1var.get())
    Label(app,text=calendar.calendar(yy),bg="light yellow").pack()
    app.mainloop()
t1=Label(text="CALENDAR",bg="light green",fg="black",height=4,font="comicsans 15 bold").pack(fill=X,pady=10)
t2=Label(text="Enter Year",bg="light green", fg="black",height=3,font="comicsans 10 bold").pack(fill=X,pady=20)
e1var=IntVar()
e1=Entry(ap,width=20,bg="light blue",fg="black",textvariable=e1var).pack()
b1=Button(text="Show",height=2,width=10,bg="light green",fg="black",command=show).pack(pady=20)
b2=Button(text="Exit",height=2, width=10,bg="brown",fg="black",command=ap.destroy).pack()
ap.mainloop()