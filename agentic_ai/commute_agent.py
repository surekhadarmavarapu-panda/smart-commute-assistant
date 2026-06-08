
import json
from agentic_ai.gemini_client import call_gemini
from agentic_ai.commute_prompt import build_commute_prompt
from tools import (
    get_user_details,
    get_calendar_events,
    get_traffic_status,
    get_weather
)

class SmartCommuteAgent:

    def __init__(self):
        pass

    def select_tools(self, question):

        return [
            "get_calendar_events",
            "get_traffic_status",
            "get_weather"
        ]

    def run(
            self,
            question,
            user_id,
            source=None,
            destination=None
    ):

        print("\nPlanning...")
        user = get_user_details(
            user_id
        )
        if not user:
            raise ValueError(
                f"User '{user_id}' not found."
            )

        if not source:
            source = user.get("source")

        if not destination:
            destination = user.get("destination")

        tools = self.select_tools(
            question
        )

        events = []
        traffic = {}
        weather = {}

        if "get_calendar_events" in tools:

            print(
                "Calling Calendar Tool..."
            )

            events = get_calendar_events(
                user_id
            )

        if "get_traffic_status" in tools:

            print(
                "Calling Traffic Tool..."
            )

            traffic = get_traffic_status(
                source,
                destination
            )
        if "get_weather" in tools:

            print(
                "Calling Weather Tool..."
            )

            weather = get_weather(
                user["location"]
            )

        tool_results = {
            "user": user,
            "source": source,
            "destination": destination,
            "calendar": events,
            "traffic": traffic,
            "weather": weather
        }

        print("\nTool Results:")

        print(
            json.dumps(
                tool_results,
                indent=2
            )
        )

        print(
            "\nGenerating Recommendation..."
        )
        prompt = build_commute_prompt(
            question,
            user,
            events,
            traffic,
            weather
        )

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = call_gemini(payload)
        if "error" in response:
            return response["error"]

        print("\nGemini Response:")
        print(json.dumps(response, indent=2))

        return response["candidates"][0]["content"]["parts"][0]["text"]
