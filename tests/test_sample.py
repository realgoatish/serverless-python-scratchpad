import json
from glue.handler import hello

def func(x):
    return x + 1


def test_answer():
    message = hello("test event", "test context")["body"]

    parsed_message = json.loads(message)

    print(parsed_message)

    assert parsed_message["message"] == "here's your SSM parameter: THIS IS THE TEST API KEY"