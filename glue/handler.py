import json
import os

def hello(event, context):

    body = {

        "message": "AYOOOOOOOO",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
