import json
from agentic_ai.gemini_client import call_gemini
from tools import get_user_details
from agentic_ai.tools_registry import TOOL_MAP, TOOLS_SCHEMA

class SmartCommuteAgent:

    def __init__(self, userid, source, destination):
        self.user_id = userid
        self.user = get_user_details(self.user_id)

        if not self.user:
            raise ValueError(f"User '{self.user_id}' not found.")

        self.source = source or self.user.get("source")
        self.destination = destination or self.user.get("destination")

        self.messages = []
        self._add_message(
            "system",
            f"""You are a smart commute assistant.Your task is to help users plan their commute by providing personalized recommendations based on their calendar, traffic conditions, and weather.
                    User info: {json.dumps(self.user)}
                    User Id: {self.user_id}
                    Source: {self.source}
                    Destination: {self.destination}

                    Only summarize when user explicitly asks about conversation history.
                    Otherwise answer normally and use tools when required.
                """
            )

    def _add_message(self, role, text):
        self.messages.append({
            "role": role,
            "parts": [{"text": text}]
        })

    def run(self, question):
        self._add_message("user", question)

        for _ in range(5):
            response = call_gemini(self.messages, tools=TOOLS_SCHEMA)

            if "error" in response:
                return response["error"]

            parts = response["candidates"][0]["content"]["parts"]
            final_text = ""
            tool_called = 0

            for part in parts:

                if "functionCall" in part:
                    tool_called = 1

                    tool_name = part["functionCall"]["name"]
                    args = part["functionCall"]["args"]

                    tool_func = TOOL_MAP.get(tool_name)

                    if not tool_func:
                        self._add_message("model", f"Unknown tool: {tool_name}")
                        continue

                    result = tool_func(**args)

                    self._add_message(
                        "model",
                        f"The tool `{tool_name}` returned {json.dumps(result)}"
                    )

                    self._add_message("user", "continue with the task")

                else:
                    final_text += part["text"]

            if not tool_called:
                self._add_message("model", final_text)
                return final_text

        return "Sorry, I couldn't come up with a response in time."