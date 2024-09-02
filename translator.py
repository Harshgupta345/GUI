from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator,LANGUAGES


def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

#def change(text="type",src="English",dest="Hindi"):
    #text1=text
    #src1=src
    #dest1=dest
    #trans =Translator()
    #trans1=trans.translate(text,src=src1,dest=dest1)
    #return trans1.text


def translate_text():
    source_text = text12.get("1.0",END)
    src_lang = combo1.get()
    dest_lang = combo2.get()

    translator = Translator()
    translation = translator.translate(source_text, src=src_lang, dest=dest_lang)

    text1.delete("1.0", END)
    text12.insert(END, translation.text)


root=Tk()

root.title("translator")
root.geometry("1080x630")
root.config(bg="black")


language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=30)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=80)


f1=Frame(root,bg="light blue",bd=5)
f1.place(x=10,y=150,width=440,height=210)


text12=Text(f1,font="Robote 20 bold",bg="white",relief=GROOVE,wrap=WORD)
text12.place(x=0,y=0,width=430,height=200)

s1=Scrollbar(f1)
s1.pack(side="right",fill="y")

s1.configure(command=text12.yview)
text12.configure(yscrollcommand=s1.set)


combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=30)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="SELECT LANGUAGE",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=80)

f2=Frame(root,bg="light blue",bd=5)
f2.place(x=630,y=150,width=440,height=210)

text1=Text(f2,font="Robote 20 bold",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

s2=Scrollbar(f2)
s2.pack(side="right",fill="y")

s2.configure(command=text1.yview)
text1.configure(yscrollcommand=s2.set)


t=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground="purple",cursor="hand2",bd=5,bg="red",fg="white",command=translate_text)

t.place(x=450,y=400)
label_change()


root.mainloop()