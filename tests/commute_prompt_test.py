from agentic_ai.commute_prompt import (
    build_commute_prompt
)


def test_prompt_contains_question():

    prompt = build_commute_prompt(
        question="When should I leave?",
        user={},
        events=[],
        traffic={},
        weather={}
    )

    assert "When should I leave?" in prompt


def test_prompt_contains_user():

    prompt = build_commute_prompt(
        question="test",
        user={"name": "Surekha"},
        events=[],
        traffic={},
        weather={}
    )

    assert "Surekha" in prompt


def test_prompt_contains_calendar():

    prompt = build_commute_prompt(
        question="test",
        user={},
        events=[{
            "title": "Client Demo"
        }],
        traffic={},
        weather={}
    )

    assert "Client Demo" in prompt