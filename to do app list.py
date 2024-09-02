from tkinter import *
import time
root=Tk()
root.config(bg="black")
root.geometry("400x500")

r=Label(root,text="To Do List",bg="black",fg="light blue",anchor="center",width=10,font="Arial 35 bold")
r.pack()

t=time.strftime('%H:%M')

r=Label(root,text=t,bg="black",fg="light blue",anchor="center",width=10,font="Arial 10 bold")
r.pack(anchor="ne")

list=[]

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 25 bold")
screen.pack(pady=15,padx=10)
root.config(bg="black")

i=0
def add(event):
    global i
    global scvalue
    global screen
    value=scvalue.get()
    list.append(value)
    scvalue.set("")
    screen.update()

def view(event):
    global scvalue
    global screen
    value=scvalue.get()
    lbx.insert(ACTIVE,"all are your tasks")
    for i, task in enumerate(list, 1):
         lbx.insert(ACTIVE,f"{i}.{task}")

def delu(event):
     lbx.delete(0,END)

def delete(event):
    global i
    global scvalue
    global screen
    value=int(scvalue.get())
    list.pop(value-1)
    lbx.delete(0,END)
    lbx.insert(ACTIVE,"all are your tasks")
    for i, task in enumerate(list, 1):
         lbx.insert(ACTIVE,f"{i}.{task}")
    scvalue.set("")
    screen.update()

f=Frame(root,bg="black")

b=Button(f,text="add new task",padx=10,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=25,pady=0)
b.bind("<Button-1>",add)

b=Button(f,text="view task",padx=25,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=25,pady=8)
b.bind("<Button-1>",view)

f.pack(anchor="nw",fill=X)

f=Frame(root,bg="black")

b=Button(f,text="delete task",padx=20,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=25,pady=8)
b.bind("<Button-1>",delete)

b=Button(f,text="close list",padx=25,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(padx=25,pady=8,side=LEFT)
b.bind("<Button-1>",delu)

f.pack(anchor="nw",fill=X)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

lbx=Listbox(root,height=450,width=100,font="lucida 16 bold",bg="pink",yscrollcommand=scrollbar.set)
lbx.pack(anchor="ne",padx=25,pady=25)
scrollbar.config(command=lbx.yview)

root.mainloop()