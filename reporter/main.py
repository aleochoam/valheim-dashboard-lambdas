import json, boto3

def handler(event, context):
    client = boto3.client('ec2', region_name='us-east-2')
    response = client.describe_instances(
        InstanceIds=[
            os.getenv('INSTANCE_ID'),
        ]
    )

    instance = response.get('Reservations')[0]['Instances'][0]
    public_ip = instance['PublicIpAddress']
    state = instance['State']['Name']

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {
            "content-type": "application/json"
        },
        "body" : json.dumps({
            "public_ip": public_ip,
            "state": state
        })
    }
