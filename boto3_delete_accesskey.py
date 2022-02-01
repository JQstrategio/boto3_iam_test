import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser_delete_accesskey')

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

def main():
	response = delete_iamuser_accesskey(username)
	print(response)

if __name__ == '__main__':
	main()
