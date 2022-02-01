import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser_delete_profile')

#create iam client
iam = boto3.client('iam')

#Take input from screen
username = input('Please enter a name:\n')


def delete_iamuser_profile(username):
	try:
		reponse = iam.delete_login_profile(UserName=username)
		logger.info('Deleted login profile for %s.', username)
	except ClientError:
		logger.exception("Couldn't delete login profile for %s.", username)
	else:
		return reponse



def main():
	response = delete_iamuser_profile(username)
	print(response)

if __name__ == '__main__':
	main()
