import boto3
from typing import Union, List
from pprint import pprint
import os

ec2 = boto3.client('ec2')
sns=boto3.client('sns')
snsarn=os.environ['sns']

def describeState(id) -> List[dict]:
    ec2_exec = ec2.describe_instances(
        InstanceIds=[id]
    )
    return ec2_exec


def getTags(ec2data) -> Union[List[dict], None]:
    for data in ec2data['Reservations'][0]['Instances']:
        tags = data.get('Tags', None)
        if tags is None:
            return None
        else:
            return tags


def terminate(id) -> None:
    ec2.terminate_instances(
        InstanceIds=[
            id
        ]
    )

def sendSns(message):
    sns.publish(
        TopicArn=snsarn,
        Subject="Ec2 Instance Status",
        Message=message
    )

def validateTags(tags, id) -> str:
    if tags is None:
        terminate(id)
        return f'Ec2 instance -{id} got terminated for no tags'
    else:
        for data in tags:
            application = data.get('Key', None)
            value=data.get('Value',None)
            print(application)
            print(value)
            if application is None:
                print('Terminating instance as it doesnt have application tags')
                terminate(id)
                return f'Ec2 instance -{id} got terminated for no application key tag'
            elif application is not None:
                if value.lower() not in ['aws', 'neo']:
                    print('Terminating instance as it doesnt have value tags mapped correctly')
                    terminate(id)
                    return f'Ec2 instance -{id} got terminated due to wrong user tags -{value}'
                else:
                    print("valid Instance so not terminating it")
                    return f'Ec2 instance -{id} got success for tags -{value}'


def lambda_handler(event, context) -> None:
    print('started here')
    id = event['detail']['instance-id']
    state=event['detail']['state']
    if state in ['pending','running']:
        data = describeState(id)
        print(data)
        tags = getTags(data)
        print(tags)
        message=validateTags(tags,id)
        print(message)
        sendSns(message)
        print('Closed here')
    else:
        print(f'Ec2 phase is not meant to be checked {id}')



