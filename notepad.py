from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
root=Tk()
import os
root.title("untitted - notepad")
root.geometry("644x788")

Textarea=Text(root,   font="lucida 13")
file=None
Textarea.pack(expand=True,fill=BOTH)
scroll=Scrollbar(Textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scroll.set)

def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    Textarea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),
                                                            ("Text Documents","*.txt")])
    
    if file=="":
        filr= None
def savefile():
    pass
def quitapp():
    pass
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label="New",command=newfile)

filemenu.add_command(label="Open",command=openfile)

filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitapp)

menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
editmenu=Menu(menubar,tearoff=0)

editmenu.add_command(label="Cut",command=cut)

editmenu.add_command(label="copy",command=copy)

editmenu.add_command(label="paste",command=paste)
editmenu.add_separator()
editmenu.add_command(label="Exit",command=quitapp)

menubar.add_cascade(label="Edit",menu=editmenu)
def about():
    showinfo("notepad","notepad by harsh")
root.config(menu=menubar)
helpmenu=Menu(menubar,tearoff=0)

helpmenu.add_command(label="About notepad",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)
root.config(menu=menubar)






root.mainloop()