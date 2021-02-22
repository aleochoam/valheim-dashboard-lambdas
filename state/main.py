import json, boto3, os
from botocore.exceptions import ClientError

def handler(event, context):
    client = boto3.client('ec2', region_name='us-east-2')

    body = json.loads(event['body'])
    action = body['state']
    instance_id = os.getenv('INSTANCE_ID')

    try:
        if action == 'on':
            response = client.start_instances(InstanceIds=[instance_id])
        else:
            response = client.stop_instances(InstanceIds=[instance_id])
        print(response)
    except ClientError as e:
        print(e)

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {
            "content-type": "application/json",
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body" : json.dumps({
            'success': True
        })
    }
