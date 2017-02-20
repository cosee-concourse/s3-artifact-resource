#! /usr/bin/env python3
import os
import sys

from concourse import common
from model import Model, Request
from util import archive_util, json_output
from util.s3client import S3Client
from colorama import init


def execute(destination):
    try:
        model = Model(Request.IN)
    except TypeError:
        return -1

    s3client = S3Client(model.get_access_key(), model.get_secret(), model.get_region_name())

    if not s3client.does_bucket_exist(model.get_bucket()):
        return -1

    archive_filename = os.path.join(destination,model.get_version())
    s3client.download_file(model.get_bucket(), model.get_version(), archive_filename)

    archive_util.uncompress_file(archive_filename, destination)
    os.remove(archive_filename)

    print(json_output.inout_output(model.get_version()))

    return 0

if __name__ == '__main__':
    init(autoreset=True)
    if len(sys.argv) != 2:
        common.log_error("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))
