from agentic_ai.commute_agent import (
    SmartCommuteAgent
)
import pytest

def test_invalid_user():

    agent = SmartCommuteAgent()

    with pytest.raises(ValueError):
        agent.run(
            question="When should I leave?",
            user_id="invalid_user"
        )


def test_select_tools():

    agent = SmartCommuteAgent()

    tools = agent.select_tools(
        "When should I leave?"
    )

    assert (
        "get_calendar_events"
        in tools
    )

    assert (
        "get_traffic_status"
        in tools
    )

    assert (
        "get_weather"
        in tools
    )