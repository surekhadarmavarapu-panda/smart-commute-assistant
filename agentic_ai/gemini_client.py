import json
import urllib.request
import urllib.error

from config import GEMINI_API_KEY

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

def call_gemini(payload):

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
            return json.loads(
                response.read().decode("utf-8")
            )


    except urllib.error.HTTPError as e:

        print("HTTP Status:", e.code)

        try:

            error_body = e.read().decode()

            print(error_body)

        except:

            pass

        if e.code == 429:
            return {

                "error": (

                    "Gemini API quota exceeded. "

                    "Please try again after a minute."

                )

            }

        return {

            "error": f"Gemini API failed with status {e.code}"

        }