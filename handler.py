import json
import boto3
import base64


def hello(event, context):
    body = json.loads(event['body'])

    client = boto3.client('polly')
    response = client.synthesize_speech(
        Text=body['text'],
        OutputFormat="mp3",
        VoiceId=body['voice']
    )

    result = {
        'voice': str(base64.b64encode(response['AudioStream'].read()))[2:-1]
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": {
            "Access-Control-Allow-Origin" : "*"
        }
    }
