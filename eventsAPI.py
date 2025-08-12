import requests
from config import EVENTSAPIKEYS

def get_events(city):
    url =f"https://www.eventbriteapi.com/v3/events/search/?q=tech&location.address={city}"
    headers = {"Authorization": f"Bearer {EVENTSAPIKEYS}"}

    response = requests.get(url, headers=headers)
    if response.status_code ==200:
        return response.json().get("events", [])
    return[]
