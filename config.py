import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER=os.getenv("OPENWEATHER_API_KEY")
NEWSAPIKEYS=os.getenv("NEW_API_KEY")
EVENTSAPIKEYS=os.getenv("EVENTBRITE_API_KEY")

