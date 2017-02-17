#! /usr/bin/env python3
import io
import os
import sys

import schemas
from concourse import common
from model import Model, Request
from util import archive_util, json_output
from util.s3client import S3Client


def execute(sources_directory):
    try:
        model = Model(Request.OUT)
    except:
        return -1

    s3client = S3Client(model.get_access_key(), model.get_secret(), model.get_region_name())

    if not s3client.does_bucket_exist(model.get_bucket()):
        common.log("Bucket does not exist")
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

