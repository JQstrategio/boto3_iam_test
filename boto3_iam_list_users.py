import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamusers_list')

#create iam client
iam = boto3.client('iam')

#creating starts instance function
def list_iamusers():
	try:
		response = iam.list_users()
		paginator = iam.get_paginator('list_users')
		for response in paginator.paginate():
			for user in response['Users']:
				print(f"Username: {user['UserName']}")
		logger.info("listing iam users %s")
	except ClientError:
		logger.exception("couldn't list iam users %s.")
		raise
	else:
		return response

resposne = list_iamusers()
