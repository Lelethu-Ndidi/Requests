from tkinter import *
from tkinter import messagebox
import requests

def weather() :
    api_key = "422f2a8448fe972fdcc3eef2"
    # url variable to store url
    url = "http://api.openweathermap.org/data/2.5/weather?"
    # take a city name from city_field entry box
    city_name = city_entry.get()
    # main_url variable to store complete url address
    main_url = url + "appid =" + api_key+ "&q =" + city_name
    # get method of requests module return response object
    responses = requests.get(main_url)
    # json method of response object convert json format data into python format data
    json_data = responses.json()
    # check the value of "cod" key is equal to "404" or not if not that means city is found otherwise city is not found
    if json_data["cod"] != "404" :
        # store the value corresponding to the "temp" key
        current_temperature = ((json_data['main']['temperature'])-273.15)
        # store the value corresponding to the "pressure" key
        current_pressure = json_data['main']["pressure"]
        # store the value corresponding to the "humidity"
        current_humidiy = json_data['main']["humidity"]
        # store the value corresponding to the "description" key
        weather_description = json_data['weather'][0]["description"]
        # Inserting in the entry box
        temp_entry.insert(15, str(current_temperature) + " degree celsius")
        pressure_entry.insert(10, str(current_pressure) + " hPa")
        humidity_entry.insert(15, str(current_humidiy) + " %")
        description_entry.insert(10, str(weather_description) )
    # if city is not found
    else :
        # Displaying an error message
        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name")

        # clear the content of city_field entry box
        city_entry.delete(0, END)


# Function for clearing the
# contents of all text entry boxes
def clear_all() :
    city_entry.delete(0, END)
    temp_entry.delete(0, END)
    pressure_entry.delete(0, END)
    humidity_entry.delete(0, END)
    description_entry.delete(0, END)



# Create a GUI window
tkWindow = Tk()
tkWindow.title("Weather App")
tkWindow.configure(background = "light grey")

tkWindow.geometry("500x250")

mainlabel = Label(tkWindow, text = "Weather Gui Application")
city_lbl = Label(tkWindow, text = "City name : ")
temp_lbl = Label(tkWindow, text = "Temperature :")
pressure_lbl = Label(tkWindow, text = "pressure :")
humidity_lbl = Label(tkWindow, text = "humidity :")
description_lbl = Label(tkWindow, text = "description  :")

# PLacing the labels
mainlabel.grid(row = 0, column = 1)
city_lbl.grid(row = 1, column = 0, sticky ="E")
temp_lbl.grid(row = 3, column = 0, sticky ="E")
pressure_lbl.grid(row = 4, column = 0, sticky ="E")
humidity_lbl.grid(row = 5, column = 0, sticky ="E")
description_lbl.grid(row = 6, column = 0, sticky ="E")


# Creating text entry boxes
city_entry = Entry(tkWindow)
temp_entry = Entry(tkWindow)
pressure_entry = Entry(tkWindow)
humidity_entry = Entry(tkWindow)
description_entry = Entry(tkWindow)

# placing my entries
city_entry.grid(row = 1, column = 1, ipadx ="100")
temp_entry.grid(row = 3, column = 1, ipadx ="100")
pressure_entry.grid(row = 4, column = 1, ipadx ="100")
humidity_entry.grid(row = 5, column = 1, ipadx ="100")
description_entry.grid(row = 6, column = 1, ipadx ="100")

# Creating a Submit Button and attached
display_button = Button(tkWindow, text = "Display",command = weather)

# Creating a submit button
clear_button = Button(tkWindow, text = "Clear", command = clear_all)

# placing the buttons
display_button.grid(row = 2, column = 1)
clear_button.grid(row = 7, column = 1)

tkWindow.mainloop()

