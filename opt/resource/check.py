#! /usr/bin/env python3

from model import Model, Request
from util import json_output, matcher
from util.s3client import S3Client
from colorama import init


def execute():
    try:
        model = Model(Request.CHECK)
    except TypeError:
        return -1

    s3client = S3Client(model.get_access_key(), model.get_secret(), model.get_region_name())

    if not s3client.does_bucket_exist(model.get_bucket()):
        return -1

    files = s3client.list_files(model.get_bucket())

    version = model.get_version()
    if version is None or version is "":
        versions = []
    else:
        regexp = '{}(.*).tar.gz'.format(model.get_filename())
        versions = matcher.match_versions(regexp, files, model.get_version())

    print(json_output.check_output(versions))

    return 0

if __name__ == '__main__':
    init(autoreset=True)
    exit(execute())
