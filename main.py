import argparse
from agentic_ai.commute_agent import SmartCommuteAgent

parser = argparse.ArgumentParser()

parser.add_argument(
    "--userid",
    required=True
)

parser.add_argument(
    "--source"
)

parser.add_argument(
    "--destination"
)

args = parser.parse_args()

agent = SmartCommuteAgent(args.userid,source=args.source,
            destination=args.destination)

print("Smart Commute Assistant")

while True:

    question = input(
        "\nAsk a question (type 'exit' to quit): "
    )

    if question.lower() == "exit":
        print("ThankYou!")
        break

    try:

        answer = agent.run(
            question=question
        )
        print(answer)

    except ValueError as e:

        print(f"\n{e}")
        break