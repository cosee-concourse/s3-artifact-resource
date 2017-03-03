#! /usr/bin/env python3

from concourse_common.jsonutil import *
from concourse_common.matcher import *

import schemas
from model import *
from s3client import S3Client


def execute():
    valid, payload = load_and_validate_payload(schemas, Request.CHECK)

    if not valid:
        return -1

    s3client = S3Client(get_source_value(payload, ACCESS_KEY),
                        get_source_value(payload, SECRET_KEY),
                        get_source_value(payload, REGION_NAME))

    if not s3client.does_bucket_exist(get_source_value(payload, BUCKET)):
        return -1

    files = s3client.list_files(get_source_value(payload, BUCKET))

    version = get_version(payload, VERSION_KEY_NAME)

    if version is None or version is "":
        versions = []
    else:
        regexp = '{}(.*).tar.gz'.format(get_source_value(payload, FILE_NAME))
        versions = match_versions(regexp, files, get_version(payload, VERSION_KEY_NAME))

    print(versions_as_list(versions, VERSION_KEY_NAME))

    return 0

if __name__ == '__main__':
    exit(execute())
