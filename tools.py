import json
import os

DATA_DIR = "mock_data"

def load_json(filename):
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def get_user_details(user_id):
    users = load_json("users.json")
    return users.get(user_id, {})

def get_calendar_events(user_id):
    calendar = load_json("calendar.json")
    return calendar.get(user_id, [])

def get_traffic_status(
        source,
        destination
):

    traffic = load_json(
        "traffic.json"
    )

    route = (
        f"{source}-{destination}"
    )

    return traffic.get(
        route,{}
    )

def get_weather(location):
    weather = load_json("weather.json")
    return weather.get(location, {})
