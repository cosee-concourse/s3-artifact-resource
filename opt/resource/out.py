#! /usr/bin/env python3
import os
import sys

from concourse_common.jsonutil import *
from model import *
from s3client import S3Client
from concourse_common.archiveutil import *
from concourse_common.ioutil import *
from concourse_common.common import *
import schemas


def execute(sources_directory):
    valid, payload = load_and_validate_payload(schemas, Request.CHECK)
    if not valid:
        return -1

    s3client = S3Client(get_source_value(payload, ACCESS_KEY),
                        get_source_value(payload, SECRET_KEY),
                        get_source_value(payload, REGION_NAME))

    if not s3client.does_bucket_exist(get_source_value(payload, BUCKET)):
        return -1

    version_file_path = join_paths(sources_directory,  get_params_value(payload, VERSION_FILE))
    artifacts_folder_path = os.path.join(sources_directory, get_params_value(payload, FOLDER_PATH))

    version = read_file(version_file_path)
    archive_filename = get_source_value(payload, FILE_NAME) + version + '.tar.gz'

    compress_folder(archive_filename, artifacts_folder_path)

    archive_file_path = join_paths(artifacts_folder_path, archive_filename)

    s3client.upload_file(get_source_value(payload, BUCKET), archive_filename, archive_file_path)

    os.remove(archive_file_path)

    print(get_version_output(archive_filename, VERSION_KEY_NAME))

    return 0


if __name__ == '__main__':
    if not check_system_argument_number():
        exit(-1)
    exit(execute(sys.argv[1]))
