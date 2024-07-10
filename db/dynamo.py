import boto3

dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table('userbase')