from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city +  "&appid=fa71156ad750a7986eb6865dd8635596").json()
    W_label1.config(text=data["weather"][0]["main"])
    Wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather Forecasting")
win.config(bg= "blue")
win.geometry("500x570")

name_label = Label(win,text="Weather Forecasting App",font= ("Time New Roman",20,"bold"))
name_label.place(x=25 , y=50 , height=50 , width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather Forecasting App",values = list_name,font= ("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=25 , y=120 , height=50 , width=450)

W_label = Label(win,text="Weather climate",font= ("Time New Roman",15))
W_label.place(x=25 , y=260 , height=50 , width=200)
W_label1 = Label(win,text=" ",font= ("Time New Roman",15))
W_label1.place(x=250 , y=260 , height=50 , width=200)

Wb_label = Label(win,text="Weather description",font= ("Time New Roman",15))
Wb_label.place(x=25 , y=330 , height=50 , width=200)
Wb_label1 = Label(win,text=" ",font= ("Time New Roman",15))
Wb_label1.place(x=250 , y=330 , height=50 , width=200)


temp_label = Label(win,text="Temperature",font= ("Time New Roman",15))
temp_label.place(x=25 , y=400 , height=50 , width=200)
temp_label1 = Label(win,text=" ",font= ("Time New Roman",15))
temp_label1.place(x=250 , y=400 , height=50 , width=200)

pre_label = Label(win,text="Pressure",font= ("Time New Roman",15))
pre_label.place(x=25 , y=470 , height=50 , width=200)
pre_label1 = Label(win,text=" ",font= ("Time New Roman",15))
pre_label1.place(x=250 , y=470 , height=50 , width=200)

done_button = Button(win,text="Done",font= ("Time New Roman",15,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()