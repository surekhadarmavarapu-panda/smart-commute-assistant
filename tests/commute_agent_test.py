import pytest

from agentic_ai.commute_agent import SmartCommuteAgent
from agentic_ai.tools_registry import TOOLS_SCHEMA

def test_invalid_user():
    with pytest.raises(ValueError):
        SmartCommuteAgent(
            userid="invalid_user",
            source=None,
            destination=None
        )

def test_tools_registered():
    tool_names = {tool["name"] for tool in TOOLS_SCHEMA}

    assert "get_user_details" in tool_names
    assert "get_calendar_events" in tool_names
    assert "get_traffic_status" in tool_names
    assert "get_weather" in tool_names

def test_agent_initialization():
    agent = SmartCommuteAgent(
        userid="user1",
        source=None,
        destination=None
    )

    assert agent.user_id == "user1"
    assert agent.user is not None
    assert agent.source is not None
    assert agent.destination is not None
    assert len(agent.messages) > 0

def test_add_message():
    agent = SmartCommuteAgent(
        userid="user1",
        source=None,
        destination=None
    )

    initial_count = len(agent.messages)

    agent._add_message("user", "Hello")

    assert len(agent.messages) == initial_count + 1
    assert agent.messages[-1]["role"] == "user"
    assert agent.messages[-1]["parts"][0]["text"] == "Hello"