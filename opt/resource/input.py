#! /usr/bin/env python3
import sys
import os

from model import Model
from s3client import S3Client
import json_output
import archive_util
from concourse_common import common


def execute(destination):
    try:
        model = Model()
    except TypeError:
        return -1

    s3client = S3Client(model.get_access_key(), model.get_secret(), model.get_region_name())

    if not s3client.does_bucket_exist(model.get_bucket()):
        return -1

    if model.get_version() is (None or ""):
        common.log("No Version", file=sys.stderr)
        return -1

    filename = destination + model.get_version()
    s3client.download_file(model.get_bucket(), model.get_version(), filename)

    archive_util.uncompress_file(filename,destination)
    os.remove(filename)

    print(json_output.inout_output(model.get_version()))

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))
