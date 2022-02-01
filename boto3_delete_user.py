import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser_delete')

#create iam client
iam = boto3.client('iam')

#Take input from screen
username = input('Please enter a name:\n')

def delete_iamuser_accesskey(username):
	try:
		key = iam.list_access_keys(UserName=username)
		for data in key['AccessKeyMetadata']:
			accessKeyId = data['AccessKeyId']
			response = iam.delete_access_key(UserName=username, AccessKeyId=accessKeyId)
			logger.info("Deleted access key %s for user %s", accessKeyId, username)
	except ClientError:
		logger.exception("Couldn't delete access keys for %s.", username)
		raise
	else:
		return response

def delete_iamuser_profile(username):
	try:
		reponse = iam.delete_login_profile(UserName=username)
		logger.info('Deleted login profile for %s.', username)
	except ClientError:
		logger.exception("Couldn't delete login profile for %s.", username)
	else:
		return reponse

def delete_user(username):
	try:
		response = iam.delete_user(UserName=username)
		logger.info('Deleted user %s.', username)
	except ClientError:
		logger.exception("Couldn't delete user %s.", username)
	else:
		return response

def main():
	# print(delete_iamuser_accesskey(username))
	print(delete_iamuser_profile(username))
	print(delete_user(username))

if __name__ == '__main__':
	main()





