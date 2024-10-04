import json
import os
# from glue.ssm_parameters import create_ssm_parameters

def hello(event, context):
    
    environment_variables = os.environ.items()

    body = {

        "message": f"{environment_variables}",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}

# def ssm_cron(event, context):
#     return create_ssm_parameters()