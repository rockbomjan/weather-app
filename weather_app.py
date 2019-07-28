import tkinter as tk
import requests
from tkinter import font
from PIL import Image, ImageTk
HEIGHT = 500
WIDTH = 600
def weather_report(entry1):
    print("Button Clicked", entry1)

def format_response(weather):
    try:
        name = weather['name']
        weather_cond = weather['weather'][0]['description']
        temp = weather['main']['temp']
        # final_str = str(name) + ' '+ str(weather_cond)+ ' ' + str(temp)
        final_str = 'City: %s \nConditions: %s \nTemperature(C):%s'%(name, weather_cond, temp)
    except:
        final_str = 'Problem in retrieving information.'
    return final_str


def get_weather(city):
    weather_key = '1612aabcc11637d219bcb44540678669'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params = params)
    weather = response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    lbl1['text'] = format_response(weather)

root = tk.Tk()
root.title("Weather Information")
cnvs1 = tk.Canvas(root, height = HEIGHT, width = WIDTH )
cnvs1.pack()
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# img1 = Image.open('Nepal.jpg')
background_image = tk.PhotoImage(file = 'damak1.png')# './' for current directory
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)
frm1 = tk.Frame(root, bg = '#80c1ff', bd = 5)
frm1.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n' )

entry1 = tk.Entry(frm1, font = 40)
entry1.place(relwidth = 0.65, relheight = 1)
entry1.focus()

btn1 = tk.Button(frm1, text = 'Weather Report', font = 40, command = lambda:get_weather(entry1.get()))
btn1.place(relx = 0.7, relwidth = 0.3, relheight = 1)

frm2 = tk.Frame(root, bg = '#80c1ff', bd = 5)
frm2.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

lbl1 = tk.Label(frm2, font = ('Garamod',20), anchor = 'nw', justify = 'left')
lbl1.place(relwidth = 1, relheight = 1)
root.mainloop()