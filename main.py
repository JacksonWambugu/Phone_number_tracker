from tkinter import *
from unittest import result
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x584")
root.resizable(False,False)
def track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)
    
    #country
    locate=geocoder.description_for_number(number,"en")
    country.config(text=locate)
    
    
    
    
    #operator airtel etc
    operator=carrier.name_for_number(number,"en")
    sim.config(text=operator)
    
    #phone timezone
    time = timezone.time_zones_for_number(number)
    zone.config(text=time)
    
    
    #longitude latitude
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(locate)
    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)
    
    
    
    #time showing in phone
    
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    phonetime.config(text=current_time)
    
    


    



#logo
logo=PhotoImage(file="logo image.png")
Label(root,image=logo).place(x=240,y=70)
heading= Label(root,text="TRACK NUMBER",font=("arial",15,"bold"))
heading.place(x=90,y=110)


#entry
Entry_back=PhotoImage(file="search png.png")
Label(root,image=Entry_back).place(x=20,y=190)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,bd=0,font=("arial ",20)).place(x=50,y=220)


#button

searchimage=PhotoImage(file="search.png")
search=Button(image=searchimage,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=35,y=300)

#bottom
Box=PhotoImage(file="bottom png.png")
Label(root,image=Box).place(x=-2,y=355)
country=Label(root,text="COUNTRY :: ",bg="#57adff",fg="black",font=("arial",9,"bold"))
country.place(x=50,y=400)
sim=Label(root,text="SIM :: ",bg="#57adff",fg="black",font=("arial",9,"bold"))
sim.place(x=200,y=400)
zone=Label(root,text="TIMEZONE :: ",bg="#57adff",fg="black",font=("arial",9,"bold"))
zone.place(x=50,y=450)
phonetime=Label(root,text="PHONE TIME :: ",bg="#57adff",fg="black",font=("arial",9,"bold"))
phonetime.place(x=200,y=450)
longitude=Label(root,text="LONGITUDE :: ",bg="#57adff",fg="black",font=("arial",9,"bold"))
longitude.place(x=50,y=500)
latitude=Label(root,text="LATITUDE :: ",bg="#57adff",fg="black",font=("arial",9,"bold"))
latitude.place(x=200,y=500)






root.mainloop()



