from tkinter import *
import tkinter.messagebox as tmsg
ap=Tk()
def help():
    tmsg.showinfo("Help","You can contact us for any help you want")
def rate():
    a=tmsg.askquestion("feedback","did u like this gui")
    if a=="yes":
        msg="rate us on playstore"
    else:
        msg="what do u feel must be improved"
    tmsg.showinfo("Satisfied",msg)
def change():
    b=tmsg.askretrycancel("do u want to edit","no you're not authorised")
    if b:
        print("ok edit")
    else:
        print("lol")
ap.geometry("500x450")
main_menu=Menu(ap)
m1=Menu(main_menu,tearoff=0,bg="black",fg="white")
m1.add_command(label="New Project...")
m1.add_command(label="New...")
m1.add_command(label="New Scratch File...")
m1.add_separator()
m1.add_command(label="Open...")
m1.add_command(label="Save As...")
main_menu.add_cascade(label="File",menu=m1)
ap.config(menu=main_menu)

m2=Menu(main_menu,tearoff=0,bg="black",fg="white")
m2.add_command(label="Undo Backspace             Ctrl+Z")
m2.add_command(label="Redo             Ctrl+shift+Z")
m2.add_separator()
m2.add_command(label="Cut             Ctrl+X")
m2.add_command(label="Copy             Ctrl+C")
m2.add_command(label="Paste             Ctrl+V")
main_menu.add_cascade(label="Edit",menu=m2)
ap.config(menu=main_menu)
ap.configure(bg="grey")

m3=Menu(main_menu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="rate us",command=rate)
m3.add_command(label="change",command=change)
main_menu.add_cascade(label="Help",menu=m3)
ap.config(menu=main_menu)


ap.mainloop()