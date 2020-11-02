import boto3
import base64
import os
import json
sts=boto3.client('secretsmanager')

def rdsSecret(rdssec):
    secretname=rdssec
    get_secret_value_response = sts.get_secret_value(
        SecretId=secretname
    )
    if 'SecretString' in get_secret_value_response:
        secret = json.loads(get_secret_value_response['SecretString'])
        return f"""postgresql://{secret['username']}:{secret['password']}@{secret['host']}:{secret['port']}/{secret['db']}"""
    else:
        decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

def redisSecret(redissec):
    secretname = redissec
    get_secret_value_response = sts.get_secret_value(
        SecretId=secretname
    )
    secret = json.loads(get_secret_value_response['SecretString'])
    return f"""redis://{secret['rediscluster']}:6379"""



if __name__=="__main__":
    print(rdsSecret())
    print(redisSecret())
