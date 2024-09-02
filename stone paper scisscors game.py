from tkinter import *
# from PIL import Image,ImageTk
import random
import tkinter.messagebox as tsmg

root=Tk()
root.title("Snake Game Python")
root.geometry("500x700")
root.config(bg="black")

rock=0
paper=1
scissors=2
s=0
score=0

def click(event):
    global scvalue
    global screen
    global s
    global score
    comp = random.randint(0,2)
    text=event.widget.cget("text")
    if comp==0:
       scvalue2.set("Rock")
       screen2.update()
    elif comp==1:
       scvalue2.set("Paper")
       screen2.update()
    elif comp==2:
       scvalue2.set("Scissors")
       screen2.update()
   
    if text=="Rock":
       scvalue5.set("Rock")
       screen5.update()
       
    elif text=="Paper":
       scvalue5.set("Paper")
       screen5.update()
       
    elif text=="Scissors":
       scvalue5.set("Scissors")
       screen5.update()



    if text=="Rock":
        if comp==0:
           scvalue3.set(f"Comp:{s}")
           screen3.update()
           scvalue4.set(f"User:{score}")
           screen4.update()
           scvalue.set("its tie")
           screen.update()
        elif comp==1:
            s=s+1
            scvalue3.set(f"Comp:{s}")
            screen3.update()
            scvalue.set("Computer wins")
            screen.update()
        elif comp==2:
           score=score+1
           scvalue4.set(f"User:{score}")
           screen4.update()
           scvalue.set("Player wins")
           screen.update()
    elif text=="Paper":
        if comp==0:
           score=score+1
           scvalue4.set(f"User:{score}")
           screen4.update()
           scvalue.set("Player wins")
           screen.update()
        elif comp==1:
            scvalue3.set(f"Comp:{s}")
            screen3.update()
            scvalue4.set(f"User:{score}")
            screen4.update()
            scvalue.set("Its tie")
            screen.update()
        elif comp==2:
           s=s+1
           scvalue3.set(f"Comp:{s}")
           screen3.update()
           scvalue.set("computer wins")
           screen.update()
    elif text=="Scissors":
        if comp==0:
           s=s+1
           scvalue3.set(f"Comp:{s}")
           screen3.update()
           scvalue.set("Computer wins")
           screen.update() 
        elif comp==1:
            score=score+1
            scvalue4.set(f"User:{score}")
            screen4.update()
            scvalue.set("Player wins")
            screen.update()
        elif comp==2:
           scvalue3.set(f"Comp:{s}")
           screen3.update()
           scvalue4.set(f"User:{score}")
           screen4.update()
           scvalue.set("Its tie")
           screen.update()
    elif text=="Exit":
       tsmg.showinfo("Game over",f"Thanks for playing game\nPlayerScore:{score}\nComputerScore:{s}")
       root.quit()
       
    else:
        pass
    if score==5:
       tsmg.showinfo("Game over",f"Player wins\nPlayerScore:{score}\nComputerScore:{s}")
       root.quit()
    
    elif s==5:
       tsmg.showinfo("Game over",f"Computer wins\nPlayerScore:{score}\nComputerScore:{s}")
       root.quit()
       


wif=600
wih=200

# image=Image.open("hju.jpg")
# resize=image.resize((wif,wih))
# photo=ImageTk.PhotoImage(resize)

# varun=Label(image= photo,padx=6,pady=6)
# varun.pack(side=TOP,anchor="nw",padx=10,pady=10)




r=Label(root,text="Computer:        User:",bg="black",fg="light blue",width=20,font="Arial 20 bold",anchor="center")
r.pack(anchor="nw")


f=Frame(root,bg="black")

scvalue2=StringVar()
scvalue2.set("")
screen2=Entry(f,textvar=scvalue2,font="lucida 25 bold",width=10)
screen2.pack(side=LEFT,pady=10,padx=10)

scvalue5=StringVar()
scvalue5.set("")
screen5=Entry(f,textvar=scvalue5,font="lucida 25 bold",width=9)
screen5.pack(side=LEFT,pady=10,padx=10)

f.pack()

r=Label(root,text="Scores:",bg="black",fg="light blue",anchor="center",width=10,font="Arial 20 bold")
r.pack(anchor="nw")

f=Frame(root,bg="black")

scvalue3=StringVar()
scvalue3.set("")
screen3=Entry(f,textvar=scvalue3,font="lucida 20 bold",width=8)
screen3.pack(side=LEFT,pady=10,padx=10)

r=Label(f,text="Vs",bg="black",fg="light blue",width=3,font="Arial 20 bold",anchor="center")
r.pack(side=LEFT)


scvalue4=StringVar()
scvalue4.set("")
screen4=Entry(f,textvar=scvalue4,font="lucida 20 bold",width=8)
screen4.pack(side=LEFT,pady=10,padx=10)

scvalue3.set("comp:0")
screen3.update()
scvalue4.set("user:0")
screen4.update()

f.pack()

r=Label(root,text="Result:",bg="black",fg="light blue",anchor="center",width=10,font="Arial 20 bold")
r.pack(anchor="nw")

scvalue=StringVar()
scvalue.set("press the button")
screen=Entry(root,textvar=scvalue,font="lucida 25 bold")
screen.pack(pady=10,padx=10)


def check(comp, user):
  if comp ==user:
    return 0

  if(comp == 0 and user ==1):
    return -1

  if(comp == 1 and user ==2):
    return -1

  if(comp == 2 and user == 0):
    return -1

  return 1



wif2=106
wih2=100

f=Frame(root,bg="black")

# image2=Image.open("rock.jpg")
# resize2=image2.resize((wif2,wih2))
# photo2=ImageTk.PhotoImage(resize2)
# varun2=Label(f,image= photo2,padx=1,pady=1)
# varun2.pack(side=LEFT,padx=5,pady=1)


# image3=Image.open("paper.jpg")
# resize3=image3.resize((wif2,wih2))
# photo3=ImageTk.PhotoImage(resize3)
# varun3=Label(f,image= photo3,padx=1,pady=1)
# varun3.pack(side=LEFT,padx=5,pady=1)


# image4=Image.open("scissors.jpg")
# resize4=image4.resize((wif2,wih2))
# photo4=ImageTk.PhotoImage(resize4)
# varun4=Label(f,image= photo4,padx=1,pady=1)
# varun4.pack(side=LEFT,padx=5,pady=1)

# image5=Image.open("IMG-20240615-WA0028.jpg")
# resize5=image5.resize((wif2,wih2))
# photo5=ImageTk.PhotoImage(resize5)
# varun5=Label(f,image= photo5,padx=1,pady=1)
# varun5.pack(side=LEFT,padx=5,pady=1)


f.pack(side=BOTTOM)


f=Frame(root,bg="black")

b=Button(f,text="Rock",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="Paper",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="Scissors",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="Exit",padx=32,pady=15,font="lucida 12 bold",bg="light blue")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",click)


f.pack(side=BOTTOM,padx=5,pady=10)


root.mainloop()