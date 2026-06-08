import json
import urllib.error
from unittest.mock import Mock, patch

from agentic_ai.gemini_client import call_gemini

@patch("urllib.request.urlopen")
def test_call_gemini_success(mock_urlopen):

    mock_response = Mock()
    mock_response.read.return_value = json.dumps({
        "candidates": [{
            "content": {
                "parts": [{
                    "text": "Leave at 9:15 AM"
                }]
            }
        }]
    }).encode("utf-8")

    mock_urlopen.return_value.__enter__.return_value = mock_response

    result = call_gemini(
        messages=[
            {
                "role": "user",
                "parts": [{"text": "When should I leave?"}]
            }
        ]
    )

    assert "candidates" in result
    assert result["candidates"][0]["content"]["parts"][0]["text"] == "Leave at 9:15 AM"


@patch("urllib.request.urlopen")
def test_call_gemini_http_error(mock_urlopen):

    mock_urlopen.side_effect = urllib.error.HTTPError(
        url="http://test.com",
        code=500,
        msg="Internal Server Error",
        hdrs=None,
        fp=None
    )

    result = call_gemini(
        messages=[
            {
                "role": "user",
                "parts": [{"text": "When should I leave?"}]
            }
        ]
    )

    assert "error" in result
    assert "500" in result["error"]


@patch("urllib.request.urlopen")
def test_call_gemini_with_tools(mock_urlopen):

    mock_response = Mock()
    mock_response.read.return_value = json.dumps({
        "candidates": [{
            "content": {
                "parts": [{
                    "text": "Tool call successful"
                }]
            }
        }]
    }).encode("utf-8")

    mock_urlopen.return_value.__enter__.return_value = mock_response

    tools = [
        {
            "name": "get_weather",
            "description": "Get weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                }
            }
        }
    ]

    result = call_gemini(
        messages=[
            {
                "role": "user",
                "parts": [{"text": "What's the weather?"}]
            }
        ],
        tools=tools
    )

    assert "candidates" in result