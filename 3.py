from tkinter import *
root=Tk()
root.config(bg="black")
root.geometry("400x500")
r=Label(root,text="Bill",bg="black",fg="light blue",anchor="center",width=10,font="Arial 35 bold")
r.pack()
list={}

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
    scvalue.set("")
    screen.update()

def price(value):
    global scvalue
    global screen
    valu=int(scvalue.get())
    list[value]=valu
    scvalue.set("")
    screen.update()

def view(list):
    list[value]=valu
    for value,valu in list.items():
        lbx.insert(ACTIVE,f"{value}-{valu}")

def discount(event):
     lbx.delete(0,END)

def delete(event):
    global i
    global scvalue
    global screen
    value=int(scvalue.get())
    list.pop(value-1)

f=Frame(root,bg="black")

b=Button(f,text="add product",padx=10,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=35,pady=0)
b.bind("<Button-1>",add)

b=Button(f,text="price",padx=25,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=35,pady=8)
b.bind("<Button-1>",price)
f.pack(anchor="nw")
f=Frame(root,bg="black")

b=Button(f,text="discount",padx=20,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=15,pady=8)
b.bind("<Button-1>",delete)

b=Button(f,text="bill",padx=25,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(padx=15,pady=8,side=LEFT)
b.bind("<Button-1>",view)

b=Button(f,text="delete bill",padx=25,pady=10,font="lucida 12 bold",bg="light blue")
b.pack(padx=15,pady=8,side=LEFT)
b.bind("<Button-1>")

f.pack(anchor="nw")

lbx=Listbox(root,height=450,width=100,font="lucida 20 bold",bg="pink")
lbx.pack(anchor="ne",padx=25,pady=25)
root.mainloop()