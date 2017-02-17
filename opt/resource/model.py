from concourse import common
from enum import Enum
import schemas

VERSION_JSON_NAME = 'version'


class Model:

    def __init__(self, request):
        self.payload = common.load_payload()

        if request == Request.CHECK:
            schema = schemas.checkSchema
        else:
            schema = schemas.inoutSchema

        common.validate_payload(self.payload, schema)

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


class Request(Enum):
    CHECK = 1
    IN = 2
    OUT = 3