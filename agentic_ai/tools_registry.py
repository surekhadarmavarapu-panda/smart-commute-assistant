from tools import (
    get_user_details,
    get_calendar_events,
    get_traffic_status,
    get_weather
)

TOOL_MAP = {
    "get_user_details": get_user_details,
    "get_calendar_events": get_calendar_events,
    "get_traffic_status": get_traffic_status,
    "get_weather": get_weather,
}

TOOLS_SCHEMA = [
    {
        "name": "get_user_details",
        "description": "Get user details by user_id",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string"}
            },
            "required": ["user_id"]
        }
    },
    {
        "name": "get_calendar_events",
        "description": "Get calendar events for a user",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string"}
            },
            "required": ["user_id"]
        }
    },
    {
        "name": "get_traffic_status",
        "description": "Get traffic between source and destination",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {"type": "string"},
                "destination": {"type": "string"}
            },
            "required": ["source", "destination"]
        }
    },
    {
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    }
]