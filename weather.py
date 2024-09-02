from tkinter import *

from geopy.geocoders import Nominatim


from timezonefinder import TimezoneFinder

from datetime import datetime
import time

import requests
import pytz

def getweather():
    city=text.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    api="https://api.openweathermap.org/data/2.5/weather?"+city+"&appid=03a34212e277e9b4a8bd7b61258e9ab2"
    
    json_data=requests.get(api).json()

    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    t=time.strftime("%I:%M %p")
    clock.config(text=t)
    name.config(text="CURRENT WEATHER:")

    
    lab5.config(text=(temp,"C"))
    lab6.config(text=(condition,"!","FEELS","LIKE",temp,"C"))
    lab7.config(text=wind)
    lab8.config(text=humidity)
    lab0.config(text=pressure)
    lab9.config(text=description)
    


root=Tk()
root.title("Weather App")
root.geometry("900x500")
root.config(bg="black")
root.resizable(False,False)


text=Entry(root,justify="center",width=17,font="poppins 25 bold",bg="#404040",border=0,fg="white" )
text.place(x=50,y=40)


search=Button(borderwidth=0,text="Go",cursor="hand2",bg="cyan",width=5,height=2,command=getweather)
search.place(x=360,y=40)

name=Label(root,font="arial 15 bold",fg="#ee666d",bg="black")
name.place(x=30,y=100)

clock=Label(root,font="arial 15 bold",fg="#ee666d",bg="black")
clock.place(x=30,y=130)

lab=Label(root,text="WIND",font="Helvetica 15 bold",fg="white",bg="black")
lab.place(x=120,y=400)

lab2=Label(root,text="HUMIDITY",font="Helvetica 15 bold",fg="white",bg="black")
lab2.place(x=225,y=400)

lab3=Label(root,text="DESCRIPTION",font="Helvetica 15 bold",fg="white",bg="black")
lab3.place(x=430,y=400)

lab4=Label(root,text="PRESSURE",font="Helvetica 15 bold",fg="white",bg="black")
lab4.place(x=650,y=400)

lab5=Label(root,font="arial 70 bold",fg="#ee666d",bg="black")
lab5.place(x=400,y=150)

lab11=Label(root,font="arial 70 bold",fg="#ee666d",bg="black")
lab11.place(x=550,y=100)

lab6=Label(root,font="arial 15 bold",fg="white",bg="black")
lab6.place(x=400,y=250)


lab7=Label(root,text="...",font="arial 20 bold",fg="white",bg="black")
lab7.place(x=120,y=430)

lab8=Label(root,text="...",font="arial 20 bold",fg="white",bg="black")
lab8.place(x=280,y=430)

lab9=Label(root,text="...",font="arial 20 bold",fg="white",bg="black")
lab9.place(x=450,y=430)

lab0=Label(root,text="...",font="arial 20 bold",fg="white",bg="black")
lab0.place(x=670,y=430)



root.mainloop()