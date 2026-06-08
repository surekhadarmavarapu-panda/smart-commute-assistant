import json
import urllib.request
import urllib.error
from config import GEMINI_API_KEY

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

def call_gemini(messages, tools=None):

    payload = {
        "contents": messages
    }

    if tools:
        payload["tools"] = [
            {
                "functionDeclarations": tools
            }
        ]

    request = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-goog-api-key": GEMINI_API_KEY,
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        return {
            "error": f"Gemini API failed with status {e.code}"
        }