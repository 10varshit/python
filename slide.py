from tkinter import *
import tkinter.messagebox as tmsg
ap=Tk()
def Get():
    print(f"{slide.get()}")
    tmsg.showinfo("feedback","thanks for the feedback")
    with open("get.txt","a") as f:
        f.write(f"{slide.get()}\n")
ap.geometry("650x500")
slide=Scale(ap,from_=0,to=10,tickinterval=2,orient=HORIZONTAL)
slide.pack(padx=40)
a=Button(ap,text="submit",command=Get).pack()

def done():
    print(f"{var1.get()}")
    tmsg.showinfo("details","good to know")
#radio button
var1=StringVar()

var1.set("bismilla")
Label(ap,text="r u fine",justify=LEFT).pack()
radio=Radiobutton(ap,text="yes",variable=var1,value="yes").pack()
radio1=Radiobutton(ap,text="no",variable=var1,value="no").pack()
Button(text="submit",command=done).pack()

#listbox
def add():
    global i
    lb.insert(ACTIVE,f"{i}")
    i+=1
i=0
lb=Listbox(ap)
lb.pack()
lb.insert(END,"FIRST ITEM")
Button(ap,text="add",command=add).pack()


#scrollbar
scrollbar=Scrollbar(ap)
scrollbar.pack(side=RIGHT,fill=Y)
lb1=Listbox(ap,yscrollcommand=scrollbar.set)
for i in range(344):
    lb1.insert(END,f"Item{i}")
lb1.pack(fill="both")
scrollbar.config(command=lb1.yview)


ap.mainloop()

