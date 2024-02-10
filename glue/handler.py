import json
import os

def hello(event, context):
    # mailchimp_key = os.getenv("MAILCHIMP_KEY")
    # body = {
    #     "message": f"here's your SSM parameter: {mailchimp_key}",
    #     "input": event,
    # }

    body = {

        "message": "AYOOOOOOOO",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
