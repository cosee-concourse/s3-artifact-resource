#! /usr/bin/env python3
import os
import sys

from concourse import common
from model import Model, Request
from util import archive_util, json_output, io_util
from util.s3client import S3Client
from colorama import init


def execute(sources_directory):
    try:
        model = Model(Request.OUT)
    except TypeError:
        return -1

    s3client = S3Client(model.get_access_key(), model.get_secret(), model.get_region_name())

    if not s3client.does_bucket_exist(model.get_bucket()):
        return -1

    version_file_path = os.path.join(sources_directory, model.get_version_file())
    artifacts_folder_path = os.path.join(sources_directory, model.get_folderpath())

    version = io_util.read_file(version_file_path)
    archive_filename = model.get_filename() + version + '.tar.gz'

    archive_util.compress_folder(archive_filename, artifacts_folder_path)

    archive_file_path = os.path.join(artifacts_folder_path, archive_filename)

    s3client.upload_file(model.get_bucket(), archive_filename, archive_file_path)

    os.remove(archive_file_path)

    print(json_output.inout_output(archive_filename))

    return 0


if __name__ == '__main__':
    init(autoreset=True)
    if len(sys.argv) != 2:
        common.log_error("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))
