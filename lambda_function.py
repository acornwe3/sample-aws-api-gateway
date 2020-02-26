import json

print('Loading function')



def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    data = {
    "isBase64Encoded": "false",
    "statusCode": 200,
    "headers": { "headerName": "headerValue"},
    "body": "hi"
    }
    return data
