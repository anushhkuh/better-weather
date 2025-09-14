import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()

OPENWEATHER=os.getenv("OPENWEATHER_API_KEY")
NEWSAPIKEYS=os.getenv("NEW_API_KEY")
EVENTSAPIKEYS=os.getenv("TICKETMASTER_API_KEY")

@app.route("/", methods=["GET", "POST"])

def home():

    city = request.form.get("city", "san francisco")

    weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"q":city, "appid":OPENWEATHER, "units":"metric"}).json() #store in a JSON file whatever you are getting though the API key, specified city - site to get info from and units Farenheit

    #factors we need Temperature, feelsilike, humidity, wind etc
    weather = {
        "Description":weather_response["weather"][0]["description"].title(),
        "Temp": round(weather_response["main"]["temp"]),
        "feels_like": round(weather_response["main"]["feels_like"]),
        "humidity": weather_response["main"]["humidity"],
        "wind_speed": weather_response["wind"]["speed"]
    }


    forecast_response= requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params={"q":city ,"appid":OPENWEATHER, "units":"metric"}
    ).json()


    forecast =[]

    for idx in [0,8,16,24,32]:
        item= forecast_response["list"][idx]
        forecast.append({
            "day": item["dt_txt"].split(" ")[0],
            "icon": item["weather"][0]["main"].lower(),
            "temp": round(item["main"]["temp"])
        })
   

    news_response = requests.get("https://newsapi.org/v2/top-headlines", params={"country":"us","apiKey":NEWSAPIKEYS, "pageSize":5}).json()

    news = []
    for articles in news_response["articles"]:
        news.append(articles.get('title'))
    
   
    event_json = requests.get("https://app.ticketmaster.com/discovery/v2/events.json", params={"apikey":EVENTSAPIKEYS, "city":city, "size":1 }).json()['_embedded']["events"]

    weather_html = f"<h1>weather for {city}</h1> <p>news :{news}</p> <p>weather: {weather}</p><p>events:"

    for event in event_json:
        name = event["name"]
        url = event["url"]
        weather_html += f" {name} and {url} " 
    
    return render_template("index2.html")
