import os
from flask import Flask, render_template, request
import requests



app = Flask(__name__)

WEATHER_KEY    = os.getenv("OPENWEATHER_API_KEY")
NEWS_KEY       = os.getenv("NEWS_API_KEY")
EVENTBRITE_KEY = os.getenv("EVENTBRITE_API_KEY")

@app.route("/", methods=
           ["GET", "POST"])

def home():
    city = request.form.get("city", "san fransisco")

    weather_response = request.get("https://api.openweathermap.org/data/2.5/weather", params={"q":city, "appid":WEATHER_KEY, "units":"imperial"}).json() #store in a JSON file whatever you are getting though the API key, specified city - site to get info from and units Farenheit

    #factors we need Temperature, feelsilike, humidity, wind etc
    weather = {
        "Description":weather_response["weather"][0]["Description"].title(),
        "Temp": round(weather_response["temp"]),
        "feels_like": round(weather_response["feels like"]),
        "humidity": weather_response["humidity"],
        "wind_speed": weather_response["wind"]["speed"]
    }


    forecast_response= request.get(
    "https://api.openweathermap.org/data/2.5/forecast", params={"q":city ,"appid":WEATHER_KEY, "unit":"imperial"}
    ).json()

    forecast =[]

    for idx in [0,8,16,24,32]:
        item= forecast_response["list"][idx]
        forecast.append({
            "day": item["dttext"].split(" ")[0],
            "icon": item["weather"][0]["main"].lower(),
            "temp": round(item["main"]["temp"])
        })