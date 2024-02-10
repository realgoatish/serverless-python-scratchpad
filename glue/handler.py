import json
import os

def hello(event, context):
    # mailchimp_key = os.getenv("MAILCHIMP_KEY")
    # body = {
    #     "message": f"here's your SSM parameter: {mailchimp_key}",
    #     "input": event,
    # }

    body = {
<<<<<<< HEAD:handler.py
        "message": "AYOOOOOOOO",
=======
        "message": "YESH!",
>>>>>>> a35b15a378e1990bb7e5438e911619a8d880a35c:glue/handler.py
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
