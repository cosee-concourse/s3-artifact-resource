#! /usr/bin/env python3
import sys
import os
import io

from model import Model
from s3client import S3Client
from concourse_common import common
import json_output
import archive_util


def execute(sources_directory):
    try:
        model = Model()
    except:
        return -1

    s3client = S3Client(model.get_access_key(), model.get_secret(), model.get_region_name())

    if not s3client.does_bucket_exist(model.get_bucket()):
        common.log("Bucket does not exist")
        return -1

    if model.get_version_file() is (None or ""):
        common.log("No Version", file=sys.stderr)
        return -1

    if model.get_filename() is (None or ""):
        common.log("No Filename", file=sys.stderr)
        return -1

    common.log("Reading version...")

    version = io.open(os.path.join(sources_directory,model.get_version_file()), "r").read()

    common.log("Current Version: " + version)

    filename = model.get_filename() + version + '.tar.gz'

    common.log("Filename: " + filename)

    folderpath = os.path.join(sources_directory, model.get_folderpath())

    archive_util.compress_folder(filename, folderpath)

    filepath = os.path.join(folderpath,filename)

    common.log("Uploading file to s3")

    s3client.upload_file(model.get_bucket(), filename, filepath)

    common.log("Successfully uploaded file")

    os.remove(filepath)

    print(json_output.inout_output(filename))

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))

