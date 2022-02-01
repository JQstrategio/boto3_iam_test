import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser')

#Create iam client
iam = boto3.client('iam')

username = input('Please enter a name:\n')

def create_user(username):
	try:
		#Take input from screen
		response = iam.create_user(UserName=username)
		logger.info('Created a user %s.', username)
	except ClientError:
		logger.exception("Couldn't create a user %s.", username)
	else:
		return response

response = create_user(username)