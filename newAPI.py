import requests
from config import NEWSAPIKEYS

def get_news():
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPIKEYS}"
    response= requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", []) #key value pair query
    return []
