from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
import os
import pyttsx3
from tkinter import colorchooser
root=Tk()
root.title("Snake Game Python")
root.geometry("1800x1000")
root.config(bg="black")


def start_draw(event):
    global last_x,last_y
    last_x,last_y=event.x,event.y



def draw(event):
    global last_x,last_y,current
    te=text.get()
    canvas.create_line((last_x,last_y,event.x,event.y),fill=current,width=te)
    last_x,last_y=event.x,event.y


def set(new):
    global current
    current=new


def choose():
    global current
    color=colorchooser.askcolor(title="choose color")
    if color:
        current=color[1]



def clear():
    canvas.delete("all")

def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    canvas.delete("all")

def save():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("All files", ".")])
        if file_path:
            save_canvas_to_file(file_path)

def save_canvas_to_file( file_path):
    ps = canvas.postscript(colormode='color')
        
        # Convert postscript to image and save
        
    img = Image.open(file_path)
    img.save(file_path)
    

def quitapp():
    pass
    
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label="New",command=newfile)

filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitapp)

menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)


r=Label(root,text="Drawing tool",bg="black",fg="light blue",anchor="center",width=10,font="Arial 27 bold")
r.pack()

canvas=Canvas(root,bg="white",width=1500,height=620)
canvas.pack(padx=10,pady=10)

color_frame=Frame(root,bg="black")
color_frame.pack(padx=10)


f=Frame(bg="black")


r=Label(f,text="Enter Width",bg="black",fg="light blue",anchor="center",width=10,font="Arial 15 bold")
r.pack(side=LEFT)

scvalue=IntVar()
scvalue.set("")

text=Entry(f,justify="left",width=5,font="poppins 25 bold",bg="#404040",border=0,fg="white" ,text=scvalue)
text.pack(side=LEFT)


search=Button(f,borderwidth=0,text="Go",cursor="hand2",bg="cyan",width=5,height=2)
search.pack(side=LEFT)
search.bind("<Button-1>",draw)

f.pack()


colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "brown", "pink"]
for color in colors:
    color_button = Button(color_frame, bg=color, width=2, height=1, command=lambda c=color:set(c))
    color_button.pack(side=LEFT, padx=2, pady=2)


fa=Frame()

color_chooser_button = Button(f, text="Choose Color", command=choose)
color_chooser_button.pack(side=LEFT,padx=19,pady=20)

current= "black"
    


canvas.bind("<Button-1>",start_draw)
canvas.bind("<B1-Motion>",draw)

clear_button=Button(f,text="Clear",command=clear)
clear_button.pack(side=LEFT,padx=19,pady=20)

f.pack()

engine=pyttsx3.init()
engine.say("hey whats up")
engine.say("i am drawing tool") 
engine.say("do you want to draw something")
engine.runAndWait()

root.mainloop()