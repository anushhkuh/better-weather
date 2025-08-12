#utility API handlers
import requests
from config import OPENWEATHER

def get_weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER}&units=metric"
    response = requests.get(url)
    if response.status_code==200: #successful call
        return response.json()
    return None
