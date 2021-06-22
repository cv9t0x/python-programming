import requests, json


api_id = "7f379581bcfb1fd5d2bc8a52a8244231"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Введите название города : ")
lang = "ru"
complete_url = base_url + "appid=" + api_id + "&units=metric" + "&lang=" + lang + "&q=" + city_name

response = requests.get(complete_url)
data = response.json()

if data["cod"] != "404":
    current_temperature = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    current_wind = data["wind"]["speed"]
    current_pressure = data["main"]["pressure"]
    current_humidiy = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print("Температура в цельсиях: " + str(current_temperature) + " °C" +
            "\nОщущается как: " + str(feels_like) + " °C" + 
            "\nВетер: " + str(current_wind) + " м/c" +
            "\nАтмосферное давление: " + str(current_pressure) +
            "\nВлажность: " + str(current_humidiy) + "%"
            "\nПогода: " + str(weather_description))
else:
    print("Город не был найден")