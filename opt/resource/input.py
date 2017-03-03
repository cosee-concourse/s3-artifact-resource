#! /usr/bin/env python3
import os

from concourse_common.common import *
from concourse_common.jsonutil import *
from concourse_common.archiveutil import *
import schemas
from model import *
from s3client import S3Client


def execute(destination):
    valid, payload = load_and_validate_payload(schemas, Request.CHECK)
    if not valid:
        return -1

    s3client = S3Client(get_source_value(payload, ACCESS_KEY),
                        get_source_value(payload, SECRET_KEY),
                        get_source_value(payload, REGION_NAME))

    if not s3client.does_bucket_exist(get_source_value(payload, BUCKET)):
        return -1

    archive_filename = join_paths(destination, get_version(payload, VERSION_KEY_NAME))
    s3client.download_file(get_source_value(payload, BUCKET),
                           get_version(payload,VERSION_KEY_NAME),
                           archive_filename)

    uncompress_file(archive_filename, destination)
    os.remove(archive_filename)

    print(get_version_output(get_version(payload, VERSION_KEY_NAME),VERSION_KEY_NAME))

    return 0


if __name__ == '__main__':
    if not check_system_argument_number():
        exit(-1)
    exit(execute(sys.argv[1]))
