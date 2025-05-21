#!/usr/bin/env python
from flows.flow import RouterFlow

def kickoff():
    flow = RouterFlow()
    flow.kickoff()


def plot():
    flow = RouterFlow()
    flow.plot()


if __name__ == "__main__":
    # Update this conversation to test your use case.
    inputs = [
        {"u": "Hi, I want to book a court."},
    ]
    q = ""
    flow = RouterFlow()

    # while q != "exit":
    #     q = input()
    #     inputs.append({"u": q})
    result = flow.kickoff(inputs={"inputs": inputs})
        # inputs.append({"a": str(result)})
    print("Flow result:",result)
