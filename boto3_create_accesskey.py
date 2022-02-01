import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser')

#Create iam client
iam = boto3.client('iam')

#Take input from screen
username = input("Please enter a name:\n")

def create_iamuser_accesskey(username):
	try:
		repsonse = iam.create_access_key(UserName=username)
		logger.info('Created a user access key %s.', username)
	except ClientError:
		logger.exception("Couldn't create a user access key %s.", username)
	else:
		return repsonse

reponse = create_iamuser_accesskey(username)
print(reponse)