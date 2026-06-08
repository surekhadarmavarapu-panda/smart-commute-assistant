from unittest.mock import patch

from agentic_ai.commute_agent import (
    SmartCommuteAgent
)
import pytest

@patch(
    "agentic_ai.commute_agent.call_gemini"
)
def test_gemini_response(
        mock_gemini
):

    mock_gemini.return_value = {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text":
                            "Recommendation: Leave at 9:15 AM"
                        }
                    ]
                }
            }
        ]
    }

    agent = SmartCommuteAgent()

    result = agent.run(
        question="When should I leave for work?",
        user_id="user1"
    )

    assert "Recommendation" in result


@patch(
    "agentic_ai.commute_agent.call_gemini"
)
def test_gemini_quota_exceeded(
        mock_gemini
):

    mock_gemini.return_value = {
        "error":
        "Gemini API quota exceeded. Please try again after a minute."
    }

    agent = SmartCommuteAgent()

    result = agent.run(
        question="When should I leave for work?",
        user_id="user1"
    )

    assert (
        "quota exceeded"
        in result.lower()
    )


@patch(
    "agentic_ai.commute_agent.call_gemini"
)
def test_gemini_api_failure(
        mock_gemini
):

    mock_gemini.return_value = {
        "error":
        "Gemini API failed with status 500"
    }

    agent = SmartCommuteAgent()

    result = agent.run(
        question="When should I leave for work?",
        user_id="user1"
    )

    assert (
        "failed"
        in result.lower()
    )

def test_invalid_user():

    agent = SmartCommuteAgent()

    with pytest.raises(ValueError):
        agent.run(
            question="When should I leave?",
            user_id="invalid_user"
        )