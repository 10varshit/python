from tkinter import *
from PIL import Image,ImageTk
ap=Tk()

def But1():
    print("U Clicked Button 1")
def But2():
    print("U Clicked Button 2")
def But3():
    print("U Clicked Button 3")
ap.geometry("3000x1000")
ap.title("NEWSBUSS")
f1=Frame(ap,bg="black",borderwidth=10,relief=SUNKEN)
label=Label(f1,text="Todays news\n 11-01-2022",bg="green",foreground="black")
f1.pack(side=TOP,fill=X)
label.pack()
f2=Frame(ap,bg="white",relief=SUNKEN)
photo1=Image.open("1.png")
pho=ImageTk.PhotoImage(photo1)
label=Label(f2,image=pho)
label.pack()
text1=Label(f2,text="What is Lorem Ipsum?\n"
                 "Lorem Ipsum is simply dummy text of the printing and\n"
                 "typesetting industry. Lorem Ipsum has been the industry's \n"
                 "standard dummy text ever since the 1500s, when an unknown printer\n"
                 " took a galley of type and scrambled it to make a type specimen book.",bg="white",foreground="black")
text1.pack()
but1=Button(f2,text="Read",bg="yellow",foreground="black",width=5,height=2,command=But1)
but1.pack()
f2.pack(side=LEFT,fill=Y,padx=20)
f3=Frame(ap,bg="white",relief=SUNKEN)
photo2=Image.open("2.png")
pho1=ImageTk.PhotoImage(photo2)
label1=Label(f3,image=pho1)
label1.pack()
text2=Label(f3,text="Why do we use it?\n"
                 "It is a long established fact that a reader will be \n"
                    "distracted by the"
                 " readable content of a page when looking at its layout. \n"
                 "The point of using Lorem Ipsum is that it has a more-or-less normal \n"
                 "distribution of letters, as opposed to using 'Content here, content here'"
                 "\n making it look like readable English.",bg="white",foreground="black")
text2.pack()
but2=Button(f3,text="Read",bg="yellow",foreground="black",width=5,height=2,command=But2)
but2.pack()
f3.pack(side=LEFT,fill=Y,padx=20)
f4=Frame(ap,bg="white")
f4.pack(side=LEFT,fill=Y,padx=20)
photo3=Image.open("3.png")
pho2=ImageTk.PhotoImage(photo3)
label2=Label(f4,image=pho2)
label2.pack()
text3=Label(f4,bg="white",text="Where can I get.txt some?\n"
                    "There are many variations of passages of Lorem Ipsum available,\n"
                    " but the majority have suffered alteration in some form,\n"
                    " by injected humour, or randomised words which don't look \n"
                    "even slightly believable.\n"
                    " If you are going to use a passage of Lorem Ipsum,\n"
                    " you need to be sure there isn't anything embarrassing hidden \n"
                               "in the middle of text." )

text3.pack()
but3=Button(f4,text="Read",bg="yellow",foreground="black",width=5,height=2,command=But3)
but3.pack()
main_menu=Menu(ap)
m1=Menu(main_menu,tearoff=0,bg="black",fg="white")
m1.add_command(label="New Project...")
m1.add_command(label="New...")
m1.add_command(label="New Scratch File...")
m1.add_command(label="Open...")
m1.add_command(label="Save As...")
main_menu.add_cascade(label="File",menu=m1)
ap.config(menu=main_menu)

m2=Menu(main_menu,tearoff=0,bg="black",fg="white")
m2.add_command(label="Undo Backspace             Ctrl+Z")
m2.add_command(label="Redo             Ctrl+shift+Z")
m2.add_command(label="Cut             Ctrl+X")
m2.add_command(label="Copy             Ctrl+C")
m2.add_command(label="Paste             Ctrl+V")
main_menu.add_cascade(label="Edit",menu=m2)
ap.config(menu=main_menu)
ap.configure(bg="grey")

ap.mainloop()
