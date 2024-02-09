import json


def hello(event, context):
    body = {
        "message": "YESH!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
