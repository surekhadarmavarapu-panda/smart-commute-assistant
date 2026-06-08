from tools import (
    get_user_details,
    get_calendar_events,
    get_traffic_status,
    get_weather
)


def test_get_user_details():

    user = get_user_details("user1")

    assert user["name"] == "Surekha"
    assert user["location"] == "Hyderabad"


def test_invalid_user():

    user = get_user_details(
        "invalid_user"
    )

    assert user == {}


def test_get_calendar_events():

    events = get_calendar_events(
        "user1"
    )

    assert len(events) > 0
    assert events[0]["title"] == "Client Demo"


def test_get_traffic_status():

    traffic = get_traffic_status(
        "Whitefield",
        "kormangla"
    )

    assert traffic["traffic"] == "Moderate"


def test_invalid_route():

    traffic = get_traffic_status(
        "Unknown",
        "Unknown"
    )

    assert traffic == {}


def test_get_weather():

    weather = get_weather(
        "Hyderabad"
    )

    assert weather["condition"] == "Rain"


def test_invalid_location():

    weather = get_weather(
        "Unknown"
    )

    assert weather == {}