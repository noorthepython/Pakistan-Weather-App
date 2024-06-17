from tkinter import *
from tkinter import Label
from tkinter import ttk

import requests



def get_data():
    city = city_name.get()
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=763e0ebfa0646631cdf942808cb6a78f').json()
    weather_climate1.config(text = data['weather'][0]['main'])
    weather_description1.config(text = data['weather'][0]['description'])
    weather_temp1.config(text = str(round(data['main']['temp']-273)))
    
    weather_mintemp1.config(text = str(round(data['main']['temp_min']-273)))
    weather_maxtemp1.config(text = str(round(data['main']['temp_max']-273)))
    weather_pressure1.config(text = data['main']['pressure'])


win = Tk()
win.title("Noorify Weather")

win.geometry("500x500")
        




name_label = ttk.Label(win, text = "Noorify Weather", font = ("Times New Roman", 30, "bold"))
name_label.place(x=500/5, y=30, height=50, width=300)
win.resizable(False, False)
list = ['Azad Kashmir',
'Balochistan',
'Gilgit-Baltistan',
'Islamabad',
'Punjab',
'Sindh']
city_name = StringVar()
com = ttk.Combobox(win,values=list,font=50,textvariable=city_name)
com.place(x=25,y=80,height=50,width=450)

weather_details =ttk.Label(win, text = "Weather Details", font = ("Times New Roman", 20, "bold"))
weather_details.place(x=140, y=205, height=40, width=200)


weather_climate =ttk.Label(win, text = "Weather Climate:", font = ("Times New Roman", 15, "bold"))
weather_climate.place(x=25, y=250, height=30, width=300)

weather_climate1 =ttk.Label(win, text = "", font = ("Times New Roman", 15, "bold"))
weather_climate1.place(x=250, y=250, height=30, width=220)

weather_description =ttk.Label(win, text = "Weather Description:", font = ("Times New Roman", 15, "bold"))
weather_description.place(x=25, y=280, height=30, width=300)

weather_description1 =ttk.Label(win, text = "", font = ("Times New Roman", 15, "bold"))
weather_description1.place(x=250, y=280, height=30, width=220)

weather_temp =ttk.Label(win, text = "Temperature:", font = ("Times New Roman", 15, "bold"))
weather_temp.place(x=25, y=310, height=30, width=300)

weather_temp1 =ttk.Label(win, text = "", font = ("Times New Roman", 15, "bold"))
weather_temp1.place(x=250, y=310, height=30, width=220)

weather_mintemp =ttk.Label(win, text = "Minimum Temperature:", font = ("Times New Roman", 15, "bold"))
weather_mintemp.place(x=25, y=340, height=30, width=300)

weather_mintemp1 =ttk.Label(win, text = "", font = ("Times New Roman", 15, "bold"))
weather_mintemp1.place(x=250, y=340, height=30, width=220)

weather_maxtemp =ttk.Label(win, text = "Maximum Temperature:", font = ("Times New Roman", 15, "bold"))
weather_maxtemp.place(x=25, y=370, height=30, width=300)

weather_maxtemp1 =ttk.Label(win, text = "", font = ("Times New Roman", 15, "bold"))
weather_maxtemp1.place(x=250, y=370, height=30, width=220)

weather_pressure =ttk.Label(win, text = "Pressure:", font = ("Times New Roman", 15, "bold"))
weather_pressure.place(x=25, y=400, height=30, width=300)

weather_pressure1 =ttk.Label(win, text = "", font = ("Times New Roman", 15, "bold"))
weather_pressure1.place(x=250, y=400, height=30, width=220)


dedication =ttk.Label(win, text = "Dedicated to my Father, Akhtar Hussain", font = ("Times New Roman", 10))
dedication.place(x=140, y=460, height=30, width=220)

dedication1 =ttk.Label(win, text = "Stanford: Code in Place Final Project")
dedication1.place(x=140, y=5, height=30, width=220)

done_button = ttk.Button(win,text="DONE",command=get_data)
done_button.place(x=190,y=150,height=50,width=100)
# threading.Thread(target=ready_gif).start()
win.mainloop()