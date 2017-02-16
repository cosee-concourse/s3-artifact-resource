import boto3
import botocore

from concourse_common import common


class S3Client:
    def __init__(self, access_key, secret_key, region_name):
        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )

    def does_bucket_exist(self,bucket_name):
        try:
            if not self.does_bucket_exist_internal(bucket_name):
                common.log("Bucket does not exist")
                return False
        except botocore.exceptions.ClientError:
            common.log("Invalid Credentials!")
            return False
        return True

    def does_bucket_exist_internal(self, bucket_name):
        buckets = self.client.list_buckets()
        for bucketDict in buckets['Buckets']:
            if bucket_name == bucketDict['Name']:
                return True
        return False

    def list_files(self, bucket_name):
        files = []
        objects = self.client.list_objects_v2(
            Bucket = bucket_name
        )
        for content in objects['Contents']:
            files.append(content['Key'])
        return files

    def download_file(self, bucket, key, filepath):
        self.client.download_file(bucket,key,filepath)

    def upload_file(self, bucket, key, filepath):
        self.client.upload_file(filepath, bucket, key)