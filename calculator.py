import time
import pyttsx3
import tkinter as tk
from tkinter import *

root=Tk()

root.config(bg="black")
root.geometry("400x600")

list=[]

t=time.strftime('%H:%M')
ft=Frame(root,bg="black")

r=Label(ft,text="Calculator",fg="lightgrey",bg="black",anchor="center",width=8,font="Arial 18 bold")
r.pack(side=LEFT)

r=Label(ft,text=t,fg="lightgrey",bg="black",width=10,font="Arial 10 bold")
r.pack(anchor="ne",side=LEFT,pady=10)
ft.pack()

def time():
    pass

def click(event):
    global scvalue

    global screen
    text=event.widget.cget("text")

    if text=="=":
        lbx.delete(0,END)
        if scvalue.get().isdecimal():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        valu=scvalue.get()
        list.append(valu)
        lbx.insert(ACTIVE,f"{value}")
    elif text=="C":
        scvalue.set("")
        screen.update()
        lbx.delete(0,END)
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    time()

i=0


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,font="lucida 25 bold",textvariable=scvalue,width=20,justify='right')
screen.pack(pady=10,padx=10)
root.config(bg="black")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y,padx=5,pady=16)
lbx=Listbox(root,height=3,width=40,font="lucida 25 bold",bg="pink",yscrollcommand=scrollbar.set,justify='right')
lbx.pack(anchor="ne",padx=8,pady=20)
scrollbar.config(command=lbx.yview)


fr=Frame(root,bg="lightgrey")

f=Frame(root,bg="black")

b=Button(f,text="1",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button >",click)

b=Button(f,text="3",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="black")
b=Button(f,text="4",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="6",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="black")
b=Button(f,text="7",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b=Button(f,text="8",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="9",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="black")
b=Button(f,text="0",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",click)

f.pack()


f=Frame(fr,bg="black")

b=Button(f,text="(",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text=")",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",click)

f.pack()
time()


def history(value):
    lbx.insert(ACTIVE,"")
    scvalue.set("HISTORY...")

    for i ,task in enumerate(list,1):
        lbx.insert(ACTIVE,f"{i}. {task} = {eval(task)}")


def clear(event):
    lbx.delete(0,END)
    scvalue.set("")

def hi(event):
    value=int(scvalue.get())
    list.pop(value-1)
    lbx.delete(0,END)
    lbx.insert(ACTIVE,"")

    for i, task in enumerate(list, 1):
         lbx.insert(ACTIVE,f"{i}. {task} = {eval(task)} ")
    scvalue.set("")
    screen.update()   

f=Frame(root,bg="black")

b=Button(f,text="history",padx=13,pady=5,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3,anchor="nw")
b.bind("<Button-1>",history)

b=Button(f,text="clear",padx=15,pady=5,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",clear)

b=Button(f,text="history deleted",padx=13,pady=5,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3,anchor="nw")
b.bind("<Button-1>",hi)

f.pack()

# scrollbar=Scrollbar(root)
# scrollbar.pack(side=RIGHT,fill=Y,padx=5,pady=16)
# lbx=Listbox(root,height=100,width=40,font="lucida 16 bold",bg="pink",yscrollcommand=scrollbar.set)
# lbx.pack(anchor="ne",padx=8,pady=20)
# scrollbar.config(command=lbx.yview)

engine=pyttsx3.init()
engine.say("hey whats up")
engine.say("i am calculator.....") 
engine.say("do you want to use..........")
engine.runAndWait()


root.mainloop()