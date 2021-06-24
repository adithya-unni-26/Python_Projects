import tkinter as tk
import json
import requests
from tkinter.messagebox import showinfo



def get_weather_data():
    API_KEY="9579f3a132e12e4f4edbcfd1f082d123"
    city = city_entry.get() #used to get the city data entered in the gui
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    res= requests.get(URL) #this sends a GET method to the specified URL
    data=res.json()# to get the json file from the url
    weather=data['weather'][0]['description']
    temperature=data["main"]["temp"]
    humidity =data["main"]["humidity"]
    wind_speed =data["wind"]["speed"]

    showinfo(f"{city.title()}",f'Weather: {weather} \n Temperature:{temperature} \n Humidity: {humidity} \n Wind Speed: {wind_speed}') #to display in a seperate window

root=tk.Tk()
root.title('Weather GUI')

app_label= tk.Label(root, text='Weather GUI', font=('Times',20,'bold'))
app_label.grid(row=0,column=0,columnspan=2)

city_label = tk.Label(root, text='Enter city name: ')
city_label.grid(row=1,column=0,pady=10) #.grid puts it into a two dimensional table

#used to get the city entry
city_entry = tk.Entry(root,width=30)
city_entry.grid(row=1,column=1,pady=10)


button= tk.Button(root, text='Get Weather', bd=1, command=get_weather_data)
button.grid(row=2,column=2,columnspan=2,pady=10)

root.mainloop()