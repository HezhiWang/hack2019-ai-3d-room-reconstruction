import boto3
import logging
from botocore.exceptions import ClientError


BUCKET_NAME = "ai-3d-room-reconstruction"
TARGET_EXTENSION = ".obj"



class S3Downloader:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def poll_bucket(self):
        """
        Check if s3 bucket has an ODM file. If so, download it and return it.
        Note: if there are multiple ODM files, this will only return the first one found.
        :return:
        """
        objects = self.s3_client.list_objects_v2(Bucket=BUCKET_NAME)['Contents']
        for object in objects:
            file_name = object['Key']
            if ".obj" in file_name:
                return self.download(file_name)
        return None


    def download(self, file_name):
        try:
            response = self.s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        except ClientError as e:
            logging.error(e)
            return None
        file = response['Body'].read()
        return file
