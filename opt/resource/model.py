from concourse_common import common

VERSION_JSON_NAME = 'version'


class Model:

    def __init__(self):
        self.payload = common.get_payload()

        if 'source' not in self.payload:
            common.log('Invalid JSON. Source should be part of request JSON')
            raise TypeError

    def get_bucket(self):
        bucket_name = self.payload['source']['bucket']
        return bucket_name

    def get_access_key(self):
        access_key = self.payload['source']['access_key_id']
        return access_key

    def get_secret(self):
        secret_key = self.payload['source']['secret_access_key']
        return secret_key

    def get_region_name(self):
        region_name = self.payload['source']['region_name']
        return region_name

    def get_filename(self):
        file = self.payload['source']['filename']
        return file

    def get_version_file(self):
        version = self.payload['params']['version']
        return version

    def get_folderpath(self):
        folderpath = self.payload['params']['folderpath']
        return folderpath

    def get_version(self):
        try:
            version = self.payload['version'][VERSION_JSON_NAME]
        except TypeError:
            version = None
        return version
